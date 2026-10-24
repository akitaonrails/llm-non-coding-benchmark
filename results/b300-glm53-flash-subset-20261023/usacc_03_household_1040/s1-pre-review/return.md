# 2025 Form 1040 — Marcus & Elena Reyes (MFJ) — return.md

All arithmetic below was recomputed with Python; sources are the client documents in `documents/`
and only the authorities listed in `library/INDEX.md`.

## Filing status and dependents

- **Status: Married filing jointly.** Married couple living together (1040 instructions,
  `1040_instructions_tax_computation.md`, "Filing status"; status as of 12/31).
- **Standard deduction MFJ: $31,500** (same file, "Standard deduction").
- **Dependent claimed: Sofia Reyes (15).** Qualifying child, under 17 at 12/31/2025 → CTC-eligible
  (child tax credit rule, `1040_instructions_tax_computation.md`).
- **Leo (9) is NOT claimed.** Custody agreement (`custody_agreement_excerpt.pdf` ¶9): the parties
  alternate; the **Father claims Leo in odd-numbered years. 2025 is odd**, so the father
  (Mr. Castellano) claims Leo. The agreement controls for that year
  (`1040_instructions_tax_computation.md`, "Dependents — children of divorced or separated parents").
  A child claimed by the other parent under a Form 8332 release is not your qualifying child for the
  credit (same file). Consistent with that, Elena (custodial parent) should execute Form 8332
  releasing Leo for 2025 — see `judgment_calls.md`.

## Line-by-line figures

| Line | Amount | Arithmetic | Authority / document |
|---|---:|---|---|
| 1a Wages | **122,000** | 68,000 (Marcus W-2 box 1) + 54,000 (Elena W-2 box 1) | `w2_marcus_reyes_pike.pdf`, `w2_elena_reyes.pdf` |
| 2b Taxable interest | **400** | 1099-INT box 1 | `1099int_chase.pdf` |
| Sch 1 line 8 (other income) | **0** | none in file | — |
| Sch 1 items reducing AGI | **(31,050)** | (11,500) S-corp loss allowed by basis [Form 7203, below] + (19,550) rental loss allowed [Form 8582, below] | `form7203_instructions_excerpt.md`, `form8582_instructions_excerpt.md`, `k1_1120s_reyes_pike.pdf`, `rental_summary_brooklyn.md` |
| 11 AGI | **91,350** | 122,000 + 400 − 11,500 − 19,550 | — |
| 12 Deduction | **31,500** | standard deduction; itemized Alternative: Tampa mortgage interest 6,480 (1098) + NY income tax withheld 6,752 (3,842 + 2,910) = 13,232 < 31,500, so standard wins even before any SALT limitation | `1040_instructions_tax_computation.md`; `1098_mortgage.pdf` |
| 15 Taxable income | **59,850** | 91,350 − 31,500 | — |
| 16 Tax | **6,708** | Tax Table row "At least 59,850 / but less than 59,900 → 6,708". Taxable income < 100,000, so the Tax Table (not rate schedules) **must** be used | `tax_table_2025_excerpt.md`; computation rule in `1040_instructions_tax_computation.md` |
| 19 CTC | **2,200** | 1 qualifying child under 17 × 2,200 (Sofia). Leo excluded (8332 release, above) | `1040_instructions_tax_computation.md` |
| Sch 2 excess APTC (8962 line 28) | **1,900** | Form 8962 computation below | `form8962_instructions_excerpt.md` |
| 24 Total tax | **6,408** | 6,708 − 2,200 + 1,900 | — |
| 25d Withholding | **8,730** | 5,120 (Marcus W-2 box 2) + 3,610 (Elena W-2 box 2) | W-2s |
| 34 Refund | **2,322** | 8,730 − 6,408 | — |

No estimated payments appear anywhere in the file; **assumption: none were made.**

## Form 7203 — S-corp stock basis (Reyes & Pike Consulting Inc, 40%, K-1 box 1 = (28,000))

Rule (`form7203_instructions_excerpt.md`, IRC §1366(d)): losses allowed only to the extent of
**adjusted stock basis + debt basis** (stock basis increased by contributions and income, decreased
by distributions and losses, in that order); excess is **suspended and carried forward indefinitely**.
A **guarantee** of corporate debt does not create debt basis — Marcus's note says the bank line is
personally guaranteed by **Pike**, and Marcus never lent the company money, so **debt basis = 0**.

Rollover (order: contributions → income → distributions → losses):

| Year | Beginning | + Contribution | + Income/(loss) | − Distributions | Ending |
|---|---:|---:|---:|---:|---:|
| 2021 | 0 | 10,000 | (2,100) | 0 | 7,900 |
| 2022 | 7,900 | — | 6,400 | 0 | 14,300 |
| 2023 | 14,300 | — | 9,800 | (12,000) | 12,100 |
| 2024 | 12,100 | — | 4,600 | (5,200) | 11,500 |
| 2025 | 11,500 | — | | | |

Check: 10,000 − 2,100 + 6,400 + 9,800 − 12,000 + 4,600 − 5,200 = **11,500**. Prior-year
distributions never exceeded basis at the time (2023: 24,100 available vs 12,000; 2024: 16,700 vs
5,200), so no prior distributions are taxable gain.

2025 (K-1 box 16D distributions = 0, consistent with Marcus's note):

- Stock basis at 1/1/2025: **11,500**
- Loss (28,000) vs basis 11,500 → allowed = lesser = **11,500** (Part I, line 11)
- **Suspended / carryforward (line 12 et seq.) = 28,000 − 11,500 = 16,500**

Marcus expected the loss to "come straight off"; **only 11,500 of the 28,000 is deductible this
year** because of the basis limitation. Marcus materially participates (K-1 Part II G: Yes), so the
allowed loss is nonpassive and enters AGI directly.

## Form 8582 — Brooklyn rental (318 Dean St #4B)

Rental results before limitation (`rental_summary_brooklyn.md`):

- Income: rent 12 × 1,500 = **18,000**
- Expenses excl. depreciation: 11,900 + 7,860 + 5,140 + 2,350 + 1,150 + 800 = **29,200**
- Depreciation: 270,000 ÷ 27.5 = 9,818.18 → **9,818** (whole-dollar; 18¢ difference — see
  `judgment_calls.md`)
- Total expenses = 39,018 → **loss = 18,000 − 39,018 = (21,018)**

Limitation (`form8582_instructions_excerpt.md`, §469(i)): Elena actively participates (she handles
tenants, repairs herself), so the **$25,000 special allowance** applies, reduced by 50% of MAGI
over 100,000:

- **MAGI** = AGI excluding the passive rental loss, but including the nonpassive basis-allowed
  S-corp loss (per the 8582 excerpt): 122,000 + 400 − 11,500 = **110,900** (no SE/W-2 adjustments,
  IRA, or student-loan items exist here)
- Phase-out: 110,900 − 100,000 = 10,900 → reduction = 10,900 × 50% = 5,450
- **Special allowance = 25,000 − 5,450 = 19,550** (not at zero — MAGI < 150,000)
- **Allowed = min(21,018, 19,550) = 19,550** → enters AGI
- **Carryforward = 21,018 − 19,550 = 1,468**

The unused allowance itself is not carried forward; only the disallowed loss (1,468) is, to 2026
(`form8582_instructions_excerpt.md`, Part VII).

## Form 8962 — PTC reconciliation (Form 1095-A, 6 months Jan–Jun)

From `1095a_marketplace.pdf` (annual totals, all = 6 monthly values): enrollment premiums (col A)
**10,320** (1,720/mo); SLCSP (col B) **10,140** (1,690/mo); advance PTC (col C) **9,900** (1,650/mo).
Covered: Marcus, Elena, Sofia, Leo.

- **Household income = MAGI = 91,350** (AGI 91,350; no tax-exempt interest, no nontaxable SS
  per `form8962_instructions_excerpt.md`). Leo is a covered individual but not a 2025 dependent and
  has no income — no effect.
- **FPL % = 91,350 ÷ 31,200 = 2.92788 → 292.79% of FPL** (FPL $31,200, family of 4, per excerpt).
- **Applicable figure:** 292.79% falls in the 250–300% band (4.00–6.00%), interpolated linearly:
  4.00% + (292.788 − 250) ÷ 50 × 2.00% = 4.00% + 1.7115% = **5.71%** (5.711538…% unrounded, used
  unrounded below).
- **Monthly contribution = 91,350 × 5.711538% ÷ 12 = 5,217.50 ÷ 12 = 434.79**
- **Monthly PTC = lesser of (enrollment premium 1,720) and (SLCSP 1,690 − 434.79 = 1,255.21) →
  1,255.21** for each of the 6 months
- **Annual PTC = 1,255.21 × 6 = 7,531** (7,531.25)
- **APTC = 9,900** → **Excess APTC = 9,900 − 7,531 = 2,369** (2,368.75)
- **Repayment limitation:** household income 292.79% is in the 200%–<300% band → cap **1,900**
- **Repayment (8962 line 28 → Sch 2) = min(2,369, 1,900) = 1,900**

## NY part-year allocation (IT-203)

Rule (`ny_it203_part_year_excerpt.md`): a part-year resident is taxed on **all income during the
resident period** plus **NY source income during the nonresident period**; wages for services
performed outside NY in the nonresident period are NY source **under the convenience-of-the-employer
rule** when the employee works remotely for a **New York employer** for the employee's own
convenience.

- **Resident period Jan 1 – Jun 30 (181 days)**: Brooklyn lease ended 6/30, Tampa closing 7/3
  (`email_move_dates.txt`). 181/365; the June 28–30 days at Elena's mother's were in Queens (NY),
  consistent. **Resident days = 181.**
- **Marcus — NY wages 68,000 (100%).** Resident-period wages are NY income regardless of
  where performed; post-move he works remotely from FL for his NYC-based employer (Reyes & Pike,
  1 Liberty Plaza) for his own convenience (he moved; the employer did not require it) → convenience
  rule makes those nonresident-period wages NY source too. The W-2 shows NY state wages 68,000 all
  year, consistent.
- **Elena — NY wages 54,000 (100%).** Same analysis: NYC employer (Halvorsen, 230 Park Ave S);
  "Halvorsen let me go fully remote" — permission, i.e., the employee's choice → convenience rule →
  NY source all year. W-2 NY state wages 54,000, NY withholding 2,910, consistent.
- **Method: convenience of the employer.** A day-count/workday ratio allocation was not needed
  because both ratios are 100%; attach IT-203-B showing resident-period income plus NY-source
  nonresident income, each 100%. The excerpt confirms tax withheld in excess of NY tax due would be
  refunded on IT-203.
