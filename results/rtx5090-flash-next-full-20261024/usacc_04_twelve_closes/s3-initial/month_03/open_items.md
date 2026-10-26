# Open items — March 2025
**To:** Board, Northwind Analytics Inc. · **From:** Controller · **Re:** March 2025 close; prior-period disclosure correction; judgment calls; carried flags

---

## 0. CORRECTION TO PRIOR-MONTH DISCLOSURES (February package) — Pinecone release schedule arithmetic

**What was wrong.** The February package repeatedly stated that **"24,000.00 of the Pinecone deferred balance releases in 2026"** and that a year-end split would move that 24,000.00 to non-current. That figure is **arithmetically wrong** under the assumed 12-month term (2025-02-01 → 2026-01-31) that our own books use. It appeared in:
- `month_02/open_items.md` §1 and the §7 response log;
- `month_02/deferred_revenue_rollforward.json` presentation_note ("Pinecone 24,000.00 (Jan 2026, beyond 12 months)") and contract note;
- `month_02/trial_balance.json` note on account 2200;
- `deliverable/STATUS.md` (February section).

**The correct figures.** The Pinecone balance at 2025-02-28 was 33,000.00 = **11 remaining monthly releases of 3,000.00 each (Mar 2025 through Jan 2026)**. Of that: 30,000.00 releases Mar–Dec 2025 and **only 3,000.00 (Jan 2026) falls in calendar 2026** — not 24,000.00. (The 24,000.00 figure appears to have been transposed from the *Trestle renewal contract amount*, which happens to be 24,000.00.) The February note also claimed releases through "Jan–Aug 2026" — that implies a 19-month run-off, contradicting the 12-month assumption in our own memos.

**Knock-on correction.** Because the last Pinecone release (Jan 2026) is within 12 months of 2025-02-28, **every component of deferred revenue was in fact within 12 months of the February reporting date** — the February claim that January's "all within 12 months" statement "no longer holds" was itself wrong. January's statement stood all along.

**What is NOT affected.** No journal entry, no trial balance, and no roll-forward *balance* ever used 24,000.00: monthly releases were 3,000.00, the 2200 balance was 77,600.00, and the roll-forward footed. This is a narrative/disclosure error only, so **no ASC 250 restatement of figures is required**; per the engagement rules ("correct openly, note in open_items.md; never quietly fix forward") the correction is made here, prominently, and the corrected classification appears in this month's `deferred_revenue_rollforward.json` presentation_note. The February files were left as originally issued (historical record) rather than silently rewritten.

**Corrected current/non-current view as of 2025-03-31:** 2200 = 80,900.00; latest release date across all contracts is 2026-02-28 (Marigold); therefore **non-current portion = 0.00** under the assumed Pinecone term. That conclusion remains contingent on the Pinecone assumption (still permanently unknown — §1).

## 1. Pinecone Dental Group (C-025) — term still permanently unknown (carried)

Nothing has changed since Q8: the client confirms no further records of the term exist. Books continue to assume a 12-month term from 2025-02-01 (36,000.00 / 12 = 3,000.00/month; March is month 2; balance 30,000.00). **Flag retained, escalated wording:** the 2025 P&L figure (33,000.00 of Pinecone revenue for the year under the assumption) cannot be verified as to *timing* allocation between 2025 and 2026. Any alternative term would shift revenue across periods; if a term is ever documented, we will correct per ASC 250-10-45-23.

## 2. NEW: Marigold Schools Inc (C-027) — annual upfront billing, cleanly documented

INV-2275, 18,000.00, billed 2025-03-01 ("Annual Subscription — 12 months, billed upfront"), collected by wire 2025-03-15. **Unlike Pinecone, the term is explicitly stated on the order form** ("Term: 12 months from service start, auto-renewing"; service start 2025-03-01), so no assumption and no question are needed:
- Billed to contract liability on 2025-03-01 (JE-2025-024; ASC 606-10-45-2 — billed before performance; Board revenue policy item 1: annual billings deferred, released straight-line).
- Recognized **1,500.00** for March (18,000.00 / 12; term 2025-03-01 → 2026-02-28); balance 16,500.00. 2025 release total will be 15,000.00; 3,000.00 falls in Jan–Feb 2026 (still within 12 months of 2025 year-end, so no non-current issue at year-end).
- "Auto-renewing": no renewal order has been received; nothing beyond the current 12-month term is recorded. If renewal occurs we will treat it as a new contract on the documented start date.
- Performance-obligation analysis: single subscription PO identical to Trestle's; released time-based. No implementation component on this order form.

## 3. Judgment call: NEW account 5600 "Professional fees" (Harbor Law LLP, 2,500.00)

First professional-fee spend of the engagement. The opening chart of accounts (documents/opening_trial_balance.csv) contains only 1000–4000-series accounts; every 5xxx expense account in these books is controller-created (5000, 5010, 5100, 5200, 5300, 5400, 5700, 5900). I opened **5600 Professional fees** rather than burying legal fees in 5900 "G&A/other" — legal/audit fees are recurring for any company heading toward year-end and deserve their own line. Expensed in full in March: the bill description ("Professional fees") gives no indication of future-period benefit, so no prepaid/deferred treatment (checklist item 3 review; nothing else in March's bills is prepay-like). If the Board prefers a different account number or naming, reclass is trivial and I will apply it with disclosure.

## 4. Minor correction: February JE-2025-012 memo composition breakdown

JE-2025-012's memo describes the 24 February invoices as "3x650 + 5x2,400 + 4x1,800 + 3x900 + 6x450". That breakdown lists only 21 invoices and sums to 26,550.00 — the **memo composition was miswritten** (the invoice *total* 30,450.00, invoice count 24, and the journal amounts were correct). The actual February composition (identical to January's and March's) is **3x650 + 5x2,400 + 5x1,800 + 4x900 + 6x450 + 1x1,200 = 30,450.00 (24 invoices)**. Verified against February invoices/bank rec credit lines. Memo-level error only: no ledger amount was ever wrong, so no restatement; disclosed here and March's memo (JE-2025-023) uses the correct breakdown. February files left as issued for historical integrity.

## 5. Carried open items (client has confirmed: no additional information exists)

1. **A/R 38,200.00 (acct 1100) — now 3+ months outstanding; risk escalated.** All March billings (48,450.00) were collected in March; the 38,200.00 is entirely the opening 2024-vintage balance. No March bank credit matches it, and none has ever been collected (Jan/Feb pattern continues). Recommend the Board obtain a customer-level aging from management and decide on a bad-debt reserve — under ASC 606 the receivable's *collectibility* is the open question; no allowance is currently recorded. I cannot evaluate allowance adequacy without the customer breakdown (Q1 remains unanswered).
2. **A/P 17,420.00 (acct 2000) — unpaid third month.** No March bank debit matches any opening payable. All March vendor bills were paid same-month, so the payment process works; the opening payables are aging without payment. Vendor names/invoices behind this balance remain undocumented.
3. **Prepaid 9,600.00 (acct 1300) — no supporting documents; no amortization recorded.** Continuing flag (Q2): without a nature/period we cannot test whether any amortization belongs in 2025. Left at cost.
4. **Pinecone term** — §1; permanent assumption, permanent flag.
5. **Depreciation policy amount 1,777.78/month** per checklist item 6: 64,000.00 / 36 months is implied but never documented; the fixed amount will not foot to zero in Dec-2027 (0.36 absorb noted in Jan; unchanged). Accumulated depreciation now 26,666.34.
6. **2024 comparatives / opening 3900 deficit 205,953.00** — no 2024 financials provided (Q3); year-end statements will present 2025 only.
7. **Payroll "other taxes"** — register's employer 5,076.00 composition (FICA/unemployment split) still undocumented; expensed in aggregate (Q4 follow-through unchanged).
8. **Stray Dec-2025 bank file** (`documents/bank_statement.csv`) — belongs to month_12; untouched.

**No new questions** were needed for March: every March document ties (Marigold term explicit, receipts↔bank 1:1, bills↔bank 1:1, payroll↔register+bank). `deliverable/QUESTIONS.md` annotated accordingly; Q1–Q8 will not be re-asked.

## 6. March 2025 results, tie-outs and validation

- **JE totals:** 12 entries (JE-2025-023 … 034), debits = credits = 209,047.78.
- **Trial balance:** debits = credits = 904,436.34; reproduced arithmetically from the February TB plus each March JE — every account agrees to the penny (validated mechanically before filing this package).
- **Revenue March 45,150.00** = 30,450.00 monthly + 8,200.00 + 2,000.00 + 3,000.00 + 1,500.00 releases. **YTD 129,450.00.** March expenses 86,167.78 (incl. 2,500.00 professional fees). **March net loss (41,017.78); YTD net loss (123,543.34)** = (82,525.56) + (41,017.78) ✓.
- **Deferred revenue:** 77,600.00 + 18,000.00 − 14,700.00 = 80,900.00 = 2200 ✓ (roll-forward ties per contract).
- **A/R:** 38,200.00 + 48,450.00 − 48,450.00 = 38,200.00 ✓ (only the aged 2024 balance remains).
- **Cash bridge (loss → cash movement):** loss (41,017.78) + depreciation 1,777.78 = (39,240.00) cash-basis loss; collections 48,450.00 exceeded recognized revenue 45,150.00 by +3,300.00 (Marigold +16,500.00 collected-not-recognized; releases without new collection −8,200.00 −2,000.00 −3,000.00); (39,240.00) + 3,300.00 = **(35,940.00)** = 333,690.00 − 369,630.00 ✓ exactly.
- **Bank:** nil difference, 33/33 lines matched (§ above); payroll agreed to register AND bank (checklist item 4).
- **Checklist (library close_checklist.md):** 1 invoices/receipts posted, A/R agreed ✓ · 2 annual billings deferred, monthly releases ✓ · 3 bills posted, prepaid reviewed (§5.3 flag) ✓ · 4 payroll both-sided ✓ · 5 bank reconciled, differences documented (none) ✓ · 6 depreciation 1,777.78 ✓ · 7 TB + roll-forward + this note ✓.
- Prior-period restatement (Dec-2024 billing omission, JE-2025-001) unchanged and still disclosed in month_01; no new ASC 250 events in the books this month — §0 and §4 are disclosure/narrative corrections only.

**Status: COMPLETE WITH OPEN ITEMS** (items above are flags, not unresolved accounting entries; every March document was accounted for and ties).
