# Bank Reconciliation — March 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-03-01 through 2025-03-31
**Statement source:** `documents/month_03/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). All items below are matched
> against the March PDF statement.

## Summary

| | Amount |
|---|---:|
| Balance per bank statement, 2025-03-31 | **$333,690.00** |
| Balance per books, account 1000 (trial balance) | **$333,690.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unpaid debits | 0.00 |
| Bank items not on the books | 0.00 |
| Book items not at the bank | 0.00 |
| **Difference** | **$0.00** |

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-02-28 | month_02 close / statement beginning balance | $369,630.00 |
| Customer receipts, 25 items (all cleared, below) | JE-2503-003 | +$48,450.00 |
| Vendor ACH payments, 6 items (below) | JE-2503-010 | −$24,910.00 |
| Payroll net pay ACH, 03/25 | JE-2503-011 | −$48,200.00 |
| Payroll tax remit ACH, 03/25 | JE-2503-013 | −$11,280.00 |
| **Book cash 2025-03-31** | | **$333,690.00** |

$369,630.00 + $48,450.00 = $418,080.00
$418,080.00 − $24,910.00 − $48,200.00 − $11,280.00 = **$333,690.00**

Trial balance account 1000 shows cumulative debits $581,350.00 (= $532,900.00
through February + $48,450.00 March receipts) and cumulative credits
$247,660.00 (= $163,270.00 through February + $24,910.00 + $48,200.00 +
$11,280.00), net **$333,690.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $369,630.00, total debits $84,390.00, total credits
$48,450.00, ending $333,690.00.
$369,630.00 + $48,450.00 − $84,390.00 = $333,690.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,160.00 + $7,200.00 + $240.00 + $1,460.00 + $2,500.00 +
$3,350.00 + $48,200.00 + $11,280.00 = $84,390.00 ✔ (8 debit lines)
Credits footing: Marigold wire $18,000.00 + 24 monthly ACHs $30,450.00 =
$48,450.00 ✔ (25 credit lines; 33 transaction lines total)

## Credits — 25 items, all cleared, matched 1:1

| Date | Bank description | Amount | Matches |
|---|---|---:|---|
| 03/15 | WIRE IN MARIGOLD SCHOOLS INC | $18,000.00 | INV-2275 advance (C-027) — cash collected; revenue **deferred to 2200**, not recognized (JE-2503-002) |
| 03/20–03/26 | 24 monthly ACHs (CEDAR LOGISTICS INC 450, ALDER STUDIOS INC 900, KESTREL FOODS CO 650, EMBER SYSTEMS INC 450, CEDAR LOGISTICS LLC 1,800, EMBER FOODS LLC 1,800, EMBER HEALTH CO 2,400, GRANITE SYSTEMS LLC 1,800, CEDAR LABS LLC 1,800, ALDER STUDIOS LLC 1,800, JUNIPER LOGISTICS LLC 650, EMBER CAPITAL INC 2,400, EMBER LOGISTICS INC 450, HARBOR LOGISTICS LLC 1,200, CEDAR STUDIOS INC 900, KESTREL SYSTEMS INC 2,400, IRIS HEALTH LLC 900, BIRCH LABS LLC 2,400, DUNE HEALTH CO 900, EMBER CAPITAL CO 2,400, FJORD HEALTH CO 450, BIRCH HEALTH CO 650, FJORD STUDIOS INC 450, DUNE FOODS CO 450) | $30,450.00 | `cash_receipts.csv` 24 items matched by date and amount, each applied to INV-2251..INV-2274 (total 30,450) |
| | **Total credits** | **$48,450.00** | |

All 24 March invoices are collected in full within the month. **Nothing was
applied to the opening A/R of $92,650.00** (third month running — U3).

## Debits — 8 items, all on the books

| Date | Bank description | Amount | Book reference |
|---|---|---:|---|
| 03/05 | ACH AWS | $10,160.00 | JE-2503-004 (6000) / JE-2503-010 |
| 03/06 | ACH WEWORK | $7,200.00 | JE-2503-005 (6100) / JE-2503-010 |
| 03/07 | ACH GUSTO FEES | $240.00 | JE-2503-006 (6200) / JE-2503-010 |
| 03/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2503-007 (6300) / JE-2503-010 |
| 03/09 | ACH HARBOR LAW LLP | $2,500.00 | JE-2503-008 (6600, new account) / JE-2503-010 |
| 03/10 | ACH GOOGLE ADS | $3,350.00 | JE-2503-009 (6400) / JE-2503-010 |
| 03/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2503-011 |
| 03/25 | ACH GUSTO TAX | $11,280.00 | JE-2503-013 |
| | **Total debits** | **$84,390.00** | |

Vendor debits agree to `vendor_bills.csv` amounts and dates 1:1. **No payment
against the opening A/P of $17,420.00** (third month running — U9).

## Payroll three-way tie (register ↔ books ↔ bank)

- Register (`payroll_register.json` 03/25): gross $54,404.00, net $48,200.00,
  employer taxes $5,076.00, remitted $11,280.00, 9 employees.
- Net pay: register $48,200.00 = book JE-2503-011 = bank GUSTO NET PAY 03/25 ✔
- Tax remit: register $11,280.00 = book JE-2503-013 = bank GUSTO TAX 03/25 ✔
- Withholding derived: $54,404.00 − $48,200.00 = $6,204.00 (U7); plus employer
  $5,076.00 = remit $11,280.00 ✔; account 2210 clears to zero cumulatively
  ($33,840.00 Dr = $33,840.00 Cr).
- Observation (U11, not re-asked): the March register is numerically identical
  to January and February for the **third consecutive month**. March ties to
  the bank like the prior months; the pattern is documented, not resolved.

## Reconciling items

None. No deposits in transit, no outstanding checks, no unrecorded bank items.
