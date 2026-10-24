#!/usr/bin/env python3
"""Create new benchmark-only aliases; never modify existing model definitions."""
import argparse
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', action='append')
    args = ap.parse_args()
    config = json.loads((ROOT / 'config/strix_models.json').read_text())

    def api(route, data=None):
        request = urllib.request.Request(config['endpoint'] + route,
            data=json.dumps(data).encode() if data else None,
            headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.load(response)

    installed = {m['name']: m for m in api('/api/tags')['models']}
    for model in config['models']:
        if args.slug and model['slug'] not in args.slug:
            continue
        alias = model.get('alias', 'noncoding-' + model['slug'] + '-64k:20261022')
        if alias in installed:
            print(json.dumps({'model': alias, 'status': 'already exists; left unchanged'}))
            continue
        if model['source'] not in installed:
            print(json.dumps({'model': alias, 'status': 'source not yet installed'}))
            continue
        if installed[model['source']]['details']['quantization_level'] != model['quant']:
            raise RuntimeError('Source quantization mismatch: ' + model['source'])
        result = api('/api/create', {'model': alias, 'from': model['source'],
                     'parameters': {'num_ctx': config['context'], **model.get('parameters', {})}, 'stream': False})
        print(json.dumps({'model': alias, 'source': model['source'], 'result': result}))


if __name__ == '__main__':
    main()
