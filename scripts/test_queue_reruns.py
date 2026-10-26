import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import queue_reruns


def test_quarantine_preserves_attempt_and_logs_reason(tmp_path):
    run = tmp_path / 'lane'
    (run / 'case_a').mkdir(parents=True)
    (run / 'case_a' / 'result.json').write_text('{"status": "completed_ungraded"}')
    preserved = queue_reruns.quarantine(run, 'case_a', 'audit: over-release')
    assert preserved == '_aborted/case_a-attempt1'
    assert (run / '_aborted/case_a-attempt1/result.json').exists()
    assert not (run / 'case_a').exists()
    row = json.loads((run / 'retries.jsonl').read_text().splitlines()[0])
    assert row['case'] == 'case_a' and row['reason'] == 'audit: over-release'


def test_quarantine_numbers_next_attempt(tmp_path):
    run = tmp_path / 'lane'
    (run / '_aborted/case_a-attempt1').mkdir(parents=True)
    (run / 'case_a').mkdir()
    assert queue_reruns.quarantine(run, 'case_a', 'again') == '_aborted/case_a-attempt2'
