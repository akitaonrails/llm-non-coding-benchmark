# Bank reconciliation — March 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_03/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 03/31/2025 (per statement) | **333,690.00** |
| Book balance, 03/31/2025 (per trial_balance.json 1000) | **333,690.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced.

## Statement integrity checks (performed line-by-line, header not trusted)

- Statement header: beginning 369,630.00 / total withdrawals 84,390.00 / total deposits 48,450.00 / ending 333,690.00. Cross-foot verified: 369,630.00 + 48,450.00 − 84,390.00 = 333,690.00 ✓.
- Beginning balance 369,630.00 = February closing bank AND February book cash ✓ (no reconciling items carried in from month_02).
- All 33 transaction printed running balances recomputed independently from beginning 369,630.00 — every one agrees to the penny ✓ (full table below).
- pdftotext layout artifact documented: on the 03/15/2025 `WIRE IN MARIGOLD SCHOOLS INC` row, the description prints alone and its amounts (18,000.00 / 362,720.00) reflow into the following block, which then carries 4 amounts and the 03/20 Cedar Logistics description. The blocks were re-merged (first amount pair → wire at its own date 03/15; second pair → Cedar at 03/20). This is a text-extraction artifact of the PDF column layout, not a bank discrepancy: the re-merged sequence makes every subsequent running balance tie (03/15: 344,720.00 + 18,000.00 = 362,720.00 ✓; 03/20: 362,720.00 + 450.00 = 363,170.00 ✓).

## Full transaction ledger — recomputation vs printed balances

Recomputed cash roll starts at 369,630.00. "Printed" = balance as printed on the statement; "Recomputed" = independent recalculation. All 33 rows OK.

| Date | Description | In | Out amt | In amt | Printed bal | Recomputed bal | Tie |
|---|---|---|---:|---:|---:|---:|---|
| 03/05/2025 | ACH AWS |  | 10,160.00 |  | 359,470.00 | 359,470.00 | OK |
| 03/06/2025 | ACH WEWORK |  | 7,200.00 |  | 352,270.00 | 352,270.00 | OK |
| 03/07/2025 | ACH GUSTO FEES |  | 240.00 |  | 352,030.00 | 352,030.00 | OK |
| 03/08/2025 | ACH NOTION/SLACK/GITHUB |  | 1,460.00 |  | 350,570.00 | 350,570.00 | OK |
| 03/09/2025 | ACH HARBOR LAW LLP |  | 2,500.00 |  | 348,070.00 | 348,070.00 | OK |
| 03/10/2025 | ACH GOOGLE ADS |  | 3,350.00 |  | 344,720.00 | 344,720.00 | OK |
| 03/15/2025 | WIRE IN MARIGOLD SCHOOLS INC | + 18,000.00 |  | 18,000.00 | 362,720.00 | 362,720.00 | OK |
| 03/20/2025 | ACH CEDAR LOGISTICS INC | + 450.00 |  | 450.00 | 363,170.00 | 363,170.00 | OK |
| 03/20/2025 | ACH ALDER STUDIOS INC | + 900.00 |  | 900.00 | 364,070.00 | 364,070.00 | OK |
| 03/20/2025 | ACH KESTREL FOODS CO | + 650.00 |  | 650.00 | 364,720.00 | 364,720.00 | OK |
| 03/20/2025 | ACH EMBER SYSTEMS INC | + 450.00 |  | 450.00 | 365,170.00 | 365,170.00 | OK |
| 03/21/2025 | ACH CEDAR LOGISTICS LLC | + 1,800.00 |  | 1,800.00 | 366,970.00 | 366,970.00 | OK |
| 03/21/2025 | ACH EMBER FOODS LLC | + 1,800.00 |  | 1,800.00 | 368,770.00 | 368,770.00 | OK |
| 03/22/2025 | ACH EMBER HEALTH CO | + 2,400.00 |  | 2,400.00 | 371,170.00 | 371,170.00 | OK |
| 03/22/2025 | ACH GRANITE SYSTEMS LLC | + 1,800.00 |  | 1,800.00 | 372,970.00 | 372,970.00 | OK |
| 03/22/2025 | ACH CEDAR LABS LLC | + 1,800.00 |  | 1,800.00 | 374,770.00 | 374,770.00 | OK |
| 03/22/2025 | ACH ALDER STUDIOS LLC | + 1,800.00 |  | 1,800.00 | 376,570.00 | 376,570.00 | OK |
| 03/23/2025 | ACH JUNIPER LOGISTICS LLC | + 650.00 |  | 650.00 | 377,220.00 | 377,220.00 | OK |
| 03/23/2025 | ACH EMBER CAPITAL INC | + 2,400.00 |  | 2,400.00 | 379,620.00 | 379,620.00 | OK |
| 03/23/2025 | ACH EMBER LOGISTICS INC | + 450.00 |  | 450.00 | 380,070.00 | 380,070.00 | OK |
| 03/23/2025 | ACH HARBOR LOGISTICS LLC | + 1,200.00 |  | 1,200.00 | 381,270.00 | 381,270.00 | OK |
| 03/23/2025 | ACH CEDAR STUDIOS INC | + 900.00 |  | 900.00 | 382,170.00 | 382,170.00 | OK |
| 03/24/2025 | ACH KESTREL SYSTEMS INC | + 2,400.00 |  | 2,400.00 | 384,570.00 | 384,570.00 | OK |
| 03/24/2025 | ACH IRIS HEALTH LLC | + 900.00 |  | 900.00 | 385,470.00 | 385,470.00 | OK |
| 03/24/2025 | ACH BIRCH LABS LLC | + 2,400.00 |  | 2,400.00 | 387,870.00 | 387,870.00 | OK |
| 03/25/2025 | ACH DUNE HEALTH CO | + 900.00 |  | 900.00 | 388,770.00 | 388,770.00 | OK |
| 03/25/2025 | ACH EMBER CAPITAL CO | + 2,400.00 |  | 2,400.00 | 391,170.00 | 391,170.00 | OK |
| 03/25/2025 | ACH FJORD HEALTH CO | + 450.00 |  | 450.00 | 391,620.00 | 391,620.00 | OK |
| 03/25/2025 | ACH GUSTO NET PAY |  | 48,200.00 |  | 343,420.00 | 343,420.00 | OK |
| 03/25/2025 | ACH GUSTO TAX |  | 11,280.00 |  | 332,140.00 | 332,140.00 | OK |
| 03/26/2025 | ACH BIRCH HEALTH CO | + 650.00 |  | 650.00 | 332,790.00 | 332,790.00 | OK |
| 03/26/2025 | ACH FJORD STUDIOS INC | + 450.00 |  | 450.00 | 333,240.00 | 333,240.00 | OK |
| 03/26/2025 | ACH DUNE FOODS CO | + 450.00 |  | 450.00 | 333,690.00 | 333,690.00 | OK |

Ending recomputed balance 333,690.00 = printed ending balance ✓.

## Deposits — 25 items, 48,450.00, all matched

| Bank (date, amount) | Source | Applied to |
|---|---|---|
| 03/15 wire Marigold Schools Inc 18,000.00 | cash_receipts.csv 2025-03-15 | INV-2275 (collected contract liability — NOT revenue at billing, see JE-2025-03-02/06) |
| 24 ACH deposits 03/20–03/26 totaling 30,450.00 | cash_receipts.csv rows 2–25 | INV-2251…INV-2274, each matched customer + amount + date |

Bank deposit multiset (date, amount) equals the cash-receipts file exactly, and all 25 receipts match a bank deposit by customer name + date + amount (verified programmatically) → **zero deposits in transit at 03/31**. Receipts 48,450.00 = recurring invoices 30,450.00 + Marigold 18,000.00 ✓, and receipts equal March billings exactly.

## Withdrawals — 8 items, 84,390.00, all matched

| Bank (date) | Item | Amount | Agrees to |
|---|---|---:|---|
| 03/05 | ACH AWS | 10,160.00 | vendor_bills.csv AWS 10,160.00 |
| 03/06 | ACH WeWork | 7,200.00 | vendor_bills.csv WeWork 7,200.00 |
| 03/07 | ACH Gusto fees | 240.00 | vendor_bills.csv Gusto fees 240.00 |
| 03/08 | ACH Notion/Slack/GitHub | 1,460.00 | vendor_bills.csv 1,460.00 |
| 03/09 | ACH Harbor Law LLP | 2,500.00 | vendor_bills.csv Harbor Law LLP 2,500.00 |
| 03/10 | ACH Google Ads | 3,350.00 | vendor_bills.csv Google Ads 3,350.00 |
| 03/25 | ACH Gusto net pay | 48,200.00 | payroll_register.json net_pay 48,200.00 |
| 03/25 | ACH Gusto tax | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 |

Vendor bills total 24,910.00 + net pay 48,200.00 + taxes 11,280.00 = 84,390.00 = total withdrawals ✓ (one-to-one, no unmatched bank item, no unmatched book item). Payroll register agrees to bank exactly (net pay AND tax remittance).

## Cash roll-forward proof

369,630.00 (Feb book close, = bank) + 48,450.00 receipts − 84,390.00 disbursements = **333,690.00** = book cash per trial_balance.json = bank per statement ✓.

## Differences

**None.** Zero difference at 03/31/2025, nothing forced, no plugs. All 33 printed running balances independently recomputed and confirmed; header amounts independently cross-footed.
