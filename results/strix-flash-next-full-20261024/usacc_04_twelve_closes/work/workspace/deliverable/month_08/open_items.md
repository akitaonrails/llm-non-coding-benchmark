# Open Items — August 2025 Close

**To:** Board of Directors, Northwind Analytics Inc.
**From:** Controller
**Period:** August 2025 (month 8 of 12)

No prior-period error was identified in August, so **no ASC 250 correcting
entry was booked this month**. July's correction (JE-2507-PC01, $15,000.00,
Pinecone C-025) remains disclosed in `month_07/open_items.md`; the January
correction remains disclosed in `month_01/open_items.md`. The one new August
event is a customer cancellation — analyzed at item 1, with **no August
adjustment required**.

## 1. Customer cancellation — C-012 Alder Studios LLC, effective 2025-08-31 (no August adjustment)

- **The document:** `documents/month_08/email_cancellation_C-012.txt`
  (received 2025-08-11) is Alder Studios LLC's notice under **MSA §6.2
  (non-renewal/cancellation)** that its subscription ends **2025-08-31**,
  with the instruction "stop invoicing after the August invoice."
- **Why no August adjustment is needed:**
  - INV-2385 ($1,800.00) was issued **2025-08-01 — before the notice** — and
    the August service month was delivered in full (cancellation effective
    only at 08/31). Under the revenue policy memo (¶1, subscriptions billed
    monthly as services are delivered) the August fee is fully earned; it was
    **collected 08/22** (bank ACH ALDER STUDIOS LLC $1,800.00, tied 1:1 to
    the receipt register, see `bank_reconciliation.md`).
  - C-012 is a **monthly subscriber with no deferred balance** in account
    2200 (see rollforward — C-012 does not appear), so there is nothing to
    accelerate, reverse, or refund. The email mentions **no termination
    fee**, and we issued no credit memo.
  - **ASC 606 contract-modification/termination view:** the contract ends at
    the end of its current monthly period with **no remaining unsatisfied
    goods or services** — the termination is accounted for prospectively and
    produces **no cumulative catch-up** in August (contrast C-025, where a
    documented remaining term existed and required one).
- **Impact is prospective only:** from September the monthly billing
  run-rate drops from 24 subscribers / $30,450.00 to **23 subscribers /
  $28,650.00**. September readiness check: September `invoices.csv` must
  contain **no** C-012 invoice.
- The email asks operations to confirm receipt of the notice — an
  administrative step, not an accounting matter. **No client question was
  required:** the document is self-contained (see QUESTIONS.md, session 8).

## 2. OBSERVATION — no Harbor Law LLP bill in August (quarterly cadence)

- August `vendor_bills.csv` contains no Harbor Law bill and the bank shows
  no Harbor Law ACH. This fits the observed quarterly cadence: $2,500.00
  billed and paid 03/09, $2,500.00 billed and paid 06/09 — **next expected
  September**.
- We recorded **no August accrual**: no evidence of services delivered in
  August, and the close checklist requires booking every invoice received —
  none was received. 6600 Professional fees stays at $5,000.00 YTD. If
  September brings no bill, or a bill without an invoice, we will raise it.
- Name caution for the Board: the monthly subscriber **Harbor Logistics
  LLC** (C-017, INV-2388) is a different party from the vendor **Harbor Law
  LLP**.

## 3. Payroll register — eighth consecutive identical month (standing unknown U11)

- Jan = Feb = Mar = Apr = May = Jun = Jul = Aug: gross $54,404.00, net
  $48,200.00, employer $5,076.00, remit $11,280.00, 9 employees. Not
  re-asked per protocol. August is clean at the bank: one net-pay debit and
  one tax-remit debit; register, books, and bank all tie; 2210 clears
  cumulatively ($90,240.00 each way = 8 × $11,280.00).

## 4. Trestle (C-026), Pinecone (C-025), Marigold (C-027), Quarry (C-028), Saltline (C-029) — routine releases

- Trestle renewal: $2,000.00 released; $8,000.00 left, covering Sep–Dec
  2025; renewal billing expected January 2026.
- Pinecone: $3,000.00 released; $15,000.00 left, covering Sep 2025 – Jan
  2026 (documented 12-month term ends 2026-01-31 — final release January).
- Marigold: $1,500.00 released; $9,000.00 left, covering Sep 2025 – Feb
  2026.
- Quarry: $2,500.00 released; $20,000.00 left, covering Sep 2025 – Apr 2026.
- Saltline: $1,800.00 released; $16,200.00 left, covering Sep 2025 – May
  2026 (auto-renew).

## 5. Opening accounts receivable — eighth month with no collections (standing unknown U3)

- The opening (pre-2025) receivable of $92,650.00 saw **no** collections in
  August: all 24 receipts applied to August invoices (a same-month
  collection pattern, new this month — timing only, no accounting effect).
  Age now beyond 20 months; we continue to carry U3 and to recommend the
  Board decide on collectibility.

## 6. Opening accounts payable — eighth month with no payments (standing unknown U9)

- The opening payable of $17,420.00 again saw **no** payments; all five
  vendor ACHs settled August invoices within the month.
- Vendor usage drift noted (no adjustment): AWS $10,760.00 vs $10,640.00 in
  July (+$120.00/month, six straight months); Google Ads $3,600.00 vs
  $3,550.00. Both match `vendor_bills.csv` one-for-one.

## 7. Prepaid expense and depreciation assumptions (U4, U5)

- 1300 Prepaid expenses $9,600.00: still no amortization schedule from the
  client; nothing amortized (U4).
- Depreciation stays $1,777.78 = $64,000.00 ÷ 36-month straight line per
  close checklist ¶6 (U5); 1510 Accumulated depreciation reaches
  $35,555.24.

## 8. Deferred revenue classification (account 2200 = $68,200.00)

| Contract | 8/31 balance | Remaining service months | Classification |
|---|---:|---|---|
| Trestle renewal (C-026) | $8,000.00 | Sep–Dec 2025 @ 2,000 | Current |
| Pinecone Dental Group (C-025) | $15,000.00 | Sep 2025–Jan 2026 @ 3,000 | Current |
| Marigold Schools (C-027) | $9,000.00 | Sep 2025–Feb 2026 @ 1,500 | Current |
| Quarry Analytics Co (C-028) | $20,000.00 | Sep 2025–Apr 2026 @ 2,500 | Current |
| Saltline Hospitality (C-029) | $16,200.00 | Sep 2025–May 2026 @ 1,800 | Current |
| **Total** | **$68,200.00** | | |

Every balance remains classifiable as **current**: all remaining service
months fall within 12 months of 2025-08-31. The U6 chart-of-accounts gap
(no non-current contract-liability account) stays **moot**, kept in case a
future multi-year contract arises. Rollforward reconciliation: opening
$79,000.00 − releases $10,800.00 = closing **$68,200.00** = account 2200
net credit ✔.

## 9. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates behind opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility — 8th month), U4 (prepaid
schedule), U5 (depreciation life/method), U6 (non-current deferred revenue
account — moot, see item 8), U7 (withholding derivation), U8 (root
`bank_statement.csv` Dec-2025 negative balances — still unused, held for
month_12), U9 (opening A/P aging — 8th month), U11 (payroll register
identical — 8th month). **U10 and U12 remain closed.**
**No new unknowns arose in August and no new questions were raised** — the
C-012 cancellation email answers itself (item 1).

## Result of the August 2025 close

- Revenue $41,250.00 = $30,450.00 monthly subscriptions + $10,800.00
  scheduled deferred releases. **No prior-period correction this month.**
- Expenses $84,517.78 (gross salaries $54,404.00 + employer taxes
  $5,076.00 + vendor bills $23,260.00 + depreciation $1,777.78).
- **Net loss $(43,267.78)**.
- Cash $123,040.00 = bank statement ending balance, difference $0.00;
  deferred revenue 2200 net $68,200.00 = rollforward closing balance;
  trial balance in balance (debits = credits = $2,706,345.24).
