# Bank Reconciliation — July 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-07-01 through 2025-07-31
**Statement source:** `documents/month_07/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). Everything below is matched
> to the July PDF statement.

## Summary

| | Amount |
|---|---:|
| Bank statement balance, 2025-07-31 | **$175,330.00** |
| Book balance, account 1000 (trial balance) | **$175,330.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unposted debits | 0.00 |
| Bank items not on books | 0.00 |
| Book items not at bank | 0.00 |
| **Difference** | **$0.00** |

Books and bank tie **with no reconciling items this month**: every one of the
31 July statement lines (7 debits, 24 credits) maps to a July journal entry.

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-06-30 | month_06 close / statement beginning balance | $227,450.00 |
| Customer receipts, 24 monthly ACHs (below) | JE-2507-002 | +$30,450.00 |
| Vendor ACH payments, 5 items (below) | JE-2507-008 | −$23,090.00 |
| Payroll net pay ACH, 07/25 | JE-2507-009 | −$48,200.00 |
| Payroll tax remit ACH, 07/25 | JE-2507-011 | −$11,280.00 |
| **Book cash 2025-07-31** | | **$175,330.00** |

$227,450.00 + $30,450.00 = $257,900.00
$257,900.00 − $23,090.00 = $234,810.00
$234,810.00 − $48,200.00 = $186,610.00
$186,610.00 − $11,280.00 = **$175,330.00**

Trial balance account 1000 shows cumulative debits $802,950.00 (= $772,500.00
through June + $30,450.00 July receipts) and cumulative credits $627,620.00
(= $545,050.00 through June + $23,090.00 + $48,200.00 + $11,280.00 July
payments), net **$175,330.00** debit — agrees with the buildup.

## Statement internal check

Statement footer: beginning $227,450.00, total debits $82,570.00, total
credits $30,450.00, ending $175,330.00.
$227,450.00 + $30,450.00 − $82,570.00 = $175,330.00 ✔ (matches the footer and
the running-balance column line by line).
Debits footing: $10,640.00 + $7,200.00 + $240.00 + $1,460.00 + $3,550.00 +
$48,200.00 + $11,280.00 = $82,570.00 ✔ (7 debit lines)
Credits footing: 24 monthly ACHs $30,450.00 = $30,450.00 ✔ (24 credit lines;
31 transaction lines total)

## Credits on the statement — all 24 items identified

**Non-customer credits (0):** none this month — every credit is a customer
subscription ACH (contrast April/May Gusto refund credits and the June
Saltline wire).

**Customer credits (24 monthly subscriptions, $30,450.00):** each matches a
`cash_receipts.csv` row by date + amount and invoice number INV-2350…INV-2373;
all 24 booked in one entry, JE-2507-002 (Dr 1000 / Cr 1100 against the July
billing JE-2507-001).

| Date | Payee per statement | Amount | Receipt row (customer / invoice) |
|---|---|---:|---|
| 07/20 | ACH CEDAR LOGISTICS INC | $450.00 | Cedar Logistics Inc — INV-2365 |
| 07/20 | ACH ALDER STUDIOS INC | $900.00 | Alder Studios Inc — INV-2367 |
| 07/20 | ACH KESTREL FOODS CO | $650.00 | Kestrel Foods Co — INV-2369 |
| 07/20 | ACH EMBER SYSTEMS INC | $450.00 | Ember Systems Inc — INV-2372 |
| 07/21 | ACH CEDAR LOGISTICS LLC | $1,800.00 | Cedar Logistics LLC — INV-2359 |
| 07/21 | ACH EMBER FOODS LLC | $1,800.00 | Ember Foods LLC — INV-2373 |
| 07/22 | ACH EMBER HEALTH CO | $2,400.00 | Ember Health Co — INV-2351 |
| 07/22 | ACH GRANITE SYSTEMS LLC | $1,800.00 | Granite Systems LLC — INV-2353 |
| 07/22 | ACH CEDAR LABS LLC | $1,800.00 | Cedar Labs LLC — INV-2358 |
| 07/22 | ACH ALDER STUDIOS LLC | $1,800.00 | Alder Studios LLC — INV-2361 |
| 07/23 | ACH JUNIPER LOGISTICS LLC | $650.00 | Juniper Logistics LLC — INV-2357 |
| 07/23 | ACH EMBER CAPITAL INC | $2,400.00 | Ember Capital Inc — INV-2360 |
| 07/23 | ACH EMBER LOGISTICS INC | $450.00 | Ember Logistics Inc — INV-2362 |
| 07/23 | ACH HARBOR LOGISTICS LLC | $1,200.00 | Harbor Logistics LLC — INV-2366 |
| 07/23 | ACH CEDAR STUDIOS INC | $900.00 | Cedar Studios Inc — INV-2370 |
| 07/24 | ACH KESTREL SYSTEMS INC | $2,400.00 | Kestrel Systems Inc — INV-2352 |
| 07/24 | ACH IRIS HEALTH LLC | $900.00 | Iris Health LLC — INV-2354 |
| 07/24 | ACH BIRCH LABS LLC | $2,400.00 | Birch Labs LLC — INV-2355 |
| 07/25 | ACH DUNE HEALTH CO | $900.00 | Dune Health Co — INV-2363 |
| 07/25 | ACH EMBER CAPITAL CO | $2,400.00 | Ember Capital Co — INV-2368 |
| 07/25 | ACH FJORD HEALTH CO | $450.00 | Fjord Health Co — INV-2371 |
| 07/26 | ACH BIRCH HEALTH CO | $650.00 | Birch Health Co — INV-2350 |
| 07/26 | ACH FJORD STUDIOS INC | $450.00 | Fjord Studios Inc — INV-2356 |
| 07/26 | ACH DUNE FOODS CO | $450.00 | Dune Foods Co — INV-2364 |
| | **Total monthly ACH credits** | **$30,450.00** | 24 rows |

Monthly ACH footing: $450+$900+$650+$450+$1,800+$1,800+$2,400+$1,800+$1,800+$1,800+$650+$2,400+$450+$1,200+$900+$2,400+$900+$2,400+$900+$2,400+$450+$650+$450+$450 = $30,450.00 ✔

Notes:
- Payee names again appear with entity-suffix variants (INC/CO/LLC); each is
  matched to its receipt row by date and amount. Same 24 customers and amounts
  as June. No unexplained credits.
- Customer **Harbor Logistics LLC** (C-017, monthly subscriber, INV-2366) is a
  different party from vendor **Harbor Law LLP** (see debits note below).
- `cash_receipts.csv` total is $30,450.00, exactly equal to statement credits
  — no bank credits outside the receipts register this month.
- **No payment applied to the $92,650.00 opening (legacy) accounts
  receivable** — seventh consecutive month, carried as unknown U3.

## Debits on the statement — all 7 items identified

| Date | Description | Amount | Booked as | Expense account |
|---|---|---:|---|---|
| 07/05 | ACH AWS | $10,640.00 | JE-2507-003 → paid JE-2507-008 | 6000 Hosting |
| 07/06 | ACH WEWORK | $7,200.00 | JE-2507-004 → paid JE-2507-008 | 6100 Rent |
| 07/07 | ACH GUSTO FEES | $240.00 | JE-2507-005 → paid JE-2507-008 | 6200 G&A |
| 07/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2507-006 → paid JE-2507-008 | 6300 Software |
| 07/09 | ACH GOOGLE ADS | $3,550.00 | JE-2507-007 → paid JE-2507-008 | 6400 Marketing |
| 07/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2507-009 (Dr 5000 / Cr 2210 / Cr 1000 net) | 5000 Salaries (net pay) |
| 07/25 | ACH GUSTO TAX | $11,280.00 | JE-2507-011 (Dr 2210 / Cr 1000) | 2210 Payroll tax clearing |
| | **Total statement debits** | **$82,570.00** | | |

Debits regrouped: $23,090.00 vendor bills + $48,200.00 net pay + $11,280.00
tax remit = $82,570.00 ✔

Notes:
- The five vendor ACHs match `vendor_bills.csv` one-for-one (date and amount).
  AWS $10,640.00 continues its steady usage growth (+$120.00/month since
  February: 10,160 → 10,280 → 10,400 → 10,520 → 10,640); Google Ads
  $3,550.00 likewise (+$50.00: 3,350 → 3,400 → 3,450 → 3,500 → 3,550).
  Usage drift of the same vendors — noted, not reconciling items.
- **No Harbor Law LLP bill in July** — consistent with the observed quarterly
  cadence (03/09 → 06/09 → next expected September). July
  `vendor_bills.csv` carries no such bill, so nothing is unposted. Account
  6600 stays at $5,000.00 year-to-date. Observation flagged in open_items.md.
- **Exactly one GUSTO NET PAY debit this month** — the April duplicate-debit
  pattern has not recurred (U12/G1 remains closed).
- **No payments at bank against the $17,420.00 opening accounts payable**
  (account 2000) — seventh consecutive month, carried as unknown U9.

## Payroll three-way tie-out — 07/25

| Level | Net pay | Tax remittance |
|---|---:|---:|
| Payroll register (`payroll_register.json`, July) | $48,200.00 | $11,280.00 |
| Books (JE-2507-009 net pay; JE-2507-011 remit) | $48,200.00 | $11,280.00 |
| Bank statement (07/25 ACH lines) | $48,200.00 | $11,280.00 |

Reconciliation math: gross $54,404.00 − net $48,200.00 = withholding
$6,204.00; withholding $6,204.00 + employer taxes $5,076.00 = remittance
$11,280.00 ✔
Account 2210 clears cumulatively: credits Jan–Jul 7 × ($6,204.00 +
$5,076.00) = $78,960.00 equal debits Jan–Jul 7 × $11,280.00 = $78,960.00;
cumulative balance $0.00 ✔.

Register is again identical to Jan–Jun (U11, 7th month): gross $54,404.00,
net $48,200.00, employer $5,076.00, remit $11,280.00, 9 employees.

## Reconciling items

**None.** Bank and book cash agree at $175,330.00 with no deposits in transit,
no unposted debits, and no unrecorded bank items.
