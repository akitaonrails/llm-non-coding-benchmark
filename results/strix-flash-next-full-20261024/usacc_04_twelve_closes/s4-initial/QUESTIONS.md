# Questions to the Client

## April 2025 close — question record (session 4) — CLOSED as asked

**Client reply received (office manager):** on G1 — *"Gusto admitted the
double debit; refund posted May 9."* For everything else the client has **no
additional information**; all previously asked matters (Jan 1–9, Feb F1–F5)
remain carried as standing unknowns U1–U11 per client protocol and are not
re-asked.

| # | Question | Client reply | Effect / treatment now in force |
|---|---|---|---|
| G1 | **Duplicate Gusto net-pay debit — recovery status.** The April bank statement shows two GUSTO NET PAY ACH debits of $48,200.00 (04/25 and 04/26) but only one April payroll was run (`payroll_register.json`; office manager's note, Gusto ticket **GS-44812** opened 4/27). Has Gusto or the bank returned the duplicate $48,200.00, or committed to returning it — and by which path (Gusto credit/refund vs bank ACH recall/dispute)? Please also keep ticket GS-44812 open and retain all correspondence: the statement's clause ("If no error is reported within 60 days the account will be considered correct") runs to approximately **2025-06-25**. | **Answered:** "Gusto admitted the double debit; refund posted May 9." | Claim was valid at 04/30, so **April books stand unchanged** (Dr 1200 / Cr 1000, JE-2504-012) — the refund is a May event, not an April restatement. Recovery entry scheduled at the **month_05 close: Dr 1000 Cash $48,200.00 / Cr 1200 Due from Gusto, dated 2025-05-09**, conditional on the credit appearing on the May bank statement (we verify against the statement; client assertion alone does not book cash). U12 → **resolved by reply; cash confirmation pending month_05**. No write-off needed. The 60-day dispute clock (to ~2025-06-25) was satisfied: GS-44812 opened 4/27 and Gusto admitted the error. |

## March 2025 close — question record (session 4, recorded retroactively with the March files) — NO new questions

The March close raised **no new questions**. Every March item was either
fully documented or already covered by an existing question or standing
unknown, so per client protocol nothing was re-asked:

- **Marigold Schools (C-027 / INV-2275, $18,000):** no question needed — the
  order form itself states the term ("12 months from service start,
  service start 2025-03-01"), so the policy #1 release of $1,500.00/month is
  computable from the documents without client input. (The Master
  Subscription Agreement v3.2 referenced on the form was already requested as
  February question **F4** — not re-asked; unlike Pinecone, the March
  treatment does not depend on facts inside the MSA.)
- **Harbor Law LLP $2,500.00:** amount undisputed; booking to new account
  6600 Professional fees is a judgment call disclosed in
  `month_03/open_items.md`, not a question for the client.
- **Pinecone / payroll identity / opening A/R & A/P / prepaid /
  depreciation:** unchanged; carried as U10, U11, U3, U9, U4, U5.

## February 2025 close — question record (session 2) — CLOSED as asked

**Client reply received (J. Alvarado).** On the Pinecone deployment/pricing
questions: *"Honestly nothing bespoke — they self-onboarded like everyone
else. Procurement just wanted it called a license."* For the remaining
questions (F1, F4, F5) the client has **no additional information**. Per the
client's protocol these are NOT re-asked in later sessions; F1/F4 are carried
as standing unknown **U10** and F5 as **U11** in `month_02/open_items.md`.

| # | Question | Client reply | Effect / treatment now in force |
|---|---|---|---|
| F1 | **Pinecone Dental Group (C-025 / INV-2250, $36,000): what is the contract term?** The order form states a 2025-02-01 service start but no term, so no ratable release can be computed. | **No additional information** | Carried as unknown **U10**. $36,000 stays in 2200 deferred revenue, **$0.00 recognized** — an over-time performance obligation with no determinable term has no computable release; guessing one would invent facts. |
| F2 | **Has the "platform deployment and user onboarding" actually been performed, and if so when?** Please provide delivery evidence. Board policy #2 recognizes implementation only when a distinct service is *actually delivered*. | **Answered:** "nothing bespoke — they self-onboarded like everyone else." | No distinct implementation service was ever delivered. Policy #2 is explicit that self-serve onboarding is **not** an implementation service → implementation recognition path closed by documented fact. |
| F3 | **Is implementation a distinct, separately priced service, or is the $36,000 one blended charge for access + set-up?** The order form shows a single line "Implementation & license — one-time" with no allocation. | **Answered (in substance):** the "license" wording was procurement's preference; nothing bespoke. | The label is cosmetic — ASC 606 substance governs (606-10-25-10 et seq.: a description correction does not change the accounting). The single performance obligation is continuous platform access, a series satisfied **over time** (606-10-25-14(b), 25-27). No allocation exists because no distinct implementation exists. Recognition still $0.00 pending the term (U10). |
| F4 | **Please provide the Northwind Master Subscription Agreement v3.2** referenced on order form C-025 — it may contain the term, renewal, and scope terms driving F1–F3. | **Not provided** (no additional information) | Carried as unknown **U10** with F1. Treatment as above. |
| F5 | **February's Gusto payroll register is numerically identical to January's in every field.** Is that correct, or is it a duplicated export? | **No additional information** | Carried as unknown **U11**. February payroll booked as registered ($59,480 total cost); three-way tie register ↔ books ↔ bank holds; nothing forced. |

## January 2025 close — question record (session 1) — CLOSED as asked

**Client reply received: no additional information was provided for any
question.** Per the client's instruction these are NOT re-asked in later
sessions; each is instead carried as an explicitly flagged unknown (U1–U9) in
every month's `open_items.md` with the assumption we operate under. Answers,
if ever provided, will be applied as corrections at that time.

| # | Question (asked month_01) | Client reply | Consequence / assumption in force |
|---|---|---|---|
| 1 | Did any other paid-in-advance contract exist at 12/31/2024 behind opening deferred revenue of $65,000? | **None** | ASC 250 correction JE-2501-PC01 (−$24,000 to 2200, +$24,000 opening retained earnings) STANDS — it is the only document-supported reading (`note_opening_deferred.md`, order form C-026 dated 2025-01-01). If evidence ever appears, reverse via ASC 250. |
| 2 | Were FY2024 books closed? Opening 4000 carries $30,450 credit; 3900 a $205,953 debit. | **None** | Opening balances carried as given; no FY2024 re-closing performed. Flagged as an unresolved opening-balance anomaly; 2025 activity is separately identifiable in the journal entries. |
| 3 | A/R aging / collectibility behind opening $92,650. | **None** | Carried at face value; no allowance booked (nothing documents impairment). UNKNOWN flagged. |
| 4 | Prepaid expenses $9,600 — nature and amortization schedule. | **None** | No amortization booked. Flagged: expenses may be understated; amount sits unchanged in 1300 until documented. |
| 5 | Equipment: 36-month life? Is $64,000 the complete asset population? | **None** | 36-month straight-line per close checklist retained ($1,777.78/mo); asset population assumed complete. Flagged assumption. |
| 6 | Deferred revenue current vs non-current presentation ($22,000 covers Feb–Dec 2025). | **None** | Entire 2200 left "current" (chart has no non-current account). Presentation flagged. |
| 7 | Per-employee payroll register / tax-component split. | **None** | Withholding $6,204 remains derived (gross − net); ties to bank remittance $11,280 exactly. Component split unknown. |
| 8 | What is `documents/bank_statement.csv` (Dec-2025 dates, negative balances)? | **None** | Excluded from January; identity unknown. Retained for the December 2025 close where its dates fall. |
| 9 | December 2024 bank statement and AP listing behind opening AP $17,420. | **None** | Opening cash/AP remain client-asserted, not independently verified. The January statement's beginning balance does agree with $412,000. |
