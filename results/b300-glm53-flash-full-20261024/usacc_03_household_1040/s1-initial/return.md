# 2025 Form 1040 — Marcus and Elena Reyes (MFJ) — figures and arithmetic

All citations are to files in `library/INDEX.md`. Line numbers follow the schema in `../CONTRACT.md`.

## Income

**Line 1a — wages: $122,000**
- Marcus W-2, Reyes & Pike Consulting Inc: $68,000 (`documents/w2_marcus_reyes_pike.pdf`)
- Elena W-2, Halvorsen Media Group LLC: $54,000 (`documents/w2_elena_reyes.pdf`)
- 68,000 + 54,000 = 122,000

**Line 2b — taxable interest: $400** — Chase 1099-INT to Elena (`documents/1099int_chase.pdf`). No tax-exempt interest is documented, so household income later equals AGI.

**Schedule 1 — net additional income: −$31,050** (flows to 1040 line 8). Components:

1. **S corporation ordinary loss, allowed portion: −$11,500.** K-1 (Form 1120-S) box 1 shows a $(28,000) ordinary loss, Marcus 40%, materially participates = Yes (`documents/k1_1120s_reyes_pike.pdf`). Basis limits the deduction — see Form 7203 below (`form7203_instructions_excerpt.md`, §1366(d) as excerpted).
2. **Rental loss, allowed after Form 8582: −$19,550.** See Form 8582 below.
3. Total: −11,500 − 19,550 = **−31,050**.

Both pass through Schedule E (rental Part I / S-corp Part II) → Schedule 1 → 1040 line 8.

**AGI (line 11): $91,350** = 122,000 + 400 − 11,500 − 19,550 = 91,350. No above-the-line deductions are documented (no SE income, no HSA, student loan, or IRA items in the file).

## Deduction (line 12)

Standard deduction MFJ 2025 = **$31,500** (`1040_instructions_tax_computation.md`).

Itemized alternative: Tampa home mortgage interest (1098, acquired 07/03/2025) $6,480 + NY state income tax withheld (3,842 + 2,910 = 6,752) = 13,232 < 31,500. The property tax on the Brooklyn condo ($5,140) is already deducted on Schedule E and cannot be itemized again. **Standard deduction claimed: 31,500.**

## Taxable income and tax

- **Line 15: 91,350 − 31,500 = $59,850.**
- **Line 16 tax: $6,708.** Taxable income is under $100,000, so the TaxTable must be used, not a rate schedule (`1040_instructions_tax_computation.md`). Bracket "59,850–59,900" MFJ → 6,708 (`tax_table_2025_excerpt.md`).

## Child tax credit (line 19)

- Sofia, age 15 (under 17 at year-end, their dependent): **$2,200** (`1040_instructions_tax_computation.md` CTC rule).
- Leo, age 9, Elena's son: **not claimed.** The custody agreement assigns odd-numbered years to the father (`documents/custody_agreement_excerpt.pdf`); the library confirms the agreement controls and a child claimed by the other parent under a Form 8332 release is not your qualifying child.
- **Line 19 = $2,200.** (Unused credit here: tax = 6,708 ≥ 2,200 so the credit is absorbed fully; any refundable/other-dependent credit mechanics are not in the library and are not invoked.)

## Form 7203 — S corporation basis (basis note and K-1)

Stock basis roll-forward (capital/income increase, then distributions, then losses — `form7203_instructions_excerpt.md`):

| Year | Event | Running stock basis |
|---|---|---:|
| 2021 | +10,000 contribution | 10,000 |
| 2021 | −2,100 loss | 7,900 |
| 2022 | +6,400 income | 14,300 |
| 2023 | +9,800 income | 24,100 |
| 2023 | −12,000 distribution | 12,100 |
| 2024 | +4,600 income | 16,700 |
| 2024 | −5,200 distribution | 11,500 |

**Beginning 2025 stock basis: $11,500.** Debt basis: **$0** — Marcus never lent the company money; the bank line is personally guaranteed by the other shareholder, and a guarantee does not create debt basis (`form7203_instructions_excerpt.md`).

- Loss allowed (line 11 logic) = lesser of loss 28,000 and basis 11,500 + 0 = **$11,500**.
- **Suspended/carryover: 28,000 − 11,500 = $16,500** (Part I line 12 et seq.; indefinite carryforward).

Marcus's expectation that the loss "comes straight off" income was half right: it is nonpassive (materially participates per K-1 Part II G), so it is not a passive loss, but **basis caps it at 11,500**.

## Form 8582 — passive activity loss limitation (rental)

Loss before limitation (`documents/rental_summary_brooklyn.md`): 18,000 − (29,200 expenses + 9,818 depreciation) = **−21,018**.

Elena actively participates (approves tenants, arranges repairs), so the §469(i) special allowance applies (`form8582_instructions_excerpt.md`):

- **MAGI** = AGI without passive losses = 122,000 + 400 − 11,500 (allowed nonpassive S-corp loss reduces MAGI per the excerpt) = **110,900**.
- **Special allowance** = 25,000 − 50% × (110,900 − 100,000) = 25,000 − 5,450 = **19,550**.
- **Loss allowed** = lesser of 21,018 and 19,550 = **19,550**.
- **Carryforward** (Part VII) = 21,018 − 19,550 = **1,468**.

Below-market-rent screening: the tenant is unrelated and the rent prevailed because it was never raised, which the excerpt treats as a fair rental for that lease, not personal use.

## Form 8962 — premium tax credit (1095-A Jan–Jun, 4 covered individuals)

- **Household income** = MAGI = AGI 91,350 + tax-exempt interest 0 = **91,350** (`form8962_instructions_excerpt.md`).
- **FPL %** = 91,350 / 31,200 (family of 4, 48 states) × 100 = **292.8%**.
- **Applicable figure**: in the 250–300% band (4.00%→6.00%, linear): 4.00 + 2.00 × (292.788 − 250)/50 = **5.7115%**.
- **Expected contribution** = 91,350 × 5.7115% / 100 = 5,217.49 → monthly 434.79.
- **Monthly PTC** = lesser of enrollment premium 1,720 and (SLCSP 1,690 − 434.79 = 1,255.21) = 1,255.21, for the 6 covered months → **annual PTC = 7,531.25 ≈ 7,531**.
- **APTC paid: $9,900** (line C).
- **Excess APTC** = 9,900 − 7,531.25 = **2,368.75 ≈ 2,369**.
- **Repayment limitation**: household income is 292.8% FPL, in the 200%–<300% band → **$1,900** cap for MFJ.
- **Repayment (Schedule 2 / 1040 line 17): $1,900.** The remaining 468.75 of the excess is simply lost (not repaid).

## Other taxes, total tax, payments

- **Line 17 (Schedule 2, excess APTC): $1,900.**
- **Line 24 total tax** = tax 6,708 − CTC 2,200 = 4,508, + 1,900 = **6,408**.
- **Line 25d withholding** = 5,120 + 3,610 = **8,730**.
- **Line 34 refund** = 8,730 − 6,408 = **$2,322 refund.**

## New York part-year (IT-203)

- **Resident period**: Jan 1 – Jun 30, 2025 (Brooklyn lease ended June 30; Tampa closing 07/03). The June 28–30 stay in Queens is inside New York. **Resident days: 181.** After June 30: nonresident, FL domicile.
- **Marcus — $68,000 NY wages (all of it).** His employer (Reyes & Pike) is in New York City and the relocation was his own request — "the company said remote was fine when I asked to move; they didn't need me out of state." Remote out-of-state work at the employee's convenience is New York source under the convenience-of-the-employer rule (`ny_it203_part_year_excerpt.md`), matching the employer's full-year NY withholding.
- **Elena — $54,000 NY wages (all of it).** The client's answer to Q3 establishes who requested the arrangement: Elena asked to go fully remote and Halvorsen approved the request (they have no Tampa office — closed years ago — but they did not *direct* the relocation). At the employee's own convenience, her post-move Florida wages are also New York source. Convenience, not necessity, controls.
- The first-turn workday allocation (129/261 → $26,690) is superceded by the client's answers and is no longer used; no allocation schedule is required because neither spouse has a non-NY-source wage component.
- NY withheld on NY wages (3,842 + 2,910 = 6,752) is compared with the New York tax due on IT-203 and any excess refunded; **the New York tax and refund cannot be computed from this library** (no NY rate table is in it) and remain an explicit unknown.
- Open/unverified: whether the Brooklyn condo's Jul–Dec rental receipts are "New York source income" for the nonresident column. The library defines the column but does not enumerate NY-source items (e.g., real property located in New York); that specific rule is **not in the library** and is flagged rather than cited.
