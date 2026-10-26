

Good question from the client — it's the most sympathetic version of the friend's plan, and it deserves a precise answer. Let me first re-read the library file so I quote exactly what it supports about adding shareholders later:





The computation is confirmed. Now let me re-read the exact current state of the files I need to edit, then write the client answer and update the deliverables:







I have full context on both files. Let me re-run the option (e) verification once, read STATUS.md, then make all edits:






All figures reconcile exactly with the earlier verified run. Now making all edits — JSON, recommendation §6/§7, calendar, STATUS:






Options (b)/(c) show a 1¢ rounding discrepancy between component sum (95,310.30) and stated total (95,310.31). Let me check the original unrounded computation:





All five options sum exactly, and every statute I cite is confirmed present in the library excerpt. One precision tweak — the library's sentence is specifically about S-corp *owner* wages, so I'll phrase §7.2 to match exactly rather than say "explicit":





All deliverables are updated and verified. Here is the answer for Priya and Tomás:

---

## Your question: "What if I list Priya as the only shareholder for now and add me later?"

**Short answer: that is the only version of your friend's plan that is technically legal — but only while you own *zero* stock, and the "later" runs into the exact same wall.** We priced it honestly anyway (new option **(e)** in `year1_comparison.json`). It costs more than the recommendation, and it breaks your deal in the meantime.

**1. "Later" is the same wall, just on a delay.** The law says a corporation may not *"have a nonresident alien as a shareholder"* — present tense, no grandfathering [§1361(b)(1)(C)]. The day you're added while still a nonresident, the S election terminates **that very day** and the company becomes a C corporation (§1362(d)(2) note in our statute excerpt). And eligibility turns on U.S. tax residency — green card or the substantial-presence test — which *you* can't schedule: your own numbers put you about **6 days short** of the 2027 flip point.

**2. Meanwhile the 50/50 deal forces a fork, and both branches lose.** Either you paper the real deal (a side agreement giving you half the economics) — which collides with the one-class-of-stock rule (§1361(b)(1)(D); mechanics outside our library, flagged [U]) — an election papered *around* is an election that unwinds later. Or you don't paper it: you're a wage employee of Priya's company, your $20,000 is a loan, your "half" is a wage promise, and **W-2 wages are not QBI** (our §199A library item says so directly — only distributions are). No equity, no capital-gain exit.

**3. The cheap part dies on day one anyway.** Your friend's $40k salaries don't survive *Watson* (library case: $24k salary recharacterized): two full-time pricing consultants producing all $610k of revenue must be paid near market. We modeled $130k each. Result: **$103,940** year-1 tax (up to **$111,592** if the S corp's small pass-through loss gets trapped by basis limits — unverified [U]) vs **$95,310** for the recommended LLC — *before* the day-you-get-added cost: Priya must **sell or gift you real stock at then-value**, a taxable event.

**4. The convergence point — the part that decides it.** If you actually become a U.S. resident under the SPT in 2027, the recommended LLC converts to an S corp anyway (Form 2553 window during 2027, final deadline Mar 15, 2028) — signed by the **existing 50/50 members, no stock transfer at all**. Same destination; your variant just pays tolls on the way: full payroll tax on every wage dollar, zero QBI (wages ≠ QBI), and Priya's 100% ownership pushes her over the assumed ~$200,300 SSTB threshold in year 2, killing the 20% deduction.

**5. "Our friend's CPA does this for everyone."** "Everyone" isn't an authority — and this fact pattern (nonresident co-owner, 50/50 economics, an eligibility rule papered around) is precisely the audit profile. If the CPA is that confident, ask them to put the position **in writing and sign the return**. Preparer-level exposure is the best litmus test, and we'll gladly read their memo.

**Bottom line: don't file Form 2553. Keep the calendar.** Your question is now logged as answered in `QUESTIONS.md`, priced as option **(e)** (all five options' totals re-verified to the cent — we also fixed a 1¢ rounding artifact in (b)/(c)), and analyzed in `recommendation.md` §7.2 and §6.