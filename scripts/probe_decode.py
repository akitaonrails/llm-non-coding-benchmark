#!/usr/bin/env python3
"""Measure warm streaming decode without disabling the model's reasoning."""
import argparse
import json
from pathlib import Path
import time
import urllib.request


def probe(endpoint, model):
    body = {'model': model, 'messages': [{'role': 'user', 'content':
        'Explain the steps of designing a reliable database backup and restore process in detail.'}],
        'max_tokens': 1024, 'stream': True, 'stream_options': {'include_usage': True}}
    start = time.monotonic()
    first = last = None
    usage = finish = None
    with urllib.request.urlopen(urllib.request.Request(endpoint + '/v1/chat/completions',
            data=json.dumps(body).encode(), headers={'Content-Type': 'application/json',
                'Authorization': 'Bearer local'}), timeout=600) as response:
        for line in response:
            if not line.startswith(b'data: ') or line.strip() == b'data: [DONE]':
                continue
            event = json.loads(line[6:])
            if event.get('usage'):
                usage = event['usage']
            for choice in event.get('choices', []):
                delta = choice.get('delta', {})
                if any(delta.get(k) for k in ['content', 'reasoning', 'reasoning_content', 'tool_calls']):
                    last = time.monotonic()
                    if first is None:
                        first = last
                if choice.get('finish_reason'):
                    finish = choice['finish_reason']
    tokens = (usage or {}).get('completion_tokens', 0)
    return {'seconds': time.monotonic() - start, 'ttft_seconds': first - start if first else None,
            'decode_tokens_per_second': (tokens - 1) / (last - first) if first and last > first else None,
            'usage': usage, 'finish_reason': finish}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--endpoint', required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--minimum-tps', type=float, default=100,
                        help='Warm decode acceptance threshold (B300 default: 100)')
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    runs = []
    for _ in range(2):
        runs.append(probe(args.endpoint, args.model))
        print(json.dumps(runs[-1]), flush=True)
    passed = bool(runs[-1]['decode_tokens_per_second'] and
                  runs[-1]['decode_tokens_per_second'] >= args.minimum_tps and
                  runs[-1]['usage']['completion_tokens'] >= 256)
    args.output.write_text(json.dumps({'model': args.model, 'runs': runs, 'passed': passed,
                          'minimum_decode_tokens_per_second': args.minimum_tps,
                          'scope': 'Stream-observed decode throughput; includes SSH transport jitter.'}, indent=2) + '\n')
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
