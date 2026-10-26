# Questions register — Ray Brightline / Brightline Cabinetry LLC

Status as of 2026-10-25: all four questions were put to the client. The client answered Q2 and states that
for the remaining questions **he has no additional information** — so the fallbacks below are stated
prominently in every deliverable, and each remaining unknown is flagged with who can resolve it and why it
matters. Do not re-ask the client what he has already answered.

---

## Q1 — Accounting method / tax basis in the $200,000 receivables — **UNANSWERED (client has no info)**

*Asked:* Is Brightline Cabinetry a cash- or accrual-method taxpayer, and what is the tax basis of the
$200,000 accounts receivable? (Last filed Form 1120-S answers this.)

*Fallback used:* **Cash method, $0 basis** — the $200,000 is ordinary income in every Buyer A scenario
($74,000 of sale-year tax at 37%). Conservative for the sale-year estimate.

*Why it is now outcome-relevant, not a footnote:* if the CPA confirms **accrual with basis = face**, each
A scenario's sale-year tax drops **$74,000** (that income was taxed when earned in prior years; lifetime
tax is similar), and at a 2026 close the **counter-allocation flips past Buyer B's PV by ≈ $11,512**
(best-case VI = 0: ≈ $28,512). The deal recommendation can change on a one-phone-call fact — **Ray's CPA
should confirm the method before Friday.**

*Related tension flagged:* the 1/1/2023 conversion appraisal lists built-in gain "other assets: $0," which
fits an accrual AR (basis = face). Under the cash-method fallback, the receivables would nominally carry
$200,000 of conversion BIG; if that contrary-to-appraisal reading is ever asserted, entity §1374 tax rises
to $279,300 and each A net falls $26,460. The primary model uses the appraisal as written.

**Resolve by:** CPA, from the last filed Form 1120-S.

## Q2 — Liabilities assumed / retained — **PARTIALLY ANSWERED**

*Asked:* What payables will Lone Star actually schedule at closing, and what contingencies (lawsuits,
warranty, tax disputes) exist?

*Client answer (2026-10):* "There's the Hardaway dispute ($9,800) and the usual warranty stuff. Nothing
big that I know of."

*What that resolves:* the known contingency pool is ≈ **$9,800 + unquantified warranty**. Modeled in full:
- **Deal A (Lone Star assumes only scheduled payables):** Hardaway and warranty stay with the seller —
  after-tax ≈ **$6,174** on Hardaway (37% pass-through deduction), $0.63 per $1 of warranty claims.
- **Deal B (Hensley assumes all liabilities, known and unknown):** **$0** to Ray if Hardaway is disclosed
  on the schedules; worst case **$8,129** after tax if repriced at the PSA. Neither moves the ranking
  (≈ 1% of the gap). Warranty exposure is **unquantified — flagged, not modeled.**

*What remains open:* the **dollar amount of trade payables** Lone Star will assume is still unknown (no
payables schedule in the file). **Fallback: $0 assumed liabilities.** Each assumed payable is extra
consideration added under the §1060 residual method (`library/irc_1060_form_8594.md`) — the effect is
taxed at the marginal class rate and slightly favors A; it cannot plausibly close a $45k–$158k gap.

**Resolve by:** PSA payables schedule (both deals); warranty loss history via the CPA/insurer.

## Q3 — Target closing date — **UNANSWERED (client has no info)**

*Asked:* When do you expect/ want to close, and is the buyer flexible on date?

*Fallback used:* **2026 close** — inside the §1374 recognition period (1/1/2023–12/31/2027 per
`library/irc_1374.md` (d)(7)), so the $237,300 entity-level BIG tax applies in every A scenario.

*Why it matters:* this is **the single biggest lever in the engagement — worth $149,499 after tax.** A
close after 12/31/2027 zeroes the entity tax: A-counter nets $2,435,300 and **beats B's PV by ≈ $87,000**
(best case ≈ $104,000); even drafted A closes to within ≈ $8,200 of B. At a 2026 close, B wins on PV in
every allocation. The whole negotiation strategy (§7 of the memo) is built on this: sign with A now,
close January 2028, or extract ~$150k of price to compensate.

**Resolve by:** Ray's decision + buyer flexibility; it is a deal term, not a fact to look up.

## Q4 — Material participation / NIIT — **UNANSWERED (client has no info)**

*Asked:* Do you materially participate in the business (you work in it daily)?

*Fallback used:* **Material participation** — owner-operator selling his own shop; per
`library/capital_gain_rates.md` the net investment income tax does not apply to active business gains,
so no NIIT is modeled.

*Sensitivity if wrong:* +3.8% × $2,720,000 gain = **+103,360** on every A scenario vs.
+3.8% × ($2,430,000 + $90,000 interest) = **+95,760** on B — a further ≈ $7,600 against A. **The 3.8%
rate is not in the library [unverified]**; the direction (it hits both, more of A's gain) follows from
the library's NIIT description.

**Resolve by:** CPA (participation records are Ray's own, but the NIIT interaction needs a preparer).

---

*Nothing else in the deliverables depends on client-only facts. All other open flags (BIG-loss ordering
convention, note credit-risk discounting, Texas franchise tax, B's post-closing S-election termination,
B's $0-covenant reallocation risk) are labeled in the memo and comparison.json as conventions or
outside-library items.*
