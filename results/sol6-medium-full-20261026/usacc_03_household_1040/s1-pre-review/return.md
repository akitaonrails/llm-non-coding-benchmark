# 2025 Reyes joint return — conditional computation

**Filing limitation:** `return.json` uses explicit assumptions for the below-market rental, the New York move date, and the Marketplace policy. Leo is claimed by his father, but the closed library gives a poverty line only for a family of four. The Marketplace calculation uses that figure as a **provisional proxy**, so the stated federal tax and refund are not verified filing amounts. See `judgment_calls.md` and `STATUS.md`.

## Federal Form 1040

| Line | Calculation | Library authority |
|---|---:|---|
| 1a wages | $68,000 Marcus + $54,000 Elena = **$122,000** | Filing framework: [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 2b interest | Chase Form 1099-INT = **$400** | Filing framework: [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 8 Schedule 1 other income | ($11,500) S corporation + ($19,550) rental = **($31,050)** | [Form 7203](../library/form7203_instructions_excerpt.md); [Form 8582](../library/form8582_instructions_excerpt.md) |
| 11 AGI | $122,000 + $400 − $31,050 = **$91,350** | [Form 7203](../library/form7203_instructions_excerpt.md); [Form 8582](../library/form8582_instructions_excerpt.md) |
| 12 deduction | MFJ standard deduction = **$31,500** | [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 15 taxable income | $91,350 − $31,500 = **$59,850** | [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 16 tax | $59,850 falls in MFJ $59,850–$59,900 Tax Table row = **$6,708** | [1040 instructions](../library/1040_instructions_tax_computation.md); [Tax Table](../library/tax_table_2025_excerpt.md) |
| 19 child tax credit | One qualifying child, Sofia, age 15: 1 × $2,200 = **$2,200** | [1040 instructions](../library/1040_instructions_tax_computation.md) |
| 17 excess APTC | Lesser of $2,369 excess and $1,900 provisional cap = **$1,900** | [Form 8962](../library/form8962_instructions_excerpt.md) |
| 24 total tax | $6,708 − $2,200 + $1,900 = **$6,408** | [1040 instructions](../library/1040_instructions_tax_computation.md); [Form 8962](../library/form8962_instructions_excerpt.md) |
| 25d withholding | $5,120 + $3,610 = **$8,730** | W-2 amounts supplied |
| 34 refund | $8,730 − $6,408 = **$2,322** | Arithmetic above |

The standard deduction exceeds the only documented home mortgage interest of $6,480. The closed library does not include complete itemized-deduction or other-credit rules; no other deduction or credit is assumed. [1040 instructions](../library/1040_instructions_tax_computation.md).

## Form 7203: Marcus's S corporation basis

Beginning 2025 stock basis = $10,000 initial contribution − $2,100 2021 loss + $6,400 2022 income + $9,800 2023 income − $12,000 2023 distribution + $4,600 2024 income − $5,200 2024 distribution = **$11,500**. Marcus reports no direct loan, so debt basis is $0; Pike's guarantee of the bank line creates no Marcus debt basis. The $28,000 K-1 loss is allowed to **$11,500** and **$16,500** is suspended. Ending stock basis after the allowed loss is $0. [Form 7203](../library/form7203_instructions_excerpt.md).

## Form 8582: Brooklyn rental

Expenses reconcile: $11,900 interest + $7,860 common charges + $5,140 property tax + $2,350 repairs + $1,150 insurance + $800 management/legal = **$29,200**. Net loss is $18,000 rent − $29,200 expenses − $9,818 supplied depreciation = **($21,018)**. The library does not independently verify the depreciation basis or life.

Elena approves tenants and repairs, supporting active participation. MAGI before passive loss = $122,000 wages + $400 interest − $11,500 allowed nonpassive S corporation loss = **$110,900**. Special allowance = $25,000 − 50% × ($110,900 − $100,000) = **$19,550**. Allowed loss is $19,550, leaving **$1,468** carried forward. This assumes $1,500 was fair rent for the existing unrelated tenant's lease. [Form 8582](../library/form8582_instructions_excerpt.md).

## Form 8962: provisional Marketplace calculation

Household income is assumed to equal AGI **$91,350**, with no reported tax-exempt interest, nontaxable Social Security, excluded foreign income, or filing-dependent income. The library's **$31,200 family-of-four FPL is used as a proxy**, although Leo is his father's dependent. The library lacks a family-of-three FPL and split-policy allocation rules. All $10,320 enrollment premiums, $10,140 SLCSP premiums, and $9,900 APTC are provisionally attributed to this return. This is **unverified**. [Form 8962](../library/form8962_instructions_excerpt.md).

- FPL percentage: $91,350 ÷ $31,200 × 100 = **292.7885%**.
- Applicable figure: 4% + (292.7885 − 250) ÷ 50 × 2% = **5.711538%**.
- Six-month contribution: $91,350 × 5.711538% × 6 ÷ 12 = **$2,608.7452**.
- Six-month PTC: lesser of $10,320 and $10,140 − $2,608.7452 = **$7,531.2548**, or **$7,531** rounded to dollars.
- Excess APTC: $9,900 − $7,531 = **$2,369**. At the proxy 292.7885% FPL, the MFJ repayment cap is **$1,900**; repayment is **$1,900**. [Form 8962](../library/form8962_instructions_excerpt.md).

## New York part-year wage allocation

Assume resident period January 1–June 30: 31 + 28 + 31 + 30 + 31 + 30 = **181 days** of 365. Time-only proration is Marcus $68,000 × 181/365 = **$33,721** resident and $34,279 after; Elena $54,000 × 181/365 = **$26,778** resident and $27,222 after, rounded by person. Both employers were New York based and approved employee-requested Florida work, with no employer necessity reported. Thus the post-move $34,279 + $27,222 = **$61,501** is provisionally New York source under the convenience rule. Total New York wages: **$68,000 Marcus + $54,000 Elena = $122,000**. [NY IT-203](../library/ny_it203_part_year_excerpt.md).

New York withholding = $3,842 + $2,910 = **$6,752**. Exact July domicile-change date and physical New York workdays were not supplied. The library lacks a New York tax table and complete rental-source allocation rules, so no New York tax or refund is asserted.
