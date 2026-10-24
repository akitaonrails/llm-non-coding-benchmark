Library confirmed: repartição percentages exist only for Anexo III (4ª faixa) — none for Anexo V. Now the calculations:

All figures verified. Writing the deliverables now — first `apuracao.json`:

One correction in `memoria.md` — the payment-window start date (typo: 01/08/2025 → 01/05/2025):

Engagement complete. All three deliverables are in `workspace/deliverable/` and validated.

## Result: DAS maio/2026 = **R$ 15.188,84**

| Step | Value | Source |
|---|---|---|
| RBT12 (12m: 2025-05→2026-04) | R$ 1.020.000,00 | `faturamento_12_meses.csv` |
| Folha 12m (payments to 04/30) | R$ 281.400,00 | `resumo_folha_12_meses.csv` − 3.200 |
| Fator R | **27,5882% < 28% → Anexo V**, faixa 4 | `lc123_art18_fator_r.md` |
| Alíquota efetiva (20,5% faixa, PD 17.100) | 18,823529% | `anexos_iii_v_tabelas.md` |
| Serviços: 82.000 − 4.000 estorno (1188, pago 29/05) | 78.000 × efetiva = **14.682,35** | |
| Locação notebooks: 6.000 → Anexo III **deduzido ISS** (não é serviço, SV 31): 750,35 − 243,86 | **506,49** | `locacao_bens_moveis_iss.md` |

**Traps handled:** the sócio's "repita o Anexo V" was verified (not trusted) via the Fator R test; his late April pró-labore paid 06/05 falls outside the 12-previous-months payment window per Res. CGSN 140 art. 26 §2º — it moves to the June/2026 window (it changes the reported Fator R from 27,90% to 27,59%, but not the annex and not the DAS); the locação did **not** go with services — it's segregated on Anexo III minus the ISS share; the estorno cut May service revenue.

**Open items (in `STATUS.md`, COMPATível com "COMPLETE WITH OPEN ITEMS"):** the library has no Anexo V repartição table, so the per-tax split of the R$ 14.682,35 services portion is left open rather than invented (JSON marks it via `reparticao_observacao`); the library's own Anexo III percentages sum to 99,85% (R$ 1,13 gap on the locação slice, not forced); assumptions P1–P3 documented in `memoria.md`, none affecting the DAS or annex choice.