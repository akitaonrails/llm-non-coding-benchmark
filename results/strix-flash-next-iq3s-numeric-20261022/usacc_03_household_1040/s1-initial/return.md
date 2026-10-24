# 2025 Form 1040 — Marcus & Elena Reyes (MFJ) — return computation

Every citation below refers to a file listed in `library/INDEX.md`.
Citations: **[1040-i]** `1040_instructions_tax_computation.md` · **[TT]** `tax_table_2025_excerpt.md` · **[7203]** `form7203_instructions_excerpt.md` · **[8582]** `form8582_instructions_excerpt.md` · **[8962]** `form8962_instructions_excerpt.md` · **[IT203]** `ny_it203_part_year_excerpt.md`

Headline result: **refund of $2,322** (withholding $8,730 vs. total tax $6,408).

Important correction to the client's expectation: the S-corp loss does **not** "come straight off"
income. Only $11,500 of the $28,000 share is allowed — the rest is suspended at $11,500 of stock
basis. **[7203]** See Form 7203 section below.

---

## 1. Form 7203 — S-corp stock basis (Reyes & Pike Consulting Inc, 40%, EIN 82-4471930)

Rules applied: basis increased by contributions and income, decreased by distributions and then
losses (in that order); a shareholder guarantee of corporate debt does **not** create debt basis —
only a direct shareholder loan does; losses above basis are suspended and carried forward. **[7203]**
Marcus never lent the company money; Pike personally guarantees the bank line (documents/
marcus_basis_note.md) — no debt basis exists (and it is Pike's guarantee, not Marcus's, in any case).
Client confirmed 10/22: nothing contributed since the 2021 formation and he has never lent the
company money, so the note's basis trail is complete. (The 2024 as-filed Form 7203 was not produced —
opening basis rests on the client's note; see `STATUS.md`.)

Roll-forward of stock basis (documents/marcus_basis_note.md; 2025 loss per K-1 box 1):

| Year | Beginning | + Income | − Distributions | Ending |
|---|---:|---:|---:|---:|
| 2021 | 10,000 (contribution) | (2,100) | 0 | 7,900 |
| 2022 | 7,900 | 6,400 | 0 | 14,300 |
| 2023 | 14,300 | 9,800 | (12,000) | 12,100 |
| 2024 | 12,100 | 4,600 | (5,200) | **11,500** |

2025: loss per K-1 = (28,000). Allowed = lesser of loss and basis = **11,500**. **[7203]**
Suspended carryforward = 28,000 − 11,500 = **16,500**. Distributions never exceeded basis, so no
gain on distributions in prior years. K-1 Part II G: shareholder materially participates — the
activity is not passive, so §469 does not limit it; only §1366(d) basis does. **[7203]**, **[8582]** (line on nonpassive S-corp loss)

- `stock_basis_begin` = 11,500 · `loss_allowed` = 11,500 · `loss_suspended` = 16,500

## 2. Form 8582 — Brooklyn condo rental (318 Dean St #4B)

Net rental loss (documents/rental_summary_brooklyn.md):

- Rent: 12 × 1,500 = 18,000
- Expenses: 29,200 (cash items) + depreciation 9,818 (270,000 ÷ 27.5, per client summary) = 39,018
- **Rental loss = 18,000 − 39,018 = (21,018)** → `rental_loss` = 21,018

Elena approves tenants and arranges repairs herself → **active participation** → eligible for the
$25,000 special allowance. **[8582]**

MAGI for the phase-out = AGI **without** the passive rental loss, but reduced by the allowed
nonpassive S-corp loss **[8582]**:

- MAGI = 122,000 (wages) + 400 (interest) − 11,500 (allowed S-corp loss) = **110,900**

Special allowance = 25,000 − 50% × (MAGI − 100,000) = 25,000 − 50% × 10,900 = 25,000 − 5,450 = **19,550** (positive; MAGI < 150,000). **[8582]**

- Loss allowed = min(21,018, 19,550) = **19,550** → `loss_allowed` = 19,550
- Carryforward (Part VII) = 21,018 − 19,550 = **1,468** → `carryforward` = 1,468

Below-market rent note: rent $1,500 vs. market ~$2,600. Treated as a rental (loss allowed) per the
library's statement that renting below market to an unrelated tenant because rent was never raised
does not by itself convert the days to personal use if the rent is a fair rental for that lease.
**[8582]** Client confirmed 10/22 both stated conditions: the tenant is unrelated (a nurse found
through a broker in 2019) and the rent "was never raised." Residual risk is the library's "fair
rental for that lease" qualifier, which the library gives no threshold for — see `judgment_calls.md` #3.

## 3. Form 1040 — income lines

- **1a Wages** = 68,000 (Marcus, W-2 Reyes & Pike Consulting) + 54,000 (Elena, W-2 Halvorsen) = **122,000**
- **2b Interest** = 400 (1099-INT, Chase, Elena)
- **Pass-through (Schedule E) losses = (31,050)**: S-corp (28,000) share limited to **11,500** by
  basis (Part II above; K-1 box 1), plus rental **(19,550)** allowed under the special allowance
  (Form 8582 above).
  - *Form-mapping note:* on the actual return these go on **Form 1040 line 5** (Schedule E). The
    deliverable template has no line-5 field, so the template's `8_other_income_sch1` carries the
    −31,050; on the filed return line 8 would be 0 and line 5 = −31,050.
- **11 AGI** = 122,000 + 400 − 11,500 − 19,550 = **91,350**
- Self-check on the 8582 MAGI: MAGI excludes the PAL itself → 122,000 + 400 − 11,500 = 110,900. ✓ consistent with §2.

## 4. Form 1040 — deduction, taxable income, tax

- **12 Standard deduction** = **31,500** (MFJ 2025). **[1040-i]** Itemizing was considered and rejected
  — known deductible amounts (Tampa mortgage interest 6,480 + condo mortgage interest 11,900 +
  condo property tax 5,140 = 23,520) are already below 31,500 even before any state income tax
  deduction and the $10,000 SALT cap (the cap itself is not in the library — unverified, and it
  only makes itemizing smaller). See `judgment_calls.md` #9.
- **15 Taxable income** = 91,350 − 31,500 = **59,850**
- **16 Tax** = **6,708**. Taxable income < 100,000 → the Tax Table must be used. **[1040-i]**
  Table row "at least 59,850, less than 59,900" → 6,708. **[TT]**
  Cross-check via the table's midpoint method: midpoint of the [59,850, 59,900) bracket = 59,875;
  10% × 23,850 + 12% × (59,875 − 23,850) = 2,385 + 4,323 = 6,708. ✓ **[TT]** rate-schedule footnote

## 5. Credits and payments

- **19 Child tax credit** = **2,200** — Sofia (15) only, $2,200 per qualifying child under 17 who is
  your dependent. **[1040-i]** **Leo (9) is not claimed**: the custody order alternates years and the
  *father* claims Leo in odd-numbered years; 2025 is odd, and the library states the agreement
  controls. **[1040-i]**, documents/custody_agreement_excerpt.pdf ¶9. A child claimed by the other
  parent under a Form 8332 release is not a qualifying child for the credit. **[1040-i]**
  Elena is the custodial parent and must execute Form 8332 for Leo's father for 2025. Client confirmed
  10/22 she signed the 8332 for Leo's father — 2025 is his year. So Leo is **not** claimed; the CTC is
  Sofia only ($2,200).
- **17 Schedule 2 excess advance PTC repayment** = **1,900** (Form 8962 below).
- Tax after credits: 6,708 + 1,900 (Sch 2) = 8,608; less CTC 2,200 → **24 Total tax = 6,408**.
  (No other taxes identified; no self-employment tax — both incomes are W-2 wages.)
- **25d Withholding** = 5,120 (Marcus) + 3,610 (Elena) = **8,730**
- **34 Refund** = 8,730 − 6,408 = **2,322**

## 6. Form 8962 — Premium Tax Credit

Facts (documents/1095a_marketplace.pdf): NY of Health marketplace, policy covered Marcus, Elena,
Sofia, Leo. **Coverage months: January–June only** — monthly A enrollment premium 1,720.00,
B SLCSP 1,690.00, C APTC 1,650.00; annual line 33 totals 10,320 / 10,140 / 9,900 = exactly 6 × the
monthly amounts, confirming 6 covered months. Elena's W-2 box 12 code DD of 7,140.00 is flagged
"Jul–Dec employer coverage," consistent with marketplace coverage ending in June. Client confirmed
10/22: Elena enrolled on Halvorsen's plan July 1 when they moved and they dropped the marketplace plan,
so coverage is 6 months and there is no second 1095-A.

- **Household income** = modified AGI = AGI 91,350 (no tax-exempt interest, nontaxable SS, or
  excluded foreign income in the file) = **91,350** **[8962]**
- **FPL** (2025, family of 4, 48 states) = **31,200** **[8962]** — family of 4 matches the four
  covered individuals on the 1095-A (see `judgment_calls.md` #6).
- **FPL %** = 91,350 ÷ 31,200 = 2.92788… → **292.79%** (band 250–300%)
- **Applicable figure** (Table 2, linear: 4.00% + 2.00% × (292.79 − 250) ÷ 50) =
  4.00 + 2.00 × 0.85577 = **5.7115%** **[8962]**
- Contribution amount = 91,350 × 5.7115% = **5,217.49**/yr → 434.79/month
- Monthly PTC = lesser of enrollment premium 1,720.00 and SLCSP − contribution
  (1,690.00 − 434.79 = 1,255.21) = **1,255.21** **[8962]**
- **Annual PTC** = 6 covered months × 1,255.21 = **7,531.26** → **7,531**
- **APTC** (1095-A line 33C) = **9,900.00**
- **Excess** = 9,900.00 − 7,531.26 = **2,368.74** → **2,369**
- **Repayment limitation**: household income at 292.79% FPL → 200%–<300% band → MFJ cap **$1,900**. **[8962]**
- **Repayment** = min(2,369, 1,900) = **1,900** → Form 8962 line 29 → Schedule 2 line 2 → **Form 1040 line 17 = 1,900**

(Without the cap the repayment would have been 2,369; the limitation saves 469.)

## 7. New York part-year (IT-203) — allocation only

Rules: part-year resident taxed on all income in the resident period plus NY-source income in the
nonresident period; wages paid by a NY employer for work performed out of state are NY source under
the **convenience of the employer** rule unless the out-of-state work is at the employer's
necessity. **[IT203]**

- **Resident days** = Jan 1 – Jun 30, 2025 = **181** (of 365; 2025 is not a leap year). NY lease
  ended June 30 and the family was out; FL closing July 3 (documents/email_move_dates.txt).
  Queens nights June 28–30 fall inside the resident period either way. Client had no additional
  information on July 1–2 physical presence — the June 30 assumption stands and is immaterial to the
  wages (full-year NY source either way, below) and to the rental (NY-source all year).
- **Marcus NY wages = 68,000 (full year)**: employer Reyes & Pike Consulting is a NY employer; he
  now works remotely from Florida after the move — a personal, not employer-driven, arrangement →
  convenience of the employer → NY source for the whole year. **[IT203]** Client confirmed 10/22: he
  *asked* to move, the company "said remote was fine… they didn't need me out of state" —
  employee-initiated, so not employer necessity.
- **Elena NY wages = 54,000 (full year)**: Halvorsen Media Group (NY) "let me go fully remote" —
  again employee convenience → NY source all year. **[IT203]** Client confirmed 10/22: Halvorsen
  closed its Tampa office years ago and *approved her request* — approval of an employee-initiated
  arrangement is convenience, not necessity. (Residual argument, rejected: a location-independent
  job "requires" no office; the library keys the exception to days worked at the employer's
  necessity, which approval of the employee's move does not establish.)
- The Brooklyn rental income/loss is NY-source real property income for the whole year as well
  (NY property); the rental is reported federally on the MFJ return above.
- **NY tax is not computed**: the library contains no NY rate schedules or IT-203 worksheets, so any
  NY tax figure would be unverifiable. Both employers withheld NY tax all year (3,842 + 2,910 = 6,752)
  because the withholding forms were never updated. **[IT203]** states only that tax withheld in
  excess of the tax due is refunded on IT-203 — whether an overpayment even exists is indeterminate
  here: under the convenience rule nearly all wages stay NY-source for the full year, broadly
  consistent with the full-year withholding. No NY refund (or balance due) is asserted.

## 8. Items outside the library (not applied — labeled unverified)

- **QBI deduction (IRC §199A)**: nothing in the library covers it, so no QBI deduction is claimed;
  whether one is available for the wages/rental/S-corp items is unverified here.
- **$10,000 SALT cap**, itemized-deduction rules, NY tax rates, EITC: not in the library; not used
  (EITC at AGI 91,350 with two children would in any case require tables the library lacks).
- Deduction mapping line 5 vs. line 8 — form mechanics noted in §3.

## 9. Reconciliation note

Nothing was forced to balance: the 8582 MAGI (110,900), AGI (91,350), and 8962 household income
(91,350) are each computed from the same components under their own definitions and agree with
their definitions as stated in the library **[8582]**, **[8962]**. The remaining assumptions (Leo's
8332 and the convenience-of-the-employer facts are now client-confirmed; the residency end date is
not obtainable) are documented assumptions, never reconciling plugs — see `QUESTIONS.md` and
`STATUS.md`.

## 10. Client responses (turn 2) — resolution of open items

The client answered five of the eight questions. Effect on the figures:

| Item | Client response | Effect on return |
|---|---|---|
| Rental tenant | Unrelated (nurse via broker, 2019); rent never raised | **Confirms** the §469(i) loss treatment (**[8582]**); no change |
| S-corp contributions/loans | Nothing added since 2021; Pike guarantees line, no shareholder loan | **Confirms** 11,500 basis / no debt basis (**[7203]**); no change |
| Convenience of the employer (both spouses) | Both employee-initiated; employers "didn't need" / merely approved | **Confirms** full-year NY-source wages 68,000 / 54,000 (**[IT203]**); no change |
| Leo Form 8332 | Elena signed it to the father for 2025 (his year) | **Confirms** Leo not claimed; CTC = Sofia only (**[1040-i]**); no change |
| Marketplace coverage end | Dropped the marketplace plan; Elena on Halvorsen's plan from July 1 | **Confirms** 6-month coverage; no second 1095-A (**[8962]**); no change |

**No federal figure changed.** Refund remains **$2,322**. The answers confirm every material
assumption; they do not alter any number.

**Remaining unknowns (client has no further information) — flagged, not plugged:**

1. **NY resident-period end date (July 1–2 physical presence).** Unresolved. Kept at Jun 30 (181 days).
   Immaterial here: wages are full-year NY source and the rental is NY-source all year, so the day
   count does not move the (uncomputed) NY allocation. See `QUESTIONS.md` unknown D.
2. **Prior-year (2024) as-filed Form 7203 basis trail.** Not produced. Opening basis 11,500 rests on
   Marcus's note, now corroborated by his statement that nothing changed since 2021. See unknown B.
3. **"Fair rental for that lease" threshold** for the below-market condo. The library states the
   carve-out but gives no dollar threshold for whether $1,500 qualifies when market is ~$2,600. Client
   confirmed the two conditions the library names (unrelated tenant, never raised); the residual
   characterization risk stands. See unknown C and `judgment_calls.md` #3.
4. **Other income/deductions not in the file** (Tampa property tax/HOA, other accounts, child support,
   HSA, retirement catch-ups). Client says none. Itemizing still cannot beat 31,500 on these facts.
   See unknown E.
5. **NY tax is still not computed** — no NY rate schedules/worksheets in the library (**[IT203]**
   excerpt is allocation-only). This is a library limitation, not an open client fact.
