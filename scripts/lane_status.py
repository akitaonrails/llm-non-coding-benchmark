#!/usr/bin/env python3
"""One-screen status for every full-suite lane, straight from retained files."""
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
LANES = ['b300-flash-next-full-20261024', 'b300-glm53-flash-full-20261024',
         'strix-flash-next-full-20261024', 'rtx5090-flash-next-full-20261024',
         'sol6-medium-full-20261024']


def lane_state(name):
    run = RESULTS / name
    cases = json.loads((ROOT / 'config/suite_full_20261024.json').read_text())['cases']
    done, failed, running, current = {}, {}, [], None
    pending = []
    for case in cases:
        dest = run / case
        result = dest / 'result.json'
        if result.exists():
            body = json.loads(result.read_text())
            (done if body['status'] == 'completed_ungraded' else failed)[case] = body
        elif dest.exists():
            current = case
            turns = sorted(t for t in dest.glob('[0-9]*.jsonl'))
            running.append((case, turns[-1].name if turns else '-'))
        for f in dest.glob('*.pending.json'):
            if not f.with_name(f.name.replace('.pending.', '.decision.')).exists():
                pending.append(f.relative_to(ROOT).as_posix())
    summary = run / 'lane-summary.json'
    return {'run': name, 'present': run.exists(), 'completed': done, 'failed': failed,
            'current': current, 'running': running, 'pending': pending,
            'finished': summary.exists(),
            'summary': json.loads(summary.read_text()) if summary.exists() else None,
            'retries': (run / 'retries.jsonl').read_text().count('\n') if (run / 'retries.jsonl').exists() else 0}


def main():
    for name in LANES:
        state = lane_state(name)
        print(f'\n{name}')
        if not state['present']:
            print('  not started')
            continue
        total = len(state['completed']) + len(state['failed'])
        print(f"  retained results: {total}/38  completed={len(state['completed'])} "
              f"failed={len(state['failed'])} retries={state['retries']} finished={state['finished']}")
        for case in list(state['failed'])[:3]:
            print(f"    FAILED {case}: {state['failed'][case]['status']} "
                  f"{str(state['failed'][case].get('error'))[:100]}")
        if len(state['failed']) > 3:
            print(f"    ... {len(state['failed']) - 3} more retained failures (see result.json files)")
        if state['running'] and not state['finished']:
            for case, turn in state['running']:
                print(f'  in progress: {case} (last turn {turn})')
            last = max((p.stat().st_mtime for p in (RESULTS / name).glob('*/[0-9]*.jsonl')), default=0)
            if last:
                print(f'  last model activity: {int((time.time() - last) / 60)} min ago')
        for path in state['pending']:
            print(f'  PENDING decision: {path}')
        if state['summary']:
            print(f"  lane summary: completed={state['summary']['completed']}/38")
        log = RESULTS / name / 'lane.log'
        if log.exists():
            events = [json.loads(line) for line in log.read_text().splitlines() if line.startswith('{')]
            if events:
                print('  last lane event:', {k: events[-1].get(k) for k in ('time', 'event', 'returncode') if k in events[-1]})


if __name__ == '__main__':
    main()
