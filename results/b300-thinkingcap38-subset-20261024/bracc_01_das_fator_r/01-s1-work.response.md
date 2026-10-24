

I'll read the library and documents now.







The PDF uses custom-encoded fonts. Let me parse its ToUnicode CMap to verify it matches the CSV statement.





Engagement complete. Deliverables are in `workspace/deliverable/` (root `deliverable/` is a symlink to it):

**Result — DAS maio/2026: R$ 15.188,84**
- **RBT12** = R$ 1.020.000 (sum of `faturamento_12_meses.csv`, 05/2025–04/2026) → 4ª faixa
- **Folha 12m (payment basis)** = 284.600 − 3.200 (pró-labore de abr, paid in May per the sócio's email/extrato) − 4.700 (encargos de abr, paid 05/07 per extrato) = **276.700**
- **Fator R** = 276.700 ÷ 1.020.000 = **27,13% < 28%** → **Anexo V** (the sócio's "repeat Anexo V" instruction is confirmed by the calculation, not assumed)
- **Alíquota efetiva (Anexo V, 4ª faixa)** = (1.020.000 × 20,5% − 17.100) ÷ 1.020.000 = **18,8235%**
- **Receitas**: serviços 82.000 − 4.000 estorno = 78.000 (estorno reduces May revenue per the library); locação de notebooks = 6.000, segregated per §4º and taxed "na forma do Anexo III, deduzida a parcela do ISS" (SV 31) — despite the sócio thinking it would ride along with services
- **DAS**: serviços 78.000 × 18,8235% = 14.682,35 · locação 6.000 × 12,5059% × (1 − 32,5%) = 506,49

**Files**
- `apuracao.json` — full schema, all citations from `library/INDEX.md`
- `memoria.md` — per-note classification, full arithmetic, library citations, extrato PDF×CSV reconciliation (I decoded the PDF's CMap; it matches the CSV line by line)
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**: (1) repartição sums to 15.001,45 vs 15.188,84 — gap of 187,39 = 164,61 correctly-deducted ISS on the locação + 22,78 because the library's distribution table sums 99,85%; left open, not force-balanced; (2) Anexo V distribution isn't in the library, so the repartição uses the only table available (Anexo III, 4ª faixa); (3) sensitivity: including April's encargos in folha gives Fator R 27,59% — still Anexo V, result unchanged.

No client questions were needed — the sócio's pró-labore doubt resolved against the library's payment-basis rule and his own statement (the 06/05 vs 16/05 date discrepancy is immaterial, both in May).