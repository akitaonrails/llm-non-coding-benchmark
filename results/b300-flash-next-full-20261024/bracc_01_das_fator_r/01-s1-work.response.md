

All calculations verified. Now writing the deliverables one by one.





The check failed only due to truncated effective rate precision in JSON (0.188235 vs 0.18823529…). Increasing stored precision:





Engagement work is done for this pass; deliverables are in `deliverable/` and I've ended the turn with specific client questions since five points genuinely depend on client facts or a library gap.

**Result (as documented): Anexo V, 4ª faixa — DAS maio/2026 = R$ 15.188,84**

| Item | Valor | Base |
|---|---:|---|
| RBT12 (05/25–04/26) | 1.020.000 | CSV faturamento, art. 18 §1º |
| Fator R (folha **paga** na janela: 281.400) | 27,59% < 28% → Anexo V | Res. CGSN 140 art. 26 §§1º–2º |
| Alíquota **efetiva** Anexo V 4ª faixa | (1.020.000×20,5% − 17.100)/1.020.000 = **18,8235%** | §1º-A |
| Serviços: 82.000 − 4.000 estorno = 78.000 | **14.682,35** | cancelamento reduz o mês em que ocorre |
| Locação notebooks: 6.000, Anexo III sem ISS (6,000×12,5059%×67,5%) | **506,49** | §5º-A + SV 31 |

**Where I corrected the sócio's instruction** (both grounded in `library/`):
1. "Repetir o Anexo V com a alíquota da faixa" → the library requires the **efetiva** (§1º-A), not the nominal 20,50% (literal compliance would overpay services by R$ 1.307,65).
2. Locação does **not** "vai junto com os serviços": it's segregated (§4º), taxed by Anexo III with the ISS share removed (§5º-A, SV 31).
3. Fator R is computed on **cash** (values paid in the window), not competência — the resumo is by competência; the extrato shows pró-labore de abril paid 06/05 and encargos de abril paid 07/05, i.e., outside the window. Sensitivity 27,13%–27,90% keeps it Anexo V regardless.

**Open items** (listed in `STATUS.md` = COMPLETE WITH OPEN ITEMS, questions in `QUESTIONS.md`): the library has **no Anexo V repartição table**, so `reparticao` in the JSON only decomposes the locação (services share refused — numbers not invented); real payment date of the April pró-labore (only fact that could flip to Anexo III); ISS-deduction mechanics for locação (my reading 8,4415% → 506,49 vs. nominal-base alternative 438,35); and the library's repartição percentages summing to 99,85% (left unreconciled, as instructed).