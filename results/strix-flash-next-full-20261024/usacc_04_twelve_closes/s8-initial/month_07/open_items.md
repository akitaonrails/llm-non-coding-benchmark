# Open Items — July 2025 Close

**To:** Board of Directors, Northwind Analytics Inc.
**From:** Controller
**Period:** July 2025 (month 7 of 12)

A prior-period error was identified from a July document and corrected this
month by an ASC 250 discrete entry, **JE-2507-PC01** (Dr 2200 / Cr 4000,
$15,000.00), on the Pinecone Dental Group contract (C-025). Full disclosure
at item 1 below. The January correcting entry (JE-2501-PC01) remains closed
and disclosed in `month_01/open_items.md`.

## 1. ASC 250 prior-period correction — Pinecone Dental Group (C-025), $15,000.00

- **What changed:** Amendment No. 1 to the C-025 order form
  (`documents/month_07/order_form_amendment_C-025.md`, effective 2025-07-02,
  signed M. Ferris, COO, for Pinecone and J. Alvarado for Northwind) states
  the 2025-02-01 order form contained a **clerical error**: the $36,000.00
  line "Implementation & License — one-time fee" is replaced with an
  "**annual platform subscription, 12-month term beginning 2025-02-01,
  billed upfront**," and "no implementation services have been or will be
  provided — onboarding was self-serve." That matches the client's own
  February answer (F2: "nothing custom — they self-onboarded like
  everyone else").
- **Nature of the error (ASC 250-10-45-23):** because the term was never
  documented (standing unknown U10), the Feb–Jun books held the entire
  $36,000.00 in contract liability (account 2200) and recognized nothing.
  With the term now documented, the performance obligation is a series of
  daily subscription services satisfied over time (ASC 606-10-25-14(b),
  25-27; revenue policy memo ¶1): $36,000.00 ÷ 12 = $3,000.00 was earned
  each month from February. At 6/30 revenue (4000) was understated and
  deferred revenue (2200) overstated by 5 × $3,000.00 = **$15,000.00**.
- **Correction booked in July:** JE-2507-PC01, dated 2025-07-02 (amendment
  effective date), Dr 2200 $15,000.00 / Cr 4000 $15,000.00, kept as a
  discrete, labeled entry rather than buried in July's routine releases
  (JE-2507-013 carries only July's own $3,000.00). No cash effect — the
  $36,000.00 was collected in February.
- **Disclosure (ASC 250-10-50-7):** the error was a misclassification of the
  contract's service period caused by the order-form clerical error; the
  correction amount is $15,000.00. The February–June Board statements
  understated revenue by $3,000.00 per month and overstated deferred
  revenue by $15,000.00 cumulatively. Prior closed books are not reopened;
  the correction is shown as the discrete, dated July entry above.
- **Alternative characterization considered:** treating July as when the
  service period became estimable — a change in estimate recognized as a
  cumulative catch-up in the period of change — produces the **identical
  July numbers** ($15,000.00 catch-up + $3,000.00 July month = $18,000.00
  to 4000). Only the label differs; we disclose both.
- **Answer to J. Alvarado** (his forwarded note asked "nothing changes on
  our side, right?"): **no — it changes revenue timing materially.** By
  7/31 we recognize $18,000.00 cumulative on C-025 ($15,000.00 prior
  periods + $3,000.00 July); the remaining $18,000.00 in 2200 releases
  $3,000.00 monthly August 2025 – January 2026.
- **U10 is closed** by the amendment itself; no client question needed.

## 2. OBSERVATION — no Harbor Law LLP bill in July (quarterly cadence)

- July `vendor_bills.csv` contains no Harbor Law bill and the bank shows no
  Harbor Law ACH. This fits the observed quarterly cadence: $2,500.00 billed
  and paid 03/09, $2,500.00 billed and paid 06/09 — next expected
  September.
- We recorded **no July accrual**: no evidence of services delivered in
  July, and the close checklist requires booking every invoice received —
  none was received. 6600 Professional fees stays at $5,000.00 YTD. If
  September brings no bill, or a bill without an invoice, we will raise it.
- Name caution for the Board: the monthly subscriber **Harbor Logistics
  LLC** (C-017) is a different party from the vendor **Harbor Law LLP**.

## 3. Payroll register — seventh consecutive identical month (standing unknown U11)

- Jan = Feb = Mar = Apr = May = Jun = Jul: gross $54,404.00, net $48,200.00,
  employer $5,076.00, remit $11,280.00, 9 employees. Not re-asked per
  protocol. July is clean at the bank: one net-pay debit; register, books,
  and bank all tie; 2210 clears cumulatively ($78,960.00 each way).

## 4. Marigold (C-027), Quarry (C-028), Saltline (C-029), Trestle renewal (C-026) — routine

- Marigold: $1,500.00 released; $10,500.00 left, covering Aug 2025 – Feb 2026.
- Quarry: $2,500.00 released; $22,500.00 left, covering Aug 2025 – Apr 2026.
- Saltline: $1,800.00 released; $18,000.00 left, covering Aug 2025 – May 2026.
- Trestle renewal: $2,000.00 released; $10,000.00 left, covering Aug – Dec
  2025; renewal billing expected January 2026.
## 5. Opening accounts receivable — seventh month with no collections (standing unknown U3)

- The opening (pre-2025) receivable of $92,650.00 saw **no** collections in
  July: all 24 receipts applied to July invoices. Age now beyond 18 months;
  we continue to carry U3 and to recommend the Board decide on collectibility.

## 6. Opening accounts payable — seventh month with no payments (standing unknown U9)

- The opening payable of $17,420.00 again saw **no** payments; all five
  vendor ACHs settled July invoices within the month.
- Vendor usage drift noted (no adjustment): AWS $10,640.00 vs $10,520.00 in
  June; Google Ads $3,550.00 vs $3,500.00. Both match `vendor_bills.csv`
  one-for-one.

## 7. Prepaid expense and depreciation assumptions (U4, U5)

- 1300 Prepaid expenses $9,600.00: still no amortization schedule from the
  client; nothing amortized (U4).
- Depreciation stays $1,777.78 = $64,000.00 ÷ 36-month straight line per
  close checklist ¶6 (U5); 1510 Accumulated depreciation reaches
  $33,777.46.

## 8. Deferred revenue classification (account 2200 = $79,000.00)

| Contract | 7/31 balance | Remaining service months | Classification |
|---|---:|---|---|
| Trestle renewal (C-026) | $10,000.00 | Aug–Dec 2025 @ 2,000 | Current |
| Pinecone Dental Group (C-025) | $18,000.00 | Aug 2025–Jan 2026 @ 3,000 (term now documented) | Current |
| Marigold Schools (C-027) | $10,500.00 | Aug 2025–Feb 2026 @ 1,500 | Current |
| Quarry Analytics Co (C-028) | $22,500.00 | Aug 2025–Apr 2026 @ 2,500 | Current |
| Saltline Hospitality (C-029) | $18,000.00 | Aug 2025–May 2026 @ 1,800 | Current |
| **Total** | **$79,000.00** | | |

For the first time since February, **every** balance is classifiable as
current: all remaining service months fall within 12 months of 2025-07-31.
The U6 chart-of-accounts gap (no non-current contract-liability account) is
**moot as of July**, but stays on the books in case a future multi-year
contract arises.

## 9. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates behind opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility — 7th month), U4 (prepaid
schedule), U5 (depreciation life/method), U6 (non-current deferred revenue
account — **moot as of July**, see item 8), U7 (withholding derivation),
U8 (root `bank_statement.csv` Dec-2025 negative balances — still unused,
held for month_12), U9 (opening A/P aging — 7th month), U11 (payroll
register identical — 7th month).
**U10 (Pinecone term) closed this month** by Amendment No. 1 — closure by
document, not by client answer. U12 (Gusto recoveries) remains closed.
**No new unknowns arose in July and no new questions were raised.**

## Result of the July 2025 close

- Revenue $56,250.00 = $30,450.00 monthly subscriptions + $10,800.00
  scheduled deferred releases + $15,000.00 prior-period correction
  (JE-2507-PC01, disclosed separately per item 1; July operations
  excluding the correction = $41,250.00).
- Expenses $84,347.78 (gross salaries $54,404.00 + employer taxes
  $5,076.00 + vendor bills $23,090.00 + depreciation $1,777.78).
- **Net loss $(28,097.78)** — $(43,097.78) excluding the prior-period
  correction.
- Cash $175,330.00 = bank statement ending balance, difference $0.00;
  deferred revenue 2200 net $79,000.00 = rollforward closing balance;
  trial balance in balance (debits = credits = $2,515,587.46).
