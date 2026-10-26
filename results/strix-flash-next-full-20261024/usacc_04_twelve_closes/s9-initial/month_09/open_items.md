# Open Items — September 2025 Close

**To:** Board of Directors, Northwind Analytics Inc.
**From:** Controller
**Period:** September 2025 (month 9 of 12)

No prior-period error was identified in September, so **no ASC 250 correcting
entry was booked this month**. July's correction (JE-2507-PC01, $15,000.00,
Pinecone C-025) remains disclosed in `month_07/open_items.md`; the January
correction remains disclosed in `month_01/open_items.md`. One billing error
did occur in September — an invoice issued in error to a cancelled customer —
but the error and its reversal both fall **inside the open September period**
(item 1), so ASC 250 is not engaged. The other new event is a paid-in-advance
contract, C-030 Vireo Clinics PBC (item 2).

## 1. Erroneous invoice to a cancelled customer — C-012 Alder Studios LLC, INV-2409 $1,800.00, voided by same-period credit memo CM-2509-01

- **The facts:** C-012 cancelled under MSA §6.2 effective **2025-08-31**
  (`documents/month_08/email_cancellation_C-012.txt`, 08/11: "stop invoicing
  after the August invoice" — analyzed at `month_08/open_items.md` item 1).
  Despite that, the billing run generated **INV-2409 ($1,800.00) dated
  09/01** (`documents/month_09/invoices.csv`). The customer objected in
  `documents/month_09/email_dispute_C-012.txt` (09/06): *"We received another
  invoice. We cancelled effective 8/31 (see our notice). We will not be
  paying this. Please issue a credit and stop."*
- **The accounting:** as of 09/01 there is no contract with C-012 (ASC
  606-10-25-1 criteria not met), no performance obligation, and no service
  delivered — so **no revenue exists to recognize**, and the revenue policy
  memo (¶1, subscriptions recognized as services are delivered) points the
  same way. The invoice was picked up by the standard billing entry
  (JE-2509-001, Dr 1100 / Cr 4000, 09/01) and **reversed in the same month**
  by credit memo **CM-2509-01** (JE-2509-002, Dr 4000 / Cr 1100 $1,800.00,
  dated 09/06). C-012 **never paid** — no 09/xx receipt in
  `cash_receipts.csv` and no corresponding bank credit (verified against the
  statement) — so no cash refund is required and both 1100 and 4000 carry
  **zero net effect** from this event. September monthly billing is therefore
  23 subscribers / $28,650.00 (gross invoicing $30,450.00 − credit memo
  $1,800.00).
- **Why this is NOT an ASC 250 prior-period correction:** ASC 250-10-45-23
  et seq. addresses errors in **previously issued** financial statements.
  Both the error (issued 09/01) and the correction (09/06) occurred inside
  the open September period, and August's books were correct (INV-2385 was
  earned in full and collected 08/22). No restatement, no opening-balance
  adjustment — a same-period journal correction is sufficient.
- **Control observation for the Board:** the billing system did **not** honor
  the cancellation stop. Please have operations confirm C-012 is suppressed
  in the billing system and that **no October invoice** is generated. If any
  payment from C-012 ever arrives, it is a refundable deposit, not revenue.
- **No client question was raised:** the documents answer themselves —
  cancellation + no September service + explicit refusal to pay ⇒ the credit
  memo is the only document-supported treatment.

## 2. New paid-in-advance contract — C-030 Vireo Clinics PBC, $27,000.00 annual (INV-2422)

- `documents/month_09/order_form_C-030.md` (signed electronically 2025-09-01):
  annual subscription **$27,000.00, billed upfront**, payment due on
  signature, service start **2025-09-01**, term **12 months, auto-renewing**,
  MSA v3.2. Billed 09/01 (INV-2422) and **collected by wire $27,000.00 on
  09/15** (register + bank 1:1).
- **ASC 606 analysis:** an enforceable contract exists (606-10-25-1). The
  single performance obligation is continuous platform access — a series of
  substantially identical daily services satisfied **over time**
  (606-10-25-14(b), 25-27); the time-based output measure applies. Release =
  $27,000.00 ÷ 12 = **$2,250.00/month** (September 2025 – August 2026).
- **Booked:** JE-2509-001 (Dr 1100 / Cr 2200 $27,000.00 at billing),
  JE-2509-003 (cash collection), JE-2509-015 (release $2,250.00). Deferred
  balance after September: **$24,750.00**. Same self-contained pattern as
  Quarry (C-028) and Saltline (C-029) — no client input needed; the
  auto-renewal date (~Aug 2026) is flagged for watching, not action.

## 3. Harbor Law LLP — quarterly cadence confirmed (billed and paid this month)

`vendor_bills.csv` carries **$2,500.00 dated 09/09** and the bank shows the
matching ACH debit 09/09 — the **third** occurrence on a clean quarterly
cadence: 03/09 → 06/09 → 09/09. August's open item 2 (expect September) is
therefore **resolved**. Account 6600 Professional fees reaches **$7,500.00**
year-to-date; the next bill is expected **December 2025**. The vendor is a
law firm, distinct from our customer **Harbor Logistics LLC** (C-017).

## 4. Payroll register — ninth consecutive identical month (standing unknown U11)

September register is identical to January–August: gross $54,404.00, net
$48,200.00, employer taxes $5,076.00, remit $11,280.00, 9 employees, pay date
09/25. Books match the register and both Gusto ACH debits match the books
(three-way tie, see `bank_reconciliation.md`). Account 2210 clears
cumulatively: 9 × $11,280.00 = **$101,520.00** debits = credits, balance
$0.00. Carried as U11 per protocol — not re-asked.

## 5. Trestle (C-026), Pinecone (C-025), Marigold (C-027), Quarry (C-028), Saltline (C-029), Vireo (C-030) — routine releases

Scheduled September releases: $2,000.00 + $3,000.00 + $1,500.00 + $2,500.00
+ $1,800.00 + $2,250.00 = **$13,050.00** (JE-2509-015). Rollforward:
opening $68,200.00 + new billing $27,000.00 − releases $13,050.00 =
closing **$82,150.00** = account 2200 net ✔ (full detail in
`deferred_revenue_rollforward.json`).

## 6. Opening accounts receivable — ninth month with no collections (standing unknown U3)

No September receipt applied to the opening $92,650.00: all 23 monthly ACHs
applied to September invoices, and the Vireo wire applied to INV-2422.
**After the CM-2509-01 reversal, the 1100 balance is now 100% legacy** —
current-period receivables are fully collected. Carried at face value; no
allowance booked (nothing documents impairment). Not re-asked.

## 7. Opening accounts payable — ninth month with no payments (standing unknown U9)

No bank payment touched the opening $17,420.00 (account 2000): the only
vendor ACHs were the six September bills ($25,930.00). Usage drift continues:
AWS **$10,880.00** (seventh straight +$120.00 step) and Google Ads
**$3,650.00**. Carried as U9 — not re-asked.

## 8. Prepaid expense and depreciation assumptions (U4, U5)

Account 1300 Prepaid expenses remains $9,600.00 with no supporting schedule
(no amortization booked — U4). Depreciation continues at $1,777.78/month
(straight-line, 36-month life per close checklist — U5); accumulated
depreciation 1510 is now **$37,333.02**.

## 9. Deferred revenue classification (account 2200 = $82,150.00)

| Contract | 9/30 balance | Remaining service months | Classification |
|---|---:|---|---|
| Trestle renewal (C-026) | $6,000.00 | Oct–Dec 2025 @ 2,000 | Current |
| Pinecone Dental Group (C-025) | $12,000.00 | Oct 2025–Jan 2026 @ 3,000 | Current |
| Marigold Schools (C-027) | $7,500.00 | Oct 2025–Feb 2026 @ 1,500 | Current |
| Quarry Analytics Co (C-028) | $17,500.00 | Oct 2025–Apr 2026 @ 2,500 | Current |
| Saltline Hospitality (C-029) | $14,400.00 | Oct 2025–May 2026 @ 1,800 | Current |
| Vireo Clinics PBC (C-030) | $24,750.00 | Oct 2025–Aug 2026 @ 2,250 | Current |
| **Total** | **$82,150.00** | | |

Every balance is classifiable as **current**: all remaining service months
fall within 12 months of 2025-09-30 (Vireo's tail ends exactly Aug 2026).
The U6 chart-of-accounts gap (no non-current contract-liability account)
remains **moot**.

## 10. Standing unknowns carried forward (not re-asked)

U1 (subscription start dates behind opening A/R), U2 (equity/AP composition
detail), U3 (opening A/R collectibility — 9th month), U4 (prepaid schedule),
U5 (depreciation life/method), U6 (non-current deferred revenue account —
moot, see item 9), U7 (withholding derivation), U8 (root `bank_statement.csv`
Dec-2025 negative balances — still unused, held for month_12), U9 (opening
A/P aging — 9th month), U11 (payroll register identical — 9th month).
**U10 and U12 remain closed.**
**No new unknowns arose in September and no new questions were raised** — the
C-012 dispute email and the C-030 order form each answer themselves
(items 1–2).

## Result of the September 2025 close

- Revenue $41,700.00 = $28,650.00 monthly subscriptions (23 customers;
  gross billing $30,450.00 **less** $1,800.00 credit memo CM-2509-01) +
  $13,050.00 scheduled deferred releases. **No prior-period correction this
  month** (the one September error was corrected within the same period).
- Expenses $87,187.78 (gross salaries $54,404.00 + employer taxes
  $5,076.00 + vendor bills $25,930.00 + depreciation $1,777.78).
- **Net loss $(45,487.78)**.
- Cash $93,280.00 = bank statement ending balance, difference $0.00;
  deferred revenue 2200 net $82,150.00 = rollforward closing balance;
  trial balance in balance (debits = credits = $2,958,693.02).
