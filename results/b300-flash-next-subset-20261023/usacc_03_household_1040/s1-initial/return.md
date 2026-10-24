# 2025 Form 1040 (MFJ) + NY Part-Year Allocation — Marcus & Elena Reyes

Prepared from the client file in `documents/`, using only the reference library (`library/INDEX.md`).
All citations below are to library files. Facts come from the client documents (cited as sources of
fact, not authority). Amounts are in whole dollars (IRS whole-dollar convention — assumption, see
`judgment_calls.md` #11).

**Headline for Marcus:** the S-corp loss does **not** "come straight off" your income. You may deduct
**$11,500** of the $28,000 K-1 loss — the rest is suspended by your stock basis and carried forward
(Form 7203). The rental loss is likewise limited by the §469(i) phase-out. Combined, the two losses
reduce AGI by $31,050, not $49,018.

---

## 1. Filing status and dependents

- MFJ: married and living together at 12/31/2025 → joint or separate; joint prepared.
  Authority: `library/1040_instructions_tax_computation.md` ("Filing status").
- **Sofia Reyes (15)** — the couple's child, lives with them, under 17 at year end → qualifying
  child, CTC $2,200. Authority: `library/1040_instructions_tax_computation.md` ("Child tax credit").
- **Leo Castellano (9, DOB 03/14/2016)** — **not** claimed in 2025. The Kings County custody order
  ¶9 alternates: father claims **odd** years, mother even. 2025 is odd → the father claims Leo via
  Form 8332; Elena is the custodial parent ("child resides primarily with the Mother") and executes
  the release. Authority: `library/1040_instructions_tax_computation.md` ("Dependents — children of
  divorced or separated parents" — "Where a decree or agreement alternates years, the agreement
  controls"; "A child claimed by the other parent under a Form 8332 release is not your qualifying
  child for the credit"). Fact source: `documents/custody_agreement_excerpt.pdf`.
- Result: dependents line = Sofia only; **line 19 CTC = $2,200** (fully absorbed: tax at line 18 is
  $8,608 > $2,200, so no refundable ACTC).

## 2. Form 7203 — Marcus's S-corp loss (Reyes & Pike Consulting Inc, 40%)

Authority: `library/form7203_instructions_excerpt.md` — losses allowed only to the extent of
adjusted stock basis + debt basis; basis is increased by contributions and income and decreased by
distributions and losses **in that order**; a guarantee of corporate debt does **not** create debt
basis. Fact source: `documents/marcus_basis_note.md`, `documents/k1_1120s_reyes_pike.pdf`.

| Year | Begin | + Contribution | + Income | − Distributions | − Loss | End |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 0 | 10,000 | 0 | 0 | (2,100) | 7,900 |
| 2022 | 7,900 | 0 | 6,400 | 0 | 0 | 14,300 |
| 2023 | 14,300 | 0 | 9,800 | (12,000) | 0 | 12,100 |
| 2024 | 12,100 | 0 | 4,600 | (5,200) | 0 | **11,500** |
| **2025** | **11,500** | 0 | 0 | 0 | loss 28,000 | **0** |

- No prior-year suspension: the 2021 loss (2,100) was fully within the $10,000 contribution basis.
- Debt basis = $0: Marcus never loaned the company money; the bank line is **personally guaranteed
  by Pike** — a guarantee does not create debt basis (`library/form7203_instructions_excerpt.md`).
- **Line 11 loss allowed = lesser of loss and basis = min(28,000, 11,500) = 11,500.**
- **Line 12+ suspended carryforward = 28,000 − 11,500 = 16,500** (indefinite until basis restored).
- K-1 Part II G says "Shareholder materially participates: Yes" → the allowed $11,500 loss is
  **nonpassive**; it reports on Schedule E and flows to Schedule 1 (Fact: K-1). Treatment as
  nonpassive matters in §4 below (per `library/form8582_instructions_excerpt.md`, such a loss, to
  the extent allowed by basis, reduces §469 MAGI).

## 3. Rental (318 Dean St #4B, Brooklyn) — Schedule E / Form 8582

Fact source: `documents/rental_summary_brooklyn.md`.

| Item | Amount |
|---|---:|
| Rent received (12 × $1,500) | 18,000 |
| Mortgage interest | (11,900) |
| Common charges | (7,860) |
| Property tax | (5,140) |
| Repairs (water heater) | (2,350) |
| Insurance | (1,150) |
| Management/legal | (800) |
| Subtotal expenses | (29,200) |
| Depreciation: 270,000 ÷ 27.5 = 9,818.18 → | (9,818) |
| **Net rental loss** | **(21,018)** |

Passive-activity status: rental is passive, but Elena **actively participates** (approves tenants,
arranges repairs herself), so the property qualifies for the §469(i) special allowance of up to
$25,000 for MFJ. Authority: `library/form8582_instructions_excerpt.md`.

Below-market rent ($1,500 vs ~$2,600 market, never raised, unrelated 6-year tenant): kept as a
**rental activity** — renting below market to an unrelated tenant because rent was never raised
"does not by itself trigger" §280A(d)(2)(C) personal-use treatment if the rent is a fair rental for
that lease. Authority: `library/form8582_instructions_excerpt.md` ("Below-market rental"). See
`judgment_calls.md` #3 — this keeps the $21,018 loss alive; the rejected alternative would
disallow the entire rental loss.

**Form 8582 computation** (all figures from `library/form8582_instructions_excerpt.md`):

- MAGI (AGI *without* the passive rental loss; the **allowed** nonpassive S-corp loss reduces it):
  68,000 + 54,000 + 400 − 11,500 = **110,900**.
- Special allowance = 25,000 − 50% × (110,900 − 100,000) = 25,000 − 5,450 = **19,550**.
  (Phase-out zeroes at MAGI ≥ 150,000; not near.)
- Loss allowed = min(21,018, 19,550) = **19,550** → flows to Schedule E/Schedule 1.
- Disallowed carryforward (Part VII) = 21,018 − 19,550 = **1,468**.

## 4. Form 1040 line by line

| Line | Item | Arithmetic | Amount |
|---|---|---|---:|
| 1a | Wages | 68,000 (Marcus W-2) + 54,000 (Elena W-2) | 122,000 |
| 2b | Taxable interest | 1099-INT box 1 (no tax-exempt interest reported) | 400 |
| 8 | Additional income, Schedule 1 | S-corp allowed loss (11,500) + rental loss allowed by 8582 (19,550), both via Schedule E | **(31,050)** |
| 11 | AGI | 122,000 + 400 − 31,050 | **91,350** |
| 12 | Deduction | Standard, MFJ (itemizing cannot win — see below) | **31,500** |
| 15 | Taxable income | 91,350 − 31,500 | **59,850** |
| 16 | Tax | Tax Table is **mandatory** under $100,000; row "at least 59,850 but less than 59,900" | **6,708** |
| 17 | Schedule 2 line 2 — excess APTC | Form 8962 repayment (§5) | 1,900 |
| 18 | Subtotal | 6,708 + 1,900 | 8,608 |
| 19 | Child tax credit | Sofia only × $2,200 (no phase-out; AGI ≪ 400,000 MFJ threshold — thresholds themselves beyond the library excerpt, but no phase-out is possible at 91,350) | **(2,200)** |
| 24 | Total tax | 8,608 − 2,200 | **6,408** |
| 25d | Federal withholding | 5,120 + 3,610 | **8,730** |
| 34 | **Overpayment / refund** | 8,730 − 6,408 | **2,322** |

Sources of fact: `w2_marcus_reyes_pike.pdf`, `w2_elena_reyes.pdf`, `1099int_chase.pdf`,
`k1_1120s_reyes_pike.pdf`, `1095a_marketplace.pdf`.

- Standard deduction $31,500 MFJ: `library/1040_instructions_tax_computation.md`.
- Tax computation: taxable income $59,850 < $100,000, so the **Tax Table must be used** (midpoint
  method), not rate schedules: `library/1040_instructions_tax_computation.md`; row value $6,708:
  `library/tax_table_2025_excerpt.md`. Cross-check only (rate schedule "for reference"): midpoint
  59,875 → 2,385 + 12% × 36,025 = 6,708 ✓.
- **Itemized check:** identifiable itemized deductions ≈ mortgage interest 6,480 (Form 1098, Tampa
  since 7/3/2025) + state/local income tax withheld 6,752 (3,842 + 2,910) + unknown Tampa property
  tax — even un-capped, far below 31,500. Standard deduction taken. (SALT cap and Tampa property
  tax not in library; immaterial either way.)
- QBI/Schedule line 13: no QBI deduction — the S-corp produced a net loss (outside contract schema; noted for completeness).

## 5. Form 8962 — Premium Tax Credit

Fact source: `documents/1095a_marketplace.pdf` — NY of Health policy NYSH-77120-RE, covered
individuals Marcus, Elena, Sofia (15), Leo (9); **coverage months January–June only** (totals
confirm: 10,320 = 6 × 1,720; 10,140 = 6 × 1,690; 9,900 = 6 × 1,650). Employer coverage (Marcus's
company) began July — Elena's W-2 box 12 code DD $7,140 "(Jul–Dec employer coverage)" corroborates.
All authority in this section: `library/form8962_instructions_excerpt.md`.

| Step | Arithmetic | Amount |
|---|---|---:|
| Household income (MAGI: AGI + tax-exempt interest + nontaxable SS + excluded foreign income) | 91,350 + 0 + 0 + 0 | **91,350** |
| FPL (2025, family of 4, contiguous) | library figure | 31,200 |
| Income as % of FPL | 91,350 ÷ 31,200 | **292.79%** |
| Applicable figure (250–300% band, linear 4.00→6.00) | 4.00% + ((292.7885 − 250) ÷ 50) × 2.00% | **5.7115%** |
| Monthly contribution | 91,350 × 5.7115% ÷ 12 | 434.79 |
| Monthly PTC | min(enrollment 1,720; SLCSP 1,690 − 434.79 = 1,255.21) → 1,255.21 | 1,255.21 |
| Annual PTC (6 covered months) | 1,255.21 × 6 | **7,531** (7,531.25) |
| APTC actually paid | 1095-A col C total | **9,900** |
| Excess APTC | 9,900 − 7,531 | **2,369** |
| Repayment limitation (MFJ, 200% ≤ income < 300% FPL) | library line-28 table | **1,900** |
| **Repayment** (Sch 2 line 2 → 1040 line 17) | min(2,369, 1,900) | **1,900** |

The limitation is what keeps this from being a bill: without the cap the repayment would be $2,369;
the household pays **$1,900**. The result is robust to rounding — at 5.71% the annual PTC is 7,532
and excess 2,368; the cap still controls. (Household includes Leo for coverage/FPL purposes — the
1095-A covers him and the library supplies the family-of-4 FPL; see `judgment_calls.md` #12.)

## 6. New York part-year allocation (IT-203)

Authority: `library/ny_it203_part_year_excerpt.md`. Facts: `documents/email_move_dates.txt`, W-2s.

- **Resident period:** Jan 1 – **Jul 2** = **183 days** (Jan 31 + Feb 28 + Mar 31 + Apr 30 + May 31
  + Jun 30 = 181, + Jul 1–2 = 183). Rationale and rejected alternatives (181 / 184+):
  `judgment_calls.md` #7.
- **Wages — convenience of the employer:** both employers are New York-based (Reyes & Pike, 1
  Liberty Plaza, NY; Halvorsen Media Group, 230 Park Ave S, NY). Marcus "just works remotely";
  Halvorsen "let [Elena] go fully remote" — employer *permission*, not employer *necessity*. Under
  the convenience-of-the-employer rule, wages paid by a NY employer to an employee working
  out-of-state for the employee's own convenience are NY source. Therefore
  **Marcus NY wages $68,000 and Elena NY wages $54,000 — 100% for the full year**, and the
  resident/nonresident day ratio is immaterial for wages.
- Other income: Brooklyn condo rent is NY real-property income (NY-source all year); the $400
  interest allocates by resident days, 400 × 183 ÷ 365 ≈ $201 to NY.
- NY withheld: 3,842 + 2,910 = **$6,752** (both W-2s withheld NY all year, per the email, because
  nobody updated the forms).

**Open item:** NY net tax and the IT-203 refund (withheld in excess of tax is refunded per the
IT-203 excerpt) **cannot be computed from this library** — no NY rate schedule, standard deduction,
or exemption figures are in `library/INDEX.md`. Labeled unverified rather than invented; see
`STATUS.md`.

---

### Reconciliation notes
- Nothing was forced to balance: AGI 91,350 = 122,400 gross − 31,050 Sch 1; tax 6,708 is straight
  from the library table row for 59,850–59,900; refund 8,730 − 6,408 = 2,322.
- Suspended losses carried to 2026: S-corp **16,500** (7203) + rental **1,468** (8582 Part VII).
- Marcus's expectation corrected: of the $28,000 K-1 loss, **$11,500** hits the 2025 return.
