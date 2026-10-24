# Status — Reyes 2025 federal + NY delivery

**COMPLETE WITH OPEN ITEMS**

Deliverables: `return.json`, `return.md`, `judgment_calls.md` all present; all figures recomputed with Python and shown with arithmetic and library citations (`return.md`).

Client question on the S-corp suspension (Marcus, 10/23/2026) answered and documented in
`judgment_calls.md` §11: **no change to any figure** — Pike's guarantee creates no debt basis and
$16,500 remains suspended.


## Open items (do not affect the figures as filed unless noted)

1. **§199A/QBI deduction — unverified, not applied.** Nothing in the library addresses the QBI
   deduction. With a basis-allowed K-1 loss the QBI component would likely be negative (deduction 0
   this year), but that is general knowledge, **not** library authority, so no figure was changed.
2. **Prior-year unallowed rental losses assumed none.** Form 8582 carryforward tagging (the 1,468)
   could shift if suspended losses exist from earlier years; AGI/tax are unchanged either way
   (the 19,550 allowance reduces AGI regardless of loss vintage).
3. **Form 8332 for Leo for 2025** should be executed by Elena (custodial parent) and sent to the
   father per the custody stipulation — required filing-grade document, not yet on file.
4. **NY state tax amount not computed.** The library's IT-203 excerpt covers the part-year
   sourcing/allocation method only; NY rate tables are outside the library. NY withholding
   (6,752) versus the IT-203 liability (on 100%-allocated NY wages) is therefore unreconciled — the
   1098/1095-style refund-twist ("tax withheld in excess of tax due is refunded") cannot be tested.
5. **Rental depreciation/basis and expense records unverified.** Building basis 270,000 and no land
   split come only from Elena's summary (no condo closing statement; no Brooklyn 1098 in the
   file); depreciation used 9,818 vs unrounded 9,818.18 (immaterial; carryforward ±0.18). The
   expense list itself likewise rests on Elena's summary: disallowance of any single expense
   exceeding the 1,468 cushion between the loss (21,018) and the allowance (19,550) would change
   the allowed loss.
6. **Assumptions on the record:** no federal estimated payments; no income/credit items beyond the
   documents in `documents/`; SALT-cap existence is outside the library (unverified) and immaterial
   here (itemized ≈ 13,232 < standard 31,500).

## Headline results

- AGI **91,350**; taxable income **59,850**; tax (Tax Table) **6,708**; CTC (Sofia) **2,200**;
  total tax **6,408**; withholding **8,730** → **refund 2,322**.
- S-corp: loss allowed **11,500**, suspended **16,500** (Marcus's "straight off" expectation is
  corrected by the basis limitation).
- Rental: loss **21,018** → allowed **19,550** (special allowance after MAGI 110,900 phase-out),
  carryforward **1,468**.
- PTC: household income 91,350 = 292.79% FPL, figure 5.71%, annual PTC **7,531** vs APTC **9,900**
  → excess **2,369**, capped repayment **1,900**.
- NY: 181 resident days; both spouses' wages 100% NY source under the convenience-of-the-employer
  rule (Marcus 68,000; Elena 54,000).

## Delivery review (10/23/2026) — changes made

Full re-check before delivery: every figure re-verified against the documents and library; JSON
re-parsed and cross-checked. Changes below — none changed a filed figure (only a display rounding
in `return.md` was corrected):

1. `return.json`: removed the extra `conventions` object so the shape matches the spec exactly;
   the sign convention moved to `return.md`.
2. `return.md` §8962: annual contribution shown correctly as 5,217.49 (had been displayed as
   5,217.50; monthly 434.79 and every filed figure unchanged); added the whole-dollar per-month
   rounding check (7,530 PTC / 2,370 excess → same capped 1,900) and a note that Elena's W-2 DD
   employer coverage (Jul–Dec) overlaps no marketplace-coverage month.
3. `return.md` §7203: reworded — prior distributions confirmed against basis; removed the
   unsupported claim that they would be "taxable gain" (that rule is not in the library).
4. `return.md` line 12: reworded the SALT clause — no SALT-cap rule exists in the library; the
   standard-deduction outcome holds with or without one.
5. `return.md` §NY: replaced the form name "IT-203-B" (not in the library) with the excerpt's own
   wording, "attach the allocation schedule."
6. `judgment_calls.md` §2: reworded the tenant point (removed the unclear "sole interest" phrase);
   added the expense-records caveat (no Brooklyn 1098; disallowance of any single expense over
   1,468 would change the allowed loss).
7. `judgment_calls.md` §9: added the whole-dollar rounding alternative to the precision note.
8. `judgment_calls.md` §11: corrected the client-pushback arithmetic, which was garbled as
   displayed; now reads (2,100) + 6,400 + 9,800 + 4,600 = 18,700 net income; 10,000 + 18,700 −
   17,200 = 11,500; without distributions 10,000 + 18,700 = 28,700 ≥ 28,000.
9. `STATUS.md`: open item 5 extended to the expense records; this review list added.
