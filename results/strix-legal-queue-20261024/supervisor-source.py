#!/usr/bin/env python3
"""Serial legal-only campaign supervisor; never guesses client answers."""
import argparse
import atexit
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CASE = 'brlaw_01_prazos_processuais'


def legal_decision(case_dir, pending, expected_pushbacks):
    """Automate only the exact existing boolean branch, with complete artifacts."""
    if pending.get('case') != CASE or pending.get('session') != 1:
        return None
    if pending.get('pushbacks') != expected_pushbacks:
        return None
    work = (case_dir / 'work').resolve()
    folder = work / 'workspace/deliverable'
    paths = [folder / name for name in ['prazos.json', 'memoria.md', 'STATUS.md']]
    for path in paths:
        if not path.resolve().is_relative_to(work) or not path.is_file():
            return None
        if not 0 < path.stat().st_size <= 1024 * 1024:
            return None
    try:
        value = json.loads(paths[0].read_text())['citacao']['prazo_em_dobro']
    except (ValueError, KeyError, TypeError):
        return None
    if type(value) is not bool:
        return None
    return {'pushback_indices': [0] if value is False else [], 'nudge': False,
            'reason': 'Deterministic legal controller: citacao.prazo_em_dobro is '
                      + str(value).lower() + '; all required artifacts are nonempty. '
                      'No client facts inferred or released.'}


def handle_pending(run, expected_pushbacks):
    manual = []
    for path in sorted((run / CASE).glob('*.pending.json')):
        target = path.with_name(path.name.replace('.pending.json', '.decision.json'))
        if target.exists():
            continue
        # All client questions, malformed artifacts and nudge choices need review.
        decision = None
        if path.name == 's1.pending.json':
            try:
                decision = legal_decision(path.parent, json.loads(path.read_text()), expected_pushbacks)
            except (OSError, ValueError):
                pass
        if decision is None:
            manual.append(str(path))
            continue
        # Link a fully written file into place atomically, never overwrite review.
        temporary = target.with_suffix('.queue-tmp')
        with temporary.open('x') as stream:
            json.dump(decision, stream)
            stream.write('\n')
        try:
            target.hardlink_to(temporary)
        except FileExistsError:
            pass
        finally:
            temporary.unlink()
    return manual


def save(path, data):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(path)


def unit_active(unit):
    state = subprocess.check_output(
        ['systemctl', '--user', 'show', unit, '--property=ActiveState', '--value'], text=True).strip()
    return state in {'active', 'activating', 'deactivating'}


def unload(model):
    if model['endpoint'] != 'http://192.168.0.90:11434':
        return  # Never issue a blanket llama-swap unload or stop someone else's service.
    if not model['model'].startswith('noncoding-'):
        raise ValueError('Only benchmark aliases may be unloaded')
    request = urllib.request.Request(model['endpoint'] + '/api/generate',
        data=json.dumps({'model': model['model'], 'keep_alive': 0}).encode(),
        headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=60) as response:
        json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--state-dir', type=Path, required=True)
    args = parser.parse_args()
    state_dir = args.state_dir.resolve()
    state_dir.mkdir(parents=True, exist_ok=False)
    config = json.loads(args.config.read_text())
    shutil.copy2(__file__, state_dir / 'supervisor-source.py')
    shutil.copy2(args.config, state_dir / 'queue-config.json')
    expected = json.loads((ROOT / 'tasks/brlaw' / CASE / 'client_script.json').read_text())['pushback']
    if len(expected) != 1 or expected[0]['when'] != 'se prazos.json disser prazo_em_dobro = false':
        raise ValueError('Legal script changed; controller must be reviewed')
    outcomes = []
    status = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'started_at': time.time(), 'outcomes': outcomes}

    def update(stage, run, manual=None):
        status.update(stage=stage, run=str(run), manual_pending=manual or [], updated_at=time.time())
        save(state_dir / 'status.json', status)

    def on_exit():
        if status.get('stage') != 'complete':
            status.update(stage='stopped_before_completion', updated_at=time.time(),
                          note='Inspect supervisor journal; no automatic restart or retry.')
            save(state_dir / 'status.json', status)
    atexit.register(on_exit)

    def wait(run, alive, stage):
        while alive():
            update(stage, run, handle_pending(run, expected))
            time.sleep(2)

    def finish(run):
        result = json.loads((run / CASE / 'result.json').read_text())
        for script in ['verify_baseline.py', 'report_local_baseline.py']:
            subprocess.run([sys.executable, str(ROOT / 'scripts' / script), str(run)], check=False)
        outcomes.append({'run': str(run), 'case_status': result['status']})
        if result['status'] == 'infrastructure_failed':
            turns = json.loads((run / CASE / 'turns.json').read_text())
            timed_out = turns and turns[-1]['returncode'] == -9 and turns[-1]['seconds'] >= 7199
            if not timed_out:
                raise RuntimeError('Infrastructure failure: stop queue for diagnosis')

    attached = ROOT / config['attach_run']
    wait(attached, lambda: unit_active(config['attach_unit']), 'attached_existing_run')
    finish(attached)
    unload({'endpoint': 'http://192.168.0.90:11434',
            'model': 'noncoding-qwen38-27b-q4-64k:20261022'})
    for model in config['models']:
        prefix = f"strix-{model['slug']}-20261024-queue"
        probe = ROOT / 'results' / ('preflight-' + prefix)
        run = ROOT / 'results' / (prefix + '-legal')
        base = [sys.executable, '-u', str(ROOT / 'scripts/run_local_baseline.py'),
                '--endpoint', model['endpoint'], '--model', model['model'], '--hardware', model['hardware']]
        with (state_dir / (model['slug'] + '.probe.log')).open('x') as log:
            child = subprocess.Popen(base + ['--run-dir', str(probe), '--probe'], stdout=log, stderr=subprocess.STDOUT)
            wait(probe, lambda: child.poll() is None, 'admission')
        if child.returncode or not (probe / 'admission.json').exists():
            raise RuntimeError('Admission failed: stop queue for diagnosis, do not launch measured run')
        if json.loads((probe / 'admission.json').read_text()).get('passed') is not True:
            raise RuntimeError('Admission did not pass')
        with (state_dir / (model['slug'] + '.runner.log')).open('x') as log:
            child = subprocess.Popen(base + ['--run-dir', str(run), '--case', CASE], stdout=log, stderr=subprocess.STDOUT)
            wait(run, lambda: child.poll() is None, 'measured')
        if child.returncode:
            raise RuntimeError('Runner process exited abnormally; stop for diagnosis')
        finish(run)
        unload(model)
    update('complete', run)


if __name__ == '__main__':
    main()
