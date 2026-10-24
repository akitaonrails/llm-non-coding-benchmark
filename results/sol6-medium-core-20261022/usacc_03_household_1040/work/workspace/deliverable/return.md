# 2025 provisional federal return and New York allocation

**Filing status:** married filing jointly as of December 31. **Provisional result:** $2,322 federal refund. The calculation assumes the Brooklyn rent was fair under the tenant's existing lease, the four people on the marketplace policy are the relevant family of four for the supplied poverty-line figure, and the work in Florida was for each employee's convenience. These assumptions are unconfirmed; see `judgment_calls.md` and `STATUS.md`. The supplied library does not resolve the marketplace treatment of Leo, whom his father claims for 2025.

## Federal Form 1040

| Line | Calculation | Amount |
|---|---:|---:|
| 1a wages | Marcus $68,000 + Elena $54,000 | $122,000 |
| 2b taxable interest | Chase 1099-INT | $400 |
| 8 Schedule 1 other income | S corporation loss ($11,500) + allowable rental loss ($19,550) | ($31,050) |
| 11 adjusted gross income | $122,000 + $400 − $31,050 | $91,350 |
| 12 standard deduction | Married filing jointly | $31,500 |
| 15 taxable income | $91,350 − $31,500 | $59,850 |
| 16 income tax | Tax Table row $59,850–$59,900, married filing jointly | $6,708 |
| 19 child tax credit | 1 qualifying child (Sofia) × $2,200 | ($2,200) |
| 17 Schedule 2 excess advance premium tax credit | Limited Form 8962 repayment | $1,900 |
| 24 total tax | $6,708 − $2,200 + $1,900 | $6,408 |
| 25d federal withholding | Marcus $5,120 + Elena $3,610 | $8,730 |
| 34 refund | $8,730 − $6,408 | $2,322 |

The $31,500 standard deduction and the requirement to use the Tax Table below $100,000 come from [IRS 2025 Form 1040 Instructions](../library/1040_instructions_tax_computation.md); the exact $6,708 tax comes from [IRS 2025 Tax Table](../library/tax_table_2025_excerpt.md). No larger itemized deduction is established by the file. Known personal mortgage interest of $6,480 plus New York income tax withheld of $6,752 totals $13,232, below the standard deduction; no other personal itemized expenses are documented. Sofia is 15 and qualifies for the $2,200 credit; Leo is allocated to his father in odd-numbered 2025 under the custody agreement, so this calculation does not claim him. The dependent and credit rules are in [IRS 2025 Form 1040 Instructions](../library/1040_instructions_tax_computation.md).

## S corporation basis and loss — Form 7203

Opening 2025 stock basis = $10,000 initial contribution − $2,100 (2021 loss) + $6,400 (2022 income) + $9,800 (2023 income) − $12,000 (2023 distribution) + $4,600 (2024 income) − $5,200 (2024 distribution) = **$11,500**. Marcus made no direct loan, so debt basis is $0. The bank line and Pike's guarantee create no debt basis for Marcus. Allowed 2025 K-1 loss = lesser of $28,000 and $11,500 = **$11,500**; basis-suspended loss = $28,000 − $11,500 = **$16,500**. The K-1 identifies Marcus as materially participating, so the basis-allowed loss is treated as nonpassive in this calculation. [IRS Form 7203 Instructions 2025](../library/form7203_instructions_excerpt.md); [IRS Form 8582 Instructions 2025](../library/form8582_instructions_excerpt.md).

## Brooklyn rental — Form 8582

Expenses before depreciation = $11,900 interest + $7,860 common charges + $5,140 property tax + $2,350 repairs + $1,150 insurance + $800 management/legal = **$29,200**. Rental result = $18,000 rent − $29,200 expenses − $9,818 depreciation = **($21,018)**. Elena actively participates. Modified AGI before passive rental loss = $122,000 wages + $400 interest − $11,500 nonpassive S corporation loss = **$110,900**. Special allowance = $25,000 − 50% × ($110,900 − $100,000) = **$19,550**. Allowed rental loss = lesser of $21,018 and $19,550 = **$19,550**; passive carryforward = $21,018 − $19,550 = **$1,468**. [IRS Form 8582 Instructions 2025](../library/form8582_instructions_excerpt.md).

This treatment assumes $1,500 monthly was fair rent under the existing tenant's lease. The tenant is unrelated and rent was never raised, facts which alone do not establish prohibited personal use under the supplied [Form 8582 instructions](../library/form8582_instructions_excerpt.md). The client cannot confirm the 2025 lease terms or personal-use days. If the rent was less than fair rental value for that lease, the supplied excerpt says the loss is not allowed, and the federal figures above would change.

## Marketplace coverage — Form 8962

Marketplace coverage was January–June only; Elena joined her employer plan July 1. The 1095-A six-month totals are enrollment premiums **$10,320** (6 × $1,720), benchmark premiums **$10,140** (6 × $1,690), and advance credit **$9,900** (6 × $1,650). No July–December marketplace amount is included.

Assuming no additional household modified-AGI items or dependent income, household income = AGI = **$91,350**. Using the supplied four-person federal poverty line, $91,350 ÷ $31,200 × 100 = **292.78846% FPL**. Linear interpolation in the 250%–300% band gives applicable figure = 4% + [(292.78846 − 250) ÷ 50 × 2%] = **5.711538%**. Annual contribution = $91,350 × 5.711538% = **$5,217.49**; monthly contribution = $5,217.49 ÷ 12 = **$434.79**. Monthly credit = lesser of $1,720 and ($1,690 − $434.79) = **$1,215.21**. Six-month credit = **$7,291.25**, rounded to **$7,291**; excess advance credit = $9,900 − $7,291 = **$2,609**. Income is between 200% and 300% FPL, so the married-filing-jointly repayment cap is **$1,900**. Repayment = lesser of $2,609 and $1,900 = **$1,900**. [IRS Form 8962 Instructions 2025](../library/form8962_instructions_excerpt.md).

**Open coverage issue:** Leo appears on the 1095-A but is claimed by his father in 2025. The supplied [Form 8962 excerpt](../library/form8962_instructions_excerpt.md) provides a poverty line only for a family of four and no rule for allocating one policy across tax households or identifying the applicable family size in this situation. This calculation provisionally uses the full 1095-A and the supplied four-person figure. The proper allocation and possibly the repayment cap remain unverified under the closed library.

## New York part-year allocation

The provisional resident period is January 1–June 30: 31 + 28 + 31 + 30 + 31 + 30 = **181 days**. The apartment lease ended June 30; the date Florida became the permanent home is unconfirmed. Both employers are based in New York. Assuming their Florida remote work was for employee convenience, all wages remain New York source during the nonresident period: Marcus **$68,000**, Elena **$54,000**, total **$122,000**. Resident-period wage shares by days, for comparison only, are $68,000 × 181 ÷ 365 = **$33,720.55** and $54,000 × 181 ÷ 365 = **$26,778.08**. Under the stated convenience assumption, the remaining wages are also New York source. New York tax withheld totals $3,842 + $2,910 = **$6,752**. [NYS IT-203-I (2025)](../library/ny_it203_part_year_excerpt.md).

The library does not supply a New York tax table or enough rules to compute an IT-203 tax or refund. Exact residency-change and workday facts, employer necessity, and New York allocation of the S corporation and rental items remain open. The JSON records the requested wage allocation under the stated assumptions, not a completed New York tax liability.
