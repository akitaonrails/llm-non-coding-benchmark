

Running a full pre-delivery audit: contract schema, library authorities, source documents, and every computation. Starting with a complete re-read:






Contract schema matches. But `/work/deliverable` exists as well — checking whether it's the same directory or a divergent copy, then reading all sources:






Now the PDFs and remaining sources:





All figures tie so far. Now the remaining three library excerpts:





Authority texts all confirmed. Now reading both narrative deliverables in full for unsupported statements and stale figures:





All source documents, the full library, and all narrative deliverables are now re-verified line by line. The audit found five substantive problems — one wrong fact, one arithmetic garble, three statements that assert authority the library doesn't actually contain, and a stale sensitivity figure that doesn't recompute. Applying fixes now:







All three files confirmed. Now applying the remaining audit fixes — different files in parallel:








All edits applied. Now final validation — JSON parse, cross-foots, schema keys, and a stale-figure sweep:





Audit complete. Every check now passes: `return.json` parses, cross-foots, matches the CONTRACT schema key-for-key, and the full 8962 chain re-derives exactly (292.79% → 5.7115% → 434.79/mo → 7,531.26 → 2,368.74 → 1,900 cap). **No headline figure changed** — federal refund stays **$2,322.00**, status stays **COMPLETE WITH OPEN ITEMS**.

## What the audit changed

**1. Wrong fact — `return.json` dependents.** Leo was listed as "Leo Reyes (b. 2017-06-21)". The custody order says **Leo Castellano, DOB 03/14/2016**. Corrected (name, DOB, age 9). Also relabeled Sofia's entry honestly: "age 15 per client email and 1095-A; exact DOB not in file" — her exact DOB appears nowhere in the file.

**2. Arithmetic garble — `return.md` rollforward.** The 2024 basis row read "income 4,600 → 10,300… i.e. 12,100 + 4,600 = 16,700". Cleaned to "income 4,600 → 16,700; distribution (5,200) → 11,500" (12,100 + 4,600 − 5,200 = 11,500 ✓).

**3. Shown arithmetic that didn't reproduce its own answer — `return.md` 8962 step 3.** The displayed interpolation used the rounded 292.79%, which yields 5.7116%, but the result stated 5.7115%. Fixed to show the unrounded ratio (292.7885%) actually used; the filed figures were already on the exact chain and are unchanged.

**4. Stale sensitivity math — 3-person 8962 scenario (4 files).** The old "repayment ≈ 2,985 / refund ≈ 1,237 / swing ≈ 1,085" didn't recompute; correct figures are **≈ 2,989 / ≈ 1,233 / ≈ 1,089** (342.78% FPL → 7.07% applicable → 538.16/mo contribution → PTC 6,911). Updated `judgment_calls.md` #4, `return.md`, `STATUS.md`, and `QUESTIONS.md`.

**5–7. Unsupported authority relabeled (library is silent on all three):**
- **$10k SALT cap** (`return.md` line 12): removed — the cap appears in no library file. Reworded: 13,232 < 31,500 holds under *any* SALT limitation. Conclusion unaffected.
- **Gain on distributions exceeding basis** (`return.md` 7203 section): the library never states that rule. Reworded to the fact (distributions never exceeded basis, 12,000 ≤ 24,100 and 5,200 ≤ 16,700), so the question never arises.
- **NY real-property rental sourcing** (`return.md` NY section, `return.json` method, `STATUS.md`, new **judgment call #12**): the IT-203 excerpt taxes nonresidents on "NY-source income" but **never defines real-property income as NY-source**. The full-year NY sourcing of the condo rental is now explicitly an outside-library assumption. Impact: none on deliverable fields (no NY tax figure is computed; the rental loss is fully used federally).
- Bonus consistency: depreciation 9,818 now marked client-prepared in `return.md` and `judgment_calls.md` #9 (library contains no depreciation authority).

**8. `STATUS.md`** — added a pre-delivery-audit bullet under Verification notes documenting all of the above.

## What the audit verified (unchanged)

All 6 library citations resolve to `library/INDEX.md` files and quote them accurately; tax table row 59,850–59,900 → 6,708 with midpoint cross-check (2,385 + 4,323 = 6,708 ✓); MAGI 110,900 → allowance 19,550 → carryforward 1,468 ✓; withholding 8,730 federal / 6,752 NY ✓; 183 resident days ✓; schema keys match CONTRACT exactly; no stale references to any old figure remain in the deliverables.