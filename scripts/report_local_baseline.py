#!/usr/bin/env python3
"""Summarize local measurements without implying task correctness or free power."""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run', type=Path)
    run = ap.parse_args().run
    manifest = json.loads((run / 'manifest.json').read_text())
    summary = json.loads((run / 'summary.json').read_text())
    cases = summary['cases']
    rows = [f'# {manifest["model"]} — {manifest.get("hardware", "Strix Halo")} diagnostic run', '',
            'Execution and timing only; task correctness is not graded.', '',
            f'- Harness: {manifest["harness"]}; {manifest["workers"]} worker.',
            f'- Wall time: {summary["wall_seconds"]/60:.2f} minutes.',
            f'- Active agent time: {sum(c["model_turn_seconds"] for c in cases)/60:.2f} minutes.',
            f'- Controller waits: {sum(c["controller_wait_seconds"] for c in cases)/60:.2f} minutes.',
            '- API charge: $0. Electricity, hardware and pod rental cost: not included.',
            '- Different agent harness from Sol; not a model-only controlled comparison.', '',
            '| Case | Agent min | Turns | Input tokens | Cached input | Output tokens | Status |',
            '|---|---:|---:|---:|---:|---:|---|']
    for c in cases:
        u = c['usage']
        rows.append(f'| {c["case"]} | {c["model_turn_seconds"]/60:.2f} | {c["turns"]} | {u["input_tokens"]:,} | {u["cached_input_tokens"]:,} | {u["output_tokens"]:,} | {c["status"]} |')
    rows += ['', 'Input includes cached input. Output/reasoning accounting is limited to provider-reported fields.',
             'Provider request logs include background title generation and are retained per case.', '']
    report = '\n'.join(rows)
    (run / 'REPORT.md').write_text(report)
    print(report)


if __name__ == '__main__':
    main()
