#!/usr/bin/env python3
"""Report explicit full-suite coverage, never infer it from runner exit status."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = [
    'sol6-medium-full-20261024',
    'sol6-medium-full-20261026',
    'b300-flash-next-full-20261024',
    'b300-glm53-flash-full-20261024',
    'rtx5090-flash-next-full-20261024',
    'strix-flash-next-full-20261024',
]


def coverage(run, expected, session_counts):
    manifest = run / 'manifest.json'
    result = {'run': run.name, 'expected_cases': len(expected),
              'expected_sessions': sum(session_counts.values()), 'errors': []}
    if manifest.exists():
        cases = json.loads(manifest.read_text())['cases']
        if len(cases) != len(expected) or set(cases) != set(expected):
            result['errors'].append('Manifest does not match the complete suite')
    else:
        result['errors'].append('Run manifest not yet present')
    outcomes = {}
    sessions = 0
    for case in expected:
        path = run / case
        f = path / 'result.json'
        if f.exists():
            outcomes[case] = json.loads(f.read_text())['status']
        f = path / 'turns.json'
        if f.exists():
            turns = json.loads(f.read_text())
            completed = {int(m.group(1)) for t in turns
                         if (m := re.fullmatch(r's(\d+)-work', t['label']))
                         and t.get('complete')}
            sessions += len(completed & set(range(1, session_counts[case] + 1)))
    pending = [str(f.relative_to(ROOT)) for f in run.glob('*/*.pending.json')
               if not f.with_name(f.name.replace('.pending.', '.decision.')).exists()]
    result.update(outcomes=dict(Counter(outcomes.values())),
                  cases_with_results=len(outcomes),
                  completed_initial_sessions=sessions,
                  missing_case_results=sorted(set(expected) - outcomes.keys()),
                  pending=pending,
                  all_cases_accounted_for=len(outcomes) == len(expected) and not result['errors'],
                  all_cases_completed=len(outcomes) == len(expected)
                  and all(v == 'completed_ungraded' for v in outcomes.values())
                  and sessions == sum(session_counts.values()) and not result['errors'])
    return result


def main():
    suite = json.loads((ROOT / 'config/suite_full_20261024.json').read_text())
    expected = suite['cases']
    counts = {}
    for case in expected:
        pack = next((ROOT / 'tasks').glob(f'*/{case}'))
        f = pack / 'sessions.json'
        counts[case] = len(json.loads(f.read_text())['sessions']) if f.exists() else 1
    assert len(expected) == len(set(expected)) == 38
    assert sum(counts.values()) == suite['session_units'] == 63
    print(json.dumps([coverage(ROOT / 'results' / name, expected, counts)
                      for name in RUNS], indent=2))


if __name__ == '__main__':
    main()
