# Bank Reconciliation — May 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-05-01 through 2025-05-31
**Statement source:** `documents/month_05/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). All items below are matched
> against the May PDF statement.

## Summary

| | Amount |
|---|---:|
| Balance per bank statement, 2025-05-31 | **$260,300.00** |
| Balance per books, account 1000 (trial balance) | **$260,300.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unpaid debits | 0.00 |
| Bank items not on the books | 0.00 |
| Book items not at the bank | 0.00 |
| **Difference** | **$0.00** |

The books tie to the bank with **no adjusting entry needed this month**: every
May statement line maps to a May journal entry, including the $48,200.00 Gusto
refund of April's duplicate net-pay debit (JE-2505-005), which clears the claim
receivable in account 1200 to zero. April's outstanding recovery (U12 / G1) is
**resolved** — cash verified.

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-04-30 | month_04 close / statement beginning balance | $233,880.00 |
| Customer receipts, 24 monthly ACHs (below) | JE-2505-003 | +$30,450.00 |
| Quarry Analytics wire for INV-2324, 05/15 | JE-2505-004 | +$30,000.00 |
| **Gusto refund of duplicate net-pay debit, 05/09 → clears claim 1200** | JE-2505-005 | +$48,200.00 |
| Vendor ACH payments, 5 items (below) | JE-2505-011 | −$22,750.00 |
| Payroll net pay ACH, 05/25 | JE-2505-012 | −$48,200.00 |
| Payroll tax remit ACH, 05/25 | JE-2505-014 | −$11,280.00 |
| **Book cash 2025-05-31** | | **$260,300.00** |

$233,880.00 + $30,450.00 = $264,330.00
$264,330.00 + $30,000.00 = $294,330.00
$294,330.00 + $48,200.00 = $342,530.00
$342,530.00 − $22,750.00 = $319,780.00
$319,780.00 − $48,200.00 − $11,280.00 = **$260,300.00**

Trial balance account 1000 shows cumulative debits $720,450.00 (= $611,800.00
through April + $30,450.00 + $30,000.00 + $48,200.00 May receipts) and
cumulative credits $460,150.00 (= $377,920.00 through April + $22,750.00 +
$48,200.00 + $11,280.00), net **$260,300.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $233,880.00, total debits $82,230.00, total
credits $108,650.00, ending $260,300.00.
$233,880.00 + $108,650.00 − $82,230.00 = $260,300.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,400.00 + $7,200.00 + $240.00 + $1,460.00 + $3,450.00 +
$48,200.00 + $11,280.00 = $82,230.00 ✔ (7 debit lines)
Credits footing: $48,200.00 refund + $30,000.00 wire + 24 monthly ACHs
$30,450.00 = $108,650.00 ✔ (26 credit lines; 33 transaction lines total)

## Credits on the statement — all 26 items identified

**Non-customer credits (2):**

| Date | Statement description | Amount | Booked as | Note |
|---|---|---:|---|---|
| 05/09 | ACH CREDIT GUSTO REFUND | $48,200.00 | JE-2505-005: Dr 1000 / Cr 1200 | Recovery of April's duplicate net-pay debit; clears claim account 1200 to $0.00. U12/G1 **resolved** |
| 05/15 | WIRE IN QUARRY ANALYTICS CO | $30,000.00 | JE-2505-004: Dr 1000 / Cr 2200 | Applied to INV-2324 per `cash_receipts.csv`; billed to deferred revenue, not income (policy #3) |

**Customer credits (24 monthly subscriptions, $30,450.00):** each matches a
`cash_receipts.csv` row by date + amount and invoice number INV-2300…INV-2323;
all 24 booked as revenue in one entry, JE-2505-003 (Dr 1000 / Cr 4000).

| Date | Payee per statement | Amount | Receipt row (customer / invoice) |
|---|---|---:|---|
| 05/20 | ACH CEDAR LOGISTICS INC | $450.00 | Cedar Logistics Inc — INV-2300 |
| 05/20 | ACH ALDER STUDIOS INC | $900.00 | Alder Studios Inc — INV-2301 |
| 05/20 | ACH KESTREL FOODS CO | $650.00 | Kestrel Foods Co — INV-2302 |
| 05/20 | ACH EMBER SYSTEMS INC | $450.00 | Ember Systems Inc — INV-2303 |
| 05/21 | ACH CEDAR LOGISTICS LLC | $1,800.00 | Cedar Logistics LLC — INV-2304 |
| 05/21 | ACH EMBER FOODS LLC | $1,800.00 | Ember Foods LLC — INV-2305 |
| 05/22 | ACH EMBER HEALTH CO | $2,400.00 | Ember Health Co — INV-2306 |
| 05/22 | ACH GRANITE SYSTEMS LLC | $1,800.00 | Granite Systems LLC — INV-2307 |
| 05/22 | ACH CEDAR LABS LLC | $1,800.00 | Cedar Labs LLC — INV-2308 |
| 05/22 | ACH ALDER STUDIOS LLC | $1,800.00 | Alder Studios LLC — INV-2309 |
| 05/23 | ACH JUNIPER LOGISTICS LLC | $650.00 | Juniper Logistics LLC — INV-2310 |
| 05/23 | ACH EMBER CAPITAL INC | $2,400.00 | Ember Capital Inc — INV-2311 |
| 05/23 | ACH EMBER LOGISTICS INC | $450.00 | Ember Logistics Inc — INV-2312 |
| 05/23 | ACH HARBOR LOGISTICS LLC | $1,200.00 | Harbor Logistics LLC — INV-2313 |
| 05/23 | ACH CEDAR STUDIOS INC | $900.00 | Cedar Studios Inc — INV-2314 |
| 05/24 | ACH KESTREL SYSTEMS INC | $2,400.00 | Kestrel Systems Inc — INV-2315 |
| 05/24 | ACH IRIS HEALTH LLC | $900.00 | Iris Health LLC — INV-2316 |
| 05/24 | ACH BIRCH LABS LLC | $2,400.00 | Birch Labs LLC — INV-2317 |
| 05/25 | ACH DUNE HEALTH CO | $900.00 | Dune Health Co — INV-2318 |
| 05/25 | ACH EMBER CAPITAL CO | $2,400.00 | Ember Capital Co — INV-2319 |
| 05/25 | ACH FJORD HEALTH CO | $450.00 | Fjord Health Co — INV-2320 |
| 05/26 | ACH BIRCH HEALTH CO | $650.00 | Birch Health Co — INV-2321 |
| 05/26 | ACH FJORD STUDIOS INC | $450.00 | Fjord Studios Inc — INV-2322 |
| 05/26 | ACH DUNE FOODS CO | $450.00 | Dune Foods Co — INV-2323 |
| | **Total monthly ACH credits** | **$30,450.00** | 24 rows |

Monthly ACH footing: $450+$900+$650+$450+$1,800+$1,800+$2,400+$1,800+$1,800+
$1,800+$650+$2,400+$450+$1,200+$900+$2,400+$900+$2,400+$900+$2,400+$450+$650+
$450+$450 = $30,450.00 ✔

Notes:
- Payee names again appear with entity-suffix variants (INC/CO/LLC); each is
  matched to its receipt row by date and amount. No unexplained credits.
- **No payment applied to the $92,650.00 opening (legacy) accounts
  receivable** — fifth consecutive month, carried as unknown U3.

## Debits on the statement — all 7 items identified

| Date | Description | Amount | Booked as | Expense account |
|---|---|---:|---|---|
| 05/05 | ACH DEBIT AWS | $10,400.00 | JE-2505-006 → paid JE-2505-011 | 6000 Hosting |
| 05/06 | ACH DEBIT WEWORK | $7,200.00 | JE-2505-007 → paid JE-2505-011 | 6100 Rent |
| 05/07 | ACH GUSTO FEES | $240.00 | JE-2505-008 → paid JE-2505-011 | 6200 G&A |
| 05/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2505-009 → paid JE-2505-011 | 6300 Software |
| 05/09 | ACH GOOGLE ADS | $3,450.00 | JE-2505-010 → paid JE-2505-011 | 6400 Marketing |
| 05/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2505-012 | 5000 Salaries & Wages |
| 05/25 | ACH GUSTO TAX | $11,280.00 | JE-2505-014 | 2210 Payroll taxes payable (clearing) |
| | **Total statement debits** | **$82,230.00** | | |

$22,750.00 + $48,200.00 + $11,280.00 = $82,230.00 ✔

Notes:
- Five vendor ACHs match `vendor_bills.csv` 1:1 (dates and amounts). AWS
  $10,400.00 vs April $10,280.00 and Google Ads $3,450.00 vs April $3,400.00
  are usage/spend variances of the same recurring vendors — noted, not
  reconciling items.
- **Exactly one GUSTO NET PAY debit this month** — April's duplicate-debit
  pattern did not recur (see below).
- No Harbor Law ACH in May: nothing was billed by Harbor Law in May, and the
  March invoice was already paid in March ($2,500.00 ACH 03/09 on the March
  statement, verified this month).
- **No payment at the bank against the $17,420.00 opening accounts payable**
  (account 2000) — fifth consecutive month, carried as unknown U9.

## Payroll three-way tie — 05/25

| Level | Net pay | Tax remit |
|---|---:|---:|
| Payroll register (`payroll_register.json`, May) | $48,200.00 | $11,280.00 |
| Books (JE-2505-012 net pay; JE-2505-014 remit) | $48,200.00 | $11,280.00 |
| Bank statement (05/25 ACH lines) | $48,200.00 | $11,280.00 |

Agreement arithmetic: gross $54,404.00 − net $48,200.00 = withholding
$6,204.00; withholding $6,204.00 + employer taxes $5,076.00 = remit $11,280.00 ✔
Account 2210 clears cumulatively: Jan–May credits 5 × ($6,204.00 withheld +
$5,076.00 employer) = $56,400.00 equal Jan–May remit debits 5 × $11,280.00 =
$56,400.00; cumulative balance $0.00 ✔.

Register remains byte-identical to Feb–Apr (U11, fifth month). April's
duplicate $48,200.00 net-pay debit (04/26) did **not** repeat in May; the
May statement carries a single net-pay debit, and the April duplicate was
returned by Gusto on 05/09 and booked as JE-2505-005.

## Reconciling items

**None.** Bank balance and book cash agree at $260,300.00 with no deposits in
transit, no outstanding debits, and no unrecorded bank items. The Gusto refund
was both received (05/09) and recorded in the same period, so no timing item
remains.
