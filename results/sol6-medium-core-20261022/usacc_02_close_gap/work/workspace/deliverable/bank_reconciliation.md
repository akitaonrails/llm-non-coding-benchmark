# Brightline Cabinetry LLC — operating account ending 2210
## Bank reconciliation at March 31, 2026

Amounts are dollars. The bank reconciliation method and treatment of unexplained differences follow [bank_rec_standard.md](../library/bank_rec_standard.md). The support column identifies the client records used for each amount.

| Bank side | Amount | Supporting document / transaction |
|---|---:|---|
| March 31 statement ending balance | 7,625.50 | `bank_statement_2026-03.pdf`, ending balance |
| Add: deposit in transit, Delgado check #4471 received and deposited March 31 | 6,250.00 | `general_ledger_2026-03.csv`, March 31 DEP; `ar_aging_2026-03-31.pdf`, footnote 1; no Delgado deposit in `bank_statement_2026-03.pdf` |
| Less: outstanding check #2041, Austin Energy | (612.40) | `general_ledger_2026-03.csv`, March 28 #2041; no #2041 clearing in `bank_statement_2026-03.pdf` |
| Less: outstanding check #2044, Blum hardware | (2,944.80) | `general_ledger_2026-03.csv`, March 30 #2044; no #2044 clearing in `bank_statement_2026-03.pdf` |
| **Adjusted bank balance** | **10,318.30** | 7,625.50 + 6,250.00 − 612.40 − 2,944.80 |

| Book side | Amount | Supporting document / transaction |
|---|---:|---|
| March 31 unadjusted GL cash | 6,041.30 | `trial_balance_2026-02-28.csv`, cash credit 7,013.13; `general_ledger_2026-03.csv`, March dated cash activity net debit 13,054.43 |
| Add: March 21 mobile deposit absent from GL, AJE-3 | 4,312.00 | `bank_statement_2026-03.pdf`, March 21 mobile deposit; absent from `general_ledger_2026-03.csv` |
| Less: March 31 monthly service fee absent from GL, AJE-4 | (35.00) | `bank_statement_2026-03.pdf`, March 31 fee; absent from `general_ledger_2026-03.csv` |
| **Adjusted book balance** | **10,318.30** | 6,041.30 + 4,312.00 − 35.00 |

**Reconciliation difference: $0.00; unresolved identification exception: $4,312.00.** The deposit is recorded to unidentified receipts / suspense under [close_policy.md](../library/close_policy.md). Ray and Carla could not identify its payer or purpose, and the client has no further detail. A zero bank difference does not resolve that exception. The March 14 $1,500 transfer appears on both bank and GL; AJE-2 corrects its classification from sales to owner's contributions based on Ray's confirmation. It is not a reconciling difference. No unsupported balancing entry was posted.

The February 28 cash credit balance of $7,013.13 agrees to the bank's March beginning overdraft of $7,013.13. The February 26 Cascade ledger history was excluded from the March roll-forward because it predates the opening trial balance.
