#!/usr/bin/env python3
"""Tests for the controller console: it must never invent a decision."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import controller


def client_pending(tmp_path):
    path = tmp_path / '01-client.pending.json'
    path.write_text(json.dumps({
        'case': 'bracc_01_das_fator_r',
        'questions': 'Q2: when was the April pro-labore paid?',
        'facts': [{'id': 'prolabore_abril', 'trigger': ['abril'], 'answer': '30 de abril'}],
        'previously_released': [], 'literal_suggestions': ['prolabore_abril']}))
    return path


def controller_pending(tmp_path):
    path = tmp_path / 's1.pending.json'
    path.write_text(json.dumps({'case': 'brlaw_01_prazos_processuais', 'pushbacks': [{'when': 'prazo_em_dobro false'}],
                                'instructions': 'inspect artifacts'}))
    return path


def test_client_decision_written_next_to_pending(tmp_path):
    path = client_pending(tmp_path)
    controller.decide(path, ['prolabore_abril'], 'Q2 asks the April payment date directly.')
    body = json.loads((tmp_path / '01-client.decision.json').read_text())
    assert body['fact_ids'] == ['prolabore_abril']
    assert body['reason'].startswith('Q2 asks')
    assert body['controller'] == controller.CONTROLLER_ID


def test_unknown_fact_is_refused(tmp_path):
    path = client_pending(tmp_path)
    with pytest.raises(SystemExit):
        controller.decide(path, ['invented_fact'], 'Should not be accepted at all.')
    assert not (tmp_path / '01-client.decision.json').exists()


def test_missing_reason_is_refused(tmp_path):
    path = client_pending(tmp_path)
    with pytest.raises(SystemExit):
        controller.decide(path, [], '')
    assert not (tmp_path / '01-client.decision.json').exists()


def test_pushback_and_nudge_cannot_both_fire(tmp_path):
    path = controller_pending(tmp_path)
    with pytest.raises(SystemExit):
        controller.decide(path, [], 'Both a pushback and a nudge would be double pressure', pushbacks=[0], nudge=True)


def test_pushback_decision_shape(tmp_path):
    path = controller_pending(tmp_path)
    controller.decide(path, [], 'Scripted condition matched the delivered file', pushbacks=[0])
    body = json.loads((tmp_path / 's1.decision.json').read_text())
    assert body['pushback_indices'] == [0] and body['nudge'] is False


def test_pending_list_excludes_answered(tmp_path, monkeypatch):
    monkeypatch.setattr(controller, 'RESULTS', tmp_path)
    run = tmp_path / 'lane-full-20261024' / 'case_a'
    run.mkdir(parents=True)
    pending = run / '01-client.pending.json'
    pending.write_text(json.dumps({'case': 'case_a', 'questions': 'none', 'facts': []}))
    assert controller.pending_files() == [pending]
    controller.decide(pending, [], 'No scripted fact covers this question')
    assert controller.pending_files() == []


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, '-q']))
