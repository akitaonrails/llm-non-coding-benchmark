# Bank reconciliation — July 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_07/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 07/31/2025 (per statement) | **175,330.00** |
| Book balance, 07/31/2025 (per trial_balance.json 1000) | **175,330.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced.

## Statement integrity checks (performed line-by-line, header not trusted)

- Header values verified **by content, not by label** (April's and May's PDF text layers printed header values misaligned under the wrong captions). This month the labels align: beginning 227,450.00 (= June bank ending AND June book close ✓), total debits 82,570.00, total credits 30,450.00, ending 175,330.00. Cross-foot verified: 227,450.00 + 30,450.00 − 82,570.00 = 175,330.00 ✓.
- Transaction rows print in slightly shifted columns in the later part of the page (pdftotext geometry, as in prior months); debit/credit classification was therefore taken from the running-balance **delta**, not column position — every row's sign is proved by the recomputation below (a misclassified row would break it). The statement prints each transaction's balance; recomputation anchors on the June-carryover beginning balance 227,450.00.
- All 31 transaction running balances recomputed independently: **31 of 31 printed balances agree to the recomputation** — a fully clean statement, no displaced amounts. Recomputed ending 175,330.00 = printed ending ✓. Transaction count: 31 (7 withdrawals + 24 deposits). Full table below.

## Full transaction ledger — recomputation vs printed balances

Recomputed cash roll starts at 227,450.00 (June close). Printed balance equals the recomputed balance on every row (tie column = ✓ where equal).

| # | Date | Description | Out (debit) | In (credit) | Balance (printed = recomputed) | Tie |
|--:|---|---:|---:|---:|---:|---|
| 1 | 07/05/2025 | ACH AWS | 10,640.00 | | 216,810.00 | ✓ |
| 2 | 07/06/2025 | ACH WEWORK | 7,200.00 | | 209,610.00 | ✓ |
| 3 | 07/07/2025 | ACH GUSTO FEES | 240.00 | | 209,370.00 | ✓ |
| 4 | 07/08/2025 | ACH NOTION/SLACK/GITHUB | 1,460.00 | | 207,910.00 | ✓ |
| 5 | 07/09/2025 | ACH GOOGLE ADS | 3,550.00 | | 204,360.00 | ✓ |
| 6 | 07/20/2025 | ACH CEDAR LOGISTICS INC | | 450.00 | 204,810.00 | ✓ |
| 7 | 07/20/2025 | ACH ALDER STUDIOS INC | | 900.00 | 205,710.00 | ✓ |
| 8 | 07/20/2025 | ACH KESTREL FOODS CO | | 650.00 | 206,360.00 | ✓ |
| 9 | 07/20/2025 | ACH EMBER SYSTEMS INC | | 450.00 | 206,810.00 | ✓ |
| 10 | 07/21/2025 | ACH CEDAR LOGISTICS LLC | | 1,800.00 | 208,610.00 | ✓ |
| 11 | 07/21/2025 | ACH EMBER FOODS LLC | | 1,800.00 | 210,410.00 | ✓ |
| 12 | 07/22/2025 | ACH EMBER HEALTH CO | | 2,400.00 | 212,810.00 | ✓ |
| 13 | 07/22/2025 | ACH GRANITE SYSTEMS LLC | | 1,800.00 | 214,610.00 | ✓ |
| 14 | 07/22/2025 | ACH CEDAR LABS LLC | | 1,800.00 | 216,410.00 | ✓ |
| 15 | 07/22/2025 | ACH ALDER STUDIOS LLC | | 1,800.00 | 218,210.00 | ✓ |
| 16 | 07/23/2025 | ACH JUNIPER LOGISTICS LLC | | 650.00 | 218,860.00 | ✓ |
| 17 | 07/23/2025 | ACH EMBER CAPITAL INC | | 2,400.00 | 221,260.00 | ✓ |
| 18 | 07/23/2025 | ACH EMBER LOGISTICS INC | | 450.00 | 221,710.00 | ✓ |
| 19 | 07/23/2025 | ACH HARBOR LOGISTICS LLC | | 1,200.00 | 222,910.00 | ✓ |
| 20 | 07/23/2025 | ACH CEDAR STUDIOS INC | | 900.00 | 223,810.00 | ✓ |
| 21 | 07/24/2025 | ACH KESTREL SYSTEMS INC | | 2,400.00 | 226,210.00 | ✓ |
| 22 | 07/24/2025 | ACH IRIS HEALTH LLC | | 900.00 | 227,110.00 | ✓ |
| 23 | 07/24/2025 | ACH BIRCH LABS LLC | | 2,400.00 | 229,510.00 | ✓ |
| 24 | 07/25/2025 | ACH DUNE HEALTH CO | | 900.00 | 230,410.00 | ✓ |
| 25 | 07/25/2025 | ACH EMBER CAPITAL CO | | 2,400.00 | 232,810.00 | ✓ |
| 26 | 07/25/2025 | ACH FJORD HEALTH CO | | 450.00 | 233,260.00 | ✓ |
| 27 | 07/25/2025 | ACH GUSTO NET PAY | 48,200.00 | | 185,060.00 | ✓ |
| 28 | 07/25/2025 | ACH GUSTO TAX | 11,280.00 | | 173,780.00 | ✓ |
| 29 | 07/26/2025 | ACH BIRCH HEALTH CO | | 650.00 | 174,430.00 | ✓ |
| 30 | 07/26/2025 | ACH FJORD STUDIOS INC | | 450.00 | 174,880.00 | ✓ |
| 31 | 07/26/2025 | ACH DUNE FOODS CO | | 450.00 | 175,330.00 | ✓ |

Column totals: withdrawals 82,570.00, deposits 30,450.00 — both agree with the statement header totals ✓.

## Deposits — 24 items, 30,450.00, all matched

The 24 customer deposits (07/20–07/26) equal cash_receipts.csv row-for-row — the bank multiset (payer, amount) equals the receipts file exactly — and every receipt matches its July invoice by customer + amount (verified programmatically): 24 recurring invoices INV-2350..INV-2373, 30,450.00, all collected in-month. No opening A/R was collected (open_items.md item 7). **Zero deposits in transit at 07/30/31.**

**Name trap checked:** deposit #19 `ACH HARBOR LOGISTICS LLC 1,200.00` is **customer C-017 Harbor Logistics LLC** paying July invoice INV-2366 — it is *not* anything from vendor **Harbor Law LLP**, the law-firm vendor of open item 2. There is no Harbor Law LLP invoice in vendor_bills.csv for July and no Harbor Law LLP payment on the statement (see below). The similar name does not create support for the May/June item continuing.

## Withdrawals — 7 items, 82,570.00, all supported

| Bank (date) | Item | Amount | Agrees to |
|---|---|---:|---|
| 07/05 | ACH AWS | 10,640.00 | vendor_bills.csv AWS 10,640.00 (June 10,520.00, +120.00 usage variance) |
| 07/06 | ACH WeWork | 7,200.00 | vendor_bills.csv WeWork 7,200.00 |
| 07/07 | ACH Gusto fees | 240.00 | vendor_bills.csv Gusto fees 240.00 |
| 07/08 | ACH Notion/Slack/GitHub | 1,460.00 | vendor_bills.csv 1,460.00 |
| 07/09 | ACH Google Ads | 3,550.00 | vendor_bills.csv Google Ads 3,550.00 (June 3,500.00, +50.00) |
| 07/25 | ACH Gusto net pay | 48,200.00 | payroll_register.json net_pay 48,200.00 |
| 07/25 | ACH Gusto tax | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 |

Withdrawals 82,570.00 = 5 bill payments 23,090.00 + net pay 48,200.00 + taxes 11,280.00 ✓. **No Harbor Law LLP debit** — the May/June 2,500.00 pattern did not continue (open item 2 re-aged). Payroll agrees to bank on BOTH legs, and the register identity holds: gross 54,404.00 = net 48,200.00 + withholdings 6,204.00, and 11,280.00 remitted = 6,204.00 + employer 5,076.00, so 48,200.00 + 11,280.00 = 59,480.00 = total employer cost — the close-checklist payroll test (register AND bank) passes to the penny. **Single net-pay debit — no duplicate** (April's one-time duplicate, refunded in May, remains non-recurring). No unidentified debit or credit anywhere on the statement (open item 5 stays an opening-balance-only mystery).

## Cash roll-forward proof (books)

227,450.00 (June book close) + 30,450.00 receipts − 23,090.00 bill payments − 59,480.00 payroll = **175,330.00** = book cash per trial_balance.json = bank statement ending ✓.

## Differences

**None at 07/31.** All seven monthly recons (Jan–Jul) now close at zero difference; April's duplicate net-pay debit (the only reconciling item of the year to date) was refunded 05/09 and closed in the May reconciliation. Statement footer boilerplate (60-day error-report clause) noted; no action — the July statement was verified line-by-line at close, well within the window.
