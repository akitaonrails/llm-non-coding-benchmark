# Open Items — January 2025 Close

**To:** Board, Northwind Analytics Inc.
**From:** Controller
**Period:** January 2025 (month 1 of 12)

## 1. Prior-period correction — opening deferred revenue overstated by $24,000 (CORRECTED, disclosed)

- Opening trial balance (12/31/2024), account 2200: **$65,000.00 credit**.
- The only documented contract liability at 12/31/2024 is the Trestle Freight
  prior annual contract (Jun 2024–May 2025): client note
  (`documents/note_opening_deferred.md`) supports **$41,000.00**
  (= 8,200 × 5 remaining months).
- The $24,000 difference would correspond to the Trestle **renewal**, but the
  renewal order form C-026 is dated **2025-01-01** with service start
  2025-01-01. A contract liability requires an enforceable contract
  (ASC 606-10-25-1; liability recognized when cash received before transfer of
  goods/services, ASC 606-10-45-2 — `library/asc606_excerpts.md`). No renewal
  contract existed at 12/31/2024, so no renewal liability could sit in the
  opening balance.
- Treatment: restated opening balance via **JE-2501-PC01**
  (Dr 2200 24,000 / Cr 3900 retained earnings 24,000), per ASC 250 correction
  of a prior-period error (`library/asc250_excerpts.md`) rather than absorbing
  it silently into 2025. Disclosed here and in the rollforward
  reconciliation.
- **Open:** this is our reading of the documents. If the client says another
  paid-in-advance contract existed at 12/31/2024, the correction reverses and
  the rollforward changes. Question 1 in `QUESTIONS.md`.

## 2. Opening accounts receivable $92,650 — zero January collections against it

All 25 January receipts apply to **January** invoices (INV-2201..INV-2225).
Not one dollar was applied to the opening A/R balance, which remains
$92,650.00. Aging and customer detail were not provided. Collectibility of the
opening balance is unverified; no allowance for doubtful accounts exists in
the chart. Left on the books at face value; aging requested (Question 3).

## 3. Prepaid expenses $9,600 — no amortization booked

Opening balance exists (account 1300) but no schedule, invoice, or terms were
provided. With no document there is nothing to support a monthly amortization
amount, and the contract says not to invent facts, so **no amortization was
booked in January**. This may understate expense; schedule requested
(Question 4). Assumption stated prominently: 1300 balance carried unchanged.

## 4. Depreciation — straight-line 36 months (assumption)

No fixed-asset register. The close checklist (`library/close_checklist.md`,
item 6) directs depreciation on computer equipment; we used equipment cost
$64,000 (opening TB) ÷ 36 months = **$1,777.78/month** (JE-2501-013).
Consistency check: opening accumulated depreciation $21,333 ≈ 12 × $1,777.78 —
consistent with the asset being one year old on a 36-month life. Useful life is
an assumption; confirm (Question 5).

## 5. Deferred revenue classification

Account 2200 is labeled "current." At 1/31/2025 it holds $54,800, of which
$22,000 relates to Feb–Dec 2025 service on the Trestle renewal. No
non-current liability account exists in the chart. Amount not reclassified
pending Board direction (Question 6).

## 6. Payroll detail

Register total ties to bank exactly (see reconciliation) but shows only
aggregate figures — 9 employees, no per-employee detail and no split of
withholding vs employer taxes beyond the single `taxes_remitted` total. With
gross $54,404 and net $48,200, withholding $6,204 is **derived**
(54,404 − 48,200), and it ties: 6,204 + 5,076 = 11,280 = register
`taxes_remitted` = bank GUSTO TAX. Flagged for detail (Question 7).

## 7. Opening trial balance oddities — 2024 appears not closed

Opening TB carries **account 4000 (Subscription revenue) with a $30,450
credit at 12/31/2024**, and retained earnings (3900) at a $205,953 **debit**.
A closed balance sheet should not carry revenue balances; this suggests FY2024
revenue/expense accounts were never closed to retained earnings. (Coincidence
worth noting: the opening 4000 credit equals exactly the January monthly
billing total, $30,450 — possibly a posting artifact.)
The opening TB does foot: debits $784,203 = credits $784,203.
We did **not** re-open or restate FY2024 — that needs client instruction
(Question 2). The cumulative trial balance therefore still shows the opening
4000 balance; 2025 activity is identifiable in the journal entries.

## 8. Stray bank file `documents/bank_statement.csv`

Transactions dated **December 2025** (future) with negative balances — not the
January statement, and not usable for any 2025 month yet. Excluded from this
close; kept for the December close. Confirm what this file is (Question 8).

## 9. Opening cash not independently verified

Opening cash $412,000 (and AP $17,420) come from the client opening TB only;
no December 2024 bank statement or AP listing was provided. The January
statement's beginning balance agrees with $412,000 ✔, which corroborates but
does not prove the opening balance.

## 10. Client response status — remaining unknowns (explicit flags)

The client responded to all month_01 questions with **no additional
information**, and instructed that they not be re-asked. The following
unknowns therefore remain explicitly open and stay flagged in every future
open_items.md until resolved by documents or instruction:

- **U1.** Whether any other contract liability existed at 12/31/2024
  (item 1). Our ASC 250 correction (JE-2501-PC01) stands as the only
  document-supported treatment; it is a judgment call, not a confirmed fact.
- **U2.** Whether FY2024 was ever closed; opening 4000 ($30,450 Cr) and 3900
  ($205,953 Dr) anomalies remain as found (item 7).
- **U3.** Collectibility/aging of opening A/R $92,650; carried at face, no
  allowance — nothing documents impairment (item 2).
- **U4.** Nature and schedule of prepaid $9,600; unamortized — January and
  ongoing expenses may be understated by an unknown monthly amount (item 3).
- **U5.** Depreciation life (36 mo, from checklist) and completeness of the
  $64,000 asset population (item 4).
- **U6.** Current/non-current split of deferred revenue ($22,000 covers
  Feb–Dec 2025); presented all-current (item 5).
- **U7.** Payroll withholding components ($6,204 derived, ties to bank)
  (item 6).
- **U8.** Identity/purpose of `documents/bank_statement.csv` (Dec-2025 dated)
  (item 8).
- **U9.** Independent verification of opening cash $412,000 / AP $17,420
  (no Dec-2024 statement) (item 9).

None of these block the monthly close. None will be silently "fixed"; each
would be handled as an ASC 250 correction with disclosure if evidence later
changes the answer.

## 11. Result of the month

January net loss **$42,677.78** = revenue $40,650.00 (JE-2501-001 30,450 +
JE-2501-014 10,200) − expenses $83,327.78. No profit-first allocation or
accrual of anything not evidenced was made.
