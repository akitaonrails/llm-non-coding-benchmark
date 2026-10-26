# 2025 Federal Form 1040 + NY Part-Year — Marcus & Elena Reyes (MFJ)

Prepared from `workspace/documents/` using only `workspace/library/` as authority. Every citation below
is a file listed in `library/INDEX.md`. Assumptions are flagged with **[ASSUMPTION]** and analyzed in
`judgment_calls.md`; open client questions are in `QUESTIONS.md`.

**Headline:** AGI $91,350 → taxable income $59,850 → total tax $6,408 vs. withholding $8,730 →
**federal refund $2,322**. Marcus's expectation that the $28,000 S-corp loss "comes straight off" income
is **wrong**: only $11,500 is allowed (stock-basis limit), $16,500 suspends.

---

## 1. Form 7203 — S-corp loss (Reyes & Pike Consulting Inc, Schedule K-1: ordinary loss $(28,000), 40%)

Authority: `form7203_instructions_excerpt.md` — loss allowed only to extent of adjusted stock + debt
basis (§1366(d)); excess suspends indefinitely; a guarantee of corporate debt does **not** create debt
basis, only a direct shareholder loan does. Pike's personal guarantee of the bank line therefore adds
nothing; Marcus confirms he never lent the company money.

Stock-basis rollforward from Marcus's note (`marcus_basis_note.md`) **[ASSUMPTION A1: the note faithfully
reproduces prior-year Forms 7203 and no loss was suspended in 2021–2024. Marcus now confirms he has made
no capital contribution and no loan to the company since 2021, but the prior-year filed returns are not
available (client has no further information) — residual open item R1]**. Basis is increased by contributions/income, then decreased by
distributions and losses, in that order:

| Step | Amount | Running basis |
|---|---:|---:|
| 2021 contribution | +10,000 | 10,000 |
| 2021 loss | (2,100) | 7,900 |
| 2022 income | +6,400 | 14,300 |
| 2023 income | +9,800 | 24,100 |
| 2023 distribution | (12,000) | 12,100 |
| 2024 income | +4,600 | 16,700 |
| 2024 distribution | (5,200) | **11,500** |

- **Line 1 stock basis, beginning of 2025: $11,500**
- 2025 loss $28,000 vs. basis $11,500 → **loss allowed: $11,500** (lesser of loss and basis, Part I line 11)
- **Suspended carryforward: $28,000 − $11,500 = $16,500**

(K-1 line 17 gross receipts $612,400 is informational; unused.)

## 2. Rental (318 Dean St #4B, Brooklyn) — Schedule E / Form 8582

Per `rental_summary_brooklyn.md`; Elena actively participates (she handles everything).

- Rent received: 12 × $1,500 = $18,000
- Expenses: 11,900 + 7,860 + 5,140 + 2,350 + 1,150 + 800 = $29,200; depreciation $270,000 ÷ 27.5 = $9,818
- **Rental loss: 18,000 − 29,200 − 9,818 = $(21,018)**

**Below-market rent ($1,500 vs ~$2,600 market).** The library's §280A(d)(2)(C) excerpt would reclassify
all days as personal use (no loss) if the dwelling is rented below fair rental value — **but** it exempts
below-market rent to an *unrelated* tenant where *the rent was simply never raised*, if the rent is a
fair rental for that lease. **[A2 — now client-corroborated: the tenant is "a stranger, a nurse we
found through a broker in 2019" and "we just never raised the rent" — precisely the library carve-out's
fact pattern. The lease document itself remains not-in-file and the client has no further information;
the "fair rental for that lease" proviso stays unverifiable — residual open item R2]** — loss preserved.
See `judgment_calls.md` §3.

Form 8582 special allowance (`form8582_instructions_excerpt.md`): up to $25,000 against nonpassive
income, reduced 50% by MAGI over $100,000. MAGI is AGI **without** the passive loss but **reduced by**
allowed nonpassive losses — Marcus's K-1 Part II G states "Shareholder materially participates: Yes," so
the $11,500 S-corp loss is nonpassive and reduces MAGI:

- MAGI = wages 122,000 + interest 400 − S-corp allowed loss 11,500 = **$110,900**
- Allowance = 25,000 − 50% × (110,900 − 100,000) = 25,000 − 5,450 = **$19,550**
- **Rental loss allowed: $19,550; carryforward (Part VII): 21,018 − 19,550 = $1,468**

## 3. Form 1040 lines

| Line | Figure | Arithmetic / authority |
|---|---:|---|
| 1a Wages | 122,000 | Marcus W-2 68,000 + Elena W-2 54,000 |
| 2b Interest | 400 | 1099-INT (Chase, Elena; joint return) |
| 8 Other income (Sch 1) | (31,050) | S-corp nonpassive loss (11,500) + allowed rental loss (19,550) |
| 11 AGI | 91,350 | 122,000 + 400 − 31,050 |
| 12 Deduction | 31,500 | MFJ standard deduction, `1040_instructions_tax_computation.md`. Itemizing would need only ~$6,480 mortgage interest (Form 1098, partial year) + property taxes + NY withholding — nowhere near 31,500 even before the SALT cap; Schedule A rules are **not in the library**, but standard clearly wins. |
| 15 Taxable income | 59,850 | 91,350 − 31,500 |
| 16 Tax | 6,708 | TI < $100,000 ⇒ **must** use Tax Table (`1040_instructions_tax_computation.md`); row "at least 59,850 / less than 59,900" MFJ = **$6,708** (`tax_table_2025_excerpt.md`). Midpoint check: 10%×23,850 + 12%×(59,875−23,850) = 2,385 + 4,323 = 6,708 ✓ |
| 19 CTC | 2,200 | $2,200 × 1 child. Sofia (15) qualifies. Leo is claimed by his father in 2025 (odd year) under the alternating custody decree — "where a decree or agreement alternates years, the agreement controls," and a child claimed by the other parent under Form 8332 is not your qualifying child (`1040_instructions_tax_computation.md`). **[CONFIRMED: Elena executed the
Form 8332 release for 2025 (client statement) — the father claims Leo; he is not our qualifying child]** |
| 17 Sch 2 excess APTC | 1,900 | Form 8962 repayment (section 4) |
| 22 After credits | 4,508 | 6,708 − 2,200 |
| 24 Total tax | 6,408 | 4,508 + 1,900 |
| 25d Withholding | 8,730 | Marcus 5,120 + Elena 3,610 (federal) |
| 34 Refund | **2,322** | 8,730 − 6,408 |

## 4. Form 8962 — Premium Tax Credit (NY State of Health, coverage Jan–Jun only)

1095-A: monthly enrollment premium $1,720; monthly SLCSP $1,690; APTC $1,650/mo; totals A $10,320,
B $10,140, C $9,900 (6 covered months; Halvorsen employer coverage began July — W-2 box 12 DD).

Authority: `form8962_instructions_excerpt.md`.

- Household income = AGI (no tax-exempt interest, nontaxable SS, or excluded foreign income in file) = **$91,350**
- FPL, family of 4, 2025: $31,200 → 91,350 ÷ 31,200 = **292.79% FPL** **[ASSUMPTION A4: family of 4 per 1095-A; the library gives no other FPL row]**
- Applicable figure, 250–300% band, linear: 4.00% + (292.79 − 250)/50 × (6.00 − 4.00)% = **5.7115%** (5.71%)
- Annual contribution = 91,350 × 5.7115% = 5,217.49; monthly = 5,217.49 ÷ 12 = **434.79**
- Monthly PTC = lesser of (a) enrollment premium 1,720 and (b) SLCSP 1,690 − 434.79 = 1,255.21 → **1,255.21**
- **Annual PTC = 1,255.21 × 6 = 7,531.25 → $7,531**
- APTC = **$9,900**; excess = 9,900 − 7,531 = **$2,369**
- Repayment limitation (MFJ, household income 200%–<300% FPL): **$1,900** (no limitation applies only at ≥400%)
- **Repayment = min(2,369, 1,900) = $1,900** → Form 1040 line 17 (Schedule 2). Since APTC > PTC, no credit on line 21.

The advance payments were set assuming much higher income (pre-loss); the S-corp and rental losses
dropped income into the 200–300% band, so the household keeps the benefit of $9,900 − 1,900 = $8,000 of
premium assistance against a $7,531 entitlement.

## 5. New York — Form IT-203 part-year

Authority: `ny_it203_part_year_excerpt.md`.

- **Resident period: Jan 1 – Jun 30 = 181 days** (Brooklyn lease ended 6/30, apartment surrendered;
  domicile abandoned — 3 nights at Elena's mother in Queens 6/28–30 is temporary lodging, not a
  maintained abode). Alternative end date 7/3 (Tampa close, 184 days) — `judgment_calls.md` §5. Client
  supplied no further facts on keys/occupancy after 6/30; 6/30 retained (residual open item R3).
- **Marcus NY wages: $68,000 (full year).** Jan–Jun he worked in NY (home office, Brooklyn) — NY source
  anyway. Jul–Dec from Florida for an NYC employer, remote at his own convenience → convenience-of-the-employer
  rule makes the wages NY source. Client confirms: he asked to move and "the company said remote was fine…
  they didn't need me out of state" — employee convenience, not employer necessity.
- **Elena NY wages: $54,000 (full year).** Same analysis; Halvorsen Media (230 Park Ave S, NY) let her go
  fully remote — her own request, approved after Halvorsen closed its Tampa office years ago — client
  confirms employee convenience, not necessity.
- Method: ratio of NY resident days (181/365) plus day-for-day sourcing of wages; the convenience rule
  makes both W-2s 100% NY source, so the day ratio does not shrink wages. Brooklyn rental income is NY
  property income in both periods; the $400 interest is NY-source only in the resident period.
- NY withholding of 3,842 + 2,910 = $6,752 is refunded to the extent it exceeds IT-203 tax ("tax withheld
  in excess of the tax due is refunded on IT-203"). **NY tax and refund not computed — no NY rate
  schedule or deduction rules in the library** (unverified what they are; stated, not cited).
- Both W-2s' NY withholding was correct-by-accident: per the convenience rule, the full-year wage
  sourcing matches the full-year withholding.

## 6. Dependents

- **Sofia Reyes, age 15** — the couple's child; under 17 → qualifying child + CTC $2,200.
- **Leo Castellano, age 9** (DOB 3/14/2016, Elena's son) — **not claimed in 2025**: custody decree
  ¶9 alternates years; father claims odd years, and 2025 is odd. Custodial parent must execute Form 8332
  for the father. The library states the agreement controls. Leo was still a 1095-A covered individual —
  that is unaffected by the dependency swap (and family-of-4 FPL is retained per A4).

## 7. Reconciliation check

Total income items: 122,000 + 400 − 11,500 − 19,550 = 91,350 = line 11 ✓; 91,350 − 31,500 = 59,850 ✓;
59,850 lands inside the library's tax-table excerpt ✓. Nothing forced; everything ties.

## 8. Client responses (round 1) — effect on figures

| Client answer | Effect |
|---|---|
| Tenant is a stranger (broker-sourced nurse, 2019); rent never raised | §280A(d)(2)(C) carve-out fits; allowed rental loss $19,550 stands. Lease document still missing (R2). |
| No capital contributions or loans since 2021; Pike guarantees the bank line | Basis note internally consistent; still unverified against filed 7203s (R1). Debt basis: none, confirmed. |
| Remote work was the employees' convenience at both firms (approved requests, no out-of-state necessity) | Convenience-of-the-employer rule applies; NY wages $68,000 / $54,000 (full year) confirmed. |
| Elena signed the Form 8332 for Leo's dad for 2025 ("it's his year") | Leo not claimed; CTC remains $2,200. The +$2,200 alternative is foreclosed. |
| Halvorsen plan from July 1; Marketplace plan dropped for everyone at June 30 | 8962 stands on the 1095-A's six covered months; no further 1095-A data needed. |
| No further information on exact residency facts, Tampa property tax, or prior-year filings | Residency 181 days (6/30 end) retained (R3); standard deduction retained (R5 — itemizing loses by a wide margin on available numbers). |

**No computed figure changed.** Residual unknowns are R1–R5 in `QUESTIONS.md` / `STATUS.md`; R1 and R2
could move numbers if contrary facts ever surface; none is answerable from the client or the library.
