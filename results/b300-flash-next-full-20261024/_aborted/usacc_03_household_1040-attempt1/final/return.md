# 2025 Form 1040 — Marcus & Elena Reyes (MFJ) — figure workpaper

All citations are to files listed in `library/INDEX.md` (short forms below). Amounts in USD.
Loss fields on Forms 7203/8582 are stated as positive loss amounts; line-8 is a signed
(Schedule 1) figure.

Cite key: **[1040-I]** `library/1040_instructions_tax_computation.md` · **[TT]**
`library/tax_table_2025_excerpt.md` · **[7203]** `library/form7203_instructions_excerpt.md` ·
**[8582]** `library/form8582_instructions_excerpt.md` · **[8962]**
`library/form8962_instructions_excerpt.md` · **[IT203]** `library/ny_it203_part_year_excerpt.md`.

---

## Headline result

Federal: **refund of $2,322.00** (line 34). NY: part-year IT-203 with a withholding refund
(NY tax computation is outside this engagement's deliverable fields).

**Marcus's expectation is wrong.** The $28,000 S-corp loss does *not* come straight off their
income. Stock basis on 1/1/2025 is only **$11,500** (rollforward below), so **$11,500 is allowed
and $16,500 is suspended** on Form 7203 — allowed only to the extent of adjusted basis,
suspended losses carry forward indefinitely until basis is restored **[7203]**. His guarantee
note doesn't help: it is Pike who personally guarantees the bank line, and a guarantee of
corporate debt does not create debt basis (only a direct shareholder loan does) **[7203]**.

---

## Form 7203 — S-corp stock basis (Reyes & Pike Consulting Inc, 40%, Marcus)

Ordering per **[7203]**: basis is increased by contributions and income, decreased by
distributions, then by losses. Source: `documents/marcus_basis_note.md`, K-1 (`documents/k1_1120s_reyes_pike.pdf`).

| Year | Transaction | Running stock basis |
|---|---|---:|
| 2021 | contribution | 10,000 |
| 2021 | loss (2,100) | 7,900 |
| 2022 | income 6,400 | 14,300 |
| 2023 | income 9,800 → 24,100; distribution (12,000) | 12,100 |
| 2024 | income 4,600 → 16,700; distribution (5,200) | **11,500** |
| 2025 | Line 1 beginning basis | **11,500** |

Distributions never exceeded basis in any year (12,000 ≤ 24,100; 5,200 ≤ 16,700); the library is
silent on distributions in excess of basis, but that question never arises on these facts.
No shareholder loans → debt basis $0.

- Loss allowed (line 11) = min(loss 28,000, basis 11,500) = **11,500**
- Suspended/carryforward (line 12 et seq.) = 28,000 − 11,500 = **16,500**

K-1 line 17 "gross receipts 612,400" is not income and does not enter the return.

## Schedule E / Form 8582 — Brooklyn condo rental

Net rental loss (Sch E Part I), from `documents/rental_summary_brooklyn.md`:

- Expenses check: 11,900 + 7,860 + 5,140 + 2,350 + 1,150 + 800 = 29,200 ✔
- Income 18,000 − expenses 29,200 − depreciation 9,818 (270,000 ÷ 27.5 per the client-prepared
  summary, full year; property rented all year — the library is silent on depreciation, so the
  figure is taken as reported; judgment call #9) = **−21,018**

Elena actively participates (approves tenants, arranges repairs herself) → special allowance
available **[8582]**.

**Modified AGI** = AGI figured without the passive rental loss, but *with* allowed nonpassive
losses reducing it — the excerpt expressly says an S-corp loss allowed by basis (material
participation = Yes on the K-1, so nonpassive) reduces MAGI **[8582]**:

- MAGI = wages 122,000 + interest 400 − S-corp loss allowed 11,500 = **110,900**
- Special allowance = 25,000 − 50% × (110,900 − 100,000) = 25,000 − 5,450 = **19,550**
  (phase-out zeroes the allowance at MAGI ≥ 150,000; we are between 100k and 150k **[8582]**)
- Loss allowed = min(21,018, 19,550) = **19,550**; carryforward (Part VII) = 21,018 − 19,550 = **1,468**

No circularity: MAGI is defined without the passive loss, so it does not depend on the
allowed amount.

## Form 1040

| Line | Figure | Arithmetic / authority |
|---|---:|---|
| 1a Wages | 122,000.00 | Marcus 68,000 + Elena 54,000 (W-2s) |
| 2b Interest | 400.00 | 1099-INT (Chase, Elena) |
| 8 Sch 1 other income | −31,050.00 | Sch E total → Sch 1 line 5: rental −19,550 + S-corp (Sch E Part II) −11,500 |
| 11 AGI | 91,350.00 | 122,000 + 400 − 31,050 |
| 12 Deduction | 31,500.00 | MFJ standard **[1040-I]**; itemized loses: 6,480 Tampa mortgage interest (1098) + state tax withheld 6,752 (3,842 + 2,910) = 13,232 < 31,500 — holds under any SALT limitation (the library is silent on itemized deductions, so no cap is cited); condo expenses/property tax are on Sch E, not itemized |
| 15 Taxable income | 59,850.00 | 91,350 − 31,500 |
| 16 Tax | 6,708.00 | TI < 100,000 → **must** use Tax Table **[1040-I]**; row "at least 59,850, but less than 59,900" = **6,708 MFJ** **[TT]**. Cross-checked by the table's documented midpoint method: midpoint 59,875 → 23,850×10% + (59,875 − 23,850)×12% = 2,385 + 4,323 = 6,708 ✔ |
| 17 Sch 2 line 2 | 1,900.00 | Excess APTC repayment, Form 8962 (below) |
| 18 | 8,608.00 | 6,708 + 1,900 |
| 19 CTC | 2,200.00 | $2,200 per qualifying child under 17 who is your dependent **[1040-I]**; Sofia (15) qualifies; Leo does **not** (below) |
| 24 Total tax | 6,408.00 | 8,608 − 2,200 (credit fully absorbed by line-18 tax) |
| 25d Withholding | 8,730.00 | Federal: 5,120 (Marcus) + 3,610 (Elena) |
| 34 Refund | **2,322.00** | 8,730 − 6,408 (line 34 refund, not line 37 owed) |

## Dependents

- **Sofia Reyes (15)** — their child, under 17 → CTC $2,200 **[1040-I]**.
- **Leo Castellano (9)** — **not claimed in 2025.** The custody order alternates years:
  father claims odd years, mother even years; 2025 is odd. The library is explicit that where
  a decree alternates years, the agreement controls, and a child claimed by the other parent
  under a Form 8332 release is not your qualifying child for the credit **[1040-I]**
  (`documents/custody_agreement_excerpt.pdf`). **Client-confirmed:** Elena signed Form 8332
  releasing Leo to his father — "it's his year" (2025 is the father's year under the order).
  Residual check: the reply read "{TY}" — the executed release should specify tax year **2025**
  (carried as an open item in STATUS).

## Form 8962 — Premium tax credit reconciliation (Jan–Jun coverage, policy NYSH-77120-RE)

From `documents/1095a_marketplace.pdf`: enrollment premium A = 1,720/mo, SLCSP B = 1,690/mo,
APPTC C = 1,650/mo, January–June only; annual C total = 9,900. Covered: 4 individuals
(Marcus, Elena, Sofia, Leo). Family size taken as **4** (see judgment calls — only the 4-person
FPL is in the library **[8962]**; an allocation to 3 would need Leo's individual SLCSP and a
3-person FPL, neither available, and the client has no further information). This remains a
**flagged assumption**: if the 3-person treatment applied instead, the repayment would grow to
≈2,989 and the refund would fall to ≈1,233 (derivation in judgment call #4; the 3-person FPL
figure itself is outside the library).

1. Household income = MAGI = AGI 91,350 (no tax-exempt interest, nontaxable SS, or excluded
   foreign income) **[8962]**
2. % FPL = 91,350 ÷ 31,200 = **292.79%**
3. Applicable figure (Table 2, 250–300% band, 4.00%→6.00%, linear) **[8962]**, computed on the
   unrounded ratio 292.7885% (the 292.79% above is its 2-decimal display):
   4.00% + (292.7885 − 250)/50 × 2.00% = 4.00% + 1.7115% = **5.7115%**
4. Monthly contribution = 91,350 × 5.7115% ÷ 12 = **434.79**
5. Monthly PTC = min(A 1,720.00, B 1,690.00 − 434.79 = 1,255.21) = **1,255.21**
6. Annual PTC = 1,255.21 × 6 months = **7,531.26**
7. Excess advance payments = 9,900 − 7,531.26 = **2,368.74**
8. Repayment limitation: household income is ≥200% and <300% FPL → MFJ cap **$1,900** **[8962]**
9. Repayment (1040 line 17) = min(2,368.74, 1,900) = **1,900.00** — the cap binds; exact figure
   is insensitive to rounding conventions (434.79 vs 433.91 monthly contribution still yields
   excess > $1,900).

## New York part-year (IT-203)

- **Resident period:** Jan 1 – **Jul 2** = **183 days** (of 365); FL domicile from Jul 3 —
  Brooklyn lease ended 6/30, nights 6/28–30 at mother's in Queens (NY abode not yet abandoned,
  FL abode not yet maintained), Tampa closing/move-in Jul 3 (`documents/email_move_dates.txt`).
  Alternative (lease-end 6/30, 181 days) rejected in `judgment_calls.md`.
- **Marcus NY wages = 68,000; Elena NY wages = 54,000 — full year.** Both employers are NY
  (Reyes & Pike, 1 Liberty Plaza; Halvorsen, 230 Park Ave S). Under the convenience-of-the-employer
  rule, wages paid by a NY employer to an employee working from an out-of-state location for the
  *employee's* convenience remain NY source; only days worked outside NY for the *employer's
  necessity* are excluded **[IT203]**. **Client-confirmed:** Marcus asked to move and the
  company "didn't need him out of state"; Elena's own remote request was approved — the
  arrangement serves the *employees'* convenience, not employer necessity, for both spouses, so
  full-year NY sourcing stands. Actual post-move NY workdays are unknown, but under convenience
  sourcing they do not change the wage sourcing.
- **Method:** part-year day-count (183/365) for income other than wages; wages fully NY-sourced
  for the year under the convenience rule **[IT203]**. The library taxes nonresidents on NY-source
  income but supplies **no sourcing rule for real-property income**, so the Brooklyn condo rental
  being NY-source for the entire year is an **outside-library assumption** (judgment call #12) —
  immaterial here: no NY tax figure is a deliverable field, and the rental loss is fully used
  federally. Per the library, income during the resident period is fully taxed, nonresident-period
  tax is on NY-source income, and over-withheld NY tax is refunded on
  IT-203 **[IT203]**. NY withholding of 6,752 (3,842 + 2,910) will substantially exceed NY part-year
  tax → refund; the NY tax computation itself is outside this engagement's deliverable fields
  (and the library has no NY rate tables — so no NY tax figure is computed rather than invented).

## Items not on the return (checked)

- W-2 box DD $7,140 (employer coverage Jul–Dec) — informational only.
- 1098 Tampa mortgage interest 6,480 — considered in the itemized comparison; standard deduction wins.
- K-1 gross receipts 612,400 — not taxable income.
