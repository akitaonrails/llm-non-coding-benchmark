# Bank Reconciliation — August 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-08-01 through 2025-08-31
**Statement source:** `documents/month_08/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). Everything below is matched
> to the August PDF statement.

## Summary

| | Amount |
|---|---:|
| Bank statement balance, 2025-08-31 | **$123,040.00** |
| Book balance, account 1000 (trial balance) | **$123,040.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unposted debits | 0.00 |
| Bank items not on books | 0.00 |
| Book items not at bank | 0.00 |
| **Difference** | **$0.00** |

Books and bank tie **with no reconciling items again this month**: every one
of the 31 August statement lines (7 debits, 24 credits) maps to an August
journal entry.

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-07-31 | month_07 close / statement beginning balance | $175,330.00 |
| Customer receipts, 24 monthly ACHs (below) | JE-2508-002 | +$30,450.00 |
| Vendor ACH payments, 5 items (below) | JE-2508-008 | −$23,260.00 |
| Payroll net pay ACH, 08/25 | JE-2508-009 | −$48,200.00 |
| Payroll tax remit ACH, 08/25 | JE-2508-011 | −$11,280.00 |
| **Book cash 2025-08-31** | | **$123,040.00** |

$175,330.00 + $30,450.00 = $205,780.00
$205,780.00 − $23,260.00 = $182,520.00
$182,520.00 − $48,200.00 = $134,320.00
$134,320.00 − $11,280.00 = **$123,040.00**

Trial balance account 1000 shows cumulative debits $833,400.00 (= $802,950.00
through July + $30,450.00 August receipts) and cumulative credits $710,360.00
(= $627,620.00 through July + $23,260.00 + $48,200.00 + $11,280.00 August
payments), net **$123,040.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $175,330.00, total debits $82,740.00, total
credits $30,450.00, ending $123,040.00.
$175,330.00 + $30,450.00 − $82,740.00 = $123,040.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,760.00 + $7,200.00 + $240.00 + $1,460.00 + $3,600.00 +
$48,200.00 + $11,280.00 = $82,740.00 ✔ (7 debit lines)
Credits footing: 24 monthly ACHs $30,450.00 = $30,450.00 ✔ (24 credit lines;
31 transaction lines total)

## Credits on the statement — all 24 items identified

**Non-customer credits (0):** none this month — every credit is a customer
subscription ACH (contrast April/May Gusto refund credits and the June
Saltline wire).

**Customer credits (24 monthly subscriptions, $30,450.00):** each matches a
`cash_receipts.csv` row by date + amount and invoice number INV-2374…INV-2397;
all 24 booked in one entry, JE-2508-002 (Dr 1000 / Cr 1100 against the August
billing JE-2508-001).

| Date | Payee per statement | Amount | Receipt row (customer / invoice) |
|---|---|---:|---|
| 08/20 | ACH CEDAR LOGISTICS INC | $450.00 | Cedar Logistics Inc — INV-2389 |
| 08/20 | ACH ALDER STUDIOS INC | $900.00 | Alder Studios Inc — INV-2391 |
| 08/20 | ACH KESTREL FOODS CO | $650.00 | Kestrel Foods Co — INV-2393 |
| 08/20 | ACH EMBER SYSTEMS INC | $450.00 | Ember Systems Inc — INV-2396 |
| 08/21 | ACH CEDAR LOGISTICS LLC | $1,800.00 | Cedar Logistics LLC — INV-2383 |
| 08/21 | ACH EMBER FOODS LLC | $1,800.00 | Ember Foods LLC — INV-2397 |
| 08/22 | ACH EMBER HEALTH CO | $2,400.00 | Ember Health Co — INV-2375 |
| 08/22 | ACH GRANITE SYSTEMS LLC | $1,800.00 | Granite Systems LLC — INV-2377 |
| 08/22 | ACH CEDAR LABS LLC | $1,800.00 | Cedar Labs LLC — INV-2382 |
| 08/22 | ACH ALDER STUDIOS LLC | $1,800.00 | Alder Studios LLC — INV-2385 |
| 08/23 | ACH JUNIPER LOGISTICS LLC | $650.00 | Juniper Logistics LLC — INV-2381 |
| 08/23 | ACH EMBER CAPITAL INC | $2,400.00 | Ember Capital Inc — INV-2384 |
| 08/23 | ACH EMBER LOGISTICS INC | $450.00 | Ember Logistics Inc — INV-2386 |
| 08/23 | ACH HARBOR LOGISTICS LLC | $1,200.00 | Harbor Logistics LLC — INV-2390 |
| 08/23 | ACH CEDAR STUDIOS INC | $900.00 | Cedar Studios Inc — INV-2394 |
| 08/24 | ACH KESTREL SYSTEMS INC | $2,400.00 | Kestrel Systems Inc — INV-2376 |
| 08/24 | ACH IRIS HEALTH LLC | $900.00 | Iris Health LLC — INV-2378 |
| 08/24 | ACH BIRCH LABS LLC | $2,400.00 | Birch Labs LLC — INV-2379 |
| 08/25 | ACH DUNE HEALTH CO | $900.00 | Dune Health Co — INV-2387 |
| 08/25 | ACH EMBER CAPITAL CO | $2,400.00 | Ember Capital Co — INV-2392 |
| 08/25 | ACH FJORD HEALTH CO | $450.00 | Fjord Health Co — INV-2395 |
| 08/26 | ACH BIRCH HEALTH CO | $650.00 | Birch Health Co — INV-2374 |
| 08/26 | ACH FJORD STUDIOS INC | $450.00 | Fjord Studios Inc — INV-2380 |
| 08/26 | ACH DUNE FOODS CO | $450.00 | Dune Foods Co — INV-2388 |
| | **Total monthly ACH credits** | **$30,450.00** | 24 rows |

Monthly ACH footing: $450+$900+$650+$450+$1,800+$1,800+$2,400+$1,800+$1,800+$1,800+$650+$2,400+$450+$1,200+$900+$2,400+$900+$2,400+$900+$2,400+$450+$650+$450+$450 = $30,450.00 ✔

Notes:
- Payees match the receipt register exactly (no entity-suffix variants this
  month). Same 24 customers and amounts as June and July. No unexplained
  credits.
- **Timing observation, no accounting effect:** August receipts applied to
  **August** invoices (INV-2374…INV-2397, collected 08/20–08/26), whereas in
  prior months the receipts applied to the prior month's invoices. Both the
  billing and the collection fall in August either way, so entries and
  balances are unaffected.
- The 08/22 **ACH ALDER STUDIOS LLC $1,800.00** (INV-2385) is this customer's
  final monthly payment: C-012 cancelled effective 08/31
  (`email_cancellation_C-012.txt`) — no August adjustment, prospective-only
  impact (open_items.md item 1).
- Customer **Harbor Logistics LLC** (C-017, monthly subscriber, INV-2388) is a
  different party from vendor **Harbor Law LLP** (see debits note below).
- `cash_receipts.csv` total is $30,450.00, exactly equal to statement credits
  — no bank credits outside the receipts register this month.
- **No payment applied to the $92,650.00 opening (legacy) accounts
  receivable** — eighth consecutive month, carried as unknown U3.

## Debits on the statement — all 7 items identified

| Date | Description | Amount | Booked as | Expense account |
|---|---|---:|---|---|
| 08/05 | ACH AWS | $10,760.00 | JE-2508-03 → paid JE-2508-008 | 6000 Hosting |
| 08/06 | ACH WEWORK | $7,200.00 | JE-2508-04 → paid JE-2508-008 | 6100 Rent |
| 08/07 | ACH GUSTO FEES | $240.00 | JE-2508-05 → paid JE-2508-008 | 6200 G&A |
| 08/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2508-06 → paid JE-2508-008 | 6300 Software |
| 08/09 | ACH GOOGLE ADS | $3,600.00 | JE-2508-07 → paid JE-2508-008 | 6400 Marketing |
| 08/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2508-009 (Dr 5000 / Cr 2210 / Cr 1000 net) | 5000 Salaries (net pay) |
| 08/25 | ACH GUSTO TAX | $11,280.00 | JE-2508-011 (Dr 2210 / Cr 1000) | 2210 Payroll tax clearing |
| | **Total statement debits** | **$82,740.00** | | |

Debits regrouped: $23,260.00 vendor bills + $48,200.00 net pay + $11,280.00
tax remit = $82,740.00 ✔

Notes:
- The five vendor ACHs match `vendor_bills.csv` one-for-one (date and amount).
  AWS $10,760.00 continues its steady usage growth (+$120.00/month since
  February: 10,160 → 10,280 → 10,400 → 10,520 → 10,640 → 10,760); Google Ads
  $3,600.00 likewise (+$50.00: 3,350 → 3,400 → 3,450 → 3,500 → 3,550 → 3,600).
  Usage drift of the same vendors — noted, not reconciling items.
- **No Harbor Law LLP bill in August** — consistent with the observed quarterly
  cadence (03/09 → 06/09 → next expected September). August
  `vendor_bills.csv` carries no such bill, so nothing is unposted. Account
  6600 stays at $5,000.00 year-to-date. Observation flagged in open_items.md.
- **Exactly one GUSTO NET PAY debit this month** — the April duplicate-debit
  pattern has not recurred (U12/G1 remains closed).
- **No payments at bank against the $17,420.00 opening accounts payable**
  (account 2000) — eighth consecutive month, carried as unknown U9.

## Payroll three-way tie-out — 08/25

| Level | Net pay | Tax remittance |
|---|---:|---:|
| Payroll register (`payroll_register.json`, August) | $48,200.00 | $11,280.00 |
| Books (JE-2508-009 net pay; JE-2508-011 remit) | $48,200.00 | $11,280.00 |
| Bank statement (08/25 ACH lines) | $48,200.00 | $11,280.00 |

Reconciliation math: gross $54,404.00 − net $48,200.00 = withholding
$6,204.00; withholding $6,204.00 + employer taxes $5,076.00 = remittance
$11,280.00 ✔
Account 2210 clears cumulatively: credits Jan–Aug 8 × ($6,204.00 +
$5,076.00) = $90,240.00 equal debits Jan–Aug 8 × $11,280.00 = $90,240.00;
cumulative balance $0.00 ✔.

Register is again identical to Jan–Jul (U11, 8th month): gross $54,404.00,
net $48,200.00, employer $5,076.00, remit $11,280.00, 9 employees.

## Reconciling items

**None.** Bank and book cash agree at $123,040.00 with no deposits in transit,
no unposted debits, and no unrecorded bank items.
