# STATUS: COMPLETE WITH OPEN ITEMS

All required deliverables are present: `return.json`, `return.md`, `judgment_calls.md`,
`QUESTIONS.md`, `STATUS.md`. Round-1 questions are answered; no figures changed as a result — the
answers **confirm** the below. Internal reconciliations (AGI, taxable income, total tax, refund,
Sch 1 = allowed S-corp + rental amounts, 8962 repayment = Form 1040 line 17) all check out. A
pre-delivery audit re-derived every figure from the source documents and the library: all
reconciliations pass; corrections were labeling/authority fixes in the write-ups plus one
precision change (`applicable_figure_pct` in `return.json` now carries the interpolated
5.7115385% so the PTC of 7,531.25 reproduces exactly). No dollar amounts on the return changed.

Headline: AGI $91,350; taxable income $59,850; total tax $6,408; refund **$2,322**. Marcus's
$28,000 S-corp loss is **not** fully deductible — only $11,500 against current basis; $16,500 is
suspended (Form 7203).

Closed by client answers (previously open, now confirmed): Leo not claimed / 8332 signed for the
father's 2025 year; below-market-rent facts (unrelated tenant since 2019, rent never raised); no
shareholder loans and Pike's bank-line guarantee (debt basis $0); both spouses' remote work is
employee convenience, so full-year wages are NY source on IT-203; file is complete as to payments
and other items (withholding $8,730 is the only federal payment).

## Open items (none block filing the federal return as prepared)

1. **Form 8962 family size / FPL — reference gap; the only item that can move a federal figure.**
   Computed with the library's only FPL (family of 4, $31,200 → 292.79% FPL → repayment capped at
   $1,900). If the correct family count is 3, the applicable FPL is **not in the library** and was
   not assumed; the repayment could rise from $1,900 to as much as **$3,642.38** (uncapped at
   ≥400% FPL), cutting the refund from $2,322 to as low as **$579.62**. Flagged, not hidden;
   resolving it requires sources outside the closed library.
2. **NY tax amount not computed — reference gap (IT-203 only).** No NY rate schedule in the
   library. Inputs are final: 181 resident days; NY wages $68,000 / $54,000; NY withholding
   $6,752; Brooklyn rental taxed at least on the resident-period portion (the general rule that NY
   real-property income is NY source is not in the library — unverified context, not cited).
   Federal return unaffected.
3. **Supporting documents unavailable (client has none):** 2019 Brooklyn lease (supports the
   §280A carve-out facts, which are client-confirmed) and prior-year Forms 7203 (basis $11,500
   rests on Marcus's note, consistent with his confirmed no-loans/no-contributions answers).
4. Items believed true but **not in the library and therefore not cited** (labeled unverified
   context): deductibility of state/local taxes and the $10,000 SALT cap; CTC phase-out thresholds
   (none reached at this income) and refundability mechanics (not in play — tax exceeds the credit);
   2025 FPL amounts beyond the family-of-4 figure; NY resident tax rates; the rule that NY
   real-property income is NY source; Sch E → Schedule 1 and 8962 line-placement logistics; and the
   27.5-year depreciation convention (used as the client's own booked computation).
