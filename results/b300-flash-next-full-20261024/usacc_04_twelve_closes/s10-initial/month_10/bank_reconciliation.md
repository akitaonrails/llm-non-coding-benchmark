# Bank reconciliation — October 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_10/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 10/31/2025 (per statement) | **38,850.00** |
| Book balance, 10/31/2025 (per trial_balance.json 1000) | **38,850.00** |
| **Difference** | **0.00** |

Reconciles exactly. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced.

## Statement integrity checks (performed line-by-line, header not trusted)

- Header values verified **by content, not by label** (April's and May's PDF text layers printed header values misaligned under the wrong captions). This month the labels align: beginning 93,280.00 (= September bank ending AND September book close ✓), total debits 83,080.00, total credits 28,650.00, ending 38,850.00. Cross-foot verified: 93,280.00 + 28,650.00 − 83,080.00 = 38,850.00 ✓.
- Transaction rows print in shifted pdftotext columns on the second page (as in prior months); debit/credit classification was therefore taken from the running-balance **delta**, not column position — every row's sign is proved by the recomputation below.
- **30/30 printed running balances equal the balances recomputed** from the 93,280.00 opening. The recomputation is the test; the printed balances are the expected values.
- 30 rows parse to 23 credits (all `ACH <CUSTOMER>` subscription receipts, 10/20–10/26) + 7 debits (5 vendor ACHs 10/05–10/09 + payroll legs 10/25). Nothing unidentified in either direction. **No wire this month** — the only 2025 wire to date was the Vireo 27,000.00 prepay collected 09/15, and no second annual prepay was billed in October.

## Line-by-line recomputation

Anchor: 93,280.00 (September close). Each printed balance is re-derived from the prior balance ± the row amount (sign from the delta).

| # | Date | Description | Debit | Credit | Recomputed | Printed |
|---|---|---|---:|---:|---:|---:|
| — | — | Beginning (September close) | | | 93,280.00 | 93,280.00 |
| 1 | 10/05 | ACH AWS | 11,000.00 |  | 82,280.00 | 82,280.00 |
| 2 | 10/06 | ACH WEWORK | 7,200.00 |  | 75,080.00 | 75,080.00 |
| 3 | 10/07 | ACH GUSTO FEES | 240.00 |  | 74,840.00 | 74,840.00 |
| 4 | 10/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 |  | 73,380.00 | 73,380.00 |
| 5 | 10/09 | ACH GOOGLE ADS | 3,700.00 |  | 69,680.00 | 69,680.00 |
| 6 | 10/20 | ACH CEDAR LOGISTICS INC |  | 450.00 | 70,130.00 | 70,130.00 |
| 7 | 10/20 | ACH ALDER STUDIOS INC |  | 900.00 | 71,030.00 | 71,030.00 |
| 8 | 10/20 | ACH KESTREL FOODS CO |  | 650.00 | 71,680.00 | 71,680.00 |
| 9 | 10/20 | ACH EMBER SYSTEMS INC |  | 450.00 | 72,130.00 | 72,130.00 |
| 10 | 10/21 | ACH CEDAR LOGISTICS LLC |  | 1,800.00 | 73,930.00 | 73,930.00 |
| 11 | 10/21 | ACH EMBER FOODS LLC |  | 1,800.00 | 75,730.00 | 75,730.00 |
| 12 | 10/22 | ACH EMBER HEALTH CO |  | 2,400.00 | 78,130.00 | 78,130.00 |
| 13 | 10/22 | ACH GRANITE SYSTEMS LLC |  | 1,800.00 | 79,930.00 | 79,930.00 |
| 14 | 10/22 | ACH CEDAR LABS LLC |  | 1,800.00 | 81,730.00 | 81,730.00 |
| 15 | 10/23 | ACH JUNIPER LOGISTICS LLC |  | 650.00 | 82,380.00 | 82,380.00 |
| 16 | 10/23 | ACH EMBER CAPITAL INC |  | 2,400.00 | 84,780.00 | 84,780.00 |
| 17 | 10/23 | ACH EMBER LOGISTICS INC |  | 450.00 | 85,230.00 | 85,230.00 |
| 18 | 10/23 | ACH HARBOR LOGISTICS LLC |  | 1,200.00 | 86,430.00 | 86,430.00 |
| 19 | 10/23 | ACH CEDAR STUDIOS INC |  | 900.00 | 87,330.00 | 87,330.00 |
| 20 | 10/24 | ACH KESTREL SYSTEMS INC |  | 2,400.00 | 89,730.00 | 89,730.00 |
| 21 | 10/24 | ACH IRIS HEALTH LLC |  | 900.00 | 90,630.00 | 90,630.00 |
| 22 | 10/24 | ACH BIRCH LABS LLC |  | 2,400.00 | 93,030.00 | 93,030.00 |
| 23 | 10/25 | ACH DUNE HEALTH CO |  | 900.00 | 93,930.00 | 93,930.00 |
| 24 | 10/25 | ACH EMBER CAPITAL CO |  | 2,400.00 | 96,330.00 | 96,330.00 |
| 25 | 10/25 | ACH FJORD HEALTH CO |  | 450.00 | 96,780.00 | 96,780.00 |
| 26 | 10/25 | ACH GUSTO NET PAY | 48,200.00 |  | 48,580.00 | 48,580.00 |
| 27 | 10/25 | ACH GUSTO TAX | 11,280.00 |  | 37,300.00 | 37,300.00 |
| 28 | 10/26 | ACH BIRCH HEALTH CO |  | 650.00 | 37,950.00 | 37,950.00 |
| 29 | 10/26 | ACH FJORD STUDIOS INC |  | 450.00 | 38,400.00 | 38,400.00 |
| 30 | 10/26 | ACH DUNE FOODS CO |  | 450.00 | 38,850.00 | 38,850.00 |

Every printed balance equals the recomputed balance; the closing recomputation lands on 38,850.00 = the printed ending balance. **Difference 0.00.**

## Deposits (credits) — 23 rows, 28,650.00

The 23 bank credits matched **exactly, 1:1 by payer and amount (multiset equality), to the 23 October receipts in documents/month_10/cash_receipts.csv** — every one of the 23 continuing customers paying its October invoice (INV-2423..INV-2446 with INV-2434 absent), collected 10/20–10/26. Total 28,650.00 = total statement credits ✓.

- **No ALDER STUDIOS LLC deposit — the churn guard holds for the second consecutive month.** C-012 cancelled effective 08/31 (open item 16), yet the billing system AGAIN issued INV-2434 1,800.00 on 10/01 (open item 17, now an escalated recurring control failure). The customer did **not** pay — 10/06 email: "We will not be paying this. Please issue a credit and stop." — and the statement confirms it: no 1,800.00 deposit from Alder Studios LLC exists anywhere among the 30 recomputed rows. The ghost invoice was credited in October (JE-2025-10-02), never became cash, and never aged in A/R.
- **ALDER STUDIOS INC 900.00 (row 7, 10/20) IS legitimate** — that is C-018 Alder Studios **Inc**, a different, continuing customer (the name trap first flagged in August: the churning entity is the **LLC**). C-018 stays billed and paid.
- **Name trap checked (kept on the record every month since it first appeared):** the payer list contains deliberately confusing near-duplicates — `ALDER STUDIOS INC` (row 7, 900.00) — the only Alder on the statement, and the entity the dispute is NOT about; `CEDAR LOGISTICS INC` (row 6, 450.00) vs `CEDAR LOGISTICS LLC` (row 10, 1,800.00); `CEDAR LABS LLC` (row 14) vs `CEDAR STUDIOS INC` (row 19); `EMBER CAPITAL INC` (row 16) vs `EMBER CAPITAL CO` (row 24) — both real, different-terms customers (2,400.00 each); `KESTREL SYSTEMS INC` (row 20) vs `KESTREL FOODS CO` (row 8); `FJORD HEALTH CO` (row 25) vs `FJORD STUDIOS INC` (row 29); `DUNE HEALTH CO` (row 23) vs `DUNE FOODS CO` (row 30); `EMBER HEALTH CO` (row 12) vs `EMBER SYSTEMS INC` / `EMBER FOODS LLC` / `EMBER LOGISTICS INC`. The payer-and-amount multiset equality to the 23 receipts proves every deposit is the right invoice payment despite the near-identical names.
- **HARBOR LOGISTICS LLC 1,200.00 (row 18, 10/23)** is **customer C-017 Harbor Logistics LLC** paying its October invoice — NOT the law-firm vendor Harbor Law LLP. The two entities share the first word only; direction distinguishes them (this is a customer deposit; a Harbor Law payment would be a withdrawal — and there is none this month, consistent with the quarterly cycle).

## Withdrawals (debits) — 7 rows, 83,080.00

| Bank row | Amount | Support |
|---|---:|---|
| 10/05 AWS | 11,000.00 | vendor bill 10/05 (5000 Hosting; +120.00, the same +120.00/month step since April — item 11) |
| 10/06 WEWORK | 7,200.00 | vendor bill 10/06 (5100 Rent, flat all year) |
| 10/07 GUSTO FEES | 240.00 | vendor bill 10/07 (5400 G&A other) |
| 10/08 NOTION/SLACK/GITHUB | 1,460.00 | vendor bill 10/08 (5200 Software) |
| 10/09 GOOGLE ADS | 3,700.00 | vendor bill 10/09 (5300 Marketing; +50.00, the same +50.00/month step since April — item 11) |
| 10/25 GUSTO NET PAY | 48,200.00 | payroll register net_pay (single net-pay debit — no duplicate) |
| 10/25 GUSTO TAX | 11,280.00 | payroll register taxes_remitted (6,204.00 withheld + 5,076.00 employer) |

- Bills total 23,600.00 and payroll totals 59,480.00 on both legs; 23,600.00 + 59,480.00 = 83,080.00 = total statement debits ✓. Payroll agrees to the register AND to the bank to the penny (close-checklist item 4).
- **No HARBOR LAW LLP withdrawal — expected and correct.** The law-firm bill is quarterly (paid 03/09, 06/09, 09/09); nothing is owed in October and the next bill is expected 12/09 (open item 2, closed — October's absence is the cycle behaving as proven).
- **Every October vendor bill was paid in-month** (ACH same day as the bill date) — so opening A/P 17,420.00 remains the only A/P on the books (item 8, tenth month untouched).
- Every debit traces to a source document; nothing unexplained.

## Cash roll-forward (book side)

93,280.00 (9/30 book = bank) + 28,650.00 receipts − 23,600.00 vendor payments − 48,200.00 net pay − 11,280.00 tax remittance = **38,850.00** = trial_balance.json 1000 = bank ending. **Difference 0.00; nothing forced.**
