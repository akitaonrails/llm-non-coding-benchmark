# Bank Reconciliation — June 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-06-01 through 2025-06-30
**Statement source:** `documents/month_06/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). All items below are matched
> against the June PDF statement.

## Summary

| | Amount |
|---|---:|
| Balance per bank statement, 2025-06-30 | **$227,450.00** |
| Balance per books, account 1000 (trial balance) | **$227,450.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unpaid debits | 0.00 |
| Bank items not on the books | 0.00 |
| Book items not at the bank | 0.00 |
| **Difference** | **$0.00** |

The books tie to the bank with **no adjusting entry needed this month**: every
one of the 33 June statement lines maps to a June journal entry.

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-05-31 | month_05 close / statement beginning balance | $260,300.00 |
| Customer receipts, 24 monthly ACHs (below) | JE-2506-003 | +$30,450.00 |
| Saltline Hospitality wire for INV-2349, 06/15 | JE-2506-004 | +$21,600.00 |
| Vendor ACH payments, 6 items (below) | JE-2506-011 | −$25,420.00 |
| Payroll net pay ACH, 06/25 | JE-2506-012 | −$48,200.00 |
| Payroll tax remit ACH, 06/25 | JE-2506-014 | −$11,280.00 |
| **Book cash 2025-06-30** | | **$227,450.00** |

$260,300.00 + $30,450.00 = $290,750.00
$290,750.00 + $21,600.00 = $312,350.00
$312,350.00 − $25,420.00 = $286,930.00
$286,930.00 − $48,200.00 = $238,730.00
$238,730.00 − $11,280.00 = **$227,450.00**

Trial balance account 1000 shows cumulative debits $772,500.00 (= $720,450.00
through May + $30,450.00 + $21,600.00 June receipts) and cumulative credits
$545,050.00 (= $460,150.00 through May + $25,420.00 + $48,200.00 + $11,280.00),
net **$227,450.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $260,300.00, total debits $84,900.00, total
credits $52,050.00, ending $227,450.00.
$260,300.00 + $52,050.00 − $84,900.00 = $227,450.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,520.00 + $7,200.00 + $240.00 + $1,460.00 + $2,500.00 +
$3,500.00 + $48,200.00 + $11,280.00 = $84,900.00 ✔ (8 debit lines)
Credits footing: $21,600.00 wire + 24 monthly ACHs $30,450.00 = $52,050.00 ✔
(25 credit lines; 33 transaction lines total)

## Credits on the statement — all 25 items identified

**Non-customer credits (1):**

| Date | Statement description | Amount | Booked as | Note |
|---|---|---:|---|---|
| 06/15 | WIRE IN SALTLINE HOSPITALITY | $21,600.00 | JE-2506-004: Dr 1000 / Cr 1100 (billing JE-2506-002 Dr 1100 / Cr 2200) | Applied to INV-2349 per `cash_receipts.csv`; new annual contract C-029 billed to deferred revenue, not income (policy #3) |

**Customer credits (24 monthly subscriptions, $30,450.00):** each matches a
`cash_receipts.csv` row by date + amount and invoice number INV-2325…INV-2348;
all 24 booked as revenue in one entry, JE-2506-003 (Dr 1000 / Cr 1100 against
the June billing JE-2506-001).

| Date | Payee per statement | Amount | Receipt row (customer / invoice) |
|---|---|---:|---|
| 06/20 | ACH CEDAR LOGISTICS INC | $450.00 | Cedar Logistics Inc — INV-2340 |
| 06/20 | ACH ALDER STUDIOS INC | $900.00 | Alder Studios Inc — INV-2342 |
| 06/20 | ACH KESTREL FOODS CO | $650.00 | Kestrel Foods Co — INV-2344 |
| 06/20 | ACH EMBER SYSTEMS INC | $450.00 | Ember Systems Inc — INV-2347 |
| 06/21 | ACH CEDAR LOGISTICS LLC | $1,800.00 | Cedar Logistics LLC — INV-2334 |
| 06/21 | ACH EMBER FOODS LLC | $1,800.00 | Ember Foods LLC — INV-2348 |
| 06/22 | ACH EMBER HEALTH CO | $2,400.00 | Ember Health Co — INV-2326 |
| 06/22 | ACH GRANITE SYSTEMS LLC | $1,800.00 | Granite Systems LLC — INV-2328 |
| 06/22 | ACH CEDAR LABS LLC | $1,800.00 | Cedar Labs LLC — INV-2333 |
| 06/22 | ACH ALDER STUDIOS LLC | $1,800.00 | Alder Studios LLC — INV-2336 |
| 06/23 | ACH JUNIPER LOGISTICS LLC | $650.00 | Juniper Logistics LLC — INV-2332 |
| 06/23 | ACH EMBER CAPITAL INC | $2,400.00 | Ember Capital Inc — INV-2335 |
| 06/23 | ACH EMBER LOGISTICS INC | $450.00 | Ember Logistics Inc — INV-2337 |
| 06/23 | ACH HARBOR LOGISTICS LLC | $1,200.00 | Harbor Logistics LLC — INV-2341 |
| 06/23 | ACH CEDAR STUDIOS INC | $900.00 | Cedar Studios Inc — INV-2345 |
| 06/24 | ACH KESTREL SYSTEMS INC | $2,400.00 | Kestrel Systems Inc — INV-2327 |
| 06/24 | ACH IRIS HEALTH LLC | $900.00 | Iris Health LLC — INV-2329 |
| 06/24 | ACH BIRCH LABS LLC | $2,400.00 | Birch Labs LLC — INV-2330 |
| 06/25 | ACH DUNE HEALTH CO | $900.00 | Dune Health Co — INV-2338 |
| 06/25 | ACH EMBER CAPITAL CO | $2,400.00 | Ember Capital Co — INV-2343 |
| 06/25 | ACH FJORD HEALTH CO | $450.00 | Fjord Health Co — INV-2346 |
| 06/26 | ACH BIRCH HEALTH CO | $650.00 | Birch Health Co — INV-2325 |
| 06/26 | ACH FJORD STUDIOS INC | $450.00 | Fjord Studios Inc — INV-2331 |
| 06/26 | ACH DUNE FOODS CO | $450.00 | Dune Foods Co — INV-2339 |
| | **Total monthly ACH credits** | **$30,450.00** | 24 rows |

Monthly ACH footing: $450+$900+$650+$450+$1,800+$1,800+$2,400+$1,800+$1,800+
$1,800+$650+$2,400+$450+$1,200+$900+$2,400+$900+$2,400+$900+$2,400+$450+$650+
$450+$450 = $30,450.00 ✔

Notes:
- Payee names again appear with entity-suffix variants (INC/CO/LLC); each is
  matched to its receipt row by date and amount. Same 24 customers and amounts
  as May. No unexplained credits.
- `cash_receipts.csv` total is $52,050.00 (24 monthly + Saltline $21,600.00),
  exactly equal to statement credits — no bank credits outside the receipts
  register this month.
- **No payment applied to the $92,650.00 opening (legacy) accounts
  receivable** — sixth consecutive month, carried as unknown U3.

## Debits on the statement — all 8 items identified

| Date | Description | Amount | Booked as | Expense account |
|---|---|---:|---|---|
| 06/05 | ACH DEBIT AWS | $10,520.00 | JE-2506-005 → paid JE-2506-011 | 6000 Hosting |
| 06/06 | ACH DEBIT WEWORK | $7,200.00 | JE-2506-006 → paid JE-2506-011 | 6100 Rent |
| 06/07 | ACH GUSTO FEES | $240.00 | JE-2506-007 → paid JE-2506-011 | 6200 G&A |
| 06/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2506-008 → paid JE-2506-011 | 6300 Software |
| 06/09 | ACH HARBOR LAW LLP | $2,500.00 | JE-2506-009 → paid JE-2506-011 | 6600 Professional fees |
| 06/10 | ACH GOOGLE ADS | $3,500.00 | JE-2506-010 → paid JE-2506-011 | 6400 Marketing |
| 06/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2506-012 | 5000 Salaries & Wages |
| 06/25 | ACH GUSTO TAX | $11,280.00 | JE-2506-014 | 2210 Payroll taxes payable (clearing) |
| | **Total statement debits** | **$84,900.00** | | |

$25,420.00 + $48,200.00 + $11,280.00 = $84,900.00 ✔

Notes:
- Six vendor ACHs match `vendor_bills.csv` 1:1 (dates and amounts). AWS
  $10,520.00 vs May $10,400.00 / April $10,280.00 and Google Ads $3,500.00 vs
  May $3,450.00 are usage/spend variances of the same recurring vendors —
  noted, not reconciling items.
- **Harbor Law LLP $2,500.00 (06/09)** is a new June bill documented in
  `vendor_bills.csv` and paid in-month. It is **not** a payment against the
  $17,420.00 opening accounts payable and **not** a repeat of the March
  Harbor Law $2,500.00 (paid 03/09, verified in May): each month's bill has
  its own line in that month's `vendor_bills.csv` and each was paid exactly
  once. The 03/09 → 06/09 cadence suggests a quarterly retainer; flagged as
  an observation in open_items.md.
- **Exactly one GUSTO NET PAY debit this month** — April's duplicate-debit
  pattern has not recurred since (U12/G1 closed).
- **No payment at the bank against the $17,420.00 opening accounts payable**
  (account 2000) — sixth consecutive month, carried as unknown U9.

## Payroll three-way tie — 06/25

| Level | Net pay | Tax remit |
|---|---:|---:|
| Payroll register (`payroll_register.json`, June) | $48,200.00 | $11,280.00 |
| Books (JE-2506-012 net pay; JE-2506-014 remit) | $48,200.00 | $11,280.00 |
| Bank statement (06/25 ACH lines) | $48,200.00 | $11,280.00 |

Agreement arithmetic: gross $54,404.00 − net $48,200.00 = withholding
$6,204.00; withholding $6,204.00 + employer taxes $5,076.00 = remit $11,280.00 ✔
Account 2210 clears cumulatively: Jan–Jun credits 6 × ($6,204.00 withheld +
$5,076.00 employer) = $67,680.00 equal Jan–Jun remit debits 6 × $11,280.00 =
$67,680.00; cumulative balance $0.00 ✔.

Register remains byte-identical to Feb–May (U11, sixth month): gross
$54,404.00, net $48,200.00, employer $5,076.00, remit $11,280.00, 9 employees.

## Reconciling items

**None.** Bank balance and book cash agree at $227,450.00 with no deposits in
transit, no outstanding debits, and no unrecorded bank items.
