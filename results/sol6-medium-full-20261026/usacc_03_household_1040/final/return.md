# 2025 Reyes joint return — conditional computation

**Filing limitation:** `return.json` uses explicit assumptions for the below-market rental and New York move date. Leo is claimed by his father, but the closed library gives a poverty line only for a family of four and no policy-allocation rule. **Form 8962, total federal tax, and refund are undetermined**; their JSON fields are `null`. The earlier $1,900 repayment and $2,322 refund estimates have been withdrawn. See `judgment_calls.md` and `STATUS.md`.

## Federal Form 1040

| Line | Calculation | Library authority |
|---|---:|---|
| 1a wages | $68,000 Marcus + $54,000 Elena = **$122,000** | Source: supplied W-2 amounts. This library excerpt does not address the wage line; line placement is unverified from the closed library. |
| 2b interest | Chase Form 1099-INT = **$400** | Source: supplied 1099-INT amount. This library excerpt does not address the interest line; line placement is unverified from the closed library. |
| 8 Schedule 1 other income | ($11,500) S corporation + ($19,550) rental = **($31,050)** | [Form 7203](../library/form7203_instructions_excerpt.md); [Form 8582](../library/form8582_instructions_excerpt.md) |
| 11 AGI | $122,000 + $400 − $31,050 = **$91,350** | [Form 7203](../library/form7203_instructions_excerpt.md); [Form 8582](../library/form8582_instructions_excerpt.md) |
| 12 deduction | MFJ standard deduction = **$31,500** | [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 15 taxable income | $91,350 − $31,500 = **$59,850** | [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 16 tax | $59,850 falls in MFJ $59,850–$59,900 Tax Table row = **$6,708** | [1040 instructions](../library/1040_instructions_tax_computation.md); [Tax Table](../library/tax_table_2025_excerpt.md) |
| 19 child tax credit | One qualifying child, Sofia, age 15: 1 × $2,200 = **$2,200** | [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 17 excess APTC | **Undetermined**: applicable FPL and allocation of the shared 1095-A policy are unavailable | [Form 8962](../library/form8962_instructions_excerpt.md) |
| 24 total tax | $6,708 − $2,200 = **$4,508 before Form 8962**; final amount undetermined | [1040 instructions](../library/1040_instructions_tax_computation.md); [Form 8962](../library/form8962_instructions_excerpt.md) |
| 25d withholding | $5,120 + $3,610 = **$8,730** | Source: supplied W-2 amounts; line placement is not covered by the closed library. |
| 34 refund or 37 owed | $8,730 − $4,508 = **$4,222 before Form 8962**; final balance undetermined | Arithmetic above; [Form 8962](../library/form8962_instructions_excerpt.md) |

The documented home mortgage interest is $6,480. Even adding the $6,752 New York wage withholding as a **potential** itemized amount yields only $13,232, below the $31,500 standard deduction. Whether that tax is deductible and whether other itemized amounts exist cannot be verified from the closed library; using the standard deduction is an explicit assumption. No other deduction or credit is assumed. [1040 instructions](../library/1040_instructions_tax_computation.md).

## Form 7203: Marcus's S corporation basis

Beginning 2025 stock basis = $10,000 initial contribution − $2,100 2021 loss + $6,400 2022 income + $9,800 2023 income − $12,000 2023 distribution + $4,600 2024 income − $5,200 2024 distribution = **$11,500**. Marcus reports no direct loan, so debt basis is $0; Pike's guarantee of the bank line creates no Marcus debt basis. The $28,000 K-1 loss is allowed to **$11,500** and **$16,500** is suspended. Ending stock basis after the allowed loss is $0. [Form 7203](../library/form7203_instructions_excerpt.md).

## Form 8582: Brooklyn rental

Expenses reconcile: $11,900 interest + $7,860 common charges + $5,140 property tax + $2,350 repairs + $1,150 insurance + $800 management/legal = **$29,200**. Supplied depreciation arithmetic is $270,000 building basis ÷ 27.5 years = $9,818.18, rounded to **$9,818**. Net loss is $18,000 rent − $29,200 expenses − $9,818 depreciation = **($21,018)**. The library does not independently verify the depreciation basis or life.

Elena approves tenants and repairs, supporting active participation. MAGI before passive loss = $122,000 wages + $400 interest − $11,500 allowed nonpassive S corporation loss = **$110,900**. Special allowance = $25,000 − 50% × ($110,900 − $100,000) = **$19,550**. Allowed loss is $19,550, leaving **$1,468** carried forward. This assumes $1,500 was fair rent for the existing unrelated tenant's lease. [Form 8582](../library/form8582_instructions_excerpt.md).

## Form 8962: unresolved Marketplace calculation

Household income is provisionally AGI **$91,350** + $0 reported tax-exempt interest + $0 reported nontaxable Social Security + $0 reported excluded foreign income + $0 reported income of dependents required to file = **$91,350**. The zero items are assumptions from the supplied file, not independently verified. The 1095-A policy totals reconcile to six months: $1,720 × 6 = **$10,320** enrollment premiums; $1,690 × 6 = **$10,140** SLCSP premiums; and $1,650 × 6 = **$9,900** APTC. [Form 8962](../library/form8962_instructions_excerpt.md).

Leo appears on the policy but his father claims him for 2025. The library gives only the **family-of-four FPL of $31,200**, not a poverty line for the apparent three-person tax household or a rule for dividing a shared policy between tax households. Its applicable-figure and monthly-credit formulas cannot produce a supported figure without those inputs. Thus FPL percentage, applicable figure, annual PTC, APTC **allocated to this return**, excess, repayment cap, and repayment are undetermined. The full-policy $9,900 APTC is recorded separately in JSON as `reported_policy_aptc_before_allocation`; it is **not** asserted as this return's APTC. [Form 8962](../library/form8962_instructions_excerpt.md).

## New York part-year wage allocation

Assume resident period January 1–June 30: 31 + 28 + 31 + 30 + 31 + 30 = **181 days** of 365. Time-only proration is Marcus $68,000 × 181/365 = **$33,721** resident and $34,279 after; Elena $54,000 × 181/365 = **$26,778** resident and $27,222 after, rounded by person. Both employers were New York based and approved employee-requested Florida work, with no employer necessity reported. Thus the post-move $34,279 + $27,222 = **$61,501** is provisionally New York source under the convenience rule. Total New York wages: **$68,000 Marcus + $54,000 Elena = $122,000**. [NY IT-203](../library/ny_it203_part_year_excerpt.md).

New York withholding = $3,842 + $2,910 = **$6,752**. Exact July domicile-change date and physical New York workdays were not supplied. The library lacks a New York tax table and complete rental-source allocation rules, so no New York tax or refund is asserted.
