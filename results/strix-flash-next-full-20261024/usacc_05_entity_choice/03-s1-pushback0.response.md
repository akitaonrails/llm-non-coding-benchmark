Good question from Tomás — let me check exactly what the library says about election termination and re-election before answering, so the reply is properly grounded:

The library settles this cleanly — and notably, the "swap trick" *does* fix one problem (§351) while making everything else worse. Updating the deliverables to address it, then I'll answer:

Deliverables are updated. Here's the answer for Tomás:

---

**Tomás — short answer: yes, we're sure, and the "Priya only now, add you later" version actually makes things worse, not better.** Full analysis is now in `recommendation.md` §5(5) and §9(6), with a do-not-attempt line in the compliance calendar.

**Why your CPA's playbook doesn't fit you.** It works for startups where every owner is a U.S. person. Your fact pattern isn't that: you were in the U.S. only 118 days in 2026 (weighted total 161 < 183), so you're a nonresident alien, and a nonresident alien **cannot be an S shareholder** — that's black-letter, §1361(b)(1)(C). It also isn't a clean incorporation: Priya brings a tool with $89,000 of built-in gain ($120k FMV, $31k basis), which §721 (partnership) waves through for free but §351 (corporation) nearly trips.

**What the swap trick actually does.** To be fair, it fixes two things at formation: Priya alone passes the S eligibility rules, and her tool contribution passes §351's 80%-control test (100% by herself), so no $39,000 gain on day one. Then it breaks everything else:

1. **The election dies the day you're added.** The library's §1362(d)(2) note is blunt: the election terminates "on the day the corporation ceases to be a small business corporation" and it "is **then a C corporation**" — an unplanned **mid-year** C-corp conversion, and the only relief in the library (Rev. Proc. 2013-30) requires all shareholders to have been eligible "for the entire period," which is impossible with you in it. On your travel pattern you don't even become a U.S. resident until ~2029, so the window stays loaded for three years. (Whether there's also a 5-year bar on re-electing: that rule isn't in our source library, so we flag it **unverified** rather than cite it.)
2. **Waiting destroys your $0 entry.** Right now your 50% profits interest costs you **nothing** on receipt (Rev. Proc. 93-27). Stock granted to you in 2027–2029 is compensation income at **fair market value when it vests** (§83) — and the company is projected at $260k–$370k/year by then, so you'd be taxed on a value far above today's $70,000.
3. **Priya pays everyone's tax alone while you wait.** Illustrative year 1 (our assumed rates): $130k comp + $130k distribution → FICA $19,890 + her income tax $77,922 + $800 entity ≈ **$98,612, all on Priya**, while you receive $0 and own $0. The recommended LLC pays $112,344 **combined** — with you at 50% from day one.
4. **You'd own nothing for 1–3 years.** Every protection in the term sheet — vesting, buy-sell, shotgun deadlock, spousal joinder — assumes you're a member. "We'll add you later" is exactly the promise our buy-sell checklist exists to prevent.

**Bottom line:** the workaround buys you a valid S election only until the moment you actually become an owner — at which point you're a C corp mid-year, you take a much bigger §83 tax hit, and you've worked half the business for a promise. The recommended California LLC keeps Priya's contribution tax-free, gets you in at $0, and costs about $15k less in year 1 than even the fully-compliant S-corp alternative.

---

Files touched this round: `recommendation.md` (§5 item 5, §9 item 6), `compliance_calendar.md` (formation-window line), `STATUS.md` (round-3 note). `year1_comparison.json` and `term_sheet.md` needed no changes — the recommendation is unchanged.