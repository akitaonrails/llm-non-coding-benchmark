

Calculations verified. Now writing the deliverables.





Engagement complete. All deliverables are in `workspace/deliverable/`:

**Result — DAS maio/2026: R$ 15.188,84**

| Step | Value | Basis |
|---|---|---|
| RBT12 (mai/25–abr/26) | R$ 1.020.000,00 | sum of `faturamento_12_meses.csv` |
| Folha 12m (payment basis) | R$ 276.700,00 | 284.600 accrued − 3.200 Apr pró-labore (paid 06/05, outside window) − 4.700 Apr employer contributions (paid 07/05 per statement), per Res. CGSN 140 art. 26 §2º |
| Fator R | 27,13% (< 28%) | → **Anexo V** (robust: 27,13–27,90% in all sensitivity scenarios) |
| Faixa / alíquota | 4 · 20,50% − PD 17.100 | effective rate = (1.020.000 × 0,205 − 17.100)/1.020.000 = **18,8235%** |
| Serviços (82.000 − 4.000 estorno) | **R$ 14.682,35** | 78.000 × 18,8235% |
| Locação (Anexo III, no ISS per SV 31) | **R$ 506,49** | 6.000 × 12,5059% (III, faixa 4) × (1 − 0,3250) |

Key judgments, all documented in `memoria.md`:
- **Estorno** (NFS-e 1188): reduces May revenue to 78.000 per the library's cancellation rule.
- **Locação**: not lumped with services as the sócio suggested — segregated and taxed under Anexo III with the ISS share deducted.
- **Open items** (none affect May's DAS): the 06/05 pró-labore payment is missing from the May statement (affects June's DAS — asked in `QUESTIONS.md`); the Anexo V repartição isn't in the library, so the service share is unallocated in `reparticao` (only the rental share is broken out); and the library's Anexo III repartição sums to 99,85%, leaving a R$ 1,13 gap I did not force to balance.

`STATUS.md` = **COMPLETE WITH OPEN ITEMS**.