# Brightline Cabinetry LLC — operating bank reconciliation, March 31, 2026

Account ending 2210. Amounts are dollars. The `documents/` names below identify transaction evidence; the accounting authorities are `library/bank_rec_standard.md` and `library/close_policy.md`, both listed in `library/INDEX.md`.

## Bank side

| Item | Amount | Evidence |
|---|---:|---|
| Bank statement ending balance, March 31 | 7,625.50 | `documents/bank_statement_2026-03.pdf`, ending balance |
| Add: Delgado check #4471, deposited March 31; deposit in transit | +6,250.00 | `documents/general_ledger_2026-03.csv`, March 31 DEP; `documents/ar_aging_2026-03-31.pdf`, footnote 1; absent from March bank statement |
| Less: outstanding check #2041, Austin Energy | −612.40 | `documents/general_ledger_2026-03.csv`, March 28 #2041; absent from March bank statement |
| Less: outstanding check #2044, Blum hardware | −2,944.80 | `documents/general_ledger_2026-03.csv`, March 30 #2044; absent from March bank statement |
| **Adjusted bank balance** | **10,318.30** | 7,625.50 + 6,250.00 − 612.40 − 2,944.80 |

## Book side

| Item | Amount | Evidence |
|---|---:|---|
| GL cash before adjustments | 6,041.30 | `documents/trial_balance_2026-02-28.csv`: (7,013.13) opening; `documents/general_ledger_2026-03.csv`: March cash debits 52,300.00, credits 39,245.57; (7,013.13) + 52,300.00 − 39,245.57 = 6,041.30 |
| Add: unrecorded March 21 mobile deposit, AJE-3 | +4,312.00 | `documents/bank_statement_2026-03.pdf`, March 21 mobile deposit; no matching entry in `documents/general_ledger_2026-03.csv` |
| Less: unrecorded March 31 service fee, AJE-4 | −35.00 | `documents/bank_statement_2026-03.pdf`, March 31 monthly service fee; no matching entry in `documents/general_ledger_2026-03.csv` |
| **Adjusted book balance** | **10,318.30** | 6,041.30 + 4,312.00 − 35.00 |

**Difference: $0.00** (10,318.30 − 10,318.30). The $4,312 receipt remains unidentified. Ray and Carla could not identify it, so AJE-3 credits unidentified receipts / suspense (2100), as required by `library/close_policy.md`. A balanced reconciliation does not establish that the receipt is revenue or settle the A/R subledger discrepancy described in `open_items.md`.

The bank statement itself checks: (7,013.13) beginning + 50,362.00 credits − 35,723.37 debits = 7,625.50 ending. The February-dated Cascade posting appearing in the ledger file is excluded from the March trial-balance rollforward; the March-dated duplicate is reversed by AJE-1.
