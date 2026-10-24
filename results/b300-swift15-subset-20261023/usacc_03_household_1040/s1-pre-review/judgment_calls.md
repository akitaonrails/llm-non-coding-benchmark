# Judgment Calls — Reyes 2025

Every point where the file left room for a decision, the choice made, the library
authority, and the alternative rejected.

## 1. S-corp loss: basis-limited, not "straight off"

**Decision:** Only **$11,500** of the $28,000 K-1 loss is deductible in 2025; **$16,500**
is suspended and carried forward (Form 7203).

**Basis:** `library/form7203_instructions_excerpt.md` (IRS Form 7203 Instructions 2025) —
losses allowed only to the extent of adjusted stock basis plus debt basis; excess
suspended indefinitely. Basis trail from `documents/marcus_basis_note.md`:
10,000 − 2,100 + 6,400 + 9,800 − 12,000 + 4,600 − 5,200 = **11,500** at 1/1/2025.
Debt basis is **0** because Marcus never made a direct loan — Pike's personal guarantee
of the bank line expressly does not create debt basis under the same excerpt.

**Alternative rejected:** Marcus's expectation that the $28,000 loss "comes straight off"
his income (i.e., deduct the full 28,000). Rejected because beginning stock basis
(11,500) is less than the loss and no debt basis exists. A related sub-alternative —
treating the guaranteed bank line as debt basis — is rejected on the same authority.
Consequence: AGI is higher by 16,500 than Marcus expected, and the suspended loss must
be tracked for future years (usable only as basis is restored by future income or
contributions).

## 2. Below-market rent: bona fide lease, loss allowed

**Decision:** Treat the Brooklyn condo as an ordinary rental; allow the full $21,018
activity loss (subject to the $25,000 special allowance, which caps it at $19,550).

**Basis:** `library/form8582_instructions_excerpt.md` (IRS Form 8582 Instructions 2025) —
"Renting below market to an unrelated tenant because rent was never raised does not by
itself trigger this rule if the rent is a fair rental for that lease." The file
(`documents/rental_summary_brooklyn.md`) shows an unrelated tenant of 6 years, rent set
at lease inception and never raised, while market rose to ~$2,600. This matches the
carve-out's fact pattern: the below-market status is a function of the original lease
terms, not a preferential arrangement with a related party. Elena's self-management
(approving tenants, arranging repairs) satisfies active participation for the special
allowance.

**Alternative rejected:** IRC §280A(d)(2)(C) treatment — recharacterizing the days as
personal-use days, which would disallow the loss entirely (and would have made the
expenses, other than interest and taxes, nondeductible). Rejected because the tenant is
unrelated and the excerpt states the never-raised-rent scenario does not by itself
trigger the rule. If the client later shows the rent was set below what the parties
believed fair at lease inception, or the tenant is in any way related, this must be
revisited.

## 3. Leo not a dependent for 2025

**Decision:** Claim **only Sofia** (15). CTC = 2,200 × 1.

**Basis:** `documents/custody_agreement_excerpt.pdf` ¶9 — Father claims Leo in odd
years, Mother in even years; the custodial parent executes Form 8332 in years the
noncustodial parent claims. 2025 is odd → the father claims Leo.
`library/1040_instructions_tax_computation.md` (IRS 2025 Form 1040 Instructions) —
"Where a decree or agreement alternates years, the agreement controls which parent
claims the child for that year," and a child claimed by the other parent is not a
qualifying child for the credit here.

**Alternative rejected:** Claiming Leo as a dependent for an additional $2,200 CTC.
Rejected because the court order assigns him to the father in 2025 and he resides
primarily with the mother; claiming him would conflict with the decree (and with the
father's return).

## 4. MAGI for the $25,000 allowance phase-out

**Decision:** MAGI = **110,900** = 122,000 wages + 400 interest − 11,500 basis-allowed
S-corp loss, with the $21,018 rental loss **excluded**.

**Basis:** `library/form8582_instructions_excerpt.md` — MAGI is AGI figured without
passive activity losses, and nonpassive losses (an S-corp loss where the shareholder
materially participates, to the extent allowed by basis) **do** reduce MAGI. The K-1
shows "Shareholder materially participates: Yes."

**Alternative rejected:** Computing MAGI before the S-corp loss (which would give
122,400 → allowance 18,800 → more carryforward) or after the rental loss (91,350 →
no phase-out at all, allowance 25,000, no carryforward). Both rejected; the excerpt's
ordering is explicit.

## 5. Standard deduction over itemized

**Decision:** Take the **31,500** standard deduction (MFJ).

**Basis:** `library/1040_instructions_tax_computation.md` — MFJ standard deduction
2025 = 31,500. Itemized candidates in the file: Tampa mortgage interest 6,480 (1098) +
NY state tax withheld 3,842 + 2,910 = 13,232. (Rental mortgage interest of 11,900 is a
rental expense, not an itemized deduction.) 13,232 < 31,500.

**Alternative rejected:** Itemizing — yields a $18,268 worse deduction.

## 6. NY residency method: convenience-of-the-employer, 100% NY wages

**Decision:** No day-count allocation of wages. Both W-2s are 100% NY-source income
under the "convenience of the employer" rule; NY resident days = 181 (1/1–6/30).

**Basis:** `library/ny_it203_part_year_excerpt.md` (NYS IT-203-I (2025)) — wages for
services performed entirely outside NY are not NY-source **except** for NY employers
paying employees who work from an out-of-state location "for the employee's own
convenience." Both employers are New York entities (Reyes & Pike, NYC; Halvorsen,
230 Park Ave S, NY) and both spouses went remote for personal convenience after the
move (`documents/email_move_dates.txt`; W-2 boxes 15–17 already report all wages as
NY).

**Alternative rejected:** Allocating wages by resident days (181/365) — i.e., treating
the July–December wages as non-NY. Rejected because the convenience-of-the-employer
exception applies to both taxpayers; the IT-203 excerpt is explicit that days worked
outside NY for the employer's *necessity* are the only ones excluded, and that is not
the fact pattern here. Also rejected: asking the client to file amended W-4s to stop
NY withholding — that is a withholding election for 2026 and does not change 2025
source.

## 7. PTC rounding and line mapping

**Decision:** Compute the monthly PTC (410.21), multiply by 12, round to the dollar
(4,923), then excess = 9,900 − 4,923 = 4,977, capped at 1,900 by the MFJ 200%–<300%
FPL limitation. `return.json` maps `24_total_tax` = line 16 + line 17 (8,608) and
`34` = (25d + 19) − 24 = 2,322 refund.

**Basis:** `library/form8962_instructions_excerpt.md` (monthly PTC = lesser of
enrollment premium and SLCSP minus monthly contribution; repayment limitation line 28
tiers by FPL percentage); the schema in `CONTRACT.md` for the 1040 fields.

**Alternative rejected:** Using the unrounded annual PTC (4,922.51 → excess 4,977.49,
same capped result) — the cap makes the rounding immaterial here, but the form
convention (dollar rounding on the credit line) is the one used. Also rejected
reporting `34` as 25d − 24 only (122), because the child tax credit is a payment/credit
that reduces tax due and is not represented by any other field in the schema.

## 8. Facts assumed from the file (not questions, since the file supplies them)

- Filing status MFJ: spouses live together at year end (1040 Instructions: status as
  of 12/31); joint W-2 addresses, joint 1098, joint 1095-A household.
- No estimated tax payments, other credits, other income, or prior-year credits
  appear anywhere in the file; assumed 0 (stated in `return.md` §3).
- Depreciation of 9,818 taken as computed in Elena's summary (270,000 ÷ 27.5).
