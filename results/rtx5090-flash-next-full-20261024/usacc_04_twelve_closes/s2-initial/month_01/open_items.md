# Open items — January 2025 close
**To:** Board, Northwind Analytics Inc. **From:** Controller **Date of close:** 2025-01-31 (package due 2025-02-10 per Board policy 5)

## 1. Prior-period error found and corrected (restated opening balances) — material

The opening trial balance at 2025-01-01 carried January-2025 billings that had been posted in error in **December 2024**. Three independent pieces of evidence:

| Anomaly in opening TB | Amount | Matches exactly |
|---|---:|---|
| 4000 Subscription revenue has a balance at 2025-01-01 (should be nil at a year start) | 30,450.00 Cr | Sum of the 24 monthly invoices dated 2025-01-01 = 30,450.00 |
| 2200 Deferred revenue per TB | 65,000.00 Cr | Client opening note states opening deferred revenue is **41,000.00** (Trestle prior contract only); excess = 24,000.00 = Trestle renewal INV-2225, dated 2025-01-01 |
| Implied A/R overstatement (residual) | 54,450.00 | 30,450.00 + 24,000.00 = total January billing; 92,650.00 − 54,450.00 = 38,200.00 |

Under ASC 606-10-25-1 no 2025 contract existed at 31-Dec-2024 (order form and invoices are dated 2025-01-01), and nothing had been performed, so the December postings were an error in applying GAAP. Per ASC 250-10-45-23 an error in previously issued statements is corrected by **restating** the affected periods — not by a quiet going-forward fix (which the library expressly prohibits, ASC 250-10-50-7).

**Correction made:** JE-2025-001, dated **2025-01-01** (restatement of opening balances, disclosed in the ledger itself): Dr 4000 30,450.00; Dr 2200 24,000.00; Cr 1100 54,450.00. January activity was then booked normally (JE-2025-002/003). Effect on restated opening balances: A/R 92,650.00 → **38,200.00**; deferred revenue 65,000.00 → **41,000.00**; opening 2025 revenue balance 0.00. January 2025 revenue recognized is 40,650.00 (correct on the corrected opening).

**Judgment call / assumption (flagged, not verifiable from the file):** the offset of the error was taken to **accounts receivable**, because (a) cash and deferred-revenue anomalies are individually explained and cash agrees to the bank exactly; (b) the implied A/R excess 54,450.00 equals the January billing total to the cent. No A/R aging at 31-Dec-2024 was provided. If the true offset was elsewhere, I will correct January — question asked in `QUESTIONS.md`.

**To the Board:** if the prior bookkeeper issued December-2024 or full-year-2024 statements to the Board or a lender that included these postings, those statements need restatement per ASC 250 (nature: revenue and contract liability for 2025 contracts recognized one period early; effects: A/R −54,450.00, deferred revenue −24,000.00, revenue −30,450.00, opening retained deficit understated by 30,450.00). My correction flows through the 4000 opening balance rather than 3900, because I could not verify whether 2024 books were closed with the error inside; ask Q1 below. Either way the corrected 2025 YTD revenue is the same.

## 2. Payroll — agrees to register and bank (no force)
Gross 54,404.00 + employer taxes/benefits 5,076.00 = 59,480.00 expense. Cash out: 48,200.00 net + 11,280.00 tax = 59,480.00, matching both bank debits exactly. Internal identity: 54,404.00 − 48,200.00 (withholding 6,204.00) + 5,076.00 = 11,280.00 remitted; 2100 clears to zero. Nothing forced.

## 3. Deferred revenue
- Trestle prior contract: 8,200.00 released Jan (41,000.00 / 5 months Jan–May 2025 per client note). Closing 32,800.00.
- Trestle renewal: 24,000.00 billed upfront; invoice description says "billed upfront" but the **invoice wording does not drive accounting** — Board policy 1 and ASC 606-10-45-2 require deferral, 2,000.00/month. Closing 22,000.00.
- Judgment call: entire 54,800.00 kept in **2200 (current)**; all amounts release within 12 months. (The library has no non-current split; my practice choice, disclosed.)
- All 24 other contracts are monthly-billed; they never create contract liabilities at month-end (billed and collected within the month, and service for the billed month is complete at 31-Jan).

## 4. Items left open
1. **Opening A/R 38,200.00 (restated):** no customer breakdown/aging provided. Cannot assess collectability or identify which of the 25 known customers owes it. → Q2.
2. **Opening A/P 17,420.00:** no vendor bills or payment activity in January touched it (no bank debits other than January bills). Still unpaid at 31-Jan; aging unknown. → Q3.
3. **Prepaid expenses 9,600.00:** no supporting document in the file. Amortizing it blindly would be inventing a pattern, so I recorded **no amortization**; likely (but unverified) annual software/insurance, e.g. 800.00/month if it were a 12-month prepay starting 2025-01 — **this is arithmetic shown as a scenario, not an entry.** → Q4.
4. **Depreciation:** checklist prescribes 1,777.78/month (= 64,000.00 / 36, fully depreciated by Dec-2027; opening accumulated 21,333.00 ≈ 12 months). Note a 0.36 cumulative rounding quirk: 12 × 1,777.78 = 21,333.36 vs opening 21,333.00. Kept the checklist figure; adjust final month to make total equal exactly 64,000.00. Judgment call, immaterial.
5. **Stray file:** `documents/bank_statement.csv` (root) contains only **December 2025** transactions — outside January's scope; it appears to be a later-month statement delivered early. Ignored for this close; will reconcile it in December.
6. **January vendor bills were all paid in-month** (each traced to a bank ACH), so there are no accruals for these; open A/P remains item 2 above.
7. **No other liabilities noted:** no accrued bonuses, no interest, no taxes other than payroll noted in documents; none recorded. (No tax-return documents provided; no assumption of unrecorded tax expense stated — Q5.)

## 5. January result (arithmetic)
- Subscription revenue 40,650.00 = 30,450.00 monthly + 8,200.00 Trestle prior + 2,000.00 Trestle renewal.
- Expenses 83,327.78 = salaries 54,404.00 + employer taxes 5,076.00 + marketing 3,250.00 + rent 7,200.00 + hosting 9,920.00 + software 1,460.00 + depreciation 1,777.78 + G&A 240.00.
- **Net loss January 2025 = (42,677.78)** (40,650.00 − 83,327.78). Loss run-rate flagged for the Board.
- Loss-to-cash bridge: cash fell 27,100.00 (412,000.00 → 384,900.00). Difference vs. loss, 15,577.78 = non-cash depreciation 1,777.78 + collections ahead of revenue recognized 13,800.00 (renewal collected 24,000.00 but only 2,000.00 recognized, less 8,200.00 released from 2024 cash: 24,000.00 − 2,000.00 − 8,200.00). All cash expenses (81,550.00) were paid in January; every monthly invoice was also collected in January.

## 6. Checklist confirmation (close checklist items 1–7)
1 ✓ invoices/receipts posted, A/R agreed (restated); 2 ✓ annual billing deferred, monthly release; 3 ✓ bills posted, prepaids reviewed but unsupported (open item 4.3); 4 ✓ payroll agreed to register **and** bank; 5 ✓ bank reconciled, nil difference, every line matched; 6 ✓ depreciation 1,777.78; 7 ✓ TB, roll-forward, this note.

## 7. Client response log (received before the February close)

The client was asked Q1–Q7 (`deliverable/QUESTIONS.md`) and has confirmed it has **no additional information** for any of them. These unknowns are therefore permanently unresolvable from the record; per the working rules they are carried as **explicitly flagged assumptions**, not re-asked. Disposition:

| Q | Subject | Client response | Accounting treatment (status) |
|---|---|---|---|
| Q1 | Were Dec-2024/FY2024 statements issued; were 2024 books closed? | No information | Restatement JE-2025-001 charged through **4000** (opening revenue), not 3900 retained earnings — **assumption, permanent**. If 2024 statements are later found to include the error, the charge moves to opening retained earnings; 2025 YTD revenue is unaffected either way. |
| Q2 | A/R aging at 31-Dec-2024 | No information | A/R offset of 54,450.00 for the error (residual method) and the composition/collectability of the remaining **38,200.00** both remain **assumptions, flagged**. No allowance recorded — no evidence supports one either way. |
| Q3 | A/P composition, 17,420.00 | No information | Carried at opening value; no January payment activity observed; aging unknown — **flagged**. |
| Q4 | Prepaid 9,600.00 support | No information | **No amortization recorded** in January (recording one would invent a pattern) — **flagged**. The 800.00/month figure in item 4.3 remains arithmetic illustration only. |
| Q5 | Taxes other than payroll | No information | None recorded; absence of documentation noted — **flagged**. |
| Q6 | 2024 comparative detail | No information | 2024 comparatives cannot be independently verified; restated 2024 opening balances per the client's opening note (41,000.00 deferred) are used as given — **flagged**. |
| Q7 | Stray `documents/bank_statement.csv` (Dec-2025) | No information | Held unused; will be reconciled in the December (month_12) close. |

No January figures change as a result of this response — the client supplied no new facts, only confirmation that none exist. The restated January package stands.
