# Judgment calls — decisions made, and what I rejected

## 1. S-corp stock basis at 1/1/2025 = $11,500 (from client's note, not verified records)
- **Decision:** Rebuild basis from Marcus's note (`marcus_basis_note.md`): 10,000 contribution − 2,100 (2021) + 6,400 (2022) + 9,800 − 12,000 (2023) + 4,600 − 5,200 (2024) = 11,500. Applying the library's ordering (increases first, then distributions, then losses) makes 2021–2024 internally consistent: no loss or distribution ever exceeded basis in those years.
- **Rejected alternative:** Treat the 2023 distribution of $12,000 as an excess distribution (taxable) or treat earlier losses differently. Rejected because the note's own figures, put in the library's ordering, fit without leaving the file.
- **Residual risk:** No prior-year Forms 7203 or 2024 K-1 in the file. The 2024 ending basis of $11,500 is the client's arithmetic; if any prior loss was suspended or any basis item is wrong, the 2025 allowed/suspended split moves 1-for-1. **Client update (2025-10-25):** Marcus confirms no contributions since 2021 and never a shareholder loan; Pike guarantees the bank line. Client has no additional records ("no additional information"), so the note stays the sole evidence and this residual risk remains open.

## 2. The 2025 loss is allowed only to $11,500 — Marcus's expectation rejected
- **Decision:** Loss allowed = basis ($11,500); $16,500 suspended per IRC §1366(d) as stated in the Form 7203 excerpt. Debt basis = $0: Marcus never lent the corporation money, and Pike's guarantee of the bank line creates no basis for Marcus (the excerpt is explicit that guarantees create nothing; a *direct loan* would).
- **Rejected alternative:** Deduct the full $28,000 "straight off income" as Marcus believes. Also rejected any attribution of the bank line to Marcus — it is guaranteed by the *other* shareholder.

## 3. The allowed S-corp loss is nonpassive and reduces §469 MAGI
- **Decision:** K-1 Part II G certifies "Shareholder materially participates: Yes," so the allowed loss is nonpassive; the 8582 excerpt says such a loss "does reduce MAGI." MAGI = 122,400 − 11,500 = 110,900 → allowance 19,550.
- **Rejected alternative:** Compute MAGI without the S-corp loss (MAGI 122,400 → allowance 13,800, rental carryforward 7,218). Rejected as contrary to the library text. (Note the counter-intuitive result worth telling Marcus: the S-corp loss *increases* the rental allowance while itself being capped.)

## 4. Below-market Brooklyn rent ($1,500 vs ~$2,600 market): treated as a real rental
- **Decision:** Allow the rental loss. The library excerpt carves out exactly this fact pattern: renting below market to an **unrelated** tenant "because rent was never raised" does not itself trigger §280A(d)(2)(C) "if the rent is a fair rental for that lease."
- **Rejected alternative:** Treat all rental days as personal-use (no loss at all; net expenses would only be Schedule A items). This is the outcome if the 2025 rent of $1,500 is held *not* to be a fair rental under the lease (e.g., if the lease's terms allow or required increases that were waived as a courtesy to the tenant). The 2019 lease is not in the file.
- **Client update (2025-10-25):** the tenant "is a stranger, a nurse we found through a broker in 2019. We just never raised the rent." Both carve-out predicates (unrelated tenant; rent never raised, not a courtesy discount) are now client-confirmed. Remaining unknown (labeled, cannot be closed): the written lease was never produced and the client has no more to give, so the sub-element "the rent is a fair rental **for that lease**" rests on the client's account rather than the document.

## 5. Form 8962 family size / FPL: family of 4 ($31,200)
- **Decision:** Use the only FPL figure in the library: family of 4, $31,200. The 1095-A policy covered four individuals (Marcus, Elena, Sofia, Leo) for the covered months, and the library gives no other household-size figure, so a family-of-4 computation is the only one the library supports.
- **Rejected alternative:** Family of 3 (excluding Leo, whom the father claims in 2025). If the 8962 "tax family" excludes Leo, household income would be measured against a smaller FPL — FPL% rises above 300%, the applicable figure and repayment cap both change — but no family-of-3 FPL exists in the library, so that computation cannot be verified here. This is the largest single sensitivity in the 8962 result; client confirmation requested in QUESTIONS.md.
- Related call: Leo is on the 1095-A but **not** claimed as a dependent (see #8), and nothing in the library ties 8962 family size to the 1095-A; the excerpt simply supplies the family-of-4 line.
- **Client update (2025-10-25):** Elena confirms she signed the 8332 to Leo's dad — "it's his year" (the response's `{TY}` placeholder read as 2025). That settles #8 but does **not** settle family size: the library's line reads "Federal poverty line **used for 2025 coverage** (family of 4…): $31,200" — the phrase "used for 2025 coverage" matches the four-person coverage unit enrolled on the policy for the covered months, which is the only FPL figure in the closed library, so the family-of-4 computation stands.
- **Quantified sensitivity (labeled, not computed):** a family-of-3 FPL is not in the library, so that alternative cannot be computed. Direction is nonetheless determinable: any family-of-3 FPL below $31,200 pushes FPL% above 292.79%; if it lands in the 300–<400% band, the applicable figure rises to at least 6.00%, annual contribution ≥ $5,481, monthly PTC ≤ $1,233.25, annual PTC ≤ $7,399.50, excess ≥ $2,500.50, and the repayment (capped at $3,150 in that band) would fall in the range **[$2,500.50, $3,150]** — i.e., at least $600 higher than the $1,900 booked. Above 400% FPL there is no cap. Flagged in STATUS.md; do not book any of these figures.

## 6. NY resident period ends June 30 (181 days), not July 3
- **Decision:** Resident period Jan 1–Jun 30. They gave up the Brooklyn abode at lease end (June 30), slept in Queens (still NY) June 28–30, and left the state June 30; Tampa was closed July 3 but occupied from that weekend.
- **Rejected alternative:** End the resident period at the July 3 closing (184 days). Rejected: a few days of gap between leaving NY and occupying the FL home should not extend the NY period; and the difference is immaterial because of #7.

## 7. Convenience of the employer: **all** wages remain NY source — ratio 100%
- **Decision:** Marcus's and Elena's entire wages ($68,000 and $54,000) are NY source. Both employers are NY-based; work from Tampa after the move is remote by permission ("he just works remotely now"; "Halvorsen let me go fully remote") with no facts showing the work was out-of-state for the *employer's necessity*. The IT-203 excerpt makes convenience-of-employee remote wages NY source, and nothing in the file establishes the necessity exception.
- **Client update (2025-10-25):** Marcus — "the company said remote was fine when I asked to move; they didn't need me out of state"; Elena — "Halvorsen closed their Tampa office years ago; they approved my request" (her employer's office per the W-2 is 230 Park Ave S, NY). Both moves were employee-initiated with employer permission; neither shows employer necessity → the convenience-of-the-employer rule applies and the 100% NY-source conclusion is now client-confirmed, not assumed.
- **Rejected alternative:** Day-count allocation only (181/365 → NY wages ≈ $33,742 + $26,766). Rejected as directly contrary to the library's convenience rule; it would understate NY source income and risk an IT-203 adjustment.
- Consequence flagged: moving to Florida barely reduces NY exposure — wages, the Brooklyn rental (NY real property), and the NYC S-corp items are all NY source.

## 8. Leo claimed by the father in 2025
- **Decision:** Leo (9) is not a dependent on this return and generates no CTC. The 2019 order alternates years and says "The Father shall claim the child in odd-numbered tax years"; 2025 is odd; the library says the agreement controls and an 8332-released child is not our qualifying child for the credit.
- **Rejected alternative:** Claim Leo anyway because Elena is the custodial parent ("the child resides primarily with the Mother"). Rejected: the library defers to alternating-year agreements, and the mother must execute Form 8332 for the father this year.
- **Client update (2025-10-25):** confirmed — "I signed the 8332 for Leo's dad for {TY}, it's his year." The `{TY}` template placeholder is read as **2025** (consistent with the odd-year clause and her "it's his year" statement). The rejected alternative (claiming Leo) is now affirmatively off the table; CTC remains Sofia only.

## 9. Sofia is the only CTC; full credit usable
- **Decision:** $2,200, one qualifying child. Tax before credits ($6,708) exceeds the credit so it is fully usable. Rejected: any phaseout (nothing in the library states one, and at AGI $91,350 MFJ it would be irrelevant) — labeled unverified rather than cited.

## 10. Standard deduction over itemizing
- **Decision:** $31,500 standard. Itemized estimate: 6,480 (Tampa mortgage, partial year) + min(10,000, 5,140 property tax + 6,752 NY withholding) ≈ $16,480. Rejected itemizing.
- Caveat: the $10,000 SALT cap and the deductibility figures used in the *estimate* are my arithmetic context; the library contains only the standard-deduction amounts, so the itemized comparison is labeled approximate/unverified — the conclusion is robust because even ignoring the cap, 6,480 + 11,892 = 18,372 < 31,500.

## 11. Tax must come from the Tax Table, not the rate schedule
- **Decision:** TI $59,850 < $100,000 → table row 59,850–59,900 → $6,708. The rate-schedule computation at the bracket midpoint (6,708.00) matches, but the library forbids using the schedule under $100,000 — the table figure is what goes on the return.

## 12. NY tax not computed
- **Decision:** Report NY source wages, resident days, and method; refuse a NY tax/refund number. **No NY rate schedule is in the library**, and the rule is "if something you believe to be the law is not in the library, say so explicitly and label it unverified." Rejected: estimating NY tax from memory of NY rates — uncitable and out of bounds.

## 13. K-1 "Gross receipts 612,400" — no effect taken
- The K-1 shows Part II AC gross receipts $612,400 and material participation Yes. Gross receipts affect only deductions I was not asked to compute (e.g., possible §199A-type items, which are not in the library). No entity-level item beyond line 1 (loss) and line 16 (no distributions) exists in the K-1. Flagged so the number is not mistaken for income.

## 14. Repayment cap band — correction made this round (was $3,150; correct is $1,900)
- **Decision:** At household income 292.79% FPL the MFJ repayment limitation is the **200%–<300% band → $1,900** (`form8962_instructions_excerpt.md` line 14: "$750 if < 200% FPL; **$1,900 if 200%–<300%**; $3,150 if 300%–<400%"). Repayment = min(2,368.74, 1,900) = **$1,900**; $468.74 of the excess is not repayable. 1040 line 17 = 1,900 → total tax 6,408 → refund **2,322**.
- **What changed:** the first draft applied $3,150 — the 300–<400% band — to a 292.79%-FPL household, i.e., it repaid the full $2,368.74 excess. That was my band-selection error, not a client correction. Re-reading the library table after the client's 8332 answer (which put the family-size question back on the table) exposed it. Prior figures 2,369 / 6,877 / 1,853 are superseded by 1,900 / 6,408 / 2,322 in `return.json` and `return.md`.
- **Rejected alternative:** Repaying the full excess $2,368.74. Rejected: the library says the excess "you must repay is **limited**" to the band figure; the 300–<400% $3,150 row does not apply below 300% FPL.
