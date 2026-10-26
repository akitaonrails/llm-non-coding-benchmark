#!/usr/bin/env python3
"""Focused tests for the lane supervisor's retry and quarantine decisions."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_lane


def make_case(run_dir, case, status=None, partial=False):
    dest = run_dir / case
    dest.mkdir(parents=True)
    if status:
        (dest / 'result.json').write_text(json.dumps({'case': case, 'status': status}))
    elif partial:
        (dest / '01-s1-work.jsonl').write_text('{}\n')
    return dest


def test_completed_and_output_limit_cases_are_final(tmp_path):
    make_case(tmp_path, 'done', 'completed_ungraded')
    make_case(tmp_path, 'limited', 'candidate_output_limit')
    assert run_lane.plan(tmp_path, ['done', 'limited'], max_attempts=3) == []


def test_interrupted_case_is_preserved_then_retried(tmp_path):
    dest = make_case(tmp_path, 'bracc_01', partial=True)
    todo = run_lane.plan(tmp_path, ['bracc_01'], max_attempts=3)
    assert todo == ['bracc_01']
    assert not dest.exists()
    preserved = tmp_path / '_aborted' / 'bracc_01-attempt1' / '01-s1-work.jsonl'
    assert preserved.is_file()
    assert json.loads((tmp_path / 'retries.jsonl').read_text().strip())['reason'] == 'interrupted'


def test_infrastructure_failure_is_retried_up_to_the_cap(tmp_path):
    make_case(tmp_path, 'usacc_02', 'infrastructure_failed')
    assert run_lane.plan(tmp_path, ['usacc_02'], max_attempts=3) == ['usacc_02']
    make_case(tmp_path, 'usacc_02', 'infrastructure_failed')
    todo = run_lane.plan(tmp_path, ['usacc_02'], max_attempts=3)
    assert todo == ['usacc_02']
    make_case(tmp_path, 'usacc_02', 'infrastructure_failed')
    # Third retained failure is reported, never silently replaced.
    assert run_lane.plan(tmp_path, ['usacc_02'], max_attempts=3) == []
    assert run_lane.case_state(tmp_path, 'usacc_02') == ('infrastructure_failed', 3)


def test_missing_case_is_scheduled_without_quarantine(tmp_path):
    assert run_lane.plan(tmp_path, ['uslaw_03'], max_attempts=3) == ['uslaw_03']
    assert not (tmp_path / '_aborted').exists()
    assert run_lane.case_state(tmp_path, 'uslaw_03') == ('absent', 0)


def test_attempt_numbering_does_not_overwrite_preserved_attempts(tmp_path):
    for _ in range(2):
        make_case(tmp_path, 'brlaw_04', partial=True)
        run_lane.plan(tmp_path, ['brlaw_04'], max_attempts=3)
    names = sorted(p.name for p in (tmp_path / '_aborted').iterdir())
    assert names == ['brlaw_04-attempt1', 'brlaw_04-attempt2']


def test_suite_scope_is_the_full_38_cases():
    suite = json.loads(run_lane.SUITE.read_text())
    assert len(suite['cases']) == 38 == len(set(suite['cases']))


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, '-q']))
