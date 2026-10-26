#!/usr/bin/env python3
"""Controller console for the scripted-client protocol.

The harness blocks on `<stem>.pending.json` until a matching `<stem>.decision.json`
appears (one hour at most). This tool lists what is waiting, shows the exact
question text plus the scripted facts and pushback conditions, and writes the
decision. It never guesses: `--facts` and `--pushbacks` must be given explicitly,
and every decision records who ruled and why.

    python3 scripts/controller.py list
    python3 scripts/controller.py show results/<lane>/<case>/01-client.pending.json
    python3 scripts/controller.py decide results/<lane>/<case>/01-client.pending.json \
        --facts prolabore_abril --reason "Q2 asks the April payment date directly."
"""
import argparse
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'


def pending_files():
    return sorted(p for p in RESULTS.glob('*-full-*/*/*.pending.json')
                  if not p.with_name(p.name.replace('.pending.', '.decision.')).exists())


def kind(path):
    return 'client' if path.name.endswith('-client.pending.json') else 'controller'


def list_pending():
    now = time.time()
    for path in pending_files():
        payload = json.loads(path.read_text())
        lane = path.parts[-3]
        print(f'{path.relative_to(ROOT)}  [{kind(path)}]  case={payload.get("case")} '
              f'age={int((now - path.stat().st_mtime) / 60)}m '
              f'suggestions={payload.get("literal_suggestions", payload.get("pushbacks") and "see --show")}')
        if kind(path) == 'client':
            first = [line for line in payload['questions'].splitlines() if line.strip()][:3]
            print('     ', ' / '.join(first)[:220])
    files = pending_files()
    print(f'\n{len(files)} pending')


def show(path):
    payload = json.loads(path.read_text())
    print(json.dumps({k: v for k, v in payload.items() if k not in {'facts', 'pushbacks'}},
                     indent=2, ensure_ascii=False))
    for fact in payload.get('facts', []):
        print(f'\nFACT {fact["id"]}\n  triggers: {fact.get("trigger")}\n  answer: {fact["answer"]}')
    for i, push in enumerate(payload.get('pushbacks', [])):
        print(f'\nPUSHBACK {i} ({push.get("id", "-")})\n  when: {push.get("when")}\n  message: {push.get("message")}')
    work = path.parent / 'work' / 'workspace' / 'deliverable'
    if work.exists():
        print('\nDELIVERABLES:', ', '.join(sorted(p.name for p in work.rglob('*') if p.is_file())) or '(empty)')


CONTROLLER_ID = 'claude-fable-5.1-session-agent'


def decide(path, facts, reason, pushbacks=None, nudge=None, send_response=None, controller=CONTROLLER_ID):
    path = Path(path)
    if not reason or len(reason) < 15:
        raise SystemExit('A substantive reason is required')
    payload = json.loads(path.read_text())
    if kind(path) == 'client':
        valid = {f['id'] for f in payload['facts']}
        if not set(facts) <= valid:
            raise SystemExit(f'Unknown fact ids: {sorted(set(facts) - valid)}')
        body = {'fact_ids': facts}
        if send_response is not None:
            body['send_response'] = send_response
    else:
        body = {'pushback_indices': pushbacks or [], 'nudge': bool(nudge)}
        if not 0 <= len(pushbacks or []) <= 1 or (nudge and (pushbacks or [])):
            raise SystemExit('At most one scripted pushback and no simultaneous nudge')
    body['reason'] = reason
    body['controller'] = controller
    body['decided_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    target = path.with_name(path.name.replace('.pending.', '.decision.'))
    target.write_text(json.dumps(body, ensure_ascii=False) + '\n')
    shown = target.relative_to(ROOT) if target.is_relative_to(ROOT) else target
    print(f'wrote {shown}: {body}')


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    s = sub.add_parser('show')
    s.add_argument('path')
    w = sub.add_parser('wait', help='Block until a decision is waiting, then list it')
    w.add_argument('--seconds', type=int, default=900)
    d = sub.add_parser('decide')
    d.add_argument('path')
    d.add_argument('--facts', default='', help='Comma-separated scripted fact ids to release')
    d.add_argument('--pushbacks', default='', help='Comma-separated scripted pushback indices')
    d.add_argument('--nudge', action='store_true')
    d.add_argument('--no-response', action='store_true',
                   help='Client round only: archive the questions without sending scripted answers')
    d.add_argument('--reason', required=True)
    d.add_argument('--controller', default=CONTROLLER_ID, help='Identity recorded on the decision')
    args = ap.parse_args()
    if args.command == 'wait':
        deadline = time.monotonic() + args.seconds
        while time.monotonic() < deadline and not pending_files():
            time.sleep(10)
        list_pending()
    elif args.command == 'list':
        list_pending()
    elif args.command == 'show':
        show(Path(args.path))
    else:
        split = lambda text: [x for x in (text or '').replace(' ', '').split(',') if x]
        decide(args.path, split(args.facts), args.reason,
               pushbacks=[int(x) for x in split(args.pushbacks)],
               nudge=args.nudge or None,
               send_response=False if args.no_response else None, controller=args.controller)


if __name__ == '__main__':
    main()
