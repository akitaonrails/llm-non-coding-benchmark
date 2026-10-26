

A proper review pass means re-verifying everything from source: authority files, source documents, and every arithmetic claim. Starting with full re-reads of the library and source data:








Library confirmed. One critical thing to check: the library's 4ª faixa spans **720.000,01–1.800.000** — if the memoria cites real-world LC 155 bounds (870k–1.08M), that's unsupported. Reading the memoria in full and re-running all source math:






Source data verified against the memoria's §3/§4.1 lists — they match the CSVs exactly. Now reading the rest of the memoria (§5.1 tail through §9):





Now applying the fixes. First, confirming the extrato really contains no April payroll/pro-labore debits before adding that corroboration note:





Confirmed — in the May transaction statement (extrato), the only debits in April are DARF/GPS/FGTS (one month's delay in charges) and DAS. The absence of debits labeled FOLHA ABR / PRO-LABORE ABR supports the in-month payment premise. Applying three fixes:







Fixes applied. Final sweep for residual defects — dot/comma inconsistencies, stale figures across all files, and a last arithmetic re-check:






Review complete. The full re-verification found no substantive errors — all authority checks and all arithmetic passed — and three presentation/reinforcement defects were fixed.

## What was checked (and held up)

**Authority** — all three library files + INDEX re-read end to end. Every citation in the deliverables traces to a provision that actually exists there and is accurately characterized: §1º-A effective-rate formula, §§5º-J/5º-M (28% Fator R), Res. CGSN 140 art. 26 (cash-basis payroll), §4º segregation, the devoluções rule ("reduz a receita do mês em que ocorrer"), §5º-A/SV 31 (locação = Anexo III sem ISS), table rates (20,50% − 17.100; 16% − 35.640) and the 4ª faixa bound of 1.800.000 — the memoria correctly uses the **library's** bounds (720k–1,8M), and no real-world LC 155 bounds (870k–1,08M) leaked into any file. Nothing outside the library is cited; gaps remain labeled NÃO VERIFICADO in §7.

**Arithmetic** — every headline figure re-computed with exact fractions against the raw CSVs: RBT12 = 1.020.000 (exact sum); effective 18,8235% (192.000/1.020.000); serviços 14.682,35; folha 284.600 (193.000 + 35.200 + 56.400); Fator R 27,90%; DAS total 15.188,84; flip 10.261,08; ISS alternative 15.120,70; all repartição cotas; extrato chain to 86.100,33; notas 82.000 − 4.000 = 78.000. All reconcile.

**Non-reconciliations left open deliberately** (per contract): 99,85% table sum, 1,13 cota gap, 06/05 email contradiction — all flagged as U1–U6, nothing forced.

## What I changed (3 fixes, all in `deliverable/memoria.md`)

1. **§5.4** — `506.49` → `506,49`: a stray decimal point inside the Portuguese-format total block.
2. **§5.3 code block** — displayed multiplication didn't check: `0,12505882 × 0,675` actually yields 0,08441470, not …71. Replaced with the exact fraction `(127.560 / 1.020.000) × 0,675 = 86.103 / 1.020.000 = 0,08441471` (verified: 86.103/1.020.000 = 0,0844147058…), so every shown step now verifies exactly. Rate (8,4415%) and result (R$ 506,49) unchanged.
3. **§4 payroll premise reinforced** — added corroboration found during review: the May extrato has **no** "FOLHA ABR"/"PRO-LABORE ABR" debits (the only ABR entries are DARF/GPS/FGTS with its 1-month lag and the DAS payment), which independently supports the in-month payment pattern and the client's 30/04 pró-labore date.

No numbers moved: **Anexo V, 4ª faixa, DAS maio/2026 = R$ 15.188,84**, status remains **COMPLETE WITH OPEN ITEMS** (U1–U6). Ready for delivery.