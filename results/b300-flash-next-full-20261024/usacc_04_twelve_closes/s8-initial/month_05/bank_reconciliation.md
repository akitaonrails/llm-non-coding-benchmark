# Bank reconciliation — May 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_05/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 05/31/2025 (per statement) | **260,300.00** |
| Book balance, 05/31/2025 (per trial_balance.json 1000) | **260,300.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced. The one reconciling item carried into May — the bank-side duplicate net-pay debit of 48,200.00 from April (ticket #GS-44812) — **extinguished this month**: the statement shows `05/09/2025 ACH CREDIT GUSTO REFUND 48,200.00`. Consistent with the commitment in month_04/open_items.md item 12, **no journal entry was booked for the refund**: the books never recorded the duplicate debit, so the refund belongs to the bank reconciliation only — it brings the bank roll back onto the book roll and then closes with no residual. Item 12 is closed.

## Statement integrity checks (performed line-by-line, header not trusted)

- Statement header is again misaligned in the PDF text layer: this month all four values print, each one label below its caption — 233,880.00 prints under "Total debits", 82,230.00 under "Total credits", 108,650.00 under "Ending balance", and 260,300.00 floats after it. Treated by content, not by label: beginning 233,880.00 (= April bank ending AND April book close ✓), total debits 82,230.00, total credits 108,650.00, ending 260,300.00. Cross-foot verified: 233,880.00 + 108,650.00 − 82,230.00 = 260,300.00 ✓.
- A repeated column caption ("1 / Credit / Balance") prints mid-page (after the 05/24 Birch Labs row) — a page-break artifact, not a transaction. True transaction count is 33 (7 withdrawals + 26 deposits).
- All 33 transaction running balances recomputed independently from beginning 233,880.00: **33 of 33 printed balances agree to the recomputation** — a fully clean statement (every row prints its balance; no displaced amounts). Recomputed ending 260,300.00 = printed ending ✓. Full table below.

## Full transaction ledger — recomputation vs printed balances

Recomputed cash roll starts at 233,880.00. "Printed" = balance as printed on the statement; "Recomputed" = independent recalculation.

| Date | Description | Out (debit) | In (credit) | Printed bal | Recomputed bal | Tie |
|---|---|---:|---:|---:|---:|---|
| 05/05/2025 | ACH AWS | 10,400.00 |  | 223,480.00 | 223,480.00 | ✓ |
| 05/06/2025 | ACH WEWORK | 7,200.00 |  | 216,280.00 | 216,280.00 | ✓ |
| 05/07/2025 | ACH GUSTO FEES | 240.00 |  | 216,040.00 | 216,040.00 | ✓ |
| 05/08/2025 | ACH NOTION/SLACK/GITHUB | 1,460.00 |  | 214,580.00 | 214,580.00 | ✓ |
| 05/09/2025 | ACH GOOGLE ADS | 3,450.00 |  | 211,130.00 | 211,130.00 | ✓ |
| 05/09/2025 | ACH CREDIT GUSTO REFUND |  | 48,200.00 | 259,330.00 | 259,330.00 | ✓ |
| 05/15/2025 | WIRE IN QUARRY ANALYTICS CO |  | 30,000.00 | 289,330.00 | 289,330.00 | ✓ |
| 05/20/2025 | ACH CEDAR LOGISTICS INC |  | 450.00 | 289,780.00 | 289,780.00 | ✓ |
| 05/20/2025 | ACH ALDER STUDIOS INC |  | 900.00 | 290,680.00 | 290,680.00 | ✓ |
| 05/20/2025 | ACH KESTREL FOODS CO |  | 650.00 | 291,330.00 | 291,330.00 | ✓ |
| 05/20/2025 | ACH EMBER SYSTEMS INC |  | 450.00 | 291,780.00 | 291,780.00 | ✓ |
| 05/21/2025 | ACH CEDAR LOGISTICS LLC |  | 1,800.00 | 293,580.00 | 293,580.00 | ✓ |
| 05/21/2025 | ACH EMBER FOODS LLC |  | 1,800.00 | 295,380.00 | 295,380.00 | ✓ |
| 05/22/2025 | ACH EMBER HEALTH CO |  | 2,400.00 | 297,780.00 | 297,780.00 | ✓ |
| 05/22/2025 | ACH GRANITE SYSTEMS LLC |  | 1,800.00 | 299,580.00 | 299,580.00 | ✓ |
| 05/22/2025 | ACH CEDAR LABS LLC |  | 1,800.00 | 301,380.00 | 301,380.00 | ✓ |
| 05/22/2025 | ACH ALDER STUDIOS LLC |  | 1,800.00 | 303,180.00 | 303,180.00 | ✓ |
| 05/23/2025 | ACH JUNIPER LOGISTICS LLC |  | 650.00 | 303,830.00 | 303,830.00 | ✓ |
| 05/23/2025 | ACH EMBER CAPITAL INC |  | 2,400.00 | 306,230.00 | 306,230.00 | ✓ |
| 05/23/2025 | ACH EMBER LOGISTICS INC |  | 450.00 | 306,680.00 | 306,680.00 | ✓ |
| 05/23/2025 | ACH HARBOR LOGISTICS LLC |  | 1,200.00 | 307,880.00 | 307,880.00 | ✓ |
| 05/23/2025 | ACH CEDAR STUDIOS INC |  | 900.00 | 308,780.00 | 308,780.00 | ✓ |
| 05/24/2025 | ACH KESTREL SYSTEMS INC |  | 2,400.00 | 311,180.00 | 311,180.00 | ✓ |
| 05/24/2025 | ACH IRIS HEALTH LLC |  | 900.00 | 312,080.00 | 312,080.00 | ✓ |
| 05/24/2025 | ACH BIRCH LABS LLC |  | 2,400.00 | 314,480.00 | 314,480.00 | ✓ |
| 05/25/2025 | ACH DUNE HEALTH CO |  | 900.00 | 315,380.00 | 315,380.00 | ✓ |
| 05/25/2025 | ACH EMBER CAPITAL CO |  | 2,400.00 | 317,780.00 | 317,780.00 | ✓ |
| 05/25/2025 | ACH FJORD HEALTH CO |  | 450.00 | 318,230.00 | 318,230.00 | ✓ |
| 05/25/2025 | ACH GUSTO NET PAY | 48,200.00 |  | 270,030.00 | 270,030.00 | ✓ |
| 05/25/2025 | ACH GUSTO TAX | 11,280.00 |  | 258,750.00 | 258,750.00 | ✓ |
| 05/26/2025 | ACH BIRCH HEALTH CO |  | 650.00 | 259,400.00 | 259,400.00 | ✓ |
| 05/26/2025 | ACH FJORD STUDIOS INC |  | 450.00 | 259,850.00 | 259,850.00 | ✓ |
| 05/26/2025 | ACH DUNE FOODS CO |  | 450.00 | 260,300.00 | 260,300.00 | ✓ |

## Deposits — 26 items, 108,650.00, all matched

25 customer deposits (05/15–05/26) equal cash_receipts.csv row-for-row — the bank multiset (date, payer, amount) equals the receipts file exactly, and every receipt matches its invoice by customer + amount (verified programmatically): 24 recurring invoices 30,450.00 collected in-month (wires 05/20–05/26) plus Quarry Analytics Co 30,000.00 wire 05/15 (INV-2324). No opening A/R was collected (open_items.md item 7). The 26th deposit is the 48,200.00 Gusto refund addressed above — bank-side only, not booked. **Zero deposits in transit at 05/31.**

## Withdrawals — 7 items, 82,230.00, all supported

| Bank (date) | Item | Amount | Agrees to |
|---|---|---:|---|
| 05/05 | ACH AWS | 10,400.00 | vendor_bills.csv AWS 10,400.00 |
| 05/06 | ACH WeWork | 7,200.00 | vendor_bills.csv WeWork 7,200.00 |
| 05/07 | ACH Gusto fees | 240.00 | vendor_bills.csv Gusto fees 240.00 |
| 05/08 | ACH Notion/Slack/GitHub | 1,460.00 | vendor_bills.csv 1,460.00 |
| 05/09 | ACH Google Ads | 3,450.00 | vendor_bills.csv Google Ads 3,450.00 |
| 05/25 | ACH Gusto net pay | 48,200.00 | payroll_register.json net_pay 48,200.00 |
| 05/25 | ACH Gusto tax | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 |

Withdrawals 82,230.00 = bills 22,750.00 + net pay 48,200.00 + taxes 11,280.00 ✓. Payroll register agrees to bank on BOTH legs (net pay and tax remittance), and the register's identity holds (54,404.00 + 5,076.00 = 48,200.00 + 11,280.00 = 59,480.00) — the payroll test required by the close checklist passes cleanly; **no duplicate net-pay debit this month** (April's duplicate has been refunded, not repeated).

## Cash roll-forward proof (books)

282,080.00 (April book close) + 60,450.00 receipts (30,450.00 recurring + 30,000.00 Quarry) − 22,750.00 bill payments − 59,480.00 payroll = **260,300.00** = book cash per trial_balance.json = bank statement ending ✓.

## Differences

**None at 05/31.** The 48,200.00 bank duplicate from April was reversed by the bank on 05/09 (ACH CREDIT GUSTO REFUND) exactly as anticipated under ticket #GS-44812; per the stated treatment it was never on the books, so the reversal required no entry and leaves no residual. The two rolls now agree to the penny. January, February and March recons also closed at zero difference — April's duplicate was the only reconciling item in the year to date, and May returns to zero. Statement footer boilerplate (60-day error-report clause) noted; no action — the May statement was verified line-by-line at close, well within the window.
