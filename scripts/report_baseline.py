#!/usr/bin/env python3
"""Summarize retained measurements; never imply execution completion is correctness."""
import argparse
import json
from pathlib import Path
import statistics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run', type=Path)
    args = ap.parse_args()
    run = args.run
    manifest = json.loads((run/'manifest.json').read_text())
    summary = json.loads((run/'summary.json').read_text()) if (run/'summary.json').exists() else None
    rows = [json.loads(p.read_text()) for p in sorted(run.glob('*/result.json'))]
    totals = {k: sum(r['usage'].get(k, 0) for r in rows) for k in ['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens']}
    lines = ['# Sol 6 medium — core timing baseline', '',
             f"Model: `{manifest['model']}`; reasoning: `{manifest['reasoning_effort']}`; concurrency: {manifest['workers']}; started: {manifest['started_at']}.", '',
             f"Finished executions: {sum(r['status']=='completed_ungraded' for r in rows)}/{len(manifest['cases'])}. Infrastructure failures: {sum(r['status']=='infrastructure_failed' for r in rows)}. Correctness is not yet graded.", '']
    if summary:
        lines += [f"Suite elapsed wall time: **{summary['wall_seconds']/60:.2f} minutes** (includes controller waits).", '']
    if rows:
        lines += [f"Summed active candidate time: {sum(r['model_turn_seconds'] for r in rows)/60:.2f} minutes. Median per engagement: {statistics.median(r['model_turn_seconds'] for r in rows)/60:.2f} minutes.",
                  f"Summed controller waiting: {sum(r['controller_wait_seconds'] for r in rows)/60:.2f} minutes; these waits can overlap across workers.", '',
                  f"Input: {totals['input_tokens']:,}, including {totals['cached_input_tokens']:,} cached and {totals['cache_write_input_tokens']:,} cache-write tokens. Output: {totals['output_tokens']:,}, including {totals['reasoning_output_tokens']:,} reasoning tokens.", '',
                  f"Estimated API-equivalent cost: **${sum(r['api_equivalent_usd'] for r in rows):.4f}**. Authentication used ChatGPT subscription; this is not an observed API invoice.", '',
                  '| Engagement | Active min | Elapsed min | Turns | Input | Cached | Output | API equiv. USD | Status |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---|']
    for r in rows:
        u = r['usage']
        lines.append(f"| {r['case']} | {r['model_turn_seconds']/60:.2f} | {r['elapsed_seconds']/60:.2f} | {r['turns']} | {u['input_tokens']:,} | {u['cached_input_tokens']:,} | {u['output_tokens']:,} | {r['api_equivalent_usd']:.4f} | {r['status']} |")
    phases = {}
    for path in run.glob('*/turns.json'):
        for t in json.loads(path.read_text()):
            label = t['label']
            phase = 'Final review' if label.startswith('review') else 'Pushback' if 'pushback' in label else 'Nudge' if 'nudge' in label else 'Client follow-up' if 'client' in label else 'Initial/session work'
            bucket = phases.setdefault(phase, {'turns': 0, 'seconds': 0, 'cost': 0})
            u = t['usage']
            bucket['turns'] += 1
            bucket['seconds'] += t['seconds']
            bucket['cost'] += ((u['input_tokens']-u['cached_input_tokens']-u.get('cache_write_input_tokens',0))*2 + u['cached_input_tokens']*.2 + u.get('cache_write_input_tokens',0)*2.5 + u['output_tokens']*10)/1e6
    lines += ['', '| Phase | Turns | Summed active min | API equiv. USD |', '|---|---:|---:|---:|']
    for name, value in phases.items():
        lines.append(f"| {name} | {value['turns']} | {value['seconds']/60:.2f} | {value['cost']:.4f} |")
    lines += ['', 'Standard API-equivalent rates per million tokens: uncached input $2; cache reads $0.20; cache writes $2.50; output $10. Reasoning is included in output, not added twice. Rates checked 2026-10-22: [official model pricing](https://developers.openai.com/api/docs/models/gpt-6-sol).', '',
              'Setup, preflight, the invalidated first attempt, and Astra controller usage are excluded from these candidate measurements. Normal provider caching was enabled; this is not a cold-cache measurement. Four workers were scheduled, but controller pauses and uneven case lengths affect effective concurrency. This single timing pilot does not establish reliability or professional fitness. Controller decisions about question paraphrases and scripted pushback are documented in docs/BASELINE_RUN.md; all client answers are verbatim from the frozen script.', '']
    (run/'REPORT.md').write_text('\n'.join(lines))
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
