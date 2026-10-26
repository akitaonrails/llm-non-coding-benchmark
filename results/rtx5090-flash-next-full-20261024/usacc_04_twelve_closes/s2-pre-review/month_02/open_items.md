# Open items — February 2025 close
**To:** Board, Northwind Analytics Inc. **From:** Controller **Date of close:** 2025-02-28 (package due 2025-03-10 per Board policy 5)

## 1. NEW — Pinecone Dental Group (C-025), $36,000 "Implementation & license — one-time" — prominent assumption
*[Post-close client response received — characterization confirmed, term still unknown; see §7 response log.]*

**Facts in the file:** order form dated 2025-02-01 (also INV-2250); one line item, $36,000.00, described "Implementation & license — one-time"; payment due on signature; **service start 2025-02-01**; scope "platform deployment and user onboarding for up to 40 seats"; governed by Master Subscription Agreement v3.2. **The subscription term is not stated anywhere**, and there is no separate price for implementation, no delivery/acceptance evidence, and no SOW. Cash of 36,000.00 was received 2025-02-15 (wire, matched to bank).

**Accounting conclusion (documented):**
- Not revenue at billing: amounts billed before performance are a contract liability (ASC 606-10-45-2). The library's revenue never follows the invoice label ("one-time").
- Board policy 2 allows implementation revenue **only if** a separately priced, distinct service is actually delivered. Neither condition is evidenced: implementation is not separately priced (one bundled line), and nothing in the file shows delivered implementation services in February. The library further states set-up activities that do not transfer a service to the customer are not a performance obligation (ASC 606-10-25-17); "platform deployment and user onboarding" is exactly that kind of activity absent contrary evidence.
- The remaining promise is continuous platform access (a "license" under the MSA), which the library recognizes **over time / ratably** (ASC 606-10-25-14(b), 25-27; Board policy 1).
- Therefore the full 36,000.00 sits in 2200 (JE-2025-013) and is released ratably (JE-2025-022).

**The assumption (prominent, flagged):** subscription term **assumed 12 months, 2025-02-01 → 2026-01-31**, giving 36,000.00 / 12 = **3,000.00/month** starting February. Basis: the only annual-term precedent in the file is the Trestle renewal (24,000.00 / 12); the order form states a service start but no end. This is an assumption, not a documented fact — new question Q8 in `QUESTIONS.md`; the client has previously said it has no additional information, so it may remain unresolved. Scenarios (arithmetic only, not booked):
 - If the term is 12 months from 2025-02-01 (booked): Feb revenue 3,000.00; 2025 Pinecone revenue 33,000.00; **24,000.00 stays deferred into 2026**.
 - If the term were monthly/month-to-month (no stated end): recognition would be over the expected/demonstrated period — the library gives no term default; outcome would differ materially. Not booked; flagged.
 - If distinct implementation was in fact delivered in February: a portion could be recognized when performed — but that requires evidence (SOW/acceptance) and a separate price, neither of which exists. Not booked; flagged.

**Presentation flag (supersedes one January statement):** January's open-items note said all deferred amounts release within 12 months. That holds only for January's balances. From February, under the assumed term, **24,000.00 of the Pinecone balance releases in 2026** (8 remaining months Jan–Aug 2026 × 3,000.00). The entire balance is still carried in **2200 (current)** — the library prescribes no non-current split and consistency with January was kept — but the Board should note a current/non-current split, if adopted at year-end, would move 24,000.00 to non-current. Disclosed here per the correction rule (no quiet changes).

## 2. Payroll — agrees to register and bank (no force)
Gross 54,404.00 (identical to January, 9 employees) + employer taxes/benefits 5,076.00 = 59,480.00 expense. Cash out 48,200.00 net + 11,280.00 tax = 59,480.00, matching both bank debits exactly. Withholding 6,204.00 + employer 5,076.00 = 11,280.00 remitted; 2100 clears to zero. Nothing forced.

## 3. Deferred revenue (roll-forward detail in `deferred_revenue_rollforward.json`)
- Trestle prior: 8,200.00 released Feb; closing 24,600.00; releases left: **March and May 2025**.
- Trestle renewal: 2,000.00 released Feb; closing 20,000.00; runs through Dec-2025.
- Pinecone: 36,000.00 billed, 3,000.00 released (assumption above); closing 33,000.00.
- 2200: 54,800.00 + 36,000.00 − 13,200.00 = **77,600.00** (ties to TB).

## 4. Items carried from January (all still open — client has no additional information; flagged, not re-asked)
1. **Opening A/R 38,200.00 (restated):** still entirely uncollected at 28-Feb-2025 — no bank credit matched any receipt to it in either month. This 2024-vintage balance is now roughly two months old with no aging detail; collectability risk **increased** and is flagged again. No allowance recorded: the file supports neither collectability nor impairment, and I will not invent an estimate.
2. **Opening A/P 17,420.00:** no bank payment against it in February either; unpaid since before 2025-01-01. Flagged; aging unknown.
3. **Prepaid 9,600.00:** no amortization (no support exists in the file); unchanged.
4. **Depreciation:** 1,777.78/month kept (checklist item 6); cumulative 1510 = 21,333.00 + 3,555.56 = 24,888.56. The 0.36 cumulative rounding quirk still stands; December-2027 entry will absorb it so accumulated depreciation totals exactly 64,000.00. (Immaterial; judgment call.)
5. **Stray `documents/bank_statement.csv` (Dec-2025):** unused; reserved for the month_12 close.
6. **February bills all paid in-month** (traced to ACH), so no new A/P accruals; no other taxes/accruals documented, none recorded.
7. **Restatement (JE-2025-001)** stands as booked; per the client's standing response, Q1/Q2 remain unanswerable — the A/R offset and the through-4000 presentation remain flagged assumptions.

## 5. February result (arithmetic)
- Revenue 43,650.00 = 30,450.00 monthly + 8,200.00 Trestle prior + 2,000.00 Trestle renewal + 3,000.00 Pinecone (assumed term).
- Expenses 83,497.78 = salaries 54,404.00 + employer taxes 5,076.00 + marketing 3,300.00 + rent 7,200.00 + hosting 10,040.00 + software 1,460.00 + depreciation 1,777.78 + G&A 240.00.
- **Net loss February 2025 = (39,847.78)**. YTD: revenue 84,300.00 − expenses 166,825.56 = **(82,525.56)**. Loss run-rate remains a going-concern-adjacent flag for the Board (I offer no conclusion — the library contains no going-concern guidance; flagged as unverified territory).
- Cash bridge: cash fell 15,270.00 (384,900.00 → 369,630.00). Loss (39,847.78) + non-cash depreciation 1,777.78 = cash burn 38,100.00 = debits 81,720.00 − credits 66,450.00 ✓. Collections exceeded February-recognized revenue by 22,800.00 = Pinecone collected 36,000.00 vs 3,000.00 recognized, less 8,200.00 + 2,000.00 recognized from prior-period collections (36,000.00 − 3,000.00 − 8,200.00 − 2,000.00); plus the 1,777.78 non-cash expense: 22,800.00 + 1,777.78 = 24,577.78 = difference between loss and cash change ✓.

## 6. Checklist confirmation (close checklist items 1–7)
1 ✓ invoices/receipts posted; A/R agreed: Feb billings 66,450.00 fully collected, A/R unchanged at restated 38,200.00 (flag §4.1); 2 ✓ annual/upfront billings → deferred, monthly releases booked; 3 ✓ bills posted; prepaids reviewed, still unsupported (open); 4 ✓ payroll agreed to register **and** bank; 5 ✓ bank reconciled, nil difference, every line matched; 6 ✓ depreciation 1,777.78; 7 ✓ TB, roll-forward, this note.

## 7. Client response log (Q8) — received after the February package was issued, before the March close

Verbatim, from Alvarado: *"Honestly nothing bespoke — they self-onboarded like everyone else. Procurement just wanted it called a license."* For the part not answered above (the subscription term), the client has **no additional information**.

| Q8 part | Client says | Effect on the books |
|---|---|---|
| Was a separately-priced, distinct implementation service delivered in February? | **No** — customer self-onboarded "like everyone else"; nothing bespoke. "Implementation" is only an invoice label. | **Confirms booked treatment (JE-2025-013/022):** no implementation performance obligation — self-serve onboarding is not implementation (Board policy 2) and set-up activities that transfer no service are not performance obligations (ASC 606-10-25-17). The §1 alternative scenario "implementation actually delivered" is now **eliminated by client statement**. No JE change. |
| Does "license" mean a license (right-of-use) transfer, i.e., different recognition? | **No** — "Procurement just wanted it called a license." Substance is the same self-service platform access as every other customer, under the MSA. | **Confirms booked treatment:** continuous subscription service recognized ratably (Board policy 1; ASC 606-10-25-14(b), 25-27). Label does not drive accounting; substance does. No JE change. |
| Subscription term (start/end dates)? | **No information** (permanent). | **Unresolved — now a permanently flagged assumption**, joining Q1–Q7. Booked remains: 12-month term 2025-02-01 → 2026-01-31, 3,000.00/month. The answer does **not** confirm 12 months; "just like everyone else" (all other customers are monthly-billed with no documented fixed term in the file) makes a month-to-month term plausible, but no expected term is quantifiable from the documents, so no alternative is bookable. The 24,000.00 release falling in 2026 and the current/non-current presentation flag (§1) stand. Q8 is not re-asked. |

**No February figures change as a result of this response** — the client confirmed (rather than contradicted) the characterization already booked; only the term assumption persists, prominently flagged. February files are re-issued unchanged; this log is the record per the no-quiet-changes rule.
