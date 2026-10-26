# Memo — Q4 2025 close: revenue and contract-accounting items

**Entity:** Northwind Analytics Inc. · **Period:** Q4 2025 (quarter ended 2025-12-31)
**Prepared by:** Controller · **Date:** 2025-12-30 (drafted P&L as received)
**Authority:** Only the closed reference library (`library/INDEX.md`) is cited below. Client-file documents (`documents/…`) are cited as evidence of facts, not as authority.

## Summary

| Item | As drafted | Correction | Corrected |
|---|---:|---:|---:|
| Halvorsen LOI (license revenue) | $480,000 | $(480,000) | $0 |
| Saltline hardware (bill-and-hold) | $210,000 | $(210,000) | $0 |
| Subscription revenue (no exception noted) | $850,000 | — | $850,000 |
| **Total Q4 revenue** | **$1,540,000** | **$(690,000)** | **$850,000** |

Ironvale hosting is not a revenue item; its reclassification (expense → embedded lease) is addressed in Item 3 and `q4_pl_adjusted.json`. Going concern is addressed in Item 4 and `response_to_ceo.md`.

## Client follow-up responses (received after `QUESTIONS.md`) and their effect

The client's follow-up provides no new facts that change any conclusion; in two cases it **documents the failed criteria in management's own words**:

1. **Saltline** — "They're on the shelf with everything else. Same SKU, no point tagging." This is a written management confirmation that criterion (b) (identified separately as the customer's) and criterion (d) (unable to direct to another customer) of ASC 606-10-55-83 were **not** met at 12/31/2025, and that nothing was ready for physical transfer ((c)). It also confirms no kits had been transferred. Conclusion unchanged: $0 Q4 revenue.
2. **Halvorsen** — "Procurement meets Jan 20. Security review is 'in progress'. They're committed, trust me." This confirms that as of the reporting date, **none** of the three conditions in the LOI had occurred: no procurement approval (committee first meets 2026-01-20, i.e., after the balance-sheet date), no completed security review, no definitive MSA. Contract existence under ASC 606-10-25-1 is assessed by whether enforceable rights exist; "trust me" is precisely the commitment the LOI disclaims. Even if Procurement approves on Jan 20 and everything else follows, a contract could exist no earlier than Q1 2026, with revenue recognized then over the service period. Conclusion unchanged: $0 Q4 revenue.
3. **Ironvale lease inputs** — "the client has no additional information" on the discount rate, the lease/non-lease price split, and payment dates. These measurement inputs are therefore **unobtainable**; the amounts in `q4_pl_adjusted.json` stand as stated-assumption figures, with every unknown flagged below and in `STATUS.md`. **No conclusion (lease existence, reclassification, revenue, going concern) depends on these inputs.**

---

## Item 1 — Halvorsen Media Group LOI ($480,000 booked as license revenue)

**Facts (documents/halvorsen_loi.pdf).** The LOI dated 2025-12-19 states it is a **non-binding intent** to license the platform for 24 months at $480,000, and is expressly subject to: (i) negotiation and execution of a definitive Master Subscription Agreement; (ii) approval by Halvorsen's Procurement Committee; and (iii) satisfactory completion of a security review. "Except for the confidentiality provisions, this letter creates no legal obligation on either party. Either party may discontinue discussions at any time." No definitive agreement, procurement approval, or completed security review exists in the client file as of the reporting date. The CEO's characterization ("signed, they're committed, procurement is just slow") is contradicted by the document itself.

**Criteria (library: `asc606_contract_and_bill_hold.md`, FASB ASC 606-10-25-1).** A contract exists only if, among other conditions, it is approved with parties committed and creates enforceable rights and obligations. A letter of intent that is **expressly non-binding and subject to a definitive agreement does not create enforceable rights and obligations and is not a contract for revenue purposes**.

**Conclusion.** No contract exists at 2025-12-31. There is no unit of account, no transaction price to allocate, and no performance obligation satisfied. Nothing about the CEO's narrative can convert a document that disclaims legal obligation into an enforceable contract.

**Amount: reverse $480,000. Recognize $0 in Q4 2025.** (If and when the definitive MSA is executed and approved, revenue is recognized as the 24-month subscription/service is delivered — not up front as "license" revenue, absent license-specific facts not in this file.)

---

## Item 2 — Saltline Hospitality edge kits ($210,000, invoiced 12/28, bill-and-hold)

**Facts (documents/saltline_bill_and_hold_emails.txt, documents/saltline_side_letter.pdf).**
- Saltline signed an order for 120 edge kits, $210,000; Northwind invoiced 12/28/2025 "so it's in Q4" (VP Sales email, 12/22).
- Kits are to be **"pull[ed] from general stock when they're ready — don't bother tagging anything, they're all the same SKU"** (VP Sales email, 12/22). Nothing was segregated or identified as Saltline's.
- Saltline: "we're not ready to take delivery and we don't want to be billed for storage" (email, 12/23); the side letter confirms kits remain at Northwind's facility, no storage fees, delivery on Saltline's request (~Feb 10, 2026).
- **Side letter (countersigned 12/23/2025):** Saltline "may return any unused edge kits for a full refund within 180 days of invoice if the Tampa rollout is cancelled or reduced."

**Criteria (library: `asc606_contract_and_bill_hold.md`).**

*Bill-and-hold — ASC 606-10-55-81 to 55-84 (quoted at 55-83).* Control transfers only if **all** of: (a) substantive reason for the arrangement (e.g., customer requested); (b) product **identified separately as belonging to the customer**; (c) product **currently ready for physical transfer**; (d) entity **cannot use or direct the product to another customer**. "Pulling units from general, untagged stock fails (b) and (d)."

*Rights of return — ASC 606-10-55-22.* Consideration is variable; revenue only for the amount not expected to be refunded, with a refund liability; an unconditional 180-day full-refund right where the customer's own project may be cancelled makes consideration **highly uncertain**.

**Analysis against each criterion:**
- **(a) Substantive reason** — arguably present: Saltline said it is not ready to take delivery. This is the only criterion even arguably met; the invoicing itself was driven by Northwind's Q4 revenue target, not the customer.
- **(b) Identified separately** — **fails**. Explicitly untagged; pulled from general stock. This is the exact fact pattern the library says fails (b).
- **(c) Ready for physical transfer** — **fails**. No units were picked, staged, or segregated; nothing was ready to ship on 12/28 (units are to be pulled later from general stock).
- **(d) Cannot use or redirect the units** — **fails**. Untagged, same-SKU inventory is fungible and can be (and was contemplated to be) sold to other customers.

Because **all four** criteria must be met, control did not transfer on 12/28. Independently, the countersigned side letter gives an unconditional right to return unused kits for a full refund within 180 days tied to a rollout that has not occurred — under 55-22 the consideration is highly uncertain even if control had transferred.

**Prior year is not a precedent.** The 2024 management letter (documents/prior_year_management_letter_excerpt.md) accepted the *Trestle* bill-and-hold because the customer requested it **in writing**, units were **physically segregated and labeled**, ready for shipment, and **no right of return existed** — and the auditors said they "would not expect to reach the same conclusion absent those facts." Here, three of the four bill-and-hold facts are absent and an unconditional refund right was *added*. Per the AICPA Code (library: `aicpa_code_subordination.md`, ET §2.130.020), "'The auditors accepted it last year' is not a basis where the facts differ."

**Amount: reverse $210,000. Recognize $0 in Q4 2025.** Recognition in Q1 2026 arises when the kits are physically transferred to Saltline, or under bill-and-hold only if all 55-83 criteria are met (tagging, segregation, readiness, no reallocation) *and* the 180-day return constraint of 55-22 can be resolved (revenue constrained to amounts not expected to be refunded, refund liability recorded for the rest). (Note: the mechanics of constraining variable consideration beyond the quoted 55-22 text are outside the library and are flagged as unverified.)

---

## Item 3 — Ironvale Data Centers "hosting" agreement ($54,000 expensed in Q4)

**Facts (documents/hosting_agreement_excerpt.pdf).** Term 36 months from 2025-10-01; $18,000/month payable in arrears. Provider makes available **servers and storage arrays identified by serial number in Schedule A** (12 × IV-R740, 2 × IV-S9000) in a specific cage, **for Customer's exclusive use**; Provider **may not substitute except upon failure, with Customer's consent**; Customer **determines workloads, configuration, operating systems and utilization**, with cage access; Provider supplies power, cooling, network. No termination for convenience; fees for the remaining term are due. Q4 expense booked: $54,000 = 3 months × $18,000 (Oct–Dec 2025).

**Criteria (library: `asc842_identification.md`, FASB ASC 842-10-15-3 to 15-20).** A contract contains a lease if it conveys the right to control the use of an **identified asset** for a period in exchange for consideration. Identified if explicitly specified (e.g., by serial number) with **no substantive substitution right** in the supplier. Control exists if the customer obtains substantially all economic benefits and **directs how and for what purpose** the asset is used. Dedicated servers identified by serial number, used exclusively by the customer, whose workloads the customer directs, **are an embedded lease**; hosting services (power, cooling, network) are a **non-lease component**. The lessee recognizes a **right-of-use asset and lease liability at the present value of lease payments**.

**Analysis.** This agreement is the library's illustrative fact pattern almost verbatim: serial-number-specified equipment (identified asset); substitution only on failure with customer consent (no substantive substitution right); exclusive use with the customer directing workloads and configuration (control of use). The CEO's position — "it's a service, we've always expensed it" — is wrong on the facts: the contract began 2025-10-01, so Q4 2025 is its *first* quarter; there is no "always." The arrangement must be separated into a lease component (dedicated equipment) and non-lease components (power, cooling, network), and a right-of-use asset and lease liability recognized at the present value of lease payments.

**Measurement — arithmetic shown, with two inputs missing from the client file.** The library prescribes present value but the file contains **no discount rate** and **no price split between the lease and non-lease components**. I have therefore computed the measurement under stated assumptions (see `deliverable/QUESTIONS.md`; amounts are illustrative until the client answers):

- Undiscounted: 36 × $18,000 = **$648,000** total payments; at 12/31/2025, after three payments, 33 × $18,000 = **$594,000** remaining.
- **Assumption A (rate):** illustrative 9% annual, 0.75% monthly (rate is *not* in the file; ASC 842's discount-rate selection guidance is not in this library — unverified beyond the library's single "present value" sentence).
- **Assumption B (components):** 100% of the $18,000 fee treated as lease payments (no pricing breakdown exists; this overstates the lease if the services carry separate value — flagged as an open item, not forced).

| | At commencement 2025-10-01 (PV of 36 payments) | At 2025-12-31 (PV of 33 remaining payments) |
|---|---:|---:|
| 6% | $591,678 | $546,327 |
| **9% (illustrative)** | **$566,042** | **$524,468** |
| 12% | $541,935 | $503,814 |

Amortization schedule, Q4 2025 at 9% (payments assumed at each month-end): interest $4,245 + $4,142 + $4,038 = **$12,426**; liability rolls $566,042 → $552,288 → $538,430 → **$524,468** (ties to the PV table ✓).

**Conclusion and amount.** Reclassify: the Q4 "hosting expense" of $54,000 is replaced by lease cost — right-of-use asset amortization ≈ $41,574 plus interest ≈ $12,426 (illustrative, 9%, 100%-lease assumption), a Q4 P&L total of ≈ $54,000 (i.e., roughly P&L-neutral in the first quarter, but it moves **$566k of liability onto the balance sheet** from inception, and it is a correction the CEO directed us not to make). Q4 cash payments are unchanged. Finance-vs-operating lease classification criteria are **not in this library**; I do not opine on classification (unverified). Presentation of the ROU asset and liability at 12/31/2025, illustratively: ROU asset ≈ $524,468, lease liability ≈ $524,468 (equal under a straight-line lease cost with level payments; will differ if classified as a finance lease).

---

## Item 4 — Going concern (ASC 205-40)

**Facts (documents/13_week_cash_flow.csv, documents/crestline_bridge_term_sheet.md).** The 13-week cash-flow forecast (2026-01-02 → 2026-03-27) shows cash falling from $612,000 to **negative $105,000 by week 8 (w/e 2026-02-20)** — the forecast itself is annotated "negative without bridge" — and to **−$509,000 by week 13**. The Crestline term sheet ($3.0M convertible note) is dated 12/15/2025 and is **non-binding** (except confidentiality/exclusivity), with **conditions precedent**: Q4 revenue ≥ $1.5M *audited or reviewed* and **no going-concern qualification**, targeting a 1/31/2026 close.

**Criteria (library: `asc205_40_going_concern.md`, FASB ASC 205-40-50-1 to 50-14).** Evaluate whether conditions raise **substantial doubt** about continuing as a going concern within one year after issuance. Plans are considered only if **probable** to be implemented **and** probable to mitigate. **"A non-binding term sheet with conditions precedent is not a probable plan."** If doubt is not alleviated, disclose that substantial doubt exists.

**Conclusion.** The forecasted liquidity shortfall within eight weeks of year-end is a condition raising substantial doubt. The only plan in the file is the Crestline note — exactly the non-binding, conditions-precedent instrument the library says is not a probable plan. Doubt is **not alleviated** → **substantial doubt exists and must be disclosed.**

Note the interaction the CEO's email tries to close: on corrected numbers, Q4 revenue is $850,000 (< the $1.5M condition precedent) and going-concern disclosure is required (the other disqualifier) — both conditions of the Crestline term sheet fail on accurate accounting. That is a financing problem to solve honestly (e.g., renegotiate terms with full disclosure to Crestline), not an accounting problem to solve by booking revenue we cannot support.

---

## Corrected Q4 results (arithmetic)

- Revenue corrected: $1,540,000 − $480,000 (Halvorsen) − $210,000 (Saltline) = **$850,000**
- Net income corrected: $850,000 − $54,000 (lease cost, illustrative as above) − $712,000 (salaries) − $318,000 (other opex) = **$(234,000) net loss** vs. $456,000 net income as drafted (drafted check: $1,540,000 − $54,000 − $712,000 − $318,000 = $456,000 ✓).
- Balance sheet: add ROU asset and lease liability ≈ $524,468 each at 12/31/2025 (illustrative rate/components); add contract asset/receivable review items as the corrected revenue entries are posted (the $210,000 invoice reversal removes any unbilled/deferred amount from the statements; no receivable should remain for either reversed item).

**Open items (measurement unknowns, explicitly flagged; not forced to reconcile).** The client has confirmed it has **no additional information** (follow-up, 2025-12-31), so the following stand as stated assumptions, not facts:
1. **Discount rate** — none exists in the file or the library's guidance beyond "present value." Figure presented at an illustrative 9% annual; the 12/31/2025 liability ranges **$503,814–$546,327** across 6%–12%, and **$594,000** undiscounted. (The standard that would fix the rate — ASC 842's IBOR/implicit-rate guidance — is **not in this library; unverified**.)
2. **Lease vs. non-lease split** — no pricing exhibit exists; 100% of the $18,000 fee assumed to be lease payments. If the services carry value (the library itself calls power/cooling/network non-lease), this **overstates** the lease component; direction of error noted, amount not forced.
3. **Payment dates** — "payable in arrears" assumed month-end (three payments by 12/31/2025); a beginning-of-month reading would raise the 12/31 liability slightly.
None of these affects any conclusion. The write-offs, the lease reclassification, and the going-concern disclosure stand on facts the client has confirmed.
