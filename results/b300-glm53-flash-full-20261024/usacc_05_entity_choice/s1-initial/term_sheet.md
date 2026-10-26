# Term Sheet — Operating Agreement ("Natarajan Herrera Advisory, LLC")

**Prepared:** October 25, 2026 · For discussion; not an agreement. Every bracketed citation is to a file in `library/INDEX.md`; items marked **[not in library]** are practice conventions we have flagged for counsel to verify.

This term sheet implements the exposure in `recommendation.md`: California LLC, partnership tax classification, Priya's §721 tool contribution, Tomás's $20,000 cash + 50% profits interest with 3-year vesting.

---

## 1. Parties and structure

- **Members.** Priya Natarajan ("Member A", single) and Tomás Herrera ("Member B", married, community property — Mexico).
- **Capital interests.** Member A: 100% of the capital as of formation, contributed as the PriceLab tool at $120,000 appraised FMV per `tool_appraisal.pdf` (tax basis $31,000, client-confirmed per her CPA, 2026-10-25 — workpapers not provided). Member B: a purchased capital interest of **$20,000** funded with his own cash at formation **[self-supplied; no bargain element]**.
- **Profits interest.** Member B receives **50% of profits ("Profits Units")** for services, designed per §4 below so that on an immediate liquidation **at fair market value** he receives **nothing** beyond return of his own $20,000 capital — the Rev. Proc. 93-27 §4.01 condition (`irc_721_and_revproc_93-27.md`).
- **Tax classification.** Partnership (no S election — `irc_1361_excerpt.md` bars Tomás as NRA shareholder; see `year1_comparison.json` option A).

## 2. Contributions

| Member | Property | FMV | Tax basis | Treatment |
|---|---|---|---|---|
| Priya | PriceLab codebase, models, docs | $120,000 | $31,000 (client-confirmed per CPA, 2026-10-25; $89,000 previously deducted) | §721 nonrecognition; **carryover basis $31,000**; built-in gain of $89,000 follows the asset — allocations must preserve it (allocation mechanics not in library: open item 3 in `STATUS.md`) (`irc_721_and_revproc_93-27.md`) |
| Tomás | Cash | $20,000 | $20,000 | Purchased capital interest |
| Tomás | Services (client relationships, selling) | — | — | 50% **profits interest**; *not* taxable at grant under Rev. Proc. 93-27 §4.01 if liquidation-at-FMV test met; protective §83(b) election file within 30 days per Rev. Proc. 2001-43 (`irc_83b.md`) |

Reliance caveat: the $120,000 FMV is the appraisal's own going-concern license basis; if the members dispute it at formation, a new appraisal 4 weeks later is possible. The $31,000 basis is now **client-confirmed per her CPA** (about $89,000 expensed on her Schedule C 2023–2025; received October 25, 2026) — the workpapers were not provided, so it remains a confirmed client/CPA assertion.

## 3. Capital accounts and liquidation waterfall

1. Capital accounts at formation: **Priya $120,000** (the PriceLab tool at appraised FMV, basis $31,000); **Tomás $20,000** (cash) — total $140,000.
2. **Liquidation at FMV on any date:** (a) return each member's positive capital account balance; (b) then remaining value **50/50** between Member A and Member B's **then-vested** Profits Units (unvested Profits Units lapse first per §4).
3. This waterfall is what makes Member B's service interest a **profits interest**, not a capital interest: **at grant**, liquidation at FMV of $140,000 equals the capital accounts, so Member B receives only back his own $20,000 and **nothing more** — the Rev. Proc. 93-27 §4.01 condition (`irc_721_and_revproc_93-27.md`). Without this waterfall, a 50/50 capital split granted for services (a capital interest) is taxable compensation at receipt or vesting (same file).

## 4. Vesting (Member B's Profits Units)

| Tranche date | Vesting % |
|---|---|
| Grant (2026-11-02) | 0% (forfeits all if exit earlier) |
| Month 12 (2027-11-02) | **33%** |
| Month 24 (2028-11-02) | **66%** |
| Month 36 (2029-11-02) | **100%** |

- **1-year cliff**: if Member B leaves before month 12, the Profits Units are **forfeited in full**; unvested portions repurchased at **$0** (per `llc_buy_sell_checklist.md` "repurchase at cost for unvested"; here cost = none: they were for services at grant).
- **Protective §83(b)** within 30 days of grant, filed per Treas. Reg. §1.83-2 30-day rule (`irc_83b.md`); because of the 2001-43 interim-years holding treatment, while unvested Member B nonetheless **is taxed on his distributive share** of each year's profits (that is the model in `year1_comparison.json`, option B).
- Dilution: the profits share is 50% of a fixed pie, so **Member A's economics go to 50% of all profits — subject only to forfeiture of his unvested fraction if he leaves — even though she contributed all of the capital value today**. Both members chose this when they asked for 50/50 with vesting; it is the agreed trade.
- Once fully vested, profits split 50/50; if the members agree capital ought to move toward parity, they may re-balance capital accounts by written amendment (see §9.3).

## 5. Transfer restrictions and spousal arrangements

1. **No transfer** of any interest without drafting member's consent, except: (i) inheritance-on-death; (ii) transfers to the other member.
2. **Tomás's spouse consent**: Tomás is married, resides in Mexico, and (client-confirmed this turn) has **no prenuptial agreement**; the questionnaire describes the regime as Mexican community property. The spouse must consent in writing to the operating agreement **spousal provisions**, and agree that the Profits Units are Tomás's separate business interest dealt with solely under the buy-sell rules. The applicable legal consequence of the Mexican regime on US member units is **[not in library — regime specifics and marriage date not provided; open item]**; per `llc_buy_sell_checklist.md` we nonetheless require a signed consent before/at grant and on any transfer — the no-prenup fact makes this consent more important, not less.
3. **Divorce clause** (specifically required here): on Tomás's divorce the spouse must sign a **waiver of possession** to the units and any interest is treated as part of the **buy-sell event** (section 6 trigger (v)), not transferred outright.
4. Community-property caution: the checklist item includes "transfer restrictions and spousal consent in community-property jurisdictions" — the spouse's written consent plus the operating-agreement clause are the practical backbone; the underlying law of the Mexican community regime is **[not in library]**.

## 6. Buy-sell triggers and pricing (`llc_buy_sell_checklist.md`)

| # | Trigger | Mechanics |
|---|---|---|
| i | Death | Estate/nominee **must sell**, surviving member **may elect to buy** at the price in §7; payment per §7 |
| ii | Disability (long-term, >6 months without substantial work) | Effectively a forced sale by the disabled member, right of first refusal to the other; price per §7 |
| iii | Voluntary departure (resignation) | Departing member offers units for sale; other member may elect to buy at **book value or FMV, whichever the departing member takes, subject to discounts** per §7 |
| iv | For-cause removal (material breach, fraud, disqualification by conviction or refusal of fiduciary duty vetting) | Interests subject to **mandatory repurchase at the lower of cost or FMV** at the time of the event — an agreed penalty clause **[penalty enforceability not in library — flag for counsel]** |
| v | Divorce (Tomás) | Spousal interest must be bought out entirely per the divorce protocol in §5.3 |
| vi | Bankruptcy / insolvency | Mandatory sale; the checklist lists bankruptcy as a trigger event (`llc_buy_sell_checklist.md`) — the effect of a member's bankruptcy on the units under US law is **[not in library — flag for counsel]** |
| vii | Attempted transfer in breach of §5 | Deemed trigger (iii) |

While **unvested** Profits Units exist, the repurchase price for those units is **$0 under every trigger** (vesting rule controls; `llc_buy_sell_checklist.md`).

## 7. Price, discounts, payment

1. **Default price:** appraised **FMV** unless members mutually elect a **formula**.
2. **Appraisal:** a member-selected appraiser and one chosen by the other side; if they differ more than 10%, average — **[arbitration structure not in library]**; appraisal to be on the same going-concern license basis used in `tool_appraisal.pdf`.
3. **Discounts:** lack of control / lack of marketability discounts apply to the departing interest **as the appraisal concludes**, taken from the departing member's value, not added to the buyers'. Buy-sell checklist contemplates discounts — the actual determination is appraisal-driven.
4. **Payment:** 25% cash at closing; balance over **48 months** with interest at prime + 2% **[payment terms, the interest rate, and any usury limit are not in library — practice; flagged for counsel]**.
5. **Pre-emptive funding:** the buying member covenants to carry key-person insurance so trigger (i) is funded at all times **[insurance mechanics not in library — practice item]**.

## 8. Deadlock resolution (`llc_buy_sell_checklist.md`)

1. Ordinary matters: 50/50 votes; **deadlock** = a matter voted on twice more than 7 days apart without resolution.
2. **Step 1 — Mediation:** either member may trigger; 30 days.
3. **Step 2 — If still deadlocked: mutual buy-sell ("shotgun").** Sender states a **per-unit price and notifies the other member, who must either (a) sell all of their units at that price, or (b) buy the sender's units at that price**, closing within 45 days.
4. Drag-along / tag-along rights: the checklist directs that these be included for closely held two-member firms (`llc_buy_sell_checklist.md`); their full mechanics are **[not in library — practice item for counsel]**.
5. If deadlock is intractable (three deadlocks in 12 months): the operating agreement permits **plain dissolution** as a terminal step, **[dissolution tax math not in library — flag]**.

## 9. Governance and amendment

1. **Managers:** both members; routine operational items decided by the manager whose function it is; items above a threshold go to member consent per §8 deadlock rules. No management fee without both consents.
2. **Distribution policy:** profits allocate **50/50** for tax purposes per the waterfall and capital accounts; **cash distributions** require unanimous consent, but the members state a good-faith intent to make quarterly distributions sized to the partners' tax bills on their allocations — **[not in library, practice item]**.
3. **Amendment:** unanimous written consent; capital-interest rebalancing (toward parity) described in §4 is a permitted amendment **if** applicable tax accounting remains neutral to Priya's $89,000 built-in-gain preservation (basis preservation client-confirmed per `QUESTIONS.md` Q2, answered 2026-10-25; allocation mechanics: `STATUS.md` open item 3).
4. **S-corp flip (pre-agreed contingency):** if Tomás ever meets the substantial presence test (formula in `irc_7701b_substantial_presence.md`: current + 1/3 prior + 1/6 prior-prior ≥ 183) and both members vote for it, the members agree to re-appraise and a **corporate S election** under `irc_1361_excerpt.md` and `form_2553_deadline.md` timing — at that point reasonable compensation must be set at a market rate per `reasonable_compensation.md`. The members pre-commit to the survey work but NOT to flipping.

