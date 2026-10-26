# Bank Reconciliation — Brightline Cabinetry LLC
**Account:** Cash — Operating, Hill Country Community Bank, acct …2210 (COA 1000)
**Period:** March 1 – March 31, 2026 · Prepared 2026-10-25 by outsourced accountant
**Form per:** `library/bank_rec_standard.md` (AICPA practice aid excerpt)

## Reconciling items and their documents
Every item below is supported by a named document. No plug or unsupported entry is used.

| # | Item | Amount | Supporting document |
|---|---|---|---|
| DIT-1 | Deposit in transit — Delgado check #4471, received & deposited 3/31, not yet on bank statement | +6,250.00 | `general_ledger_2026-03.csv` 3/31 "DEP — Delgado (check #4471)"; `ar_aging_2026-03-31.pdf` fn ¹ |
| OSC-1 | Outstanding check #2041 — Austin Energy, written 3/28, not on statement | −612.40 | GL 3/28 "#2041"; absent from `bank_statement_2026-03.pdf` |
| OSC-2 | Outstanding check #2044 — Blum hardware, written 3/30, not on statement | −2,944.80 | GL 3/30 "#2044"; absent from statement |
| BFE-1 | Bank error | none identified | statement internal check below ties |
| BOO-1 | 3/21 mobile deposit on bank, not on books — payer unidentified → recorded to 2100 suspense (AJE-1) | +4,312.00 | `bank_statement_2026-03.pdf` 03/21 "MOBILE DEPOSIT"; policy `library/close_policy.md` (unidentified receipts → 2100, not revenue) |
| BOO-2 | Monthly service fee, on bank, not on books (AJE-2) | −35.00 | `bank_statement_2026-03.pdf` 03/31 "MONTHLY SERVICE FEE" |
| BOE-1 | Book error in cash | none | see duplicate-bill entry AJE-3 — it does not touch cash (check #2040 cleared once) |

## Reconciliation

**Bank side** (`bank_statement_2026-03.pdf`)

| | |
|---|---:|
| Bank ending balance 3/31/2026 | 7,625.50 |
| + Deposits in transit (DIT-1) | +6,250.00 |
| − Outstanding checks (#2041 612.40, #2044 2,944.80; total) | −3,557.20 |
| ± Bank errors | 0.00 |
| **Adjusted bank balance** | **10,318.30** |

Bank statement internal arithmetic: beginning (7,013.13) + credits 50,362.00 − debits 35,723.37 = **7,625.50** ✔ (agrees with printed ending balance).

**Book side** (`general_ledger_2026-03.csv`, acct 1000)

| | |
|---|---:|
| GL cash balance 3/31/2026, before adjustments | 6,041.30 |
| + Credits not yet recorded — mobile deposit 3/21 (BOO-1, AJE-1) | +4,312.00 |
| − Debits not yet recorded — service fee 3/31 (BOO-2, AJE-2) | −35.00 |
| ± Book errors in cash | 0.00 |
| **Adjusted book balance** | **10,318.30** |

GL cash roll-forward: beginning −7,013.13 (Feb TB acct 1000, = statement beginning) + bank-side receipts 52,300.00 (9,200.00 + 14,350.00 + 11,800.00 + 9,200.00 + 6,250.00 + 1,500.00) − recorded payments 39,245.57 (4,500.00 + 7,315.00 + 4,860.00 + 612.40 + 2,944.80 + 7,100.00 + 653.20 + 7,100.00 + 653.20 + 3,188.22 + 318.75) = 6,041.30. (LOC interest 318.75 was already booked 3/31.)

**Difference remaining: 0.00.** The two adjusted balances agree, tied item-by-item to the documents above.

## Items examined and cleared (no reconciling entry needed)
- Every bank deposit and debit was matched to a GL entry: 3/3 Whitmore 9,200.00; 3/5 Summit payment 3,188.22; 3/9 #2036 4,500.00; 3/10 Cole 14,350.00; 3/13 Gusto payroll 7,100.00 + tax 653.20; 3/14 transfer *4420 1,500.00 (owner's personal-checking transfer, reclassified to contributions per AJE-6 — cash unaffected); 3/15 #2038 7,315.00; 3/17 Alvarez 11,800.00; 3/22 #2040 4,860.00; 3/24 Whitmore 9,200.00; 3/27 payroll + tax; 3/31 LOC interest 318.75.
- Cascade Hardwoods check #2040 (4,860.00) cleared once on 3/22; the bill itself was double-booked on the books — corrected by AJE-3, which does not affect cash.
- Check sequence gap (#2037, #2039, #2042, #2043 appear on neither statement nor books) — not a reconciling item; reported in `open_items.md`.

## Summit Visa card reconciliation (`credit_card_statement_summit_2026-03.pdf`, COA 2050)
Opening balance 3,188.22 (paid in full 3/5 by ACH, cleared — matches GL CCPAY entry). Statement new charges 2,306.12 = GL postings 182.40 + 214.77 + 1,188.00 + 212.00 + 341.10 + 167.85 ✔. Statement closing balance **2,306.12 = GL 2050 balance 2,306.12** ✔. One charge (Uchi dinner 212.00) was confirmed by the owner as personal ("my anniversary dinner… put it on me") and is reclassified from 6500 Meals to 3200 Owner's draws per close checklist #4 via AJE-7; this affects classification only, not cash.

## Note to the lender
The reconciliation ties to zero with no unexplained difference. Disclosures: 6,250.00 deposit in transit and 3,557.20 outstanding checks listed above; a 4,312.00 March deposit remains in suspense (2100) — the payer is still unidentified (owner and office manager Carla checked, neither knows), so it is held in suspense per policy rather than recognized as revenue; the account was briefly overdrawn during March (min −5,501.35 on 3/9, −4,719.55 on 3/15). Separately, the accounts-receivable balance does **not** agree to its subledger — see `open_items.md` — and is material; it should not be presented to the lender as supported without that detail.
