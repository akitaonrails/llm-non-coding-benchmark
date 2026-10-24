# Judgment calls — Reyes 2025 (MFJ)

Every decision where something had to be decided, with the alternative rejected and why.

**Client follow-up reviewed 10/23/2026 — no change to any figure.** Marcus asked why $16,500 is
suspended and whether Pike's guarantee counts; see section 11 below.

## 1. S-corp loss "comes straight off" — it does not (basis limitation)

- **Decision:** Only **11,500** of the 28,000 K-1 loss is deductible; **16,500 is suspended**
  (Form 7203 logic, `form7203_instructions_excerpt.md` — losses limited to adjusted stock basis +
  debt basis, IRC §1366(d)).
- **Rejected alternative:** Marcus's belief (echoed by "a friend") that the loss comes straight off.
  It would only be true with enough basis.
- **Debt basis = 0:** Marcus never lent the company money; the bank line is personally guaranteed by
  **Pike**. The library is explicit that a **guarantee does not create debt basis**, so no debt basis
  is added. (If Marcus had documented a direct shareholder loan, part of the loss might have been
  allowed — but there is evidence of none.)
- **Basis history accepted as complete:** Marcus's note reconstructs 2021–2025 from formation. I
  take it as complete (the K-1's box 16D = 0 distributions for 2025 corroborates it). Rejected
  alternative: asking the client for the basis ledger — the note is self-consistent (see check
  total 11,500) and the contract says to use the library/documents.
- **Order of operations** (income before distributions within a year, per the excerpt) matters for
  2023–2024 and confirms no distribution exceeded basis then (24,100 vs 12,000; 16,700 vs 5,200).

## 2. Rental — below-market rent: treated as a valid rental, loss allowed

- **Decision:** The $1,500 rent (vs ~$2,600 "market") does **not** convert the property to
  personal use. The library (`form8582_instructions_excerpt.md`, §280A(d)(2)(C) sentence) treats
  below-market terms as personal use **only** when the rent is not a fair rental "for that lease";
  a long-standing lease whose rent "was never raised" (unrelated tenant, 6-year tenancy, management
  entirely by Elena) falls on the allowed side of that sentence.
- **Rejected alternative:** Treating all days as personal use → **no loss at all** (that would be
  the mechanically harsher reading of "below market"). Rejected because the library's own carve-out
  covers exactly this fact pattern; also the tenant is unrelated with no family connection to
  the owners, so the unit is a genuine rental, not family use.
- **Depreciation:** Used the client's **9,818** (270,000 ÷ 27.5 = 9,818.18, rounded to whole
  dollars). Alternative (unrounded 9,818.18, loss 21,018.18, carryforward 1,468.18) changes nothing
  material — the 19,550 allowance controls and AGI is identical to the dollar.
- **Building basis unverified:** The 270,000 depreciable basis is from Elena's summary; no condo
  settlement/closing statement is in the file, and no land vs building split is shown. Relied on the
  client figure; flagged (no effect on allowed loss).
- **Expense mix per Elena's records; no Brooklyn 1098 in the file:** the itemized expenses
  (mortgage interest 11,900, common charges, repairs, etc.) come from
  `rental_summary_brooklyn.md` with no supporting statements on file. Sensitivity: the loss
  (21,018) sits only 1,468 above the allowance (19,550), so disallowance of any single expense
  larger than 1,468 would lower the allowed loss. Relied on the client's summary; flagged.

## 3. Rental loss phase-out — S-corp loss reduces MAGI, shrinking the allowance

- **Decision:** MAGI for the $25,000 special allowance = **110,900** (wages + interest − 11,500
  allowed S-corp loss; the rental loss excluded). The 8582 excerpt says nonpassive losses allowed
  by basis (like this materially-participated S-corp loss) **do reduce MAGI**.
- **Rejected alternative:** Computing MAGI without the S-corp loss (122,400), which would yield
  allowance 11,300 and a much larger carryforward. That contradicts the library's express sentence.

## 4. Leo (custody) — not claimed in 2025

- **Decision:** Father claims Leo in odd years under the court-ordered alternation
  (`custody_agreement_excerpt.pdf`); 2025 is odd → **only Sofia claimed**; CTC = 2,200 for one child.
- **Rejected alternative:** Claiming Leo as dependent/CTC. The agreed alternation controls for that
  year even though Leo "resides primarily with the Mother"; the library instructs that the
  agreement controls and that a child claimed by the other parent under a Form 8332 release is not
  yours for the credit.
- **Action needed:** Elena should execute the 2025 Form 8332 releasing Leo to the father
  (the agreement requires it each such year). Not on file.

## 5. NY residency dates — resident period Jan 1 – Jun 30 (181 days)

- **Decision:** Domicile left NY when the household moved the week of June 28 – July 3: lease ended
  6/30, closed/moved into Tampa 7/3. Resident period = Jan 1 – Jun 30 → **181 days**; nonresident
  Jul 1 – Dec 31 (184). Status as of 12/31 does not itself matter — part-year treatment does.
- **Rejected alternative:** Treating July 1–2 (mother's house until "we slept there June 28–30…
  then drove down") as still-resident. For 2–3 anomalous days the result is identical because the
  convenience rule makes post-move wages NY source anyway; any difference would affect only those
  2 days' income characterization, which is the same under either method here.

## 6. NY method — convenience of the employer for both spouses (100% NY source)

- **Decision:** Both W-2s → 100% NY source (Marcus 68,000; Elena 54,000). Both employers are
  New York employers; both spouses moved to FL for personal reasons, not employer requirement →
  post-move out-of-state work is **for the employee's convenience** → NY source wage under the
  IT-203 excerpt's exception to the out-of-state exclusion.
- **Rejected alternative:** Day-count/workday allocation (e.g., Marcus 68,000 × NY workdays ÷
  Total workdays, which would strip roughly the July–December half). Under the convenience rule the
  out-of-state remote days count as NY workdays, so the ratio is 100% for both; the excerpt's
  "necessity of the employer" carve-out (which could defeat NY sourcing) requires the employer to
  have required the out-of-state work — the file says the opposite ("nobody updated the forms";
  "he just works remotely now"; "Halvorsen **let** me go fully remote"). The NY withholding already
  on the W-2s (3,842 + 2,910) matches this method.
- **Note:** If either employer had documented a requirement (necessity) to work from Florida, the
  post-move days would not be NY source and a refund of some withholding would follow; no such
  document exists.

## 7. Standard deduction vs itemizing

- **Decision:** Standard deduction **31,500**. Itemized would be Tampa mortgage interest 6,480 +
  NY tax withheld 6,752 = 13,232 (plus any property tax on the Tampa condo not evidenced).
- **Note (unverified):** The library contains **no** law on whether/where SALT is capped, so I
  applied no cap; itemizing loses regardless of any cap because 13,232 < 31,500. The Brooklyn
  condo's property tax and mortgage interest are already deducted against rental income on
  Schedule E and cannot be re-itemized. Anything about SALT caps should be labeled **unverified —
  not in the library**.

## 8. Child tax credit pipeline

- **Decision:** CTC 2,200 (Sofia only), applied against 6,708 of tax. The library excerpt gives the
  2,200 amount and dependency rules but **not** refundability/phase-out thresholds; since the tax
  exceeds 2,200 on these numbers, the credit is fully absorbed either way and refundability is moot
  here.

## 9. Repayment figure on the 1095-A and PTC precision

- **Decision:** Interpolated the applicable figure linearly within the 250–300% band exactly as the
  excerpt directs (5.7115%), kept monthly premiums uniform (Jan–Jun all identical on the 1095-A),
  computed monthly PTC 1,255.21 × 6 = 7,531.25, excess 2,368.75 → 2,369, capped at **1,900**
  (200%–<300% band, 292.79%). Rounding of the band endpoints used: figure rounded for display only
  (5.71%), unrounded used in computation. Whole-dollar per-month rounding instead (contribution
  435 → PTC 1,255/month → annual 7,530, excess 2,370) reaches the same capped 1,900.
- **Rejected alternative:** Using real-world memory of Table 2's stepwise 0.02% steps or the actual
  2025 repayment ceilings — those are **not in the library** and may differ from this excerpt; the
  excerpt is the authority.

## 10. Assumptions stated prominently (no client question was needed)

1. **No federal estimated payments** in 2025 (nothing in the file).
2. **No prior-year unallowed rental loss** carried into Form 8582 (Elena's summary covers 2025
   only; the 6-year tenancy suggests earlier years also produced losses, but their MAGI history is
   unknown). *Materiality:* whatever the loss pool's vintage, the 19,550 allowance still reduces
   AGI by 19,550 this year — taxable income, tax, and refund are unchanged; only the loss-carryforward
   tagging would shift (2025's 1,468 vs part of earlier losses). Confirm at next filing.
3. **No other income/credits** beyond the documents provided (no dividend statements, no state
   refund item, no HSA/IRA/education items).
4. **§199A/QBI:** the library contains nothing on the QBI deduction. It is **unverified** here and
   **not applied**. Flagged as an open item — with a basis-allowed loss the QBI component may be
   negative (deduction zero, possible loss carryforward), but that cannot be verified from the
   library and must not be asserted as authority.
5. **NY state tax itself:** the IT-203 excerpt covers sourcing/allocation only. NY's rate schedule
   is not in the library, so the NY tax figure (and whether NY withholding 6,752 overpays) is **not
   computed** — allocation was, per the deliverable spec.

## 11. Client pushback on the $16,500 suspension (10/23/2026)

Marcus: "My buddy's CPA let him take his whole loss. Why are you suspending $16,500? Can't we count
Pike's guarantee or something?"

- **Decision reconfirmed: suspend 16,500; allow only 11,500.** The library rule is unqualified:
  losses are allowed only to the extent of **stock basis plus debt basis**, and "a guarantee of
  corporate debt does **not** create debt basis; only a **direct loan from the shareholder** to the
  corporation does" (`form7203_instructions_excerpt.md`, IRC §1366(d)).
- **Pike's guarantee = zero debt basis.** Pike put his own credit at risk; nothing was lent by
  Marcus. Marcus's own note says he never lent the company money. A guarantee someone *else* signed
  (or even one Marcus signed, absent him actually paying on it) is not a shareholder loan.
- **Why Marcus's friend could differ:** basis is shareholder-specific. A full loss deduction requires
  stock or debt basis of the shareholder equal to at least the loss — e.g., capital kept in the
  company, a bona fide shareholder loan, or no large draws. Marcus's own history shows the opposite:
  he took **$17,200 of distributions** (2023: 12,000; 2024: 5,200) against only $10,000 contributed.
  Combined 2021–2024 K-1 results: (2,100) + 6,400 + 9,800 + 4,600 = **18,700 net income**, so basis
  = 10,000 + 18,700 − 17,200 = **11,500** (the same 11,500 as the return, checked independently).
  **If Marcus had taken no distributions, basis would have been 10,000 + 18,700 = 28,700 — enough
  to absorb the whole $28,000 loss.** The draws are what left the 16,500 gap.
- **Rejected alternative (client suggestion):** counting Pike's guarantee, or Marcus's "understanding
  from a friend," as authority. Outside the library rule; rejected.
- **What restores basis later:** future K-1 income, new capital contributions, or an actual direct
  loan from Marcus to the corporation; the suspended 16,500 then becomes deductible
  (carryforward is indefinite per the excerpt). If Marcus wants the 2025 loss fully taken, the
  mechanical fix for a *future* year is a genuine shareholder loan — but nothing like that exists in
  2025 (and creating one now would not backdate basis to before the loss).
