# Bank reconciliation — November 2025

**Account:** Pacific Summit Bank, acct ending 5531 (documents/month_11/bank_statement.pdf, extracted with pdftotext)
**Book account:** 1000 Cash — Operating

## Summary

| | Amount |
|---|---:|
| Bank balance, 11/30/2025 (per statement) | **($15,750.00)** — overdrawn |
| Book balance, 11/30/2025 (per trial_balance.json 1000, a credit balance) | **($15,750.00)** |
| **Difference** | **0.00** |

Reconciles exactly — to the cent, in overdraft. No deposits in transit, no outstanding checks, no bank-side adjustments, nothing forced. The account is **negative for the first time in the year**; that is real, it is proved by every row below, and it is opened as **new open item 19** (see open_items.md). The reconciliation difference is 0.00 not because the cash position is comfortable but because the books record exactly what the bank did.

## Statement integrity checks (performed line-by-line, header not trusted)

- Header values verified **by content, not by label** (April's and May's PDF text layers printed header values misaligned under the wrong captions). This month the labels align: beginning 38,850.00 (= October bank ending AND October book close ✓), total debits 83,250.00, total credits 28,650.00, ending ($15,750.00). Cross-foot verified: 38,850.00 + 28,650.00 − 83,250.00 = (15,750.00) ✓.
- Transaction rows print in shifted pdftotext columns on the second page (as in prior months); debit/credit classification was therefore taken from the running-balance **delta**, not column position — every row's sign is proved by the recomputation below. Negative running balances print parenthesized — `($6,020.00)`, `($17,300.00)`, `($16,650.00)`, `($16,200.00)`, `($15,750.00)` — and each parenthesis rendering was checked against the recomputed sign, not assumed.
- **30/30 printed running balances equal the balances recomputed** from the 38,850.00 opening. The recomputation is the test; the printed balances are the expected values.
- 30 rows parse to 23 credits (all `ACH <CUSTOMER>` subscription receipts, 11/20–11/26) + 7 debits (5 vendor ACHs 11/05–11/09 + payroll legs 11/25). Nothing unidentified in either direction. **No wire this month** — the only 2025 wire to date remains the Vireo 27,000.00 prepay collected 09/15, and no annual prepay was billed in November.

## Overdraft onset — documented from the rows themselves

The account runs at 15,080.00 after the five vendor ACHs (11/05–11/09), rebuilds to 42,180.00 through 11/20–11/25 collections, then the single day's payroll of 59,480.00 (rows 26–27) overwhelms it: **the account goes negative on 11/25 at ($6,020.00), reaches the low point ($17,300.00) the same day after GUSTO TAX, and recovers only to ($15,750.00) on the three 11/26 deposits.** Two facts of consequence, both proved by the statement:

- **The bank funded the entire shortfall with no NSF/return item and charged nothing:** zero rows on the statement contain any overdraft fee, returned-item debit, interest, or penalty. Five ACH vendor debits had already cleared before the shortfall existed; the two payroll debits cleared straight into the negative.
- **No loan, line, or overdraft-facility document exists anywhere in the engagement file**, and the library contains no cash-classification guidance. The books therefore record the bank's own number faithfully (1000 carries a credit balance of 15,750.00 = negative cash) and the classification question is escalated, not decided by fiat — see item 19 for the year-end presentation stance, which is stated and labeled **unverified belief**, not cited.

## Line-by-line recomputation

Anchor: 38,850.00 (October close). Each printed balance is re-derived from the prior balance ± the row amount (sign from the delta).

| # | Date | Description | Debit | Credit | Recomputed | Printed |
|---|---|---|---:|---:|---:|---:|
| — | — | Beginning (October close) | | | 38,850.00 | 38,850.00 |
| 1 | 11/05 | ACH AWS | 11,120.00 |  | 27,730.00 | 27,730.00 |
| 2 | 11/06 | ACH WEWORK | 7,200.00 |  | 20,530.00 | 20,530.00 |
| 3 | 11/07 | ACH GUSTO FEES | 240.00 |  | 20,290.00 | 20,290.00 |
| 4 | 11/08 | ACH NOTION/SLACK/GITHUB | 1,460.00 |  | 18,830.00 | 18,830.00 |
| 5 | 11/09 | ACH GOOGLE ADS | 3,750.00 |  | 15,080.00 | 15,080.00 |
| 6 | 11/20 | ACH CEDAR LOGISTICS INC |  | 450.00 | 15,530.00 | 15,530.00 |
| 7 | 11/20 | ACH ALDER STUDIOS INC |  | 900.00 | 16,430.00 | 16,430.00 |
| 8 | 11/20 | ACH KESTREL FOODS CO |  | 650.00 | 17,080.00 | 17,080.00 |
| 9 | 11/20 | ACH EMBER SYSTEMS INC |  | 450.00 | 17,530.00 | 17,530.00 |
| 10 | 11/21 | ACH CEDAR LOGISTICS LLC |  | 1,800.00 | 19,330.00 | 19,330.00 |
| 11 | 11/21 | ACH EMBER FOODS LLC |  | 1,800.00 | 21,130.00 | 21,130.00 |
| 12 | 11/22 | ACH EMBER HEALTH CO |  | 2,400.00 | 23,530.00 | 23,530.00 |
| 13 | 11/22 | ACH GRANITE SYSTEMS LLC |  | 1,800.00 | 25,330.00 | 25,330.00 |
| 14 | 11/22 | ACH CEDAR LABS LLC |  | 1,800.00 | 27,130.00 | 27,130.00 |
| 15 | 11/23 | ACH JUNIPER LOGISTICS LLC |  | 650.00 | 27,780.00 | 27,780.00 |
| 16 | 11/23 | ACH EMBER CAPITAL INC |  | 2,400.00 | 30,180.00 | 30,180.00 |
| 17 | 11/23 | ACH EMBER LOGISTICS INC |  | 450.00 | 30,630.00 | 30,630.00 |
| 18 | 11/23 | ACH HARBOR LOGISTICS LLC |  | 1,200.00 | 31,830.00 | 31,830.00 |
| 19 | 11/23 | ACH CEDAR STUDIOS INC |  | 900.00 | 32,730.00 | 32,730.00 |
| 20 | 11/24 | ACH KESTREL SYSTEMS INC |  | 2,400.00 | 35,130.00 | 35,130.00 |
| 21 | 11/24 | ACH IRIS HEALTH LLC |  | 900.00 | 36,030.00 | 36,030.00 |
| 22 | 11/24 | ACH BIRCH LABS LLC |  | 2,400.00 | 38,430.00 | 38,430.00 |
| 23 | 11/25 | ACH DUNE HEALTH CO |  | 900.00 | 39,330.00 | 39,330.00 |
| 24 | 11/25 | ACH EMBER CAPITAL CO |  | 2,400.00 | 41,730.00 | 41,730.00 |
| 25 | 11/25 | ACH FJORD HEALTH CO |  | 450.00 | 42,180.00 | 42,180.00 |
| 26 | 11/25 | ACH GUSTO NET PAY | 48,200.00 |  | (6,020.00) | (6,020.00) |
| 27 | 11/25 | ACH GUSTO TAX | 11,280.00 |  | (17,300.00) | (17,300.00) |
| 28 | 11/26 | ACH BIRCH HEALTH CO |  | 650.00 | (16,650.00) | (16,650.00) |
| 29 | 11/26 | ACH FJORD STUDIOS INC |  | 450.00 | (16,200.00) | (16,200.00) |
| 30 | 11/26 | ACH DUNE FOODS CO |  | 450.00 | (15,750.00) | (15,750.00) |

Every printed balance equals the recomputed balance; the closing recomputation lands on (15,750.00) = the printed ending balance. **Difference 0.00.**

## Deposits (credits) — 23 rows, 28,650.00

The 23 bank credits matched **exactly, 1:1 by payer and amount (multiset equality), to the 23 November receipts in documents/month_11/cash_receipts.csv** — every one of the 23 continuing customers paying its November invoice (INV-2447..INV-2470 with INV-2458 absent), collected 11/20–11/26. Total 28,650.00 = total statement credits ✓.

- **No ALDER STUDIOS LLC deposit — the churn guard holds for the third consecutive month.** C-012 cancelled effective 08/31 (open item 16), yet the billing system issued the ghost invoice a THIRD time — INV-2458, 1,800.00, 11/01 — despite the October close's explicit written demand that management confirm billing suppression BEFORE the November run (open item 17, escalated again; see open_items.md). The customer did **not** pay — 11/06 email, verbatim third time: "We will not be paying this. Please issue a credit and stop." — and the statement confirms it: **no deposit from Alder Studios LLC exists anywhere among the 30 recomputed rows.** The proof is by payer NAME, never by amount: exactly four 1,800.00 deposits cleared (rows 10, 11, 13, 14) and every one is a different, legitimate customer — Cedar Logistics LLC, Ember Foods LLC, Granite Systems LLC, Cedar Labs LLC. The ghost was credited in November (JE-2025-11-02), never became cash, and never aged in A/R.
- **ALDER STUDIOS INC 900.00 (row 7, 11/20) IS legitimate and MUST keep being billed** — that is C-018 Alder Studios **Inc**, a different, continuing customer (the name trap first flagged in August: the churning entity is the **LLC**). No over-correction: C-018's INV-2464 stands and its payment cleared.
- **Name trap checked (kept on the record every month since it first appeared):** the payer list again contains the deliberately confusing near-duplicates — `ALDER STUDIOS INC` (row 7, 900.00), the only Alder on the statement and the entity the dispute is NOT about; `CEDAR LOGISTICS INC` (row 6, 450.00) vs `CEDAR LOGISTICS LLC` (row 10, 1,800.00); `CEDAR LABS LLC` (row 14) vs `CEDAR STUDIOS INC` (row 19); `EMBER CAPITAL INC` (row 16) vs `EMBER CAPITAL CO` (row 24) — both real, different-terms customers (2,400.00 each); `KESTREL SYSTEMS INC` (row 20) vs `KESTREL FOODS CO` (row 8); `FJORD HEALTH CO` (row 25) vs `FJORD STUDIOS INC` (row 29); `DUNE HEALTH CO` (row 23) vs `DUNE FOODS CO` (row 30); `EMBER HEALTH CO` (row 12) vs `EMBER SYSTEMS INC` / `EMBER FOODS LLC` / `EMBER LOGISTICS INC`. The payer-and-amount multiset equality to the 23 receipts proves every deposit is the right invoice payment despite the near-identical names.
- **HARBOR LOGISTICS LLC 1,200.00 (row 18, 11/23)** is **customer C-017 Harbor Logistics LLC** paying its November invoice — NOT the law-firm vendor Harbor Law LLP. The two entities share the first word only; direction distinguishes them (this is a customer deposit; a Harbor Law payment would be a withdrawal — and there is none this month, consistent with the quarterly cycle).

## Withdrawals (debits) — 7 rows, 83,250.00

| Bank row | Amount | Support |
|---|---:|---|
| 11/05 AWS | 11,120.00 | vendor bill 11/05 (5000 Hosting; +120.00 over October — the same +120.00/month step since April, item 11) |
| 11/06 WEWORK | 7,200.00 | vendor bill 11/06 (5100 Rent, flat all year) |
| 11/07 GUSTO FEES | 240.00 | vendor bill 11/07 (5400 G&A other) |
| 11/08 NOTION/SLACK/GITHUB | 1,460.00 | vendor bill 11/08 (5200 Software) |
| 11/09 GOOGLE ADS | 3,750.00 | vendor bill 11/09 (5300 Marketing; +50.00 over October — the same +50.00/month step since April, item 11) |
| 11/25 GUSTO NET PAY | 48,200.00 | payroll register net_pay (single net-pay debit — no duplicate); drove the account into overdraft |
| 11/25 GUSTO TAX | 11,280.00 | payroll register taxes_remitted (6,204.00 withheld + 5,076.00 employer) |

- Bills total 23,770.00 and payroll totals 59,480.00 on both legs; 23,770.00 + 59,480.00 = 83,250.00 = total statement debits ✓. Payroll agrees to the register AND to the bank to the penny (close-checklist item 4) — the seventh consecutive month the register is identical to the cent (May–Nov; observation, item noted in open_items.md).
- **No HARBOR LAW LLP withdrawal — expected and correct.** The law-firm bill is quarterly (paid 03/09, 06/09, 09/09); nothing is owed in November and the next bill is expected **12/09** (open item 2 stays closed — a second consecutive clean month of the cycle behaving as proven).
- **No overdraft fee, NSF, or return-item debit anywhere on the statement**, although the bank funded 17,300.00 of negative balance — recorded as fact, escalated as item 19.
- **Every November vendor bill was paid in-month** (ACH same day as the bill date) — so opening A/P 17,420.00 remains the only A/P on the books (item 8, eleventh month untouched).
- Every debit traces to a source document; nothing unexplained.

## Cash roll-forward (book side)

38,850.00 (10/31 book = bank) + 28,650.00 receipts − 23,770.00 vendor payments − 48,200.00 net pay − 11,280.00 tax remittance = **(15,750.00)** = trial_balance.json 1000 (credit 15,750.00) = bank ending. **Difference 0.00; nothing forced.** The negative is reported as it stands — the presentation question belongs to item 19, not to the reconciliation.
