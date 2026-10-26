# STATUS — Northwind Analytics Inc. engagement (twelve monthly closes, 2025)

**Months closed: 2 of 12 — January 2025 and February 2025, both `COMPLETE WITH OPEN ITEMS`.** Months 03–12 await the client's monthly documents; the engagement is not blocked.

## February 2025 close — `deliverable/month_02/` complete and verified
- `journal_entries.json` — 13 entries (JE-2025-014…026), each balanced and each agreed to source documents (`invoices.csv`, `cash_receipts.csv`, `vendor_bills.csv`, `payroll_register.json`, order form C-025).
- `trial_balance.json` — cumulative at 2025-02-28; total **$908,658.56 Dr = $908,658.56 Cr**; January's closing balances plus February activity only; nothing forced.
- `deferred_revenue_rollforward.json` — per-contract: opening $78,800.00 + billed $36,000.00 (Pinecone) − recognized $10,200.00 = closing **$104,600.00**, agreeing to account 2200.
- `bank_reconciliation.md` — book cash **$369,630.00 = bank $369,630.00; difference $0.00**; all 25 deposits ($66,450.00) and 7 disbursements ($81,720.00) agreed to detail; payroll tied to register **and** bank ($59,480.00; withheld $6,204.00 + employer $5,076.00 = remitted $11,280.00).
- `open_items.md` — §1 new Pinecone item; §2 the six carried January unknowns; §3 presentation point; §4 judgment calls; §5 client-response standing.

### February economics (period-only; the TB is cumulative by convention)
- Revenue $40,650.00 (24 monthly subscription invoices $30,450.00 + Trestle releases $8,200.00 + $2,000.00). **No Pinecone revenue was recognized** — the $36,000.00 one-time fee is held as a contract liability (see open items below).
- Expenses $83,497.78 → February standalone net **loss $42,847.78**. 2025 YTD activity (Jan+Feb): revenue $81,300.00; expenses $166,825.56; net loss $85,525.56.

## January 2025 close — `deliverable/month_01/` complete
All five deliverables present and consistent; 13 entries (JE-2025-001…013); TB total $840,430.78 Dr = Cr; deferment closure $78,800.00 tied to account 2200; bank reconciled with zero difference; payroll agreed to register and bank. The February statement's beginning balance ($384,900.00) independently re-verified January's closing book cash — nothing earlier changed.

## Open items (engagement-wide)
1. **ANSWERED — Pinecone Dental Group $36,000.00 (INV-2250, order form C-025): the client's answer confirms February's treatment; the fee remains held in deferred revenue.** Client (Alvarado): *"Honestly nothing bespoke — they self-onboarded like everyone else. Procurement just wanted it called a license."* Consequence: no implementation service exists — "self-serve onboarding is not an implementation service" (policy memo §2) — so no part of the fee is implementation revenue at any date; and the "license" label is a procurement naming choice with no stated term, non-substantive under 606-10-25-10 et seq. (a description-only correction does not change the accounting — the transaction stands on its substance; 606-10-45-2 contract liability). Answer recorded in `QUESTIONS.md` #7. **Remaining unknown, explicitly flagged per the client's instruction: the access period the $36,000.00 covers.** Until a document states that period there is no term to release over (policy §1), so no portion can be recognized; watched in later months for a stated period, Pinecone's appearance in monthly invoicing, or a modification adding a term. Non-blocking — the close stands as issued and the balance carries into the March roll-forward unchanged.
2. **The six January unknowns** (client: "no additional information"; not re-asked): $24,000.00 unidentified opening deferred (held unreleased); opening A/R $92,650.00 without aging detail; opening prepaid $9,600.00 without a schedule (not amortized); opening A/P $17,420.00 without vendor detail; depreciation at $1,777.78/month without an asset schedule; and the year-close convention for unclosed 2024 accounts (Controller decision documented in `month_01/open_items.md` §5).
3. `documents/bank_statement.csv` is a December 2025 statement — out of scope for months 01–11; reserved for the December/year-end session.
