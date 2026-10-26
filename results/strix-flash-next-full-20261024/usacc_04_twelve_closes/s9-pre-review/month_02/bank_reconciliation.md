# Bank Reconciliation — February 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-02-01 through 2025-02-28
**Statement source:** `documents/month_02/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). All items below are matched
> against the February PDF statement.

## Summary

| | Amount |
|---|---:|
| Balance per bank statement, 2025-02-28 | **$369,630.00** |
| Balance per books, account 1000 (trial balance) | **$369,630.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unpaid debits | 0.00 |
| Bank items not on the books | 0.00 |
| Book items not at the bank | 0.00 |
| **Difference** | **$0.00** |

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-01-31 | month_01 close / statement beginning balance | $384,900.00 |
| Customer receipts, 25 items (all cleared, below) | JE-2502-003 | +$66,450.00 |
| Vendor ACH payments, 5 items (below) | JE-2502-009 | −$22,240.00 |
| Payroll net pay ACH, 02/25 | JE-2502-010 | −$48,200.00 |
| Payroll tax remit ACH, 02/25 | JE-2502-012 | −$11,280.00 |
| **Book cash 2025-02-28** | | **$369,630.00** |

$384,900.00 + $66,450.00 = $451,350.00
$451,350.00 − $22,240.00 − $48,200.00 − $11,280.00 = **$369,630.00**

Trial balance account 1000 shows cumulative debits $532,900.00 (= $466,450.00
through January + $66,450.00 February receipts) and cumulative credits
$163,270.00 (= $81,550.00 through January + $22,240.00 + $48,200.00 +
$11,280.00), net **$369,630.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $384,900.00, total debits $81,720.00, total credits
$66,450.00, ending $369,630.00.
$384,900.00 + $66,450.00 − $81,720.00 = $369,630.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,040.00 + $7,200.00 + $240.00 + $1,460.00 + $3,300.00 +
$48,200.00 + $11,280.00 = $81,720.00 ✔
Credits footing: 24 monthly ACHs $30,450.00 + Pinecone wire $36,000.00 =
$66,450.00 ✔

Because every bank credit is a booked receipt and every bank debit is a booked
payment, and every book cash movement appears on the statement, there are **no
deposits in transit and no outstanding items at 02/28**.

## Credits matched — 25 bank deposits ↔ 25 receipts (cash_receipts.csv)

The customer list again contains near-identical names (Cedar Logistics Inc vs
Cedar Logistics LLC, Alder Studios Inc vs LLC, Ember Capital Inc vs Co, Kestrel
Foods vs Kestrel Systems, Dune Health vs Dune Foods, several "Ember" entities).
Matching was done on **date + amount + payee name**; each receipt matched
exactly one bank credit, one-to-one, no residuals on either side.

| Bank date | Bank description | Amount | Receipt (cash_receipts.csv) | Applied to |
|---|---|---:|---|---|
| 02/15 | WIRE IN PINECONE DENTAL GROUP | 36,000.00 | 02/15 Pinecone Dental Group | INV-2250 |
| 02/20 | ACH CEDAR LOGISTICS INC | 450.00 | 02/20 Cedar Logistics Inc | INV-2241 |
| 02/20 | ACH ALDER STUDIOS INC | 900.00 | 02/20 Alder Studios Inc | INV-2243 |
| 02/20 | ACH KESTREL FOODS CO | 650.00 | 02/20 Kestrel Foods Co | INV-2245 |
| 02/20 | ACH EMBER SYSTEMS INC | 450.00 | 02/20 Ember Systems Inc | INV-2248 |
| 02/21 | ACH CEDAR LOGISTICS LLC | 1,800.00 | 02/21 Cedar Logistics LLC | INV-2235 |
| 02/21 | ACH EMBER FOODS LLC | 1,800.00 | 02/21 Ember Foods LLC | INV-2249 |
| 02/22 | ACH EMBER HEALTH CO | 2,400.00 | 02/22 Ember Health Co | INV-2227 |
| 02/22 | ACH GRANITE SYSTEMS LLC | 1,800.00 | 02/22 Granite Systems LLC | INV-2229 |
| 02/22 | ACH CEDAR LABS LLC | 1,800.00 | 02/22 Cedar Labs LLC | INV-2234 |
| 02/22 | ACH ALDER STUDIOS LLC | 1,800.00 | 02/22 Alder Studios LLC | INV-2237 |
| 02/23 | ACH JUNIPER LOGISTICS LLC | 650.00 | 02/23 Juniper Logistics LLC | INV-2233 |
| 02/23 | ACH EMBER CAPITAL INC | 2,400.00 | 02/23 Ember Capital Inc | INV-2236 |
| 02/23 | ACH EMBER LOGISTICS INC | 450.00 | 02/23 Ember Logistics Inc | INV-2238 |
| 02/23 | ACH HARBOR LOGISTICS LLC | 1,200.00 | 02/23 Harbor Logistics LLC | INV-2242 |
| 02/23 | ACH CEDAR STUDIOS INC | 900.00 | 02/23 Cedar Studios Inc | INV-2246 |
| 02/24 | ACH KESTREL SYSTEMS INC | 2,400.00 | 02/24 Kestrel Systems Inc | INV-2228 |
| 02/24 | ACH IRIS HEALTH LLC | 900.00 | 02/24 Iris Health LLC | INV-2230 |
| 02/24 | ACH BIRCH LABS LLC | 2,400.00 | 02/24 Birch Labs LLC | INV-2231 |
| 02/25 | ACH DUNE HEALTH CO | 900.00 | 02/25 Dune Health Co | INV-2239 |
| 02/25 | ACH EMBER CAPITAL CO | 2,400.00 | 02/25 Ember Capital Co | INV-2244 |
| 02/25 | ACH FJORD HEALTH CO | 450.00 | 02/25 Fjord Health Co | INV-2247 |
| 02/26 | ACH BIRCH HEALTH CO | 650.00 | 02/26 Birch Health Co | INV-2226 |
| 02/26 | ACH FJORD STUDIOS INC | 450.00 | 02/26 Fjord Studios Inc | INV-2232 |
| 02/26 | ACH DUNE FOODS CO | 450.00 | 02/26 Dune Foods Co | INV-2240 |
| | **Total credits** | **$66,450.00** | | |

Subtotal check: 24 monthly deposits = $30,450.00 (ties to the 24 monthly
invoices in `invoices.csv`, INV-2226..INV-2249) + Pinecone wire $36,000.00
(INV-2250) = $66,450.00 ✔. **No receipt was applied against the opening A/R
balance of $92,650.00** for the second consecutive month (see `open_items.md`
item 2, unknown U3). The Pinecone receipt collected a billed advance; it did
not transfer revenue — the $36,000 sits in 2200 (JE-2502-002).

## Debits matched — 7 bank debits

| Bank date | Bank description | Amount | Matched to | Entry |
|---|---|---:|---|---|
| 02/05 | ACH AWS | 10,040.00 | vendor_bills.csv 02/05 AWS $10,040.00 | JE-2502-004, paid in JE-2502-009 |
| 02/06 | ACH WEWORK | 7,200.00 | vendor_bills.csv 02/06 WeWork $7,200.00 | JE-2502-005, paid in JE-2502-009 |
| 02/07 | ACH GUSTO FEES | 240.00 | vendor_bills.csv 02/07 Gusto fees $240.00 | JE-2502-006, paid in JE-2502-009 |
| 02/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 | vendor_bills.csv 02/08 $1,460.00 | JE-2502-007, paid in JE-2502-009 |
| 02/09 | ACH GOOGLE ADS | 3,300.00 | vendor_bills.csv 02/09 Google Ads $3,300.00 | JE-2502-008, paid in JE-2502-009 |
| 02/25 | ACH GUSTO NET PAY | 48,200.00 | payroll_register.json net_pay 48,200.00 | JE-2502-010 |
| 02/25 | ACH GUSTO TAX | 11,280.00 | payroll_register.json taxes_remitted 11,280.00 | JE-2502-012 |
| | **Total debits** | **$81,720.00** | ties to statement footer ✔ | |

$22,240.00 + $48,200.00 + $11,280.00 = $81,720.00 ✔

## Payroll three-way tie (register ↔ books ↔ bank)

| Check | Register | Bank | Agrees |
|---|---:|---:|---|
| Net pay | 48,200.00 | 48,200.00 (GUSTO NET PAY 02/25) | ✔ |
| Gross pay | 54,404.00 | — | — |
| Withholding (derived) | 54,404.00 − 48,200.00 = 6,204.00 | — | — |
| Employer taxes & benefits | 5,076.00 | — | — |
| Tax remittance | 11,280.00 | 11,280.00 (GUSTO TAX 02/25) | ✔ |
| Components check | 6,204.00 + 5,076.00 = 11,280.00 | | ✔ |

February's register is numerically identical to January's (gross 54,404, net
48,200, employer 5,076, remit 11,280, 9 employees) — noted in
`open_items.md` item 5, not assumed wrong absent evidence. Payroll agrees to
the register **and** the bank with no forced plug. 2210 payroll taxes payable:
February activity cleared to zero (6,204.00 + 5,076.00 credited, 11,280.00
paid); cumulative TB 2210 debits = credits = 22,560.00.

## Opening cash caveat

Opening bank balance $384,900.00 agrees with the January statement's ending
balance and our January book close ✔. Opening cash/AP as of 12/31/2024 remain
client-asserted, not independently verified (unknown U9).
