# Bank reconciliation — June 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_06/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 06/30/2025 (per statement) | **227,450.00** |
| Book balance, 06/30/2025 (per trial_balance.json 1000) | **227,450.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced. April's duplicate net-pay debit (item 12) was refunded in May and closed then; it did not recur in June — the statement shows a single `ACH GUSTO NET PAY 48,200.00`.

## Statement integrity checks (performed line-by-line, header not trusted)

- Header values were again verified **by content, not by label** because April's and May's PDF text layers printed the header values misaligned under the wrong captions. This month the labels happen to align: beginning 260,300.00 (= May bank ending AND May book close ✓), total debits 84,900.00, total credits 52,050.00, ending 227,450.00. Cross-foot verified: 260,300.00 + 52,050.00 − 84,900.00 = 227,450.00 ✓.
- No repeated column caption mid-page this month (unlike April and May): the page break after the 06/24 Birch Labs row prints only a bare page number, and page 2 continues directly with the 06/25 transactions. Transaction rows print in slightly shifted columns on page 2; debit/credit classification was therefore taken from column geometry anchored on page 1 and then **confirmed by content** — every row's sign is proved by the running-balance recomputation below (a misclassified row would break the recomputation).
- All 33 transaction running balances recomputed independently from beginning 260,300.00: **33 of 33 printed balances agree to the recomputation** — a fully clean statement (every row prints its balance; no displaced amounts). Recomputed ending 227,450.00 = printed ending ✓. Transaction count: 33 (8 withdrawals + 25 deposits). Full table below.

## Full transaction ledger — recomputation vs printed balances

Recomputed cash roll starts at 260,300.00. "Printed" = balance as printed on the statement; "Recomputed" = independent recalculation.

| Date | Description | Out (debit) | In (credit) | Printed bal | Recomputed bal | Tie |
|---|---|---:|---:|---:|---:|---|
| 06/05/2025 | ACH AWS | 10,520.00 |  | 249,780.00 | 249,780.00 | ✓ |
| 06/06/2025 | ACH WEWORK | 7,200.00 |  | 242,580.00 | 242,580.00 | ✓ |
| 06/07/2025 | ACH GUSTO FEES | 240.00 |  | 242,340.00 | 242,340.00 | ✓ |
| 06/08/2025 | ACH NOTION/SLACK/GITHUB | 1,460.00 |  | 240,880.00 | 240,880.00 | ✓ |
| 06/09/2025 | ACH HARBOR LAW LLP | 2,500.00 |  | 238,380.00 | 238,380.00 | ✓ |
| 06/10/2025 | ACH GOOGLE ADS | 3,500.00 |  | 234,880.00 | 234,880.00 | ✓ |
| 06/15/2025 | WIRE IN SALTLINE HOSPITALITY |  | 21,600.00 | 256,480.00 | 256,480.00 | ✓ |
| 06/20/2025 | ACH CEDAR LOGISTICS INC |  | 450.00 | 256,930.00 | 256,930.00 | ✓ |
| 06/20/2025 | ACH ALDER STUDIOS INC |  | 900.00 | 257,830.00 | 257,830.00 | ✓ |
| 06/20/2025 | ACH KESTREL FOODS CO |  | 650.00 | 258,480.00 | 258,480.00 | ✓ |
| 06/20/2025 | ACH EMBER SYSTEMS INC |  | 450.00 | 258,930.00 | 258,930.00 | ✓ |
| 06/21/2025 | ACH CEDAR LOGISTICS LLC |  | 1,800.00 | 260,730.00 | 260,730.00 | ✓ |
| 06/21/2025 | ACH EMBER FOODS LLC |  | 1,800.00 | 262,530.00 | 262,530.00 | ✓ |
| 06/22/2025 | ACH EMBER HEALTH CO |  | 2,400.00 | 264,930.00 | 264,930.00 | ✓ |
| 06/22/2025 | ACH GRANITE SYSTEMS LLC |  | 1,800.00 | 266,730.00 | 266,730.00 | ✓ |
| 06/22/2025 | ACH CEDAR LABS LLC |  | 1,800.00 | 268,530.00 | 268,530.00 | ✓ |
| 06/22/2025 | ACH ALDER STUDIOS LLC |  | 1,800.00 | 270,330.00 | 270,330.00 | ✓ |
| 06/23/2025 | ACH JUNIPER LOGISTICS LLC |  | 650.00 | 270,980.00 | 270,980.00 | ✓ |
| 06/23/2025 | ACH EMBER CAPITAL INC |  | 2,400.00 | 273,380.00 | 273,380.00 | ✓ |
| 06/23/2025 | ACH EMBER LOGISTICS INC |  | 450.00 | 273,830.00 | 273,830.00 | ✓ |
| 06/23/2025 | ACH HARBOR LOGISTICS LLC |  | 1,200.00 | 275,030.00 | 275,030.00 | ✓ |
| 06/23/2025 | ACH CEDAR STUDIOS INC |  | 900.00 | 275,930.00 | 275,930.00 | ✓ |
| 06/24/2025 | ACH KESTREL SYSTEMS INC |  | 2,400.00 | 278,330.00 | 278,330.00 | ✓ |
| 06/24/2025 | ACH IRIS HEALTH LLC |  | 900.00 | 279,230.00 | 279,230.00 | ✓ |
| 06/24/2025 | ACH BIRCH LABS LLC |  | 2,400.00 | 281,630.00 | 281,630.00 | ✓ |
| 06/25/2025 | ACH DUNE HEALTH CO |  | 900.00 | 282,530.00 | 282,530.00 | ✓ |
| 06/25/2025 | ACH EMBER CAPITAL CO |  | 2,400.00 | 284,930.00 | 284,930.00 | ✓ |
| 06/25/2025 | ACH FJORD HEALTH CO |  | 450.00 | 285,380.00 | 285,380.00 | ✓ |
| 06/25/2025 | ACH GUSTO NET PAY | 48,200.00 |  | 237,180.00 | 237,180.00 | ✓ |
| 06/25/2025 | ACH GUSTO TAX | 11,280.00 |  | 225,900.00 | 225,900.00 | ✓ |
| 06/26/2025 | ACH BIRCH HEALTH CO |  | 650.00 | 226,550.00 | 226,550.00 | ✓ |
| 06/26/2025 | ACH FJORD STUDIOS INC |  | 450.00 | 227,000.00 | 227,000.00 | ✓ |
| 06/26/2025 | ACH DUNE FOODS CO |  | 450.00 | 227,450.00 | 227,450.00 | ✓ |

## Deposits — 25 items, 52,050.00, all matched

25 customer deposits (06/15–06/26) equal cash_receipts.csv row-for-row — the bank multiset (date, payer, amount) equals the receipts file exactly, and every receipt matches its invoice by customer + amount (verified programmatically): 24 recurring invoices 30,450.00 collected in-month (ACH 06/20–06/26) plus Saltline Hospitality 21,600.00 wire 06/15 (INV-2349). No opening A/R was collected (open_items.md item 7). **Zero deposits in transit at 06/30.**

## Withdrawals — 8 items, 84,900.00, all supported

| Bank (date) | Item | Amount | Agrees to |
|---|---|---:|---|
| 06/05 | ACH AWS | 10,520.00 | vendor_bills.csv AWS 10,520.00 |
| 06/06 | ACH WeWork | 7,200.00 | vendor_bills.csv WeWork 7,200.00 |
| 06/07 | ACH Gusto fees | 240.00 | vendor_bills.csv Gusto fees 240.00 |
| 06/08 | ACH Notion/Slack/GitHub | 1,460.00 | vendor_bills.csv 1,460.00 |
| 06/09 | ACH Harbor Law LLP | 2,500.00 | vendor_bills.csv Harbor Law LLP 2,500.00 (second month in a row — open item 2) |
| 06/10 | ACH Google Ads | 3,500.00 | vendor_bills.csv Google Ads 3,500.00 |
| 06/25 | ACH Gusto net pay | 48,200.00 | payroll_register.json net_pay 48,200.00 |
| 06/25 | ACH Gusto tax | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 |

Withdrawals 84,900.00 = bills 25,420.00 + net pay 48,200.00 + taxes 11,280.00 ✓. Payroll register agrees to bank on BOTH legs (net pay and tax remittance), and the register's identity holds (54,404.00 + 5,076.00 = 48,200.00 + 11,280.00 = 59,480.00) — the payroll test required by the close checklist passes cleanly; **single net-pay debit, no duplicate** (April's one-time duplicate was refunded in May and is not repeated).

## Cash roll-forward proof (books)

260,300.00 (May book close) + 52,050.00 receipts (30,450.00 recurring + 21,600.00 Saltline) − 25,420.00 bill payments − 59,480.00 payroll = **227,450.00** = book cash per trial_balance.json = bank statement ending ✓.

## Differences

**None at 06/30.** January, February, March, May and June recons all closed at zero difference; April's duplicate net-pay debit (the only reconciling item of the year to date) was refunded 05/09 and closed in the May reconciliation. Statement footer boilerplate (60-day error-report clause) noted; no action — the June statement was verified line-by-line at close, well within the window.
