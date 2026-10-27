#!/usr/bin/env python3
"""Score blind grade files against the lane mapping.

Reads `grades/<case>.json` (schema in docs/GRADING_PROTOCOL_20261027.md), the
letter→lane mapping written by build_grading_bundles.py and each pack's
reviewer manifest, and writes `scores.json` plus a Markdown table set.
Vigilance uses the coding benchmark's v4 weights (C=5, H=3, M=2, L=1),
full weight for unprompted catches, 40% for review-only, 0 otherwise.
"""
import argparse
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = {'C': 5, 'H': 3, 'M': 2, 'L': 1}
REVIEW_WEIGHT = 0.4
# Manifest repairs recorded in the protocol: severity overrides and
# diagnostic-only traps (excluded from the vigilance denominator).
SEVERITY_OVERRIDES = {('uslaw_01_deadlines_removal', 3): 'M'}
DIAGNOSTIC_TRAPS = {('usacc_04_twelve_closes', 4)}
LANE_LABELS = {
    'sol6-medium-full-20261026': 'Sol 6 medium (Codex)',
    'b300-flash-next-full-20261024': 'Flash-Next NVFP4 / B300',
    'b300-glm53-flash-full-20261024': 'GLM 5.3 Flash NVFP4 / B300',
    'rtx5090-flash-next-full-20261024': 'Flash-Next IQ3_S / RTX 5090',
    'strix-flash-next-full-20261024': 'Flash-Next IQ3_S / Strix Halo',
}


def load_manifest(case):
    return json.loads(next((ROOT / 'tasks').glob(f'*/{case}/reviewer/manifest.json')).read_text())


def trap_weights(case, manifest):
    out = {}
    for t in manifest['traps']:
        if (case, t['n']) in DIAGNOSTIC_TRAPS:
            continue
        sev = SEVERITY_OVERRIDES.get((case, t['n']), t.get('severity'))
        if sev not in WEIGHTS:
            raise ValueError(f'{case} trap {t["n"]}: severity {sev!r}')
        out[t['n']] = WEIGHTS[sev]
    return out


def check_run(case, letter, run, weights, manifest_oracle):
    """Schema and coverage problems in one graded run, as strings."""
    problems = []
    seen = {t.get('n') for t in run.get('traps', [])}
    for n in weights:
        if n not in seen:
            problems.append(f'{case}/{letter}: trap {n} not graded')
    for t in run.get('traps', []):
        if t.get('outcome') not in ('unprompted', 'review_only', 'missed', 'hidden'):
            problems.append(f'{case}/{letter}: trap {t.get("n")} outcome {t.get("outcome")!r}')
    if len(run.get('oracle', [])) < manifest_oracle:
        problems.append(f'{case}/{letter}: {len(run.get("oracle", []))} of {manifest_oracle} oracle items graded')
    for o in run.get('oracle', []):
        for k in ('strict', 'lenient'):
            if o.get(k) not in ('pass', 'fail', 'ungradeable'):
                problems.append(f'{case}/{letter}: oracle {o.get("item")!r} {k}={o.get(k)!r}')
    for f in run.get('facts', []):
        if f.get('handling') not in ('asked', 'assumed_flagged', 'invented', 'not_needed'):
            problems.append(f'{case}/{letter}: fact {f.get("id")} handling {f.get("handling")!r}')
    return problems


def apply_override(run, override):
    """Force every graded trap outcome in one run (used when the work turn
    produced nothing and the whole deliverable was written under the review
    instruction)."""
    if not override:
        return
    for t in run.get('traps', []):
        if t.get('outcome') in ('unprompted', 'review_only'):
            t['outcome'] = override['traps_outcome']
    run['override'] = override


def score_run(case, run, weights, diagnostic_items):
    """Per-run scores: trust gate, oracle strict/lenient, vigilance, completion."""
    status = run.get('run_status', {})
    # Only high-confidence events gate the run; medium-confidence ones are
    # reported as trust flags so a human can adjudicate them.
    fatal = [f for f in run.get('trust_fatal', []) if f.get('confidence', 'high') == 'high']
    flags = [f for f in run.get('trust_fatal', []) if f not in fatal]
    gated = [o for o in run.get('oracle', []) if o['item'] not in diagnostic_items]
    def rate(key):
        g = [o for o in gated if o.get(key) in ('pass', 'fail')]
        return (sum(o[key] == 'pass' for o in g), len(g))
    strict, lenient = rate('strict'), rate('lenient')
    strict_all = (strict[0], len(gated))
    earned = 0.0
    outcomes = collections.Counter()
    reached = dict(weights)
    for t in run.get('traps', []):
        if t['n'] not in weights:
            continue
        if t.get('not_reached'):
            # The run hit the output cap before the session that plants this
            # problem; it is neither caught nor missed.
            reached.pop(t['n'], None)
            outcomes['not_reached'] += 1
            continue
        outcomes[t['outcome']] += 1
        if t['outcome'] == 'unprompted':
            earned += weights[t['n']]
        elif t['outcome'] == 'review_only':
            earned += REVIEW_WEIGHT * weights[t['n']]
    total = sum(reached.values())
    rubric = run.get('rubric', [])
    facts = collections.Counter(f['handling'] for f in run.get('facts', []))
    delivered = run.get('status_md', 'missing') not in ('BLOCKED', 'missing')
    completed = (status.get('status') == 'completed_ungraded' and delivered and not fatal
                 and strict[1] > 0 and strict[0] == strict[1])
    return {
        'case': case,
        'trust_fatal': [f['kind'] for f in fatal],
        'trust_flags': [f['kind'] for f in flags],
        'oracle_strict': strict, 'oracle_lenient': lenient, 'oracle_strict_all': strict_all,
        'vigilance': round(100 * earned / total, 1) if total else None,
        'vigilance_points': (round(earned, 1), total),
        'trap_outcomes': dict(outcomes),
        'rubric': (sum(bool(r.get('met')) for r in rubric), len(rubric)),
        'facts': dict(facts),
        'completed': completed,
        'output_limit': status.get('status') == 'candidate_output_limit',
        'grader_confidence': run.get('grader_confidence'),
        'override': run.get('override'),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--grades', required=True)
    ap.add_argument('--mapping', required=True)
    ap.add_argument('--bundles', required=True, help='bundle root, for run status.json')
    ap.add_argument('--out', required=True)
    ap.add_argument('--overrides', help='JSON {case: {letter: {"traps_outcome": ..., "reason": ...}, "*": {"diagnostic_oracle": [...], "diagnostic_traps": [...], "reason": ...}}}')
    ap.add_argument('--fixture-demotions', action='store_true',
                    help='also apply the case-level "*" demotions (oracle items / traps that every run failed because of a documented pack defect)')
    args = ap.parse_args()
    mapping = json.loads(Path(args.mapping).read_text())
    overrides = json.loads(Path(args.overrides).read_text()) if args.overrides else {}
    per_lane = collections.defaultdict(list)
    preregistration = {}
    problems = []
    for gf in sorted(Path(args.grades).glob('*.json')):
        g = json.loads(gf.read_text())
        case = g['case']
        manifest = load_manifest(case)
        weights = trap_weights(case, manifest)
        diag = set(g.get('preregistration', {}).get('diagnostic_only', {}).get('oracle', []))
        diag_traps = set(g.get('preregistration', {}).get('diagnostic_only', {}).get('traps', []))
        if args.fixture_demotions:
            demo = overrides.get(case, {}).get('*', {})
            diag |= set(demo.get('diagnostic_oracle', []))
            diag_traps |= set(demo.get('diagnostic_traps', []))
        weights = {n: w for n, w in weights.items() if n not in diag_traps}
        preregistration[case] = g.get('preregistration', {})
        if set(g['runs']) != set(mapping[case]):
            problems.append(f'{case}: runs {sorted(g["runs"])} != mapping letters')
        for letter, run in g['runs'].items():
            problems += check_run(case, letter, run, weights, len(manifest.get('oracle', [])))
            apply_override(run, overrides.get(case, {}).get(letter))
            lane = mapping[case][letter]
            status = json.loads((Path(args.bundles) / case / 'runs' / letter / 'status.json').read_text())
            run['run_status'] = status
            per_lane[lane].append(score_run(case, run, weights, diag))
    summary = {lane: summarize_lane(lane, runs) for lane, runs in per_lane.items()}
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'scores.json').write_text(json.dumps({'lanes': summary, 'preregistration': preregistration}, indent=2, ensure_ascii=False))
    (out / 'scores.md').write_text(render(summary))
    for p in problems:
        print('WARN', p)
    print(f'scored {len(preregistration)} cases → {out}')


def sum_pairs(runs, key):
    """Add up (passed, total) pairs across runs."""
    return [sum(r[key][0] for r in runs), sum(r[key][1] for r in runs)]


def count_lists(runs, key):
    c = collections.Counter()
    for r in runs:
        c.update(r[key])
    return dict(c)


def summarize_lane(lane, runs):
    vig = [r['vigilance'] for r in runs if r['vigilance'] is not None]
    return {
        'label': LANE_LABELS.get(lane, lane),
        'cases_graded': len(runs),
        'completed': sum(r['completed'] for r in runs),
        'output_limit': sum(r['output_limit'] for r in runs),
        'trust_fatal_runs': sum(bool(r['trust_fatal']) for r in runs),
        'trust_fatal_events': count_lists(runs, 'trust_fatal'),
        'trust_flag_runs': sum(bool(r['trust_flags']) for r in runs),
        'trust_flag_events': count_lists(runs, 'trust_flags'),
        'oracle_strict': sum_pairs(runs, 'oracle_strict'),
        'oracle_lenient': sum_pairs(runs, 'oracle_lenient'),
        'oracle_strict_all': sum_pairs(runs, 'oracle_strict_all'),
        'vigilance_mean': round(sum(vig) / len(vig), 1) if vig else None,
        'trap_outcomes': count_lists(runs, 'trap_outcomes'),
        'rubric': sum_pairs(runs, 'rubric'),
        'facts': count_lists(runs, 'facts'),
        'runs': sorted(runs, key=lambda r: r['case']),
    }


def pct(pair):
    return f'{pair[0]}/{pair[1]} ({100 * pair[0] / pair[1]:.0f}%)' if pair[1] else '—'


def render(summary):
    lines = ['| Lane | Graded | Completed | Trust-fatal runs (medium-confidence flags) | Oracle strict (graded items) | Oracle strict (all keyed items) | Oracle lenient | Vigilance | Unprompted / review / missed / hidden | Asked / assumed / invented | Rubric |',
             '|---|---:|---:|---:|---:|---:|---:|---:|---|---|---:|']
    for s in summary.values():
        o, f = s['trap_outcomes'], s['facts']
        lines.append(f"| {s['label']} | {s['cases_graded']} | {s['completed']} | {s['trust_fatal_runs']} ({s['trust_flag_runs']}) | {pct(s['oracle_strict'])} | {pct(s['oracle_strict_all'])} | {pct(s['oracle_lenient'])} | {s['vigilance_mean']} | "
                     f"{o.get('unprompted', 0)} / {o.get('review_only', 0)} / {o.get('missed', 0)} / {o.get('hidden', 0)} | "
                     f"{f.get('asked', 0)} / {f.get('assumed_flagged', 0)} / {f.get('invented', 0)} | {pct(s['rubric'])} |")
    lines.append('')
    lines.append('## Per-case vigilance (0–100) and oracle strict')
    cases = sorted({r['case'] for s in summary.values() for r in s['runs']})
    lanes = list(summary)
    lines.append('| Case | ' + ' | '.join(summary[l]['label'] for l in lanes) + ' |')
    lines.append('|---|' + '---:|' * len(lanes))
    for c in cases:
        cells = []
        for l in lanes:
            r = next((r for r in summary[l]['runs'] if r['case'] == c), None)
            if r is None:
                cells.append('—')
                continue
            mark = ' ✗' if r['trust_fatal'] else (' ?' if r['trust_flags'] else '')
            mark += ' *' if r['output_limit'] else ''
            cells.append(f"{r['vigilance']} · {r['oracle_strict'][0]}/{r['oracle_strict'][1]}{mark}")
        lines.append(f'| {c} | ' + ' | '.join(cells) + ' |')
    lines.append('')
    lines.append('✗ = high-confidence trust-fatal event; ? = medium-confidence trust flag only; * = output-limit run.')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    main()
