# Open items — January 2025 close · to the Board

Prepared by the controller, February 2025; revised same month after the client's response to `QUESTIONS.md`
("**no additional information** is available for questions 1–7"). Package: journal entries, trial balance,
deferred-revenue roll-forward, bank reconciliation, this note (close checklist item 7; policy memo item 5).

**Corrections of prior months: none, and none possible.** This is the first close in the engagement, and no
prior deliverable or prior-period statement issued by us exists, so there is nothing to restate. Per
`library/asc250_excerpts.md` (ASC 250-10-45-23, -50-7), an error correction requires *restatement* of the
affected prior period with disclosure of the nature of the error and the effect on each line item. Without the
client records requested in Q1–Q2 (composition of the deferred-revenue opening; whether account 4000's opening
credit is unclosed prior-year revenue), we cannot establish the first period to restate or the amount of the
offsetting opening retained-earnings adjustment, so no correction has been made — including prospectively,
which the excerpt expressly prohibits for errors. Items 1 and 2 are therefore **recorded as-is, disclosed, and
carried open to December 2025**, where the year-end statements are the first period we issue and the correction,
if any, must be disclosed there. If the client later supplies the detail, items 1 and 2 convert from open items
to a disclosed restatement of the opening position; the amounts are stated below so that conversion is a
one-entry exercise.

**Nothing was estimated or forced.** Where a required input does not exist, no entry was booked and the
unknown is flagged.

## A. Unresolved items — carried to the next close

1. **Deferred revenue: 24,000.00 of the opening balance is unsupported.** Account 2200 opened at 65,000.00;
   `documents/note_opening_deferred.md` supports 41,000.00 only (Trestle prior contract, 98,400 × 5/12 remaining
   = 41,000.00, releasing 8,200.00/month Jan–May 2025). The **24,000.00** remainder has no contract, invoice, or
   payment in the client file and equals the Trestle renewal invoice (INV-2225) to the dollar, which is exactly
   the shape of a renewal already sitting in deferred revenue before 1/1/2025 — in which case my JE-2025-01-02
   double-counts it.
   *Treatment:* invoice recorded (it is documented), the two supported releases recorded, the 24,000.00 left in
   2200 **unreleased** and shown as its own line in the roll-forward. Recorded closing 2200 = 65,000.00 +
   24,000.00 − 10,200.00 = **78,800.00**; supported-only alternative = 41,000.00 + 24,000.00 − 10,200.00 =
   **54,800.00**. Maximum overstatement of liabilities: **24,000.00**. Maximum overstatement of FY2025 revenue if
   the whole balance is eventually released: 24,000.00 (2,000.00/month from January 2025).
   *Risk if left open:* February–May 2025 releases are also affected — the prior Trestle contract's 8,200.00/month
   release ends after May 2025 and its remaining balance (32,800.00 at 1/31) needs the composition confirmed
   before June. 2. **Revenue account 4000 opened with a 30,450.00 credit.** An opening (post-closing) trial balance should carry no
   revenue. 30,450.00 is precisely one month of the 24-customer run-rate, consistent with December 2024 revenue
   never closed to retained earnings.
   *Treatment:* carried as-is. Account 4000 ends January at **71,100.00 cumulative**, of which **January 2025
   activity is 40,650.00** = 30,450.00 monthly invoices + 10,200.00 deferred releases. `trial_balance.json`
   discloses both figures so no later reader mistakes 71,100.00 for 2025 revenue.
   *Contingent entry, ready to post on confirmation:* Dr 4000 30,450.00 / Cr 3900 30,450.00 → deficit
   205,953.00 → **175,503.00**; effect on 2025 income statement: revenue 71,100.00 → 40,650.00. Not posted,
   because confirming it requires the fact the client does not have.
3. **A/R 92,650.00 has no customer detail or aging.** All 25 January receipts applied to January invoices, so
   account 1100 ends January at exactly **92,650.00** — the opening receivable is untouched and unexamined.
   No allowance for credit losses has been recorded: establishing one requires customer-level information
   (aging, disputes, collection history) that the client has confirmed does not exist, and an estimate invented
   here would not be a supportable measurement. The full 92,650.00 is therefore presented at gross with this
   disclosure — a stated limitation on the balance, not an assertion that it is collectible.
4. **Prepaid expenses 1300: 9,600.00, composition unknown, no amortization booked.** Close-checklist item 3
   requires prepaids to be reviewed; there is no schedule to review. No January amortization was recorded —
   the amount cannot be derived from anything in the file, and a guess would misstate both 1300 and expense.
   Sensitivity, for the Board's information only, **not** a booking: if the whole balance were, say, a 12-month
   prepayment started 12/01/2024, the January charge would be 800.00 (9,600.00 ÷ 12); a 6-month term would give
   1,600.00. Undischarged prepaid expense is the open exposure.
5. **A/P 2000: 17,420.00 opening balance, vendor detail unknown, nothing paid in January.** Roll-forward:
   17,420.00 + 22,070.00 − 22,070.00 = **17,420.00**. All five January ACH debits tie to *January* bills, so no
   bank item can be attributed to the opening balance. Presented as valid liabilities (the conservative
   treatment). If any part was in fact settled in a prior period, liabilities and retained earnings are
   misstated by that amount; it is not measurable on the present file.

## B. Assumptions, now locked (client has confirmed no further records exist)

6. **Depreciation 1,777.78/month is a stated directive, not a derived figure.** Close-checklist item 6 dictates
   the amount; there is no fixed-asset register. The arithmetic is self-consistent — 64,000.00 ÷ 36 = 1,777.78,
   and opening accumulated depreciation 21,333.00 ≈ 12 × 1,777.78 (rounded), i.e. roughly 12 months of a 36-month
   life from ~January 2024. Accumulated depreciation after January: 21,333.00 + 1,777.78 = **23,110.78**; implied
   fully depreciated October 2026. We apply the checklist amount as an explicit assumption and will not extend it
   to additions that were never documented.
7. **Expense accounts opened.** The opening chart of accounts contained no expense accounts. Added 5000 Hosting
   & infrastructure, 5100 Payroll — salaries & wages, 5110 Payroll — employer taxes & benefits, 5200 Rent &
   occupancy, 5300 Software & tools, 5400 Marketing, 5500 Depreciation expense, 5900 G&A other. Bills were posted
   using the `category_hint` column of `vendor_bills.csv`.
8. **January 2025 operating result: revenue 40,650.00, expenses 83,327.78, net loss 42,677.78** (expenses =
   9,920 hosting + 54,404 salaries + 5,076 employer taxes + 7,200 rent + 1,460 software + 3,250 marketing +
   1,777.78 depreciation + 240 Gusto platform fee). This excludes the disputed 30,450.00 opening credit in 4000
   (item 2). Cash sanity check: 412,000.00 → 384,900.00, a 27,100.00 fall, explained by deferred-revenue and
   depreciation movements against the loss.

## C. Facts recorded as received, requiring no further input

9. **Revenue treatment.** Monthly invoices recognized in January, service delivered in the period
   (606-10-25-14(b), 25-27 series over time). Trestle 24,000.00 billed upfront booked wholly to deferred with
   1/12 released (606-10-45-2; policy memo #1) — the invoice wording "billed upfront" did not drive the
   treatment, as the contract requires. The renewal order form is treated as a new 12-month contract from
   2025-01-01 on its own terms; the alternative reading as a modification of the expiring contract (606-10-25-10
   et seq.) yields the identical 2,000.00 January release, so the judgment has no numerical effect. Policy memo
   #2 (implementation), #3 (cancellations) and #4 (unidentified receipts) were not triggered: no separately
   priced implementation was delivered, no contract was cancelled, and all 25 receipts matched an invoice
   (nothing posted to 2300).
10. **Bank and payroll.** Bank reconciles to a **0.00** difference with all 32 January items matched
    line-for-line. Payroll agrees to register **and** bank: withheld 54,404.00 − 48,200.00 = 6,204.00;
    6,204.00 + employer 5,076.00 = 11,280.00 remitted; total cash out 48,200.00 + 11,280.00 = 59,480.00 = total
    expense 54,404.00 + 5,076.00. The 240.00 Gusto platform fee is a vendor bill, not a payroll tax, so it sits
    in 5900 rather than 5110.
11. **Stray file `documents/bank_statement.csv`.** Contains only transactions dated **December 2025** on a
    negative balance — future-dated relative to this period and not January activity for account ending 5531.
    Not used. Recorded as an unresolved provenance question: if it is a forecast or a second account, it has
    never been reconciled and we cannot rule out a further bank account.

## D. Library coverage gaps — stated explicitly, unverified

The library contains **no** excerpt on expected credit losses (ASC 326), income taxes (ASC 740), lease accounting
(ASC 842), or share-based compensation. We did **not** rely on any belief about those areas, and we do not cite
them; we note the gap because each would matter here if facts developed:

- **Credit losses (item 3):** the A/R limitation in item 3 is a documentation limitation, not a conclusion that
  ASC 326 is satisfied. The library does not address it, so we make no claim about it. **Unverified and not relied on.**
- **Income taxes:** no tax accounts, tax expense, or deferred tax balances exist in the chart of accounts or in
  the documents. January reflects tax payments only as payroll remittances. We make no income-tax assertion in
  either direction. **Unverified and not relied on.**
- **Leases:** WeWork rent of 7,200.00/month is expensed as paid. Whether any lease requires balance-sheet
  recognition cannot be assessed from the library, which is silent. **Unverified and not relied on.**

**Citations used, all listed in `library/INDEX.md`:** `asc606_excerpts.md` (FASB ASC 606-10-25, -32, -55),
`asc250_excerpts.md` (FASB ASC 250-10-45-23, -50-7), `revenue_policy_memo.md` (Internal policy),
`close_checklist.md` (Internal). No authority outside the library is relied on or cited; where we believe a
requirement may exist outside the library, item D labels it unverified rather than citing it.
