# STATUS.md

**COMPLETE WITH OPEN ITEMS**

*Turn 2 — October 25, 2026: client answers processed. **Answered:** Q2 (basis $31,000 confirmed per CPA, ~$89,000 expensed 2023–2025), Q3 as an estimate (TN visa, no green card/application, ~⅓ of the year ≈ 122 days — consistent with the 118-day projection), Q5 partially (married in Mexico, **no prenup**; Priya single). **Not answered** (carried as flagged unknowns, no new questions sent): Q1 (2026 operating history), Q4 (withholding vendor), Q6 (salary study), Q7 (insurance decision). **No structural or numeric change:** the substantial-presence formula gives 161 < 183 on the projection and still 165 < 183 at the client's own ~122-day estimate; break-even is 140 current-year days.*

## What has been delivered

- `recommendation.md` — entity/tax/ownership recommendation (CA LLC, partnership classification, §721 tool contribution, 50% profits interest for Tomás with 3-yr/1-yr-cliff vesting + protective §83(b)), all alternatives rejected with reasons. Updated this turn: TN-visa/122-day confirmation and the 140-day break-even arithmetic; basis confirmation.
- `year1_comparison.json` — three options with arithmetic and stated assumptions: (a) founders' plan as stated — modeled hypothetically because it is **invalid in 2026** (Tomás = nonresident alien shareholder, §1361(b)(1)(C)); (b) recommendation; (c) S-corp structure corrected for reasonable compensation (illustrative $100k salaries, flagged as no library number). Updated this turn: `client_answers_2026_10_25` block; NRA and basis assumptions annotated with the confirmations. Totals unchanged: A $84,808.48 / B $99,482.47 (with disclosed $0.01 rounding note) / C $108,498.40.
- `compliance_calendar.md` — formation, §83(b) 30-day deadline, CA $800/$2,500, estimated taxes, standing obligations; unconfirmed premise (no 2026 activity before formation) now explicitly flagged. Key date: **§83(b) by December 2, 2026 (T + 30 days, hard)**.
- `term_sheet.md` — operating-agreement terms: waterfall, vesting, buy-sell triggers, discounts, payment terms, deadlock (mediation → shotgun), transfers, spousal consents (now reflecting: married in Mexico, no prenup), S-flip contingency (§9.4).
- `QUESTIONS.md` — now an **answer log**: Q2/Q3/Q5 answered as reported above; remaining unknowns listed; no new questions sent (client had nothing further).

## Open items (do not block the recommendation; flagged in place)

1. **2026 operating history unknown** (was Q1, unanswered) — the calendar assumes nothing operated in 2026 before the Nov 2 formation; if business already ran, every date keyed to T moves and the year-1 catch-up changes. Structure unaffected.
2. **Tomás's partner-level US tax mechanics + no withholding vendor** (was Q4) — §1446 withholding, ECI rules, treaty relief, Mexican tax interplay: **not in the library**; his numbers in `year1_comparison.json` are modeled resident-equivalent, flagged in the file. Year-end log check also lives here: estimate ≈ 122 days vs 118 projected; 2026 break-even = 140 days; he stays NR for the modeled year under any figure the client described.
3. **Built-in-gain (§704(c)-type) allocations** of Priya's tool ($89,000) — **not in the library**; term sheet requires allocations preserve it; precise rules unverified. Basis amount itself is now client-confirmed per her CPA (workpapers not seen).
4. **Reasonable-compensation number** — the library gives rule + precedent (*Watson*) but no market figure; no study selected (was Q6). Needed only for the deferred S-corp contingency, not for the partnership plan.
5. **Due-date mechanics** (CA $800/fee dates, 1065/K-1 dates, estimated-payment dates) — **not in the library**; shown as conventional provisional dates.
6. **Mexican community-property characterization + consent logistics** (Q5 partial) — married, no prenup confirmed; regime specifics/marriage date not provided; **not in library**. Written spousal consent before/at grant remains required per `llc_buy_sell_checklist.md` and is re-emphasized.
7. **Key-person insurance decision** (was Q7, unanswered) — quote vs self-funding the 48-month buy-out note; term sheet §7.5 defaults to self-funding.

## One reconciliation note

Option B's total ($99,482.47) recomputed from the rounded founder lines gives $99,482.46 — a $0.01 rounding artifact, disclosed in `year1_comparison.json` rather than forced to balance.
