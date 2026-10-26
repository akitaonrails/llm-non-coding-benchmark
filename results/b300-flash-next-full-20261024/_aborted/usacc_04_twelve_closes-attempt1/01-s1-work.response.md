

One correction before running — bills must flow through AP (record, then pay), not directly to cash, so the AP rollforward stays clean:





All ties pass. Now the markdown deliverables:





January 2025 close is complete. All five deliverables are in `deliverable/month_01/`, with `QUESTIONS.md` and `STATUS.md` at the root of `deliverable/`.

**What was booked (8 entries, all balanced):**
- Monthly subscriptions INV-2201–2224: Dr A/R / Cr 4000 **30,450.00** (recognized — service delivered in January)
- Trestle renewal INV-2225 24,000.00 → deferred, 1/12 = **2,000.00** released (ASC 606-10-45-2; policy #1)
- Trestle prior contract release **8,200.00** per the opening note (41,000 ÷ 5 remaining months)
- Receipts 54,450.00; bills 22,070.00 through AP; payroll Dr 54,404 + 5,076 / Cr cash 59,480; depreciation 1,777.78

**Key ties (computed in Python, nothing forced):**
- Bank: 412,000 − 81,550 + 54,450 = **384,900 = book cash, difference 0.00**; all 32 bank lines matched one-for-one (including name-collision customers like Alder Studios Inc/LLC)
- Payroll three-way: withheld 54,404 − 48,200 = 6,204 + employer 5,076 = 11,280 = bank tax debit ✓; net 48,200 ✓
- TB balances at 1,008,700.78 (gross); January 2025 net loss **42,677.78**

**Judgment calls I flagged rather than buried (open_items.md):**
1. Opening deferred 65,000 vs. note's 41,000 — the unsupported 24,000 equals the Trestle renewal exactly (possible pre-existing double count); left in 2200 unreleased as its own roll-forward line
2. Opening 4000 carries an unclosed 30,450 of apparent prior-year revenue — 2025 activity is disclosed separately (40,650); proposed ASC 250 opening reclass pending client confirmation, not made unilaterally
3. A/R 92,650, prepaids 9,600, and A/P 17,420 opened without detail — carried unchanged, schedules requested
4. The stray `documents/bank_statement.csv` (December **2025** dates, negative balances) was not used; January reconciled to `month_01/bank_statement.pdf` (extracted via pdftotext)

STATUS: **COMPLETE WITH OPEN ITEMS** — seven specific questions are in `deliverable/QUESTIONS.md` awaiting the client's reply.