#!/usr/bin/env python3
"""Isolated Codex timing pilot. Controller decisions are explicit, logged JSON files.

Only the case workspace is mounted into the candidate namespace. Controller,
answer keys, other runs and future documents are never mounted. Codex's inner
workspace-write sandbox disables network for model shell commands.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import tempfile
import time
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
REVIEW = "Before delivery, review your work for errors, unsupported authority, and anything that does not reconcile. Fix what you find and list what you changed."
NUDGES = ["Review the original request against your current deliverable. Complete any unfinished part and verify it before concluding.", "Run the checks available to you, investigate anything that does not reconcile, and finish the original task. Do not assume the previous attempt completed it."]


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.casefold()) if not unicodedata.combining(c))


def match_facts(question, facts, released):
    q = normalize(question)
    return [f for f in facts if f['id'] not in released and any(normalize(t) in q for t in f['trigger'])]


def wait_reply(request, payload):
    reply = request.with_name(request.name.replace('.pending.', '.decision.'))
    save(request, payload)
    start = time.monotonic()
    while not reply.exists():
        if time.monotonic() - start > 3600:
            raise TimeoutError('Controller did not adjudicate pending interaction')
        time.sleep(1)
    return json.loads(reply.read_text()), time.monotonic()-start


def sandbox(work, state, install):
    cmd = ['bwrap', '--die-with-parent', '--unshare-pid', '--unshare-ipc', '--unshare-uts',
           '--ro-bind', '/usr', '/usr', '--symlink', 'usr/bin', '/bin',
           '--symlink', 'usr/lib', '/lib', '--symlink', 'usr/lib64', '/lib64',
           '--proc', '/proc', '--dev', '/dev', '--tmpfs', '/tmp',
           '--dir', '/home/bench', '--bind', str(state), '/home/bench/.codex',
           '--bind', str(work), '/work', '--ro-bind', str(install), '/opt/codex']
    for p in ['/etc/ssl', '/etc/ca-certificates', '/etc/resolv.conf', '/etc/hosts', '/etc/nsswitch.conf', '/etc/passwd', '/etc/group']:
        if Path(p).exists():
            cmd += ['--ro-bind', p, p]
    return cmd + ['--chdir', '/work', '--clearenv', '--setenv', 'HOME', '/home/bench',
                  '--setenv', 'PATH', '/opt/codex/bin:/usr/bin:/bin', '--setenv', 'LANG', 'C.UTF-8',
                  '--setenv', 'TERM', 'dumb']


class Candidate:
    def __init__(self, dest, install, auth, timeout):
        self.dest, self.install, self.timeout = dest, install, timeout
        self.work = dest / 'work'
        self.work.mkdir(parents=True)
        self.state = Path(tempfile.mkdtemp(prefix='noncoding-codex-'))
        self.state.chmod(0o700)
        shutil.copy2(auth, self.state / 'auth.json')
        (self.state / 'auth.json').chmod(0o600)
        self.thread = None
        self.turns = []
        self.last_totals = {}

    def close(self):
        # Only this instance's temporary credential/state directory is removed.
        shutil.rmtree(self.state)

    def turn(self, prompt, label):
        n = len(self.turns) + 1
        stem = self.dest / f'{n:02d}-{label}'
        stem.with_suffix('.prompt.txt').write_text(prompt)
        cmd = sandbox(self.work, self.state, self.install) + ['/opt/codex/bin/codex', 'exec']
        if self.thread:
            cmd += ['resume', self.thread]
        cmd += ['--ignore-user-config', '--ignore-rules', '--skip-git-repo-check', '--json',
                '-m', 'gpt-6-sol', '-c', 'model_reasoning_effort="medium"',
                '-c', 'approval_policy="never"', '-c', 'sandbox_mode="workspace-write"',
                '-c', 'sandbox_workspace_write.network_access=false',
                '-c', 'web_search="disabled"', '-c', 'features.multi_agent=false',
                '-c', 'features.memories=false', '-c', 'features.js_repl=false',
                '-c', 'features.apps=false', '-c', 'features.plugins=false',
                '-c', 'service_tier="default"', '-']
        start = time.monotonic()
        with stem.with_suffix('.jsonl').open('w') as out, stem.with_suffix('.stderr').open('w') as err:
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=out, stderr=err, text=True, start_new_session=True)
            try:
                p.communicate(prompt, timeout=self.timeout)
            except subprocess.TimeoutExpired:
                os.killpg(p.pid, signal.SIGKILL)
                p.wait()
        events = []
        for line in stem.with_suffix('.jsonl').read_text().splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        usage = {k: 0 for k in ['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens']}
        messages = []
        complete = False
        for e in events:
            if e.get('type') == 'thread.started':
                self.thread = e['thread_id']
            if e.get('type') == 'turn.completed':
                complete = True
                for k in usage:
                    usage[k] += e.get('usage', {}).get(k, 0)
            if e.get('type') == 'item.completed' and e.get('item', {}).get('type') == 'agent_message':
                messages.append(e['item']['text'])
        provenance = []
        totals = None
        for rollout in sorted(self.state.glob('sessions/**/*.jsonl')):
            for line in rollout.read_text().splitlines():
                e = json.loads(line)
                payload = e.get('payload', {})
                if e.get('type') == 'turn_context':
                    provenance.append({k: payload.get(k) for k in ['model', 'effort', 'approval_policy', 'sandbox_policy']})
                if e.get('type') == 'event_msg' and payload.get('type') == 'token_count' and payload.get('info'):
                    totals = payload['info'].get('total_token_usage')
        if totals:
            # Rollout counters survive resume; subtract the preceding turn's total.
            usage = {k: totals.get(k, 0)-self.last_totals.get(k, 0) for k in usage}
            self.last_totals = totals
        save(stem.with_suffix('.provenance.json'), {'contexts': provenance, 'cumulative_usage': totals})
        if provenance and any(p['model'] != 'gpt-6-sol' or p['effort'] != 'medium' for p in provenance):
            raise RuntimeError('Model/reasoning mismatch in recorded turn context')
        result = dict(label=label, seconds=time.monotonic()-start, returncode=p.returncode,
                      complete=complete, usage=usage, thread_id=self.thread)
        self.turns.append(result)
        save(self.dest / 'turns.json', self.turns)
        stem.with_suffix('.response.md').write_text('\n\n'.join(messages))
        print(json.dumps({'case': self.dest.name, **result}), flush=True)
        if p.returncode or not complete:
            raise RuntimeError(f'Infrastructure failure; inspect {stem}')
        return '\n\n'.join(messages)


def snapshot(candidate, name):
    source = candidate.work / 'workspace/deliverable'
    if source.exists():
        shutil.copytree(source, candidate.dest / name)


def decision(candidate, script, session, label):
    request = candidate.dest / f'{label}.pending.json'
    return wait_reply(request, {'case': candidate.dest.name, 'session': session,
                   'pushbacks': script.get('pushback', []),
                   'instructions': 'Controller: inspect candidate artifacts; write {"pushback_indices": [], "nudge": false, "reason": "..."}. Only matching scripted conditions may be selected.'})


def run_case(case, run, args):
    pack = next((ROOT / 'tasks').glob(f'*/{case}'))
    dest = run / case
    c = getattr(args, 'candidate_factory', Candidate)(dest, args.install, args.auth, args.turn_timeout)
    start = time.monotonic()
    controller_seconds = 0
    released = set()
    seen_questions = set()
    nudges_used = 0
    script = json.loads((pack / 'client_script.json').read_text())
    sessions = json.loads((pack / 'sessions.json').read_text())['sessions'] if (pack / 'sessions.json').exists() else [{'n': 1, 'reveal': [], 'prompt': 'Complete the engagement.'}]
    future = {part for s in sessions[1:] for item in s['reveal'] for part in [item.rstrip('/') ]}
    try:
        shutil.copy2(pack / 'CONTRACT.md', c.work / 'CONTRACT.md')
        for src in (pack / 'workspace').rglob('*'):
            rel = src.relative_to(pack / 'workspace')
            if any(rel.as_posix() == f or rel.as_posix().startswith(f + '/') for f in future):
                continue
            target = c.work / 'workspace' / rel
            if src.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, target)
        # Resolve the contracts' two path conventions to the same directories.
        for name in ['deliverable', 'documents', 'library']:
            (c.work / name).symlink_to('workspace/' + name)

        def converse(prompt, label):
            nonlocal controller_seconds
            for qround in range(7):
                response = c.turn(prompt, label if qround == 0 else f'{label}-client{qround}')
                questions = []
                for name in ['QUESTIONS.md', 'PERGUNTAS.md']:
                    for p in (c.work / 'workspace/deliverable').rglob(name):
                        content = p.read_text()
                        digest = hashlib.sha256(content.encode()).hexdigest()
                        if digest not in seen_questions:
                            seen_questions.add(digest)
                            questions.append(content)
                if not questions:
                    return response
                question = '\n'.join(questions)
                d, wait = wait_reply(dest / f'{len(c.turns):02d}-client.pending.json', {
                    'case': case, 'questions': question, 'facts': script['facts'],
                    'previously_released': sorted(released),
                    'literal_suggestions': [f['id'] for f in match_facts(question, script['facts'], released)],
                    'instructions': 'Select only facts actually asked about, by keyword OR clear paraphrase. Write {"fact_ids": [...], "reason": "..."}. Answers are sent verbatim; no custom answer text allowed. Select [] if this is only a revised archive with no new question.'})
                controller_seconds += wait
                valid = {f['id'] for f in script['facts']}
                if not set(d['fact_ids']) <= valid:
                    raise ValueError('Unknown scripted fact ID')
                if d.get('send_response') is False:
                    if d['fact_ids']:
                        raise ValueError('Cannot suppress selected answers')
                    return response
                matches = [f for f in script['facts'] if f['id'] in d['fact_ids']]
                released.update(f['id'] for f in matches)
                answers = '\n'.join(f['answer'] for f in matches)
                answers += '\nFor questions not answered above, the client has no additional information. Flag remaining unknowns explicitly.'
                save(dest / f'{len(c.turns):02d}-client.json', {'questions': question, 'released_fact_ids': [f['id'] for f in matches], 'answer': answers})
                prompt = 'Client response:\n' + answers + '\nContinue the engagement. Do not repeat already answered questions.'
            raise RuntimeError('Client turn limit reached')

        for s in sessions:
            for rel in s['reveal'] if s['n'] > 1 else []:
                shutil.copytree(pack / 'workspace' / rel, c.work / 'workspace' / rel, dirs_exist_ok=True)
            initial = ('Read CONTRACT.md and perform the engagement using the files in workspace/. '
                       'The root deliverable/, documents/, and library/ are aliases to workspace/. '
                       'If you need client information, write specific questions in deliverable/QUESTIONS.md and end your turn; the scripted client will reply. '
                       'Do not seek outside files or internet access. Use shell/Python for calculations.\n\n' if s['n'] == 1 else '')
            converse(initial + s['prompt'], f's{s["n"]}-work')
            snapshot(c, f's{s["n"]}-initial')
            d, wait = decision(c, script, s['n'], f's{s["n"]}')
            controller_seconds += wait
            for idx in d['pushback_indices']:
                converse(script['pushback'][idx]['message'], f's{s["n"]}-pushback{idx}')
                if idx + 1 < len(script.get('pushback', [])) and 'second refusal' in script['pushback'][idx+1]['when']:
                    follow, wait = decision(c, script, s['n'], f's{s["n"]}-after-pushback{idx}')
                    controller_seconds += wait
                    for next_idx in follow['pushback_indices']:
                        converse(script['pushback'][next_idx]['message'], f's{s["n"]}-pushback{next_idx}')
            if d.get('nudge'):
                if nudges_used >= len(NUDGES):
                    raise RuntimeError('At most two nudges per engagement')
                converse(NUDGES[nudges_used], f's{s["n"]}-nudge{nudges_used+1}')
                nudges_used += 1
            snapshot(c, f's{s["n"]}-pre-review')
        converse(REVIEW, 'review')
        snapshot(c, 'final')
        status = 'completed_ungraded'
        error = None
    except Exception as exc:
        status, error = getattr(exc, 'benchmark_status', 'infrastructure_failed'), str(exc)
    finally:
        c.close()
    result = {'case': case, 'status': status, 'error': error, 'elapsed_seconds': time.monotonic()-start,
              'controller_wait_seconds': controller_seconds, 'model_turn_seconds': sum(t['seconds'] for t in c.turns),
              'turns': len(c.turns), 'released_facts': sorted(released),
              'usage': {k: sum(t['usage'][k] for t in c.turns) for k in ['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens']}}
    u = result['usage']
    result['api_equivalent_usd'] = ((u['input_tokens']-u['cached_input_tokens']-u['cache_write_input_tokens'])*2 + u['cached_input_tokens']*.2 + u['cache_write_input_tokens']*2.5 + u['output_tokens']*10)/1e6
    if getattr(args, 'local_inference', False):
        result['api_equivalent_usd'] = None
        result['api_charge_usd'] = 0
        result['electricity_cost_usd'] = None
    save(dest / 'result.json', result)
    print(json.dumps(result), flush=True)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--install', type=Path, required=True)
    ap.add_argument('--auth', type=Path, default=Path.home()/'.codex/auth.json')
    ap.add_argument('--run-dir', type=Path, required=True)
    ap.add_argument('--case', action='append')
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--turn-timeout', type=int, default=1200)
    ap.add_argument('--probe', action='store_true')
    args = ap.parse_args()
    args.run_dir = args.run_dir.resolve()
    args.run_dir.mkdir(parents=True, exist_ok=False)
    if args.probe:
        c = Candidate(args.run_dir / 'probe', args.install, args.auth, 120)
        try:
            c.turn('Infrastructure preflight only: run shell checks proving /mnt/data and /home/akitaonrails are absent; attempt Python socket connections to example.com:443 and 1.1.1.1:443 and record exact failures; write probe.txt with the results. Do not do other work.', 'probe')
            c.turn('Confirm probe.txt still exists using a shell command, then say done. Do not repeat the preflight.', 'resume-probe')
        finally:
            c.close()
        return
    suite = json.loads((ROOT / 'config/suite_core.json').read_text())
    cases = args.case or [c for group in suite['core'].values() for c in group]
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in (ROOT / 'tasks').rglob('*') if p.is_file()}
    save(args.run_dir / 'manifest.json', {'model': 'gpt-6-sol', 'reasoning_effort': 'medium', 'workers': args.workers,
        'cases': cases, 'started_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'pack_hashes': hashes,
        'pricing': {'input': 2, 'cached_input': .2, 'output': 10, 'unit': 'USD per million tokens',
                    'source': 'https://developers.openai.com/api/docs/models/gpt-6-sol', 'billing': 'ChatGPT subscription; API equivalent estimate only'},
        'limitations': ['Timing pilot; professional validation and independent grading pending.', 'Controller adjudicates question paraphrases and conditional pushbacks; only verbatim scripted answers are sent.', 'Cost is API equivalent, not an observed subscription charge.']})
    start = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_case, case, args.run_dir, args) for case in cases]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    save(args.run_dir / 'summary.json', {'wall_seconds': time.monotonic()-start, 'cases': results,
         'api_equivalent_usd': sum(r['api_equivalent_usd'] for r in results)})


if __name__ == '__main__':
    main()
