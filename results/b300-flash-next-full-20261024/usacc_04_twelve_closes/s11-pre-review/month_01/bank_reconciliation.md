# Bank reconciliation — January 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_01/bank_statement.pdf, "January 2025")
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank ending balance, 2025-01-31 (statement) | 384,900.00 |
| Book cash balance per ledger (acct 1000) | 384,900.00 |
| **Unreconciled difference** | **0.00** |

Book roll: opening 412,000.00 + receipts 54,450.00 − vendor bill payments 22,070.00 − payroll cash 59,480.00 = 384,900.00.
Bank roll: opening 412,000.00 + credits (deposits) 54,450.00 − debits (withdrawals) 81,550.00 = 384,900.00 (statement header totals verified against line items).
Bank opening 412,000.00 agrees with opening trial balance acct 1000.

## Deposits — bank 54,450.00 vs cash_receipts.csv 54,450.00 (25 items, all matched one-for-one, amounts and dates)

All 24 January monthly-subscription receipts (30,450.00) and the Trestle Freight wire of 24,000.00 (01/15) cleared the bank in January. **No deposits in transit; no unidentified receipts** (acct 2300 not needed; revenue_policy_memo #4).

| Customer | Amount | Receipt date | Bank date |
|---|---:|---|---|
| Trestle Freight LLC (wire) | 24,000.00 | 01/15 | 01/15 |
| Cedar Logistics Inc | 450.00 | 01/20 | 01/20 |
| Alder Studios Inc | 900.00 | 01/20 | 01/20 |
| Kestrel Foods Co | 650.00 | 01/20 | 01/20 |
| Ember Systems Inc | 450.00 | 01/20 | 01/20 |
| Cedar Logistics LLC | 1,800.00 | 01/21 | 01/21 |
| Ember Foods LLC | 1,800.00 | 01/21 | 01/21 |
| Ember Health Co | 2,400.00 | 01/22 | 01/22 |
| Granite Systems LLC | 1,800.00 | 01/22 | 01/22 |
| Cedar Labs LLC | 1,800.00 | 01/22 | 01/22 |
| Alder Studios LLC | 1,800.00 | 01/22 | 01/22 |
| Juniper Logistics LLC | 650.00 | 01/23 | 01/23 |
| Ember Capital Inc | 2,400.00 | 01/23 | 01/23 |
| Ember Logistics Inc | 450.00 | 01/23 | 01/23 |
| Harbor Logistics LLC | 1,200.00 | 01/23 | 01/23 |
| Cedar Studios Inc | 900.00 | 01/23 | 01/23 |
| Kestrel Systems Inc | 2,400.00 | 01/24 | 01/24 |
| Iris Health LLC | 900.00 | 01/24 | 01/24 |
| Birch Labs LLC | 2,400.00 | 01/24 | 01/24 |
| Dune Health Co | 900.00 | 01/25 | 01/25 |
| Ember Capital Co | 2,400.00 | 01/25 | 01/25 |
| Fjord Health Co | 450.00 | 01/25 | 01/25 |
| Birch Health Co | 650.00 | 01/26 | 01/26 |
| Fjord Studios Inc | 450.00 | 01/26 | 01/26 |
| Dune Foods Co | 450.00 | 01/26 | 01/26 |
| **Total** | **54,450.00** | | |

## Withdrawals — bank 81,550.00, all matched (0 unmatched items)

| Bank item | Bank | Ledger source | Ledger | Diff |
|---|---:|---|---:|---:|
| ACH AWS 01/05 | 9,920.00 | vendor_bills.csv AWS | 9,920.00 | 0 |
| ACH WEWORK 01/06 | 7,200.00 | vendor_bills.csv WeWork | 7,200.00 | 0 |
| ACH GUSTO FEES 01/07 | 240.00 | vendor_bills.csv Gusto fees | 240.00 | 0 |
| ACH NOTION/SLACK/GITHUB 01/08 | 1,460.00 | vendor_bills.csv | 1,460.00 | 0 |
| ACH GOOGLE ADS 01/09 | 3,250.00 | vendor_bills.csv Google Ads | 3,250.00 | 0 |
| ACH GUSTO NET PAY 01/25 | 48,200.00 | payroll_register.json net_pay | 48,200.00 | 0 |
| ACH GUSTO TAX 01/25 | 11,280.00 | payroll_register.json taxes_remitted | 11,280.00 | 0 |
| **Total** | **81,550.00** | | **81,550.00** | **0** |

**Outstanding checks: none** — every January bill cleared in January.

## Payroll agreement (checklist item 4 — register **and** bank)

- Register gross 54,404.00; net pay 48,200.00 → withheld from employees = 54,404.00 − 48,200.00 = **6,204.00**.
- Register taxes_remitted 11,280.00; employer taxes/benefits 5,076.00 → employee withholding implied by remittance = 11,280.00 − 5,076.00 = **6,204.00**. The two 6,204.00 figures agree, so the register is internally consistent.
- Bank: GUSTO NET PAY 48,200.00 = register net pay; GUSTO TAX 11,280.00 = register taxes_remitted. **Payroll agrees to register and bank with no forcing.** Total cash out 59,480.00 booked in JE-2025-01-08 (expense 54,404.00 + 5,076.00).

## Notes

- Statement header line extraction was re-verified line-by-line: beginning 412,000.00, deposits 54,450.00, withdrawals 81,550.00, ending 384,900.00; 412,000 + 54,450 − 81,550 = 384,900 ✓.
- The file `documents/bank_statement.csv` sitting in the workspace root is dated **December 2025** — it cannot be a January 2025 document. It was **not used** in this reconciliation; see open_items.md.
