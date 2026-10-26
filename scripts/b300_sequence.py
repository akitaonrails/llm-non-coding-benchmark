#!/usr/bin/env python3
"""Run the B300 lanes back to back without a human in the loop.

Waits for the lane that is already running, exports its pod evidence, swaps the
served model on the pinned pod, re-admits it, then supervises the next lane.
Every step is recorded in `results/b300-sequence.log`; a failure stops the
sequence instead of silently substituting a model or a subset.
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def log(event, **fields):
    line = json.dumps({'time': stamp(), 'event': event, **fields})
    print(line, flush=True)
    with (RESULTS / 'b300-sequence.log').open('a') as out:
        out.write(line + '\n')


def ssh(host, command, timeout=120, check=False):
    proc = subprocess.run(['ssh', '-T', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15',
                           host, command], capture_output=True, text=True, timeout=timeout)
    if check and proc.returncode:
        raise RuntimeError(f'ssh failed ({proc.returncode}): {proc.stderr.strip()[:400]}')
    return proc


def models(host):
    proc = ssh(host, 'curl -s -m 8 -H "Authorization: Bearer local" http://127.0.0.1:18081/v1/models')
    try:
        return [m['id'] for m in json.loads(proc.stdout)['data']]
    except (json.JSONDecodeError, KeyError):
        return []


def gpu_used_mib(host):
    proc = ssh(host, "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits")
    try:
        return int(proc.stdout.strip().splitlines()[0])
    except (ValueError, IndexError):
        return -1


def wait_until(predicate, seconds, step, what):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if predicate():
            return True
        time.sleep(step)
    log('timeout_waiting', what=what, seconds=seconds)
    return False


def export_evidence(host, model_id, run_dir):
    evidence = run_dir / 'pod-evidence'
    evidence.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(['ssh', '-T', '-o', 'BatchMode=yes', host,
                           f'cd /workspace/noncoding-benchmark/{model_id} && tar czf - .'],
                          capture_output=True, timeout=1800)
    if proc.returncode:
        log('evidence_export_failed', model=model_id, stderr=proc.stderr.decode()[:300])
        return
    archive = evidence / f'{model_id}-pod-evidence.tar.gz'
    archive.write_bytes(proc.stdout)
    subprocess.run(['tar', 'xzf', str(archive), '-C', str(evidence)], check=True)
    log('evidence_exported', model=model_id, files=len(list(evidence.rglob('*'))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--host', default='b300-noncoding')
    ap.add_argument('--wait-lane', type=Path, required=True,
                    help='Run directory of the lane that must finish first')
    ap.add_argument('--model', required=True, help='Pod model id to serve next, e.g. glm-5.3-flash')
    ap.add_argument('--run-dir', type=Path, required=True)
    ap.add_argument('--preflight-dir', type=Path, required=True)
    ap.add_argument('--hardware', required=True)
    ap.add_argument('--ready-seconds', type=int, default=3600)
    ap.add_argument('--stop-after', action='store_true', help='Stop the served model when the lane ends')
    args = ap.parse_args()
    wait_lane = args.wait_lane.resolve()
    run_dir = args.run_dir.resolve()
    preflight = args.preflight_dir.resolve()
    previous_model = json.loads((wait_lane / 'manifest.json').read_text())['model']

    log('sequence_start', waiting_for=wait_lane.name, next_model=args.model)
    if not wait_until(lambda: (wait_lane / 'lane-summary.json').exists(), 5 * 86400, 120,
                      f'{wait_lane.name} lane completion'):
        sys.exit('previous lane did not finish')
    log('previous_lane_finished',
        summary=json.loads((wait_lane / 'lane-summary.json').read_text())['completed'])
    export_evidence(args.host, previous_model, wait_lane)

    log('stopping_server', model=previous_model)
    ssh(args.host, "pkill -f 'vllm serve' || true")
    if not wait_until(lambda: gpu_used_mib(args.host) < 5000, 600, 15, 'GPU to drain before swap'):
        sys.exit('GPU did not drain; refusing to launch a second model')

    log('starting_server', model=args.model)
    launch = (f'cd /workspace && setsid nohup /workspace/noncoding-venv/bin/python '
              f'/workspace/b300_prepare.py --config /workspace/b300_single.json --model {args.model} '
              f'>/workspace/{args.model}-serve.out 2>&1 </dev/null &')
    # `setsid nohup ... &` keeps the SSH channel open until the client gives up;
    # a client-side timeout here does not mean the remote launch failed.
    try:
        ssh(args.host, launch, timeout=120)
    except subprocess.TimeoutExpired:
        log('launch_ssh_timeout', model=args.model,
            note='remote process may already be starting; readiness poll decides')
    if not wait_until(lambda: args.model in models(args.host), args.ready_seconds, 30,
                      f'{args.model} readiness'):
        ssh(args.host, f'tail -50 /workspace/noncoding-benchmark/{args.model}/*.log')
        sys.exit(f'{args.model} did not become ready')
    log('server_ready', model=args.model)

    preflight.mkdir(parents=True, exist_ok=False)
    probe = subprocess.run([sys.executable, str(ROOT / 'scripts/run_local_baseline.py'),
                            '--endpoint', 'http://127.0.0.1:18081', '--ssh-host', args.host,
                            '--model', args.model, '--hardware', args.hardware,
                            '--run-dir', str(preflight), '--probe'], text=True)
    if probe.returncode:
        sys.exit('admission probe failed; refusing to run the lane')
    log('admission_passed', model=args.model, preflight=preflight.name)

    lane = subprocess.run([sys.executable, str(ROOT / 'scripts/run_lane.py'),
                           '--run-dir', str(run_dir), '--endpoint', 'http://127.0.0.1:18081',
                           '--ssh-host', args.host, '--model', args.model,
                           '--hardware', args.hardware])
    log('lane_finished', model=args.model, returncode=lane.returncode,
        summary=(json.loads((run_dir / 'lane-summary.json').read_text())
                 if (run_dir / 'lane-summary.json').exists() else None))
    export_evidence(args.host, args.model, run_dir)
    if args.stop_after:
        ssh(args.host, "pkill -f 'vllm serve' || true")
        log('server_stopped', model=args.model, note='pod and billing continue')


if __name__ == '__main__':
    main()
