# Judgment calls

Every place where the file did not decide the answer for me, with the alternative I rejected and the dollar impact. Numbered for cross-reference from `return.md` and `STATUS.md`.

---

### 1. The S-corp loss is basis-limited, not "straight off the income"
**Decided:** allowed $11,500, suspended $16,500; beginning stock basis $11,500.
**Rejected:** Marcus's stated expectation (via "a friend") that the full $28,000 comes off 2025 income.
**Authority:** a shareholder's share of losses is allowed **only to the extent of adjusted stock basis plus debt basis**; the excess is suspended and carried forward indefinitely. [library: form7203_instructions_excerpt.md]
**Basis arithmetic:** 10,000 − 2,100 = 7,900 → +6,400 = 14,300 → +9,800 − 12,000 = 12,100 → +4,600 − 5,200 = **11,500**.
**Client-confirmed:** Marcus "hasn't put anything in since 2021 and never lent it money" — consistent with his note, whose only capital contribution is the $10,000 at 2021 formation (the later "+" figures are income allocations, not contributions). Beginning basis $11,500 is locked.
**Impact:** $16,500 of deduction deferred to a future year (only when Marcus restores basis — e.g. a capital contribution, or a **direct** loan to the corporation, which he has never made). Also cascades: it keeps §469 MAGI at $110,900 instead of $94,400, which cuts the rental special allowance from $25,000 to $19,550 (see #11).

### 2. Pike's personal guarantee of the bank line creates no debt basis
**Decided:** debt basis $0.
**Rejected:** treating the guaranteed bank line as giving Marcus basis for the excess loss.
**Authority:** a guarantee of corporate debt does **not** create debt basis; only a direct loan from the shareholder to the corporation does. [library: form7203_instructions_excerpt.md] Impact: $16,500 stays suspended rather than being deducted. Client-confirmed: Marcus never lent the company money; the bank line is personally guaranteed by **Pike**, not Marcus — no debt basis either way.

### 3. Ordering of basis adjustments (distributions before losses)
**Decided:** increase basis for income first, then apply distributions, then losses.
**Rejected:** applying the current-year loss before distributions.
**Authority:** basis is increased by contributions and income and decreased by distributions and losses "in that order." [library: form7203_instructions_excerpt.md]
**Impact:** none in 2025 (no distributions in 2025), and none in 2023/2024 (basis was sufficient under either ordering). Note the 2023 $12,000 and 2024 $5,200 distributions never exceeded basis, so no shareholder gain arises — checked, not assumed.

### 4. Leo Castellano (9) is **not** claimed in 2025
**Decided:** father claims him. 2025 is an odd-numbered year and the decree says "The Father shall claim the child in odd-numbered tax years; the Mother … in even-numbered tax years," with the custodial parent executing Form 8332. Where a decree alternates years, the agreement controls. [library: 1040_instructions_tax_computation.md]; `custody_agreement_excerpt.pdf` ¶9.
**Rejected:** claiming Leo because he is Elena's son, lives primarily with her, and is covered on the family's 1095-A. Custody alone would normally make Elena the claimant, but the alternating-years decree overrides for 2025; and a child claimed by the other parent under an 8332 release is **not** a qualifying child for the credit.
**Impact:** CTC is $2,200 (Sofia only) instead of $4,400 → refund $2,322 instead of $4,522. **CLOSED — client-confirmed:** Elena signed and delivered the Form 8332 release for Leo for 2025 ("it's his year"), so the father claims Leo for 2025 and the $4,522 variant is off the table. In 2026, an even year, the claim flips back to Elena with no release needed.

### 5. Below-market rent on the Brooklyn condo — loss allowed
**Decided:** the $1,500/month rent (market ≈ $2,600) does **not** convert the days to personal-use days, so the rental loss is not disallowed under §280A(d)(2)(C).
**Rejected:** the conservative treatment that any sub-market rent recharacterizes all 365 days as personal use and disallows the entire $21,018 loss.
**Authority (this is the pivot):** "Renting below market to an **unrelated tenant because rent was never raised** does not by itself trigger this rule **if the rent is a fair rental for that lease**." [library: form8582_instructions_excerpt.md] The facts fit the carve-out: same unrelated tenant for 6 years, one lease, no rent increase — a legacy contract rate, not a below-market accommodation.
**Why it was the riskiest position — now de-risked by client confirmation:** the library's carve-out is conditional ("if the rent is a fair rental for that lease"). The client has confirmed every factual element: the tenant is **a stranger** (a nurse found through a broker in 2019), there is one lease, and the rent was simply never raised — a legacy broker-set rate, not a below-market accommodation, and no family relationship or side arrangement. Residual risk is documentary only: the lease itself is still not in the file. Impact if the position were nevertheless lost: AGI rises to $110,900, taxable income to $79,400 — **outside the Tax Table excerpt in the library**, so the resulting tax/refund cannot be computed from the library; it would be a several-thousand-dollar swing and it would also change Form 8962. Documented in `judgment_calls.md` and left as a documentation open item, not balanced around.

### 6. Rental treated as *passive* with the §469(i) allowance, not as a nonpassive business
**Decided:** rental real estate, actively participated in (Elena approves tenants, arranges repairs), so the special allowance applies; only $19,550 of the $21,018 loss is currently deductible.
**Rejected:** arguing Elena's hands-on management makes the rental nonpassive, which would deduct all $21,018 with no cap.
**Authority:** the library routes rental real estate losses through the $25,000 special allowance for *actively participating* taxpayers; it supplies no rule making a landlord's rental nonpassive. [library: form8582_instructions_excerpt.md]
**Impact:** $1,468 of loss deferred; the aggressive position would also require a real-estate-professional/material-participation analysis that this library cannot support.

### 7. §469 MAGI includes the allowed S-corp loss
**Decided:** MAGI $110,900 = wages $122,000 + interest $400 − allowed S-corp loss $11,500, excluding the passive rental loss entirely.
**Rejected:** (a) MAGI that also excluded the S-corp loss → $122,400 → allowance $13,800; (b) MAGI net of the rental loss (circular).
**Authority:** MAGI is AGI without any passive activity loss, and a nonpassive S-corp loss where the shareholder materially participates **does** reduce MAGI. [library: form8582_instructions_excerpt.md] The K-1 states Marcus materially participates, so the S-corp loss is nonpassive.
**Impact:** allowance $19,550 (vs $13,800 under (a)); AGI $91,350 (vs $85,600), which also lowers Form 8962 income and therefore *increases* the credit.

### 8. Tax table, not the rate schedule
**Decided:** tax $6,708 read from the MFJ bracket "at least 59,850 but less than 59,900."
**Rejected:** computing from the rate schedule (23,850×10% + 36,000×12% = $6,708 here — identical by coincidence of bracket midpoints, but the method is not permitted).
**Authority:** taxable income under $100,000 **must** use the Tax Table; the rate schedule in the excerpt is marked "reference only — not to be used under $100,000." [library: 1040_instructions_tax_computation.md]; [library: tax_table_2025_excerpt.md]

### 8b. §55 minimum-tax comparison (required by the library; adds $0)
**Decided:** tax stays $6,708.
**Rejected:** subtracting the $55,250 figure from the tax (it is not a deduction or credit — misreading it that way would produce a nonsense negative tax).
**Authority:** the library says the 11.2% effective rate behind the table figure is a comparison figure: "compare to a 26%/28% §55 tentative minimum with the 50% limitation. The §55 minimum tax is the excess of that amount over the regular tax, but never less than zero." [library: 1040_instructions_tax_computation.md]
**Arithmetic:** 50% limitation: 28% × 59,850 = 55,250. Minimum tax = max(0, 55,250 − 6,708) = **0**. Impact: $0; the QBI-style deduction embedded in the 11.2% is fully realized at this taxable income.

### 9. Standard deduction
**Decided:** $31,500.
**Rejected:** itemizing — Schedule A items in the file total ≈ $13,232 (Tampa mortgage interest 6,480 + NY withholding 6,752; rental interest/tax already on Schedule E).
**Authority:** MFJ standard deduction $31,500. [library: 1040_instructions_tax_computation.md]

### 10. Form 8962 household size = 4
**Decided:** family of 4 (Marcus, Elena, Sofia, Leo). Leo is not a claimed dependent but he is Elena's child, resides primarily with her, and is an enrolled member of the policy.
**Rejected:** a 3-person household (Marcus, Elena, Sofia — excluding Leo because he is not claimed in 2025).
**Authority:** the library supplies the FPL for **family of 4** only ($31,200), and the 1095-A lists four covered individuals. [library: form8962_instructions_excerpt.md]; `1095a_marketplace.pdf`.
**Honest caveat:** the rule that puts a §152(e)-released child in the custodial parent's household for §36B purposes is **not in this library** — labelled unverified. The library's family-of-4 figure is the only FPL I can cite. If the household were 3, the % FPL would rise (320%+ territory), the applicable figure and contribution would rise, the excess APTC would rise, and the repayment cap would jump from $1,900 to $3,150 — I cannot compute that variant with a verifiable FPL. Client provided no further information (Q1 unanswered): the 4-person household stands as a stated assumption, supported by the 1095-A's four covered individuals and Leo residing primarily with Elena.

### 11. Form 8962 contribution spread over the 6 covered months
**Decided:** monthly contribution $434.79 = annual $5,217.49 ÷ 12, applied to each of the 6 covered months → annual PTC $1,255.21 × 6 = $7,531.26.
**Rejected:** netting the *full 12-month* contribution ($5,217.49) against only 6 months of SLCSP premium ($10,140) → PTC $4,922.51 and excess $4,977.49.
**Authority:** monthly PTC = lesser of enrollment premium and (SLCSP − monthly contribution amount), where the monthly contribution amount = household income × applicable figure ÷ 12. [library: form8962_instructions_excerpt.md]
**Impact:** excess $2,368.74 vs $4,977.49 — but **the repayment is capped at $1,900 either way**, so the tax consequence is zero. Rounding the applicable figure (5.7115% vs 5.71%) is likewise immaterial for the same reason.

### 12. Marketplace coverage = January–June only (6 months)
**Decided:** 6 covered months; annual APTC $9,900 = $1,650 × 6.
**Rejected:** reading the stray "21–26" on the 1095-A as a second block of covered months (12 months → APTC $19,800, and a much larger repayment).
**Why:** the three annual totals each equal exactly 6 × the monthly figures (10,320 / 10,140 / 9,900), and Elena's W-2 code DD shows **employer** coverage Jul–Dec ($7,140). The two documents agree on a January–June marketplace period followed by employer coverage. **CLOSED — client-confirmed:** Elena joined Halvorsen's plan July 1, 2025 and the marketplace plan was dropped then; the stray "21–26" is a printing artifact, not extra covered months.

### 13. Where the pass-through losses sit on the 1040
**Decided:** the contract's `8_other_income_sch1` slot carries the Schedule 1 total, $(31,050) = S-corp $(11,500) + rental $(19,550).
**Rejected:** putting only the S-corp amount, $(11,500), in that slot; on a real 2025 return **both** items reach Schedule 1 through Schedule E (S-corp in Part II, rental in Part I), so a literal "line 8 other income" reading would drop the rental loss and overstate AGI by $19,550.
**Impact:** AGI $91,350 vs $110,900. Flagged as a template-mapping note, not a tax position.

### 14. New York residency end date — June 30 (181 resident days)
**Decided:** resident period 1/1–6/30 = 181 days; nonresident 7/1–12/31 = 184 days.
**Rejected:** residency ending July 3 (closing/move-in in Tampa) = 184 days; and the notion that Queens nights of 6/28–6/30 continued NY residency past 6/30 (they did — but those days are inside the 6/30 cut-off anyway).
**Authority:** the library excerpt defines what a part-year resident is taxed on but gives **no** rule for fixing the change-of-residency date, so this is an assumption stated prominently. [library: ny_it203_part_year_excerpt.md]; `email_move_dates.txt`.
**Impact:** 3 days of day-count allocation, which matters only for income allocated by days (the Chase interest, and wages if the day ratio were used — see #15). Small; client offered no further information (Q4 unanswered), so 6/30 remains the stated assumption.

### 15. Convenience of the employer → **both** spouses' wages are 100% NY source
**Decided:** Marcus $68,000 and Elena $54,000 are entirely NY source for the full year.
**Rejected:** the day-ratio result — Marcus $33,720.55 and Elena $26,778.08 (wages × 181/365) — i.e. treating July–December Florida wages as non-NY source simply because they were physically worked in Florida.
**Authority:** wages for services performed entirely outside NY during the nonresident period are not NY source, **except** that under the convenience-of-the-employer rule wages paid by a **New York employer** to an employee working from an out-of-state location for the **employee's own convenience** *are* NY source; days worked outside NY for the **employer's necessity** are not. [library: ny_it203_part_year_excerpt.md]
**Applied to the facts — and now client-confirmed:** Reyes & Pike Consulting Inc — 1 Liberty Plaza, New York NY (and Marcus is a 40% owner): "the company said remote was fine when I asked to move; **they didn't need me out of state**." Halvorsen Media Group LLC — 230 Park Ave S, New York NY: closed its Tampa office years ago and "**approved my request**" for remote work. Both are NY employers; both remote arrangements were employee-initiated accommodations with no employer necessity. Convenience-of-the-employer sourcing for **both** spouses is confirmed by testimony, not merely assumed.
**Impact:** $61,501.37 of wages stays in the NY base (122,000 vs 60,498.63). This is the single largest NY item, and it is why both employers' full-year NY withholding is not obviously wrong. With the client's answers, the day-ratio alternative is now formally rejected on confirmed facts, not on a gap in the record.

### 16. NY tax due / IT-203 refund left uncomputed
**Decided:** no NY tax figure, no NY refund figure.
**Rejected:** estimating NY tax with an out-of-library rate schedule.
**Reason:** the library contains no NY rates, deduction, or subtraction modifications. Withheld NY tax is $6,752 (3,842 + 2,910) and the library says only that over-withheld tax is refunded on IT-203. Stated as an open item rather than forced to balance. [library: ny_it203_part_year_excerpt.md]

### 17. Client-schedule figures taken as given (documentation gaps, not disputes)
- Rental depreciation $9,818/yr on a $270,000 building basis ÷ 27.5 (the summary's own rounding; exact is $9,818.18). No prior-year depreciation schedule or placed-in-service/basis documentation in the file.
- Condo mortgage interest $11,900 with no 1098 for that property (the only 1098 in the file is the Tampa home, $6,480).
- Condo "common charges" $7,860 treated as an operating expense.
- The Tampa 1098 ($6,480 ≈ 6 × $1,080 from a 7/3 closing) is *not* deducted anywhere — it is a personal itemized item and the standard deduction wins (#9).

### 18. No adjustments to income
**Decided:** Schedule 1 adjustments $0 (Form 1040 line 10 blank), so AGI equals total income less the two allowed losses.
**Rejected:** none — there are no IRA, student loan interest, HSA, educator or similar items in the file. Stated because "AGI = total income − adjustments" should not look accidental. (The library's §469 MAGI definition lists IRA deductions, student loan interest and one-half SE tax as MAGI add-backs; none exist here, which is why §469 MAGI and AGI differ only by the passive loss.)
