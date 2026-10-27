# Full-suite execution summary — verified 2026-10-27

Execution-level results for the five completed full-suite lanes (38 cases,
63 session-units each). **Correctness is ungraded**: every retained result is
either `completed_ungraded` (all sessions and the final review finished) or
`candidate_output_limit` (a turn hit the 16,384-token response cap without
completing). Nothing below ranks answer quality. Source files are each case's
`result.json`; the cross-lane verification that produced these numbers is
`scripts/verify_full_suite.py`, and coverage is
`results/full-suite-coverage-20261024.json`.

## What was verified

For each lane: the manifest lists exactly the 38 suite cases; every case holds
a `result.json`; every completed case has all of its scripted sessions and the
final review turn marked complete; every provenance record names the lane's
model (Sol: `gpt-6-sol` at medium effort on all 572 contexts); every released
fact id exists in the case's client script; every pending controller round has
a decision; every quarantined attempt under `_aborted/` is listed in
`retries.jsonl`; the four local lanes share one harness configuration (OpenCode
2.1.2, 64K context, 16,384-token response cap, same permissions). The pack
hashes differ from the current `tasks/` only for the two client scripts
corrected to v1.1 (`usacc_03`, `bracc_06`); their retained results were either
re-run on v1.1 or never released the affected fact.

## Outcomes and active time

| Lane | Completed | Output-limit | Model-active minutes | Median min/case | Longest case | Reported output tokens | Output tok/s |
|---|---:|---:|---:|---:|---|---:|---:|
| Sol 6 medium / Codex, 4 workers | 38 | 0 | 248 | 5.7 | usacc_04 (22) | 767,268 | 52 |
| Flash-Next NVFP4 / B300 | 33 | 5 | 622 | 12.1 | usacc_04 (97) | 5,533,462 | 148 |
| GLM 5.3 Flash NVFP4 / B300 | 31 | 7 | 725 | 17.5 | brlaw_04 (53) | 5,056,360 | 116 |
| Flash-Next IQ3_S / RTX 5090 | 35 | 3 | 432 | 9.4 | bracc_04 (29) | 3,981,009 | 153 |
| Flash-Next IQ3_S / Strix Halo | 34 | 4 | 2,105 | 46.7 | usacc_04 (219) | 5,026,982 | 40 |

Model-active minutes exclude controller waits. Sol's wall time was 72.9 min
with four workers and US$16.72 API-equivalent (list prices, not the
subscription charge). Sol reports reasoning tokens separately (229,369); the
B300 vLLM lanes report them inside the usage block (3.1M and 3.3M); the Strata
lanes (RTX 5090, Strix) do not break them out, and all four local providers ran
with their default reasoning behaviour, so "output tokens" is comparable only
as the provider-reported figure. The median slowdown relative to Sol on the
same case is 1.6× (RTX 5090), 1.9× (B300 Flash-Next), 2.7× (B300 GLM) and
7.7× (Strix). The single-stream decode rate of the RTX 5090 IQ3_S build is on
par with the B300 NVFP4 build in this harness; the B300's advantage was never
single-stream latency.

## Output-limit cases

The 16,384-token cap was hit only by the local lanes and concentrates on the
long multi-session cases:

| Case | B300 FN | B300 GLM | RTX 5090 | Strix |
|---|---|---|---|---|
| usacc_04_twelve_closes | s12 work | s3 work | s5 work | s10 work |
| usacc_06_sale_asset_vs_stock | s1 work | review | — | s1 work |
| brlaw_04_execucao_fiscal | review | s5 work | — | — |
| bracc_02_escolha_regime | — | s1 client reply | — | review |
| bracc_04_lucro_real_trimestre | — | s3 work | s2 work | — |
| bracc_05_abertura_empresa | — | review | — | — |
| bracc_01_das_fator_r | — | review | — | — |
| bracc_06_venda_quotas_vs_ativos | — | — | — | review |
| usacc_05_entity_choice | review | — | — | — |
| usacc_02_close_gap | — | — | review | — |
| uslaw_04_litigation_sequence | review | — | — | — |

These are retained as explicit non-completions, never retried, and should be
graded as failures of the configuration under this cap, not excluded.

## Per-case model-active minutes

`*` marks `candidate_output_limit`.

| Case | Sol | B300 FN | B300 GLM | RTX 5090 | Strix |
|---|---:|---:|---:|---:|---:|
| bracc_01_das_fator_r | 5 | 13 | 11* | 8 | 40 |
| bracc_02_escolha_regime | 6 | 10 | 12* | 10 | 69* |
| bracc_03_cbs_ibs_ano_teste | 6 | 13 | 13 | 9 | 35 |
| bracc_04_lucro_real_trimestre | 9 | 17 | 19* | 29* | 48 |
| bracc_05_abertura_empresa | 7 | 24 | 17* | 15 | 47 |
| bracc_06_venda_quotas_vs_ativos | 5 | 7 | 11 | 7 | 77* |
| bracc_07_holding_patrimonial | 5 | 36 | 27 | 10 | 35 |
| bracc_08_recuperacao_judicial | 11 | 12 | 26 | 9 | 123 |
| bracc_09_distribuicao_lucros | 4 | 6 | 20 | 6 | 37 |
| bracc_10_provisoes_covenant | 5 | 9 | 13 | 9 | 28 |
| brlaw_01_prazos_processuais | 2 | 6 | 15 | 8 | 13 |
| brlaw_02_contrato_lgpd | 6 | 9 | 15 | 9 | 20 |
| brlaw_03_pejotizacao | 5 | 18 | 21 | 13 | 45 |
| brlaw_04_execucao_fiscal | 10 | 37* | 53* | 25 | 84 |
| brlaw_05_divorcio_partilha | 6 | 9 | 29 | 12 | 39 |
| brlaw_07_credor_rj | 5 | 9 | 12 | 9 | 34 |
| brlaw_08_ma_diligencia | 7 | 13 | 19 | 10 | 57 |
| brlaw_09_justa_causa_estabilidade | 6 | 9 | 30 | 6 | 32 |
| brlaw_10_cobranca_prescrita | 4 | 15 | 8 | 6 | 28 |
| usacc_01_schedule_c | 6 | 10 | 14 | 12 | 128 |
| usacc_02_close_gap | 5 | 23 | 22 | 12* | 28 |
| usacc_03_household_1040 | 7 | 9 | 13 | 13 | 61 |
| usacc_04_twelve_closes | 22 | 97* | 24* | 26* | 219* |
| usacc_05_entity_choice | 8 | 15* | 29 | 10 | 40 |
| usacc_06_sale_asset_vs_stock | 7 | 33* | 13* | 9 | 64* |
| usacc_07_holding_qsbs | 6 | 8 | 14 | 9 | 29 |
| usacc_08_chapter11_debtor | 12 | 18 | 21 | 16 | 71 |
| usacc_09_revenue_going_concern | 4 | 8 | 21 | 10 | 19 |
| usacc_10_fraud_indicators | 5 | 5 | 7 | 8 | 76 |
| uslaw_01_deadlines_removal | 5 | 11 | 18 | 7 | 42 |
| uslaw_02_msa_playbook | 4 | 9 | 11 | 3 | 11 |
| uslaw_03_noncompete_memo | 5 | 21 | 21 | 27 | 58 |
| uslaw_04_litigation_sequence | 11 | 16* | 49 | 13 | 58 |
| uslaw_05_divorce_split_support | 6 | 10 | 19 | 9 | 47 |
| uslaw_07_chapter11_creditor | 6 | 17 | 9 | 8 | 77 |
| uslaw_08_sale_diligence_apa | 7 | 15 | 19 | 16 | 50 |
| uslaw_09_retaliation_termination | 4 | 8 | 13 | 6 | 87 |
| uslaw_10_llc_squeeze_out | 6 | 18 | 16 | 7 | 46 |

## Controller provenance of the retained results

| Lane | Decisions by Claude Fable 5.1 | Decisions by the original orchestrator (DeepSeek V4.1 Flash, audited) | Audit re-runs | Quarantined attempts |
|---|---:|---:|---:|---:|
| Sol 6 medium (2026-10-26 run) | 110 | 0 | — | 0 |
| B300 Flash-Next | 25 | 144 (+1 early decision with no controller tag) | 8 | 11 |
| B300 GLM 5.3 Flash | 27 | 128 | 7 | 15 |
| RTX 5090 | 41 | 123 (+1 untagged) | 9 | 88 |
| Strix | 34 | 147 (+1 untagged) | 4 | 10 |

The untagged decision is `bracc_01_das_fator_r/01-client.decision.json` in
three lanes: it predates the `controller` field, carries a reason, and its
releases match the literal suggestions; the audit reviewed it with the rest.
The RTX 5090 quarantine count is dominated by the 2026-10-24 reserve-guard stop
(25 cases × 3 failed attempts against a dead server, recorded in `retries.jsonl`
with a wildcard `preserved` entry per case). Every other orchestrator decision
that the audit left in place was judged correct or a "silent round" (no facts
leaked; the model was not told the client had nothing more), which the re-run
rule deliberately did not re-run.

## Known limits of this comparison

- Different harnesses (Codex vs OpenCode), different quantisations and serving
  stacks, and a response cap that only the local lanes could hit.
- Two review turns (B300 Flash-Next `brlaw_03`, RTX 5090 `brlaw_04`) logged one
  HTTP error among ~28 requests each; both turns completed.
- The pilot directories from 2026-10-22/24 (`sol6-medium-core-20261022-r2`,
  `rtx5090-flash-next-reserved-subset-20261024`,
  `strix-flash-next-iq3s-numeric-20261022`) and the quota-failed
  `sol6-medium-full-20261024` still contain the pre-v1.1 placeholder leak in
  `usacc_03` / `bracc_06`; they are superseded by the full suite and were not
  re-run.
- One run per configuration. No repetitions, so none of the timings carry an
  error bar.
- Grading of the retained deliverables was done on 2026-10-27; see
  [`FULL_SUITE_GRADING_20261027.md`](FULL_SUITE_GRADING_20261027.md). Human
  spot-check of the trust events and demotions is the remaining gate.
