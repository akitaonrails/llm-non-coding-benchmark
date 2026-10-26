# STATUS — Reyes 2025 engagement

**COMPLETE**

All deliverables final: `return.json`, `return.md`, `judgment_calls.md`, `QUESTIONS.md` (now an answered-question log).

Client-turn effects: Marcus's and Elena's relocations are both employee-requested/employer-approved → both spouses' full-year wages are NY source under the convenience-of-the-employer rule; Elena's NY wages corrected from $26,690 (withdrawn workday assumption) to **$54,000**. The Form 8332 for Leo is confirmed signed for 2025. **No federal figure changed** — line 34 refund stands at $2,322.

Remaining unknowns (deliberately not resolved; none is in the library, none changes a delivered figure):

1. **NY tax due / NY refund** cannot be computed — the library contains no New York rate or tax table. Wage-source and withholding figures (6,000-range: 3,842 + 2,910 = 6,752 NY withheld) are final for allocation purposes.
2. **Unverified law, flagged instead of cited** (`judgment_calls.md` §11): SALT item cap; CTC phase-out thresholds; Schedule 8812 refundable-credit mechanics; NY-source treatment of the Brooklyn condo's Jul–Dec rental income for the IT-203 nonresident column (real-property-source rule not in `ny_it203_part_year_excerpt.md`). The contract's NY output block has no rental field, so nothing delivered depends on it.
3. **Completeness of the client file** — the client states they have no additional information, so the return assumes no undocumented 2025 items (1099-DIV/1099-G, HSA, student loan interest, charitable gifts, Tampa property tax bill). If any surface before filing, revisit lines 8/12 and the itemized-vs-standard comparison.
4. Minor: rental depreciation taken at the client's rounded $9,818 rather than $9,818.18; PTC fractions shown rounded to whole dollars in `return.json` with unrounded arithmetic in `return.md`.

## Final review (pre-delivery self-check)

A full self-review pass was run before delivery: every delivered figure re-verified against fresh source re-extractions (`pdftotext -layout`) and Python recomputation; every citation checked against `../library/INDEX.md`; non-reconciling items traced. Changes made (all narrative/presentational — **no delivered figure changed**):

1. **`judgment_calls.md` §1** — corrected the rejected-counterfactual arithmetic for the full $28,000 S-corp loss (previous text was wrong): it would put MAGI at $94,400 (under the $100,000 line), so the full $25,000 special allowance would apply and the entire $21,018 rental loss would be allowed; AGI $73,382 (cut of $17,968, not $16,500); household income ≈ 235% FPL so the PTC would rise materially. The rejected conclusion (basis rule limits the loss to $11,500) is unchanged.
2. **`judgment_calls.md` §8** — corrected the rejected-alternative arithmetic: stripping the allowed S-corp loss from MAGI gives MAGI $122,400 → special allowance 25,000 − 50%×(122,400 − 100,000) = **$13,800** (was misstated as 16,750); AGI would be $97,100.
3. **`judgment_calls.md` §2** — removed a stray word ("intern") from a rejected-alternative note.
4. **`judgment_calls.md` §3 / `return.md` / `return.json` `ny.method`** — added the corroborating source facts: both employers are New York entities (Reyes & Pike: 1 Liberty Plaza, NYC; Halvorsen: 230 Park Ave S, NY) and both W-2s report full-year box 16 NY state wages ($68,000 / $54,000). Wording only.
5. **`return.md` PTC block** — showed the exact unrounded chain (292.788…% FPL → applicable figure 5.711538…% → 5,217.49/yr → 434.79/mo → 1,255.21/mo → 7,531.25 ≈ 7,531; excess 2,368.75 ≈ 2,369 → capped at 1,900). Presentation only.
6. **`return.md`** — typo fix ("exemption's" → "excerpt's") and "superceded" → "superseded".

Re-verified after the review: tax $6,708, repayment $1,900, total tax $6,408, withholding $8,730, **refund $2,322**; allowance $19,550 / carryforward $1,468; basis $11,500 allowed / $16,500 suspended; NY wages $68,000 / $54,000 (box 16); deliverable JSON schema matches CONTRACT.md. All citations resolve to the six indexed library files; all flagged-unverified items are labeled, not cited. Still unknown (unchanged): NY tax/refund amount — no NY rate table in the library.
