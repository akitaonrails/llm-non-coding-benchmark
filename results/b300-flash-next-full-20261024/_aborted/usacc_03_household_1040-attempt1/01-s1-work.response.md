

Now the library files:







The taxable income 59,850 lands exactly inside the library's tax-table excerpt (row 59,850–59,900 = 6,708, confirmed by the midpoint method) — the right path. But my 8962 code grabbed the wrong band: 292.79% FPL is in the 250–300% band (4→6%), and the repayment tier is 200–<300% → **$1,900 limit**. Recomputing:





All numbers reconcile, and the $1,900 repayment cap binds under either rounding convention (robust). Now writing the deliverables:





Engagement complete. All deliverables are in `deliverable/` (aliases to `workspace/deliverable/`), `return.json` validates and every internal cross-foot passes.

**Headline: federal refund $2,322.00.** Marcus's expectation is corrected — the $28,000 S-corp loss does **not** come straight off income: the basis rollforward (contributions + income, then distributions, then losses) leaves only **$11,500** of stock basis at 1/1/2025, so 11,500 is allowed and **16,500 suspended** (Form 7203). Pike's guarantee of the bank line creates no debt basis.

Key figures (all arithmetic in `return.md`, authorities keyed to `library/INDEX.md`):

| Item | Result |
|---|---|
| AGI (line 11) | 91,350 = wages 122,000 + interest 400 − Sch E net 31,050 (S-corp 11,500 + rental 19,550) |
| Form 8582 | loss 21,018; MAGI 110,900 (allowed S-corp loss reduces it, per the excerpt); allowance 25,000 − 5,450 = 19,550; carryforward 1,468 |
| Taxable income / tax | 59,850 → **6,708** from the library table row (midpoint method cross-check agrees) |
| Form 8962 | 91,350 = 292.79% of FPL 31,200; applicable figure 5.7115%; annual PTC 7,531.26 vs 9,900 APTC → excess 2,368.74, **capped at $1,900** (200–<300% tier; cap binds under either rounding convention) |
| Dependents / CTC | Sofia only, $2,200 — Leo goes to the father in odd years per the custody order (agreement controls per the 1040 excerpt) |
| Total tax / refund | 8,608 − 2,200 = 6,408 vs withholding 8,730 → refund 2,322 |
| NY part-year | 183 resident days (FL domicile Jul 3); both spouses' wages NY-source all year under convenience-of-the-employer (permission ≠ necessity); rental remains NY-source; big IT-203 withholding refund |

Notable judgment calls (each with the rejected alternative in `judgment_calls.md`): the below-market rent fits the library's "unrelated tenant, never raised" carve-out (biggest swing item — reversal would add 19,550 to AGI and break the tax table's excerpt range); family size 4 on Form 8962 (only the 4-person FPL exists in the library); residency end Jul 2 not Jun 30.

`STATUS.md` reads **COMPLETE WITH OPEN ITEMS**: five confirmation questions (father's Leo claim, NY workdays/necessity, rent facts, policy enrollment, file completeness) are in `QUESTIONS.md` with the dollar effect of each reversal noted. NY tax itself was left uncomputed rather than invented — the library contains no NY rate tables.