# Bank reconciliation — April 2025
**Account:** Pacific Summit Bank, acct ending 5531 · **Statement period:** 2025-04-01 to 2025-04-30 · **Prepared:** controller, April close (package due 2025-05-10 per Board policy 5)

## Summary

| | Amount |
|---|---:|
| Bank statement ending balance 2025-04-30 | 233,880.00 |
| Add: deposits in transit | 0.00 |
| Less: outstanding checks/payments | 0.00 |
| Adjusted bank balance | **233,880.00** |
| General ledger cash (1000) per trial_balance.json | **233,880.00** |
| **Unreconciled difference** | **0.00** |

Beginning balance agrees to the March close (333,690.00). Statement arithmetic: 333,690.00 − total debits 130,260.00 + total credits 30,450.00 = 233,880.00 ✓ (running balance re-footed on all 32 transaction lines; final line 233,880.00 ✓). Ledger movement in 1000: +30,450.00 (JE-2025-036) − 22,580.00 (JE-2025-037) − 48,200.00 (JE-2025-038) − 11,280.00 (JE-2025-040) − 48,200.00 (JE-2025-041, disputed) = −99,810.00 net; 333,690.00 − 99,810.00 = 233,880.00 ✓. Nothing forced.

## ⚠ Important context on the nil difference (read before accepting)

The difference is nil **only because the second, disputed GUSTO NET PAY debit of 48,200.00 (04/26) was recorded in the ledger** (JE-2025-041 → Dr 1200 claim / Cr 1000). This is not a plug and nothing was forced:

- Every ledger entry above the disputed debit is register- or document-supported, and book cash before that debit was **282,080.00 = 333,690.00 + 30,450.00 − 22,580.00 − 48,200.00 − 11,280.00**, which equals the statement's own running balance on the line immediately before the disputed debit (282,080.00). The two records agree on every cent up to that line and differ only on that line.
- The office manager's note (received 2025-04-27) confirms only ONE April payroll was run and that ticket **#GS-44812** is open with Gusto support ("two net-pay debits hit our account, only one payroll was run").
- Recording the debit keeps GL cash = actual bank cash; the offset sits in **1200 Other receivables — disputed bank debits** as a claim whose **recoverability is NOT confirmed**. If Gusto/the bank deny it, it will be written off to expense with disclosure. Full analysis, rejected alternatives and the 60-day bank-notice action: open_items.md §1.

## Line-by-line match (all 32 statement transactions matched)

### Debits (8)
| Statement line | Amount | Ledger match |
|---|---:|---|
| 04/05 ACH AWS | 10,280.00 | Vendor bill AWS (JE-2025-037, acct 5300) |
| 04/06 ACH WEWORK | 7,200.00 | Vendor bill WeWork (JE-2025-037, acct 5200) |
| 04/07 ACH GUSTO FEES | 240.00 | Vendor bill Gusto platform fee (JE-2025-037, acct 5900) |
| 04/08 ACH NOTION/SLACK/GITHUB | 1,460.00 | Vendor bill software (JE-2025-037, acct 5400) |
| 04/09 ACH GOOGLE ADS | 3,400.00 | Vendor bill Google Ads (JE-2025-037, acct 5100) |
| 04/25 ACH GUSTO NET PAY | 48,200.00 | Payroll register net pay (JE-2025-038) — the ONLY April payroll |
| 04/25 ACH GUSTO TAX | 11,280.00 | Payroll tax remittance (JE-2025-040) = 6,204.00 withheld + 5,076.00 employer |
| 04/26 ACH GUSTO NET PAY | 48,200.00 | **DISPUTED duplicate — NOT payroll** (JE-2025-041, acct 1200 claim; open_items.md §1) |
| **Total debits** | **130,260.00** | agrees to statement header ✓ (22,580.00 vendors + 48,200.00 payroll + 11,280.00 tax + 48,200.00 disputed) |

### Credits (24) — every credit matched to a cash receipt dated the same day and to its April invoice
| Statement line | Amount | Receipt / invoice |
|---|---:|---|
| 04/20 ACH CEDAR LOGISTICS INC | 450.00 | INV-2291 |
| 04/20 ACH ALDER STUDIOS INC | 900.00 | INV-2293 |
| 04/20 ACH KESTREL FOODS CO | 650.00 | INV-2295 |
| 04/20 ACH EMBER SYSTEMS INC | 450.00 | INV-2298 |
| 04/21 ACH CEDAR LOGISTICS LLC | 1,800.00 | INV-2285 |
| 04/21 ACH EMBER FOODS LLC | 1,800.00 | INV-2299 |
| 04/22 ACH EMBER HEALTH CO | 2,400.00 | INV-2277 |
| 04/22 ACH GRANITE SYSTEMS LLC | 1,800.00 | INV-2279 |
| 04/22 ACH CEDAR LABS LLC | 1,800.00 | INV-2284 |
| 04/22 ACH ALDER STUDIOS LLC | 1,800.00 | INV-2287 |
| 04/23 ACH JUNIPER LOGISTICS LLC | 650.00 | INV-2283 |
| 04/23 ACH EMBER CAPITAL INC | 2,400.00 | INV-2286 |
| 04/23 ACH EMBER LOGISTICS INC | 450.00 | INV-2288 |
| 04/23 ACH HARBOR LOGISTICS LLC | 1,200.00 | INV-2292 |
| 04/23 ACH CEDAR STUDIOS INC | 900.00 | INV-2296 |
| 04/24 ACH KESTREL SYSTEMS INC | 2,400.00 | INV-2278 |
| 04/24 ACH IRIS HEALTH LLC | 900.00 | INV-2280 |
| 04/24 ACH BIRCH LABS LLC | 2,400.00 | INV-2281 |
| 04/25 ACH DUNE HEALTH CO | 900.00 | INV-2289 |
| 04/25 ACH EMBER CAPITAL CO | 2,400.00 | INV-2294 |
| 04/25 ACH FJORD HEALTH CO | 450.00 | INV-2297 |
| 04/26 ACH BIRCH HEALTH CO | 650.00 | INV-2276 |
| 04/26 ACH FJORD STUDIOS INC | 450.00 | INV-2282 |
| 04/26 ACH DUNE FOODS CO | 450.00 | INV-2290 |
| **Total credits** | **30,450.00** | agrees to statement header and to cash_receipts.csv total ✓ (24 receipts = 24 invoices INV-2276..2299) |

## Differences and observations
- **Unreconciled difference: 0.00**, subject to the disputed-debit caveat above (the 48,200.00 is a recorded, documented outflow with an open claim — not a timing difference; it will NOT self-clear next month).
- No deposits in transit, no outstanding items at 2025-04-30: all 24 receipts land 04/20–04/26; all vendor bills paid same-day as billing; payroll/tax on register date 04/25.
- Payroll agrees to **both** the register and the bank (checklist item 4) — for the single register run: gross 54,404.00 / net 48,200.00 ↔ GUSTO NET PAY 48,200.00 (04/25); withholding 6,204.00 + employer 5,076.00 = 11,280.00 ↔ GUSTO TAX 11,280.00. The bank shows one MORE net-pay debit than the register supports — that is the open item, not a matching failure. Recommended additional safeguard (open_items.md §1): confirm with employees that no employee received two net-pay deposits in April.
- No bank activity touched the opening A/P 17,420.00 (acct 2000, now 4th month unpaid) or the 2024-vintage A/R 38,200.00 (acct 1100, now 4th month with zero collections): no debit matches an opening payable, and every credit is matched to a 2025 invoice. Escalated in open_items.md §5.
- Cash bridge (why cash fell 99,810.00 while the net loss was only 38,687.78): net loss (38,687.78) + non-cash depreciation 1,777.78 = operating cash outflow (36,910.00); minus deferred-revenue releases recognized without April cash (14,700.00) = (51,610.00); minus the disputed outflow (48,200.00, non-P&L) = **(99,810.00)** = 233,880.00 − 333,690.00 ✓. A/R and A/P balances were unchanged month to month.
