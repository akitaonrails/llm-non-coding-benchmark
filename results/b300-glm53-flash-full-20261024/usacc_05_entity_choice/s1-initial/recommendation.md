# Recommendation — Natarajan Herrera Advisory

**Prepared:** October 25, 2026 · **Prepared for:** Priya Natarajan, Tomás Herrera
**Sources:** only files in `library/INDEX.md` (cited below). Client facts from `documents/`.
Anything relied on that is not in the library is labeled **[unverified]** and appears only as a stated assumption.

---

## 1. Bottom line

Form a **multi-member LLC through the California Secretary of State** (not only Delaware), operated as a
**partnership for tax purposes** (no S election), with:

- **Priya** contributing the PriceLab tool under **IRC §721** (`irc_721_and_revproc_93-27.md`) — no gain, no 80% control problem;
- **Tomás** contributing **$20,000 cash** as a purchased capital interest **plus** a **profits interest for services** that vests over 3 years (1-year cliff), so his sweat equity is **not taxable at grant** under **Rev. Proc. 93-27**, with a protective **§83(b)** filing under Rev. Proc. 2001-43 (`irc_83b.md`, `irc_721_and_revproc_93-27.md`);
- **50/50 of profits** from day one; 50/50 of capital only as his profits interest vests and his capital account grows;
- **Do not make the S election in 2026** — it is **not available at all** while Tomás is a shareholder (constraint 1 below). It becomes possible only in a later year if he meets the substantial presence test, and on the travel-calendar pattern that is not yet in sight.

The friends' plan ("LLC, S election, $40k salaries, distribute the rest") **fails on three independent grounds**: the election is invalid in 2026, the reasonable-compensation premise is weak on these facts, and the predicted payroll-tax savings exist only as long as the compensation is unreasonable — at defensible market salaries the corrected S corp is the most expensive option modeled. Details in §3 and in `year1_comparison.json`.

## 2. The three driving facts

**(1) Tomás is a nonresident alien for 2026, and an S corporation cannot have him as a shareholder.**
§1361(b)(1)(C) forbids a nonresident-alien shareholder (`irc_1361_excerpt.md`); an election by a corporation that ceases to be a small business corporation terminates (§1362(d)(2), same file). Under §7701(b)(3)(A) (`irc_7701b_substantial_presence.md`), Tomás meets the substantial presence test only if current + 1/3 prior + 1/6 second-prior days ≥ 183:

- **2026: 118 + (96 × 1/3) + (66 × 1/6) = 118 + 32 + 11 = 161 < 183 → nonresident alien.**

(He clears 31 days, but not 183.) So a 2026 S election with him holding 50% is void in year 1. Nothing in the library changes this; the only lever is his actual day count.

**Client confirmation (received this turn):** Tomás holds a **TN visa**, has no green card, and no residency application pending; his own estimate is **roughly one-third of the year in the US** (≈ 122 of 365 days) — consistent with the 118-day projection on his travel calendar. The conclusion above is robust to that estimate: even counting every US day as a presence day, 122 + (96 × 1/3) + (66 × 1/6) = 122 + 32 + 11 = **165 < 183**. The break-even is **140 current-year days** (140 + 32 + 11 = 183, holding 2024/2025 counts fixed) — far from anything the client describes. If any of his days turned out to be excludable under some rule outside the library, the tallied total could only fall, which would only reinforce the nonresident result. Precise year-end verification of the day log remains a standing calendar item, not an open question to the client.

**(2) Contributing the PriceLab tool to a corporation risks an $89,000 gain; to an LLC taxed as a partnership it does not.**
§351 requires property transferors **in control (80%, §368(c))** immediately after the exchange, and stock issued **for services is not treated as issued for property** (`irc_351_excerpt.md`). Priya would hold 50%; Tomás's stock is largely service-issued (the 50/50 is described as vesting-based compensation for "the client relationships and all the selling"). Without further allocation rules (Treas. Reg. §1.351-1 details are **[unverified] — not in the library**), we cannot conclude the property-transferor group controls 80%, so contributing the appraised tool to a corporation risks recognizing

> **FMV $120,000 − remaining basis $31,000 = $89,000 of gain** (appraisal: `tool_appraisal.pdf`; the $31,000 basis is now **confirmed by the client per her CPA** — about $89,000 expensed on her Schedule C over 2023–2025, workpapers not provided).

§721 has **no 80% control requirement**: a property contribution to a partnership in exchange for an interest is tax-free (`irc_721_and_revproc_93-27.md`). In an LLC taxed as a partnership, Priya takes a carryover basis ($31,000); because she has already **deducted $89,000 of development costs**, the $120,000 − $31,000 spread of built-in gain follows the asset into the firm, and the allocation of that built-in gain across partners (the §704(c) rules) is **[unverified] — not in the library** (open item).

**(3) The reasonable-compensation premise of the S-corp salary plan is weak on these facts.**
A boutique consulting firm whose owners generate essentially all revenue is exactly the *Watson* situation: distributions to shareholder-employees who generate the firm's income get recharacterized as wages where salary is set far below comparable professional pay (`reasonable_compensation.md`). Consulting is a **specified service trade or business** (`irc_199a_sstb.md`), i.e., the income is their skill. $40,000 salaries against $260,000 of profit is the fact pattern that triggers the recharacterization in *Watson* ($24,000 of salary vs. ~$200,000 of distributions). The library supplies the rule and the case, not a market salary figure — so the correct reasonable-compensation level for each founder is an **open item** (needs a market survey of pricing-strategy consultants; nothing in the library sets a number). In `year1_comparison.json` we model an **illustrative $100,000 each** purely to show the sensitivity, labeled as an assumption.

## 3. Why the recommended structure fits

**Entity.** LLC (a) delivers §721 treatment for the tool (no corporation can); (b) has no reasonable-compensation doctrine to police — partners are taxed on their shares of profit (the library's reasonable-compensation rule addresses S corporation shareholder-employees, `reasonable_compensation.md`); (c) satisfies "50/50 with vesting", which a corporation cannot replicate without §83 tax on service-issued stock (§83 mechanics per `irc_83b.md`; §351(d) treatment of service stock per `irc_351_excerpt.md`).

**Location.** Operations are in California, so the LLC **must** register as a foreign LLC in California and pays California's $800 annual tax + gross-receipts fee ($2,500 at $500k–$999,999 revenue) **wherever it is formed** (`ca_llc_franchise.md`) — the state of formation does not change the California exposure. Forming directly in California is the cleaner course for a services firm whose entire nexus is San Diego plus a California-serving practice, and it avoids running an out-of-state entity alongside the required registration. The same file gives the consequence of skipping that registration: the company is barred from maintaining an action in California courts, plus penalties. **[Unverified, not in library]:** Delaware's own formation/maintenance costs, California's corporate franchise tax on corporations, and whether California even recognizes S elections are all outside the library — further reason the S-corp option is modeled cautiously.

**Ownership / vesting.**
- Priya: capital interest from her §721 contribution; carries her $31,000 basis and the built-in gain.
- Tomás: two pieces. **(i)** A **capital interest purchased with his $20,000 cash** (he pays $20,000 and receives a capital account of $20,000 — self-supplied value, no bargain element, no compensation). **(ii)** A **profits interest for services**, designed so he would receive *nothing* on an immediate liquidation at fair market value beyond the return of his own capital — the Rev. Proc. 93-27 §4.01 safe harbor (`irc_721_and_revproc_93-27.md`). The profits interest is **50% of profits from grant**, **vesting 0/33/66/100%** at months 12/24/36 (1-year cliff), forfeit+repurchase at $0 for unvested portions. Under Rev. Proc. 2001-43 an unvested profits interest is held from grant if he is treated as a partner from grant; a **protective §83(b) election within 30 days** is customary (`irc_83b.md`; `irc_721_and_revproc_93-27.md`).
- Effect: a liquidation today returns each member's own capital account — Priya the tool value ($120,000), Tomás exactly his $20,000 — and nothing more to either (remaining value = $0 at today's FMV); **all existing value (tool + cash) sits inside the capital accounts, none of it attributable to Tomás's service interest**; **profits from day one split 50/50** — which is the economics they asked for ("his share vesting over 3 years since he's putting in less money"), arrived at without either founder recognizing compensation income at grant.

**Why not just restructure later.** Restructuring a profitable practice is never free — every later move is its own taxable transaction whose rules are outside this library, not a clean reset. The one moment when the choice costs nothing is now, before any entity exists and before the tool is placed inside one; that is why the structure decision belongs at formation.

## 4. Options rejected

1. **The friends' plan (LLC + S election + $40k salaries), 2026.** Invalid — §1361(b)(1)(C) bars Tomás as NRA shareholder (constraint 1). Even if he were eligible: (i) $40k is noncompensatory against a *Watson* fact pattern (constraint 3); (ii) the payroll-tax saving is smaller than in the pitch, because salaries must compete for the whole profit, and (iii) salaries are **not QBI** while partnership allocations are (`irc_199a_sstb.md`), so the S corp forfeits the 20% deduction on its entire wage portion. See `year1_comparison.json`.

2. **Delaware corporation (even C corp) now.** Same §351 gain risk on the tool ($89,000), same NRA-barred election, plus double tax (rates **[unverified]** — corporate rates are not in the library), plus Delaware maintenance on top of California fees. Rejected.

3. **S corp with Priya as sole shareholder and Tomás as W-2 employee.** Cleared of the NRA bar, but (a) gives Tomás no ownership — contradicts the founders' agreed 50/50 economics; (b) still requires setting market-level reasonable compensation for them both — the very issue the friends' plan tried to sidestep; (c) leaves a future buy-in for Tomás to somehow purchase — no lender and no values exist. Rejected as interim structure; retainable as a fallback if the partnership proves unworkable and Tomás later meets substantial presence.

4. **Corporation taxed as S corp in a later year** (when Tomás is a resident alien). **Deferred, not rejected forever.** If his pattern becomes many more days (not the current pattern), a real option becomes "convert partnership → S corp (or new corp) at reasonable compensation $X per market data". Preserve the option in the operating agreement (see `term_sheet.md` §9.4).

## 5. What the team should verify in later work

1. Market reasonable-compensation and market salary range for both roles (`reasonable_compensation.md` gives rule and precedent; no number).
2. Allocation of Priya's built-in gain across the partnership (the §704(c) rules) — **[unverified]**, not in the library.
3. Tomás's US taxation as a foreign partner: §1446 withholding, effectively-connected-income rules, US–Mexico treaty positions, Montana/Mexico income tax interplay — all **[unverified]**, not in the library. In our model we compute his tax as if he were a resident purely so the arithmetic closes; the actual NRA mechanics (which the library does not supply) will change that computation, and the direction of the change cannot be determined from what we have. The client's status confirmation this turn (TN visa, no green card, no application) goes to residency only — it supplies none of these mechanics, and no withholding vendor has been identified for the partner-level withholding decision.
4. California income tax bracket and filing requirements on him as a nonresident — **[unverified]**.
5. Choice of §83(b) timing on the profits interest: Rev. Proc. 2001-43's protective route; confirm with the client within 30 days of grant.
6. **Whether any part of the practice already operated in 2026 — the client did not answer this.** If it did, the formation dates, the first-year California fee timing, and the estimated-tax catch-up all move (see `compliance_calendar.md`); the structural recommendation itself does not change.

---

*Prepared by: engagement team. Every citation above is to a file in `library/INDEX.md`. Assumptions used for arithmetic are stated in `year1_comparison.json` and `STATUS.md`.*
