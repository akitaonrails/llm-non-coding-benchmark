# Bank Reconciliation — April 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-04-01 through 2025-04-30
**Statement source:** `documents/month_04/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). All items below are matched
> against the April PDF statement.

## Summary

| | Amount |
|---|---:|
| Balance per bank statement, 2025-04-30 | **$233,880.00** |
| Balance per books, account 1000 (trial balance) | **$233,880.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unpaid debits | 0.00 |
| Bank items not on the books | 0.00 (the duplicate net-pay debit has been **recorded on the books**, see below) |
| Book items not at the bank | 0.00 |
| **Difference** | **$0.00** |

The books tie to the bank to the dollar **only because the second (duplicate)
GUSTO NET PAY debit was recorded** — as a recovery claim in new account
1200, not as an expense. See "Duplicate net-pay debit" below; this is the
month's critical item (`open_items.md` item 1).

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-03-31 | month_03 close / statement beginning balance | $333,690.00 |
| Customer receipts, 24 items (all cleared, below) | JE-2504-002 | +$30,450.00 |
| Vendor ACH payments, 5 items (below) | JE-2504-008 | −$22,580.00 |
| Payroll net pay ACH, 04/25 | JE-2504-009 | −$48,200.00 |
| Payroll tax remit ACH, 04/25 | JE-2504-011 | −$11,280.00 |
| **Duplicate net-pay ACH, 04/26 → claim asset 1200 (NOT expense)** | JE-2504-012 | −$48,200.00 |
| **Book cash 2025-04-30** | | **$233,880.00** |

$333,690.00 + $30,450.00 = $364,140.00
$364,140.00 − $22,580.00 = $341,560.00
$341,560.00 − $48,200.00 − $11,280.00 − $48,200.00 = **$233,880.00**

Trial balance account 1000 shows cumulative debits $611,800.00 (= $581,350.00
through March + $30,450.00 April receipts) and cumulative credits $377,920.00
(= $247,660.00 through March + $22,580.00 + $48,200.00 + $11,280.00 +
$48,200.00), net **$233,880.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $333,690.00, total debits $130,260.00, total
credits $30,450.00, ending $233,880.00.
$333,690.00 + $30,450.00 − $130,260.00 = $233,880.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,280.00 + $7,200.00 + $240.00 + $1,460.00 + $3,400.00 +
$48,200.00 + $11,280.00 + $48,200.00 = $130,260.00 ✔ (8 debit lines)
Credits footing: 24 monthly ACHs = $30,450.00 ✔ (24 credit lines; 32
transaction lines total)

## Credits — 24 items, all cleared, matched 1:1

| Date | Bank description | Amount | Matches |
|---|---|---:|---|
| 04/20–04/26 | 24 monthly ACHs (CEDAR LOGISTICS INC 450, ALDER STUDIOS INC 900, KESTREL FOODS CO 650, EMBER SYSTEMS INC 450, CEDAR LOGISTICS LLC 1,800, EMBER FOODS LLC 1,800, EMBER HEALTH CO 2,400, GRANITE SYSTEMS LLC 1,800, CEDAR LABS LLC 1,800, ALDER STUDIOS LLC 1,800, JUNIPER LOGISTICS LLC 650, EMBER CAPITAL INC 2,400, EMBER LOGISTICS INC 450, HARBOR LOGISTICS LLC 1,200, CEDAR STUDIOS INC 900, KESTREL SYSTEMS INC 2,400, IRIS HEALTH LLC 900, BIRCH LABS LLC 2,400, DUNE HEALTH CO 900, EMBER CAPITAL CO 2,400, FJORD HEALTH CO 450, BIRCH HEALTH CO 650, FJORD STUDIOS INC 450, DUNE FOODS CO 450) | $30,450.00 | `cash_receipts.csv` 24 items matched by date and amount, each applied to INV-2276..INV-2299 (total 30,450) |
| | **Total credits** | **$30,450.00** | |

All 24 April invoices are collected in full within the month. **Nothing was
applied to the opening A/R of $92,650.00** (fourth month running — U3).

## Debits — 8 items, all on the books

| Date | Bank description | Amount | Book reference |
|---|---|---:|---|
| 04/05 | ACH AWS | $10,280.00 | JE-2504-003 (6000) / JE-2504-008 |
| 04/06 | ACH WEWORK | $7,200.00 | JE-2504-004 (6100) / JE-2504-008 |
| 04/07 | ACH GUSTO FEES | $240.00 | JE-2504-005 (6200) / JE-2504-008 |
| 04/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2504-006 (6300) / JE-2504-008 |
| 04/09 | ACH GOOGLE ADS | $3,400.00 | JE-2504-007 (6400) / JE-2504-008 |
| 04/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2504-009 |
| 04/25 | ACH GUSTO TAX | $11,280.00 | JE-2504-011 |
| **04/26** | **ACH GUSTO NET PAY (second, duplicate)** | **$48,200.00** | **JE-2504-012 → Dr 1200 Due from Gusto (claim), NOT payroll expense** |
| | **Total debits** | **$130,260.00** | |

Vendor debits agree to `vendor_bills.csv` amounts and dates 1:1. There is no
Harbor Law bill in April (the March $2,500.00 was one-time). **No payment
against the opening A/P of $17,420.00** (fourth month running — U9).

## Duplicate net-pay debit — why it is on the books as a claim, not an expense

- The bank shows **two** GUSTO NET PAY debits of $48,200.00 (04/25 and 04/26),
  but `payroll_register.json` shows **one** April payroll (gross $54,404.00,
  net $48,200.00, 9 employees), and `documents/month_04/note_from_office_manager.txt`
  (Gusto ticket GS-44812, opened 4/27) states: *"two net-pay debits hit our
  account, only one payroll was run."*
- The cash outflow is real and must be recorded for the books to agree with
  the bank; but recognizing it as a **second payroll expense** would contradict
  the register and overstate April expense by $48,200.00. It is booked as a
  recovery claim (asset 1200, new account — judgment call flagged in
  `open_items.md`).
- **Payroll three-way tie (register ↔ books ↔ bank):** holds for the items it
  should: net $48,200.00 = JE-2504-009 = bank 04/25 ✔; tax remit $11,280.00 =
  JE-2504-011 = bank 04/25 ✔; withholding $54,404.00 − $48,200.00 =
  $6,204.00 (U7) plus employer $5,076.00 = $11,280.00 ✔; account 2210 clears
  cumulatively ($45,120.00 Dr = $45,120.00 Cr). The 04/26 debit matches **no**
  register item — it is isolated and documented, not forced into payroll.

## Time limit on recovery

The statement carries the clause: *"If no error is reported within 60 days the
account will be considered correct."* Sixty days from the 04/26 debit is
approximately **2025-06-25** — the duplicate must stay under dispute (Gusto
GS-44812 and/or bank recall) through that date. See `open_items.md` item 1 and
April question G1.

## Reconciling items

None. No deposits in transit, no outstanding checks, no unrecorded bank items.
