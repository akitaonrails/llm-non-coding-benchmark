Final consistency pass is done. The last residual wording issue is fixed and the four deliverables now tell one consistent story.

## What changed in this pass

**`deliverable/opinion.md` §6(b)** — the $1.2M refinancing distribution is now described as explaining why the *capital account* is negative, not as explaining part of the $1,760,000 reconciliation difference. The stale `$560,000` residual (which only made sense if the distribution partially explained the gap) is gone, and the reasoning is stated: a distribution out of a disregarded entity moves cash out and reduces the capital account equally, changing neither inside basis nor the +$1,380,000 assets-minus-liabilities figure — so it cannot close the gap at either end. `STATUS.md` item 2 and `opinion.md` §8.7(1) were aligned to the same formulation.

Also completed in this pass:
- §7 "not verified" list extended to 11 items — added the M&A/deal-structure unknowns (item 9), the per-issuer cap mechanics question worth up to $9,988,000 (item 10), and **G1**, whether the steps were already executed per the 2025-11-04 "Step 1: Wyoming" note (item 11).
- Stale question pointers replaced with the current `QUESTIONS.md` numbering: `R1(1)` (gross-asset support), `R1(4)` (ROFR/transfer restrictions), `R2(1)` (CPA records for the gap).
- Cross-references corrected: §8.1 row 2 and §8.2 consequence 2 now point to §8.7 (not §8.5); §8.5 has six hard rules, so the §8.5(5) cite in `agreements_required.md` item 43 resolves.
- Mortgage payoff now presented on **both branches** (opinion §8.7, `numbers.json` → `mortgage_payoff_after_exit`, agreements item 7b): partnership branch = $1,881,000 §752(b) shift vs basis $5,161,000 / $3,401,000 → `max(0, …) = $0`; disregarded branch = §752/§731 inapplicable, no deemed distribution to test. No gain either way.
- Citation hygiene tightened: no out-of-library code section is named even inside a disclaimer, except the 2020 §83(b) election, which is a *document* recited in the SPA.

## Verification run

- All four tables files: column counts consistent, no malformed rows.
- `numbers.json` valid; required keys present: `qsbs_exclusion_at_risk` 9,388,000 (range 8,988,000–9,988,000), `imputed_interest_annual` 22,660 (conditional, $0 if the entities stay disregarded), `properties_contribution_gain_estimate` 0.
- Every statutory cite in the deliverables maps to one of the five files in `library/`; all five are cited; none invented.
- Arithmetic re-checked: gift-shift breakpoint 0.79 × 1,900,000 = 1,501,000; a 99% transfer produces exactly 380,000 of §731(a) gain on reading B — which equals negative tax capital exactly, since gain = 0.99D − (TC + 0.99D) = −TC.

## State

`STATUS.md`: **COMPLETE WITH OPEN ITEMS**. Nothing further can move without third parties — G1 (were the steps executed?), then R1 (Helio records incl. deal structure), R2 (CPA), R3 (lender), R4 (§1202 specialist on cap mechanics), R5 (estate counsel), R6 (rates/Colorado conformity). The $1,760,000 balance-sheet gap stays deliberately unforced, with outside basis carried as two readings (A $3,280,000 / B $1,520,000).