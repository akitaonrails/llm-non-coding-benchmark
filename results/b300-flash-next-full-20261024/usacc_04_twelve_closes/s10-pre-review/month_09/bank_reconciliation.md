# Bank reconciliation — September 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_09/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 09/30/2025 (per statement) | **93,280.00** |
| Book balance, 09/30/2025 (per trial_balance.json 1000) | **93,280.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced.

## Statement integrity checks (performed line-by-line, header not trusted)

- Header values verified **by content, not by label** (April's and May's PDF text layers printed header values misaligned under the wrong captions). This month the labels align: beginning 123,040.00 (= August bank ending AND August book close ✓), total debits 85,410.00, total credits 55,650.00, ending 93,280.00. Cross-foot verified: 123,040.00 + 55,650.00 − 85,410.00 = 93,280.00 ✓.
- Transaction rows print in shifted pdftotext columns on the second page (as in prior months); debit/credit classification was therefore taken from the running-balance **delta**, not column position — every row's sign is proved by the recomputation below.
- **32/32 printed running balances equal the balances recomputed** from the 123,040.00 opening. The recomputation is the test; the printed balances are the expected values.
- 32 rows parse to 24 credits (23 `ACH <CUSTOMER>` subscription receipts 09/20–09/26 + 1 `WIRE IN` customer prepay 09/15) + 8 debits (6 vendor ACHs 09/05–09/10 + payroll legs 09/25). Nothing unidentified in either direction.

## Line-by-line recomputation

Anchor: 123,040.00 (August close). Each printed balance is re-derived from the prior balance ± the row amount (sign from the delta).

| — | — | Beginning (August close) | | | 123,040.00 | 123,040.00 |
| 1 | 09/05 | ACH AWS | 10,880.00 |  | 112,160.00 | 112,160.00 |
| 2 | 09/06 | ACH WEWORK | 7,200.00 |  | 104,960.00 | 104,960.00 |
| 3 | 09/07 | ACH GUSTO FEES | 240.00 |  | 104,720.00 | 104,720.00 |
| 4 | 09/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 |  | 103,260.00 | 103,260.00 |
| 5 | 09/09 | ACH HARBOR LAW LLP | 2,500.00 |  | 100,760.00 | 100,760.00 |
| 6 | 09/10 | ACH GOOGLE ADS | 3,650.00 |  | 97,110.00 | 97,110.00 |
| 7 | 09/15 | WIRE IN VIREO CLINICS PBC |  | 27,000.00 | 124,110.00 | 124,110.00 |
| 8 | 09/20 | ACH CEDAR LOGISTICS INC |  | 450.00 | 124,560.00 | 124,560.00 |
| 9 | 09/20 | ACH ALDER STUDIOS INC |  | 900.00 | 125,460.00 | 125,460.00 |
| 10 | 09/20 | ACH KESTREL FOODS CO |  | 650.00 | 126,110.00 | 126,110.00 |
| 11 | 09/20 | ACH EMBER SYSTEMS INC |  | 450.00 | 126,560.00 | 126,560.00 |
| 12 | 09/21 | ACH CEDAR LOGISTICS LLC |  | 1,800.00 | 128,360.00 | 128,360.00 |
| 13 | 09/21 | ACH EMBER FOODS LLC |  | 1,800.00 | 130,160.00 | 130,160.00 |
| 14 | 09/22 | ACH EMBER HEALTH CO |  | 2,400.00 | 132,560.00 | 132,560.00 |
| 15 | 09/22 | ACH GRANITE SYSTEMS LLC |  | 1,800.00 | 134,360.00 | 134,360.00 |
| 16 | 09/22 | ACH CEDAR LABS LLC |  | 1,800.00 | 136,160.00 | 136,160.00 |
| 17 | 09/23 | ACH JUNIPER LOGISTICS LLC |  | 650.00 | 136,810.00 | 136,810.00 |
| 18 | 09/23 | ACH EMBER CAPITAL INC |  | 2,400.00 | 139,210.00 | 139,210.00 |
| 19 | 09/23 | ACH EMBER LOGISTICS INC |  | 450.00 | 139,660.00 | 139,660.00 |
| 20 | 09/23 | ACH HARBOR LOGISTICS LLC |  | 1,200.00 | 140,860.00 | 140,860.00 |
| 21 | 09/23 | ACH CEDAR STUDIOS INC |  | 900.00 | 141,760.00 | 141,760.00 |
| 22 | 09/24 | ACH KESTREL SYSTEMS INC |  | 2,400.00 | 144,160.00 | 144,160.00 |
| 23 | 09/24 | ACH IRIS HEALTH LLC |  | 900.00 | 145,060.00 | 145,060.00 |
| 24 | 09/24 | ACH BIRCH LABS LLC |  | 2,400.00 | 147,460.00 | 147,460.00 |
| 25 | 09/25 | ACH DUNE HEALTH CO |  | 900.00 | 148,360.00 | 148,360.00 |
| 26 | 09/25 | ACH EMBER CAPITAL CO |  | 2,400.00 | 150,760.00 | 150,760.00 |
| 27 | 09/25 | ACH FJORD HEALTH CO |  | 450.00 | 151,210.00 | 151,210.00 |
| 28 | 09/25 | ACH GUSTO NET PAY | 48,200.00 |  | 103,010.00 | 103,010.00 |
| 29 | 09/25 | ACH GUSTO TAX | 11,280.00 |  | 91,730.00 | 91,730.00 |
| 30 | 09/26 | ACH BIRCH HEALTH CO |  | 650.00 | 92,380.00 | 92,380.00 |
| 31 | 09/26 | ACH FJORD STUDIOS INC |  | 450.00 | 92,830.00 | 92,830.00 |
| 32 | 09/26 | ACH DUNE FOODS CO |  | 450.00 | 93,280.00 | 93,280.00 |
| | | **Totals** | **85,410.00** | **55,650.00** | **93,280.00** | **93,280.00** |
32/32 tie. Recomputed totals agree with the printed header: debits 85,410.00 ✓, credits 55,650.00 ✓.

## Deposits (credits) — 24 rows, 55,650.00

The 24 bank credits matched **exactly, 1:1 by payer and amount (multiset equality), to the 24 September receipts in documents/month_09/cash_receipts.csv**. 23 of them are the September subscription payments — **28,650.00**, every one of the 23 continuing customers, collected 09/20–09/26 — matched 1:1 by customer and amount to invoices INV-2398..INV-2421 **except INV-2409**; the 24th is the **WIRE IN VIREO CLINICS PBC 27,000.00 (row 7, 09/15)** — the only wire on the statement (every subscription collection is ACH), paying new-customer annual prepay INV-2422 (order form C-030; open item 18).

- **No ALDER STUDIOS LLC deposit — the churn guard holds.** C-012 cancelled effective 08/31 (open item 16), yet the billing system still issued INV-2409 1,800.00 on 09/01 (open item 17). The customer did **not** pay — 09/06 email: "We will not be paying this. Please issue a credit and stop." — and the statement confirms it: no 1,800.00 deposit from Alder Studios LLC exists anywhere among the 32 recomputed rows. The ghost invoice was credited in September (JE-2025-09-02), never became cash, and never aged in A/R.
- **ALDER STUDIOS INC 900.00 (row 9, 09/20) IS legitimate** — that is C-018 Alder Studios **Inc**, a different, continuing customer (the name trap flagged in August: the churning entity is the **LLC**). C-018 stays billed and paid.
- **Name trap checked (kept on the record every month since it first appeared):** the customer list contains deliberately confusing near-duplicates — `ALDER STUDIOS INC` (row 9, 900.00) — the only Alder on the statement; `CEDAR LOGISTICS INC` (row 8, 450.00) vs `CEDAR LOGISTICS LLC` (row 12, 1,800.00); `CEDAR LABS LLC` (row 16) vs `CEDAR STUDIOS INC` (row 21); `EMBER CAPITAL INC` (row 18) vs `EMBER CAPITAL CO` (row 26) — both real, different-terms customers (2,400.00 each); `KESTREL SYSTEMS INC` (row 22) vs `KESTREL FOODS CO` (row 10); `FJORD HEALTH CO` (row 27) vs `FJORD STUDIOS INC` (row 31); `DUNE HEALTH CO` (row 25) vs `DUNE FOODS CO` (row 32); `EMBER HEALTH CO` (row 14) vs `EMBER SYSTEMS INC` / `EMBER FOODS LLC` / `EMBER LOGISTICS INC`. The payer-and-amount multiset equality to the 24 receipts proves every deposit is the right invoice payment despite the near-identical names.
- **HARBOR LOGISTICS LLC 1,200.00 (row 20, 09/23)** is **customer C-017 Harbor Logistics LLC** paying its September invoice — NOT the vendor Harbor Law LLP whose 2,500.00 bill went out the same month (row 5, open item 2, now closed). Different entity, opposite direction.

## Withdrawals (debits) — 8 rows, 85,410.00

| Bank row | Amount | Support |
|---|---:|---|
| 09/05 AWS | 10,880.00 | vendor bill 09/05 (5000 Hosting; +120.00, the same +120.00/month step since April) |
| 09/06 WEWORK | 7,200.00 | vendor bill 09/06 (5100 Rent, flat all year) |
| 09/07 GUSTO FEES | 240.00 | vendor bill 09/07 (5400 G&A other) |
| 09/08 NOTION/SLACK/GITHUB | 1,460.00 | vendor bill 09/08 (5200 Software) |
| 09/09 HARBOR LAW LLP | 2,500.00 | vendor bill 09/09 (5400; **third quarterly bill — 03/09, 06/09, 09/09 — open item 2 closes**) |
| 09/10 GOOGLE ADS | 3,650.00 | vendor bill 09/10 (5300 Marketing; +50.00, the same +50.00/month step since April) |
| 09/25 GUSTO NET PAY | 48,200.00 | payroll register net_pay (single net-pay debit — no duplicate) |
| 09/25 GUSTO TAX | 11,280.00 | payroll register taxes_remitted (6,204.00 withheld + 5,076.00 employer) |

- Bills total 25,930.00 and payroll totals 59,480.00 on both legs; 25,930.00 + 59,480.00 = 85,410.00 = total statement debits ✓. Payroll agrees to the register AND to the bank to the penny (close-checklist item 4).
- **Every September vendor bill was paid in-month** (ACH same day or next day after the bill date) — so opening A/P 17,420.00 remains the only A/P on the books (item 8).
- Every debit traces to a source document; nothing unexplained.

## Cash roll-forward (book side)

123,040.00 (8/31 book = bank) + 55,650.00 receipts − 25,930.00 vendor payments − 48,200.00 net pay − 11,280.00 tax remittance = **93,280.00** = trial_balance.json 1000 = bank ending. **Difference 0.00; nothing forced.**
