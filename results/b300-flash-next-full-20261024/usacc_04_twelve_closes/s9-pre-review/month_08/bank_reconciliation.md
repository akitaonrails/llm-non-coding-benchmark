# Bank reconciliation — August 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_08/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 08/31/2025 (per statement) | **123,040.00** |
| Book balance, 08/31/2025 (per trial_balance.json 1000) | **123,040.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced.

## Statement integrity checks (performed line-by-line, header not trusted)

- Header values verified **by content, not by label** (April's and May's PDF text layers printed header values misaligned under the wrong captions). This month the labels align: beginning 175,330.00 (= July bank ending AND July book close ✓), total debits 82,740.00, total credits 30,450.00, ending 123,040.00. Cross-foot verified: 175,330.00 + 30,450.00 − 82,740.00 = 123,040.00 ✓.
- Transaction rows print in shifted pdftotext columns on the second page (as in prior months); debit/credit classification was therefore taken from the running-balance **delta**, not column position — every row's sign is proved by the recomputation below.
- **31/31 printed running balances equal the balances recomputed** from the 175,330.00 opening. The recomputation is the test; the printed balances are the expected values.
- 31 rows parse to 24 credits (all `ACH <CUSTOMER>` receipts, 08/20–08/26) + 7 debits (5 vendor ACHs 08/05–08/09 + payroll legs 08/25). Nothing unidentified in either direction.

## Line-by-line recomputation

Anchor: 175,330.00 (July close). Each printed balance is re-derived from the prior balance ± the row amount (sign from the delta).

| # | Date | Description | Out (debit) | In (credit) | Balance printed | Balance recomputed |
|---:|---|---|---:|---:|---:|---:|
| — | — | Beginning (July close) | | | 175,330.00 | 175,330.00 |
| 1 | 08/05 | ACH AWS | 10,760.00 | | 164,570.00 | 164,570.00 |
| 2 | 08/06 | ACH WEWORK | 7,200.00 | | 157,370.00 | 157,370.00 |
| 3 | 08/07 | ACH GUSTO FEES | 240.00 | | 157,130.00 | 157,130.00 |
| 4 | 08/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 | | 155,670.00 | 155,670.00 |
| 5 | 08/09 | ACH GOOGLE ADS | 3,600.00 | | 152,070.00 | 152,070.00 |
| 6 | 08/20 | ACH CEDAR LOGISTICS INC | | 450.00 | 152,520.00 | 152,520.00 |
| 7 | 08/20 | ACH ALDER STUDIOS INC | | 900.00 | 153,420.00 | 153,420.00 |
| 8 | 08/20 | ACH KESTREL FOODS CO | | 650.00 | 154,070.00 | 154,070.00 |
| 9 | 08/20 | ACH EMBER SYSTEMS INC | | 450.00 | 154,520.00 | 154,520.00 |
| 10 | 08/21 | ACH CEDAR LOGISTICS LLC | | 1,800.00 | 156,320.00 | 156,320.00 |
| 11 | 08/21 | ACH EMBER FOODS LLC | | 1,800.00 | 158,120.00 | 158,120.00 |
| 12 | 08/22 | ACH EMBER HEALTH CO | | 2,400.00 | 160,520.00 | 160,520.00 |
| 13 | 08/22 | ACH GRANITE SYSTEMS LLC | | 1,800.00 | 162,320.00 | 162,320.00 |
| 14 | 08/22 | ACH CEDAR LABS LLC | | 1,800.00 | 164,120.00 | 164,120.00 |
| 15 | 08/22 | ACH ALDER STUDIOS LLC | | 1,800.00 | 165,920.00 | 165,920.00 |
| 16 | 08/23 | ACH JUNIPER LOGISTICS LLC | | 650.00 | 166,570.00 | 166,570.00 |
| 17 | 08/23 | ACH EMBER CAPITAL INC | | 2,400.00 | 168,970.00 | 168,970.00 |
| 18 | 08/23 | ACH EMBER LOGISTICS INC | | 450.00 | 169,420.00 | 169,420.00 |
| 19 | 08/23 | ACH HARBOR LOGISTICS LLC | | 1,200.00 | 170,620.00 | 170,620.00 |
| 20 | 08/23 | ACH CEDAR STUDIOS INC | | 900.00 | 171,520.00 | 171,520.00 |
| 21 | 08/24 | ACH KESTREL SYSTEMS INC | | 2,400.00 | 173,920.00 | 173,920.00 |
| 22 | 08/24 | ACH IRIS HEALTH LLC | | 900.00 | 174,820.00 | 174,820.00 |
| 23 | 08/24 | ACH BIRCH LABS LLC | | 2,400.00 | 177,220.00 | 177,220.00 |
| 24 | 08/25 | ACH DUNE HEALTH CO | | 900.00 | 178,120.00 | 178,120.00 |
| 25 | 08/25 | ACH EMBER CAPITAL CO | | 2,400.00 | 180,520.00 | 180,520.00 |
| 26 | 08/25 | ACH FJORD HEALTH CO | | 450.00 | 180,970.00 | 180,970.00 |
| 27 | 08/25 | ACH GUSTO NET PAY | 48,200.00 | | 132,770.00 | 132,770.00 |
| 28 | 08/25 | ACH GUSTO TAX | 11,280.00 | | 121,490.00 | 121,490.00 |
| 29 | 08/26 | ACH BIRCH HEALTH CO | | 650.00 | 122,140.00 | 122,140.00 |
| 30 | 08/26 | ACH FJORD STUDIOS INC | | 450.00 | 122,590.00 | 122,590.00 |
| 31 | 08/26 | ACH DUNE FOODS CO | | 450.00 | 123,040.00 | 123,040.00 |
| | | **Totals** | **82,740.00** | **30,450.00** | **123,040.00** | **123,040.00** |

31/31 tie. Recomputed totals agree with the printed header: debits 82,740.00 ✓, credits 30,450.00 ✓.

## Deposits (credits) — 24 rows, 30,450.00

The 24 bank credits matched **exactly, 1:1 by payer and amount (multiset equality), to the 24 August receipts in documents/month_08/cash_receipts.csv**, which in turn matched 1:1 by customer and amount to the 24 August invoices INV-2374..INV-2397 (30,450.00). All August billings collected in-month (08/20–08/26); no opening A/R collected (open item 7).

- **Name trap checked (kept on the record every month since it first appeared):** the customer list contains deliberately confusing near-duplicates — `ALDER STUDIOS INC` (row 7, 900.00) vs `ALDER STUDIOS LLC` (row 15, 1,800.00); `CEDAR LOGISTICS INC` (row 6, 450.00) vs `CEDAR LOGISTICS LLC` (row 10, 1,800.00); `CEDAR LABS LLC` (row 14) vs `CEDAR STUDIOS INC` (row 20); `EMBER CAPITAL INC` (row 17) vs `EMBER CAPITAL CO` (row 25); `KESTREL SYSTEMS INC` (row 21) vs `KESTREL FOODS CO` (row 8); `FJORD HEALTH CO` (row 26) vs `FJORD STUDIOS INC` (row 30); `DUNE HEALTH CO` (row 24) vs `DUNE FOODS CO` (row 31); `EMBER HEALTH CO` (row 12) vs `EMBER SYSTEMS INC` / `EMBER FOODS LLC` / `EMBER LOGISTICS INC`. The payer-and-amount multiset equality proves every deposit is the right invoice payment despite the near-identical names — this month's matching is unambiguous.
- **HARBOR LOGISTICS LLC 1,200.00 (row 19)** is **customer C-017 Harbor Logistics LLC** paying its August invoice — NOT the vendor Harbor Law LLP (open item 2). Different entity, opposite direction.
- **ALDER STUDIOS LLC 1,800.00 (row 15)** is C-012's **final** subscription payment — the customer cancels effective 2025-08-31 (documents/month_08/email_cancellation_C-012.txt; open item 16). August service was performed, so the collection is earned revenue; the churn affects the September run-rate, not August revenue.

## Withdrawals (debits) — 7 rows, 82,740.00

| Bank row | Amount | Support |
|---|---:|---|
| 08/05 AWS | 10,760.00 | vendor bill 08/05 (5000 Hosting; +120.00 usage variance vs July 10,640.00) |
| 08/06 WEWORK | 7,200.00 | vendor bill 08/06 (5100 Rent, flat all year) |
| 08/07 GUSTO FEES | 240.00 | vendor bill 08/07 (5400 G&A other) |
| 08/08 NOTION/SLACK/GITHUB | 1,460.00 | vendor bill 08/08 (5200 Software) |
| 08/09 GOOGLE ADS | 3,600.00 | vendor bill 08/09 (5300 Marketing; +50.00 usage variance vs July 3,550.00) |
| 08/25 GUSTO NET PAY | 48,200.00 | payroll register net_pay (single net-pay debit — no duplicate) |
| 08/25 GUSTO TAX | 11,280.00 | payroll register taxes_remitted (6,204.00 withheld + 5,076.00 employer) |

- Bills total 23,260.00 and payroll totals 59,480.00 on both legs; 23,260.00 + 59,480.00 = 82,740.00 = total statement debits ✓. Payroll agrees to the register AND to the bank to the penny (close-checklist item 4).
- **No Harbor Law LLP debit** — and no Harbor Law bill in vendor_bills.csv (open item 2, second consecutive silent month). The only "Harbor" on the statement is the C-017 customer deposit above.
- Every debit traces to a source document; nothing unexplained.

## Cash roll-forward (book side)

175,330.00 (7/31 book = bank) + 30,450.00 receipts − 23,260.00 vendor payments − 48,200.00 net pay − 11,280.00 tax remittance = **123,040.00** = trial_balance.json 1000 = bank ending. **Difference 0.00; nothing forced.**
