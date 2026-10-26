#!/usr/bin/env python3
"""Supervise one full-suite lane until every case holds a retained result.

The model harness (`run_local_baseline.py`) is single-process and one case at a
time. This supervisor adds only durability: it restarts the harness after a
crash, quarantines interrupted or transport-failed case directories under
`_aborted/` before a clean retry, and records every restart in `retries.jsonl`.
It never rewrites, reinterprets or fabricates a case result; a case that keeps
failing on infrastructure retains an explicit `infrastructure_failed` result.

Usage (one lane, detached):
    setsid nohup python3 scripts/run_lane.py --run-dir results/<lane> \
        --endpoint http://127.0.0.1:18081 --ssh-host b300-noncoding \
        --model qwen3.8-flash-next --hardware "..." > /dev/null 2>&1 &
"""
import argparse
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'scripts/run_local_baseline.py'
SUITE = ROOT / 'config/suite_full_20261024.json'
# Model outcomes are results, not infrastructure: never retried by the supervisor.
FINAL_STATUSES = {'completed_ungraded', 'candidate_output_limit'}


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def case_state(run_dir, case):
    """Return (status, attempts) for one case directory."""
    dest = run_dir / case
    aborted = run_dir / '_aborted'
    attempts = len(list(aborted.glob(f'{case}-*'))) if aborted.exists() else 0
    result = dest / 'result.json'
    if result.exists():
        try:
            return json.loads(result.read_text())['status'], attempts + 1
        except (json.JSONDecodeError, KeyError):
            return 'unreadable_result', attempts + 1
    if dest.exists():
        return 'interrupted', attempts + 1
    return 'absent', attempts


def quarantine(run_dir, case, why):
    dest = run_dir / case
    aborted = run_dir / '_aborted'
    aborted.mkdir(exist_ok=True)
    attempt = 1
    while (aborted / f'{case}-attempt{attempt}').exists():
        attempt += 1
    dest.rename(aborted / f'{case}-attempt{attempt}')
    with (run_dir / 'retries.jsonl').open('a') as out:
        out.write(json.dumps({'case': case, 'reason': why,
                              'preserved': f'_aborted/{case}-attempt{attempt}',
                              'time': stamp()}) + '\n')
    return attempt


def plan(run_dir, cases, max_attempts):
    """Decide which cases still need a run, quarantining what must be retried."""
    todo = []
    for case in cases:
        status, attempts = case_state(run_dir, case)
        if status == 'completed_ungraded' or status == 'candidate_output_limit':
            continue
        if attempts >= max_attempts:
            continue  # retained explicit failure; reported, not overwritten
        if status in {'interrupted', 'unreadable_result'} and (run_dir / case).exists():
            quarantine(run_dir, case, status)
        elif status == 'infrastructure_failed':
            quarantine(run_dir, case, f'infrastructure_failed retry (attempt {attempts})')
        todo.append(case)
    return todo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-dir', required=True, type=Path)
    ap.add_argument('--endpoint', required=True)
    ap.add_argument('--model', required=True)
    ap.add_argument('--hardware', required=True)
    ap.add_argument('--ssh-host')
    ap.add_argument('--case', action='append')
    ap.add_argument('--turn-timeout', type=int, default=7200)
    ap.add_argument('--max-attempts', type=int, default=3,
                    help='Total attempts per case, including the first')
    ap.add_argument('--stall-seconds', type=int, default=12600,
                    help='Kill and restart the harness after this long without output (default 3.5 h)')
    ap.add_argument('--cooldown', type=int, default=120)
    ap.add_argument('--vram-samples', type=Path,
                    help='Sample GPU free MiB every supervision tick into this JSONL file (desktop lanes)')
    args = ap.parse_args()
    run_dir = args.run_dir.resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    cases = args.case or json.loads(SUITE.read_text())['cases']
    log = run_dir / 'lane.log'

    def emit(event, **fields):
        line = json.dumps({'time': stamp(), 'event': event, **fields})
        print(line, flush=True)
        with log.open('a') as out:
            out.write(line + '\n')

    emit('lane_start', cases=len(cases), model=args.model, ssh_host=args.ssh_host)
    restarts = 0
    while True:
        todo = plan(run_dir, cases, args.max_attempts)
        if not todo:
            break
        command = [sys.executable, str(RUNNER), '--run-dir', str(run_dir), '--resume',
                   '--endpoint', args.endpoint, '--model', args.model,
                   '--hardware', args.hardware, '--turn-timeout', str(args.turn_timeout)]
        if args.ssh_host:
            command += ['--ssh-host', args.ssh_host]
        for case in todo:
            command += ['--case', case]
        emit('harness_start', remaining=len(todo), restarts=restarts,
             first=todo[0], last=todo[-1])
        with log.open('a') as out:
            proc = subprocess.Popen(command, stdout=out, stderr=subprocess.STDOUT,
                                    start_new_session=True)
        last_size, last_change = -1, time.monotonic()
        killed_for_stall = False
        while proc.poll() is None:
            time.sleep(30)
            if args.vram_samples:
                try:
                    free = subprocess.check_output(
                        ['nvidia-smi', '--query-gpu=memory.free', '--format=csv,noheader,nounits'],
                        text=True, timeout=5).strip().splitlines()[0]
                    with args.vram_samples.open('a') as out:
                        out.write(json.dumps({'time': stamp(), 'free_mib': int(free)}) + '\n')
                except (subprocess.SubprocessError, ValueError, IndexError) as exc:
                    emit('vram_sample_failed', error=str(exc)[:200])
            size = log.stat().st_size
            if size != last_size:
                last_size, last_change = size, time.monotonic()
            elif time.monotonic() - last_change > args.stall_seconds:
                emit('stall_kill', quiet_seconds=int(time.monotonic() - last_change))
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    proc.wait(timeout=60)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait()
                killed_for_stall = True
                break
        restarts += 1
        emit('harness_exit', returncode=proc.returncode, stall_kill=killed_for_stall,
             statuses={case: case_state(run_dir, case) for case in todo})
        if not killed_for_stall:
            time.sleep(args.cooldown)
    statuses = {case: case_state(run_dir, case) for case in cases}
    summary = {'finished_at': stamp(), 'model': args.model, 'hardware': args.hardware,
               'cases': {case: {'status': s, 'attempts': a} for case, (s, a) in statuses.items()},
               'retained_results': sum(1 for s, _ in statuses.values() if s != 'absent'),
               'completed': sum(1 for s, _ in statuses.values() if s in FINAL_STATUSES)}
    (run_dir / 'lane-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    emit('lane_end', completed=summary['completed'], of=len(cases))


if __name__ == '__main__':
    main()
