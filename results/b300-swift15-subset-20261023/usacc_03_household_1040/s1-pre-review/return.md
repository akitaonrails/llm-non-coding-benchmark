# 2025 Federal Return + NY Part-Year Allocation — Marcus & Elena Reyes (MFJ)

Computation detail for every figure in `return.json`. All citations point to files listed in
`library/INDEX.md`. No outside authorities were used.

**Client file used:** `documents/` — W-2 (Marcus, Reyes & Pike), W-2 (Elena, Halvorsen),
K-1 (Reyes & Pike Consulting Inc), Marcus's stock basis note, Brooklyn rental summary,
1099-INT (Chase, $400), 1095-A (NY State of Health), 1098 (Tampa mortgage), custody
agreement excerpt, and Elena's email with move dates.

---

## 1. Form 7203 — S corporation stock basis (Reyes & Pike Consulting Inc)

Authority: `library/form7203_instructions_excerpt.md` (IRS Form 7203 Instructions 2025) —
loss allowed only to the extent of adjusted stock basis plus debt basis; excess suspended
and carried forward; basis increases with contributions and income, decreases with
distributions then losses; a guarantee of corporate debt does **not** create debt basis.

Reconstructing stock basis from `documents/marcus_basis_note.md`:

| Year | Income/(loss) | Distributions | Ending basis |
|---|---:|---:|---:|
| 2021 (formation) | (2,100) | 0 | 10,000 − 2,100 = **7,900** |
| 2022 | 6,400 | 0 | 7,900 + 6,400 = **14,300** |
| 2023 | 9,800 | (12,000) | 14,300 + 9,800 − 12,000 = **12,100** |
| 2024 | 4,600 | (5,200) | 12,100 + 4,600 − 5,200 = **11,500** |
| **2025 begin** | | | **11,500** |

- Debt basis = **0**: Marcus never lent the company money; the bank line is personally
  guaranteed by Pike, which does not create debt basis (7203 excerpt, para. 1).
- 2025 K-1 loss: **$28,000** (`documents/k1_1120s_reyes_pike.pdf`, box 1); 2025 distributions: 0.
- **Loss allowed** = min(28,000; 11,500 + 0) = **$11,500**.
- **Loss suspended** = 28,000 − 11,500 = **$16,500** (carried forward indefinitely).
- Ending stock basis = 11,500 − 11,500 = **$0**.

This is why the loss does **not** "come straight off": only $11,500 of the $28,000 is
deductible in 2025. See `judgment_calls.md`, item 1.

## 2. Form 8582 — Brooklyn condo rental (passive activity)

Authority: `library/form8582_instructions_excerpt.md` (IRS Form 8582 Instructions 2025;
IRC §469(i)) — $25,000 special allowance for actively participated rentals, reduced 50%
per dollar of MAGI over $100,000 (zero at $150,000, MFJ); MAGI excludes passive losses
but **includes** nonpassive losses such as a materially participating S-corp loss to the
extent basis-allowed; disallowed loss carried forward in Part VII; below-market rental
carve-out for unrelated tenants.

Rental activity (from `documents/rental_summary_brooklyn.md`):

```
Rent received              18,000
Expenses (per summary)    29,200   (11,900 + 7,860 + 5,140 + 2,350 + 1,150 + 800)
Depreciation              (9,818)   (270,000 ÷ 27.5 = 9,818.18, as stated in the file)
Rental loss              (21,018)
```

- Active participation: Elena handles everything herself (approves tenants, arranges
  repairs) → qualifies for the special allowance.
- Below-market rent ($1,500 vs ~$2,600 market): treated as a bona fide lease to an
  **unrelated** tenant; the lease's rent was not raised as market rose, which the 8582
  excerpt states does not by itself trigger the IRC §280A(d)(2)(C) personal-use rule.
  See `judgment_calls.md`, item 2.
- **MAGI** = wages + interest − basis-allowed S-corp loss, **excluding** the passive
  rental loss (8582 excerpt, para. 2):
  `122,000 + 400 − 11,500 = 110,900`.
- Phase-out = 50% × (110,900 − 100,000) = 50% × 10,900 = **5,450**.
- **Special allowance** = 25,000 − 5,450 = **19,550** (MAGI < 150,000, so not zeroed).
- **Loss allowed** = min(21,018; 19,550) = **19,550**.
- **Carryforward** (Part VII) = 21,018 − 19,550 = **1,468**.

## 3. Form 1040 (federal)

Authority: `library/1040_instructions_tax_computation.md` (IRS 2025 Form 1040
Instructions) and `library/tax_table_2025_excerpt.md` (IRS 2025 Tax Table).

| Line | Item | Arithmetic | Amount |
|---|---|---|---:|
| 1a | Wages | 68,000 (Marcus W-2 box 1) + 54,000 (Elena W-2 box 1) | **122,000** |
| 2b | Interest | 1099-INT box 1 (Chase) | **400** |
| 8 (Sch 1) | Other income, net | S-corp loss (11,500) + rental loss (19,550) | **(31,050)** |
| 11 | AGI | 122,000 + 400 − 31,050 | **91,350** |
| 12 | Deduction | Standard deduction, MFJ = 31,500 (1040 Instructions). Itemized for comparison: 6,480 Tampa mortgage interest (1098) + 3,842 + 2,910 NY state tax withheld = 13,232 < 31,500 → standard wins | **31,500** |
| 15 | Taxable income | 91,350 − 31,500 | **59,850** |
| 16 | Tax | Tax Table, MFJ: 59,850 falls in the "at least 59,850 / but less than 59,900" bracket → **6,708**. (Table must be used: taxable income < 100,000 per 1040 Instructions) | **6,708** |
| 17 (Sch 2) | Excess APTC | Form 8962, below | **1,900** |
| 19 | Child tax credit | 2,200 × 1 qualifying child (Sofia, 15) (1040 Instructions: $2,200 per qualifying child under 17) | **2,200** |
| 24 | Total tax | 16 + 17 = 6,708 + 1,900 | **8,608** |
| 25d | Withholding | 5,120 (Marcus W-2 box 2) + 3,610 (Elena W-2 box 2) | **8,730** |
| 34 | Refund | (25d + 19) − 24 = (8,730 + 2,200) − 8,608 | **2,322 (refund)** |

Notes:
- No estimated tax payments, prior-year credits, or other payments appear in the file;
  none are assumed (25a–25c = 0).
- The simplified schema maps `34` as: payments + credits minus total tax (positive =
  refund). If a figure on this return changes, recompute the chain above.

## 4. Form 8962 — Premium Tax Credit

Authority: `library/form8962_instructions_excerpt.md` (IRS Form 8962 Instructions 2025;
Rev. Proc. 2024-35; Rev. Proc. 2024-40).

Inputs: `documents/1095a_marketplace.pdf` — family of 4 (Marcus, Elena, Sofia 15, Leo 9);
SLCSP premium (annual B) **$10,140**; enrollment premium (annual A) **$10,320**;
advance PTC (annual C) **$9,900**.

- **Household income** = MAGI of the household (no tax-exempt interest, nontaxable
  Social Security, or excluded foreign income in the file) = AGI = **91,350**.
- FPL (2025, family of 4, 48 contiguous states) = **31,200** (8962 excerpt).
- **FPL %** = 91,350 ÷ 31,200 = 2.927885 → **292.79%**.
- **Applicable figure %** — 292.79% is in the 250–300% band (4.00% → 6.00%, linear):
  4.00% + (292.7885 − 250) × (2.00 ÷ 50)% = 4.00% + 42.7885 × 0.04% = 4.00% + 1.7115% =
  **5.7115%**.
- Monthly contribution amount = 91,350 × 5.7115% ÷ 12 = 5,217.49 ÷ 12 = **434.79**.
- Monthly PTC = lesser of (a) enrollment premium 10,320 ÷ 12 = 860.00 and
  (b) SLCSP 10,140 ÷ 12 = 845.00 − 434.79 = **410.21** → 410.21.
- **Annual PTC** = 410.21 × 12 = 4,922.51 → **4,923** (rounded to the dollar).
- **APT C** = 9,900 (1095-A line 33C).
- **Excess** = 9,900 − 4,923 = **4,977**.
- **Repayment limitation** — household income 292.79% of FPL is in the 200%–<300% band
  (MFJ) → **1,900** (8962 excerpt, line 28).
- **Repayment** = min(4,977; 1,900) = **1,900** → flows to Sch 2 / 1040 line 17.

Eligibility check: household income 292.79% of FPL < 400%, so the family is eligible for
the credit.

## 5. Dependents

Authority: `library/1040_instructions_tax_computation.md` (IRS 2025 Form 1040
Instructions) — where a decree or agreement alternates years, the agreement controls
which parent claims the child; a child claimed by the other parent under a Form 8332
release is not your qualifying child for the credit.

- **Sofia Reyes (15)** — the Reyeses' child, covered on the 1095-A, lives with them.
  Qualifying child and dependent → claimed here (drives the $2,200 CTC).
- **Leo Castellano (9)** — Elena's son from a prior relationship; resides primarily with
  the mother. `documents/custody_agreement_excerpt.pdf` ¶9: parents **alternate** —
  Father claims in **odd** years, Mother in **even** years. 2025 is odd → the **father
  claims Leo**. The Reyeses do **not** claim Leo for 2025, and no additional CTC is
  taken for him. See `judgment_calls.md`, item 3.

Dependents on this return: **Sofia Reyes (age 15)**.

## 6. New York — part-year resident allocation

Authority: `library/ny_it203_part_year_excerpt.md` (NYS IT-203-I (2025)) — part-year
residents are taxed on all income received during the resident period plus NY-source
income during the nonresident period; wages for services performed entirely outside NY
are not NY-source **except** under the "convenience of the employer" rule (NY employer +
out-of-state remote work for the employee's own convenience = NY source).

- **Resident period:** Jan 1 – Jun 30, 2025 (Brooklyn lease ended 6/30; Tampa closed
  7/3 and they moved in that weekend — `documents/email_move_dates.txt`).
  Jan 31 + Feb 28 + Mar 31 + Apr 30 + May 31 + Jun 30 = **181 resident days**.
- **Wages — 100% NY-source:**
  - Marcus: NY employer (Reyes & Pike, 1 Liberty Plaza, NYC), now working remotely from
    FL for his own convenience → convenience-of-the-employer rule → **68,000** NY wages
    (matches W-2 boxes 15/16/17: NY, 68,000, 3,842 withheld).
  - Elena: NY employer (Halvorsen Media Group, 230 Park Ave S, NY), fully remote from
    FL for her own convenience → same rule → **54,000** NY wages (matches W-2: NY,
    54,000, 2,910 withheld).
- **Method (as stated in `return.json`):** no day-count allocation of wages is required
  because the convenience-of-the-employer rule makes the entire year's wages NY-source;
  NY taxes all income received during the 181-day resident period plus NY-source income
  after 6/30. Both employers withheld NY tax all year (per Elena's email, nobody
  updated W-4s), and the W-2s confirm 100% of wages reported as NY.
- Open item: the $400 interest (Chase) — the 1099-INT does not state the payer's
  location or the date(s) credited. If any of it was received after 6/30, its NY
  source must be confirmed for the IT-203; if received during the resident period it is
  NY income regardless of source. This does not affect the federal figures above.
  See `STATUS.md`.

The requested NY deliverable fields (days, per-spouse NY wages, method) are complete; a
full IT-203 tax computation (state rates not in the library) is out of scope.

## 7. Reconciliation

- AGI: 122,400 − 11,500 − 19,550 = 91,350 ✓
- Taxable income 59,850 lies inside the tax-table excerpt range (59,000–61,000), so the
  table lookup is verifiable from the library ✓
- Total tax 8,608 vs payments+credits 10,930 → refund 2,322 ✓
- All figures tie to `return.json`; nothing was forced to balance.
