# Judgment calls — decisions made and alternatives rejected

Each entry: the decision, why, and the alternative rejected. Library authority cited where the
library resolves the point; otherwise flagged as judgment/assumption.

1. **S-corp loss limited to basis ($11,500 of $28,000).** Marcus expects the loss to "come
   straight off" income. Rejected: deducting the full $28,000. `form7203_instructions_excerpt.md`
   — allowed only to the extent of adjusted stock + debt basis; excess suspended.
2. **Basis ordering (income first, then distributions, then losses).** Used the excerpt's stated
   order to roll the basis forward (2023: 14,300 + 9,800 − 12,000 = 12,100). Rejected: netting
   year-by-year in a different order (e.g., reducing basis by distributions before adding current
   income), which could distort whether a distribution ever exceeded basis. No material difference
   arises here because only 2025 carries a loss.
3. **No debt basis.** The company's bank line is personally guaranteed **by Pike**, and Marcus
   never made a direct loan. Rejected: treating the guarantee as debt basis (would have allowed
   more of the loss). `form7203_instructions_excerpt.md` is explicit: a guarantee does not create
   debt basis.
4. **No prior-year suspended loss carried into 2025.** The 2021 loss (2,100) was within the
   $10,000 contribution basis; every later year had positive income or distributions only.
   Rejected: assuming an unexplained carryforward. Marcus's note covers 2021–2025 completely.
5. **Below-market rent kept as rental, loss preserved.** $1,500/mo vs ~$2,600 market to an
   unrelated 6-year tenant, "never raised." Chose fair-rental-for-that-lease treatment, so the
   $21,018 Schedule E loss stands. Rejected: §280A(d)(2)(C) personal-use recharacterization (rented
   below fair rental value to anyone converts days to personal use and **no loss** would be
   allowed). `form8582_instructions_excerpt.md` — never having raised rent to an unrelated tenant
   "does not by itself trigger this rule if the rent is a fair rental for that lease." Risk noted in
   STATUS: documentation of the lease/market comparables would firm this up.
6. **Active participation established from the file.** Elena "handles everything herself." This
   unlocks the $25,000 §469(i) allowance. Rejected: classifying the rental as fully passive with no
   allowance (would have suspended all $21,018).
7. **§469 MAGI includes the basis-allowed S-corp loss.** MAGI = 122,400 − 11,500 = 110,900.
   Rejected: MAGI before the S-corp loss (122,400), which would have shrunk the allowance to
   25,000 − 0.5×22,400 = 13,800 — a $5,750 swing in allowed loss that would also have pushed AGI
   (~108,600) into the 300–400% FPL band on Form 8962 (lower PTC, repayment band cap $3,150),
   materially changing lines 11–34. `form8582_instructions_excerpt.md`
   states expressly that a nonpassive S-corp loss (material participation), to the extent allowed
   by basis, **does** reduce MAGI.
8. **S-corp loss treated as nonpassive.** Relied on K-1 Part II G ("Shareholder materially
   participates: Yes"). Rejected: defaulting the rental-like treatment where the §469(i) allowance
   would also have to juggle the S-corp loss.
9. **Leo not claimed in 2025.** The 2019 stipulation alternates: father claims odd years.
   Rejected: claiming Leo anyway because he "resides primarily with the Mother" (custodial parent
   normally claims, but the alternating agreement controls; and a child released on Form 8332 is not
   the other parent's qualifying child for CTC). `1040_instructions_tax_computation.md`. Leo **is**
   still counted in the 1095-A household (he's covered) and the library gives the family-of-4 FPL.
10. **CTC $2,200 = Sofia only.** Consequence of #9.
11. **Whole-dollar reporting** (e.g., depreciation 9,818.18 → 9,818; PTC 7,531.25 → 7,531).
    Assumption: standard IRS rounding; the library is silent. Effect ≤ $1; the repayment cap makes
    the 8962 outcome insensitive to it.
12. **8962 MAGI vs §469 MAGI are different numbers on purpose.** 8962 household income = AGI
    91,350 (the rental loss is *in* AGI); §469(i) MAGI = 110,900 (rental loss excluded). Rejected:
    using one figure for both. Each definition quoted from its respective excerpt.
13. **PTC computed monthly × 6 covered months.** The library defines the **monthly** PTC; the
    1095-A shows Jan–Jun and 6× monthly totals; employer coverage (W-2 DD 7,140) covered Jul–Dec.
    Rejected: annualizing the SLCSP formula over 12 months (would overstate the credit ~×2 and was
    never right anyway — only 6 months are covered).
14. **Repayment capped at $1,900**, not the full $2,369 excess — income at 292.79% FPL falls in the
    MFJ 200–<300% band. Rejected: paying the uncapped excess, and (separately) any thought of a
    "400% cliff" — not applicable below 400%. `form8962_instructions_excerpt.md`.
15. **Standard deduction ($31,500).** Identifiable itemized deductions (1098 mortgage interest
    $6,480 + NY income tax withheld $6,752 + unknown Tampa property tax) cannot reach $31,500.
    Rejected: itemizing. (SALT cap rules are not in the library — noted, immaterial here.)
16. **Tax from the Tax Table, not rate schedules.** TI $59,850 < $100,000 → Tax Table mandatory;
    used row 59,850–59,900 → $6,708. Rejected: straight rate-schedule math (gives $6,705 — $3 low;
    the table brackets' midpoint method governs). `1040_instructions_tax_computation.md`,
    `tax_table_2025_excerpt.md`.
17. **NY resident period ended July 2 (183 days).** Facts: lease ended June 30 ("out by then"),
    nights of June 28–30 at mother's **in Queens**, closed on Tampa **July 3**, moved in "that
    weekend." Rejected: (a) June 30 / 181 days — domicile is abandoned when a new one is acquired,
    and they remained physically in NY July 1–2; (b) July 3+ / 184–186 days — a day-count over 183
    is irrelevant here anyway because no NY permanent abode was maintained after June 30, so
    statutory residency doesn't attach regardless. Chose the date new domicile was legally acquired
    minus one (last full day in NY).
18. **All wages NY-source for the whole year (convenience of the employer).** Both employers are
    NYC-based; Marcus "just works remotely," Halvorsen "let me go fully remote" — permission, not
    necessity; no evidence of employer-required out-of-state workdays. Rejected: treating post-move
    wages as non-NY source (excluded only for work out of state "for the employer's necessity").
    `ny_it203_part_year_excerpt.md`. Consequence: the 183-vs-181 day choice doesn't move tax;
    NY withholding was plausibly correct all year, and only the ~$200 of allocated interest differs
    across day-count variants.
19. **Both spouses MFJ for NY part-year** (one IT-203 combined allocation). Assumption — the
    library excerpt is silent on filing-status interaction; MFJ at the federal level drives the
    same NY status absent contrary authority. Flagged as unverified.
20. **No QBI line reported.** The contract schema omits Form 1040 line 13; in any case the S-corp
    produced a net loss (a negative QBI component wouldn't yield a 2025 deduction), and no §199A
    authority exists in the library. Noted, not forced.
21. **1095-A "months 21–26 / 33" column labels** in the PDF are artifacts of the simulated
    substitute statement; treated coverage as Jan–Jun from the explicit "January–June" row and the
    6× totals cross-check. Rejected: reading "21–26" as months of coverage (would contradict the
    monthly totals and the W-2 DD employer-coverage code).
