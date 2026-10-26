# Bank reconciliation — April 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_04/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 04/30/2025 (per statement) | **233,880.00** |
| Book balance, 04/30/2025 (per trial_balance.json 1000) | **282,080.00** |
| **Difference** | **48,200.00** |

The difference is **one bank-side duplicate debit** — a second `ACH GUSTO NET PAY` of 48,200.00 posted 04/26/2025 when only one payroll was run in April (documents/month_04/note_from_office_manager.txt: "two net-pay debits hit our account, only one payroll was run", Gusto support ticket #GS-44812 opened 04/27, unresolved). The payroll register supports exactly one payroll (gross 54,404.00 + employer 5,076.00; net 48,200.00 + remitted 11,280.00 = 59,480.00), and the books record exactly that one payroll (JE-2025-04-08). **The books are not adjusted for the bank's error; nothing is forced.** Reconciling item: bank 233,880.00 + 48,200.00 reversal expected from bank/Gusto = 282,080.00 = book. See open_items.md item 12.

## Statement integrity checks (performed line-by-line, header not trusted)

- Statement header is misaligned in the PDF text layer: the three header values print one label below their captions ("Beginning balance" prints blank; 333,690.00 prints under "Total debits", 130,260.00 under "Total credits", 30,450.00 under "Ending balance"; the 233,880.00 ending appears only as the last running balance). Treated by content, not by label: beginning 333,690.00 (agrees with March book AND bank close), withdrawals 130,260.00, deposits 30,450.00. Cross-foot verified: 333,690.00 + 30,450.00 − 130,260.00 = 233,880.00 ✓ — the bank's own totals are internally consistent, i.e. the bank actually processed both net-pay debits; this is a processing duplicate, not a display error.
- Withdrawals cross-check: bills 22,580.00 + one payroll net 48,200.00 + taxes 11,280.00 = 82,060.00 supported; 82,060.00 + duplicate 48,200.00 = 130,260.00 = statement withdrawals ✓.
- All 32 statement lines recomputed independently from beginning 333,690.00. Of the 31 lines that print a running balance, 30 agree to the penny; the one printed mismatch is the duplicate NET PAY row itself, whose printed "340,010.00" is an extraction/column artifact — 340,010.00 is the Fjord Health deposit's true running balance (339,560.00 + 450.00), displaced onto the last row because the 04/25 Fjord row prints no balance and the final row's third amount (233,880.00) is the printed ending balance. With that documented re-merge, the recomputed sequence lands exactly on the printed ending 233,880.00 ✓. Full table below.

## Full transaction ledger — recomputation vs printed balances

Recomputed cash roll starts at 333,690.00. "Printed" = balance as printed on the statement; "Recomputed" = independent recalculation.

| Date | Description | Out (debit) | In (credit) | Printed bal | Recomputed bal | Tie |
|---|---|---:|---:|---:|---:|---|
| 04/05/2025 | ACH AWS | 10,280.00 |  | 323,410.00 | 323,410.00 | OK |
| 04/06/2025 | ACH WEWORK | 7,200.00 |  | 316,210.00 | 316,210.00 | OK |
| 04/07/2025 | ACH GUSTO FEES | 240.00 |  | 315,970.00 | 315,970.00 | OK |
| 04/08/2025 | ACH NOTION/SLACK/GITHUB | 1,460.00 |  | 314,510.00 | 314,510.00 | OK |
| 04/09/2025 | ACH GOOGLE ADS | 3,400.00 |  | 311,110.00 | 311,110.00 | OK |
| 04/20/2025 | ACH CEDAR LOGISTICS INC |  | 450.00 | 311,560.00 | 311,560.00 | OK |
| 04/20/2025 | ACH ALDER STUDIOS INC |  | 900.00 | 312,460.00 | 312,460.00 | OK |
| 04/20/2025 | ACH KESTREL FOODS CO |  | 650.00 | 313,110.00 | 313,110.00 | OK |
| 04/20/2025 | ACH EMBER SYSTEMS INC |  | 450.00 | 313,560.00 | 313,560.00 | OK |
| 04/21/2025 | ACH CEDAR LOGISTICS LLC |  | 1,800.00 | 315,360.00 | 315,360.00 | OK |
| 04/21/2025 | ACH EMBER FOODS LLC |  | 1,800.00 | 317,160.00 | 317,160.00 | OK |
| 04/22/2025 | ACH EMBER HEALTH CO |  | 2,400.00 | 319,560.00 | 319,560.00 | OK |
| 04/22/2025 | ACH GRANITE SYSTEMS LLC |  | 1,800.00 | 321,360.00 | 321,360.00 | OK |
| 04/22/2025 | ACH CEDAR LABS LLC |  | 1,800.00 | 323,160.00 | 323,160.00 | OK |
| 04/22/2025 | ACH ALDER STUDIOS LLC |  | 1,800.00 | 324,960.00 | 324,960.00 | OK |
| 04/23/2025 | ACH JUNIPER LOGISTICS LLC |  | 650.00 | 325,610.00 | 325,610.00 | OK |
| 04/23/2025 | ACH EMBER CAPITAL INC |  | 2,400.00 | 328,010.00 | 328,010.00 | OK |
| 04/23/2025 | ACH EMBER LOGISTICS INC |  | 450.00 | 328,460.00 | 328,460.00 | OK |
| 04/23/2025 | ACH HARBOR LOGISTICS LLC |  | 1,200.00 | 329,660.00 | 329,660.00 | OK |
| 04/23/2025 | ACH CEDAR STUDIOS INC |  | 900.00 | 330,560.00 | 330,560.00 | OK |
| 04/24/2025 | ACH KESTREL SYSTEMS INC |  | 2,400.00 | 332,960.00 | 332,960.00 | OK |
| 04/24/2025 | ACH IRIS HEALTH LLC |  | 900.00 | 333,860.00 | 333,860.00 | OK |
| 04/24/2025 | ACH BIRCH LABS LLC |  | 2,400.00 | 336,260.00 | 336,260.00 | OK |
| 04/25/2025 | ACH DUNE HEALTH CO |  | 900.00 | 337,160.00 | 337,160.00 | OK |
| 04/25/2025 | ACH EMBER CAPITAL CO |  | 2,400.00 | 339,560.00 | 339,560.00 | OK |
| 04/25/2025 | ACH FJORD HEALTH CO |  | 450.00 | — | 340,010.00 | — (prints no balance) |
| 04/25/2025 | ACH GUSTO NET PAY | 48,200.00 |  | 291,810.00 | 291,810.00 | OK |
| 04/25/2025 | ACH GUSTO TAX | 11,280.00 |  | 280,530.00 | 280,530.00 | OK |
| 04/26/2025 | ACH BIRCH HEALTH CO |  | 650.00 | 281,180.00 | 281,180.00 | OK |
| 04/26/2025 | ACH FJORD STUDIOS INC |  | 450.00 | 281,630.00 | 281,630.00 | OK |
| 04/26/2025 | ACH DUNE FOODS CO |  | 450.00 | 282,080.00 | 282,080.00 | OK |
| 04/26/2025 | ACH GUSTO NET PAY | 48,200.00 |  | 340,010.00 | 233,880.00 | MISMATCH — see note |

Recomputed ending balance **233,880.00** = printed ending balance ✓ (recomputed roll counts the duplicate debit as the bank did; the BOOK roll below excludes it).

## Deposits — 24 items, 30,450.00, all matched

24 ACH deposits 04/20–04/26 totaling 30,450.00 equal cash_receipts.csv row-for-row: the bank deposit multiset (date, payer name, amount) equals the receipts file exactly, and every receipt matches its invoice by customer + amount (all verified programmatically) → **zero deposits in transit at 04/30**. Receipts 30,450.00 = April recurring invoices INV-2276..INV-2299 exactly; all collected in-month; no opening A/R collected (open_items.md item 7).

## Withdrawals — 8 items, 130,260.00 (7 supported, 82,060.00; 1 bank duplicate)

| Bank (date) | Item | Amount | Agrees to |
|---|---|---:|---|
| 04/05 | ACH AWS | 10,280.00 | vendor_bills.csv AWS 10,280.00 |
| 04/06 | ACH WeWork | 7,200.00 | vendor_bills.csv WeWork 7,200.00 |
| 04/07 | ACH Gusto fees | 240.00 | vendor_bills.csv Gusto fees 240.00 |
| 04/08 | ACH Notion/Slack/GitHub | 1,460.00 | vendor_bills.csv 1,460.00 |
| 04/09 | ACH Google Ads | 3,400.00 | vendor_bills.csv Google Ads 3,400.00 |
| 04/25 | ACH Gusto net pay | 48,200.00 | payroll_register.json net_pay 48,200.00 |
| 04/25 | ACH Gusto tax | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 |
| 04/26 | ACH Gusto net pay | 48,200.00 | **nothing — bank-side duplicate** (ticket GS-44812); no second payroll exists in the register; not booked |

Supported withdrawals 82,060.00 = bills 22,580.00 + net pay 48,200.00 + taxes 11,280.00 ✓. Payroll register agrees to bank for the real payroll (net pay AND tax remittance); the register cannot and does not support the 04/26 second debit.

## Cash roll-forward proof (books)

333,690.00 (March book close, = March bank) + 30,450.00 receipts − 22,580.00 bills − 59,480.00 payroll (one payroll: net 48,200.00 + taxes 11,280.00) = **282,080.00** = book cash per trial_balance.json ✓. Bank differs only by the 48,200.00 duplicate debit the books never recorded.

## Differences

**48,200.00 — one item, fully identified, nothing forced, no plug.** The bank double-posted the April net-pay debit (04/25 and 04/26) for a single payroll run. Books carry one payroll per the register; a receivable/claim for the duplicate is NOT booked — the library provides no guidance on bank-error claims and I will not invent policy (stated library gap, same treatment discipline as prior months). Follow-up: Gusto ticket #GS-44812 (opened 04/27, unresolved at close); expect reversal in May; open_items.md item 12 carries the aging.
