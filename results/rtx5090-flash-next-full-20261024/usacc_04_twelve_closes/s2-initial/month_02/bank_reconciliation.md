# Bank reconciliation — February 2025
**Account:** Pacific Summit Bank, acct ending 5531 · **Statement period:** 2025-02-01 to 2025-02-28 · **Prepared:** controller, February close (package due 2025-03-10 per Board policy 5)

## Summary

| | Amount |
|---|---:|
| Bank statement ending balance 2025-02-28 | 369,630.00 |
| Add: deposits in transit | 0.00 |
| Less: outstanding checks/payments | 0.00 |
| Adjusted bank balance | **369,630.00** |
| General ledger cash (1000) per trial_balance.json | **369,630.00** |
| **Unreconciled difference** | **0.00** |

Beginning balance agrees to the January close (384,900.00). Statement arithmetic: 384,900.00 − total debits 81,720.00 + total credits 66,450.00 = 369,630.00 ✓. Ledger movement: +66,450.00 (JE-2025-014) − 22,240.00 (JE-2025-015) − 48,200.00 (JE-2025-016) − 11,280.00 (JE-2025-018) = −15,270.00; 384,900.00 − 15,270.00 = 369,630.00 ✓. Nothing forced.

## Line-by-line match (all 32 statement transactions matched)

### Debits (7)
| Statement line | Amount | Ledger match |
|---|---:|---|
| 02/05 ACH AWS | 10,040.00 | Vendor bill 2025-02-05 AWS 10,040.00 → JE-2025-015 (5300) |
| 02/06 ACH WEWORK | 7,200.00 | Vendor bill 2025-02-06 WeWork 7,200.00 → JE-2025-015 (5200) |
| 02/07 ACH GUSTO FEES | 240.00 | Vendor bill 2025-02-07 Gusto fees 240.00 → JE-2025-015 (5900) |
| 02/08 ACH NOTION/SLACK/GITHUB | 1,460.00 | Vendor bill 2025-02-08 1,460.00 → JE-2025-015 (5400) |
| 02/09 ACH GOOGLE ADS | 3,300.00 | Vendor bill 2025-02-09 Google Ads 3,300.00 → JE-2025-015 (5100) |
| 02/25 ACH GUSTO NET PAY | 48,200.00 | Payroll register net pay 48,200.00 → JE-2025-016 |
| 02/25 ACH GUSTO TAX | 11,280.00 | Register taxes_remitted 11,280.00 → JE-2025-018 |

Debits total: 10,040 + 7,200 + 240 + 1,460 + 3,300 + 48,200 + 11,280 = **81,720.00** = statement total ✓

### Credits (25)
Every bank credit matches one cash_receipts.csv row (dates and amounts identical) and one open February invoice:

| Invoice | Amount | Receipt / bank date | Customer |
|---|---:|---|---|
| INV-2250 | 36,000.00 | 02/15 | Pinecone Dental Group (WIRE IN) |
| INV-2241 | 450.00 | 02/20 | Cedar Logistics Inc |
| INV-2243 | 900.00 | 02/20 | Alder Studios Inc |
| INV-2245 | 650.00 | 02/20 | Kestrel Foods Co |
| INV-2248 | 450.00 | 02/20 | Ember Systems Inc |
| INV-2235 | 1,800.00 | 02/21 | Cedar Logistics LLC |
| INV-2249 | 1,800.00 | 02/21 | Ember Foods LLC |
| INV-2227 | 2,400.00 | 02/22 | Ember Health Co |
| INV-2229 | 1,800.00 | 02/22 | Granite Systems LLC |
| INV-2234 | 1,800.00 | 02/22 | Cedar Labs LLC |
| INV-2237 | 1,800.00 | 02/22 | Alder Studios LLC |
| INV-2233 | 650.00 | 02/23 | Juniper Logistics LLC |
| INV-2236 | 2,400.00 | 02/23 | Ember Capital Inc |
| INV-2238 | 450.00 | 02/23 | Ember Logistics Inc |
| INV-2242 | 1,200.00 | 02/23 | Harbor Logistics LLC |
| INV-2246 | 900.00 | 02/23 | Cedar Studios Inc |
| INV-2228 | 2,400.00 | 02/24 | Kestrel Systems Inc |
| INV-2230 | 900.00 | 02/24 | Iris Health LLC |
| INV-2231 | 2,400.00 | 02/24 | Birch Labs LLC |
| INV-2239 | 900.00 | 02/25 | Dune Health Co |
| INV-2244 | 2,400.00 | 02/25 | Ember Capital Co |
| INV-2247 | 450.00 | 02/25 | Fjord Health Co |
| INV-2226 | 650.00 | 02/26 | Birch Health Co |
| INV-2232 | 450.00 | 02/26 | Fjord Studios Inc |
| INV-2240 | 450.00 | 02/26 | Dune Foods Co |

Credits total: 36,000.00 + 30,450.00 (24 monthly invoices) = **66,450.00** = statement total ✓

## Items noted (no reconciling difference)
- **No bank debits against opening A/P (2000, 17,420.00)** — the opening payable remains unpaid through February; aging concern raised in open_items.md.
- **No bank credits against the restated opening A/R (1100, 38,200.00)** — none of the 2024-vintage receivable has been collected by 28-Feb; see open_items.md.
- No bank fees, interest, FX or unknown items on the statement; no unidentified receipts, so account 2300 (Board policy 4) was not used.
- Payroll agrees to the register **and** the bank (checklist item 4): gross 54,404.00 + employer 5,076.00 = 59,480.00 expense; cash out 48,200.00 + 11,280.00 = 59,480.00. Withholding identity: 54,404.00 − 48,200.00 = 6,204.00; 6,204.00 + 5,076.00 = 11,280.00 remitted ✓; 2100 clears to zero.
- December-2025 stray file `documents/bank_statement.csv` remains unused and out of period (reserved for the month_12 close).
