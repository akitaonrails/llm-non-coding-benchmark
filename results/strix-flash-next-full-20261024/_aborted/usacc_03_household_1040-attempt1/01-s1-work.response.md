All 12 decisions have rejected alternatives and valid citations. One strict-schema issue remains: `return.json` contains two extra metadata keys, violating "every key in that schema, no others." That information is already duplicated in `return.md` and `STATUS.md`, so I'll remove them.

Heading mismatch in my guard check, not the file. Adjusting the assertion:

One last check for dangling references to the removed keys:

Final consistency pass is done. The engagement package under `workspace/deliverable/` is closed out for this turn:

**What changed in this last pass**
- `return.json`: removed the two extra metadata keys (`_sign_conventions`, `_not_determinable_from_library`) so the file now matches the CONTRACT.md schema exactly — top-level keys are only `form1040`, `form7203`, `form8582`, `form8962`, `dependents`, `ny`. Nothing was lost: the sign conventions are documented in `return.md`/§1 and judgment call 11, and the "not determinable from library" list is in `STATUS.md`.
- Re-verified programmatically: JSON parses, schema keys match the contract template key-for-key, and every arithmetic invariant holds (9 = 11 = 91,350 · 15 = 59,850 · 18 = 6,708 + 1,900 = 8,608 · 24 = 8,608 − 2,200 = 6,408 · refund = 8,730 − 6,408 = 2,322 · 7203: 11,500 + 16,500 = 28,000 · 8582: 21,018 − 19,550 = 1,468 · 8962: 9,900 − 7,531.25 = 2,368.75 → capped at 1,900).
- Confirmed all citations in the three markdown files resolve to files in `library/INDEX.md`, all 12 judgment calls carry a rejected alternative, and no dangling references to the pruned keys exist.

**Final position**
- Federal: AGI **$91,350**, taxable income **$59,850**, tax **$6,708** (Tax Table row 59,850–59,900), +$1,900 excess APTC, −$2,200 CTC → total tax **$6,408**, withholding $8,730 → **refund $2,322**.
- Marcus's expectation refuted: $11,500 of the $28,000 S-corp loss allowed, **$16,500 suspended** (stock basis only).
- Rental: $19,550 allowed under §469(i), $1,468 carryforward (MAGI $110,900).
- Leo not claimed (odd-year custody); dependents: Sofia only.
- NY allocation: 181 resident days; both spouses' wages 100% NY source under convenience-of-the-employer; **NY tax itself is stated as not computable from the library** rather than estimated.

`STATUS.md` remains **COMPLETE WITH OPEN ITEMS**. The nine client questions in `QUESTIONS.md` are still open — when the scripted replies arrive, the figures to watch are prior-year basis (Q1), Form 8332 for Leo (Q2), post-June coverage (Q3), 8962 family size (Q4), NY day counts (Q5), and the Brooklyn rent/market-rate facts (Q6); any of those could move basis, dependents, repayment, or the rental allowance.