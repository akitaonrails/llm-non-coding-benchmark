# Bank Reconciliation — Cash — Operating, Hill Country Community Bank (account ending 2210)

**Period:** March 1 – March 31, 2026
**Prepared:** October 25, 2026, outsourced accounting, per *Brightline — monthly close checklist* item 3 and the bank-rec standard form (`library/bank_rec_standard.md`).
Every reconciling item below cites a specific document. No plug or unsupported entry was used.

## 1. Bank side

| | | Source |
|---|---:|---|
| Bank statement ending balance, 3/31/26 | **7,625.50** | `bank_statement_2026-03.pdf` (summary: begin (7,013.13) + credits 50,362.00 − debits 35,723.37 = 7,625.50 — statement is internally consistent) |
| Add: Deposit in transit — Delgado check #4471, received and deposited 3/31/26, not credited by bank until April | +6,250.00 | GL ref DEP 3/31/26; `ar_aging_2026-03-31.pdf` note 1 ("Check #4471 received 3/31, deposited same day") |
| Less: Outstanding check #2041 — Austin Energy, issued 3/28/26 | (612.40) | GL ref #2041 3/28/26; no clearing line on statement |
| Less: Outstanding check #2044 — Blum hardware, issued 3/30/26 | (2,944.80) | GL ref #2044 3/30/26; no clearing line on statement |
| Bank errors | — none identified | |
| **Adjusted bank balance** | **10,318.30** | 7,625.50 + 6,250.00 − 612.40 − 2,944.80 |

## 2. Book (GL) side

| | | Source |
|---|---:|---|
| GL 1000 balance before adjustments, 3/31/26 | **6,041.30** | Feb 28 TB (7,013.13) credit balance, i.e. overdrawn, per `trial_balance_2026-02-28.csv`; March deposits 52,300.00 − March disbursements 39,245.57 per `general_ledger_2026-03.csv`: −7,013.13 + 52,300.00 − 39,245.57 = 6,041.30 |
| Add: 3/21/26 mobile deposit not recorded in the GL | +4,312.00 | `bank_statement_2026-03.pdf` line 03/21 "MOBILE DEPOSIT"; recorded by **AJE-2** to suspense 2100 (payer unidentified — see open items) |
| Less: 3/31/26 monthly service fee not recorded in the GL | (35.00) | `bank_statement_2026-03.pdf` line 03/31; recorded by **AJE-3** to 6700 Bank charges |
| Book errors | — none identified | |
| **Adjusted book balance** | **10,318.30** | 6,041.30 + 4,312.00 − 35.00 |

## 3. Difference

| | |
|---|---:|
| Adjusted bank balance | 10,318.30 |
| Adjusted book balance | 10,318.30 |
| **Difference** | **0.00** |

The reconciliation ties with no residual unexplained difference. Every line above is supported by the document cited; nothing was "put somewhere sensible" to force agreement — the rec ties because each bank and book item was matched to a document.

## 4. Line-by-line matching (statement ↔ GL)

| Bank stmt line | Amt | GL entry | Status |
|---|---:|---|---|
| 03/03 deposit Whitmore progress | 9,200.00 | DEP 3/3 | matched |
| 03/05 ACH Summit card payment | 3,188.22 | CCPAY 3/5 | matched |
| 03/09 check #2036 (shop rent) | 4,500.00 | #2036 3/7 | matched, cleared |
| 03/10 deposit Cole final (Feb inv) | 14,350.00 | DEP 3/10 | matched |
| 03/13 Gusto payroll net | 7,100.00 | PAYROLL 3/13 | matched |
| 03/13 Gusto payroll tax | 653.20 | PAYROLL 3/13 | matched |
| 03/14 online transfer from check *4420 | 1,500.00 | XFER 3/14 | cash matched; had been keyed to Sales — reversed by AJE-4 and classified to 3100 Owner's contributions per owner confirmation (AJE-8; open_items.md §2) |
| 03/15 check #2038 (Austin Lumber) | 7,315.00 | #2038 3/13 | matched, cleared |
| 03/17 deposit Alvarez (Feb inv) | 11,800.00 | DEP 3/17 | matched |
| 03/21 mobile deposit | 4,312.00 | — | **book reconciling item, AJE-2** |
| 03/22 check #2040 (Cascade CH-7731) | 4,860.00 | #2040 3/20 | matched, cleared |
| 03/24 deposit Whitmore balance | 9,200.00 | DEP 3/24 | matched |
| 03/27 Gusto payroll net | 7,100.00 | PAYROLL 3/27 | matched |
| 03/27 Gusto payroll tax | 653.20 | PAYROLL 3/27 | matched |
| 03/31 loan interest LOC 88-2210 | 318.75 | LOC 3/31 | matched |
| 03/31 monthly service fee | 35.00 | — | **book reconciling item, AJE-3** |
| — | 6,250.00 | DEP 3/31 (Delgado #4471) | **deposit in transit** |
| — | 612.40 | #2041 3/28 | **outstanding check** |
| — | 2,944.80 | #2044 3/30 | **outstanding check** |

Opening balances agree with no carry-over items: GL 1000 at 2/28 was (7,013.13) and the bank's 3/1 beginning balance was (7,013.13).

## 5. Supplement — Summit Visa card (ending 0917), close-checklist item 4

| | |
|---|---:|
| Card statement new balance, 3/31/26 (`credit_card_statement_summit_2026-03.pdf`) | 2,306.12 |
| GL 2050 (AJE-7 does not touch 2050 — it reclasses the expense side, Meals 6500 → draws 3200): 3,188.22 opening + charges 2,306.12 − payment 3,188.22 (`general_ledger_2026-03.csv` refs CC, CCPAY) | 2,306.12 |
| **Difference** | **0.00** |

All six statement charges are on the books. Per the owner's policy, the 3/15 "Uchi dinner" charge (212.00; statement note: "4 guests, Saturday 8:40pm") was reclassified from Meals 6500 to Owner's draws 3200 (AJE-7) as a personal charge — owner confirmed on 2026-10-25 ("my anniversary dinner, I grabbed the wrong card. Put it on me."); the classification is final.

## 6. Notes for the reader (lender copy)

- The account operated at a **negative balance part of the month**: (7,013.13) at 3/1, negative again 3/5 through 3/9 (low point (5,501.35)) and on 3/15 ((4,719.55)), restored by the Cole and Alvarez deposits that cleared 3/10 and 3/17 (see statement running-balance column). Adjusted cash at 3/31 is positive 10,318.30.
- The 3/14 transfer of 1,500.00 is in adjusted cash and is now classified as an **owner contribution (account 3100)** — the owner confirmed on 2026-10-25 that he moved the money from his personal checking to cover payroll: "my money, not a sale" (AJE-8). The 3/21 mobile deposit of 4,312.00 is also in adjusted cash but remains in **suspense (account 2100, balance 4,312.00)**: neither the owner nor his office manager can identify it, and per client policy an unidentified receipt is not revenue until matched and may not sit in suspense past the next month-end (April close).
- Statement carries the bank's 60-day error-reporting clause; no bank-side exceptions were identified.
