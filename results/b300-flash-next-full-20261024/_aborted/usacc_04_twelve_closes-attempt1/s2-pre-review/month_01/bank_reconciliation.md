# Bank Reconciliation — January 2025

**Account:** 1000 Cash — Operating · **Bank:** Pacific Summit Bank, acct ending 5531
**Statement period:** January 2025 (source: `documents/month_01/bank_statement.pdf`, text extracted with `pdftotext`)
**Prepared:** 2025-02 close (controller) · Closes per close checklist item 5 (`library/close_checklist.md`)

## 1. Balance summary

| | Bank statement | Company books |
|---|---:|---:|
| Balance 12/31/2024 / 01/01/2025 | 412,000.00 | 412,000.00 |
| (+) Deposits / credits | 54,450.00 | 54,450.00 |
| (−) Payments / debits | 81,550.00 | 81,550.00 |
| **Balance 01/31/2025** | **384,900.00** | **384,900.00** |

Arithmetic: bank 412,000.00 − 81,550.00 + 54,450.00 = 384,900.00 (agrees to statement ending balance and to the statement's own summary line: debits 81,550.00, credits 54,450.00).
Books: 412,000.00 (opening TB) + 54,450.00 (JE-2025-01-03 receipts) − 22,070.00 (JE-2025-01-05 vendor payments) − 59,480.00 (JE-2025-01-06 payroll 48,200.00 net + 11,280.00 tax) = 384,900.00.

## 2. Standard reconciliation form

| Line | Amount |
|---|---:|
| Balance per bank statement, 01/31/2025 | 384,900.00 |
| Add: deposits in transit | 0.00 |
| Less: outstanding checks / unpaid ACH | 0.00 |
| Add/less: bank fees, interest, adjustments not on books | 0.00 |
| **Adjusted bank balance** | **384,900.00** |
| Balance per books (account 1000), 01/31/2025 | 384,900.00 |
| Add/less: items on bank not yet on books | 0.00 |
| Corrections / reclassifications | 0.00 |
| **Adjusted book balance** | **384,900.00** |
| **Difference** | **0.00** |

**Every difference documented:** there are none. All 32 bank transactions matched a book item line-for-line; no unmatched bank item and no unmatched book item remains.

## 3. Line-for-line matching (32 of 32 transactions matched)

**Debits — 5 vendor ACHs tie to `vendor_bills.csv` (JE-2025-01-04/05); 2 payroll ACHs tie to `payroll_register.json` (JE-2025-01-06):**

| Bank date | Bank item | Bank amt | Book source |
|---|---|---:|---|
| 01/05 | ACH AWS | 9,920.00 | Bill AWS 9,920.00 ✓ |
| 01/06 | ACH WEWORK | 7,200.00 | Bill WeWork 7,200.00 ✓ |
| 01/07 | ACH GUSTO FEES | 240.00 | Bill Gusto fees 240.00 ✓ |
| 01/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 | Bill Notion/Slack/GitHub 1,460.00 ✓ |
| 01/09 | ACH GOOGLE ADS | 3,250.00 | Bill Google Ads 3,250.00 ✓ |
| 01/25 | ACH GUSTO NET PAY | 48,200.00 | Register net_pay 48,200.00 ✓ |
| 01/25 | ACH GUSTO TAX | 11,280.00 | Register taxes_remitted 11,280.00 ✓ |
| | **Total debits** | **81,550.00** | |

**Credits — all 25 customer receipts in `cash_receipts.csv` appear on the bank, same customer, amount, and date; none missing, none extra** (Trestle wire 24,000.00 on 01/15 plus 24 monthly ACH receipts of 24 customers, 01/20–01/26). Total credits 54,450.00 = receipts total 54,450.00. Verified programmatically by normalized name+amount matching, including the near-identical pairs (Alder Studios Inc 900 / LLC 1,800; Cedar Logistics Inc 450 / LLC 1,800; Ember Foods/Capital/Health/Logistics/Systems; Dune Health/Foods; Kestrel Systems/Foods; Fjord Health/Studios).

## 4. Payroll three-way tie (close checklist item 4)

- Register ↔ bank: net 48,200.00 = GUSTO NET PAY ✓; remitted 11,280.00 = GUSTO TAX ✓.
- Register internal: withheld = gross − net = 54,404.00 − 48,200.00 = 6,204.00; 6,204.00 + employer 5,076.00 = 11,280.00 remitted ✓ (no payroll liability left at month-end).
- Total January cash out for payroll 48,200.00 + 11,280.00 = 59,480.00 = expense 54,404.00 + 5,076.00 ✓. Nothing forced.

## 5. Notes

- Opening book cash (412,000.00 from `documents/opening_trial_balance.csv`) equals the bank beginning balance — no prior-period timing items carried into January.
- The file `documents/bank_statement.csv` (sitting at the documents root) contains only **December 2025-dated** transactions on a **negative** balance and cannot be a January 2025 statement for this account; it was **not** used. See `open_items.md` item 6 / QUESTIONS.md Q7.
- No bank fees, interest, or bank-originated adjustments appear in January.
