The client replies close several assumptions — and one reply prompted me to re-verify the 8962 repayment bands against the library, where I find an error in my own first-pass figures. Let me re-check carefully:

JSON is corrected. Now let me read the current markdown deliverables to apply the matching edits.

Now applying the matching edits to `return.md`:

Let me re-verify the library cap-table text to be certain of the correction, and read the remaining deliverables:

Now adding the repayment-cap correction as its own judgment entry (#14), and reading `QUESTIONS.md` to record answers:

All deliverables are now consistent and every arithmetic identity re-verifies (assertions pass; JSON keys match the CONTRACT schema exactly).

## What changed this round

**One real correction (my error, caught on re-reading the library):** the 8962 repayment cap. Household income is 292.79% FPL → the **200%–<300% band → $1,900 cap** (`form8962_instructions_excerpt.md`, line 14), not the $3,150 figure I first used (that's the 300%–<400% band). So:

- Excess APTC $2,368.74 → **repayment $1,900** ($468.74 of the excess is *not* repayable)
- Form 1040 line 17: 2,369 → **1,900** · total tax: 6,877 → **6,408** · refund: 1,853 → **$2,322**

This is documented transparently in `judgment_calls.md` #14 and `STATUS.md`, not silently patched.

**Client answers applied (no re-asks):**
- **Leo:** 8332 signed to the father — his year (the `{TY}` placeholder read as 2025). Leo not claimed; CTC = Sofia only. 8962 family size stays 4: the library's only FPL line is keyed to "2025 **coverage**" (the 4-person policy). The family-of-3 alternative stays labeled, bounded but not computed (repayment would rise to $2,500.50–$3,150 — ≥$600 more).
- **Tenant:** unrelated (broker-sourced nurse, 2019), rent never raised → §280A(d)(2)(C) carve-out confirmed; rental loss allowed.
- **S-corp:** no contributions since 2021, no shareholder loans, Pike guarantees the line → debt basis $0 confirmed.
- **NY:** both remote moves were employer-permitted, not employer necessity → convenience-of-the-employer rule confirmed; all $122,000 wages stay NY source.
- **Coverage:** marketplace plan dropped 7/1 → 6-month 8962 confirmed.

## Final numbers
AGI $91,350 → TI $59,850 → tax $6,708 → CTC −$2,200 → 8962 repayment +$1,900 → **total tax $6,408, refund $2,322**.

## Still open (client has no further information)
1. $11,500 opening basis rests solely on Marcus's note — no prior K-1s/7203s exist to verify it.
2. Written Brooklyn lease never produced — "fair rental for that lease" rests on the client's account.
3. Family-of-3 FPL figure absent from the library — sensitivity bounded, not booked.
4. NY tax uncomputable from the closed library (no rate schedule); NY prep scope unanswered.

`STATUS.md` reads **COMPLETE WITH OPEN ITEMS**.