# Open items — April 2025
**To:** Board, Northwind Analytics Inc. · **From:** Controller · **Re:** April 2025 close; NEW material item — disputed duplicate net-pay debit of 48,200.00; correction to prior-month disclosures (February/March Trestle release prose); judgment calls; carried flags

---

## 1. NEW — Duplicate GUSTO NET PAY debit of 48,200.00: recorded as a claim, recoverability NOT confirmed

**The facts.** The April bank statement shows **two** identical ACH debits "GUSTO NET PAY" of 48,200.00 — one dated 04/25 and one dated 04/26. The payroll register shows **exactly one** April payroll run, with net pay of 48,200.00 (see bank_reconciliation.md: the 04/25 debit agrees to the register; gross 54,404.00 / net 48,200.00 / taxes 11,280.00 ↔ the separate GUSTO TAX debit). The office manager's note (received 2025-04-27) states: *"Gusto support ticket #GS-44812 opened 4/27: 'two net-pay debits hit our account, only one payroll was run'. No resolution yet."* So the client itself asserts only one payroll was run.

**Evidence the second debit is an error, not a second payroll.**
- Register: one run, one net-pay figure. A second payroll of the identical amount would require a second register, which does not exist in the records provided.
- Pre-debit tie-out: book cash supported by all other April activity is **282,080.00** = 333,690.00 + 30,450.00 − 22,580.00 − 48,200.00 − 11,280.00, exactly the statement's own running balance on the line immediately before the disputed debit. The two records agree on every cent up to that line and differ on that line only.
- No vendor bill, tax notice or other document explains a 48,200.00 outflow besides payroll.

**Treatment recorded (JE-2025-041): Dr 1200 "Other receivables — disputed bank debits" 48,200.00 / Cr 1000 48,200.00.** Rationale:
- The cash genuinely left the bank, so ledger cash must reflect it (GL 1000 = 233,880.00 = bank exactly).
- It is **not an expense**: no goods, services or payroll obligation was incurred; the company holds a claim against Gusto/the bank. Expensing it would overstate the April loss by 48,200.00 and pre-judge the dispute.
- **This classification is controller judgment, not library-supported.** I checked the entire citable library (library/INDEX.md and its four files); it contains **no guidance on cash-claim / disputed-debit treatment** — so the label "unverified" applies to the classification itself. Creating account 1200 follows the same practice as 5600 (March, §3 there): the opening chart of accounts (documents/opening_trial_balance.csv) has no fit, and every account outside the opening list is flagged as controller-created.

**Alternatives considered and rejected.**
1. *Leave (48,200.00) as an unreconciled difference on the bank rec.* Contract-legal (differences must be documented, nothing forced), but rejected: the difference would persist indefinitely with GL cash contradicting bank cash, and we already have documentation (note + ticket) supporting a claim — better to record the claim and flag it than to park a negative plug.
2. *Expense it immediately.* Rejected for the rationale above; would be correct **only** if the claim is denied (see follow-up below).

**Flag, loud and clear:** recoverability is **not confirmed**. Gusto ticket #GS-44812 is open with no resolution; no bank acknowledgment of error exists yet. Account 1200's 48,200.00 is carried at full amount because no evidence supports a different measure — that is an assumption, not a valuation.

**Required action — time-sensitive.** The bank statement boilerplate states: *"If no error is reported within 60 days the account will be considered correct."* The April statement is dated 2025-04-30, so the window closes on or about **2025-06-25**. The Gusto ticket alone may not satisfy the bank's notice requirement. **Recommend the Board (a) send Pacific Summit Bank written notice of the disputed 04/26 debit before ~2025-06-25, referencing the statement date and GS-44812; (b) chase GS-44812 to written resolution; (c) obtain employee-level confirmation that no employee received two net-pay deposits in April** — if any employee *was* double-paid, the claim converts into an employee-recovery matter, not a bank claim, and the accounting changes.

**Follow-up accounting.** Reversal received → Cr 1200, Dr 1000, disclosed. Claim denied (by Gusto or the bank, including via lapse of the 60-day clause) → write off 48,200.00 to expense in the month of denial with prominent disclosure. Either event lands in the May close or later; carried as an open item until resolved.

## 2. CORRECTION TO PRIOR-MONTH DISCLOSURES (February and March packages) — Trestle prior-contract remaining-release prose

**What was wrong.** Three narrative statements about the Trestle Freight LLC (C-026) **prior** subscription's remaining releases were wrong. The release schedule is 8,200.00/month for **five** months, Jan–May 2025 (client opening note: 41,000.00 over 5 remaining months). That makes: Jan 1st, Feb 2nd, **Mar 3rd**, Apr 4th, May 5th (final).

- `month_02/deferred_revenue_rollforward.json` contract note: *"Remaining releases: March and May 2025"* — **omits April**. Correct at 2025-02-28: **March, April and May 2025** (3 × 8,200.00 = 24,600.00, which is exactly that roll-forward's closing balance).
- `month_02/open_items.md` contract summary: *"releases left: March and May 2025"* — same omission.
- `month_02/deferred_revenue_rollforward.json` presentation_note: releases after 2025-02-28 listed as *"prior 16,400.00 (Mar, May) + renewal 18,000.00 (Mar-Dec) + …"*. Both figures are wrong: prior remaining = **24,600.00 (Mar, Apr, May)** (16,400.00 is the *March-end* balance), and renewal remaining = **20,000.00 (Mar–Dec 2025)** (18,000.00 is the March-end renewal balance). The misstated components also don't foot: 16,400 + 18,000 + 30,000 + 24,000 = 88,400 vs the actual 2200 balance 77,600. (The "Pinecone 24,000.00 (Jan 2026)" element of that same note was already corrected in March §0.)
- `month_03/deferred_revenue_rollforward.json` contract note and `month_03/journal_entries.json` JE-2025-031 memo: *"March is 4th of 5 releases; one release remains (May 2025)"* — March was the **3rd** of 5, and **two** releases remained (April and May).

**What is NOT affected.** Every journal amount, roll-forward balance and tie-out was always correct: Feb closing 24,600.00 = 3 × 8,200.00 (ties to 2200 = 77,600.00); Mar closing 16,400.00 = 2 × 8,200.00 (ties to 2200 = 80,900.00); the March presentation_note schedule itself ("Trestle prior 16,400.00 (Apr, May 2025)") was right. This is a **narrative/ordinal error only — no ASC 250 restatement of figures** and no change to any prior trial balance.

**How corrected.** Per the engagement rules (correct openly, never quietly fix forward): the error is disclosed here; the April package carries the corrected prose in the JE-2025-043 memo and the deferred_revenue_rollforward.json note/presentation_note; February and March files are left as originally issued (historical record).

## 3. Judgment calls and observations this month

- **New account 1200 "Other receivables — disputed bank debits"** (controller-created, second after 5600): full analysis in §1, including the negative library check. Numbering/naming is trivial to reclass if the Board prefers otherwise; I would keep the separation from 1100 because 1100 is customer trade A/R with its own collectibility problem (§5.1).
- **Vendor-spend variance observed, no action:** AWS 10,280.00 (April) and Google Ads 3,400.00 (April) differ from prior months — usage-based bills; each ties 1:1 to its bill and its ACH debit; no prepaid/deferred element identified (checklist item 3 review).
- **April invoices/receipts clean:** 24 invoices INV-2276…2299 totaling 30,450.00; 24 receipts 04/20–04/26 matching 24 bank credits 1:1 by name, amount and date; all five vendor bills paid in-month.

## 4. Client communications log (April) — and action items for the client

- **2025-04-27, note from office manager** (documents/month_04/note_from_office_manager.txt), verbatim: *"Gusto support ticket #GS-44812 opened 4/27: 'two net-pay debits hit our account, only one payroll was run'. No resolution yet."* — logged as client communication supporting §1; not a formal question to the client.
- **Client action items (not questions — the client has no more information to give until the bank/Gusto act):** (a) written notice to Pacific Summit Bank re the 04/26 disputed debit before ~2025-06-25 (60-day clause); (b) resolution of GS-44812 in writing; (c) employee-level confirmation of no double payment. See §1.
- **No new formal questions** were required for April: every April document ties except the disputed debit, which is documented by the client's own note and ticket. Q1–Q8 remain unanswered by design (client confirmed no additional information exists) and will not be re-asked. `deliverable/QUESTIONS.md` annotated accordingly.

## 5. Carried open items (client has confirmed: no additional information exists)

1. **A/R 38,200.00 (acct 1100) — FOURTH month outstanding; zero collections.** All April billings (30,450.00) were collected in-month; the 38,200.00 is entirely the 2024-vintage opening balance and no April bank credit matches it (all 24 credits tie to 2025 invoices). Customer-level aging still unavailable (Q1); no allowance recorded; collectibility judgment remains the Board's.
2. **A/P 17,420.00 (acct 2000) — unpaid for the FOURTH month.** No April bank debit matches any opening payable (all nine debits identified in bank_reconciliation.md). Current vendor bills are paid same-month, so the process works; the opening payables just age. Supporting vendor invoices remain undocumented (Q3/Q5 family).
3. **Prepaid 9,600.00 (acct 1300) — no supporting documents; no amortization recorded.** Continuing flag (Q2); left at cost.
4. **Pinecone Dental Group term — permanently unknown (Q8).** Books assume 12 months from 2025-02-01 (April = month 3; balance 27,000.00). Timing allocation across 2025/2026 unverifiable; flag permanent.
5. **Depreciation policy 1,777.78/month** (checklist item 6): implied 64,000.00 / 36 months, never documented; will not foot to zero in Dec-2027 (0.36 absorption already noted). Accumulated depreciation now **28,444.12** = opening 21,333.00 (2024, per opening TB) + 4 x 1,777.78 booked Jan–Apr 2025.
6. **2024 comparatives / opening 3900 deficit 205,953.00** — no 2024 financials provided (Q3); year-end statements will present 2025 only.
7. **Payroll tax composition** — employer 5,076.00/month and withheld 6,204.00/month are expensed/paid in aggregate; FICA/unemployment split undocumented (Q4 family).
8. **NEW carried item: recoverability of the 48,200.00 duplicate-debit claim (acct 1200)** — §1; tracked to GS-44812 / bank written notice; resolution expected May or later.
9. **Stray Dec-2025 bank file** (`documents/bank_statement.csv`) — belongs to month_12; untouched.

## 6. April 2025 results, tie-outs and validation

- **JE totals:** 12 entries (JE-2025-035 … 046), debits = credits = **218,917.78** (includes the 48,200.00 disputed-debit entry JE-2025-041).
- **Trial balance:** debits = credits = **936,664.12**; reproduced arithmetically from the March TB plus each April JE — every account agrees to the penny (validated mechanically before filing this package).
- **Revenue April 45,150.00** = 30,450.00 monthly + 8,200.00 + 2,000.00 + 3,000.00 + 1,500.00 releases. **YTD 174,600.00.** April expenses **83,837.78**. **April net loss (38,687.78); YTD net loss (162,231.12)** = (123,543.34) + (38,687.78) ✓.
- **Deferred revenue:** 80,900.00 + 0.00 billed − 14,700.00 released = **66,200.00** = 2200 ✓ (roll-forward ties per contract; Trestle prior balance now 8,200.00 — one final release in May).
- **A/R:** 38,200.00 + 30,450.00 − 30,450.00 = 38,200.00 ✓ (only the aged 2024 balance remains).
- **Cash bridge (loss → cash movement):** loss (38,687.78) + non-cash depreciation 1,777.78 = (36,910.00); − 14,700.00 revenue released without April cash = (51,610.00); − 48,200.00 disputed outflow (non-P&L) = **(99,810.00)** = 233,880.00 − 333,690.00 ✓ exactly. Cross-check: cash operating outflows 22,580.00 vendors + 48,200.00 net pay + 11,280.00 taxes = 82,060.00 = April expenses 83,837.78 − depreciation 1,777.78 ✓; collections 30,450.00 equal April monthly billings exactly.
- **Bank:** nil difference with 32/32 statement transactions matched (8 debit lines + 24 credit lines; March had 33 = 8 + 25 because of the Marigold 3/15 wire) — **subject to the §1 caveat** (nil only because the disputed debit was recorded; not a plug). Payroll agreed to register AND bank for the single run (checklist item 4).
- **Checklist (library close_checklist.md):** 1 ✓ invoices/receipts posted, A/R agreed (aged balance flagged §5.1); 2 ✓ annual/upfront billings deferred, monthly releases booked; 3 ✓ bills posted, prepaid reviewed (still unsupported, §5.3); 4 ✓ payroll both-sided (second debit is an error item, §1, not a matching failure); 5 ✓ bank reconciled, difference documented (nil, with caveat); 6 ✓ depreciation 1,777.78; 7 ✓ TB, roll-forward, this note.
- **May carry-forward:** Trestle prior FINAL release 8,200.00 (contract closes); Trestle renewal 2,000.00; Pinecone 3,000.00; Marigold 1,500.00; depreciation 1,777.78; plus any GS-44812/bank resolution (reversal Cr 1200, or write-off with disclosure per §1).
- Prior-period restatement (Dec-2024 billing omission, JE-2025-001) unchanged and still disclosed in month_01. **No new ASC 250 events in the books this month** — §2 is a narrative/disclosure correction only.

**Status: COMPLETE WITH OPEN ITEMS** (the disputed 48,200.00 is recorded, documented and flagged — not an unresolved entry; every April document was accounted for and ties).
