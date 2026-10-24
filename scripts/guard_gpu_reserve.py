#!/usr/bin/env python3
"""Stop only the owned benchmark process group if GPU headroom is exhausted."""
import argparse
import os
import signal
import subprocess
import time


def free_mib():
    result = subprocess.run(
        ['nvidia-smi', '--id=0', '--query-gpu=memory.free', '--format=csv,noheader,nounits'],
        capture_output=True, text=True, check=True, timeout=5)
    return int(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--minimum-mib', type=int, default=3072)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command or args.minimum_mib < 3072:
        parser.error('A command and a minimum reserve of 3072 MiB are required')
    if free_mib() < args.minimum_mib:
        raise SystemExit('Insufficient GPU headroom before launch')
    child = subprocess.Popen(command, start_new_session=True)
    def interrupted(signum, frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, interrupted)
    try:
        while child.poll() is None:
            available = free_mib()
            if available < args.minimum_mib:
                raise RuntimeError(f'GPU reserve breached: {available} MiB free; stopping owned server')
            time.sleep(0.5)
        return child.returncode
    finally:
        # The process group contains only this launch, never desktop applications.
        try:
            os.killpg(child.pid, signal.SIGTERM)
            time.sleep(1)
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        child.wait()


if __name__ == '__main__':
    raise SystemExit(main())
