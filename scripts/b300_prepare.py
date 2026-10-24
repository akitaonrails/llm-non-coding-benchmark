#!/usr/bin/env python3
"""Run on the authorized pod: pin/download one model, then serve on loopback.

No credentials, public listener, fixture files, or grading materials needed.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import time

from huggingface_hub import HfApi, snapshot_download


def main():
    cuda = '/workspace/noncoding-venv/lib/python3.12/site-packages/nvidia/cu13'
    os.environ['CUDA_HOME'] = cuda
    os.environ['PATH'] = cuda + '/bin:/workspace/noncoding-venv/bin:' + os.environ.get('PATH', '')
    os.environ['LD_LIBRARY_PATH'] = cuda + '/lib:' + os.environ.get('LD_LIBRARY_PATH', '')
    # Wheel toolkits omit the conventional unversioned runtime/linker paths.
    for link, target in [(Path(cuda) / 'lib64', 'lib'),
                         (Path(cuda) / 'lib/libcudart.so', 'libcudart.so.13')]:
        if not link.exists() and not link.is_symlink():
            link.symlink_to(target)
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--download-only', action='store_true')
    args = parser.parse_args()
    model = next(m for m in json.loads(args.config.read_text())['models'] if m['id'] == args.model)
    root = Path('/workspace/noncoding-benchmark')
    root.mkdir(exist_ok=True)
    evidence = root / model['id']
    evidence.mkdir(exist_ok=True)
    pin = evidence / 'weights.json'
    if pin.exists():
        metadata = json.loads(pin.read_text())
        if metadata['repo'] != model['repo']:
            raise RuntimeError('Existing pin does not match requested repository')
    else:
        info = HfApi().model_info(model['repo'], files_metadata=True)
        metadata = {'repo': model['repo'], 'revision': info.sha,
                    'resolved_at': time.time(),
                    'files': [{'path': f.rfilename, 'size': f.size} for f in info.siblings]}
        pin.write_text(json.dumps(metadata, indent=2) + '\n')
    print(json.dumps({'stage': 'download', 'repo': model['repo'], 'revision': metadata['revision']}), flush=True)
    destination = root / 'weights' / model['id']
    completion = evidence / 'download-complete.json'
    if not completion.exists():
        snapshot_download(model['repo'], revision=metadata['revision'], local_dir=destination,
                          ignore_patterns=['*.bin', '*.pt', '*.pth', '*.gguf'], max_workers=8)
        completion.write_text(json.dumps({'revision': metadata['revision'], 'time': time.time()}) + '\n')
    elif json.loads(completion.read_text())['revision'] != metadata['revision']:
        raise RuntimeError('Downloaded revision does not match pin')
    print(json.dumps({'stage': 'download_complete', 'time': time.time()}), flush=True)
    if args.download_only:
        return
    command = ['/workspace/noncoding-venv/bin/vllm', 'serve', str(destination),
               '--served-model-name', model['id'], '--host', '127.0.0.1', '--port', '18081',
               '--tensor-parallel-size', '1', '--max-model-len', '65536',
               '--max-num-seqs', '4', '--gpu-memory-utilization', '0.92',
               '--enable-auto-tool-choice', '--enable-prefix-caching', '--enable-chunked-prefill',
               '--performance-mode', 'interactivity', *model['args']]
    launch = {'command': command, 'started_at': time.time(), 'pid': os.getpid(), 'cuda_home': cuda,
              'gpu': subprocess.check_output(['nvidia-smi', '--query-gpu=name,memory.total,driver_version', '--format=csv'], text=True),
              'packages': subprocess.check_output(['uv', 'pip', 'freeze', '--python', '/workspace/noncoding-venv/bin/python'], text=True)}
    (evidence / f'launch-{time.time_ns()}.json').write_text(json.dumps(launch, indent=2) + '\n')
    print(json.dumps({'stage': 'serve', 'command': command}), flush=True)
    # Retain server output on the pod, separately from the downloader transcript.
    log = os.open(evidence / f'server-{time.time_ns()}.log', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.dup2(log, 1)
    os.dup2(log, 2)
    os.close(log)
    os.execv(command[0], command)


if __name__ == '__main__':
    main()
