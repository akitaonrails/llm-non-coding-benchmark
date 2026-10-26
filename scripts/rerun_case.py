#!/usr/bin/env python3
"""Preserve and re-run one case inside an existing lane after a recorded fault.

Used when a controller error or a corrupted attempt makes a case's result
unusable. The old attempt is moved to `_aborted/<case>-attemptN` and noted in
`retries.jsonl`; the case is then re-run with the same harness and server, and
the lane summary is rebuilt so coverage still reflects every case.
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-dir', required=True, type=Path)
    ap.add_argument('--case', required=True)
    ap.add_argument('--reason', required=True)
    ap.add_argument('--endpoint', required=True)
    ap.add_argument('--model', required=True)
    ap.add_argument('--hardware', required=True)
    ap.add_argument('--ssh-host')
    ap.add_argument('--wait-for-summary', action='store_true',
                    help='Wait until the lane finishes before re-running the case')
    ap.add_argument('--wait-seconds', type=int, default=5 * 86400)
    args = ap.parse_args()
    run = args.run_dir.resolve()
    dest = run / args.case
    if args.wait_for_summary:
        deadline = time.monotonic() + args.wait_seconds
        while time.monotonic() < deadline and not (run / 'lane-summary.json').exists():
            time.sleep(60)
        if not (run / 'lane-summary.json').exists():
            sys.exit('lane did not finish in the allotted time; nothing re-run')
        time.sleep(30)  # let the supervising harness exit
    aborted = run / '_aborted'
    aborted.mkdir(exist_ok=True)
    attempt = 1
    while (aborted / f'{args.case}-attempt{attempt}').exists():
        attempt += 1
    if dest.exists():
        dest.rename(aborted / f'{args.case}-attempt{attempt}')
    with (run / 'retries.jsonl').open('a') as out:
        out.write(json.dumps({'case': args.case, 'reason': f'controller-fault re-run: {args.reason}',
                              'preserved': f'_aborted/{args.case}-attempt{attempt}',
                              'time': stamp()}, ensure_ascii=False) + '\n')
    command = [sys.executable, str(ROOT / 'scripts/run_lane.py'), '--run-dir', str(run),
               '--endpoint', args.endpoint, '--model', args.model,
               '--hardware', args.hardware, '--case', args.case]
    if args.ssh_host:
        command += ['--ssh-host', args.ssh_host]
    print(json.dumps({'event': 'rerun_start', 'case': args.case, 'time': stamp()}), flush=True)
    raise SystemExit(subprocess.run(command).returncode)


if __name__ == '__main__':
    main()
