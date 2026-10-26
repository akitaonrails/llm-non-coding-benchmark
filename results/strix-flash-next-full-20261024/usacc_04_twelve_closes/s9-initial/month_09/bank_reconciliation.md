# Bank Reconciliation — September 2025

**Book account:** 1000 Cash — Operating
**Bank:** Pacific Summit Bank, account ending 5531
**Statement period:** 2025-09-01 through 2025-09-30
**Statement source:** `documents/month_09/bank_statement.pdf`

> **Statement selection note.** `documents/bank_statement.csv` (workspace
> documents root) was again **not** used: its transactions are dated December
> 2025 and its balances are negative (unknown U8). Everything below is matched
> to the September PDF statement.

## Summary

| | Amount |
|---|---:|
| Bank statement balance, 2025-09-30 | **$93,280.00** |
| Book balance, account 1000 (trial balance) | **$93,280.00** |
| Deposits in transit | 0.00 |
| Outstanding checks / unposted debits | 0.00 |
| Bank items not on books | 0.00 |
| Book items not at bank | 0.00 |
| **Difference** | **$0.00** |

Books and bank tie **with no reconciling items again this month**: every one
of the 32 September statement lines (8 debits, 24 credits) maps to a September
journal entry.

## Book cash buildup (arithmetic)

| Item | Reference | Amount |
|---|---|---:|
| Opening cash 2025-08-31 | month_08 close / statement beginning balance | $123,040.00 |
| Customer receipts: 23 monthly ACHs + Vireo wire (below) | JE-2509-003 | +$55,650.00 |
| Vendor ACH payments, 6 items (below) | JE-2509-010 | −$25,930.00 |
| Payroll net pay ACH, 09/25 | JE-2509-011 | −$48,200.00 |
| Payroll tax remit ACH, 09/25 | JE-2509-013 | −$11,280.00 |
| **Book cash 2025-09-30** | | **$93,280.00** |

$123,040.00 + $55,650.00 = $178,690.00
$178,690.00 − $25,930.00 = $152,760.00
$152,760.00 − $48,200.00 = $104,560.00
$104,560.00 − $11,280.00 = **$93,280.00**

Trial balance account 1000 shows cumulative debits $889,050.00 (= $833,400.00
through August + $55,650.00 September receipts) and cumulative credits
$795,770.00 (= $710,360.00 through August + $25,930.00 + $48,200.00 +
$11,280.00 September payments), net **$93,280.00** debit — agrees with the
buildup.

## Statement internal check

Statement header: beginning $123,040.00, total debits $85,410.00,
total credits $55,650.00, ending $93,280.00.
$123,040.00 + $55,650.00 − $85,410.00 = $93,280.00 ✔
(matches the header and the running-balance column line by line, including
across the statement's page break).
Debits footing: $10,880.00 + $7,200.00 + $240.00 + $1,460.00 + $2,500.00 +
$3,650.00 + $48,200.00 + $11,280.00 = $85,410.00 ✔ (8 debit lines)
Credits footing: Vireo Clinics PBC wire $27,000.00 + 23 monthly ACHs
$28,650.00 = $55,650.00 ✔ (24 credit lines; 32 transaction lines total)

## Credits on the statement — all 24 items identified

**Non-customer credits (0):** none — the 09/15 wire is a customer payment
(INV-2422); contrast April/May Gusto refund credits and the June Saltline wire.

**Customer credits (24, $55,650.00):** one Vireo Clinics PBC wire and
23 monthly subscription ACHs; each matches a `cash_receipts.csv` row by date +
amount + payee, and the register's `applied_to` gives the invoice. All booked
in one entry, JE-2509-003 (Dr 1000 / Cr 1100 against billing JE-2509-001).

| Date | Payee per statement | Amount | Receipt row (customer / invoice) |
|---|---|---:|---|
| 09/15 | WIRE IN VIREO CLINICS PBC | $27,000.00 | Vireo Clinics PBC — INV-2422 |
| 09/20 | ACH CEDAR LOGISTICS INC | $450.00 | Cedar Logistics Inc — INV-2413 |
| 09/20 | ACH ALDER STUDIOS INC | $900.00 | Alder Studios Inc — INV-2415 |
| 09/20 | ACH KESTREL FOODS CO | $650.00 | Kestrel Foods Co — INV-2417 |
| 09/20 | ACH EMBER SYSTEMS INC | $450.00 | Ember Systems Inc — INV-2420 |
| 09/21 | ACH CEDAR LOGISTICS LLC | $1,800.00 | Cedar Logistics LLC — INV-2407 |
| 09/21 | ACH EMBER FOODS LLC | $1,800.00 | Ember Foods LLC — INV-2421 |
| 09/22 | ACH EMBER HEALTH CO | $2,400.00 | Ember Health Co — INV-2399 |
| 09/22 | ACH GRANITE SYSTEMS LLC | $1,800.00 | Granite Systems LLC — INV-2401 |
| 09/22 | ACH CEDAR LABS LLC | $1,800.00 | Cedar Labs LLC — INV-2406 |
| 09/23 | ACH JUNIPER LOGISTICS LLC | $650.00 | Juniper Logistics LLC — INV-2405 |
| 09/23 | ACH EMBER CAPITAL INC | $2,400.00 | Ember Capital Inc — INV-2408 |
| 09/23 | ACH EMBER LOGISTICS INC | $450.00 | Ember Logistics Inc — INV-2410 |
| 09/23 | ACH HARBOR LOGISTICS LLC | $1,200.00 | Harbor Logistics LLC — INV-2414 |
| 09/23 | ACH CEDAR STUDIOS INC | $900.00 | Cedar Studios Inc — INV-2418 |
| 09/24 | ACH KESTREL SYSTEMS INC | $2,400.00 | Kestrel Systems Inc — INV-2400 |
| 09/24 | ACH IRIS HEALTH LLC | $900.00 | Iris Health LLC — INV-2402 |
| 09/24 | ACH BIRCH LABS LLC | $2,400.00 | Birch Labs LLC — INV-2403 |
| 09/25 | ACH DUNE HEALTH CO | $900.00 | Dune Health Co — INV-2411 |
| 09/25 | ACH EMBER CAPITAL CO | $2,400.00 | Ember Capital Co — INV-2416 |
| 09/25 | ACH FJORD HEALTH CO | $450.00 | Fjord Health Co — INV-2419 |
| 09/26 | ACH BIRCH HEALTH CO | $650.00 | Birch Health Co — INV-2398 |
| 09/26 | ACH FJORD STUDIOS INC | $450.00 | Fjord Studios Inc — INV-2404 |
| 09/26 | ACH DUNE FOODS CO | $450.00 | Dune Foods Co — INV-2412 |
| | **Total statement credits** | **$55,650.00** | 24 rows |

Monthly ACH footing: $450.00 + $900.00 + $650.00 + $450.00 + $1,800.00 + $1,800.00 + $2,400.00 + $1,800.00 + $1,800.00 + $650.00 + $2,400.00 + $450.00 + $1,200.00 + $900.00 + $2,400.00 + $900.00 + $2,400.00 + $900.00 + $2,400.00 + $450.00 + $650.00 + $450.00 + $450.00 = $28,650.00 ✔

Notes:
- Payees match the receipt register exactly. The September receipt population
  is the 23 active subscribers — **no payment on INV-2409** (C-012 Alder
  Studios LLC): the invoice was issued in error after the 08/31 cancellation,
  the customer refused to pay (email 09/06), and we voided it with credit memo
  CM-2509-01 (JE-2509-002, open_items.md item 1). Nothing is owed or owed back
  for September on C-012.
- **ACH ALDER STUDIOS INC $900.00 (09/20) is customer C-018, still active** —
  a different entity from the cancelled C-012 **Alder Studios LLC**. Do not
  confuse the two when reviewing the September and future receipts.
- **WIRE IN VIREO CLINICS PBC $27,000.00 (09/15)** is new-contract advance
  billing (INV-2422), not monthly subscription cash; it sits in account 2200
  after JE-2509-001 and releases $2,250.00/month (JE-2509-015). First wire-in
  from a customer since the June Saltline wire.
- **Timing observation, no accounting effect:** September receipts applied to
  **September** invoices (INV-2398…INV-2421, collected 09/20–09/26), the
  second consecutive month of that pattern; billing and collection are in the
  same month either way.
- **No payment applied to the $92,650.00 opening (legacy) accounts
  receivable** — ninth consecutive month, carried as unknown U3. After the
  credit memo, current-month receivables are fully collected and the 1100
  balance is 100% legacy.

## Debits on the statement — all 8 items identified

| Date | Description | Amount | Booked as | Expense account |
|---|---|---:|---|---|
| 09/05 | ACH AWS | $10,880.00 | JE-2509-004 → paid JE-2509-010 | 6000 Hosting |
| 09/06 | ACH WEWORK | $7,200.00 | JE-2509-005 → paid JE-2509-010 | 6100 Rent |
| 09/07 | ACH GUSTO FEES | $240.00 | JE-2509-006 → paid JE-2509-010 | 6200 G&A |
| 09/08 | ACH NOTION/SLACK/GITHUB | $1,460.00 | JE-2509-007 → paid JE-2509-010 | 6300 Software |
| 09/09 | ACH HARBOR LAW LLP | $2,500.00 | JE-2509-008 → paid JE-2509-010 | 6600 Professional fees |
| 09/10 | ACH GOOGLE ADS | $3,650.00 | JE-2509-009 → paid JE-2509-010 | 6400 Marketing |
| 09/25 | ACH GUSTO NET PAY | $48,200.00 | JE-2509-011 (Dr 5000 / Cr 2210 / Cr 1000 net) | 5000 Salaries (net pay) |
| 09/25 | ACH GUSTO TAX | $11,280.00 | JE-2509-013 (Dr 2210 / Cr 1000) | 2210 Payroll tax clearing |
| | **Total statement debits** | **$85,410.00** | | |

Debits regrouped: $25,930.00 vendor bills + $48,200.00 net pay + $11,280.00
tax remit = $85,410.00 ✔

Notes:
- The six vendor ACHs match `vendor_bills.csv` one-for-one (date and amount).
  AWS $10,880.00 is the **seventh** straight +$120.00/month usage step
  (10,160 → 10,280 → 10,400 → 10,520 → 10,640 → 10,760 → 10,880); Google Ads
  $3,650.00 likewise (+$50.00: … → 3,600 → 3,650). Same-vendor usage drift —
  noted, not reconciling items.
- **ACH HARBOR LAW LLP $2,500.00 (09/09)** — the bill arrived and was paid on
  schedule. Third occurrence on a clean quarterly cadence: 03/09 → 06/09 →
  09/09; cadence now confirmed, next expected December. Account 6600 reaches
  $7,500.00 year-to-date. The vendor is distinct from customer **Harbor
  Logistics LLC** (C-017, paid $1,200.00 on 09/23).
- **Exactly one GUSTO NET PAY debit this month** — the April duplicate-debit
  pattern has not recurred (U12/G1 remains closed).
- **No payments at bank against the $17,420.00 opening accounts payable**
  (account 2000) — ninth consecutive month, carried as unknown U9.

## Payroll three-way tie-out — 09/25

| Level | Net pay | Tax remittance |
|---|---:|---:|
| Payroll register (`payroll_register.json`, September) | $48,200.00 | $11,280.00 |
| Books (JE-2509-011 net pay; JE-2509-013 remit) | $48,200.00 | $11,280.00 |
| Bank statement (09/25 ACH lines) | $48,200.00 | $11,280.00 |

Reconciliation math: gross $54,404.00 − net $48,200.00 = withholding
$6,204.00; withholding $6,204.00 + employer taxes $5,076.00 = remittance
$11,280.00 ✔
Account 2210 clears cumulatively: credits Jan–Sep 9 × ($6,204.00 +
$5,076.00) = $101,520.00 equal debits Jan–Sep 9 × $11,280.00 = $101,520.00;
cumulative balance $0.00 ✔.

Register is again identical to Jan–Aug (U11, 9th month): gross $54,404.00,
net $48,200.00, employer $5,076.00, remit $11,280.00, 9 employees. The 09/25
payroll debits post before the last 09/26 receipt ACHs in the statement's
running-balance column, consistent with prior months.

## Reconciling items

**None.** Bank and book cash agree at $93,280.00 with no deposits in
transit, no unposted debits, and no unrecorded bank items.
