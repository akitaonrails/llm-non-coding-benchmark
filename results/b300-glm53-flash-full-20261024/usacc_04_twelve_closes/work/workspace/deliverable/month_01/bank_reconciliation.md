# Bank reconciliation — Northwind Analytics Inc.
## Pacific Summit Bank, account ending 5531 — January 31, 2025

Prepared by the Controller per the monthly close checklist item 5 (`library/close_checklist.md`, Internal).

### Arithmetic

| | Amount |
|---|---:|
| Balance per bank statement, 2025-01-31 | $384,900.00 |
| Add: deposits in transit | 0.00 |
| Less: outstanding checks/withdrawals | 0.00 |
| **Adjusted balance per bank** | **$384,900.00** |
| Balance per books (GL 1000, per `trial_balance.json`) | $384,900.00 |
| **Difference** | **$0.00** |

Book cash, shown as arithmetic: $412,000.00 (books, 2025-01-01) + $54,450.00 receipts (JE-2025-003, JE-2025-004) − $22,070.00 vendor ACHs (JE-2025-005…009) − $59,480.00 payroll (JE-2025-010) = **$384,900.00**.

Statement, shown as arithmetic: $412,000.00 beginning + credits $54,450.00 − debits $81,550.00 = **$384,900.00** (agrees to the statement's printed totals).

### Agreement of detail
- **Cleared deposits (25, $54,450.00):** the 25 receipts in `documents/month_01/cash_receipts.csv` (Trestle Freight wire $24,000.00 on 01/15; 24 customer ACHs from $450.00 to $2,400.00, 01/20–01/26) equal the statement's 25 credits of $54,450.00 in total and in each date/amount pairing. All were recorded as JE-2025-003 and JE-2025-004.
- **Cleared disbursements (7, $81,550.00):** AWS $9,920.00 (01/05), WeWork $7,200.00 (01/06), Gusto fees $240.00 (01/07), Notion/Slack/GitHub $1,460.00 (01/08), Google Ads $3,250.00 (01/09), Gusto Net Pay $48,200.00 and Gusto Tax $11,280.00 (01/25) — each posted at its statement date (JE-2025-005…010).
- **Account 2300 (unidentified receipts):** not used; every receipt was identified and applied to an invoice (`documents/month_01/cash_receipts.csv`, policy memo §4 — `library/revenue_policy_memo.md`).

### Differences
None. There are no deposits in transit, no outstanding items, no unidentified receipts, and no bank errors reported on the statement ("no error is reported"—the statement shows none).

### Payroll tie (checklist item 4 — agree to register **and** bank)
- Register (`documents/month_01/payroll_register.json`): gross $54,404.00; net pay $48,200.00; employer taxes & benefits $5,076.00; taxes remitted $11,280.00.
- Withheld from employees: $54,404.00 − $48,200.00 = **$6,204.00**; remittance check: $6,204.00 + $5,076.00 = **$11,280.00** = register "taxes remitted" ✓.
- Bank: ACH Gusto Net Pay $48,200.00 + ACH Gusto Tax $11,280.00 = **$59,480.00** cash out = gross $54,404.00 + employer $5,076.00 paid in full on 01/25 (JE-2025-010). **No unpaid payroll liability remains at 01/31**, and nothing is forced to tie — the amounts agree independently.
