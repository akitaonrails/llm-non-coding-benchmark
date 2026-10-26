# Brightline Cabinetry LLC — operating account 2210
## March 31, 2026 bank reconciliation

Amounts in dollars. The bank and book sides follow the standard form in [bank_rec_standard.md](../library/bank_rec_standard.md). “Document” identifies the client record supporting each amount.

### Bank side

| Item | Add | Deduct | Document and trace |
|---|---:|---:|---|
| March 31 statement ending balance | 7,625.50 | — | `bank_statement_2026-03.pdf`, ending balance |
| Deposit in transit: Delgado check #4471, deposited March 31 | 6,250.00 | — | `general_ledger_2026-03.csv`, March 31 DEP; `ar_aging_2026-03-31.pdf`, footnote 1; absent from March bank statement |
| Outstanding check #2041, Austin Energy | — | 612.40 | `general_ledger_2026-03.csv`, March 28 #2041; absent from March bank statement |
| Outstanding check #2044, Blum hardware | — | 2,944.80 | `general_ledger_2026-03.csv`, March 30 #2044; absent from March bank statement |
| **Adjusted bank balance** | **10,318.30** | | **7,625.50 + 6,250.00 − 612.40 − 2,944.80** |

### Book side

| Item | Add | Deduct | Document and trace |
|---|---:|---:|---|
| Unadjusted March 31 GL cash | 6,041.30 | — | `trial_balance_2026-02-28.csv`, opening cash credit 7,013.13; `general_ledger_2026-03.csv`, March cash debits 52,300.00 and credits 39,245.57. Calculation: −7,013.13 + 52,300.00 − 39,245.57 = 6,041.30. The ledger's February 26 row is excluded from March activity by date; it also has no cash line. |
| Unrecorded March 21 mobile deposit, AJE-6 | 4,312.00 | — | `bank_statement_2026-03.pdf`, March 21 mobile deposit; no corresponding GL deposit. Owner and office cannot identify payer; credited to 2100 suspense under [close_policy.md](../library/close_policy.md). |
| Unrecorded March 31 monthly service fee, AJE-7 | — | 35.00 | `bank_statement_2026-03.pdf`, March 31 fee; no corresponding GL charge |
| **Adjusted book balance** | **10,318.30** | | **6,041.30 + 4,312.00 − 35.00** |

**Remaining bank reconciliation difference: $0.00** ($10,318.30 − $10,318.30). The deposit's payer and purpose remain unknown; its suspense balance and the separate A/R difference are disclosed in `open_items.md`. A numerical bank tie does not resolve those items. The treatment of unknown receipts and unexplained differences follows [close_policy.md](../library/close_policy.md) and [bank_rec_standard.md](../library/bank_rec_standard.md).
