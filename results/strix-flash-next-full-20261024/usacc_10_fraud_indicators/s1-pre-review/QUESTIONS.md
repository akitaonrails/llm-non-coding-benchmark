# Questions for the Partnership Finance Committee / client — Q1 2026 close

Answers are requested in writing. Items A1–A3, B and E are connected to the irregularities report
(`communication_to_dr_r_patel.md`) filed under ¶4 of the engagement letter; because that report
may involve the Managing Partner, we request that answers come from the Committee, not from Dr. Harlow,
until the Committee directs otherwise.

## Response status — 2026-10-25

Responses received from "Carla" (staff respondent; surname not in the documents we hold — we do not assume she
is the "office mgr" named in `vendor_master.csv`). For all other items the client states it has **no additional
information**. Answered parts are not re-asked below; partial items list only what is still missing.

| # | Status | What we now know / still need |
|---|---|---|
| A1 | **No answer** | Complete register, ADP detail, ID-sequence confirmation still missing |
| A2 | **No answer** | ADP billing statements, Form 941, state wage reports still missing |
| A3 | **Partial** | Answered: staff has **never met** T. Nguyen; per Carla, Dr. Harlow said the person "works from home on regional projects"; payment is a **paper check mailed to the P.O. box**. Still needed: offer letter, I-9, job description, time records/work product, and **which account those checks are drawn on** (no such check appears in the account provided) |
| A4 | **No answer** | Still needed — and now pointed to by A3: if the Nguyen checks are real, they come from an account we have not been given |
| B1 | **Partial** | Answered: Dr. Harlow created the vendor himself. Still needed: W-9, beneficial ownership, confirmation of the Kevin Marsh relationship |
| B2 | **Partial** | Answered (corroboration): Carla has **never seen a delivery** from Summit Supply. Still needed: contract/SOW, deliverables, maintenance work orders |
| B3 | **Partial** | Answered: the documented authority is none — Dr. Harlow told staff verbally to "just pay those when they come in". Still needed: any written waiver authority and the second-partner acknowledgment |
| B4, B5 | **Open — Committee decisions, not client questions** | Classification and suspension direction still awaited |
| C1 | **No answer — UNKNOWN, flagged** | Funding source of the overdrawn balance remains unidentified |
| C2 | **No answer — UNKNOWN, flagged** | Bank overdraft handling unknown; no fees/returned items appear in the statement |
| D1 | **No answer** | Lease, payee legal name/W-9, vendor setup for the rent payee still missing |
| D2 | **No answer** | Schein/Patterson invoices, POs, approvals still missing |
| D3 | **No answer** | Processor statements still missing; gross-vs-net of merchant fees remains **unknown** |
| D4 | **No answer** | Dentrix recurring amount unconfirmed |
| E1–E3 | **Open — Committee** | Instruction source, independent review, population completeness |

If the client has no further documents, items A1, A2, C1, D1–D3 can only be closed by the Committee
obtaining them from third parties (ADP, the bank, the processor, the landlord) or they stay open.

## A. Payroll

- **A1. Complete Q1 payroll register.** The file provided (`documents/payroll_register_q1.csv`) lists only 7
  employees (IDs E-01, E-02, E-03, E-14, E-15, E-22, E-23; if the IDs run sequentially, E-04…E-13 and E-16…E-21
  are absent) and
  $65,576.15 gross per period × 6 periods = $393,456.90, against bank ADP payroll debits of $526,713.92 —
  a **$133,257.02** difference. Please provide the full register for all six Q1 periods for **all** employees:
  gross pay, each deduction, employer taxes, and the payee/method per employee. Please also confirm whether the
  employee-ID sequence is continuous and, if so, who IDs E-04…E-13 and E-16…E-21 are.
- **A2. ADP billing detail.** Provide the six ADP billing statements / payroll registers matching each ACH debit
  (2026-01-15, 01-28, 02-15, 02-28, 03-15, 03-28) showing how each debit splits between **net pay, employee
  withholdings, and employer taxes**, plus the Q1 2026 Form 941 and state quarterly wage reports. The six
  `ADP TAX` debits ($24,479.29 + $24,671.21 + $24,217.06 + $24,130.66 + $24,257.41 + $24,580.93 = $146,336.56)
  cannot be classified without this; we have kept them out of "payroll" to avoid double-counting.
- **A3. T. Nguyen (E-22).** Provide the signed offer letter, Form I-9, job description, and any time records or
  work product for the "Regional coordinator" hired 2025-08-01 ($2,850.00/period → $17,100.00 in Q1). Why are
  time-clock hours zero and benefits off? Why is this employee on a **paper check** and a **PO Box in Plano, TX**
  while every other employee is on direct deposit? Who prepares and releases that check, and from which account
  is it drawn (no such check appears in the account we were given)?
- **A4.** Are there employees at the three locations (Balcones, Round Rock, Cedar Park) who are paid from an
  account we have not been given? If so, please provide those account statements for Q1 2026.

## B. Summit Supply LLC (vendor V-017) — $44,250.00 in Q1

- **B1.** Provide a completed **W-9** and beneficial-ownership information for Summit Supply LLC
  (`documents/vendor_master.csv` shows `w9_on_file = no`), and confirm the relationship, if any, between
  Summit and Kevin Marsh (listed as K. Harlow's brother-in-law at the vendor's street address).
- **B2.** Provide the written contract / statement of work and the actual **deliverables** for the four
  "Consulting"/"practice optimization" invoices (SS-100, SS-102, SS-105, SS-106; $19,600.00) and the two
  "Equipment maintenance" invoices (SS-103, SS-108; $9,800.00), including work orders for the maintenance.
- **B3.** On what documented authority was the purchase-order requirement waived (`po_required = "no (exempted by KH)"`),
  and where is the second-partner acknowledgment the 2022 approval policy requires for a new vendor
  (`documents/approval_policy.md`)?
- **B4.** How should the nine payments be characterized in the books — supplies, management/consulting fees,
  or something else? Until we are told, they are shown separately in `q1_close.json` under
  `summit_supply_consulting_and_maintenance` ($29,400.00) and `summit_supply_supplies_misc` ($14,850.00).
- **B5.** Does the Committee want further Summit payments suspended and the vendor record deactivated pending
  its review? We will not stop or release payments on our own authority.

## C. Funding of the cash deficit

- **C1.** The Capital City Bank operating account (…0441) has been **overdrawn since 2026-02-28** and ends
  Q1 at **($118,735.42)**, with monthly deficits of $109,327.94 / $115,665.04 / $106,182.62 and no loan,
  transfer-in, or owner-contribution credits in the statement. What is funding the shortfall — another bank
  account, a line of credit, owner advances, or an intercompany transfer? Please provide **statements for all
  business bank accounts** for 2026-01-01 through 2026-03-31.
- **C2.** How are the bank's negative running balances being handled by the bank (overdraft notices, fees,
  returned items)? None appear in the statement.

## D. Other vendors and support

- **D1. PROPERTY MGMT RENT 3 LOCATIONS** ($21,600.00 × 3 = $64,800.00): there is **no vendor-master record** and
  no lease in the file. Provide the lease(s), the payee's legal name/W-9, and the vendor setup.
- **D2.** Provide invoices and purchase orders for **Henry Schein** ($34,046.10 Q1; each monthly debit exceeds the
  $5,000.00 two-partner-plus-PO threshold and `po_required = yes`) and **Patterson Dental** ($13,534.66), and the
  approvals required by `documents/approval_policy.md`.
- **D3. Revenue detail:** the 12 merchant deposits ($509,241.47) are our only revenue evidence. Provide the
  merchant-processor statements and the production / insurance-receivable reports so we can state whether the
  deposits are gross or net of merchant discount fees (currently unknown; we flagged it rather than assumed).
- **D4.** Confirm the Dentrix subscription ($1,290.00 × 3) is the correct recurring amount.

## E. Instructions and governance

- **E1.** Confirm that the Committee (not the Managing Partner) directs our work while the ¶4 report is open,
  and tell us **when** we may discuss the reported items with Dr. Harlow.
- **E2.** Has the Committee engaged independent counsel and/or a forensic specialist (our recommendation)? If a
  forensic specialist is engaged, we would request their Q1 payroll reconciliation so the $133,257.02 payroll
  difference can be closed on their work rather than ours.
- **E3.** Is there any Q1 activity outside this operating account (petty cash, credit cards, Zelle/Venmo for
  patient co-pays) we should be told about before the close is considered final?
