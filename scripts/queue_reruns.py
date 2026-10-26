#!/usr/bin/env python3
"""Quarantine several retained cases of one lane and re-run them as a batch.

Used after an audit finds controller faults in retained attempts. Each listed
case directory is moved to `_aborted/<case>-attemptN`, the reason is appended
to `retries.jsonl`, and `run_lane.py` is then started for exactly those cases
with the same harness, endpoint and model. Nothing else in the lane is touched.
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def quarantine(run, case, reason):
    dest = run / case
    aborted = run / '_aborted'
    aborted.mkdir(exist_ok=True)
    attempt = 1
    while (aborted / f'{case}-attempt{attempt}').exists():
        attempt += 1
    preserved = None
    if dest.exists():
        dest.rename(aborted / f'{case}-attempt{attempt}')
        preserved = f'_aborted/{case}-attempt{attempt}'
    with (run / 'retries.jsonl').open('a') as out:
        out.write(json.dumps({'case': case, 'reason': reason, 'preserved': preserved,
                              'time': stamp()}, ensure_ascii=False) + '\n')
    return preserved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-dir', required=True, type=Path)
    ap.add_argument('--case', action='append', required=True)
    ap.add_argument('--reason', required=True)
    ap.add_argument('--endpoint', required=True)
    ap.add_argument('--model', required=True)
    ap.add_argument('--hardware', required=True)
    ap.add_argument('--ssh-host')
    ap.add_argument('--quarantine-only', action='store_true')
    args = ap.parse_args()
    run = args.run_dir.resolve()
    for case in args.case:
        print(json.dumps({'event': 'quarantined', 'case': case,
                          'preserved': quarantine(run, case, args.reason)}), flush=True)
    if args.quarantine_only:
        return
    command = [sys.executable, str(ROOT / 'scripts/run_lane.py'), '--run-dir', str(run),
               '--endpoint', args.endpoint, '--model', args.model, '--hardware', args.hardware]
    if args.ssh_host:
        command += ['--ssh-host', args.ssh_host]
    for case in args.case:
        command += ['--case', case]
    raise SystemExit(subprocess.run(command).returncode)


if __name__ == '__main__':
    main()
