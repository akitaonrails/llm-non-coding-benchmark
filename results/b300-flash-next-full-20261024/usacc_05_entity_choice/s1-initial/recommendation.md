# Recommendation — Natarajan Herrera Advisory

**Bottom line.** Form a **California LLC**, taxed as a **partnership**, 50/50 profits with capital accounts tracking what each actually contributes. **Do not attempt the S election** — it is legally impossible while Tomás is a nonresident alien. Revisit S status for 2028 **only if** Tomás meets the substantial presence test in 2027. Every number below that uses a tax rate or dollar threshold is an **assumption labeled as unverified** — the library contains no rate schedules (see §8 and `year1_comparison.json`).

## 1. The friend's plan fails at step one

The plan is "form an LLC, elect S-corp, pay $40,000 salaries, distribute the rest." An S corporation may not **have a nonresident alien shareholder** — that disqualifies the corporation entirely as a small business corporation, and any election is invalid from inception (or terminates the day eligibility is lost, §1362(d)(2) noted in `library/irc_1361_excerpt.md`). [26 U.S.C. §1361(b)(1)(C)]

Is Tomás a nonresident alien? Yes, on these facts:

- He has no green card and none pending (questionnaire; **reconfirmed by the client in the Oct 2026 response**).
- Substantial presence test, 2026 (formation year): **118 + 96/3 + 66/6 = 118 + 32 + 11 = 161 < 183** → fails the test (he meets the 31-day prong but not the 183-point sum). [26 U.S.C. §7701(b)(3)(A)]
- 2025: 96 + 66/3 + (2023 days)/6 ≤ 96 + 22 + 61 = 179 < 183 even if he had been present all 365 days capped at… precisely: the maximum possible 2023 contribution is 365/6 ≈ 60.8, so 2025 was ≤ 178.8 → nonresident in 2025 as well.
- The first-year election under §7701(b)(4) (referenced in `library/irc_7701b_substantial_presence.md`) cannot rescue 2026 — he was already present in 2024–2025, so 2026 is not a "first year"; the library does not restate the election's conditions, so this reasoning is labeled **unverified**.
- **Unverified assumption:** TN-visa days count toward the test (TN holders are not "exempt individuals"). The exempt-individual rules are not in the library. Same conclusion results either way for 2025–2026 only if the days count; if TN days did *not* count, he is even more clearly a nonresident.

**Sensitivity (important):**
- 2026: projected 118 days gives 161 points. If he actually reaches **140 U.S. days** in 2026, the sum hits 183 and he becomes a **resident** — which would also make a 2026 S election conceivably reachable, so track his days before filing anything.
- 2027: points = days₂₀₂₇ + 118/3 + 96/6 = days + 55.33 → **≥ 128 U.S. days in 2027 makes him a 2027 resident**, and then a valid S election becomes possible effective 2028 (Form 2553 could be filed any time during 2027, or by ~March 15, 2028 — `library/form_2553_deadline.md`).
- **Client update (Oct 2026):** he says he is in the U.S. "**maybe a third of the year**" ≈ 122 days → projected 2027 sum = **122 + 39.33 + 16 = 177.33 < 183**, so the nonresident assumption is confirmed as the planning base — **but with only ~6 days of margin below the 128-day flip point**, well inside the vagueness of "maybe a third." The monthly day log (term sheet §7; calendar) is what turns this from an assumption into a fact. A flip to residency is not a disaster — it just changes the model (worldwide taxation; S election becomes reachable) — but every number in this memo would be re-run.

## 2. Recommended structure

**Entity/tax:** LLC **formed in California** (not Delaware — see §4), taxed as a partnership (multi-member LLC default; no election to file). Priya and Tomás share **50/50 in profits**; capital accounts reflect actual contributions ($120,000 / $20,000).

**How each contribution becomes equity:**

- **Priya — PriceLab tool.** Independent appraisal FMV **$120,000** (Coastline Valuation Advisors, valuation date Jan 15, 2026); her remaining basis is **$31,000** ($89,000 of development costs already deducted 2023–2025). Contributing it to the partnership in exchange for a partnership interest is a **non-recognition event** — no gain on the $89,000 of built-in gain, and *no 80% control requirement* to trip over. [26 U.S.C. §721(a), `library/irc_721_and_revproc_93-27.md`] Her capital account is credited at FMV ($120,000); her **outside basis is $31,000** (carryover — standard doctrine, **not restated in the library; unverified**). The built-in gain must be tracked (a §704(c)-type allocation on any sale/distribution — **outside the library; unverified**).
- **Tomás — $20,000 cash + services ("client relationships and all the selling").** Services are not a contribution that buys tax-free equity in a partnership: a **capital interest** (share of existing capital) received for services **is taxable compensation** at receipt or vesting. [Rev. Proc. 93-27, `library/irc_721_and_revproc_93-27.md`] So structure his 50% as a **profits interest**:
  - His $20,000 cash buys a $20,000 **capital account**.
  - His 50% share of *future profits* is a **profits interest** — under the safe harbor, the IRS will not treat receipt as a taxable event, because on an immediate liquidation at FMV he would receive nothing beyond return of his $20,000. [Rev. Proc. 93-27 §4.01]
  - Vesting (3 years, 1-year cliff, as requested) applies to the profits interest. Under Rev. Proc. 2001-43 an unvested profits interest is treated as held from the grant date if he is treated as a partner from grant, and a **protective §83(b) election within 30 days** is customary — no extensions exist. [Rev. Proc. 2001-43; 26 U.S.C. §83(b); Treas. Reg. §1.83-2, `library/irc_83b.md`]
- **Result:** $120,000 : $20,000 capital, 50/50 economics, no taxable compensation event at formation, and Priya's appreciation sheltered by §721 rather than exposed.

**Compensation:** take **no salaries and no guaranteed payments** in year 1. Guaranteed payments are not QBI and would push income out of the §199A-safe zone; pure distributive shares preserve the 20% deduction while below threshold (§3). Distributions in excess of basis are the cash-flow constraint to watch (Priya's basis is only $31,000 — **unverified doctrine**).

## 3. §199A — the deduction the friend's plan would have squandered anyway

Consulting is a **specified service trade or business**, so the 20% QBI deduction dies once taxable income exceeds the threshold (library: ~$200,300 single / $400,600 joint for 2026, "verify") plus the $75,000/$150,000 phase-in. [26 U.S.C. §199A(d)(2), (e)(2), `library/irc_199a_sstb.md`] **Below the threshold the SSTB limitation does not apply.**

- Recommended structure: each founder's year-1 share ≈ **$128,350** → well below threshold → each eligible person takes ≈ 20% × share. (Salaried plan: **W-2 wages are not QBI; only the $85,010 K-1 share is** — the salary choice literally converts QBI into non-QBI wages.)
- Year 2 ($370,000 → $185,000 each): Priya's taxable income stays below ~$200,300 — still inside, but the margin is thin. Any outside income, marriage, or faster growth pushes her into the phase-in; revisit before year 2.
- **Assumed (unverified):** the §199A deduction is unavailable to a nonresident alien, so Tomás's share may generate no deduction.

## 4. Why California, not Delaware

Operations are in California, so the entity is "doing business in California" regardless of where it is formed. A **Delaware LLC must register as a foreign LLC in California and pay the same $800 annual tax plus the gross-receipts fee** — and failure to register bars it from maintaining an action in California courts and incurs penalties. [Cal. Corp. Code §17708.02; Cal. Rev. & Tax. Code §§17941, 17942, 23153, `library/ca_llc_franchise.md`] Year-1 revenue $610,000 → **$2,500 fee band ($500k–$999,999)**, plus the $800 annual tax; year 2 revenue $820,000 stays in the $2,500 band. Delaware would add a second state's franchise tax and a registered agent — amounts the library does not cover, so **not quantified** — for zero tax or liability benefit here. "Like startups do" is a venture-funding convention; this is a cash-flow consulting firm.

## 5. Why the $40,000-salary idea is wrong even in a world where it is legal

An S corporation shareholder performing substantial services **must** be paid reasonable compensation before taking distributions; in a personal-services firm where the owners generate essentially all revenue, courts recharacterize distributions as wages and assess payroll taxes, penalties and interest (*Watson*: $24,000 salary vs ~$200,000 distributions recharacterized in large part). [Rev. Rul. 74-44; *Watson v. Commissioner*, 668 F.3d 1008 (8th Cir. 2012); FS-2008-25, `library/reasonable_compensation.md`] Two full-time pricing consultants producing $610,000 of revenue are worth far more than $40,000 each; the plan's "savings" are exactly the recharacterization risk. (This matters again if you convert to S status in 2028 — set salaries near market then.)

## 6. Year-1 comparison (detail in `year1_comparison.json`; all rates are labeled assumptions)

| Option | Entity tax | Priya | Tomás | Payroll | Total |
|---|---:|---:|---:|---:|---:|
| (a) Friend's plan **as if valid** — impossible | $3,300 | $26,308 | $26,308 | $12,800 | **$68,716** |
| (b) **Recommended** — CA LLC partnership | $3,300 | $23,700 | $32,039 | $36,271 | **$95,310** |
| (c) DE LLC partnership (extra unquantified DE costs) | $3,300 | $23,700 | $32,039 | $36,271 | **$95,310** |
| (d) Friend's plan **actual** — invalid election, corporate status elected → C-corp | $37,029 | $22,422 | $28,197 | $12,800 | **$100,448** |

Read honestly: the recommendation costs about **$26,600 more** than the impossible fantasy — that gap is SE tax you legally owe on partnership distributions; there is no way to buy it back at 50/50 ownership with a nonresident-alien owner. It is the *lawful* minimum of the three pass-through paths, beats the botched-corporation trap (d) by ~$5,100, and (a) carries *additional* unpriced exposure: *Watson* recharacterization (had it been possible) and, as actually executed, an invalid election. Tomás's line is the **worst case that all his services are U.S.-performed**. The client has since confirmed the direction — he works **mostly from Monterrey**, Priya is all-San-Diego — so his true U.S./CA tax should be **below** the shown figures; the exact split is still unknown, so the upper bound stands in the table (sourcing rules are outside the library; see `QUESTIONS.md` open item 2).

## 7. Rejected alternatives

1. **S election now (the friend's plan).** Invalid — §1361(b)(1)(C) flatly bars a nonresident alien shareholder; no Form 2553 deadline maneuvering cures ineligibility (`library/form_2553_deadline.md` late-election relief requires all shareholders *eligible for the entire period* — Tomás never was in 2026). Also fails the reasonable-compensation test (§5).
2. **S corp with Priya as sole 100% shareholder, Tomás as employee.** Fixes eligibility but abandons the 50/50 deal, and puts Tomás's upside in wages of a company he half-owns — rejected as inconsistent with the founders' stated intent; also wages for a TN employee of a company he effectively owns raises its own immigration problems (§8).
3. **C corporation via §351.** §351 shelters property-for-stock exchanges only if the transferors of **property** hold **80%** control immediately after (§368(c)), and **stock issued for services is not issued for property** — it is compensation income at FMV when vested (§351(d); §83). [26 U.S.C. §351(a),(d); §368(c), `library/irc_351_excerpt.md`] Priya's tool (worth $120k of the $140k contributed) exchanges for only ~50% of the stock — **less than 80% — so §351 fails for Priya too and she would recognize gain on the appreciated tool**, while Tomás pays tax on stock received for selling. Then double taxation, no QBI, and 30% NRA dividend withholding on Tomás (treaty rate **not verifiable in library**). Option (d) prices the disaster.
4. **Delaware LLC, partnership** (§4): identical tax, extra cost, extra compliance.
5. **Tomás as contractor instead of owner.** Sidesteps nothing — the founders want him as a 50% owner; a contractor arrangement re-creates his selling-for-nobody's-equity problem and misprices the deal.
6. **Capital interest for Tomás with an 83(b).** Viable fallback if the safe harbor's "nothing on liquidation" condition can't be met as drafted: he'd pay tax on grant-date FMV of the restricted 50%, no extension beyond 30 days (26 U.S.C. §83(b)). Worse: real inclusion today versus $0 under the profits-interest route, and he pays tax on value he may forfeit.

## 8. Flagged but NOT in the library (unverified / outside scope — do not act on these from this memo)

- **Immigration:** TN status is tied to employment by a U.S. employer in the TN profession; working for (and especially as an owner-employee of) a new company may not fit TN terms at all. **Consult immigration counsel before either founder works for the entity.** Nothing in the library touches this.
- **Mexico-side tax on Tomás's Monterrey-work income, U.S.–Mexico treaty tie-breaker and dividend rates, totalization agreement:** not in library — unverifiable; his worst-case numbers assume zero relief. Client furnished no treaty/Mexican-filing information; Mexican advisor engaged (calendar).
- **Partnership withholding on a foreign partner's share of U.S.-source income/ECI (Form 8804/8805-type regime):** now directly relevant because Tomás is a confirmed foreign partner — **not in library**; raise with a U.S. international tax advisor before Year-1 close (calendar line), do not act from this memo.
- **All rates:** federal brackets/standard deduction (assumed 2025), SE tax 15.3%/92.35%/$176,100, FICA, FUTA/CA UI, CA flat 9.3% proxy for graduated CA rates, 21% corporate, 15% qualified dividend, 30% NRA withholding, $199A thresholds "≈verify" per library.
- **Partnership doctrine not restated in library (used but unverified):** LLC members' distributive shares subject to SE tax; outside-basis carryover under §722-type rules; §704(c) built-in-gain allocations; NRAs taxable on ECI at graduated rates without standard deduction; no §199A for NRAs; sourcing of services income.
- **S-conversion watch items for 2028:** §1361(b)(1)(D) one-class-of-stock vs. vesting/buy-sell terms; §1362(d)(2) auto-termination if Tomás ever reverts to nonresident status; Form 2553 timing; *Watson* salary study.

## 9. Open items (after the client's Oct 2026 response)

**Answered and folded in:** Tomás is TN, no green card or application, ~⅓ of the year in the U.S. (≈122 days → projected 2027 SPT 177.33 < 183, nonresident base confirmed but ~6 days from the flip); Priya works all from San Diego; Tomás works mostly from Monterrey; Tomás married in Mexico **with no prenup** (spousal consent is now a required closing condition), Priya single.

**Still unknown — standing assumptions/flags, none of which changes the direction:** formation timing (Nov 3, 2026 assumed, unconfirmed); exact Mexico/US work split (100%-US modeled as upper bound); the wife's willingness to sign (made a condition precedent); outside income (assumed none — watch Priya's thin Year-2 §199A margin, ~$15,000 of headroom); TN category/employer-of-record/role details (immigration counsel gate stands); draw policy (flexible assumed; Priya's ~$31k basis is the constraint); buy-sell note term / insurance budget / for-cause discount (term-sheet placeholders, not invented); treaty and Mexican-tax positions (outside library). Full disposition in `QUESTIONS.md`.
