Reviewing everything before delivery. First, the full library and source documents to re-verify every citation and fact:

All citations cross-checked against the library files. Now re-verifying every number independently in Python, including the sensitivity break-evens:

Numbers all confirmed. Two real defects found (the R$ 7.17 mi remainder and the break-even band) plus two authority flags to add. Let me pull the exact current text of the passages to fix:

All texts in hand. Getting the exact §0/P2 wording, then applying the fixes:

Now applying all fixes:

Fixes applied. Now syncing the STATUS gaps list with the two new [não verificado] flags and running final consistency checks:

Pre-delivery review is done. Full sweep: every citation was re-checked against the 5 library files, every fact against `relacao_imoveis.csv`/`familia.md`, and every number recomputed independently in Python. Almost everything reconciled exactly; **two real errors and two unsupported-authority gaps** were found and fixed.

## What I changed

**1. Parecer §5, item 2 — arithmetic error (double count).**
Said Marcos' floor would come out of a remainder containing "quotas remanescentes ≈ R$ 7,17 mi". That figure came from 16,430,000 − 9,265,000, which counts the 11 properties — but the holding quotas only cover the 9 rented ones, and Campos/Cotia were already listed separately (the item then summed to 11.27 mi against a stated 9.265 mi). Fixed to **R$ 5.165.000** (14.430.000 − 9.265.000), so the remainder now closes exactly: 2,10 + 1,40 + 0,60 + 5,165 = **R$ 9.265.000** = the disponível.

**2. Parecer §9(ii) + STATUS + QUESTIONS — break-even band didn't reconcile.**
The "vantagem PJ some acima de R$ 447–581 mil/ano" was wrong at both ends: the 581 mil came from extrapolating the −17,5 mil/100 mil slope past the point where **IRRF hits zero** (expenses of R$ 213.264/ano drag distributions to R$ 50 mil/mês). Corrected to a piecewise sensitivity (−17,5 mil/100 mil até R$ 213 mil; depois só −27,5 mil/100 mil) with true break-evens **R$ 447.174** (expenses also cut accounting profit) or **R$ 369.623** (only PF abates) — i.e. **36%–44% da receita**, not 44%–57%. Also clarified: if vacant-property expenses aren't deductible in PF, the advantage **never** disappears. Conclusion (holding worth under any plausible expense) unchanged.

**3. Added two [não verificado] flags (authority gaps found in review).**
- §4: the rule for valuing **nua-propriedade com usufruto reservado** when measuring the disponível is not in the library — the R$ 9.265.000 cap was set at full market value (conservative); now flagged.
- §0 P2: the rule fixing **which state's ITCMD law applies** (domicile/situs) is not in the library — kept as reasonable inference (all assets and doadora in SP), now flagged.

**4. STATUS "lacunas" list** updated with those two items plus "atualização de valor das doações na colação" (flagged in §10 but missing from the summary list). Parecer header now notes the pre-delivery review.

## What I verified and left untouched
- All 5 library citations (arts. 544/549/1.845-1.846/1.848, mention of 1.961-1.965, Decreto 46.655 note, CF 156 §2º I / CTN 37 / Tema 796 / RE 1.495.108 note, Lei 9.249 art. 23, ITCMD 4% + 2/3+1/3 "verificar", presumido 32%/15%+adicional/9%/3,65%, Lei 15.270 IRRF, LC 214) — every one supported by the library text.
- All facts vs CSV: 16.430.000 / 4.720.000 / 14.430.000 / 4.220.000 / R$ 84.900→1.018.800 / Guarulhos 3.100.000 — all exact.
- All arithmetic: PF 247.004,40 (24,2%); PJ 124.031,64 + IRRF 21.326,44 = 145.358,08 (14,3%); economia 101.646,32; payback 4,26 (banda 3,95–4,87); ITBI 432.900/306.300/126.600, banda 401.900–494.900; GCAP 1.531.500/2.297.250; ITCMD 370.600 (247.067+123.533); legítima 18.530.000 → disponível 9.265.000 → piso 3.088.333; fonte 11,33%/14,53% reconciliation — all confirmed.
- `numeros.json`: schema matches the contract exactly (7 keys, no extras) and every value re-checked — no changes needed there (the fixes don't touch its figures).

The deliverables in `workspace/deliverable/` are ready for delivery: **COMPLETE WITH OPEN ITEMS**, with both corrections documented inline in the parecer.