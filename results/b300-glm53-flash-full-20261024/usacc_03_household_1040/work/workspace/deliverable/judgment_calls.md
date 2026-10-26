# Judgment calls — Reyes, 2025 Form 1040

Each entry: the decision, why, and the alternative rejected.

## 1. S-corp loss — basis limitation (Form 7203)

**Decision:** Allow $11,500 of the $28,000 K-1 loss; suspend $16,500.
**Why:** Stock basis begin-2025 = $11,500 (roll-forward from `documents/marcus_basis_note.md`); debt basis $0 because Marcus made no direct loans and a guarantee (here by Pike) does not create debt basis (`form7203_instructions_excerpt.md`). Loss limited to adjusted stock + debt basis.
**Rejected alternative:** Marcus's stated expectation that the loss "comes straight off" income — i.e., deducting the full $28,000. Recomputed counterfactual: AGI would fall from $91,350 to $73,382 — a cut of $17,968, more than the $16,500, because the lower MAGI ($94,400, under the $100,000 line) would make the full $25,000 rental special allowance available, so the entire $21,018 rental loss would be allowed instead of $19,550 — and the PTC would rise materially (household income ≈ 235% FPL). It is wrong under the library's basis rule (Form 7203).

## 2. Residency method and dates (NY)

**Decision:** NY resident Jan 1–Jun 30, 2025 (181 resident days); two-column IT-203.
**Why:** Lease ended June 30, Tampa closing 07/03/2025, and the June 28–30 Queens stay is inside New York.
**Rejected alternatives:** (a) treating June 28–30 as already nonresident — pointless because they were physically in New York (Queens) those days; (b) moving the cut-off to July 3 — nobody's days or wages turn on it, since the intervening days were spent traveling/staying with family in New York anyway.
*Superseded item:* the first-turn wage-allocation analysis (New York workday ratio) became moot once the client confirmed employee-requested relocations — see §3.

## 3. Convenience of the employer — both spouses' wages NY source (client-confirmed)

**Decision:** Marcus's full-year wages ($68,000) and Elena's full-year wages ($54,000) are NY source; no workday allocation.
**Why:** The governing distinction is who wanted the employee working out of state. The client's replies establish both moves were employee-initiated: Marcus asked to move and the company simply said remote was acceptable, "they didn't need me out of state"; Elena requested the fully remote arrangement and Halvorsen approved it. Wages earned out of state at the employee's own convenience are New York source; only days worked outside New York for the employer's necessity escape (`ny_it203_part_year_excerpt.md`). Corroborated by the source documents: both employers are New York entities (Reyes & Pike at 1 Liberty Plaza, NYC; Halvorsen at 230 Park Ave S, NY), and both W-2s report the full-year wages as NY state wages in box 16 ($68,000 / $54,000) with full-year NY withholding.
**Rejected alternatives:**
- *Employer-necessity for Elena* (first-turn reading of "Halvorsen let me go fully remote," which produced a $26,690 allocation via the 129/261 workday ratio, pending the workday question in QUESTIONS.md). We treated "let"/"approved" as employer-directed before the client clarified the sequence — her request, their approval. Superseded by the Q3 answer.
- *Treating "Halvorsen closed their Tampa office years ago" as employer necessity.* Neutral fact: no duty-assignment to Florida existed; the employer merely accommodated an employee request, which is the definition of employee convenience here.
- *Allocation for Marcus* (would have cut his NY wages to the resident period only). Rejected on the rule text: his convenience, not his employer's necessity, put him in Florida.

## 4. Dependents / child tax credit

**Decision:** Claim Sofia ($2,200 CTC); do not claim Leo.
**Why:** The stipulation alternates years and assigns odd years to the father; the library says the agreement controls and that a child claimed by the other parent under a Form 8332 release is not your qualifying child. 2025 is odd.
**Rejected alternative:** Claiming Leo on the theory that he "resides primarily with the Mother." That residency fact matters for who the custodial parent is (hence who must sign the Form 8332), not for overriding the agreed year assignment. The client confirmed the 2025 release was signed and delivered to the father — conclusion stands without qualification.

## 5. Below-market rent — eligibility of the rental loss

**Decision:** Treat the $1,500 rent as a fair rental for that lease; the loss qualifies for §469 treatment (special allowance) rather than being disallowed as personal use.
**Why:** `documents/rental_summary_brooklyn.md` says the rent is below market *because it was never raised* over a 6-year unrelated tenancy; the library's below-market paragraph says exactly this situation does not trigger the fair-rental-value personal-use rule (`form8582_instructions_excerpt.md`).
**Rejected alternative:** Reclassifying all rent days as personal use under §280A(d)(2)(C) → entire $21,018 loss disallowed. Rejected on the library's own carve-out; note the practical stakes were limited because the §469 special allowance capped the allowed loss at $19,550 anyway.

## 6. Standard vs itemized deduction

**Decision:** Standard deduction $31,500.
**Why:** Itemized (6,480 mortgage + 6,752 NY income tax withholding = 13,232) is far below 31,500 `1040_instructions_tax_computation.md`.
**Rejected alternative:** Itemizing. Also noted: a statutory cap on the state-tax item (commonly $10,000) is **not in the library**, so I neither applied nor relied on it — and it would not change the outcome here (13,232 < 31,500 regardless). Labeled unverified.

## 7. Family size of 4 for the PTC (Leo in the FPL count)

**Decision:** Use the family-of-4 FPL of $31,200, i.e., count Leo even though he is not the taxpayers' dependent in 2025.
**Why:** The 1095-A lists four covered individuals for all covered months and the library's FPL is keyed to "family of 4"; Leo's own income is nil either way, so household income is unaffected. The count follows the policy's covered individuals.
**Rejected alternative:** Family of 3 ($25,800-ish FPL not in the library anyway), which would have put household income at a higher FPL % and raised the applicable figure. Not supported by the 8962 excerpt's terms.

## 8. MAGI used for the 8582 special allowance

**Decision:** MAGI = 110,900 — includes the $11,500 *allowed* S-corp loss, excludes rental losses.
**Why:** The Form 8582 excerpt defines MAGI without passive losses and states that allowed nonpassive losses (an S-corp loss where the shareholder materially participates, to the extent of basis) do reduce MAGI.
**Rejected alternative:** Basing MAGI on full AGI 91,350, or on pre-basis loss AGI. The former double-counts the rental loss; the latter would inflate MAGI by 11,500 (to $122,400), shrink the special allowance to 25,000 − 50%×(122,400 − 100,000) = $13,800, and raise AGI to $97,100.

## 9. Depreciation figure

**Decision:** Use the client-prepared $9,818 (270,000 ÷ 27.5 = 9,818.18 unrounded).
**Why:** It is the client's own documentation and the 27.5-year residential straight-line method; the 18-cent difference cannot change any bracket or allowance this year.
**Rejected alternative:** Recomputing at 9,818.18 and reshuffling rounding through Schedule E — no benefits; adds noise.

## 10. PTC — covered months and repayment cap

**Decision:** Compute PTC only for Jan–Jun (the 1095-A coverage window); apply the $1,900 MFJ repayment cap because household income is in the 200%–<300% band.
**Why:** Column C advances are for exactly 6 months; Elena's W-2 box 12 DD shows employer coverage Jul–Dec, consistent with the family leaving the Marketplace mid-year. The repayment-limitation table in the 8962 excerpt sets $1,900 for 200%–<300%.
**Rejected alternative:** Computing a *no-limit* clawback of the full $2,369 excess (household income < 400% FPL, so the no-limit rule cannot apply). Note the unrounded excess is $2,368.75, rounded to $2,369; the final repayment is the capped $1,900.

## 11. Unverified / not-in-library (stated rather than cited)

- **SALT cap** (see #6) — not in library; irrelevant at these numbers.
- **CTC phase-out thresholds** — not in library; at AGI $91,350 any conceivable MFJ threshold would not bind, and the credit is absorbed by tax anyway.
- **Refundable/other-dependent credit mechanics (Schedule 8812)** — not in library; not needed (tax exceeds the credit).
- **NY-source treatment of the Brooklyn condo's Jul–Dec rental income** for IT-203 column B — the library says the nonresident column is "New York source income" but does not enumerate real-property income as NY source. Flagged open; no NY rental field exists in the contract's NY output anyway.
- **NY tax computation / refund amount** — no NY rate table in the library; the wage allocation deliverable is completed, the NY refund cannot be computed here.
