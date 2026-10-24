# 2025 Federal Return — Marcus and Elena Reyes (Married Filing Jointly)

Tax year 2025. Filing status: married filing jointly (status as of 12/31; couple living together — IRS 2025 Form 1040 Instructions).
All citations are to files listed in `workspace/library/INDEX.md`.

## Sources (client file)

| Document | Facts used |
|---|---|
| `documents/w2_marcus_reyes_pike.pdf` | Marcus wages $68,000; federal withholding $5,120; NY withholding $3,842; employer Reyes & Pike Consulting Inc, New York NY |
| `documents/w2_elena_reyes.pdf` | Elena wages $54,000; federal withholding $3,610; NY withholding $2,910; employer Halvorsen Media Group LLC, New York NY |
| `documents/k1_1120s_reyes_pike.pdf` | S-corp ordinary loss (28,000); distributions $0; 40% stock; materially participates: Yes |
| `documents/1099int_chase.pdf` | Interest income $400 |
| `documents/1095a_marketplace.pdf` | Annual enrollment premium $10,320 (A); SLCSP premium $10,140 (B); APTC $9,900 (C); covered: Marcus, Elena, Sofia (15), Leo (9) |
| `documents/1098_mortgage.pdf` | Tampa residence (acquired 7/3/2025) mortgage interest $6,480 (not itemized — see below) |
| `documents/marcus_basis_note.md` | Stock purchase 2021 ($10,000); 2021–2024 income/loss and distributions; no shareholder loans; Pike personally guarantees bank line |
| `documents/rental_summary_brooklyn.md` | Brooklyn condo rental income/expenses/depreciation; below-market rent to long-time tenant |
| `documents/email_move_dates.txt` | Moved NY→FL; Brooklyn lease ended 6/30/25 (family still in NY through 6/30, at mother's in Queens 6/28–30); Tampa closed 7/3/25; employers withheld NY all year; Sofia (15) is theirs; Leo (9) is Elena's son from before |
| `documents/custody_agreement_excerpt.pdf` | Leo: parents alternate; father claims in odd years, mother in even years; child resides primarily with mother; 8332 required for years the noncustodial parent claims |

---

## 1. Form 7203 — S-corp stock basis (loss limitation)

**Basis history** (per Marcus's note; stock basis increases by contributions and income, decreases by distributions and losses — IRS Form 7203 Instructions 2025):

| Year | Start | Income/(loss) | Distributions | End |
|---|---:|---:|---:|---:|
| 2021 | 10,000 (contribution) | (2,100) | 0 | 7,900 |
| 2022 | 7,900 | 6,400 | 0 | 14,300 |
| 2023 | 14,300 | 9,800 | (12,000) | 12,100 |
| 2024 | 12,100 | 4,600 | (5,200) | **11,500** |

- **stock_basis_begin (2025) = $11,500**
- Debt basis = $0. Marcus never made a direct loan to the corporation; Pike's *personal guarantee* of the bank line does **not** create debt basis (IRS Form 7203 Instructions 2025).
- **loss_allowed = lesser of loss $28,000 and basis $11,500 = $11,500**
- **loss_suspended = 28,000 − 11,500 = $16,500** (carried forward indefinitely; released as basis is restored).

**This rejects Marcus's expectation that the loss "comes straight off":** only $11,500 is deductible in 2025; $16,500 is suspended (see `judgment_calls.md`, item 1).

## 2. Form 8582 — Rental passive loss (Brooklyn condo)

- Rental loss before allowance = rent $18,000 − expenses $29,200 − depreciation $9,818 = **($21,018)** (per Elena's rental summary; depreciation = $270,000 ÷ 27.5).
- **MAGI** for the special allowance = AGI figured without passive losses, but *including* the allowed S-corp loss (material participation → nonpassive) (IRS Form 8582 Instructions 2025):
  `MAGI = $122,000 (wages) + $400 (interest) − $11,500 (S-corp loss) = $110,900`
- **Special allowance** = $25,000 − 50% × ($110,900 − $100,000) = $25,000 − $5,450 = **$19,550** (MFJ phase-out; active participation — Elena approves tenants and arranges repairs).
- **loss_allowed = lesser of $21,018 and $19,550 = $19,550**
- **carryforward = 21,018 − 19,550 = $1,468** (Part VII).
- Below-market rent: loss is allowed — see `judgment_calls.md`, item 3 (IRS Form 8582 Instructions 2025, below-market rental note).

## 3. Form 1040

| Line | Amount | Arithmetic | Authority |
|---|---:|---|---|
| 1a wages | $122,000 | $68,000 (Marcus W-2) + $54,000 (Elena W-2) | W-2s |
| 2b interest | $400 | Chase 1099-INT | 1099-INT |
| 8 other income (Sch 1) | ($31,050) | S-corp loss (11,500) + rental loss (19,550) | Form 7203 & 8582 computations above (IRS Form 7203 / 8582 Instructions 2025) |
| 11 AGI | $91,350 | 122,000 + 400 − 31,050 | — |
| 12 deduction | $31,500 | Standard deduction, MFJ (itemized would be at most ~$6,480 mortgage interest — far less; see judgment item 5) | IRS 2025 Form 1040 Instructions |
| 15 taxable income | $59,850 | 91,350 − 31,500 | — |
| 16 tax | $6,708 | Taxable income < $100,000 → **must use Tax Table**; row "59,850 / 59,900" → $6,708 | IRS 2025 Form 1040 Instructions; IRS 2025 Tax Table |
| 19 CTC | $2,200 | $2,200 × 1 qualifying child (Sofia, age 15). Leo is not a 2025 Reyes dependent (odd year → father per custody agreement). A child claimed by the other parent under 8332/decree is not a qualifying child for the credit | IRS 2025 Form 1040 Instructions |
| 17 Sch 2 excess APTC | $1,900 | Form 8962 repayment (computed below) | IRS Form 8962 Instructions 2025 |
| 24 total tax | $6,408 | 6,708 + 1,900 − 2,200 | — |
| 25d withholding | $8,730 | $5,120 (Marcus) + $3,610 (Elena) | W-2s |
| 34 refund | **$2,322** | 8,730 − 6,408 (positive = refund; if negative it would be line 37) | — |

## 4. Form 8962 — Premium Tax Credit

- **Household income** = modified AGI of taxpayer and dependents required to file = AGI $91,350 (no tax-exempt interest, nontaxable Social Security, or excluded foreign income) (IRS Form 8962 Instructions 2025).
- **FPL** (2025, family of 4, 48 contiguous states) = $31,200 (household: Marcus, Elena, Sofia, Leo — Leo is covered on the 1095-A and resides primarily with Elena) (IRS Form 8962 Instructions 2025).
- **fpl_pct** = 91,350 ÷ 31,200 = **292.79%** (292.7885% exact).
- **Applicable figure**: 250–300% band is 4.00%→6.00%, linear within band:
  `4.00% + (292.7885% − 250%) × (2.00% ÷ 50 pp) = 4.00% + 1.7115% = 5.7115%` → **5.71%**.
- **Monthly contribution** = 91,350 × 5.7115% ÷ 12 = $5,217.49 ÷ 12 = $434.79.
- **Monthly PTC** = lesser of (a) enrollment premium $10,320 ÷ 12 = $860.00 and (b) SLCSP premium $10,140 ÷ 12 = $845.00 − $434.79 = $410.21 → **$410.21**.
- **annual_ptc** = 410.21 × 12 = **$4,922.51**.
- **APTC** (1095-A col. C) = $9,900.
- **Excess** = 9,900 − 4,922.51 = **$4,977.49**.
- **Repayment limitation**: household income 292.79% FPL falls in 200%–<300% band → **$1,900** (IRS Form 8962 Instructions 2025).
- **repayment = lesser of $4,977.49 and $1,900 = $1,900** (added to tax on Sch 2 line 3 → 1040 line 17).

## 5. Dependents

- **Sofia Reyes (15)** — claimed by Reyes; qualifying child (under 17 → CTC).
- **Leo (9) — NOT claimed.** Custody stipulation (NY Family Court, V-04418-19): parents alternate; father claims in odd-numbered years, mother in even years. 2025 is an odd year → Leo is the father's dependent. "Where a decree or agreement alternates years, the agreement controls which parent claims the child for that year" (IRS 2025 Form 1040 Instructions). Leo resides primarily with Elena, but the decree controls for 2025; Elena will execute Form 8332 for the father (see `judgment_calls.md`, item 2).

## 6. New York part-year allocation (IT-203)

- **Resident period: Jan 1 – Jun 30 = 181 days.** Brooklyn lease ended 6/30; the family was still in NY through 6/30 (at Elena's mother's in Queens 6/28–30); closed on the Tampa home 7/3 and moved in that weekend (Elena's email). **Nonresident period: Jul 1 – Dec 31 = 184 days.**
- **Method** (NYS IT-203-I (2025)): a part-year resident is taxed on (i) all income received during the resident period, plus (ii) NY-source income during the nonresident period. Wages for services performed entirely outside NY during the nonresident period are not NY source, **except** under the convenience-of-the-employer rule (NY employer; out-of-state remote work for the employee's own convenience).
- **Marcus — $68,000 NY wages.** During the resident period: all wages NY (residency). During the nonresident period: employer is in NYC and Marcus works remotely from Tampa by his own choice after the family's voluntary move → convenience-of-the-employer rule → NY source. Allocation: $68,000 × 181/365 = $33,720.55 (resident-period) + $34,279.45 (nonresident, NY-source) = **$68,000**.
- **Elena — $26,778 NY wages.** During the resident period: all wages NY. During the nonresident period: her employer (NYC) **permitted** her to work fully remote — remote work at the employer's allowance, not the employee's own convenience — so post-move wages are not NY source. NY wages = $54,000 × 181/365 = $26,778.08 → **$26,778**.
- NY tax due is not computed here: the library contains no NY rate tables, only the IT-203 allocation rules. Total NY withholding of $6,752 ($3,842 + $2,910) will be carried to IT-203; any excess is refunded on IT-203 per the same excerpt.

## Reconciliation

- 1040: 122,000 + 400 − 31,050 = 91,350 (AGI); − 31,500 = 59,850 (TI); table tax 6,708; + 1,900 APTC repayment − 2,200 CTC = 6,408 (total tax); 8,730 − 6,408 = **2,322 refund**. All figures tie; nothing left open on the federal side.
- 7203: 11,500 + 11,500 (used) = 23,000 … 28,000 loss = 11,500 allowed + 16,500 suspended. Ties.
- 8582: 21,018 = 19,550 allowed + 1,468 carryforward. Ties.
- 8962: 9,900 APTC = 4,922.51 credit + 4,977.49 excess; repayment capped at 1,900. Ties.
