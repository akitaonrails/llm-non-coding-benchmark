#!/usr/bin/env python3
"""Check measurement provenance and required artifact presence, not correctness."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    'usacc_02_close_gap': ['bank_reconciliation.md', 'adjusting_entries.json', 'trial_balance_2026-03-31.json', 'open_items.md'],
    'usacc_03_household_1040': ['return.json', 'return.md', 'judgment_calls.md'],
    'usacc_06_sale_asset_vs_stock': ['comparison.json', 'memo.md', 'form_8594_counter.md'],
    'usacc_09_revenue_going_concern': ['revenue_memo.md', 'q4_pl_adjusted.json', 'response_to_ceo.md'],
    'bracc_01_das_fator_r': ['apuracao.json', 'memoria.md'],
    'bracc_03_cbs_ibs_ano_teste': ['apuracao_teste.json', 'orientacao.md'],
    'bracc_06_venda_quotas_vs_ativos': ['comparativo.json', 'memorando.md'],
    'bracc_10_provisoes_covenant': ['classificacoes.json', 'nota_explicativa.md', 'carta_diretoria.md'],
    'uslaw_01_deadlines_removal': ['deadlines.json', 'memo.md'],
    'uslaw_03_noncompete_memo': ['memo.md', 'citations.json'],
    'uslaw_04_litigation_sequence': ['session1/assessment.md', 'session1/demand_letter.md', 'session2/advice.md', 'session2/reply_letter.md', 'session3/advice.md', 'session4/strategy_memo.md', 'session5/settlement.json', 'session5/term_sheet.md'],
    'uslaw_09_retaliation_termination': ['risk_assessment.json', 'corrected_separation_agreement_terms.md', 'advice_to_hr.md'],
    'brlaw_01_prazos_processuais': ['prazos.json', 'memoria.md'],
    'brlaw_03_pejotizacao': ['parecer.json', 'parecer.md'],
    'brlaw_07_credor_rj': ['estrategia.json', 'habilitacao_divergencia.md', 'resposta_cliente.md'],
    'brlaw_10_cobranca_prescrita': ['analise.json', 'memorando.md'],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run', type=Path)
    run = ap.parse_args().run
    manifest = json.loads((run/'manifest.json').read_text())
    failures, artifacts, contexts = [], 0, 0
    for name, digest in manifest['pack_hashes'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != digest:
            failures.append(f'Frozen input changed: {name}')
    for case in manifest['cases']:
        directory = run/case
        result = json.loads((directory/'result.json').read_text())
        turns = json.loads((directory/'turns.json').read_text())
        if result['status'] != 'completed_ungraded':
            failures.append(f'{case}: execution did not finish')
        for name in REQUIRED[case] + ['STATUS.md']:
            p = directory/'final'/name
            if not p.is_file() or not p.stat().st_size:
                failures.append(f'{case}: missing/empty {name}')
            else:
                artifacts += 1
                if p.suffix == '.json':
                    try:
                        json.loads(p.read_text())
                    except json.JSONDecodeError:
                        failures.append(f'{case}: malformed JSON {name}')
        for key, value in result['usage'].items():
            if sum(t['usage'].get(key, 0) for t in turns) != value:
                failures.append(f'{case}: inconsistent usage {key}')
        for path in directory.glob('*.provenance.json'):
            data = json.loads(path.read_text())
            if manifest.get('harness') == 'opencode 2.1.2':
                contexts += 1
                if data.get('model') != manifest['model'] or data.get('network') != 'unshare-all; allowlisted model-only Unix gateway':
                    failures.append(f'{case}: unexpected local model/network context')
                if data.get('usage_source') != 'provider SSE usage':
                    failures.append(f'{case}: incomplete provider usage evidence')
            for context in data.get('contexts', []):
                contexts += 1
                if context['model'] != 'gpt-6-sol' or context['effort'] != 'medium' or context['sandbox_policy'].get('network_access'):
                    failures.append(f'{case}: unexpected model/effort/network context')
        for pending in directory.glob('*.pending.json'):
            if not pending.with_name(pending.name.replace('.pending.', '.decision.')).exists():
                failures.append(f'{case}: unanswered controller request {pending.name}')
        if manifest.get('harness') == 'opencode 2.1.2':
            started = (directory/'provider-started.jsonl').read_text().splitlines()
            completed = [json.loads(line) for line in (directory/'provider-requests.jsonl').read_text().splitlines()]
            if len(started) != len(completed) or any(r['http_status'] != 200 or not r.get('usage') for r in completed):
                failures.append(f'{case}: incomplete provider request accounting or HTTP errors')
    outcome = {'passed': not failures, 'failures': failures, 'cases': len(manifest['cases']),
               'nonempty_required_artifacts': artifacts, 'checked_context_records_including_repeats': contexts,
               'frozen_files_checked': len(manifest['pack_hashes']),
               'scope': 'Execution provenance, artifact presence/JSON syntax, frozen inputs and usage accounting only. No correctness score.'}
    (run/'verification.json').write_text(json.dumps(outcome, indent=2)+'\n')
    print(json.dumps(outcome, indent=2))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
