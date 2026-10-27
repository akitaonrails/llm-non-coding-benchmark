# 2025 Federal Form 1040 + New York part-year allocation
**Taxpayers:** Marcus D Reyes and Elena M Reyes — married filing jointly
**Prepared from:** the file in `workspace/documents/`. Only `workspace/library/` is cited. Every citation below is to a file listed in `library/INDEX.md`.

> **Headline for Marcus: the S-corp loss does not "come straight off" your income.**
> Of the $28,000 K-1 loss, **$11,500** is allowed and **$16,500 is suspended** and carried forward, because your stock basis on January 1, 2025 was only $11,500 and you have no debt basis. [library: form7203_instructions_excerpt.md]
> The basis limit also has a second-order effect: it keeps your §469 MAGI *above* $100,000, which shrinks the rental special allowance from $25,000 to $19,550.

---

## 1. Filing status and dependents

| Item | Result | Authority |
|---|---|---|
| Filing status | **MFJ** — status determined as of Dec 31; married couple living together files jointly or separately | [library: 1040_instructions_tax_computation.md] |
| Sofia Reyes (15) | **Dependent + child tax credit $2,200** (under 17 at year end) | [library: 1040_instructions_tax_computation.md] |
| Leo Castellano (9, DOB 03/14/2016) | **Not claimed in 2025.** Custody decree: "The Father shall claim the child in odd-numbered tax years; the Mother shall claim the child in even-numbered tax years." 2025 is odd → father claims. Where a decree alternates years, the agreement controls. A child claimed by the other parent under a Form 8332 release is not your qualifying child for the credit. **Client-confirmed:** Elena signed the Form 8332 release for 2025 ("it's his year"). | [library: 1040_instructions_tax_computation.md]; `documents/custody_agreement_excerpt.pdf` ¶9 |

**Dependents on the return: Sofia only.** (Leo lives primarily with Elena, so he stays in her *household* for Form 8962 purposes — see §7 — but he is not a claimed dependent and not a CTC child. See `judgment_calls.md` #4.)

---

## 2. Income and AGI (Form 1040 lines 1a–11)

| Line | Figure | Arithmetic | Source / authority |
|---|---:|---|---|
| 1a Wages | **$122,000.00** | 68,000.00 (Marcus, Reyes & Pike Consulting Inc) + 54,000.00 (Elena, Halvorsen Media Group) | `w2_marcus_reyes_pike.pdf`, `w2_elena_reyes.pdf` |
| 2b Taxable interest | **$400.00** | Chase 1099-INT, recipient Elena | `1099int_chase.pdf` |
| 9 Total income | **$122,400.00** | 122,000 + 400 | |
| Schedule 1 / Schedule E pass-throughs (contract slot **line 8**) | **($31,050.00)** | S-corp loss allowed (11,500) + rental loss allowed (19,550) | §3 and §4 below |
| **11 AGI** | **$91,350.00** | 122,000 + 400 − 11,500 − 19,550 | |

*Mapping note:* on the actual 2025 return both pass-through items reach Schedule 1 through Schedule E (S-corp in Part II, rental in Part I), not Form 1040 line 8 "other income." The contract's `8_other_income_sch1` slot is filled with the Schedule 1 additional-income total, which is the figure that actually feeds line 11.

---

## 3. Form 7203 — S-corp loss (Reyes & Pike Consulting Inc, EIN 82-4471930, 40%, Marcus)

K-1: box 1 ordinary loss **($28,000)**; Part II line 17 "Gross receipts 612,400"; Part II G: **"Shareholder materially participates: Yes"** → not a passive activity, so §469 does not gate it; the limit is the shareholder basis rule. [library: form7203_instructions_excerpt.md]

**Stock basis rollforward** (increases for contributions and income; decreases for distributions and losses, in that order; guarantee of the bank line by Pike creates **no** debt basis — only a direct shareholder loan does, and Marcus made none):

| Year | Opening | + Income | − Distributions | Closing |
|---|---:|---:|---:|---:|
| 2021 | 10,000 (contribution) | (2,100) loss, fully allowed | 0 | **7,900** |
| 2022 | 7,900 | +6,400 | 0 | **14,300** |
| 2023 | 14,300 | +9,800 | (12,000) | **12,100** |
| 2024 | 12,100 | +4,600 | (5,200) | **11,500** |
| **2025** | **11,500** | — | 0 | **0** |

2025: loss allowed = lesser of loss and basis available = **min(28,000; 11,500) = $11,500**.
Suspended/carryforward = 28,000 − 11,500 = **$16,500** (indefinite, until basis is restored).
Debt basis: **$0**. [library: form7203_instructions_excerpt.md] The client asked (Oct 2026) whether Pike's bank-line guarantee could unlock the suspended $16,500 — it cannot: the library's Form 7203 instructions state that a guarantee never creates debt basis (only a direct shareholder loan does), and this guarantee is Pike's, not Marcus's. The carryforward is restored only when Marcus himself contributes cash or lends directly to the company. See `judgment_calls.md` #2.

| Form 7203 field | Value |
|---|---:|
| stock_basis_begin | 11,500 |
| loss_allowed | 11,500 |
| loss_suspended | 16,500 |

---

## 4. Form 8582 — Brooklyn condo (318 Dean St #4B)

Elena "handles everything herself (approves tenants, arranges repairs)" → **actively participates**, so the special allowance is available. [library: form8582_instructions_excerpt.md]

**Schedule E rental loss** (per `rental_summary_brooklyn.md`):

```
Rent received                       12 × 1,500.00 =  18,000.00
Mortgage interest                             (11,900.00)
Common charges                                 (7,860.00)
Property tax                                   (5,140.00)
Repairs (water heater, Jun)                    (2,350.00)
Insurance                                      (1,150.00)
Management/legal                                 (800.00)
   Expenses excl. depreciation  = 11,900+7,860+5,140+2,350+1,150+800 = (29,200.00)
Depreciation                       270,000 / 27.5 =  (9,818.00)   [file figure; 9,818.18 exact]
Net rental loss                     18,000 − 29,200 − 9,818 = (21,018.00)
```

**MAGI for §469(i)** — AGI figured *without* any passive activity loss; the allowed nonpassive S-corp loss **does** reduce MAGI:

```
MAGI = 122,000 (wages) + 400 (interest) − 11,500 (allowed S-corp loss) = 110,900
```

**Special allowance** (phase-out: reduced 50% of MAGI over $100,000; zero at $150,000+ MFJ):

```
25,000 − 0.50 × (110,900 − 100,000) = 25,000 − 5,450 = 19,550   (MAGI 110,900 < 150,000)
```

**Allowed / carried forward:**

```
Loss allowed this year   = min(21,018 ; 19,550) = 19,550
Carryforward (Part VII)  = 21,018 − 19,550       =  1,468
```

| Form 8582 field | Value |
|---|---:|
| rental_loss | 21,018 |
| magi | 110,900 |
| special_allowance | 19,550 |
| loss_allowed | 19,550 |
| carryforward | 1,468 |

**Below-market rent ($1,500 charged vs ~$2,600 market) — allowed.** The library's own carve-out governs: renting below market **to an unrelated tenant because rent was never raised does not by itself trigger** the personal-use rule "if the rent is a fair rental for that lease." **Client-confirmed (Q3 answer):** the tenant is a complete stranger — a nurse found through a broker in 2019 — and the rent was simply never raised. Every factual predicate of the library's carve-out (unrelated tenant, broker-set initial rate, rent never raised, no family relationship or side arrangement) is now confirmed by the client. Days are therefore **not** recharacterized as personal-use days and the loss is not disallowed under §280A(d)(2)(C). Residual risk is documentary only: the lease itself is still not in the file. See `judgment_calls.md` #5. [library: form8582_instructions_excerpt.md]

---

## 5. Deduction and taxable income

| Line | Figure | Arithmetic / authority |
|---|---:|---|
| 12 Deduction | **$31,500.00** | MFJ standard deduction, 2025. [library: 1040_instructions_tax_computation.md] |
| 15 Taxable income | **$59,850.00** | 91,350 − 31,500 |

**Itemizing checked and rejected:** the only plausible Schedule A items in the file are the Tampa mortgage interest $6,480 (`1098_mortgage.pdf`) and NY income tax withheld $6,752 (3,842 + 2,910). Total ≈ **$13,232**, far below $31,500. (The condo's $11,900 mortgage interest and $5,140 property tax belong on Schedule E and are already deducted there.) [library: 1040_instructions_tax_computation.md]

---

## 6. Tax (Form 1040 line 16)

Taxable income $59,850 is **under $100,000, so the Tax Table must be used** — the rate schedules were not used. [library: 1040_instructions_tax_computation.md]

Lookup: at least **59,850** but less than 59,900 → **MFJ tax $6,708**. [library: tax_table_2025_excerpt.md]

*(For reference only: the table's $6,708 equals the rate schedule computed at the bracket **midpoint** 59,875 — 23,850×10% + (59,875−23,850)×12% = 2,385 + 4,323 = 6,708. Applying the schedule to the actual $59,850 would instead give 23,850×10% + (59,850−23,850)×12% = 2,385 + 4,320 = 6,705 — and the schedule is expressly marked "not to be used under $100,000". The table is the controlling method.)*

**Correction (pre-delivery review):** an earlier draft of this memo included a "§55 minimum-tax comparison" (28% × 59,850 = 55,250, subject to a 50%-of-taxable-income limitation) citing the library's 1040 instructions excerpt. **No such rule exists in that file — or in any of the six library files** — so the comparison and its citation have been removed. The tax is taken from the Tax Table alone, the only computation method the library prescribes for taxable income under $100,000. See judgment call 8b for the correction record.

---

## 7. Form 8962 — Premium Tax Credit reconciliation

**Coverage:** Form 1095-A, NY State of Health, policy NYSH-77120-RE, covered individuals Marcus, Elena, Sofia, Leo. **Months covered: January–June (6 months)**; totals reconcile at 6 months: 1,720×6 = 10,320; 1,690×6 = 10,140; 1,650×6 = 9,900. Cross-check: Elena's W-2 box 12 code DD shows employer coverage **Jul–Dec** only. **Client-confirmed (Q5 answer):** Elena enrolled on Halvorsen's plan July 1, 2025 and the marketplace plan was dropped then — coverage is January–June only, and the stray "21–26" on the form is a printing artifact, not extra covered months. (`1095a_marketplace.pdf`)

| Step | Figure | Arithmetic | Authority |
|---|---:|---|---|
| Household income | **$91,350.00** | AGI 91,350 + tax-exempt interest 0 + nontaxable SS 0 + excluded foreign income 0 | [library: form8962_instructions_excerpt.md] |
| FPL | **$31,200** | family of 4, 48 contiguous states, 2025 coverage | same |
| % FPL | **292.79%** | 91,350 ÷ 31,200 × 100 = 292.7885% | same |
| Applicable figure | **5.7115%** | band 250–300% → 4.00%→6.00% linear: 4.00 + 2.00 × (292.7885 − 250)/50 = 4.00 + 1.7115 | same (Table 2) |
| Annual contribution | **$5,217.46** | 91,350 × 5.7115% = 5,217.45525 | same |
| Monthly contribution | **$434.79** | 5,217.46 ÷ 12 = 434.79 | same |
| Monthly PTC | **$1,255.21** | lesser of (a) enrollment premium 1,720.00 and (b) SLCSP 1,690.00 − 434.79 = 1,255.21 | same |
| **Annual PTC** | **$7,531.26** | 1,255.21 × 6 months covered | same |
| APTC paid | **$9,900.00** | 1095-A column C total (1,650 × 6) | `1095a_marketplace.pdf` |
| Excess APTC | **$2,368.74** | 9,900.00 − 7,531.26 | same |
| Repayment limitation | **$1,900** | MFJ, household income 200%–<300% FPL (292.79%) | same (line 28) |
| **Repayment** | **$1,900** | min(2,368.74; 1,900) → Form 1040 line 17 / Schedule 2 | same |

*Rounding is not material:* using a 5.71% applicable figure gives annual PTC 7,531.98 and excess 2,368.02; the repayment is capped at $1,900 either way.

---

## 8. Credits, payments, refund

| Line | Figure | Arithmetic |
|---|---:|---|
| 16 Tax | $6,708.00 | §6 above |
| 17 Schedule 2 — excess APTC repayment | $1,900.00 | §7 above |
| 18 Subtotal | $8,608.00 | 6,708 + 1,900 |
| 19 Child tax credit | **($2,200.00)** | $2,200 × 1 qualifying child (Sofia). Leo: father claims in 2025 per the decree and Elena has **signed the 8332** (client-confirmed). Fully absorbed by the $8,608 subtotal, so no refundable-portion analysis is needed. The refundable additional CTC is not addressed in the library — not needed here, and flagged as unverified if it ever were. [library: 1040_instructions_tax_computation.md] |
| 20 Other nonrefundable credits | $0 | none in file |
| 22 Other taxes | $0 | no SE tax (S-corp shareholder wages are not self-employment earnings — not a library point, treated as unverified but immaterial: no Schedule C/SE income exists in the file); no §55/tentative-minimum-tax rule exists anywhere in the library, so no comparison applies — judgment call 8b records the removal of an earlier unsupported one — and no Form 621 items exist in the file; no additional Medicare tax (wages $122,000 MFJ, below the $250,000 threshold — threshold not in library, flagged unverified) |
| **24 Total tax** | **$6,408.00** | 6,708 + 1,900 − 2,200 |
| 25d Federal income tax withheld | **$8,730.00** | 5,120 (Marcus W-2) + 3,610 (Elena W-2) |
| Estimated payments | $0 | none in file; client has no additional information (Q7) — treated as $0, flagged |
| **34 Refund** | **$2,322.00** | 8,730 − 6,408 → **refund**, not amount owed |

---

## 9. New York part-year (IT-203)

**Resident period: January 1 – June 30, 2025 = 181 days**; nonresident period July 1 – Dec 31 = 184 days. Assumed end-of-residency date is 6/30, when the Brooklyn lease ended and they were "out by then" (they slept in Queens 6/28–6/30, still inside NY); the Tampa closing/move-in was 7/3. Client offered no further information on this point (Q4 unanswered) — the 6/30 date remains a stated assumption. [library: ny_it203_part_year_excerpt.md]; `email_move_dates.txt`. Alternative 7/3 end-date → 184 days; see `judgment_calls.md` #14.

**A part-year resident is taxed on all income received during the resident period plus NY source income during the nonresident period.** [library: ny_it203_part_year_excerpt.md]

| Category | NY-includible? | Why |
|---|---|---|
| Marcus wages $68,000 | **$68,000 (100%, full year)** | Reyes & Pike Consulting Inc is at 1 Liberty Plaza, **New York NY** → a New York employer. Under the **convenience-of-the-employer rule**, wages paid by a NY employer to an employee working from an out-of-state location for the *employee's own convenience* are NY source. **Client-confirmed (Q6 answer):** "the company said remote was fine when I asked to move; they didn't need me out of state" — no employer necessity, so the full $68,000 is NY source. |
| Elena wages $54,000 | **$54,000 (100%, full year)** | Halvorsen Media Group LLC is at 230 Park Ave S, **New York NY** → a New York employer. **Client-confirmed (Q6 answer):** Halvorsen closed its Tampa office years ago and "approved my request" for remote work — employee-initiated accommodation, not employer necessity, so the convenience rule applies to her Jul–Dec wages too. |
| Brooklyn condo rental (Sch E, net (21,018)) | **100%** | Rental real property located in New York; NY source for the entire year, resident period or not. |
| Chase interest $400 | resident-period share at minimum | Intangible income; included for the resident period. The library excerpt is **silent** on sourcing intangible income during the nonresident period, so the Jul–Dec share is left unallocated rather than assumed to follow an FL domicile — the excerpt addresses no domicile rule for intangibles. Not needed for the requested fields. |
| S-corp loss $(28,000)/$(11,500 allowed) | NY-source entity | The corporation is NYC-based; no NY allocation data appears on the K-1, and the library excerpt gives no rule for sourcing S-corp passthrough to IT-203. Left open — see `STATUS.md` open items. |

**Method:** convenience-of-the-employer, **not** a 181/365 day ratio, for wages. The library's day-ratio sentence ("allocate by the ratio of days in the resident period **(or New York workdays)** to total days/workdays") is the general mechanism, but for these wages the NY-workday measure is the whole year because the convenience rule converts every workday into a NY workday.

**Rejected alternative** (documented for the client): a straight day-ratio allocation would put only Marcus $33,720.55 (68,000 × 181/365) and Elena $26,778.08 (54,000 × 181/365) in NY. That is the intuitive answer and it is wrong on these facts — it is exactly the trap the convenience rule sets.

**Not computed — flagged, not forced:** the **NY tax due and the IT-203 refund of the $6,752 NY withholding** (3,842 + 2,910) cannot be figured from this library: it contains no NY rate schedule, no NY standard deduction, and no NY subtraction modifications. The library says only that "tax withheld in excess of the tax due is refunded on IT-203." [library: ny_it203_part_year_excerpt.md] This is left open rather than estimated.

---

## 10. What is *not* in the library (stated rather than cited)

Per the working rules, the following are things a preparer might reach for that this library does not contain, so they are **not relied on** and none of them changes a figure above:

- Any NY tax rates, NY deductions, or IT-203 line mechanics beyond the excerpt → NY tax/refund not computable.
- The at-risk rules (§465) and the basis-vs-at-risk interaction for the S-corp.
- Refundable/additional child tax credit mechanics; other-dependent credit ($500) — irrelevant, Leo is not claimed.
- Whether S-corp shareholder W-2 wages are exempt from self-employment tax (assumed yes, unverified, and no SE income item exists in the file).
- The $250,000 MFJ additional Medicare tax threshold (unverified; wages $122,000, comfortably below any plausible threshold).
- FPL for a family of 3 (only the family-of-4 figure is given) → the household-size judgment in §7/`judgment_calls.md` #10 cannot be re-run on 3 people with verified numbers (client had no additional information on this point).
- Cost basis/placed-in-service documentation for the condo's $270,000 building basis (taken from Elena's summary; the prior-year depreciation schedule is not in the file).
