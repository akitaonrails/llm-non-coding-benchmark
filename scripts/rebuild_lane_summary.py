#!/usr/bin/env python3
"""Rebuild a lane's `lane-summary.json` over the full suite from retained results.

`run_lane.py` writes a summary only for the cases it was given, so a partial
re-run batch overwrites the full-suite summary. This recomputes it from every
case directory, counting preserved attempts under `_aborted/` the same way the
supervisor does. It never changes a result.
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_lane  # noqa: E402

SUITE = Path(__file__).resolve().parents[1] / 'config/suite_full_20261024.json'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-dir', required=True, type=Path)
    args = ap.parse_args()
    run = args.run_dir.resolve()
    cases = json.loads(SUITE.read_text())['cases']
    manifest = json.loads((run / 'manifest.json').read_text())
    statuses = {case: run_lane.case_state(run, case) for case in cases}
    summary = {'rebuilt_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               'model': manifest['model'], 'hardware': manifest['hardware'],
               'cases': {case: {'status': s, 'attempts': a} for case, (s, a) in statuses.items()},
               'retained_results': sum(1 for s, _ in statuses.values() if s != 'absent'),
               'completed': sum(1 for s, _ in statuses.values() if s in run_lane.FINAL_STATUSES)}
    (run / 'lane-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps({k: summary[k] for k in ('rebuilt_at', 'model', 'retained_results', 'completed')}))


if __name__ == '__main__':
    main()
