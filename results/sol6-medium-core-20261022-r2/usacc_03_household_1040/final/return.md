# 2025 federal return and New York part-year wage allocation

**Status:** Working return, subject to the open items in `STATUS.md`. Dollar amounts in `return.json` are rounded to whole dollars. The rental deduction and Form 8962 calculation rely on the assumptions described below.

## Form 1040

| Line | Amount | Arithmetic and authority |
|---|---:|---|
| 1a, wages | $122,000 | Marcus W-2 $68,000 + Elena W-2 $54,000. W-2 amounts are client facts. |
| 2b, taxable interest | $400 | Chase 1099-INT $400. |
| 8, Schedule 1 other income | ($31,050) | Allowed S-corp loss ($11,500) + allowed rental loss ($19,550) = ($31,050). See Forms 7203 and 8582 below. |
| 11, adjusted gross income | $91,350 | $122,000 + $400 − $11,500 − $19,550 = $91,350. |
| 12, standard deduction | $31,500 | Married filing jointly amount in `library/1040_instructions_tax_computation.md`. The $6,480 home mortgage interest by itself is below this amount; no other personal itemized expenses were supplied. |
| 15, taxable income | $59,850 | $91,350 − $31,500. |
| 16, income tax | $6,708 | $59,850 falls in the $59,850–$59,900 married-filing-jointly row of `library/tax_table_2025_excerpt.md`. The lower endpoint is included in that row. The Tax Table is mandatory below $100,000 under `library/1040_instructions_tax_computation.md`. |
| 19, child tax credit | $2,200 | One dependent child, Sofia, age 15 × $2,200 under `library/1040_instructions_tax_computation.md`. Leo is assigned to his father for odd tax years under the custody order. |
| 17, Schedule 2 excess advance PTC | $1,900 | Lesser of $2,369 excess and $1,900 repayment limit; see Form 8962 below. Authority: `library/form8962_instructions_excerpt.md`. |
| 24, total tax | $6,408 | $6,708 − $2,200 + $1,900. |
| 25d, federal withholding | $8,730 | Marcus $5,120 + Elena $3,610. |
| 34, refund | $2,322 | $8,730 − $6,408. |

## Form 7203 — S-corp basis limitation

Beginning 2025 stock basis: $10,000 initial contribution − $2,100 2021 loss + $6,400 2022 income + $9,800 2023 income − $12,000 2023 distribution + $4,600 2024 income − $5,200 2024 distribution = **$11,500**. No direct shareholder loan and no 2025 distribution are reported. The bank debt guarantee does not create basis. Thus, of the $28,000 2025 K-1 ordinary loss, **$11,500 is allowed** and **$16,500 is suspended** ($28,000 − $11,500). Marcus materially participates, so the allowed loss is nonpassive. Authority: `library/form7203_instructions_excerpt.md`; `library/form8582_instructions_excerpt.md`.

## Form 8582 — Brooklyn rental

Expenses before depreciation total $11,900 + $7,860 + $5,140 + $2,350 + $1,150 + $800 = **$29,200**. Rental result: $18,000 rent − $29,200 expenses − $9,818 depreciation = **($21,018)**. Elena approves tenants and repairs, which supports active participation. MAGI before a passive rental loss: $122,000 wages + $400 interest − $11,500 allowed nonpassive S-corp loss = **$110,900**. The special allowance is $25,000 − 50% × ($110,900 − $100,000) = **$19,550**. Allowed rental loss is the lesser of $21,018 and $19,550, or **$19,550**; carryforward is $21,018 − $19,550 = **$1,468**. Authority: `library/form8582_instructions_excerpt.md`.

This calculation assumes the unrelated tenant's broker-arranged tenancy and unchanged $1,500 rent remain a fair rental for the lease. The current estimated market rent is $2,600; the 2025 lease and terms are unavailable. If the rent fails the library's fair-rental exception, the loss is disallowed under its personal-use rule and the federal figures need recomputation. The library addresses the loss limitation and below-market rule, but it does not independently verify each expense's deductibility or the supplied $9,818 depreciation amount; those are client-supplied working figures. Authority for the stated limitations: `library/form8582_instructions_excerpt.md`.

## Form 8962 — January–June Marketplace coverage

The working case uses the library's four-person federal poverty line of **$31,200** and assigns the complete Form 1095-A policy to this return; the allocation involving Leo's father's tax household is unknown. Household income is $91,350 AGI; no tax-exempt interest, nontaxable Social Security, excluded foreign income, or dependent income was reported. $91,350 ÷ $31,200 × 100 = **292.78846% FPL**. Linear interpolation within the 250%–300% band gives 4.00% + [($292.78846 − 250) ÷ 50] × 2.00% = **5.71154%**. Monthly contribution: $91,350 × 5.71153846% ÷ 12 = **$434.79**. Monthly PTC is the lesser of $1,720 enrollment premium and $1,690 SLCSP − $434.79 = **$1,255.21**. Six months give $1,255.2091346 × 6 = $7,531.25, rounded to **$7,531**. Excess advance payment: $9,900 − $7,531 = **$2,369**. Because income is between 200% and 300% FPL, the married-filing-jointly repayment limit is **$1,900**; repayment is **$1,900**. Authority: `library/form8962_instructions_excerpt.md`.

The library gives only a four-person poverty line and does not explain the tax-family treatment of a covered child claimed by another taxpayer or a policy allocation between tax households. The four-person and full-policy treatments are assumptions, not verified rules. A different allocation or family size may change the credit, repayment, and refund.

## New York IT-203 wage allocation

Resident period: January 1 through June 30, **31 + 28 + 31 + 30 + 31 + 30 = 181 days**. The family remained in New York through June 30 and moved to Florida in early July. Marcus's New York employer permitted the Florida arrangement after his request; Elena's New York employer approved her request. Neither described an employer necessity for Florida work. Thus the working allocation includes resident-period wages plus post-move wages sourced to New York under the convenience-of-the-employer rule: **Marcus $68,000; Elena $54,000; total $122,000**. The W-2s do not split resident and post-move wages, but the split does not change the total allocated amount under this method. Authority: `library/ny_it203_part_year_excerpt.md`.

The $400 interest was received during an unspecified part of the year. The library provides no New York tax table or rate calculation, so this engagement determines the requested wage allocation but does not calculate an IT-203 liability or state refund. New York withholding totals $3,842 + $2,910 = **$6,752**; a refund cannot be measured without tax due.
