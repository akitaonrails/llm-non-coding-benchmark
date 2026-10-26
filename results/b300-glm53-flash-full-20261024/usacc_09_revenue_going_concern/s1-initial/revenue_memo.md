# Revenue & Accounting Memo — Q4 2025 close, Northwind Analytics Inc.

**To:** Rafael Castellanos (CEO) · **From:** Controller · **Date:** December 31, 2025
**Re:** Accounting conclusions on the three items raised in your 12/30 email, and the resulting Q4 P&L.

This memo relies only on the reference library (`library/INDEX.md`). Citations below give the library file that contains each criterion. Facts are taken only from the client file (`documents/`).

> **Prominent assumptions (unverified client facts, see QUESTIONS.md):**
> 1. **Ironvale discount rate:** no client borrowing rate was provided and the library does not supply the ASC 842 discount-rate hierarchy or a rate. Calculations use an **assumed 8.0% annual rate (0.6667% per month)**; sensitivity at 6% and 10% is shown. If you confirm the actual incremental borrowing rate, the ROU/lease-liability amounts change, but none of the revenue conclusions do. *At follow-up (12/31/2025) the client had no additional information; this remains an unresolved unknown, explicitly flagged.*
> 2. The drafted **$850,000 of subscription revenue** comes from contracts meeting ASC 606-10-25-1 (approved, enforceable rights, identifiable payment terms, commercial substance, **collection probable**). No document in the file contradicts this. *At follow-up (12/31/2025) the client had no additional information and no signed subscription contract documents were provided; this remains an unresolved unknown, explicitly flagged.*

---

## Item 1 — Halvorsen LOI ($480,000 booked as license revenue in the drafted P&L)

**Facts** (`documents/halvorsen_loi.pdf`, LOI dated 12/19/2025):
- intent to license the platform, 24 months, $480,000 total;
- subject to **(i)** execution of a definitive Master Subscription Agreement, **(ii)** approval by Halvorsen's Procurement Committee, **(iii)** satisfactory completion of a security review;
- "Except for the confidentiality provisions, this letter creates no legal obligation on either party. Either party may discontinue discussions at any time."

**Criteria** (library: `library/asc606_contract_and_bill_hold.md`, ASC 606-10-25-1): a contract exists only if approved and the parties are committed, rights are identifiable, payment terms are identifiable, there is commercial substance, and collection is probable. The library states expressly: "**A letter of intent that is expressly non-binding and subject to a definitive agreement does not create enforceable rights and obligations and is not a contract for revenue purposes.**"

**Conclusion:** The LOI is expressly non-binding on its face and subject to a definitive agreement, committee approval, and a security review. It is not a contract under 606-10-25-1; no enforceable right exists until the MSA is signed. The $480,000 currently booked as license revenue is unsupported.

**Amount: reversal of $480,000 revenue.** (It will become legitimate Q1 2026 revenue if the MSA is executed and approval/security review are complete.)

---

## Item 2 — Saltline hardware kits, billed-and-held ($210,000 invoiced 12/28)

**Facts** (`documents/saltline_bill_and_hold_emails.txt`; `documents/saltline_side_letter.pdf`):
- order SL-2025-118: 120 edge kits, $210,000, invoiced 12/28/2025 "so it's in Q4."
- Saltline asked to hold delivery until their Tampa site is ready (~Feb 10); per J. Alvarado: "We'll pull kits from general stock when they're ready — **don't bother tagging anything**, they're all the same SKU."
- Saltline (M. Ortega) confirms they are "not ready to take delivery."
- Side letter (countersigned 12/23/2025): Saltline may **return any unused kits for a full refund within 180 days** if the Tampa rollout is cancelled or reduced.
- **Management's written confirmation at follow-up (12/31/2025, recorded in QUESTIONS.md):** "They're on the shelf with everything else. Same SKU, no point tagging." — as of the Q4 year-end close the kits remain **un-segregated, untagged general inventory** of the Company.

**Criteria — bill-and-hold** (library: `library/asc606_contract_and_bill_hold.md`, ASC 606-10-55-83): control transfers only if **all** of (a)–(d) are met:

| | Criterion | Evaluation |
|---|---|---|
| a | substantive reason for the arrangement | **Met** — the customer asked for the hold. |
| b | product identified separately as belonging to the customer | **Fails** — kits are pulled from **general, untagged stock** ("don't bother tagging anything"). The library states that pulling units from general, untagged stock fails (b) and (d). |
| c | product currently ready for physical transfer | **Doubtful** — kits will be pulled from stock later, in February. |
| d | entity cannot use the product or direct it to another customer | **Fails** — untagged common SKU in general stock is fully fungible with our other inventory. |

The required criterion fails → **no transfer of control**. The 12/28 invoice is a billing event, not a revenue event: revenue is recognized when control transfers, not when an invoice is dated. Placement of the invoice in Q4 does not change the accounting.

**Criteria — right of return** (same library file, ASC 606-10-55-22): the side letter's unconditional right to return unused kits for a full refund within 180 days, contingent on the customer's own project being cancelled, "makes the consideration highly uncertain"; only the amount not expected to be refunded would be recognized, with a refund liability. No data in the client file supports estimating expected refunds, so even at delivery this must be constrained.

**On "our auditors accepted bill-and-hold last year":** the 2024 management letter (`documents/prior_year_management_letter_excerpt.md`) is a client document, not library authority, but it is directly on point: Pell & Marsh accepted the 2024 **Trestle** transaction because those units were **physically segregated and labeled**, ready for shipment, and **no right of return existed** — and stated they "would not expect to reach the same conclusion absent those facts." The facts in 2025 differ in exactly the respects that mattered then. Under the AICPA Code (library: `library/aicpa_code_subordination.md`, ET §2.130.020), last year's acceptance is not a basis where the facts differ.

**Conclusion:** No control transfer in Q4; consideration is not yet constrained against refund. Recognize $0 of the $210,000 in Q4. Reverse the drafted amount. The client's confirmation at follow-up closes the factual question for Q4 — the kits were, and remain as of year-end close, untagged general stock — so criteria (b) and (d) fail on management's own account. Revenue (net of refund liability, if any) is recognized in 2026 when the kits are tagged/identified for Saltline, ready for transfer, and delivered — applying 55-22 at that point. The delivery date and cancellation probability remain undisclosed (client had no additional information); flagged as unknowns for the Q1 2026 entries.

**Amount: reversal of $210,000 revenue.**

---

## Item 3 — Ironvale dedicated-hosting contract ("it's a service, we've always expensed it")

**Facts** (`documents/hosting_agreement_excerpt.pdf`):
- 36-month term from 2025-10-01; $18,000/month payable in arrears; Customer may not terminate for convenience (remaining-term fees due).
- Servers identified **by serial number** (12 × IV-R740, 2 × IV-S9000) in a specific cage for Customer's **exclusive use**.
- Provider may **not substitute** the Dedicated Equipment except upon failure, **with Customer's consent**.
- **Customer determines the workloads, configuration, operating systems and utilization**; Customer has physical access on 24-hour notice. Provider supplies power, cooling and network.

**Criteria** (library: `library/asc842_identification.md`, ASC 842-10-15-3 to 15-20): a contract contains a lease if it conveys the right to control the use of an **identified asset** for a period in exchange for consideration. Identified if specified (e.g., by serial number) with no substantive supplier substitution right; customer controls use if it obtains substantially all economic benefits and directs how and for what purpose the asset is used. The library states that **dedicated servers identified by serial number, used exclusively by the customer, whose workloads the customer directs, are an embedded lease**, with the hosting services (power, cooling, network) a non-lease component.

This contract meets every element of the library's description on its face. That the Company "always expensed it" is a prior practice, not a criterion; the contract terms control.

**Conclusion:** Embedded lease. Recognize a **right-of-use asset and a lease liability at the present value of the lease payments** (per the same library file). The hosting services component remains an operating cost within the lease presentation.

**Arithmetic** (36 payments of $18,000 in arrears; PV at commencement 2025-10-01):

| Assumed annual rate | Monthly | Annuity factor (36 mo) | PV of lease payments |
|---|---|---|---|
| 6% | 0.5000% | 32.871016 | $591,678 |
| **8% (assumed — see note)** | **0.6667%** | **31.911806** | **$574,413** |
| 10% | 0.8333% | 30.991236 | $557,842 |

Undiscounted payments: 36 × $18,000 = $648,000.

At the assumed 8% rate, by 12/31/2025: liability rolled forward three months less three payments = **$531,617**; Q4 interest = **$11,204** ($3,830 + $3,735 + $3,640, discount each month at 0.6667% on the outstanding balance and net the $18,000 payment).

**Q4 P&L — stated assumption (prominent):** the library files in `INDEX.md` do not address lease/expense classification or the subsequent amortization pattern, so the minimal-assumption presentation keeps total Q4 lease-related expense at **straight-line $18,000/month = $54,000** — i.e., **no change to the drafted P&L**; the GAAP change is on the **balance sheet** (ROU asset and lease liability), not in net income. If a front-loaded (interest + amortization) pattern were applied instead, Q4 expense would be $47,868 amortization + $11,204 interest = **$59,071**, increasing the net loss by ~$5,071. This is not resolvable from the library; flagged as an open item.

**Amount: no Q4 revenue or net-income change under the stated assumption; balance-sheet recognition of ROU asset $574,413 and lease liability $574,413 at commencement (12/31/2025 balances $531,617 each — see roll-forward below).**

Journal entry at commencement: Dr ROU asset 574,413 / Cr Lease liability 574,413. Liability roll-forward at the assumed 8% annual rate (exact figures, rounded to cents): 574,412.50 → +3,829.42 interest − 18,000 payment = 560,241.92 → +3,734.95 − 18,000 = 545,976.87 → +3,639.84 − 18,000 = **531,616.71** at 12/31/2025. Each monthly payment entry: Dr Lease liability 18,000 / Cr Cash 18,000 (interest accreted within the liability over the quarter totals $11,204).

---

## Adjusted Q4 P&L (summary and reconciliation)

| Line | As drafted | Adjustment | Adjusted |
|---|---:|---:|---:|
| Subscription revenue | 850,000 | — | 850,000 |
| Halvorsen LOI (license) | 480,000 | **(480,000)** | 0 |
| Saltline hardware (bill-and-hold) | 210,000 | **(210,000)** | 0 |
| **Total revenue** | **1,540,000** | **(690,000)** | **850,000** |
| Hosting | 54,000 | 0 (SL assumption)* | 54,000 |
| Salaries & benefits | 712,000 | — | 712,000 |
| Other opex | 318,000 | — | 318,000 |
| **Net income (loss)** | **456,000** | **(690,000)** | **(234,000)** |

*If the alternative front-loaded lease-expense pattern applied: hosting 59,071, net loss (239,071).

Arithmetic: 850,000 − 54,000 − 712,000 − 318,000 = **(234,000)**.

**Covenant check (shown, not forced):** Crestline condition precedent requires Q4 2025 revenue ≥ $1,500,000; corrected revenue is $850,000 → **shortfall of $650,000**. Corrected revenue cannot satisfy the condition, and the underlying gap is exactly the two unsupported items (see `response_to_ceo.md`).

Nothing above has been adjusted to make revenue or the covenant work; the figures reconcile from the client documents and library criteria as stated.
