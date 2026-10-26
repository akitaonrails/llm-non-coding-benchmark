Now the appraisal PDF:

I have all client documents and the full library. Let me verify the key computations (substantial presence test, the year-1 tax models, and the critical election deadlines) with Python before drafting.

The schema was correct (my assert omitted `total`); rerunning the check:

Engagement complete. All six deliverables are in `workspace/deliverable/`, all JSON totals reconcile, and every authority cited is one of the ten files in `library/INDEX.md` (the only other `.md` mentions are internal cross-references between deliverables).

## Headline findings

**The founders' plan is void as stated.** Tomás fails the substantial presence test for 2026: 118 + 96/3 + 66/6 = **161 < 183** (he'd need 140 US days) — so he's a nonresident alien, and §1361(b)(1)(C) bars an NRA S-corporation shareholder. A Form 2553 election now would never be effective; the company would simply be a **C corporation**. And even in a world where he's a US resident, *Watson*-safe compensation (~$130k each) at $260k net exhausts the profit — the friend's "fortune in self-employment tax" is ~$0 (option totals: stated-plan reality $97,680 but understated by penalties/withholding; recommended $104,183 → ~$93,309 with the credits I conservatively excluded; hypothetical proper S corp $102,180).

**Recommendation:** one **California LLC taxed as a partnership** (Delaware buys nothing in CA — same $800 + $2,500 fee either way per the library), split 50/50:
- **Priya:** tool contribution ($120k FMV / $31k basis) → 50% capital interest, tax-free under §721 (no 80% control test, unlike §351).
- **Tomás:** $20k cash capital + **50% profits interest** vesting 3y/1y cliff — not taxable at grant under Rev. Proc. 93-27, with a **protective §83(b) election due Dec 2, 2026 (30 days, no extension)**. This sidesteps the §351(d)/§83 trap that would tax ~$50k of his service-stock in a corporation.

**Deliverables:** `recommendation.md` (analysis + rejected alternatives + assumptions register), `year1_comparison.json` (4 options, arithmetic shown, non-library rates flagged), `compliance_calendar.md` (83(b), 2553 reference dates, CA fee, estimates — each row marked ✔ library-backed or ⚠ assumed), `term_sheet.md` (vesting at cost for unvested, buy-sell triggers incl. divorce/spousal consent for Mexican community property, mediation→shotgun deadlock for the 50/50, transfer restrictions that also fence off future S-election ineligibility), `QUESTIONS.md`, `STATUS.md` — **COMPLETE WITH OPEN ITEMS**, chiefly: assumed Nov 2 2026 formation date, Tomás's actual day counts, TN-status work authorization (no immigration authority exists in the library — must clear with counsel before formation), and NRA taxation of his income share (library gap, flagged rather than invented).