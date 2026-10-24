# STATUS: COMPLETE WITH OPEN ITEMS

All required deliverables are in place:

- `return.json` — federal 1040, Form 7203, Form 8582, Form 8962, dependents, NY part-year fields
- `return.md` — arithmetic and library authority for every figure
- `judgment_calls.md` — every decision point with the alternative rejected
- `STATUS.md` — this file

No `QUESTIONS.md` was needed: every fact material to the requested deliverables is in
the client file, and the one gap below does not block the federal return or the
requested NY fields (residency days, per-spouse NY wages, method).

## Open items

1. **NY — source of the $400 interest (Chase 1099-INT).** The statement does not state
   the payer's location or the date(s) the interest was credited. It does not affect the
   federal return. For a full IT-203, any interest received **after 6/30/2025** must be
   sourced (NY vs other) before the nonresident-period allocation is finalized;
   interest received during the 1/1–6/30 resident period is NY income regardless of
   source. Flagged in `return.md` §6.
2. **Carryforwards to track for 2026** (informational, not a deliverable): suspended
   S-corp loss **$16,500** (Form 7203, usable as basis is restored) and passive rental
   loss **$1,468** (Form 8582 Part VII, subject to next year's special-allowance phase-out).
3. **Lease document not in file** (minor): the below-market-rent judgment
   (`judgment_calls.md` item 2) rests on `rental_summary_brooklyn.md`, which states the
   lease is "attached to prior-year file." The conclusion (bona fide lease to an
   unrelated tenant) is unchanged; obtain the lease only if the client wants the
   analysis re-verified against the actual lease terms.

## Pre-delivery review

Full re-verification from raw document values (Python): 7203 basis chain (11,500 →
11,500 allowed / 16,500 suspended); 8582 (expenses 29,200; loss 21,018; MAGI 110,900;
phase-out 5,450; allowance 19,550; carryforward 1,468); 1040 chain (AGI 91,350;
TI 59,850; tax 6,708; total tax 8,608; withholding 8,730; refund 2,322); 8962
(292.79% FPL; 5.7115% applicable figure; PTC 4,923; excess 4,977; cap 1,900);
1095-A annual totals = 6 × monthly premiums (Jan–Jun coverage); 181 resident days.
**All figures reconcile; no numeric errors found; no numbers changed.**
Documentation fixes applied during the review:

- `return.md` §3: noted that line labels follow the CONTRACT.md schema (official form
  line numbers can differ) and that the itemized comparison is a document-amount
  sanity check, not a library-cited computation (the library has no itemized rules).
- `return.md` §4: noted the 1095-A shows 6 months of coverage (Jan–Jun; annual totals
  = 6 × monthly), consistent with the July move; PTC computation unaffected.
- `return.md` §4 / `judgment_calls.md` item 7: removed the unsupported "form
  convention" phrasing; rounding is immaterial given the $1,900 cap.
- `judgment_calls.md` item 2: noted the lease document is not in the file (the call
  rests on the rental summary).

## Headline results

- 2025 loss deduction: **$11,500** of $28,000 (basis-limited); **$16,500** suspended
- Rental loss allowed: **$19,550** of $21,018 (special allowance $25,000 − $5,450 phase-out); **$1,468** carried forward
- AGI **$91,350**; taxable income **$59,850**; tax **$6,708** (2025 Tax Table, MFJ)
- PTC: annual **$4,923** vs APTC **$9,900** → excess $4,977 capped at **$1,900** repayment
- CTC **$2,200** (Sofia only — Leo is the father's in odd years per the custody decree)
- **Refund: $2,322**
- NY: part-year resident, 181 days; 100% of both W-2s is NY-source (convenience of the employer)
