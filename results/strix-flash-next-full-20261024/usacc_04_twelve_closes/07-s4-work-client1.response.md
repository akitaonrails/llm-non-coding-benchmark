No May documents exist yet — month_05 can't be closed until its source files arrive. So the correct actions are: close out G1 in the question log, record the recovery as a scheduled May entry, and update STATUS. The April books stay as booked (the refund is a May event — post-balance-sheet to 4/30).

Updating QUESTIONS.md first:

Now updating STATUS.md — item 1, the question status section, and a post-close reply note:

Verifying both files render correctly and that the April JSONs remain untouched:

One stale line in Key figures — updating it:

G1 is closed and the records are updated. Here's where things stand:

## G1 resolved — duplicate debit recovered

**Accounting treatment:** April books stay exactly as closed. The claim (Dr 1200 / Cr 1000, JE-2504-012) was valid at 04/30, and the **May 9 refund is a post-balance-sheet event** — it's not an April restatement. The recovery entry is scheduled for the May close:

- **Dr 1000 Cash / Cr 1200 Due from Gusto — $48,200.00, dated 2025-05-09**, conditional on the credit actually appearing on the May bank statement (we verify against the statement; a client assertion alone doesn't book cash).
- No write-off of the claim was ever needed, and the 60-day dispute clock (to ~2025-06-25) was comfortably satisfied — GS-44812 opened 4/27 and Gusto admitted the error.
- **U12 → resolved by reply**, to be formally closed at the month_05 close once the refund credit is verified.

## Remaining unknowns — explicit (client has no additional information on any of these; none re-asked)

- **U1–U9** (Jan set): opening A/R start dates, equity/AP composition, opening A/R collectibility (4 months zero collections), prepaid schedule, depreciation life/method, non-current deferred-revenue account, payroll withholding split, Dec-2025 root `bank_statement.csv`, opening A/P aging (4 months unpaid)
- **U10**: Pinecone term / MSA v3.2 — $36,000 still fully deferred, $0 released
- **U11**: identical payroll registers, now 4 months running — **strengthened**, not resolved, by the duplicate debit; the control concern stands even though this cash incident ends well

Updated files: `deliverable/QUESTIONS.md` (April record flipped to CLOSED as asked with the reply and its effect) and `deliverable/STATUS.md` (reply note, explicit unknown-status section, readiness plan). The April JSONs are untouched (checksums verified).

## Engagement continuation — month_05 blocked on documents

`documents/` still contains only month_01–month_04, so the May close can't be performed yet. When May's bank statement, invoices, receipts, payroll register, and vendor bills arrive, the close will additionally include: the $48,200 recovery entry (verified against the statement), the **final Trestle prior-contract release of $8,200** (May is its last service month — that rollforward line then closes), Pinecone at $0 (U10), and Marigold $1,500 + Trestle renewal $2,000 continuing. Please provide the month_05 documents to proceed.