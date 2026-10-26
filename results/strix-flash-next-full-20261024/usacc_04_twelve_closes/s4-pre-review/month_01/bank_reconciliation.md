# Bank Reconciliation — January 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-01-01 through 2025-01-31
**Statement source:** `documents/month_01/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was **not** used: its transactions are dated December 2025
> and its balances are negative, so it cannot be the January 2025 statement.
> It is flagged to the client (`open_items.md` item 8). All items below are
> matched against the PDF statement.

## Summary

| | Amount |
|---|---:|
| Balance per bank statement, 2025-01-31 | **$384,900.00** |
| Balance per books, account 1000 (trial balance) | **$384,900.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unpaid debits | 0.00 |
| Bank items not on the books | 0.00 |
| Book items not at the bank | 0.00 |
| **Difference** | **$0.00** |

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2024-12-31 | opening_trial_balance.csv | $412,000.00 |
| Customer receipts, 25 items (all cleared, below) | JE-2501-003 | +$54,450.00 |
| Vendor ACH payments, 5 items (below) | JE-2501-009 | −$22,070.00 |
| Payroll net pay ACH, 01/25 | JE-2501-010 | −$48,200.00 |
| Payroll tax remit ACH, 01/25 | JE-2501-012 | −$11,280.00 |
| **Book cash 2025-01-31** | | **$384,900.00** |

$412,000.00 + $54,450.00 = $466,450.00
$466,450.00 − $22,070.00 − $48,200.00 − $11,280.00 = **$384,900.00**

Trial balance account 1000 shows debits $466,450.00 (= $412,000.00 opening +
$54,450.00 receipts) and credits $81,550.00 (= $22,070.00 + $48,200.00 +
$11,280.00), net **$384,900.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $412,000.00, total debits $81,550.00, total credits
$54,450.00, ending $384,900.00.
$412,000.00 + $54,450.00 − $81,550.00 = $384,900.00 ✔ (matches the footer and
the running-balance column line by line).

Because every bank credit is a booked receipt and every bank debit is a booked
payment, and every book cash movement appears on the statement, there are **no
deposits in transit and no outstanding items at 01/31**.

## Credits matched — 25 bank deposits ↔ 25 receipts (cash_receipts.csv)

The customer list contains near-identical names (Cedar Logistics Inc vs Cedar
Logistics LLC, Alder Studios Inc vs LLC, Ember Capital Inc vs Co, Kestrel
Foods vs Kestrel Systems, Dune Health vs Dune Foods, several "Ember"
entities). Matching was done on **date + amount + payee name**; each receipt
matched exactly one bank credit.

| Bank date | Bank description | Amount | Receipt (cash_receipts.csv) | Applied to |
|---|---|---:|---|---|
| 01/15 | WIRE IN TRESTLE FREIGHT LLC | 24,000.00 | 01/15 Trestle Freight LLC | INV-2225 |
| 01/20 | ACH CEDAR LOGISTICS INC | 450.00 | 01/20 Cedar Logistics Inc | INV-2216 |
| 01/20 | ACH ALDER STUDIOS INC | 900.00 | 01/20 Alder Studios Inc | INV-2218 |
| 01/20 | ACH KESTREL FOODS CO | 650.00 | 01/20 Kestrel Foods Co | INV-2220 |
| 01/20 | ACH EMBER SYSTEMS INC | 450.00 | 01/20 Ember Systems Inc | INV-2223 |
| 01/21 | ACH CEDAR LOGISTICS LLC | 1,800.00 | 01/21 Cedar Logistics LLC | INV-2210 |
| 01/21 | ACH EMBER FOODS LLC | 1,800.00 | 01/21 Ember Foods LLC | INV-2224 |
| 01/22 | ACH EMBER HEALTH CO | 2,400.00 | 01/22 Ember Health Co | INV-2202 |
| 01/22 | ACH GRANITE SYSTEMS LLC | 1,800.00 | 01/22 Granite Systems LLC | INV-2204 |
| 01/22 | ACH CEDAR LABS LLC | 1,800.00 | 01/22 Cedar Labs LLC | INV-2209 |
| 01/22 | ACH ALDER STUDIOS LLC | 1,800.00 | 01/22 Alder Studios LLC | INV-2212 |
| 01/23 | ACH JUNIPER LOGISTICS LLC | 650.00 | 01/23 Juniper Logistics LLC | INV-2208 |
| 01/23 | ACH EMBER CAPITAL INC | 2,400.00 | 01/23 Ember Capital Inc | INV-2211 |
| 01/23 | ACH EMBER LOGISTICS INC | 450.00 | 01/23 Ember Logistics Inc | INV-2213 |
| 01/23 | ACH HARBOR LOGISTICS LLC | 1,200.00 | 01/23 Harbor Logistics LLC | INV-2217 |
| 01/23 | ACH CEDAR STUDIOS INC | 900.00 | 01/23 Cedar Studios Inc | INV-2221 |
| 01/24 | ACH KESTREL SYSTEMS INC | 2,400.00 | 01/24 Kestrel Systems Inc | INV-2203 |
| 01/24 | ACH IRIS HEALTH LLC | 900.00 | 01/24 Iris Health LLC | INV-2205 |
| 01/24 | ACH BIRCH LABS LLC | 2,400.00 | 01/24 Birch Labs LLC | INV-2206 |
| 01/25 | ACH DUNE HEALTH CO | 900.00 | 01/25 Dune Health Co | INV-2214 |
| 01/25 | ACH EMBER CAPITAL CO | 2,400.00 | 01/25 Ember Capital Co | INV-2219 |
| 01/25 | ACH FJORD HEALTH CO | 450.00 | 01/25 Fjord Health Co | INV-2222 |
| 01/26 | ACH BIRCH HEALTH CO | 650.00 | 01/26 Birch Health Co | INV-2201 |
| 01/26 | ACH FJORD STUDIOS INC | 450.00 | 01/26 Fjord Studios Inc | INV-2207 |
| 01/26 | ACH DUNE FOODS CO | 450.00 | 01/26 Dune Foods Co | INV-2215 |
| | **Total credits** | **$54,450.00** | | |

Subtotal check: 24 monthly deposits = $30,450.00 (ties to the 24 invoices in
`invoices.csv`, INV-2201..INV-2224) + Trestle wire $24,000.00 (INV-2225) =
$54,450.00 ✔. Every receipt was applied to a January invoice; **no receipt was
applied against the opening A/R balance of $92,650.00** (see
`open_items.md` item 2).

## Debits matched — 7 bank debits

| Bank date | Bank description | Amount | Matched to | Entry |
|---|---|---:|---|---|
| 01/05 | ACH AWS | 9,920.00 | vendor_bills.csv 01/05 AWS $9,920.00 | JE-2501-004, paid in JE-2501-009 |
| 01/06 | ACH WEWORK | 7,200.00 | vendor_bills.csv 01/06 WeWork $7,200.00 | JE-2501-005, paid in JE-2501-009 |
| 01/07 | ACH GUSTO FEES | 240.00 | vendor_bills.csv 01/07 Gusto fees $240.00 | JE-2501-006, paid in JE-2501-009 |
| 01/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 | vendor_bills.csv 01/08 $1,460.00 | JE-2501-007, paid in JE-2501-009 |
| 01/09 | ACH GOOGLE ADS | 3,250.00 | vendor_bills.csv 01/09 Google Ads $3,250.00 | JE-2501-008, paid in JE-2501-009 |
| 01/25 | ACH GUSTO NET PAY | 48,200.00 | payroll_register.json net_pay 48,200.00 | JE-2501-010 |
| 01/25 | ACH GUSTO TAX | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 | JE-2501-012 |
| | **Total debits** | **$81,550.00** | ties to statement footer ✔ | |

$22,070.00 + $48,200.00 + $11,280.00 = $81,550.00 ✔

## Payroll three-way tie (register ↔ books ↔ bank)

| Check | Register | Bank | Agrees |
|---|---:|---:|---|
| Net pay | 48,200.00 | 48,200.00 (GUSTO NET PAY 01/25) | ✔ |
| Gross pay | 54,404.00 | — | — |
| Withholding (derived) | 54,404.00 − 48,200.00 = 6,204.00 | — | — |
| Employer taxes & benefits | 5,076.00 | — | — |
| Tax remittance | 11,280.00 | 11,280.00 (GUSTO TAX 01/25) | ✔ |
| Components check | 6,204.00 + 5,076.00 = 11,280.00 | | ✔ |

Payroll agrees to the register **and** the bank with no forced plug. 2210
payroll taxes payable cleared to zero ($6,204.00 + $5,076.00 credited,
$11,280.00 paid).

## Opening cash caveat

Opening bank balance $412,000.00 was taken from the client opening trial
balance; no December 2024 bank statement was provided to verify it (see
`open_items.md` item 9 and `QUESTIONS.md`).
