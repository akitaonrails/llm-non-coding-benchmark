# Bank reconciliation — January 2025

**Account:** Pacific Summit Bank, operating account ending **5531**
**Statement period:** 2025-01-01 to 2025-01-31 (`documents/month_01/bank_statement.pdf`)

## Summary

| | Amount |
|---|---:|
| Bank — beginning balance (per statement) | 412,000.00 |
| Bank credits (deposits) | +54,450.00 |
| Bank debits (withdrawals) | −81,550.00 |
| **Bank — ending balance 2025-01-31** | **384,900.00** |
| | |
| Books (GL 1000) — beginning balance | 412,000.00 |
| Cash receipts JE-2025-004 | +54,450.00 |
| Vendor bill payments JE-2025-005 | −22,070.00 |
| Payroll net JE-2025-006 | −48,200.00 |
| Payroll tax remittance JE-2025-008 | −11,280.00 |
| **Books — ending balance 2025-01-31** | **384,900.00** |
| | |
| **Unreconciled difference** | **0.00** |

Arithmetic: 412,000.00 + 54,450.00 − 81,550.00 = 384,900.00 (statement internally consistent: credits 54,450.00 = 24,000.00 + 30,450.00; debits 81,550.00 = 9,920.00 + 7,200.00 + 240.00 + 1,460.00 + 3,250.00 + 48,200.00 + 11,280.00).
Books: 412,000.00 + 54,450.00 − 22,070.00 − 48,200.00 − 11,280.00 = 384,900.00.

Opening book cash (opening trial balance 1000) equals the statement opening balance — beginning balance verified.

## Line-by-line matching

### Deposits (bank credits) — 25 items, all matched to `cash_receipts.csv`
| Bank | Books | Match |
|---|---|---|
| 01/15 WIRE IN TRESTLE FREIGHT LLC 24,000.00 | Receipt 2025-01-15, INV-2225 | ✓ |
| 01/20 CEDAR LOGISTICS INC 450.00 | 01-20, INV-2216 | ✓ |
| 01/20 ALDER STUDIOS INC 900.00 | 01-20, INV-2218 | ✓ |
| 01/20 KESTREL FOODS CO 650.00 | 01-20, INV-2220 | ✓ |
| 01/20 EMBER SYSTEMS INC 450.00 | 01-20, INV-2223 | ✓ |
| 01/21 CEDAR LOGISTICS LLC 1,800.00 | 01-21, INV-2210 | ✓ |
| 01/21 EMBER FOODS LLC 1,800.00 | 01-21, INV-2224 | ✓ |
| 01/22 EMBER HEALTH CO 2,400.00 | 01-22, INV-2202 | ✓ |
| 01/22 GRANITE SYSTEMS LLC 1,800.00 | 01-22, INV-2204 | ✓ |
| 01/22 CEDAR LABS LLC 1,800.00 | 01-22, INV-2209 | ✓ |
| 01/22 ALDER STUDIOS LLC 1,800.00 | 01-22, INV-2212 | ✓ |
| 01/23 JUNIPER LOGISTICS LLC 650.00 | 01-23, INV-2208 | ✓ |
| 01/23 EMBER CAPITAL INC 2,400.00 | 01-23, INV-2211 | ✓ |
| 01/23 EMBER LOGISTICS INC 450.00 | 01-23, INV-2213 | ✓ |
| 01/23 HARBOR LOGISTICS LLC 1,200.00 | 01-23, INV-2217 | ✓ |
| 01/23 CEDAR STUDIOS INC 900.00 | 01-23, INV-2221 | ✓ |
| 01/24 KESTREL SYSTEMS INC 2,400.00 | 01-24, INV-2203 | ✓ |
| 01/24 IRIS HEALTH LLC 900.00 | 01-24, INV-2205 | ✓ |
| 01/24 BIRCH LABS LLC 2,400.00 | 01-24, INV-2206 | ✓ |
| 01/25 DUNE HEALTH CO 900.00 | 01-25, INV-2214 | ✓ |
| 01/25 EMBER CAPITAL CO 2,400.00 | 01-25, INV-2219 | ✓ |
| 01/25 FJORD HEALTH CO 450.00 | 01-25, INV-2222 | ✓ |
| 01/26 BIRCH HEALTH CO 650.00 | 01-26, INV-2201 | ✓ |
| 01/26 FJORD STUDIOS INC 450.00 | 01-26, INV-2207 | ✓ |
| 01/26 DUNE FOODS CO 450.00 | 01-26, INV-2215 | ✓ |

Every January receipt cleared in January; same dates in both records. No deposits in transit; no unidentified receipts (account 2300 remains unused; per Board policy 4 it would hold unmatched receipts).

### Withdrawals (bank debits) — 7 items, all matched to books
| Bank | Books | Match |
|---|---|---|
| 01/05 ACH AWS 9,920.00 | Vendor bill AWS (JE-2025-005) | ✓ |
| 01/06 ACH WEWORK 7,200.00 | Vendor bill WeWork (JE-2025-005) | ✓ |
| 01/07 ACH GUSTO FEES 240.00 | Vendor bill Gusto fees (JE-2025-005) | ✓ |
| 01/08 ACH NOTION/SLACK/GITHUB 1,460.00 | Vendor bill (JE-2025-005) | ✓ |
| 01/09 ACH GOOGLE ADS 3,250.00 | Vendor bill (JE-2025-005) | ✓ |
| 01/25 ACH GUSTO NET PAY 48,200.00 | Payroll register net pay (JE-2025-006) | ✓ |
| 01/25 ACH GUSTO TAX 11,280.00 | Register taxes_remitted 11,280.00 = withholding 6,204.00 (54,404.00 gross − 48,200.00 net) + employer 5,076.00 (JE-2025-008) | ✓ |

## Payroll agreement (close checklist item 4)
Register ↔ bank: net 48,200.00 = bank NET PAY; remitted 11,280.00 = bank TAX; internal check 54,404.00 − 48,200.00 + 5,076.00 = 11,280.00. **Payroll agrees to the register and the bank; nothing forced.**

## Differences and observations
1. **Unreconciled difference: none (0.00).** No outstanding checks, no deposits in transit, no bank fees beyond Gusto fees (recorded), no interest noted.
2. **Note (not a reconciling item):** opening A/R of 92,650.00 was overstated by 54,450.00 due to a Dec-2024 posting error; corrected 2025-01-01 via JE-2025-001 (A/R credit, not cash — no effect on this reconciliation). See `open_items.md`.
3. The statement carries the bank's 60-day error-reporting clause; this reconciliation was prepared 2025-01-31 and shows no statement error.
