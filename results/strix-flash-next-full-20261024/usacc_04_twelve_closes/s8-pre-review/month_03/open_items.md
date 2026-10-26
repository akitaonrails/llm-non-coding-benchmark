# Open Items — March 2025 Close

**To:** Board, Northwind Analytics Inc.
**From:** Controller
**Period:** March 2025 (month 3 of 12)

No prior-period errors were identified in March activity, so **no ASC 250
restatement entry was needed this month** (January's JE-2501-PC01 correction
stands as closed and disclosed in `month_01/open_items.md`).

## 1. NEW — Marigold Schools Inc (C-027 / INV-2275): $18,000 billed and collected, recognized $1,500

- Order form C-027 (2025-03-01): one line, "Annual subscription — 12 months,
  billed upfront," $18,000.00; payment due on signature; **service start
  2025-03-01; term: 12 months from service start, auto-renewing**; governed by
  Master Subscription Agreement v3.2 (still not in the documents provided).
- Treatment: billed to 2200 deferred revenue (JE-2503-002); released
  $18,000.00 ÷ 12 = **$1,500.00 for March** (JE-2503-015), leaving $16,500.00
  covering Apr-2025 through Feb-2026. Why:
  - Board revenue policy #1 (`library/revenue_policy_memo.md`): annual
    upfront-billed subscriptions go to deferred revenue and release 1/12 per
    month.
  - The advance is a contract liability until the service transfers
    (ASC 606-10-45-2); the 03/15 wire collects the advance — collection does
    not create revenue.
  - The subscription is a single performance obligation satisfied over time
    (ASC 606-10-25-14(b), 25-27).
- **Contrast with Pinecone (C-025, U10):** here the term **is stated on the
  order form itself**, so the release is computable from the documents with no
  invented facts. Pinecone's order form states no term, and its release stays
  at $0.00.
- The MSA v3.2 was already requested (February question F4, no client
  information available) and is **not re-asked**: unlike Pinecone, the March
  treatment does not depend on facts that exist only inside the MSA. The
  auto-renewal clause does not extend the current recognition period —
  revenue is recognized for the stated 12-month term; a renewal, if it occurs,
  is a separate arrangement.

## 2. NEW — account 6600 Professional fees opened

- Harbor Law LLP bill $2,500.00 (03/09, `vendor_bills.csv`, paid 03/09) has no
  home in the chart of accounts. Opened **6600 Professional fees** rather than
  burying legal fees in 6200 G&A other (JE-2503-008). This is a judgment call
  on account structure; the amount is not in dispute.

## 3. Pinecone Dental Group — unchanged (standing unknown U10)

- No new Pinecone documents in March. $36,000.00 remains fully deferred in
  2200, recognized $0.00 for the second month running — an over-time
  performance obligation with no determinable term has no computable release;
  guessing one would invent facts. Not re-asked per client protocol.

## 4. Payroll — third consecutive identical register (standing unknown U11)

- January = February = March: gross $54,404.00, net $48,200.00, employer
  $5,076.00, remitted $11,280.00, 9 employees. March ties to the bank
  (net-pay and tax ACHs) like the prior months, so the books are supportable
  for March; the pattern is flagged as fact and remains unresolved. Not
  re-asked per client protocol.

## 5. Opening A/R — third month uncollected (standing unknown U3)

- $92,650.00 of opening (pre-2025) receivables: **zero** collections applied
  in March. All 25 March receipts applied to March invoices.

## 6. Opening A/P — third month unpaid (standing unknown U9)

- $17,420.00 of opening payables: **no** payments in March. All March vendor
  payments were March bills.

## 7. Prepaid expense and depreciation assumptions (U4, U5)

- 1300 Prepaid expense $9,600.00: no amortization schedule provided; nothing
  amortized in March (U4).
- Depreciation $1,777.78 = $64,000.00 ÷ 36 months straight-line per close
  checklist item 6 (U5 assumption carried); 1510 accumulated $26,666.34.

## 8. Deferred revenue classification (account 2200 = $86,900.00)

| Contract | 03/31 balance | Service months remaining | Classification |
|---|---:|---|---|
| Trestle prior contract (C-026, corrected) | $16,400.00 | Apr–May 2025 @ 8,200 | Current |
| Trestle renewal (C-026) | $18,000.00 | May–Dec 2025 @ 2,000 | Current |
| Marigold C-027 | $16,500.00 | Apr 2025–Feb 2026 @ 1,500 | Current (within 12 months of 03/31) |
| Pinecone C-025 | $36,000.00 | Unknown term (U10) | **Not classifiable** (also U6: no non-current contract-liability account exists) |

## 9. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates for opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility), U4 (prepaid schedule), U5
(depreciation life/method), U6 (non-current deferred-revenue account), U7
(withholding derivation), U8 (root `bank_statement.csv` Dec-2025 negative
balances), U9 (opening A/P aging), U10 (Pinecone term), U11 (identical
payroll registers). March adds **no new unknowns** — Marigold is fully
documented on its order form.

## Result of the March close

- Revenue $42,150.00 (30,450.00 monthly + 11,700.00 releases); expenses
  $86,167.78; **net loss $(44,017.78)**.
- Cash $333,690.00 = bank; deferred revenue 2200 net $86,900.00 = rollforward
  closing; trial balance in balance (debits = credits = $1,535,056.34).
