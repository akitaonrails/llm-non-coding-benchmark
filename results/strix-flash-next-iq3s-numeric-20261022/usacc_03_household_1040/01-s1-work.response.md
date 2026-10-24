pdftotext is available. Let me extract all the PDFs.

Now let me read the library files.

Engagement complete. All deliverables are written under `deliverable/` (= `workspace/deliverable/`), and the JSON passes internal reconciliation checks.

## Bottom line
**Federal refund: $2,322** — AGI **91,350**, taxable income **59,850**, tax **6,708** (Tax Table row 59,850–59,900), CTC −2,200 (Sofia only), excess-APTC repayment +1,900, total tax **6,408** vs. withholding **8,730**.

## Key findings (where the client's expectations were wrong)
1. **The S-corp loss does NOT come straight off income.** Stock basis roll-forward (2021 $10,000 contribution ± income/distributions per 7203 ordering) leaves **$11,500** opening basis. Only 11,500 of the 28,000 loss is allowed; **16,500 is suspended**. Pike's personal guarantee of the bank line creates no debt basis.
2. **Rental loss $21,018 is limited to $19,550** by the §469(i) special-allowance phase-out: MAGI 110,900 (the allowed nonpassive S-corp loss *does* reduce MAGI) → allowance 25,000 − 5,450; **1,468 carries forward**.
3. **Leo is not claimable in 2025** — the custody order gives odd years to the father, and the library says the agreement controls. No CTC for Leo; Elena signs Form 8332.
4. **Form 8962:** coverage was only Jan–Jun (1095-A annual totals = 6× monthly; Elena's box-DD says "Jul–Dec employer coverage"). Household income 91,350 = 292.79% FPL → applicable figure 5.71% → PTC 7,531 vs. APTC 9,900 → excess 2,369, **capped at $1,900** (200–300% FPL MFJ band).
5. **NY part-year:** 181 resident days; but under **convenience of the employer**, both spouses' full-year wages (68,000 / 54,000) stay NY source since both moved remotely by choice. NY tax itself was deliberately **not** computed — the library has no NY rate schedules; the over-withheld NY tax refunds on IT-203.

## Deliverables
- `return.json` — all template fields filled, self-consistent
- `return.md` — every figure with arithmetic + library citations only
- `judgment_calls.md` — 15 decisions with rejected alternatives (biggest risk: below-market rent could disallow the full rental loss)
- `QUESTIONS.md` — 8 targeted questions (Leo's 8332, necessity-of-remote-work facts, residency end date, tenant relationship, prior-year 7203, Jul–Dec coverage)
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS** (assumptions listed; nothing forced to balance; unverified items like QBI/SALT/EITC flagged, not claimed)