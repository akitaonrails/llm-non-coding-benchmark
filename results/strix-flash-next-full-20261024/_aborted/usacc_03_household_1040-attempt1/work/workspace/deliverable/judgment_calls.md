# Judgment calls

Every place I had to choose, with the alternative I rejected and the dollar consequence. Amounts marked
**[unverified]** rest on rules that are **not in `library/`**, so they cannot be cited. Client answers
of 2026-10-25 are recorded where they confirm or close a call; they changed no figure.

---

## 1. S-corp loss: $11,500 allowed, not $28,000 (the biggest call in the return)

**Decided:** loss allowed $11,500 = beginning stock basis; $16,500 suspended to Form 7203 carryover.
**Rejected:** Marcus's expectation (via his "friend") that the loss "comes straight off our income."

- Authority: [form7203_instructions_excerpt.md] — losses allowed only to the extent of adjusted stock
  basis plus debt basis; excess is suspended indefinitely.
- Debt basis is zero: the bank line is guaranteed by **Pike**, not Marcus, and a guarantee does not
  create debt basis. **Rejected alternative:** treat the guaranteed bank line as Marcus's debt basis,
  which would let the full 28,000 through. Not available on these facts. *Client confirmed 2026-10-25:
  "I never lent it money. Pike guarantees the bank line" — the rejected alternative is now closed by
  testimony, not just by the file.*
- Marcus's $68,000 of W-2 wages from the S corp do **not** restore basis (compensation, not a
  contribution or share of income). **Rejected alternative:** crediting wages against the loss.
- *Client pushback after delivery ("my buddy's CPA let him take his whole loss — can't we count
  Pike's guarantee?"):* re-tested against the same excerpt and **held**. The buddy's story is a facts
  difference, not a rule difference — he evidently had basis (contributions, prior flow-through
  income, or a loan made **directly** to his corporation). A guarantee creates no basis for anyone
  until the guarantor actually pays the creditor, and any such basis would be **Pike's**, not
  Marcus's. The $16,500 is a carryforward, not a disallowance: 2026 income restores basis and
  releases it. Planning path for future years: a direct documented shareholder loan or a capital
  contribution would create debt/stock basis. 2025 figures unchanged.
- Basis ordering: income first, then distributions, then losses, per the excerpt. On these numbers the
  ordering does not change any year's ending basis, but I applied it explicitly (see the table in
  `return.md` §2).
- **Knock-on effect I had to decide not to ignore:** allowing 11,500 rather than 28,000 raises 8582
  MAGI to 110,900, which cuts the rental special allowance to 19,550 and pushes another 1,468 of
  rental loss into carryforward. Marcus's expectation was "wrong in both directions": it would have
  also produced a bigger rental deduction.

## 2. Beginning stock basis taken from a client note

**Decided:** stock_basis_begin = $11,500, computed from `marcus_basis_note.md`
(10,000 − 2,100 + 6,400 + 9,800 − 12,000 + 4,600 − 5,200).
**Rejected:** (a) asking for prior-year Forms 7203 and freezing the number — the return needs a figure
now; (b) using $10,000 (original contribution) — the note shows income and distribution history that
the library requires be reflected.
**Flag:** this is client-prepared and unaudited; every dollar of overstated 2025 basis is a dollar of
overstated loss. *Client confirmed the underlying facts 2026-10-25* (no contributions since the 2021
formation, no loans) — consistent with the note, but the prior-year Forms 7203 are still not in the
file, so the number stays client-prepared (QUESTIONS.md B2).

## 3. Rental: allowed, with the $25,000 special allowance phased down to $19,550

- **Active participation: yes** (Elena "handles everything herself — approves tenants, arranges
  repairs"). Note: the excerpt states active participation as a **condition** of the exception but does
  not define the term **[unverified definition]**; Elena's own description is the only evidence, and it
  sits comfortably inside any ordinary reading of the condition. Rejected alternative: treat it as
  non-active (professional-manager style) participation,
  which would zero the allowance and defer the whole 21,018; the facts do not support that.
- **MAGI includes the allowed S-corp loss**: 122,000 + 400 − 11,500 = 110,900. Authority: the excerpt
  states nonpassive losses allowed in the year (e.g. an S-corp loss where the shareholder materially
  participates, to the extent allowed by basis) *do* reduce MAGI. **Rejected alternative:** MAGI of
  122,400 (ignoring the S-corp loss) → allowance 13,800, allowed rental loss 13,800, carryforward
  7,218, AGI 97,100 — taxable income 65,600, which falls outside the tax-table excerpt and could not
  even be priced from this library. The library text is explicit, so I used 110,900.
- **Material participation on the S corp** was taken from K-1 Part II G ("Yes") rather than
  re-determining it from facts. Rejected alternative: treat the S corp as passive (it would then join
  the rental in the 8582 computation and *increase* MAGI to 122,400). The box is the only evidence and
  it is consistent with Marcus drawing a $68,000 wage from the company.
- **Depreciation $9,818 (270,000 ÷ 27.5) taken as given.** No depreciation authority (recovery period,
  convention, basis allocation between land and building) is in the library — **[unverified]**. I did
  not apply a mid-year convention haircut, because for a property placed in service ~6 years ago the
  year 2+ amount equals the full annual amount; if placed in service mid-year, this is still the right
  2025 figure. Rejected alternative: substituting my own depreciation. Support documents remain missing
(QUESTIONS.md B3).

## 4. Below-market rent ($1,500 vs ~$2,600 market) — decided in the taxpayers' favor, with real risk

**Decided:** not personal-use days ⇒ rental loss allowed. Tenant is **unrelated**, the rent has been
fixed for a 6-year lease, and the library says renting below market to an unrelated tenant "because
rent was never raised does not by itself trigger this rule **if the rent is a fair rental for that
lease**" ([form8582_instructions_excerpt.md], citing IRC §280A(d)(2)(C)). *Client confirmed
2026-10-25: the tenant is a stranger — a nurse found through a broker in 2019 — and "we just never
raised the rent." That is the library's carve-out scenario almost verbatim; the call is stronger,
but the "fair rental for that lease" condition remains undocumented (no lease or market evidence in
the file — QUESTIONS.md B4).*

**Rejected alternative:** treat all rental days as personal use ⇒ **no loss at all** (rent $18,000
taxable, rental expenses — including the $9,818 depreciation — disallowed). I judged the statutory
concern (renting cheaply to a *related* person) does not reach a long-standing arm's-length lease, and
the library's second sentence points the same way. **But the condition is not clearly satisfied**:
$1,500 is 42% below the stated market of $2,600, and "a fair rental for that lease" is exactly the
contested question.

Cost of being wrong (illustrative): rental loss allowed 0 instead of 19,550 → AGI 110,900, taxable
income 79,400, 8962 household income 110,900 =
355.4% FPL, applicable figure 7.386%, PTC 6,044.34, excess 3,855.66, repayment **capped at 3,150**
(300–<400% band). So the exposure is the 19,550 of lost deduction **plus** $1,250 of extra PTC
repayment. **Federal tax at TI $79,400 cannot be computed — the tax-table excerpt covers only MFJ
$59,000–$61,000.** I am leaving that branch open rather than inventing a tax figure. *(Client answers
2026-10-25 strengthened the primary call — unrelated, broker-sourced tenant, rent never raised — but
could not supply the lease or market evidence the library's condition needs, so this branch stays
disclosed: QUESTIONS.md B4.)*

## 5. Leo: not claimed, even though he lives with us

**Decided:** father's year (odd-numbered), no dependency, no CTC. Authority: the custody order ¶9 plus
[1040_instructions_tax_computation.md] ("where a decree or agreement alternates years, the agreement
controls"; a child claimed by the other parent under a Form 8332 release is not your qualifying child
for the credit).
**Rejected alternative:** claim Leo as the custodial parent because "the child resides primarily with
the Mother," which would add $2,200 of CTC. The library text on alternating agreements is directly on
point and controls. **Closed 2026-10-25:** Elena confirmed she **executed the Form 8332** releasing
2025 (the odd year) to the father — the order's mechanism was actually carried out, so the rejected
alternative is gone: Leo is the father's claim, CTC $2,200 (Sofia only) locked. *(Elena's answer
contained a literal "{TY}" placeholder, read as 2025; the order makes 2025 the father's year, so the
reading is safe.)* Leo remains a covered individual on the 1095-A, which is why the 8962 family-size
question survives as the one open item (Q/B1).

## 6. 8962 family size / FPL: used the family-of-4 line that is in the library

**Decided:** FPL $31,200 (family of 4), the only poverty line in the library, matching the four
individuals covered on the 1095-A (Marcus, Elena, Sofia, Leo).
**Rejected alternative:** family size of **3**, because we claim only Sofia as a dependent — that is
arguably the technically correct 8962 family size, but **the 2025 FPL for a family of 3 is not in the
library**, so I refuse to cite a number for it.
Sensitivity only, **[unverified figure: 27,960 for a family of 3 — not in the library, magnitude
only]**: 326.7% FPL → applicable figure 6.668% → PTC 7,094.43 → excess 2,805.57 → repayment **2,805.57**
(limit rises to 3,150 at 300%) instead of 1,900 → federal refund ~**1,416** instead of 2,322, i.e.
about **$906 worse**. This is the single most valuable open question in the 8962 (now QUESTIONS.md
B1 — the client did not answer it).

## 7. Coverage months: six months, no missing-1095-A assumption in the other direction

**Decided:** annual PTC built on Jan–Jun only. The 1095-A totals (10,320 / 10,140 / 9,900) are exactly
6 × the monthly figures, and the move explains the coverage ending. **Rejected alternatives:** (a) assuming 12 months of coverage — for illustration, at the same monthly
amounts the credit would be 12 × 1,255.209 = 15,062.51 against 19,800 of advance payments = 4,737.49
excess, still capped at **1,900** for this income band, so the repayment would not move but every Form
8962 line would change and the return must reconcile to the actual documents; (b) assuming a Florida
marketplace plan for Jul–Dec with no form in the file. Elena's
W-2 box 12 DD of $7,140 for **Jul–Dec** supports employer coverage taking over in H2. *Client
confirmed 2026-10-25: "I got on Halvorsen's plan July 1 … we dropped the marketplace plan" — there is
no second 1095-A and there will not be one; six covered months is final.*
The 1095-A also carries a garbled "Months covered 21–26" fragment; I read the covered months as
January–June from the labelled row and confirmed it arithmetically, rather than reading "21–26" as
months.

## 8. Tax Table, not the rate schedule

**Decided:** $6,708 from the table row (59,850 falls in the ≥59,850/<59,900 row). Rejected: computing
from the bracket footnotes, which the library expressly marks "for reference only — not to be used
under $100,000." Also rejected: interpolating outside the excerpt. This is why the answer is sensitive
to every other decision — a taxable income outside $59,000–$61,000 cannot be priced from this library.

## 9. NY residency end date and day count

**Decided:** resident Jan 1 – Jun 30 = **181 days**. Rejected alternatives: (a) residency ending
July 2 (183 days), on the theory that a NY abode existed until the FL home closed — they were out of
the Brooklyn lease June 30, so there was no NY abode available to them; (b) residency through July 3,
using the closing date — the closing date is when FL domicile *began*, not when NY residency ended.
The difference (181 vs 183 days) does not change my wage allocation (100% under the convenience rule)
but would matter under the day-ratio alternative: 181/365 = 0.49589 vs 183/365 = 0.50137.
**Assumption flagged:** the library excerpt does not contain NY's residency definition (abode test /
183-day test), so part-year status itself is assumed. NY visits after July 1 would count; the client
did not supply day counts (QUESTIONS.md B6) — immaterial to the wage allocation now that the
convenience treatment is confirmed (see §10), relevant only to the flagged residency assumption; the
Brooklyn lease ended June 30 and nothing suggests a maintained NY abode.

## 10. NY wages: convenience-of-the-employer rule applied to both spouses

**Decided:** Marcus $68,000 and Elena $54,000, both 100% NY source. Both employers are NY-based; the
file's language ("he just works remotely now"; Halvorsen let me — emphasis added — "go fully remote")
reads as
employee convenience, and the library makes that NY source income. *Client confirmed 2026-10-25: the
company "said remote was fine when I asked to move; they didn't need me out of state"; Halvorsen
"closed their Tampa office years ago; they approved my request." The out-of-state work was for the
employees' own convenience, and there was no longer even a Halvorsen office in Tampa — the library's
exception for days worked out of state "for the employer's necessity" is affirmatively refuted.*
**Rejected alternative:** day-ratio allocation (Marcus 33,720.55, Elena 26,778.08), which applies only
if the out-of-state days were for the **employer's necessity**. The employer's own W-2 state wages
(box 16 shows the full $54,000 / $68,000 as NY wages) are consistent with, though not proof of, the
convenience treatment; note the employers' withholding is not authority for NY source status.
**Both employers kept withholding NY tax all year** ($6,752 combined). Because the library has no NY
rate schedule or deductions, I cannot say whether that is an overpayment or a shortfall on IT-203 —
left open rather than estimated (QUESTIONS.md B6).

## 11. Sign conventions and the line-8 label

The contract's field `8_other_income_sch1` is where both losses land (Schedule E Part I rental and
Part II S corp both feed Schedule 1 line 5 → line 8), so it is **negative 31,050**, not just the
rental. `form8582.rental_loss` is stated as negative (−21,018) and the allowance/allowed/carryforward
as positive; `34_refund_or_37_owed` is +2,322 = **refund**. Rejected alternative: putting the S-corp
loss outside line 8, which would break the AGI arithmetic.

## 12. Standard deduction vs itemizing (and the Schedule A gap)

Decided: $31,500 standard. I added mortgage interest 6,480 + NY withholding 6,752 = 13,232 and did not
worry about the SALT cap or acquisition-debt limits **because those rules are not in the library
[unverified]** and cannot change the answer: even the twice-counted 18,372 is under 31,500. Rejected
alternative: reporting an itemized total as if I had authority to compute it.
