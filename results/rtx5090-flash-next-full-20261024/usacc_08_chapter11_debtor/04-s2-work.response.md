New session 2 documents — that's the data that was previously missing. Let me look:

Now professional fees memo (updated to actual Dkt. 77 mechanics + the Corbin retention trap) and the tracking files:

Now the last stale piece — STATUS.md. Let me read it in full, then update:

Session 2 is now fully rebuilt on the real April record and validated. Summary of where things stand:

## Session 2 — April MOR (`deliverable/session2/`)

**Part 1** — receipts **$1,480,300.00** (980,300 operating + 500,000 DIP draw 4/9; cumulative draws $1,550,000 of $2,500,000, headroom $950,000). Disbursements **$1,010,600.00** confirmed (payroll 398,000 × 2 + vendors 214,600) or **$1,126,800.00** if the H&P interim payment cleared in April — the file records "no objection by 4/29" but not the payment date, so both cases are carried rather than guessed. Ending cash **$2,241,330.00 / $2,125,130.00**, still understated by the permanently unquantified 3/10 swept balance.

**Part 5 — the big correction.** Dkt. 77 is a **procedures order, not a §330(a) award**: statement → 14-day objection → Debtor *may* pay **80% of fees + 100% of expenses**; 20% holdback only on court approval; **no payment for periods before the retention date**. Therefore:
- **H&P** (retained nunc pro tunc to 3/10 — bar doesn't bite): allowed interim **$116,200.00** = 140,000 × 80% + 4,200 expenses in full; holdback **$28,000.00**; paid-in-April unconfirmed.
- **Corbin — retention trap**: retained effective **3/20**, but his $45,000 statement covers **3/10–3/31**. Ten pre-retention days are **unpayable under Dkt. 77** and the file has no allocation → **allowed 0 / paid 0 / holdback 0**, payment on hold until the statement is supplemented. A day-count pro-rata ($20,454.55 barred / $24,545.45 payable / 80% = $19,636.36) is shown as illustration only, explicitly **not booked**.

**Part 2** — LSTC unchanged at **$74,110.00**; Dkt. 83's own words ("the February invoice remains an unsecured pre-petition claim") now document the Mesa treatment. Post-petition payables can't be single-valued without the vendor itemization, but the file supports one hard deduction: only $18,900 of prior vendor payables existed, so **at least $214,600 − $18,900 = $195,700** of April payments went to invoices not on the 3/31 books.

**Part 7 — "NO" pre-petition payments**, with two caveats before signing under penalty of perjury: invoice-level vendor itemization, and confirmation the 4/10 run covered a wholly post-petition period.

## Also updated
- `session2/april_mor_notes.md` — full arithmetic trail, Python cross-checked.
- `session2/professional_fees.md` — rewritten for Dkt. 77 mechanics + the Corbin trap; my earlier "order awarded $140,000" assumption formally marked superseded.
- `QUESTIONS.md` — April/Mesa/order questions closed (Mesa package mooted by **Dkt. 83**, which executed exactly the lawful route in the CFO response); now 6 April follow-ups + 5 emergence questions.
- `STATUS.md` — Session 2 rewritten, open items renumbered to 1–11; all JSON parses and cross-foots verified.

Notable: Dkt. 83 vindicates the March refusals — Mesa shipped under a post-petition trade agreement, February stayed a pre-petition claim, and the $51,400 netting was never executed.

Next: finalize Part 1/5 once the H&P payment date (Q1) and vendor itemization (Q2) come back, then emergence items 7–11.