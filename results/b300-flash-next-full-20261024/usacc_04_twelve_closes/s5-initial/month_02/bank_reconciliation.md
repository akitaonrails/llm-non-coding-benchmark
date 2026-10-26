# Bank reconciliation — February 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_02/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 02/28/2025 (per statement) | **369,630.00** |
| Book balance, 02/28/2025 (per trial_balance.json 1000) | **369,630.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced.

## Statement integrity checks (performed line-by-line, header not trusted)

- Statement header: beginning 384,900.00 / total debits 81,720.00 / total credits 66,450.00 / ending 369,630.00. Verified: 384,900.00 + 66,450.00 − 81,720.00 = 369,630.00 ✓.
- All 32 transaction running balances recomputed from beginning 384,900.00 — every printed balance agrees to the recomputation ✓ (including the 02/15 wire 36,000.00 → 398,660.00 and the 02/25 payroll pair → 379,360.00 → 368,080.00).
- Beginning balance 384,900.00 = January closing bank AND January book cash ✓ (no reconciling items carried in from month_01).

## Deposits — 25 items, 66,450.00, all matched

| Bank (date, amount) | Source | Applied to |
|---|---|---|
| 02/15 wire Pinecone Dental Group 36,000.00 | cash_receipts.csv 2025-02-15 | INV-2250 (collected contract liability — NOT revenue, see JE-2025-02-02/05) |
| 24 ACH deposits 02/20–02/26 totaling 30,450.00 | cash_receipts.csv rows 2–25 | INV-2226…INV-2249, each matched customer + amount + date |

Bank deposit multiset (date, amount) equals the cash-receipts file exactly (verified programmatically). Receipts 66,450.00 = invoices 30,450.00 + 36,000.00 ✓.

## Withdrawals — 7 items, 81,720.00, all matched

| Bank (date) | Item | Amount | Agrees to |
|---|---|---:|---|
| 02/05 | ACH AWS | 10,040.00 | vendor_bills.csv 02/05 |
| 02/06 | ACH WeWork | 7,200.00 | vendor_bills.csv 02/06 |
| 02/07 | ACH Gusto fees | 240.00 | vendor_bills.csv 02/07 |
| 02/08 | ACH Notion/Slack/GitHub | 1,460.00 | vendor_bills.csv 02/08 |
| 02/09 | ACH Google Ads | 3,300.00 | vendor_bills.csv 02/09 |
| 02/25 | ACH Gusto net pay | 48,200.00 | payroll_register net_pay 48,200.00 |
| 02/25 | ACH Gusto tax | 11,280.00 | payroll_register taxes_remitted 11,280.00 |

Vendor payments total 22,240.00 = vendor bills total ✓. Payroll: register gross 54,404.00 − net 48,200.00 = 6,204.00 withheld; 6,204.00 + employer 5,076.00 = 11,280.00 remitted — register agrees to bank exactly (checklist item 4 satisfied: agreed to register **and** bank).

## Cash roll-forward proof

Book: 384,900.00 + 66,450.00 (receipts) − 22,240.00 (bills) − 59,480.00 (payroll: 48,200.00 + 11,280.00) = **369,630.00** = bank ending ✓.

## Differences

None. Every deposit and withdrawal on the statement is explained; every book cash movement appears on the statement. Note the misfiled December-2025 `documents/bank_statement.csv` was not used (carried flag from month_01 open_items.md item 7).
