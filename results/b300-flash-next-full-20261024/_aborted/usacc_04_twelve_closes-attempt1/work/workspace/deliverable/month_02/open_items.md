# Open items — February 2025 close · to the Board

Prepared by the controller, February 2025; revised same month after the client's response to
`QUESTIONS.md` (Q9 answered — no bespoke implementation; Q8 unanswerable — access term not obtainable).
Package: journal entries, trial balance, deferred-revenue roll-forward, bank reconciliation, this note
(close checklist item 7; policy memo item 5). Prior-month detail is in `month_01/open_items.md`; only
February movement is stated below — items 1–5 are carried, not closed.

**Corrections of prior months: none.** January's treatments were re-tested against February facts and
hold: the same 24-customer run-rate invoiced and was collected, the Trestle releases repeated exactly
(8,200.00 + 2,000.00), payroll is identical to the month before, and the bank reconciled again to
**0.00**. No error in previously issued statements has been identified, so ASC 250 is not engaged this
month. New item 6 (Pinecone) is a current-month judgment on a contract whose terms are incomplete in
the file — recorded conservatively and disclosed, not an error.

**Nothing was estimated or forced.** The one amount that could have been recognized by guessing
(Pinecone, item 6) was left unreleased rather than given a assumed term — and the client's subsequent
response (item 6) confirmed that choice: no distinct implementation exists and no term is obtainable,
so the zero-release treatment is correct, not merely conservative.

## A. Unresolved items — carried to the next close

1. **Deferred revenue: 24,000.00 of the opening balance remains unsupported** (month_01 item 1).
   February movement only: supported contracts released 10,200.00 (JE-2025-02-07); the unsupported line
   was **not** released. Roll-forward closes 2200 at **104,600.00** = Trestle prior 24,600.00 + Trestle
   renewal 20,000.00 + unsupported 24,000.00 + Pinecone 36,000.00 (item 6). The prior Trestle balance of
   24,600.00 equals exactly 3 × 8,200.00 (Mar–May 2025), which is internally consistent with the note,
   but the composition question must still be resolved **before the June close**, when that contract's
   releases end. Maximum liability overstatement remains **24,000.00**; maximum FY2025 revenue
   overstatement if it is later released as renewal: 22,000.00 remaining from February.
2. **Account 4000 still carries the 30,450.00 opening credit** (month_01 item 2). February revenue
   activity is **40,650.00** (30,450.00 monthly invoices + 10,200.00 releases; Pinecone 36,000.00 is *not*
   in 4000). The cumulative 4000 credit is now **111,750.00**, of which 81,300.00 is 2025 activity —
   `trial_balance.json` discloses the split. The contingent opening reclass (Dr 4000 30,450.00 /
   Cr 3900 30,450.00, deficit 205,953.00 → 175,503.00) remains pre-written and **unposted**; the client
   has confirmed it cannot answer. Carried to December per ASC 250, where the year-end statements are
   the first period we issue and any correction must be disclosed.
3. **A/R 92,650.00: a second month with no application and no detail** (month_01 item 3). All 25
   February receipts (66,450.00) were applied to *February* invoices per `cash_receipts.csv`; none
   touched the opening receivable, which remains presented gross with the same stated limitation — a
   documentation limitation, not an assertion of collectibility, and no ASC 326 conclusion is claimed
   (section D). Aging risk increases with each untouched month; the Board should press for the
   customer-level list even though the client said none exists.
4. **Prepaid 1300: 9,600.00, still no schedule, still no amortization** (month_01 item 4). Close-
   checklist item 3 again could not be performed; the amount cannot be derived from anything in the
   file. Sensitivity on record (not booked): 800.00/month on a 12-month term, 1,600.00/month on 6
   months. February expense would change accordingly if a schedule appears.
5. **A/P 2000: 17,420.00 opening balance, still untouched** (month_01 item 5). February roll-forward:
   17,420.00 + 22,240.00 − 22,240.00 = **17,420.00**; all five February ACH debits tie to *February*
   bills line-for-line, so again no bank item can be attributed to the opening balance.
6. **NEW — Pinecone Dental Group (C-025), INV-2250, 36,000.00: billed, collected, and 100% deferred
   with zero February revenue.** Facts: order form and invoice 2025-02-01, "Implementation & license —
   one-time", due upon signature, service start 2025-02-01, scope "platform deployment and user
   onboarding for up to 40 seats", governed by a Master Subscription Agreement v3.2 **that is not in the
   file**; wire 36,000.00 collected 2025-02-15 (reconciled; collection ≠ recognition).
   *Judgment:* recorded entirely to 2200 (JE-2025-02-02). The amount was billed in advance of any
   evidenced performance (ASC 606-10-45-2); the described scope is set-up activity, which does not
   transfer a service to the customer and is not a performance obligation (ASC 606-10-25-17); and
   revenue policy #2 permits implementation revenue only for a **separately priced, distinct** service
   actually delivered — nothing in the file evidences delivery, and the invoice is a single unallocated
   line, so no separately priced implementation exists on the record. The invoice's "one-time" wording
   does not drive the treatment. The consideration therefore attaches to platform access, but **the
   access term is nowhere stated**, so no ratable release can be computed without inventing a fact.
   *Effect:* February revenue is 40,650.00 excluding the 36,000.00; liabilities include it. If a
   12-month access term starting 2025-02-01 is confirmed, the release is 36,000.00 ÷ 12 = 3,000.00/month
   and February's revenue would have been 43,650.00 — stated as sensitivity only, **not** booked.
   *Client response (received, before the March close):* Q9 answered — *"Honestly nothing bespoke — they
   self-onboarded like everyone else. Procurement just wanted it called a license."* That **closes** the
   implementation element: there was no distinct, separately priced delivery; the entire 36,000.00
   attaches to platform access and February's treatment is **confirmed as correctly recorded** — not an
   error and not a change of estimate, so ASC 250 is not engaged and no issued amount changes. Q8 closed
   as unanswerable — MSA v3.2 and the access term are not obtainable, and per instruction will not be
   re-asked. **The remaining unknown is therefore the term alone, flagged explicitly as such:** with no
   term, no release can be computed (any rate would be an invented fact), so zero revenue continues to be
   recognized and this line carries with disclosure to the December close. If term documentation ever
   surfaces, the release and any catch-up run prospectively — the client's response establishes there was
   no file we missed at booking time, so no ASC 250 error branch remains. Direction of exposure: if the
   true pattern is shorter-term or point-in-time, revenue is **understated** (by up to 36,000.00 in
   aggregate); this treatment cannot overstate revenue.
7. **Usage-bill variance, noted not adjusted:** AWS 10,040.00 (January 9,920.00, +120.00) and Google Ads
   3,300.00 (January 3,250.00, +50.00). Each February bill was paid exactly as invoiced, so no cash
   difference and no accrual/prepaid implication arises; we treat the moves as usage variance, which the
   file does not contradict. No client question is warranted at this size; re-check monthly.
8. **Stray file `documents/bank_statement.csv`** (month_01 item 11): still December-2025-dated, still
   never used for any 2025 close; provenance remains unexplained.

## B. February 2025 result and locked assumptions

9. **Result: revenue 40,650.00, expenses 83,497.78, net loss 42,847.78.** Expenses = AWS 10,040.00 +
   salaries 54,404.00 + employer taxes 5,076.00 + rent 7,200.00 + software 1,460.00 + Google Ads
   3,300.00 + Gusto platform fee 240.00 + depreciation 1,777.78. Cash sanity check: 384,900.00 →
   369,630.00, a 15,270.00 fall = −42,847.78 loss + 25,800.00 deferred-revenue increase (36,000.00
   billed − 10,200.00 released) + 1,777.78 non-cash depreciation. Loss widened vs January (42,677.78)
   solely through the 170.00 of higher usage bills.
10. **January assumptions applied unchanged** — depreciation 1,777.78/month per close-checklist item 6
    (accumulated now 23,110.78 + 1,777.78 = **24,888.56**; fully depreciated October 2026); expense
    accounts 5000/5100/5110/5200/5300/5400/5500/5900 per January item 7; no prepaid amortization
    (item 4); no A/R allowance (item 3).

## C. Facts recorded as received, requiring no further input

11. **Revenue mechanics repeated:** 24 monthly invoices (30,450.00) recognized in the period of service;
    Trestle releases 8,200.00 (month 2 of 5) + 2,000.00 (renewal, month 2 of 12) per 606-10-25-14(b)/
    25-27 and policy #1. Policy #3 (cancellations) and #4 (unidentified receipts) not triggered — no
    cancellations, and every one of the 25 receipts matched an invoice, so nothing was posted to 2300.
12. **Payroll** identical to January and triple-agreed (register ↔ bank ↔ books): gross 54,404.00,
    withheld 6,204.00, employer 5,076.00, remitted 11,280.00, net 48,200.00; cash out 59,480.00 = total
    expense. **Bank:** all 32 February items matched, statement running balances recomputed, difference
    0.00 (`bank_reconciliation.md`).

## D. Library coverage gaps — stated explicitly, unverified

Unchanged from month_01 section D: the library contains no excerpt on expected credit losses
(ASC 326 — relevant to item 3), income taxes (ASC 740 — no tax accounts exist; February again reflects
only payroll remittances), or leases (ASC 842 — WeWork 7,200.00/month expensed as paid). None is cited
or relied on; each is flagged **unverified** because the facts would matter if developed.

**Citations used, all listed in `library/INDEX.md`:** `asc606_excerpts.md` (FASB ASC 606-10-25, -32,
-45, -55), `asc250_excerpts.md` (FASB ASC 250-10-45-23, -50-7), `revenue_policy_memo.md` (Internal
policy, #1 and #2 applied), `close_checklist.md` (Internal). No authority outside the library is
relied on or cited.
