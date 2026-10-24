

Good call — let me do a systematic pre-delivery review: re-verify every figure against the source documents, check every citation against `library/INDEX.md`, and hunt for reconciliation gaps.





All arithmetic re-verified and reconciling. Now let me apply the documentation fixes I identified during the review. Let me first read the current state of the deliverables.







All checks passed and the figures reconcile. Now I'll apply the documentation fixes I identified during the review (no numeric changes needed):













All edits applied. Let me do a final verification pass — confirm every citation in the deliverables maps to a file in `library/INDEX.md` and the edited sections read cleanly:





The grep pattern for INDEX.md didn't match its format (empty second list made the cross-check meaningless). Let me read INDEX.md directly:





INDEX.md lists exactly the 6 files the deliverables cite — a perfect one-to-one match, no unsupported citations. Final check of the edited sections:






Review complete. Here's the full outcome:

## What I checked

**Arithmetic (recomputed from raw document values in Python — all passed):**
- **7203:** basis chain 10,000 − 2,100 + 6,400 + 9,800 − 12,000 + 4,600 − 5,200 = 11,500 → allowed 11,500 / suspended 16,500 (ties to the full 28,000 K-1 loss)
- **8582:** expenses 29,200 (six components sum) → loss 21,018; MAGI 110,900 → phase-out 5,450 → allowance 19,550; allowed 19,550 + CF 1,468 = 21,018
- **1040:** AGI 91,350 → TI 59,850 → tax 6,708 (row 59,850–59,900, inside the library's 59,000–61,000 excerpt) → total tax 8,608 → refund (8,730 + 2,200) − 8,608 = **2,322**
- **8962:** 292.7885% FPL → applicable figure 5.7115% → monthly PTC 410.2091 → annual 4,922.51 → 4,923; excess 4,977, capped at 1,900 (4,923 + 4,977 = 9,900 = APTC)
- **NY:** 181 resident days (1/1–6/30, non-leap year)

**Authority:** every citation in all four deliverables points to one of the 6 files in `library/INDEX.md` — the cited set and the index are an exact one-to-one match. No unsupported authorities.

**One interpretive find (no numeric impact):** the 1095-A annual totals (10,320 / 10,140 / 9,900) equal *exactly* 6 × the monthly premiums in the Jan–Jun row — i.e., coverage ran **6 months (Jan–Jun)**, consistent with the July move. The 8962 math is unaffected because the form's ÷12 × 12 mechanics cancel. Also confirmed the PTC rounding is immaterial: with the $1,900 cap, the excess is capped identically whether rounded (4,977) or not (4,977.49).

## What I found and fixed

**No numeric errors — no figures changed.** Four documentation fixes:

1. **`return.md` §3** — added a note that line labels follow the CONTRACT.md schema (on the official form, the S-corp and rental losses flow through Schedule 1 business/rental lines, and taxable interest sits on the taxable-interest line); clarified the itemized-deduction comparison (13,232) is a document-amount sanity check, not a library-cited computation — the library contains no itemized rules.
2. **`return.md` §4** — documented the 6-month (Jan–Jun) coverage finding and its consistency with the July move; noted the PTC rounding is immaterial given the cap.
3. **`judgment_calls.md` item 7** — removed the unsupported "form convention (rounding)" phrasing; the cap makes the result identical either way.
4. **`judgment_calls.md` item 2 + `STATUS.md`** — noted the lease document itself isn't in the file (the summary says it's "attached to prior-year file"); the below-market-rent conclusion rests on the summary and is unchanged. Added this as a new minor open item in STATUS.md and a "Pre-delivery review" section recording all of the above.

## Status

`COMPLETE WITH OPEN ITEMS` — unchanged, now with three open items:
1. NY source of the $400 Chase interest for the nonresident period (doesn't affect the federal return)
2. 2026 carryforwards to track: $16,500 S-corp + $1,468 rental (informational)
3. Lease document not in file (minor — obtain only if the client wants the below-market analysis re-verified)

All deliverables are ready under `workspace/deliverable/`: `return.json`, `return.md`, `judgment_calls.md`, `STATUS.md`. Headline results stand: AGI $91,350, tax $6,708, total tax $8,608, **refund $2,322**.