# Bank reconciliation — Brightline Cabinetry LLC

**Account:** Cash — Operating, Hill Country Community Bank, acct ending 2210 (GL 1000)
**Period:** March 1 – March 31, 2026
**Form and rules:** per AICPA practice aid excerpt (library/bank_rec_standard.md)
**Prepared:** 2026-03-31 close

## Opening note on the beginning balance

The March bank statement shows beginning balance **($7,013.13)** — parentheses, i.e. the
account was **overdrawn** on February 28 — and the statement's running balance confirms it
(e.g. −7,013.13 + 9,200.00 = 2,186.87, the 03/03 line). This agrees with the February trial
balance, which shows 7,013.13 in the **credit** column of account 1000 (trial_balance_2026-02-28.csv).
The March 31 ending balance is a normal positive **$7,625.50**.
Check: −7,013.13 + deposits 50,362.00 − withdrawals 35,723.37 = **7,625.50** ✓ (agrees to the statement's stated ending balance).

## Bank side

| | Amount | Document |
|---|---:|---|
| Bank statement ending balance, 03/31/2026 | 7,625.50 | bank_statement_2026-03.pdf (ending balance line) |
| **Add:** deposits in transit | | |
| Check #4471, Delgado, receipt recorded 03/31, not on statement | +6,250.00 | GL ref DEP 2026-03-31 "Deposit — Delgado (check #4471)"; ar_aging_2026-03-31.pdf footnote 1: "Check #4471 received 3/31, deposited same day" |
| **Less:** outstanding checks (recorded in GL, not on statement) | | |
| Check #2041 — Austin Energy | −612.40 | GL ref #2041 2026-03-28 |
| Check #2044 — Blum hardware dist. | −2,944.80 | GL ref #2044 2026-03-30 |
| **Adjusted bank balance** | **10,318.30** | |

Arithmetic: 7,625.50 + 6,250.00 − 612.40 − 2,944.80 = **10,318.30**

## Book side

| | Amount | Document |
|---|---:|---|
| GL 1000 balance before adjustments | 6,041.30 | GL opening (overdrawn) −7,013.13 + March deposits 52,300.00 − March payments 39,245.57 = 6,041.30 (general_ledger_2026-03.csv; opening agrees to Feb TB credit column 7,013.13) |
| **Add:** credit not on books — 03/21 MOBILE DEPOSIT | +4,312.00 | bank_statement_2026-03.pdf line 03/21 (AJE-1) |
| **Less:** debit not on books — 03/31 monthly service fee | −35.00 | bank_statement_2026-03.pdf line 03/31 (AJE-4) |
| **Adjusted book balance** | **10,318.30** | |

Arithmetic: 6,041.30 + 4,312.00 − 35.00 = **10,318.30**

## Difference remaining

**$0.00.** Adjusted bank balance = adjusted book balance = 10,318.30. Every reconciling item
above is tied to a named document. No plug or unsupported entry was used.

## Item-by-item tie-out (March bank statement vs GL)

| Statement line | Amount | GL entry | Status |
|---|---:|---|---|
| 03/03 deposit Whitmore progress | 9,200.00 | DEP 03/03 | cleared |
| 03/05 ACH Summit card payment | 3,188.22 | CCPAY 03/05 | cleared |
| 03/09 check #2036 shop rent | 4,500.00 | #2036 03/07 | cleared |
| 03/10 deposit Cole final (Feb inv) | 14,350.00 | DEP 03/10 | cleared |
| 03/13 ACH Gusto payroll net | 7,100.00 | PAYROLL 03/13 | cleared |
| 03/13 ACH Gusto tax | 653.20 | PAYROLL 03/13 | cleared |
| 03/14 online transfer from *4420 | 1,500.00 | XFER 03/14 | cleared — was posted to Sales; client confirms it is his personal checking funding payroll, so reclassified to Owner's contributions 3100 (AJE-3) |
| 03/15 check #2038 Austin Lumber | 7,315.00 | #2038 03/13 | cleared |
| 03/17 deposit Alvarez (Feb inv) | 11,800.00 | DEP 03/17 | cleared |
| 03/21 mobile deposit | 4,312.00 | **none** | added to books, AJE-1; payor unidentified → 2100 suspense |
| 03/22 check #2040 Cascade CH-7731 | 4,860.00 | #2040 03/20 | cleared — single payment; invoice was booked twice, duplicate reversed AJE-2 |
| 03/24 deposit Whitmore balance | 9,200.00 | DEP 03/24 | cleared |
| 03/27 ACH Gusto payroll net | 7,100.00 | PAYROLL 03/27 | cleared |
| 03/27 ACH Gusto tax | 653.20 | PAYROLL 03/27 | cleared |
| 03/31 LOC 88-2210 loan interest | 318.75 | LOC 03/31 | cleared |
| 03/31 monthly service fee | 35.00 | **none** | added to books, AJE-4 |
| — | | DEP 03/31 Delgado #4471 6,250.00 | deposit in transit |
| — | | #2041 03/28 612.40; #2044 03/30 2,944.80 | outstanding checks |

## Summit Visa card (ending 0917) — reconciled, no adjustment needed

Previous balance 3,188.22 = GL 2050 opening (Feb TB) ✓; payment 3,188.22 recorded GL CCPAY 03/05
and cleared bank 03/05 ✓; new charges 2,306.12 = 182.40 + 214.77 + 1,188.00 + 212.00 + 341.10 + 167.85,
all six posted in GL ✓; statement new balance 3,188.22 + 2,306.12 − 3,188.22 = **2,306.12** =
GL 2050 after activity ✓. (Reclassifications of two charges — insurance/software to prepaid,
personal dinner to draws — do not affect the card balance; see AJE-5 through AJE-7.)

## Note on the owner's request

The owner's email asked for a "clean" rec and suggested putting anything off "somewhere sensible."
Per the library standard (bank_rec_standard.md), an unsupported entry used to force agreement
would misstate the records and, for statements furnished to a lender, may be a false statement.
Here nothing needed to be forced: the account ties to a **0.00** difference with documented items.
One receipt remains *unidentified* — the 03/21 mobile deposit of 4,312.00. The client and his office
manager were asked and neither can say who sent it; the client asked to "park it somewhere." It is
parked exactly where the close policy says an uncategorized item goes: suspense liability 2100 —
visible on the balance sheet and listed in `open_items.md`, not buried in revenue or any other
account. (The 03/14 1,500.00 transfer is no longer unidentified: the client confirmed it is his own
money from personal checking *4420, now recorded as an owner contribution in 3100.)
