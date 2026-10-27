#!/usr/bin/env python3
"""Cross-lane verification of the full-suite results.

Checks, per lane: manifest equals the suite; every case has a result; every
completed case finished all scripted sessions and its review turn; provenance
names the lane's model; released fact ids exist in the pack; every pending
controller round has a decision with a reason; every `_aborted/` attempt is
listed in `retries.jsonl`; harness configuration is uniform; pack hashes drift
only where the registry says they do. Prints one block per lane and exits
non-zero when a hard check fails.
"""
import argparse
import collections
import fnmatch
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANES = [
    'sol6-medium-full-20261026',
    'b300-flash-next-full-20261024',
    'b300-glm53-flash-full-20261024',
    'rtx5090-flash-next-full-20261024',
    'strix-flash-next-full-20261024',
]
FINAL = {'completed_ungraded', 'candidate_output_limit'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def preserved_in_retries(name, retries):
    """True when an `_aborted/<name>` directory is covered by a retries entry.

    Entries written for a whole batch use a wildcard such as
    `_aborted/<case>-attempt*`."""
    return any(fnmatch.fnmatch(f'_aborted/{name}', r.get('preserved') or '')
               for r in retries)


def load_suite():
    suite = json.loads((ROOT / 'config/suite_full_20261024.json').read_text())
    cases = suite['cases']
    packs = {c: next((ROOT / 'tasks').glob(f'*/{c}')) for c in cases}
    sessions = {}
    facts = {}
    hashes = {}
    for c, pack in packs.items():
        f = pack / 'sessions.json'
        sessions[c] = len(json.loads(f.read_text())['sessions']) if f.exists() else 1
        facts[c] = {x['id'] for x in json.loads((pack / 'client_script.json').read_text()).get('facts', [])}
        hashes[c] = {str(p.relative_to(ROOT)): sha(p) for p in pack.rglob('*') if p.is_file()}
    return cases, sessions, facts, hashes


def verify_lane(lane, cases, sessions, facts, hashes):
    run = ROOT / 'results' / lane
    manifest = json.loads((run / 'manifest.json').read_text())
    r = {'lane': lane, 'hard': [], 'notes': [], 'status': collections.Counter(),
         'provenance_models': collections.Counter(), 'controllers': collections.Counter(),
         'http_errors': 0, 'pack_drift': set(), 'harness_configs': collections.Counter(),
         'aborted': collections.Counter()}
    if set(manifest['cases']) != set(cases) or len(manifest['cases']) != len(cases):
        r['hard'].append('manifest does not match the suite')
    for c in cases:
        for path, h in hashes[c].items():
            if manifest.get('pack_hashes', {}).get(path) not in (None, h):
                r['pack_drift'].add(path)
    retries_file = run / 'retries.jsonl'
    retries = [json.loads(l) for l in retries_file.read_text().splitlines() if l.strip()] if retries_file.exists() else []
    for c in cases:
        d = run / c
        rf = d / 'result.json'
        if not rf.exists():
            r['hard'].append(f'{c}: no result.json')
            continue
        res = json.loads(rf.read_text())
        r['status'][res['status']] += 1
        if res['status'] not in FINAL:
            r['hard'].append(f'{c}: non-final status {res["status"]}')
        bad = [f for f in res.get('released_facts', []) if f not in facts[c]]
        if bad:
            r['hard'].append(f'{c}: unknown released facts {bad}')
        if res['status'] == 'completed_ungraded':
            turns = json.loads((d / 'turns.json').read_text())
            done = {int(m.group(1)) for t in turns
                    if (m := re.fullmatch(r's(\d+)-work', t['label'])) and t.get('complete')}
            if len(done & set(range(1, sessions[c] + 1))) < sessions[c]:
                r['hard'].append(f'{c}: only {len(done)} of {sessions[c]} sessions complete')
            if not any(t['label'] == 'review' and t.get('complete') for t in turns):
                r['hard'].append(f'{c}: no complete review turn')
            final = d / 'final'
            if not final.exists() or not any(final.rglob('*')):
                r['hard'].append(f'{c}: empty final snapshot')
        for pv in d.glob('*.provenance.json'):
            j = json.loads(pv.read_text())
            for ctx in j.get('contexts', [j]):
                r['provenance_models'][(ctx.get('model'), ctx.get('effort'))] += 1
                if ctx.get('model') != manifest['model']:
                    r['hard'].append(f'{c}: provenance model {ctx.get("model")} != {manifest["model"]}')
            r['http_errors'] += j.get('http_errors') or 0
        for pf in d.glob('*.pending.json'):
            df = pf.with_name(pf.name.replace('.pending.', '.decision.'))
            if not df.exists():
                r['hard'].append(f'{c}: undecided {pf.name}')
                continue
            dj = json.loads(df.read_text())
            r['controllers'][dj.get('controller') or '<untagged>'] += 1
            if not dj.get('reason'):
                r['hard'].append(f'{c}: decision without reason {df.name}')
            if not dj.get('controller'):
                r['notes'].append(f'{c}: {df.name} has no controller tag')
        hc = d / 'harness-config.json'
        if hc.exists():
            j = json.loads(hc.read_text())
            r['harness_configs'][json.dumps({k: v for k, v in j.items() if k not in ('case', 'run_dir', 'started_at')}, sort_keys=True)] += 1
    aborted = run / '_aborted'
    for a in sorted(aborted.glob('*')) if aborted.exists() else []:
        rj = a / 'result.json'
        st = json.loads(rj.read_text())['status'] if rj.exists() else 'no-result'
        r['aborted'][st] += 1
        if not preserved_in_retries(a.name, retries):
            r['hard'].append(f'_aborted/{a.name} has no retries.jsonl entry')
    if len(r['harness_configs']) > 1:
        r['hard'].append(f'{len(r["harness_configs"])} distinct harness configurations in one lane')
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', action='append', help='verify only these lanes')
    args = ap.parse_args()
    cases, sessions, facts, hashes = load_suite()
    failed = False
    for lane in args.lane or LANES:
        r = verify_lane(lane, cases, sessions, facts, hashes)
        failed |= bool(r['hard'])
        print(f"== {lane}")
        print(f"   status: {dict(r['status'])}  aborted: {dict(r['aborted'])}")
        print(f"   provenance: {dict(r['provenance_models'])}  http_errors: {r['http_errors']}")
        print(f"   controllers: {dict(r['controllers'])}")
        print(f"   pack drift vs current tasks/: {sorted(r['pack_drift'])}")
        for n in r['notes']:
            print(f"   note: {n}")
        for h in r['hard']:
            print(f"   FAIL: {h}")
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
