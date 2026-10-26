# Brightline Cabinetry LLC — Bank Reconciliation

**Account:** Hill Country Community Bank — Cash — Operating (HCCB ...2210)
**Period:** 03/01/2026 – 03/31/2026
**Prepared:** Monthly close as of 03/31/2026
**Form and rules applied:** `library/bank_rec_standard.md` (via `library/INDEX.md`); `library/close_policy.md`; close checklist item 3 (client document `documents/close_checklist.md`). Every difference below is tied to a specific document.

---

## A. Balance per bank

| # | Item | Amount | Source |
|---|------|--------:|--------|
| 1 | Ending balance per statement, 03/31/2026 | 7,625.50 | `documents/bank_statement_2026-03.pdf` (ending balance) |
| 2 | **+ Deposits in transit** — Delgado check #4471, deposited 03/31 | 6,250.00 | `documents/general_ledger_2026-03.csv` 03/31 rows "Deposit — Delgado (check #4471)"; not present in the statement's transaction list; `documents/ar_aging_2026-03-31.pdf` footnote ¹ ("Check #4471 received 3/31, deposited same day") |
| 3 | **− Outstanding checks** — total 3,557.20 (see detail below) | (3,557.20) | see below |
| 4 | **+** Bank errors | 0.00 | statement foots exactly (see Section C) |
| | **Adjusted bank balance** | **10,318.30** | |

Arithmetic: 7,625.50 + 6,250.00 − 3,557.20 = **10,318.30**

Outstanding checks detail (written on/before 03/31; absent from the statement's cleared list — the only checks shown cleared are #2036, #2038, #2040):

| Check | Payee / memo | Date written | Amount | Source |
|-------|-------------|-----------|--------:|--------|
| #2041 | Austin Energy (A/P payment) | 03/28 | 612.40 | `documents/general_ledger_2026-03.csv` 03/28 rows |
| #2044 | Blum hardware dist. 55102 (A/P payment) | 03/30 | 2,944.80 | `documents/general_ledger_2026-03.csv` 03/30 rows |
| | **Total outstanding** | | **3,557.20** | 612.40 + 2,944.80 = 3,557.20 |

---

## B. Balance per books (Cash 1000)

| # | Item | Amount | Source |
|---|------|--------:|--------|
| 1 | GL cash (1000) per books before close adjustments, 03/31 | 6,041.30 | `documents/trial_balance_2026-02-28.csv` + `documents/general_ledger_2026-03.csv` (roll below) |
| 2 | **+ Credit not recorded in books** — mobile deposit 03/21 | 4,312.00 | `documents/bank_statement_2026-03.pdf` 03/21 "MOBILE DEPOSIT"; no GL row exists; recorded in the close by **AJE-3** (1000 DR / 2100 CR — payor unidentified per owner and office manager inquiry, `library/close_policy.md` suspense rule) |
| 3 | **− Debit not recorded in books** — monthly service fee 03/31 | (35.00) | `documents/bank_statement_2026-03.pdf` 03/31 "MONTHLY SERVICE FEE"; no GL row exists; recorded in the close by **AJE-4** (6700 DR / 1000 CR) |
| 4 | **± Book errors affecting cash** | 0.00 | none — see note below |
| | **Adjusted book balance** | **10,318.30** | |

Arithmetic: 6,041.30 + 4,312.00 − 35.00 = **10,318.30**

Supporting roll-forward of the book balance (all amounts net out of `documents/general_ledger_2026-03.csv` and `documents/trial_balance_2026-02-28.csv`):

| Component | Amount | Check |
|-----------|--------:|-------|
| Opening GL cash 02/28 | (7,013.13) | agrees to statement beginning balance |
| + Book receipts | 52,300.00 | cleared receipts 46,050.00 (9,200 Whitmore 03/03 + 14,350 Cole 03/10 + 11,800 Alvarez 03/17 + 1,500 transfer 03/14 + 9,200 Whitmore 03/24) + Delgado deposit 6,250.00 (in transit) — ties to statement credits of 50,362.00 (46,050.00 + the 4,312.00 mobile deposit) |
| − Book disbursements | 39,245.57 | statement-cleared 35,688.37 (Summit payment 3,188.22; #2036 4,500.00; #2038 7,315.00; #2040 4,860.00; Gusto 7,100.00 + 653.20 ×2; LOC interest 318.75) + outstanding 3,557.20 |
| = GL cash before close adjustments | **6,041.30** | 6,041.30 = 52,300.00 − 39,245.57 − 7,013.13 |

Note on book errors (none affect cash): the March duplicate posting of Cascade bill CH-7731 (corrected by **AJE-1**) is an A/P/expense misposting, and the online transfer in of 1,500.00 posted to Sales (corrected by **AJE-2**) is a classification misposting — cash itself posted correctly in both cases, so neither creates a difference in this reconciliation.

---

## C. Statement cross-foot and line-by-line match to the books

Statement totals per the summary panel (credits 50,362.00; debits 35,723.37) foot exactly to the listed transactions; **no bank errors** (`documents/bank_statement_2026-03.pdf`). Beginning balance (7,013.13) agrees to the 02/28 GL cash balance.

| Statement date | Description | Statement amount | Books? | Disposition |
|---------------|-------------|----------------:|--------|-------------|
| 03/03 | DEPOSIT WHITMORE PROGRESS | +9,200.00 | Yes | booked; cleared |
| 03/05 | ACH DEBIT SUMMIT CARD SERVICES | −3,188.22 | Yes | card payment; cleared |
| 03/09 | CHECK #2036 | −4,500.00 | Yes | A/P — shop rent; cleared |
| 03/10 | DEPOSIT COLE FINAL (FEB INV) | +14,350.00 | Yes | booked; cleared |
| 03/13 | ACH DEBIT GUSTO PAYROLL NET | −7,100.00 | Yes | cleared |
| 03/13 | ACH DEBIT GUSTO TAX | −653.20 | Yes | cleared |
| 03/14 | ONLINE TRANSFER FROM CHK *4420 | +1,500.00 | Yes (misclassified) | posted to cash; reclassified out of Sales by **AJE-2**; owner has confirmed the funds are his → reclassified to 3100 Owner's contributions by **AJE-6** |
| 03/15 | CHECK #2038 | −7,315.00 | Yes | A/P — Austin Lumber; cleared |
| 03/17 | DEPOSIT ALVAREZ (FEB INV) | +11,800.00 | Yes | booked; cleared |
| 03/21 | MOBILE DEPOSIT | +4,312.00 | **No** | **AJE-3**; payor unidentified (owner and office manager could not identify — QUESTIONS.md Q1) → 2100 suspense |
| 03/22 | CHECK #2040 | −4,860.00 | Yes | A/P — Cascade CH-7731; cleared |
| 03/24 | DEPOSIT WHITMORE BALANCE | +9,200.00 | Yes | booked; cleared |
| 03/27 | ACH DEBIT GUSTO PAYROLL NET | −7,100.00 | Yes | cleared |
| 03/27 | ACH DEBIT GUSTO TAX | −653.20 | Yes | cleared |
| 03/31 | LOAN INTEREST LOC 88-2210 | −318.75 | Yes | booked; cleared |
| 03/31 | MONTHLY SERVICE FEE | −35.00 | **No** | **AJE-4** |
| — | GL-only payments not yet cleared: #2041 612.40; #2044 2,944.80 | | | outstanding checks |
| — | GL-only receipt not yet credited: Delgado #4471 6,250.00 | | | deposit in transit |

Foots: credits 9,200.00 + 14,350.00 + 1,500.00 + 11,800.00 + 4,312.00 + 9,200.00 = 50,362.00; debits 3,188.22 + 4,500.00 + 7,100.00 + 653.20 + 7,315.00 + 4,860.00 + 7,100.00 + 653.20 + 318.75 + 35.00 = 35,723.37 — both agree to the statement summary panel.

---

## D. Difference

> Adjusted bank balance 10,318.30 − adjusted book balance 10,318.30 = **0.00**

The adjusted book balance equals account 1000 in `deliverable/trial_balance_2026-03-31.json` (10,318.30 debit), so the reconciliation is fully closed. No differences remain; nothing was cleared or "sensibly placed" without a document, per `library/bank_rec_standard.md`.

---

## E. Summit card — Business Visa ending 0917 (close checklist item 4)

| Item | Amount | Source |
|------|--------:|--------|
| Statement ending balance 03/31 (previous 3,188.22 − payments 3,188.22 + new charges 2,306.12) | 2,306.12 | `documents/credit_card_statement_summit_2026-03.pdf` |
| Books: account 2050 at 03/31 | 2,306.12 | `deliverable/trial_balance_2026-03-31.json` |

**Difference: 0.00** — the card reconciles with no reconciling items.

Classification notes per statement line (charges: Shell 182.40 03/03; Home Depot 214.77 03/08; CabinetVision license 1,188.00 03/11; Uchi dinner 212.00 03/15; Fastenal 341.10 03/22; Shell fuel 167.85 03/25 = 2,306.12):

- CabinetVision annual license 1,188.00 — coverage **04/2026–03/2027** printed on the statement; nothing consumed at 03/31, so capitalized to prepaid 1300 by **AJE-5** per `library/close_policy.md` (items covering more than one month are prepaid).
- Uchi dinner 212.00 — personal per the owner ("anniversary dinner, grabbed the wrong card"), reclassified from 6500 Meals to 3200 Owner's draws by **AJE-7** per `library/close_policy.md` (owner personal charges through business accounts go to draws). Card liability (2050) unchanged.
