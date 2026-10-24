# Judgment calls

Each entry: the decision, the authority, and the alternative considered and rejected.

## 1. S-corp loss allowed only to $11,500, not $28,000 (Marcus's "straight off" expectation)
- **Decided:** beginning 2025 stock basis $11,500; allowed $11,500; suspended $16,500. Basis
  rollforward in the order the library states: increases (contributions, income) first, then
  distributions, then losses. 2023: 14,300 + 9,800 − 12,000 = 12,100 (distributions taken *before*
  any loss adjustment matters, because 2023 had income only).
- **Authority:** `form7203_instructions_excerpt.md` — §1366(d) basis limitation; suspended losses
  carry forward indefinitely.
- **Rejected:** (a) deducting the full $28,000 (Marcus's assumption) — no basis to support it;
  (b) treating Pike's guarantee of the bank line as giving Marcus debt basis — the library is
  explicit that a guarantee creates no debt basis; only a direct shareholder loan does. Client
  confirms (round 2): Marcus never lent the corporation money (including advances) and has
  contributed nothing since the 2021 $10,000; Pike guarantees the bank line.
- **Assumption flagged:** prior-year losses (2021, $2,100) were fully allowed because each was ≤
  available basis in that year; prior-year Forms 7203 are not in the file and the client has none.

## 2. MAGI for the §469(i) phase-out includes the allowed S-corp loss
- **Decided:** MAGI = 122,400 − 11,500 = **110,900** → allowance 19,550, allowed rental loss 19,550,
  carryforward 1,468.
- **Authority:** `form8582_instructions_excerpt.md` — MAGI is AGI *without* the passive loss, and
  nonpassive losses allowed in the year (S-corp loss with material participation, to the extent
  allowed by basis) **do** reduce MAGI. K-1 Part II G shows Marcus materially participates.
- **Rejected:** (a) MAGI = 122,400 ignoring the S-corp loss (allowance would fall to 13,800) —
  contrary to the express library rule; (b) MAGI = AGI including the rental loss (91,350 → full
  25,000 allowance) — the library requires MAGI to be figured *without* the PAL.

## 3. Below-market rent on the Brooklyn condo — allowance preserved, not a §280A personal-use trap
- **Decided:** the $1,500/month rent (market ~$2,600) does **not** convert the rental days to
  personal-use days; the 21,018 loss stands and the special allowance applies.
- **Authority:** `form8582_instructions_excerpt.md` §280A(d)(2)(C) excerpt — renting below market to
  an *unrelated* tenant because rent was never raised does not by itself trigger the personal-use
  rule "if the rent is a fair rental for that lease." Client confirms (round 2): the tenant is a
  stranger — a nurse found through a broker in 2019 — and they "just never raised the rent." The
  facts now match the library's carve-out precisely (unrelated tenant, stale rent, same lease 6 years).
- **Rejected:** treating every day as personal use and disallowing the entire loss (and its
  deductions) — the library's carve-out fits these facts, now client-confirmed. Residual risk: the
  "fair rental for that lease" conclusion is supported by the client's account but the 2019 lease
  copy is not in the file and the client has no copy; it is a supporting-document gap, not a
  fact gap.

## 4. Leo Castellano not claimed in 2025
- **Decided:** dependents = Sofia only; CTC = $2,200 (one child).
- **Authority:** `1040_instructions_tax_computation.md` — where a decree or agreement alternates
  years, the agreement controls; a child claimed by the other parent under a Form 8332 release is
  not your qualifying child for the CTC. Custody agreement: father claims **odd** years; 2025 is odd.
- **Rejected:** claiming Leo because he is the custodial parent's child (he "resides primarily with
  the Mother") — the alternating agreement overrides the default custodial rule, and the mother must
  execute Form 8332 for the father's years.
- **Client confirmation (round 2):** Elena signed Form 8332 for Leo's father for 2025 ("it's his
  year"). Her message contained a year placeholder ("{TY}"); read as 2025, the odd year the
  agreement assigns to the father — consistent with the agreement and with Leo being absent from
  this return.

## 5. 8962 family size / FPL — used family of 4
- **Decided:** household income 91,350 ÷ FPL 31,200 (family of 4) = 292.79% → applicable figure
  5.71%, annual PTC 7,531.25, excess 2,368.75, repayment limited to $1,900 (200–<300% band).
- **Authority:** `form8962_instructions_excerpt.md` — FPL of $31,200 for family of 4 is the only
  FPL figure in the library; the repayment bands are given for MFJ.
- **Rejected:** treating the household as 3 for poverty-line purposes (Leo lives there and was on
  the policy, but is *not* claimed as a dependent on this return). The library does not define the
  family-size rule, and no family-of-3 FPL is in the library. **Any family-of-3 figure I believe to
  be correct is NOT in the library and is therefore unverified — not cited.** The client was asked
  and has no further information, so this is now a reference gap, not a fact gap.
- **Quantified sensitivity (library bands only, household income fixed at 91,350):**
  - 200–<300% band requires FPL > $30,450; the family-of-4 figure ($31,200) sits there → cap $1,900.
  - A smaller FPL below $30,450 puts income at ≥300% (cap $3,150) and *also increases the excess*
    (applicable figure rises): at the 300% boundary the excess is $2,500.50 — fully repayable.
  - At FPL ≤ $22,837.50 (income ≥400%) there is **no cap**; the excess maxes at $3,642.38.
  - Effect on the refund (dollar-for-dollar): $2,322 → as low as $579.62.
- **Not stated as law:** 2025 FPL amounts other than the family-of-4 figure, and any household-size
  definition, are outside the library; treated as the sole remaining figure-affecting open item.

## 6. NY residency window — resident period Jan 1–Jun 30 (181 days)
- **Decided:** resident 181 days; nonresident 184 days (Jul 1–Dec 31).
- **Authority:** `ny_it203_part_year_excerpt.md` — part-year taxation; allocation by resident-period
  days.
- **Rejected:** ending the resident period at 7/2 (184 days), i.e., through the Tampa closing — the
  Brooklyn lease ended 6/30 and the client email says they "were out by then"; the 6/28–30 nights
  at Elena's mother's in Queens are temporary lodging *inside* the chosen window and do not extend
  it; 7/1–7/2 were travel days with no NY abode.

## 7. Convenience of the employer applied to BOTH spouses' full-year wages
- **Decided:** Marcus NY wages $68,000; Elena NY wages $54,000; both treated as NY source all year.
- **Authority:** `ny_it203_part_year_excerpt.md` — wages paid by a NY employer to an employee
  working out of state for the employee's own convenience are NY source; only days worked out of
  state for the *employer's necessity* are excluded.
- **Rejected:** excluding Jul–Dec wages from NY source (ratio allocation of wages 181/365). Client
  confirms (round 2) both arrangements were employee-initiated accommodations: Marcus asked to move
  and was told remote was fine ("they didn't need me out of state"); Halvorsen closed its Tampa
  office years ago and approved Elena's request. No employer-necessity facts exist, so the
  necessity branch is closed and the convenience-of-the-employer rule applies to both spouses.
- **Note:** both employers left NY withholding on full-year wages; on IT-203 the excess is refunded
  (library: withheld in excess of tax due is refunded on IT-203). Federal line 25d uses full federal
  withholding ($8,730) regardless.

## 8. Standard deduction, not itemized
- **Decided:** $31,500 standard MFJ.
- **Authority:** `1040_instructions_tax_computation.md`.
- **Rejected:** Schedule A — mortgage interest 6,480 + state income tax withheld 6,752 ≈ 13,232,
  far below 31,500 even before any SALT-cap question. (The $10,000 SALT cap is **not** in the
  library and is therefore not cited; the comparison holds with or without it.) Brooklyn property
  tax belongs on Schedule E, not Schedule A. Tampa property tax is not in the file — it could not
  change this outcome.

## 9. Rental activity characterization
- **Decided:** passive rental with **active participation** (special allowance available), not
  material participation.
- **Authority:** `form8582_instructions_excerpt.md` — special allowance requires active
  participation; Elena "handles everything herself (approves tenants, arranges repairs)," which
  supports active participation. No facts support treating her as a real estate professional, which
  was the alternative considered (none; there is no such rule in the library).

## 10. Depreciation and cents
- Used the file's own $9,818 (270,000 ÷ 27.5 = 9,818.18) for the Sch E figure to keep the return
  consistent with the client's summary; the 18-cent difference does not move any line.

## 11. 1095-A coverage months vs. W-2 box 12 DD
- Used Jan–Jun coverage from the 1095-A (6 monthly figures × the stated annual totals reconcile:
  6 × 1,720 = 10,320; 6 × 1,690 = 10,140; 6 × 1,650 = 9,900) and noted Elena's W-2 DD code 7,140
  for "Jul–Dec employer coverage" corroborates marketplace coverage ending 6/30. No judgment
  divergence; recorded because the monthly PTC is computed month-by-month.
