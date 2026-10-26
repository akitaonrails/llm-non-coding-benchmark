# Status

COMPLETE WITH OPEN ITEMS

Deliverables present: `division.json`, `child_support.json`, `advice.md`, `QUESTIONS.md` (now an answers log + flagged-unknowns register, per client instruction not to re-ask). All citations restricted to `library/INDEX.md` items; every calculation shown in the deliverables; nothing forced to balance.

Round-2 client input incorporated:
- **Overnights confirmed:** 255/yr with Wife = 69.9% (≥65% residential-parent threshold met; Husband 110 nights = 30.1% < 35%, no shared-parenting adjustment). `child_support.json` and `advice.md` §7 updated from estimate to confirmed counts.
- **Refinance capacity answered by math:** $400k refinance on $72k salary fails underwriting in every scenario (housing ratio 58.7% salary-only; 43.8% with child support; 35.1% only while maintenance runs, which ends at month 36). Therefore **Alternative C is now the PRIMARY recommendation** and is structured so **no refinance is required** (loan stays joint, both names on title, two stacked §121 exclusions at the later sale). Alt B (sell now, joint $500k exclusion) is the fallback if Husband refuses to remain on loan/title.
- **Bonus history:** client reports Husband "always gets a bonus," 2025 ≈ $40,000 — treated as corroboration, NOT guideline income (guidelines require employer documentation); subpoena path for 2023–2025 W-2s/plan statements flagged in `division.json` and `child_support.json`.

Round-3 client pushback ("his lawyer says exactly 50/50 / biggest asset") addressed in `advice.md` §2A: face-value vs after-tax halves (770,000/770,000 vs 613,008/662,000), the house's gross-vs-net value (543,008 realizable), equitable ≠ equal + Rule 16.2(e) leverage, and why Alt C costs Husband ~$1,000 on paper while lifting Wife $613,008 → $661,004. No figures changed.

Round-4 pre-delivery audit (review for errors, unsupported authority, reconciliation): full library re-read — every citation traced to a file in `library/INDEX.md`; full independent Python recompute of every figure (mortgage payments, housing ratios, all after-tax values, sensitivities, child support, Alternative pot, joint-sale tax saving). Core figures unchanged. Fixes applied: (1) two passages in `advice.md` §2A had attributed custody/needs factors to `columbia_equitable_distribution.md` — the library excerpt lists only economic circumstances, contributions, and tax consequences (§113(1)(d)); corrected, and the "no court evicts the kids" point is now explicitly labeled outside-library practical judgment, not cited authority; (2) §1 wording "both $250k exclusions" → the $500,000 joint-return §121 exclusion (requires both parties + joint return in the sale year); (3) sale trigger "youngest completes 6th grade" (a detail I invented, and one that fires *earlier* than the client's actual goal) → "youngest finishes middle school (client's stated 3–6-year objective; exact date a drafting choice)" in all three places; (4) Alternative A in `division.json` had a $104 asymmetry (637,556/637,452) from rounding the QDRO face to 32,300 — re-derived: half-gap 24,496 ÷ 0.76 = 32,231.58 → face 32,232, both sides ≈ 637,504, with the 64-cent whole-dollar rounding residual disclosed in the file; (5) minor precision: $2,544/yr → $2,541/yr (211.74 × 12). The ~$2,012 pay-stub residual remains deliberately open (item 1 below). Both JSON files re-validated against the CONTRACT schemas.

Open items / flagged unknowns (tabulated as U1–U11 in `QUESTIONS.md`; client has no further information on these, so they are flagged, not re-asked):
1. ~$2,012 of the 2026-09-15 pay-stub difference is unexplained by the HR bonus letter — deliberately not reconciled; needs payroll discovery.
2. 2023–2025 bonus amounts undocumented — the $40k (2025) figure is client recollection only.
3. NIIT on Wife's house-gain modeled per the engagement's stated conservative convention; her actual MAGI test unverified (sensitivities given).
4. No Columbia maintenance guideline exists in the library — $2,000/mo × 36-mo cannot be benchmarked from authority here; child-support duration/health-insurance/child-care add-ons likewise outside the library excerpt.
5. Alternative B's ~$47,000 tax saving requires Husband to agree to a joint return in the sale year; Alt C requires him to stay on the loan/title — his cooperation on each is unknown (U7).
6. Brokerage short-vs-long lot split unverified (sensitivities given); Husband's age/59½ status unknown (401(k) valuation sensitivity $630k–$710k on his side).
7. Actual property taxes/insurance unknown — placeholder $1,100/mo used in affordability math, labeled as an assumption.
8. Decree timing (final before 2026-12-31?) and Wife's >half household-cost payment for head-of-household both unverified.
