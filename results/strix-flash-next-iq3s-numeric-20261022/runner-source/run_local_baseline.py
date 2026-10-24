#!/usr/bin/env python3
"""OpenCode with networkless tools and an allowlisted Unix-socket model gateway.

Only /v1/models and /v1/chat/completions reach the configured remote provider.
The model cannot reach host files, credentials, other cases, or arbitrary URLs.
"""
import argparse
import hashlib
import http.client
import http.server
import json
import os
from pathlib import Path
import shutil
import shlex
import signal
import socketserver
import subprocess
import tempfile
import threading
import time
import urllib.parse
import urllib.request
import urllib.error

import run_codex_baseline as baseline

ROOT = baseline.ROOT
BINARY = Path('/home/akitaonrails/.local/share/mise/installs/opencode/2.1.2/node_modules/.mise/@opencode+cli-linux-x64@2.1.2/node_modules/@opencode/cli-linux-x64/bin/opencode')


class OutputLimitExceeded(RuntimeError):
    benchmark_status = 'candidate_output_limit'


REMOTE_HTTP = '''import http.client,json,sys
request=json.load(sys.stdin)
connection=http.client.HTTPConnection(request['host'],request['port'],timeout=7200)
try:
    body=json.dumps(request['body']) if request['body'] is not None else None
    connection.request('POST' if body is not None else 'GET',request['path'],body,
                       {'Content-Type':'application/json','Authorization':'Bearer local'})
    response=connection.getresponse()
    print(json.dumps({'status':response.status,'content_type':response.getheader('Content-Type','application/json')}),flush=True)
    while chunk := response.read1(65536):
        sys.stdout.buffer.write(chunk)
        sys.stdout.buffer.flush()
finally:
    connection.close()
'''


class RemoteHTTP:
    """One fixed HTTP operation via authorized SSH exec, not a network tunnel."""
    def __init__(self, ssh_host, host, port, path, body=None):
        self.proc = subprocess.Popen(['ssh', '-T', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=10',
                                     ssh_host, 'python3 -c ' + shlex.quote(REMOTE_HTTP)],
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            self.proc.stdin.write(json.dumps({'host': host, 'port': port, 'path': path, 'body': body}).encode())
            self.proc.stdin.close()
            metadata = json.loads(self.proc.stdout.readline())
            self.status, self.content_type = metadata['status'], metadata['content_type']
        except Exception:
            self.close()
            raise

    def getheader(self, name, default=None):
        return self.content_type if name.lower() == 'content-type' else default

    def read1(self, size):
        return self.proc.stdout.read1(size)

    def read(self, size=-1):
        return self.proc.stdout.read(size)

    def close(self):
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait()
        for stream in [self.proc.stdin, self.proc.stdout, self.proc.stderr]:
            if stream and not stream.closed:
                stream.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def fetch_json(endpoint, path, body=None, ssh_host=None, timeout=600):
    if ssh_host:
        url = urllib.parse.urlparse(endpoint)
        response = RemoteHTTP(ssh_host, url.hostname, url.port, path, body)
    else:
        request = urllib.request.Request(endpoint.rstrip('/') + path,
            data=json.dumps(body).encode() if body is not None else None,
            headers={'Content-Type': 'application/json', 'Authorization': 'Bearer local'})
        response = urllib.request.urlopen(request, timeout=timeout)
    with response:
        if response.status >= 400:
            raise urllib.error.HTTPError(endpoint + path, response.status, 'Remote HTTP error', None, None)
        return json.load(response)


class UnixServer(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    daemon_threads = True


class Gateway(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path != '/v1/models':
            self.send_error(403)
            return
        data = json.dumps({'object': 'list', 'data': [{'id': self.server.model, 'object': 'model'}]}).encode()
        self.send_response(200)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != '/v1/chat/completions':
            self.send_error(403)
            return
        size = int(self.headers.get('Content-Length', 0))
        if not 0 < size <= 16_000_000:
            self.send_error(413)
            return
        payload = json.loads(self.rfile.read(size))
        if payload.get('model') != self.server.model:
            self.send_error(403)
            return
        # Do not accept user-supplied remote image/audio URLs through the gateway.
        if any(isinstance(m.get('content'), list) for m in payload.get('messages', [])):
            for m in payload['messages']:
                if isinstance(m.get('content'), list):
                    if any(p.get('type') != 'text' for p in m['content']):
                        self.send_error(403)
                        return
        started = time.monotonic()
        # Some OpenCode/provider combinations do not enforce the configured
        # model output limit. Normalize it at the actual HTTP boundary.
        requested = [payload.get(k) for k in ('max_tokens', 'max_completion_tokens')]
        limits = [v for v in requested if isinstance(v, int) and v > 0]
        payload.pop('max_completion_tokens', None)
        payload['max_tokens'] = min([16384, *limits])
        with self.server.metrics.with_name('provider-started.jsonl').open('a') as out:
            out.write(json.dumps({'model': payload['model'], 'max_tokens': payload['max_tokens'],
                                  'requested_limits': requested, 'started_at': time.time()}) + '\n')
        if payload.get('stream'):
            payload['stream_options'] = {'include_usage': True}
        conn = None
        try:
            if getattr(self.server, 'ssh_host', None):
                conn = response = RemoteHTTP(self.server.ssh_host, self.server.host, self.server.port,
                                             '/v1/chat/completions', payload)
            else:
                conn = http.client.HTTPConnection(self.server.host, self.server.port, timeout=1800)
                conn.request('POST', '/v1/chat/completions', json.dumps(payload),
                             {'Content-Type': 'application/json', 'Authorization': 'Bearer local'})
                response = conn.getresponse()
            self.send_response(response.status)
            self.send_header('Content-Type', response.getheader('Content-Type', 'application/json'))
            self.end_headers()
            received = bytearray()
            while chunk := response.read1(65536):
                received.extend(chunk)
                self.wfile.write(chunk)
                self.wfile.flush()
            usage, finish, timings = None, None, None
            for line in received.decode(errors='replace').splitlines():
                if not line.startswith('data: ') or line == 'data: [DONE]':
                    continue
                event = json.loads(line[6:])
                usage = event.get('usage') or usage
                timings = event.get('timings') or timings
                for choice in event.get('choices', []):
                    finish = choice.get('finish_reason') or finish
            with self.server.metrics.open('a') as out:
                out.write(json.dumps({'model': payload['model'], 'seconds': time.monotonic()-started,
                                      'http_status': response.status, 'usage': usage,
                                      'finish_reason': finish, 'max_tokens': payload['max_tokens'],
                                      'timings': timings,
                                      'requested_sampling': {k: payload.get(k) for k in ('temperature', 'top_p', 'seed', 'reasoning_effort')}}) + '\n')
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            if conn:
                conn.close()


def sandbox(work, state, gateway, config, binary=BINARY):
    cmd = ['bwrap', '--die-with-parent', '--unshare-all',
           '--ro-bind', '/usr', '/usr', '--symlink', 'usr/bin', '/bin',
           '--symlink', 'usr/lib', '/lib', '--symlink', 'usr/lib64', '/lib64',
           '--proc', '/proc', '--dev', '/dev', '--tmpfs', '/tmp',
           '--bind', str(state), '/home/bench', '--bind', str(work), '/work',
           '--ro-bind', str(binary), '/opt/opencode', '--ro-bind', str(config), '/opt/config.json',
           '--ro-bind', str(gateway), '/gateway.sock', '--chdir', '/work', '--clearenv']
    env = {'HOME': '/home/bench', 'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'TERM': 'dumb',
           'OPENCODE_CONFIG': '/opt/config.json', 'OPENCODE_DISABLE_PROJECT_CONFIG': 'true',
           'OPENCODE_DISABLE_AUTOUPDATE': 'true', 'OPENCODE_DISABLE_MODELS_FETCH': 'true'}
    for k, v in env.items():
        cmd += ['--setenv', k, v]
    return cmd


class Candidate:
    def __init__(self, dest, install, auth, timeout, *, endpoint, model, ssh_host=None):
        self.dest, self.timeout, self.model = dest, timeout, model
        self.work = dest / 'work'
        self.work.mkdir(parents=True)
        self.private = Path(tempfile.mkdtemp(prefix='noncoding-local-'))
        self.state = self.private / 'home'
        self.state.mkdir()
        self.thread, self.turns = None, []
        self.config = self.private / 'config.json'
        baseline.save(self.config, {
            '$schema': 'https://opencode.ai/config.json', 'model': 'strix/' + model,
            'small_model': 'strix/' + model, 'enabled_providers': ['strix'],
            'share': 'disabled', 'autoupdate': False,
            'permission': {'*': 'allow', 'task': 'deny', 'webfetch': 'deny', 'websearch': 'deny'},
            'provider': {'strix': {'npm': '@ai-sdk/openai-compatible', 'name': 'Strix benchmark',
                'options': {'baseURL': 'http://127.0.0.1:18080/v1', 'apiKey': 'local', 'timeout': timeout * 1000},
                'models': {model: {'name': model, 'tool_call': True, 'reasoning': False,
                                   'limit': {'context': 65536, 'output': 16384},
                                   'cost': {'input': 0, 'output': 0}}}}}})
        shutil.copy2(self.config, dest / 'harness-config.json')
        url = urllib.parse.urlparse(endpoint)
        self.socket = self.private / 'gateway.sock'
        self.server = UnixServer(str(self.socket), Gateway)
        self.server.host, self.server.port = url.hostname, url.port
        self.server.model = model
        self.server.ssh_host = ssh_host
        self.server.metrics = dest / 'provider-requests.jsonl'
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        shutil.rmtree(self.private)

    def command(self, args):
        return sandbox(self.work, self.state, self.socket, self.config) + [
            '/bin/sh', '-c',
            'socat TCP-LISTEN:18080,bind=127.0.0.1,reuseaddr,fork UNIX-CONNECT:/gateway.sock & '
            'bridge=$!; trap "kill $bridge 2>/dev/null" EXIT; "$@"', 'bridge', *args]

    def turn(self, prompt, label):
        stem = self.dest / f'{len(self.turns)+1:02d}-{label}'
        stem.with_suffix('.prompt.txt').write_text(prompt)
        args = ['/opt/opencode', 'run', '--standalone', '--auto', '--agent', 'build',
                '--format', 'json', '--thinking', '--model', 'strix/' + self.model]
        if self.thread:
            args += ['--session', self.thread]
        else:
            # Avoid asynchronous title-generation calls that can outlive the
            # task turn and make request-level usage attribution ambiguous.
            args += ['--title', 'noncoding-' + self.dest.name]
        args += [prompt]
        start = time.monotonic()
        prior_requests = len(self.server.metrics.read_text().splitlines()) if self.server.metrics.exists() else 0
        with stem.with_suffix('.jsonl').open('w') as out, stem.with_suffix('.stderr').open('w') as err:
            proc = subprocess.Popen(self.command(args), stdout=out, stderr=err, start_new_session=True)
            try:
                proc.wait(timeout=self.timeout)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()
        events = []
        for line in stem.with_suffix('.jsonl').read_text().splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        usage = dict.fromkeys(['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens',
                               'output_tokens', 'reasoning_output_tokens'], 0)
        complete = False
        messages = []
        for e in events:
            self.thread = e.get('sessionID') or self.thread
            part = e.get('part', {})
            if e.get('type') == 'text':
                messages.append(part.get('text', ''))
            if e.get('type') == 'step_finish':
                tokens = part.get('tokens', {})
                cached = tokens.get('cache', {}).get('read', 0)
                written = tokens.get('cache', {}).get('write', 0)
                usage['input_tokens'] += tokens.get('input', 0) + cached + written
                usage['cached_input_tokens'] += cached
                usage['cache_write_input_tokens'] += written
                usage['output_tokens'] += tokens.get('output', 0)
                usage['reasoning_output_tokens'] += tokens.get('reasoning', 0)
                complete = part.get('reason') == 'stop'
        requests = [json.loads(line) for line in self.server.metrics.read_text().splitlines()[prior_requests:]] if self.server.metrics.exists() else []
        successful = [r for r in requests if r['http_status'] < 400]
        provider_usage = bool(successful) and all(r.get('usage') for r in successful)
        if provider_usage:
            usage = dict.fromkeys(usage, 0)
            for request in successful:
                raw = request['usage']
                usage['input_tokens'] += raw.get('prompt_tokens', 0)
                usage['output_tokens'] += raw.get('completion_tokens', 0)
                usage['cached_input_tokens'] += raw.get('prompt_tokens_details', {}).get('cached_tokens', 0)
                usage['reasoning_output_tokens'] += raw.get('completion_tokens_details', {}).get('reasoning_tokens', 0)
            complete = successful[-1]['finish_reason'] == 'stop' and not any(e.get('type') == 'error' for e in events)
        result = dict(label=label, seconds=time.monotonic()-start, returncode=proc.returncode,
                      complete=complete, usage=usage, thread_id=self.thread)
        self.turns.append(result)
        baseline.save(self.dest / 'turns.json', self.turns)
        baseline.save(stem.with_suffix('.provenance.json'), {'model': self.model, 'harness': 'opencode 2.1.2',
                      'network': 'unshare-all; allowlisted model-only Unix gateway',
                      'usage_source': 'provider SSE usage' if provider_usage else 'step_finish',
                      'requests': len(requests), 'http_errors': len(requests)-len(successful)})
        stem.with_suffix('.response.md').write_text('\n\n'.join(messages))
        print(json.dumps({'case': self.dest.name, **result}), flush=True)
        if proc.returncode or not complete:
            if requests and requests[-1].get('finish_reason') == 'length':
                raise OutputLimitExceeded(f'Output limit reached without a completed turn; inspect {stem}')
            raise RuntimeError(f'Incomplete local turn; inspect {stem}')
        return '\n\n'.join(messages)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--endpoint', default='http://192.168.0.90:11434')
    ap.add_argument('--model', required=True)
    ap.add_argument('--ssh-host', help='Perform fixed model HTTP requests through SSH exec on this host')
    ap.add_argument('--run-dir', required=True, type=Path)
    ap.add_argument('--case', action='append')
    ap.add_argument('--turn-timeout', type=int, default=7200)
    ap.add_argument('--probe', action='store_true')
    args = ap.parse_args()
    args.run_dir = args.run_dir.resolve()
    args.run_dir.mkdir(parents=True, exist_ok=False)
    source_dir = args.run_dir / 'runner-source'
    source_dir.mkdir()
    source_hashes = {}
    for source in [Path(__file__), Path(baseline.__file__)]:
        shutil.copy2(source, source_dir / source.name)
        source_hashes[source.name] = hashlib.sha256(source.read_bytes()).hexdigest()
    inventory = {'endpoint': args.endpoint, 'ssh_host': args.ssh_host, 'selected_model': args.model,
                 'agent_context_limit': 65536, 'agent_output_limit': 16384,
                 'reasoning': 'provider default; no reasoning override',
                 'binary_sha256': hashlib.sha256(BINARY.read_bytes()).hexdigest(),
                 'runner_source_sha256': source_hashes}
    for route in ['/api/version', '/api/tags', '/v1/models']:
        try:
            data = fetch_json(args.endpoint, route, ssh_host=args.ssh_host, timeout=10)
            if route == '/api/tags':
                data = [m for m in data.get('models', []) if m['name'] == args.model]
            inventory[route] = data
        except Exception as exc:
            inventory[route] = {'unavailable': type(exc).__name__}
    baseline.save(args.run_dir / 'inventory.json', inventory)
    args.install = args.auth = None
    args.local_inference = True
    args.candidate_factory = lambda *a: Candidate(*a, endpoint=args.endpoint, model=args.model, ssh_host=args.ssh_host)
    if args.probe:
        c = args.candidate_factory(args.run_dir / 'probe', None, None, 600)
        try:
            limit_start = time.monotonic()
            limited = fetch_json(args.endpoint, '/v1/chat/completions',
                {'model': args.model, 'messages': [{'role': 'user',
                    'content': 'List the integers from 1 to 100, one per line. Do not stop early.'}],
                    'max_tokens': 8, 'stream': False}, ssh_host=args.ssh_host)
            baseline.save(args.run_dir / 'output-limit-probe.json',
                          {'seconds': time.monotonic()-limit_start, 'requested_max_tokens': 8, 'response': limited})
            if limited.get('usage', {}).get('completion_tokens') != 8 or limited['choices'][0].get('finish_reason') != 'length':
                raise RuntimeError('Backend did not demonstrate enforcement of the requested output limit')
            checked = subprocess.run(c.command(['/usr/bin/python3', '-c',
                'import os,socket; assert not os.path.exists("/home/akitaonrails"); '
                'assert not os.path.exists("/mnt/data"); s=socket.socket(); s.settimeout(2); '
                '\ntry: s.connect(("1.1.1.1",443)); raise AssertionError("Network reachable")'
                '\nexcept OSError as e: print("Host paths absent; network denied:",repr(e))']), capture_output=True, text=True)
            baseline.save(args.run_dir / 'isolation.json', {'returncode': checked.returncode, 'stdout': checked.stdout, 'stderr': checked.stderr})
            if checked.returncode:
                raise RuntimeError('Isolation failed')
            c.turn('Use the shell tool to calculate 17*23 with Python and write the result to probe.txt. Then say done.', 'probe')
            if not (c.work / 'probe.txt').is_file() or (c.work / 'probe.txt').read_text().strip() != '391':
                raise RuntimeError('Preflight did not create the expected artifact')
            first_thread = c.thread
            response = c.turn('Read probe.txt with a tool and report its contents. Do not change it.', 'resume')
            if c.thread != first_thread or '391' not in response or (c.work / 'probe.txt').read_text().strip() != '391':
                raise RuntimeError('Session resume/artifact verification failed')
            events = [json.loads(line) for line in (c.dest / '02-resume.jsonl').read_text().splitlines() if line.startswith('{')]
            reads = [e for e in events if e.get('type') == 'tool_use'
                     and e.get('part', {}).get('state', {}).get('status') == 'completed'
                     and 'probe.txt' in json.dumps(e.get('part', {}).get('state', {}).get('input', {}))
                     and '391' in str(e.get('part', {}).get('state', {}).get('output', ''))]
            if not reads:
                raise RuntimeError('Resume did not demonstrate a successful artifact-reading tool call')
            started_requests = (c.dest / 'provider-started.jsonl').read_text().splitlines()
            completed_requests = [json.loads(line) for line in (c.dest / 'provider-requests.jsonl').read_text().splitlines()]
            if len(started_requests) != len(completed_requests) or any(r['http_status'] != 200 or not r.get('usage') for r in completed_requests):
                raise RuntimeError('Preflight request accounting is incomplete or contains HTTP errors')
            try:
                loaded = fetch_json(args.endpoint, '/api/ps', ssh_host=args.ssh_host, timeout=10)['models']
                selected = [m for m in loaded if m['name'] == args.model]
                baseline.save(args.run_dir / 'runtime.json', selected)
                if args.model.startswith('noncoding-') and (not selected or selected[0]['context_length'] != 65536):
                    raise RuntimeError('Benchmark alias did not load with the intended 64K context')
            except urllib.error.HTTPError as exc:
                if exc.code != 404:
                    raise
                baseline.save(args.run_dir / 'runtime.json', {'ollama_runtime_endpoint': 'not applicable'})
            baseline.save(args.run_dir / 'admission.json', {'passed': True, 'same_session': True,
                          'artifact': '391', 'resume_read_tool_calls': len(reads)})
        finally:
            c.close()
        return
    suite = json.loads((ROOT / 'config/suite_core.json').read_text())
    cases = args.case or [c for group in suite['core'].values() for c in group]
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in (ROOT / 'tasks').rglob('*') if p.is_file()}
    baseline.save(args.run_dir / 'manifest.json', {'model': args.model, 'endpoint': args.endpoint, 'ssh_host': args.ssh_host,
        'harness': 'opencode 2.1.2', 'workers': 1, 'cases': cases, 'pack_hashes': hashes,
        'started_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'limitations': ['Diagnostic; ungraded fixtures match Sol baseline.',
                       'Local electricity cost unmeasured; no API fee.', 'Different agent harness from Sol.']})
    start = time.monotonic()
    results = []
    for case in cases:
        results.append(baseline.run_case(case, args.run_dir, args))
        baseline.save(args.run_dir / 'progress.json', results)
    baseline.save(args.run_dir / 'summary.json', {'wall_seconds': time.monotonic()-start, 'cases': results,
                                                'api_charge_usd': 0, 'electricity_cost_usd': None})


if __name__ == '__main__':
    main()
