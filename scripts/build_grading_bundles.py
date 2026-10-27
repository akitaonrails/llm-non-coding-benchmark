#!/usr/bin/env python3
"""Build blind grading bundles for the full-suite lanes.

For every suite case, creates `<out>/<case>/runs/<letter>/` for each lane with
the candidate-visible outcome only: the final deliverable snapshot, every
pre-review snapshot, the model's turn responses and prompts, and a sanitized
`status.json`. Lane identity is replaced by a random letter; the mapping is
written to `--mapping` (outside the bundle root) so graders never see it.
Provenance, transcripts, stderr, harness config and controller decision files
are excluded because they name the model or serving stack.
"""
import argparse
import json
import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANES = [
    'sol6-medium-full-20261026',
    'b300-flash-next-full-20261024',
    'b300-glm53-flash-full-20261024',
    'rtx5090-flash-next-full-20261024',
    'strix-flash-next-full-20261024',
]
LETTERS = 'ABCDE'


def sanitize_status(res, turns):
    err = res.get('error') or ''
    limit_turn = err.rsplit('/', 1)[-1] if 'inspect' in err else None
    return {
        'status': res['status'],
        'output_limit_turn': limit_turn,
        'released_facts': res.get('released_facts', []),
        'turns': [{'label': t['label'], 'complete': bool(t.get('complete'))} for t in turns],
    }


def build_run(src, dst):
    dst.mkdir(parents=True)
    final_source = 'final'
    if (src / 'final').exists():
        shutil.copytree(src / 'final', dst / 'final')
    else:
        # Output-limit runs have no review snapshot; the deliverable as it stood
        # when the cap was hit is the last state the candidate produced.
        final_source = 'work-at-limit'
        shutil.copytree(src / 'work' / 'deliverable', dst / 'final')
    for pre in sorted(src.glob('s*-pre-review')):
        shutil.copytree(pre, dst / 'pre-review' / pre.name.replace('-pre-review', ''))
    resp = dst / 'responses'
    resp.mkdir()
    for f in sorted(src.glob('*.response.md')) + sorted(src.glob('*.prompt.txt')):
        shutil.copy(f, resp / f.name)
    res = json.loads((src / 'result.json').read_text())
    turns = json.loads((src / 'turns.json').read_text())
    status = sanitize_status(res, turns)
    status['final_source'] = final_source
    (dst / 'status.json').write_text(json.dumps(status, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--mapping', required=True)
    ap.add_argument('--seed', type=int, default=20261027)
    ap.add_argument('--case', action='append')
    args = ap.parse_args()
    suite = json.loads((ROOT / 'config/suite_full_20261024.json').read_text())
    cases = args.case or suite['cases']
    out = Path(args.out)
    rng = random.Random(args.seed)
    mapping = {}
    for case in cases:
        pack = next((ROOT / 'tasks').glob(f'*/{case}'))
        cdir = out / case
        if cdir.exists():
            shutil.rmtree(cdir)
        letters = list(LETTERS)
        rng.shuffle(letters)
        mapping[case] = {}
        for lane, letter in zip(LANES, letters):
            mapping[case][letter] = lane
            build_run(ROOT / 'results' / lane / case, cdir / 'runs' / letter)
        (cdir / 'PACK.txt').write_text(str(pack.relative_to(ROOT)) + '\n')
    Path(args.mapping).write_text(json.dumps(mapping, indent=2, sort_keys=True))
    print(f'built {len(cases)} cases under {out}; mapping at {args.mapping}')


if __name__ == '__main__':
    main()
