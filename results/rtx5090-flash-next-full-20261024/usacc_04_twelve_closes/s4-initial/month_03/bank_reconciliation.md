# Bank reconciliation — March 2025
**Account:** Pacific Summit Bank, acct ending 5531 · **Statement period:** 2025-03-01 to 2025-03-31 · **Prepared:** controller, March close (package due 2025-04-10 per Board policy 5)

## Summary

| | Amount |
|---|---:|
| Bank statement ending balance 2025-03-31 | 333,690.00 |
| Add: deposits in transit | 0.00 |
| Less: outstanding checks/payments | 0.00 |
| Adjusted bank balance | **333,690.00** |
| General ledger cash (1000) per trial_balance.json | **333,690.00** |
| **Unreconciled difference** | **0.00** |

Beginning balance agrees to the February close (369,630.00). Statement arithmetic: 369,630.00 − total debits 84,390.00 + total credits 48,450.00 = 333,690.00 ✓ (running balance on every statement line was re-footed; final line 333,690.00 ✓). Ledger movement in 1000: +48,450.00 (JE-2025-025) − 24,910.00 (JE-2025-026) − 48,200.00 (JE-2025-027) − 11,280.00 (JE-2025-029) = −35,940.00 net; 369,630.00 − 35,940.00 = 333,690.00 ✓. Nothing forced.

## Line-by-line match (all 33 statement transactions matched)

### Debits (8)
| Statement line | Amount | Ledger match |
|---|---:|---|
| 03/05 ACH AWS | 10,160.00 | Vendor bill 2025-03-05 AWS (JE-2025-026, acct 5300) |
| 03/06 ACH WEWORK | 7,200.00 | Vendor bill 2025-03-06 WeWork (JE-2025-026, acct 5200) |
| 03/07 ACH GUSTO FEES | 240.00 | Vendor bill 2025-03-07 Gusto platform fee (JE-2025-026, acct 5900) |
| 03/08 ACH NOTION/SLACK/GITHUB | 1,460.00 | Vendor bill 2025-03-08 software (JE-2025-026, acct 5400) |
| 03/09 ACH HARBOR LAW LLP | 2,500.00 | Vendor bill 2025-03-09 Harbor Law LLP (JE-2025-026, acct 5600 — new professional-fees account, open_items.md §3) |
| 03/10 ACH GOOGLE ADS | 3,350.00 | Vendor bill 2025-03-10 Google Ads (JE-2025-026, acct 5100) |
| 03/25 ACH GUSTO NET PAY | 48,200.00 | Payroll register net pay (JE-2025-027) |
| 03/25 ACH GUSTO TAX | 11,280.00 | Payroll tax remittance (JE-2025-029) = 6,204.00 withheld + 5,076.00 employer |
| **Total debits** | **84,390.00** | agrees to statement header ✓ |

### Credits (25) — every credit matched to a cash receipt dated the same day and to its March invoice
| Statement line | Amount | Receipt / invoice |
|---|---:|---|
| 03/15 WIRE IN MARIGOLD SCHOOLS INC | 18,000.00 | Marigold Schools Inc (C-027), INV-2275 annual |
| 03/20 ACH CEDAR LOGISTICS INC | 450.00 | INV-2266 |
| 03/20 ACH ALDER STUDIOS INC | 900.00 | INV-2268 |
| 03/20 ACH KESTREL FOODS CO | 650.00 | INV-2270 |
| 03/20 ACH EMBER SYSTEMS INC | 450.00 | INV-2273 |
| 03/21 ACH CEDAR LOGISTICS LLC | 1,800.00 | INV-2260 |
| 03/21 ACH EMBER FOODS LLC | 1,800.00 | INV-2274 |
| 03/22 ACH EMBER HEALTH CO | 2,400.00 | INV-2252 |
| 03/22 ACH GRANITE SYSTEMS LLC | 1,800.00 | INV-2254 |
| 03/22 ACH CEDAR LABS LLC | 1,800.00 | INV-2259 |
| 03/22 ACH ALDER STUDIOS LLC | 1,800.00 | INV-2262 |
| 03/23 ACH JUNIPER LOGISTICS LLC | 650.00 | INV-2258 |
| 03/23 ACH EMBER CAPITAL INC | 2,400.00 | INV-2261 |
| 03/23 ACH EMBER LOGISTICS INC | 450.00 | INV-2263 |
| 03/23 ACH HARBOR LOGISTICS LLC | 1,200.00 | INV-2267 |
| 03/23 ACH CEDAR STUDIOS INC | 900.00 | INV-2271 |
| 03/24 ACH KESTREL SYSTEMS INC | 2,400.00 | INV-2253 |
| 03/24 ACH IRIS HEALTH LLC | 900.00 | INV-2255 |
| 03/24 ACH BIRCH LABS LLC | 2,400.00 | INV-2256 |
| 03/25 ACH DUNE HEALTH CO | 900.00 | INV-2264 |
| 03/25 ACH EMBER CAPITAL CO | 2,400.00 | INV-2269 |
| 03/25 ACH FJORD HEALTH CO | 450.00 | INV-2272 |
| 03/26 ACH BIRCH HEALTH CO | 650.00 | INV-2251 |
| 03/26 ACH FJORD STUDIOS INC | 450.00 | INV-2257 |
| 03/26 ACH DUNE FOODS CO | 450.00 | INV-2265 |
| **Total credits** | **48,450.00** | agrees to statement header and to cash_receipts.csv total (30,450.00 monthly + 18,000.00 Marigold) ✓ |

## Differences and observations
- **Unreconciled difference: 0.00.** No deposits in transit, no outstanding items at 2025-03-31 (all 25 receipts land 03/15–03/26; all vendor bills paid same-day-to-day-after billing; payroll/tax on register date 03/25).
- No bank activity touched the opening A/P 17,420.00 (acct 2000) or the 2024-vintage A/R 38,200.00 (acct 1100): no debit matches an opening payable, and every credit above is matched to a 2025 invoice. Both items age into their third month — escalated in open_items.md §5.
- Payroll agrees to **both** the register and the bank (checklist item 4): gross 54,404.00 / net 48,200.00 ↔ GUSTO NET PAY 48,200.00; withholding + employer 11,280.00 ↔ GUSTO TAX 11,280.00.
- Note (disclosure-history correction): prior months' narrative about the Pinecone deferred-revenue release schedule contained an arithmetic error (the "24,000.00 in 2026" figure); it never affected any bank, ledger or roll-forward balance. Full correction at open_items.md §0.
