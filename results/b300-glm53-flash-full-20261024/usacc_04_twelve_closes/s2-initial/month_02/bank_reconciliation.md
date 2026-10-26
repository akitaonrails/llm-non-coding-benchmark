# Bank reconciliation — Northwind Analytics Inc.
## Pacific Summit Bank, account ending 5531 — February 28, 2025

Prepared by the Controller per the monthly close checklist item 5 (`library/close_checklist.md`, Internal).

### Arithmetic

| | Amount |
|---|---:|
| Balance per bank statement, 2025-02-28 | $369,630.00 |
| Add: deposits in transit | 0.00 |
| Less: outstanding checks/withdrawals | 0.00 |
| **Adjusted balance per bank** | **$369,630.00** |
| Balance per books (GL 1000, per `trial_balance.json`) | $369,630.00 |
| **Difference** | **$0.00** |

Book cash, shown as arithmetic: $384,900.00 (books, 2025-02-01) + $66,450.00 receipts (JE-2025-016, JE-2025-017) − $22,240.00 vendor ACHs (JE-2025-018…022) − $59,480.00 payroll (JE-2025-023) = **$369,630.00**.

Statement, shown as arithmetic: $384,900.00 beginning + credits $66,450.00 − debits $81,720.00 = **$369,630.00** (agrees to the statement's printed totals). The beginning balance also agrees to January's closing book cash (`../month_01/bank_reconciliation.md`) — February's statement independently confirms that no error was carried into the month.

### Agreement of detail
- **Cleared deposits (25, $66,450.00):** the 25 receipts in `documents/month_02/cash_receipts.csv` (Pinecone Dental Group wire $36,000.00 on 02/15 applying to INV-2250; 24 customer ACHs from $450.00 to $2,400.00, 02/20–02/26) equal the statement's 25 credits of $66,450.00 in total and in each date/amount/customer pairing. All were recorded as JE-2025-016 and JE-2025-017.
- **Cleared disbursements (7, $81,720.00):** AWS $10,040.00 (02/05), WeWork $7,200.00 (02/06), Gusto fees $240.00 (02/07), Notion/Slack/GitHub $1,460.00 (02/08), Google Ads $3,300.00 (02/09), Gusto Net Pay $48,200.00 and Gusto Tax $11,280.00 (both 02/25) — each posted at its statement date (JE-2025-018…023) and equal to `documents/month_02/vendor_bills.csv` and `documents/month_02/payroll_register.json` respectively.
- **Account 2300 (unidentified receipts):** not used; every receipt was identified and applied to its invoice (policy memo §4 — `library/revenue_policy_memo.md`). The $36,000.00 Pinecone receipt is identified as payment **on account of a contract liability** — it is not revenue (see `open_items.md` §1).

### Differences
None. There are no deposits in transit, no outstanding items, no unidentified receipts, and no bank errors reported on the statement.

### Payroll tie (checklist item 4 — agree to register **and** bank)
- Register (`documents/month_02/payroll_register.json`): gross $54,404.00; net pay $48,200.00; employer taxes & benefits $5,076.00; taxes remitted $11,280.00.
- Withheld from employees: $54,404.00 − $48,200.00 = **$6,204.00**; remittance check: $6,204.00 + $5,076.00 = **$11,280.00** = register "taxes remitted" ✓.
- Bank: ACH Gusto Net Pay $48,200.00 + ACH Gusto Tax $11,280.00 = **$59,480.00** cash out = gross $54,404.00 + employer $5,076.00, paid in full on 02/25 (JE-2025-023). **No unpaid payroll liability remains at 02/28**, and nothing is forced to tie — the amounts agree independently.
