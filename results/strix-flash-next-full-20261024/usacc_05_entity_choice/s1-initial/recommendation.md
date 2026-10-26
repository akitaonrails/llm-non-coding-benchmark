# Recommendation — entity and tax structure for Natarajan Herrera Advisory

Prepared: October 2026 engagement file. Facts from `documents/` (questionnaire, travel calendar, appraisal, projections). **All legal authority below is from `library/` (see INDEX.md); anything else is labeled UNVERIFIED and is not cited.** Key working assumption, stated prominently: **formation on February 2, 2026, as a California LLC**, unless the client directs otherwise (see QUESTIONS.md).

---

## 1. Bottom line

| Item | Recommendation |
|---|---|
| Entity | **California LLC** (not Delaware) |
| Tax classification | **Partnership** (default) — **do NOT make an S election now; it would be invalid** |
| Priya's equity | 50% capital + profits in exchange for the PriceLab tool (appraised FMV $120,000; basis $31,000) — **no gain recognized**, IRC §721 |
| Tomás's equity | $20,000 cash for a $20,000 capital account + **50% profits interest from day one** (Rev. Proc. 93-27 — not a taxable event on receipt); capital interest vests 3 years / 1-year cliff, with a protective §83(b) election within 30 days of grant |
| Compensation | No salaries; 50/50 distributive share of ~$260,000 year-1 net; self-employment tax applies; §199A 20% deduction likely available to Priya (Tomás's situation flagged, see §8) |
| Elections | **No Form 2553 in 2026.** Revisit only if and when Tomás becomes a U.S. resident under the substantial presence test — on his stated ~1/3-of-year pattern that is realistically **~2029, not 2027** (see §2) |

## 2. The controlling fact: the S election the founders want is legally unavailable in 2026

An S corporation **cannot have a nonresident alien shareholder** — 26 U.S.C. §1361(b)(1)(C) (`library/irc_1361_excerpt.md`). The library also notes that an election terminates the day the corporation ceases to be a small business corporation (`irc_1361_excerpt.md`, note on §1362(d)(2)).

Is Tomás a nonresident alien in 2026? Apply the substantial presence test, 26 U.S.C. §7701(b)(3)(A) (`library/irc_7701b_substantial_presence.md`), to his travel calendar (`documents/tomas_travel_calendar.csv`):

```
2026 weighted days = 118 (2026) + (1/3 × 96) (2025) + (1/6 × 66) (2024)
                   = 118 + 32 + 11 = 161  <  183
```

He passes the 31-day floor but fails the 183-point sum. **Tomás is a nonresident alien for 2026** (the library note adds: an alien with no green card who fails the test is a nonresident alien absent a first-year election under §7701(b)(4)). The §7701(b)(4) first-year election is named in the library but its conditions are not stated there; on its usual terms it is unavailable to someone present in the U.S. in the preceding years, which Tomás was (66 and 96 days) — **treat as unavailable; flagged as partially UNVERIFIED because the library does not state the conditions.**

**Client update (round 2): Tomás is in the U.S. "maybe a third of the year" — this puts him on the residency cliff edge.** One third of 365 days = 121.7 ≈ 122 days. Re-running §7701(b)(3)(A) on that pattern:

| Year | Weighted days (at ~122 U.S. days/yr) | Resident? | U.S. days actually needed |
|---|---|---|---|
| 2026 (actual: 118) | 118 + 96/3 + 66/6 = **161.0** | **No — confirmed** | — |
| 2027 | 122 + 118/3 + 96/6 = **177.3** | No | **128** (183 − 39.33 − 16 = 127.67) |
| 2028 (if 2027 = 122) | 122 + 122/3 + 118/6 = **182.3** | No — misses by 0.7 | **123** |
| 2029 (if 122/yr) | 122 + 122/3 + 122/6 = **183.0** | **Yes — exactly at the line** | 122 |

Steady state: coming D days every year gives weighted days D × (1 + 1/3 + 1/6) = 1.5D, so the residency line is **exactly 122 days per year**. "About a third of the year" (121.7) is within a day of flipping him into U.S. tax residency in the out-years; a Q4 push like 2026's, or continuation of the 66 → 96 → 118 trend (~140 days in 2027 → 195.3 → resident), would do it as early as 2027.

Consequences: (i) the S election is not merely void in 2026 — on his stated pattern it is also unavailable for 2027 and (by 0.7 of a day) 2028; the "S corp once resident" scenario in `year1_comparison.json` is realistically a ~2029 question, not 2027; (ii) the partnership structure is the durable answer, not a waiting room — plan it fully; (iii) **day counting is now the headline planning fact** — and because he lives in Monterrey with his spouse (confirmed), staying under vs. crossing the U.S. 183-point line interacts with Mexican residency/taxation, which is **outside the library**: get Mexican counsel before anyone optimizes his day count. Election deadlines for a future resident year remain as calendared (`library/form_2553_deadline.md`).

Also note, UNVERIFIED (not in library): whether U.S. immigration law lets a TN-status individual *work for / own* this entity from the U.S. is not addressed anywhere in the library. Client round 2 confirms **TN status, no green card and no application**, and that Tomás works **mostly from Monterrey** — which narrows the issue to the days he works physically in the U.S., but does not resolve it. **This must go to immigration counsel before Tomás performs services for the new entity from the U.S.** It does not change the entity analysis but could constrain the operating plan.

## 3. Why a partnership-taxed LLC, not a corporation — the §351 vs §721 math

**Priya contributes property with big built-in gain:** appraised FMV **$120,000** (`documents/tool_appraisal.pdf`), basis **$31,000** ($89,000 of development costs deducted 2023–2025 — questionnaire; confirmed by the appraisal's recital). Built-in gain: **$89,000.**

**If they form a corporation** (S or C), §351 nonrecognition requires that the *property* transferors control ≥80% immediately after the exchange (26 U.S.C. §351(a), §368(c) — `library/irc_351_excerpt.md`), and **stock issued for services is not counted as issued for property** (§351(d)). Here:

- Priya: tool ($120,000) → 50% of the stock.
- Tomás: $20,000 cash (property) + "client relationships and all the selling" (services), with his shares **vesting on a services schedule** — classic §83 service stock. Stock attributable to his $20,000 cash is at most ~$20,000/$140,000 ≈ 14% of the company ≈ **7 of 100 shares**.
- Property-transferor stock = ~50 + ~7 ≈ **57% < 80%** → **§351 fails**.
- Consequence: Priya recognizes gain = FMV of her stock ($70,000 = 50% × $140,000) − $31,000 basis = **$39,000** (character/rate not in library — UNVERIFIED rate). Tomás recognizes service compensation at FMV when vested: $70,000 − $20,000 paid = **$50,000 ordinary income** (§83; `irc_351_excerpt.md` note; `irc_83b.md`).

**If they form an LLC taxed as a partnership**, §721(a) gives nonrecognition on a contribution of property for a partnership interest **with no 80%-control requirement** (`library/irc_721_and_revproc_93-27.md`). Priya's $89,000 built-in gain: **$0 recognized.** Clean.

## 4. Tomás's 50/50 with vesting — the one trap that exists even in a partnership

Rev. Proc. 93-27 (`library/irc_721_and_revproc_93-27.md`): a **profits interest** received for services is not a taxable event (it would yield $0 on an immediate liquidation at FMV); a **capital interest** received for services is taxable compensation at receipt or vesting.

A straight "50% of everything" grant to Tomás is a **capital interest**: on day one he would take 50% of $140,000 of assets = $70,000, vs. $20,000 paid → **$50,000 ordinary income** immediately (or at each vesting, higher as the business grows — and it earns $260k–$370k/year, per `documents/projections.csv`).

Structure to fix it (the "how each contribution becomes equity" answer):

1. **Priya:** 50% capital + profits for the tool (FMV $120,000 per appraisal → capital account $120,000). §721, no gain.
2. **Tomás:** $20,000 cash → capital account $20,000, **plus a 50% profits interest effective at grant** (Rev. Proc. 93-27: no income on receipt — on an immediate liquidation he takes only his $20,000 back, nothing of Priya's $120,000).
3. **Capital vesting:** his right to 50% *capital* vests over 3 years, 1-year cliff (per their own wish), converting to full 50/50 capital over time. Each conversion is measured at then-FMV (§83) — future tax, open item (the library does not address conversion mechanics — UNVERIFIED detail).
4. **Protective §83(b):** for any capital-interest tranche treated as transferred at grant, file **Form 83(b) within 30 days of grant — no extensions** (§83(b); Treas. Reg. §1.83-2 — `library/irc_83b.md`); Rev. Proc. 2001-43 treats an unvested profits interest as held from grant if he is a partner from grant, and the library notes a protective §83(b) is customary. If instead Tomás simply takes the 50/50 **capital interest** at grant (their literal ask), the 83(b) locks his $50,000 inclusion at grant value instead of higher vesting-date values — recommend, and budget the ~$16,650 tax on it (assumed 33.3% rate, §6).

## 5. Why the friend's plan ("LLC + S election + $40k salaries") fails on its own terms

1. **Void election** — §1361(b)(1)(C): Tomás is an NRA for 2026 (§2 math). The LLC stays a partnership by default; the "self-employment tax savings" never happen.
2. **If the election somehow worked, $40,000 salaries are reckless.** Rev. Rul. 74-44; *Watson v. Commissioner*, 668 F.3d 1008 (8th Cir. 2012); FS-2008-25 (`library/reasonable_compensation.md`): a shareholder performing substantial services must take reasonable compensation before distributions; in *Watson*, $24,000 salary vs ~$200,000 distributions was recharacterized. Two full-time senior consultants generating $610,000 of revenue taking $40,000 each is squarely in *Watson* territory. Recharacterization exposure ≈ payroll tax on the distributions: 15.3% × $90,000 × 2 = **$27,540**, plus penalties and interest — i.e., roughly the entire "saving."
3. **§351 landmine** if they incorporate (§3 above): a ~$39,000 surprise gain for Priya before the first dollar is earned.
4. **Even the best-case legal version saves almost nothing** — see the year-2 S-corp scenario in `year1_comparison.json`: total ≈ $127,160 vs ≈ $112,344 for the recommended partnership, because §199A gives the partnership owners a 20% deduction on distributions that wages don't get (see §7).

## 6. Rate and fact assumptions used in every number here (PROMINENT — label: ASSUMPTION)

The library contains **no income-tax rate schedules, no SE-tax rate, no federal return due dates**. So:

- Composite income-tax rate **33.3%** (assumed federal 24% + California 9.3% marginal) — UNVERIFIED assumption; use only for comparison, not filing.
- Self-employment / payroll tax **15.3%** on the full amount (ignores the 92.35% net-earnings base and the Social Security wage cap — not in library, ASSUMPTION); applied to both employer and employee halves of FICA where wages exist.
- **Confirmed facts (client round 2):** Priya single, works from San Diego. Tomás married, lives in Mexico (no prenup), works mostly from Monterrey, in the U.S. ~1/3 of the year; clients all over the U.S. Tomás is still modelled symmetrically for comparison only — his NRA U.S. taxation and his Mexican taxation are **not addressed by the library** (open item §8).
- §199A thresholds per the library: ~$200,300 single / $400,600 joint (2026, "verify"), with a $75,000/$150,000 phase-in range (`library/irc_199a_sstb.md`). Both founders' taxable incomes here (~$104,000–$130,000) sit **below the single threshold**, where the SSTB limit "does not apply."
- Formation Feb 2, 2026; calendar tax years; CA sales $610,000 year 1. The CA gross-receipts fee is modelled on **all** $610,000 of receipts; the library does not state sourcing rules for a California-qualified LLC whose clients are nationwide and one member works from Mexico — flagged **[U]**, confirm before filing.

## 7. Year-1 arithmetic (full detail in `year1_comparison.json`)

Common: year-1 net before owner comp **$260,000** (questionnaire; projections.csv ties: 610,000 − 195,000 − 155,000 = 260,000 ✓). CA LLC-level: **$800 annual tax + $2,500 gross-receipts fee** (fee band $500,000–$999,999 for $610,000 of receipts) — `library/ca_llc_franchise.md`.

- **Plan as stated (assumed valid S corp, $40k salaries):** payroll 15.3% × $80,000 = $12,240; each founder: salary $40,000 + distribution $90,000 − QBI deduction 20% × $90,000 = $18,000 → taxable $112,000 × 33.3% = $37,296. Total ≈ **$90,132** — *but the election is void*, and §83/§351 items above are additional. As it would actually tax, it collapses to the partnership numbers.
- **Recommended (CA LLC as partnership):** each founder: share $130,000; SE tax 15.3% × $130,000 = $19,890; §199A: QBI deduction 20% × $130,000 = $26,000 (wages excluded from QBI don't apply — no wages; `irc_199a_sstb.md`); taxable $104,000 × 33.3% = $34,632. Entity $3,300. Total ≈ **$112,344** (≈ **$128,994** if Tomás's 50/50 capital interest is taxed at grant: + $50,000 × 33.3% = $16,650).
- **Other (S corp with reasonable comp, only possible once Tomás is a resident, e.g. 2027):** all $260,000 as wages ($130,000 each): FICA 15.3% × $260,000 = $39,780; **wages are not QBI** (`irc_199a_sstb.md`) → no §199A deduction; $130,000 × 33.3% = $43,290 each; CA corporation-level details not in library (only $800 shown; flag). Total ≈ **$127,160**.

Takeaway: even the best legitimate S-corp version roughly matches or loses to the partnership; and the version the founders proposed is both void and penalty-exposed.

## 8. Delaware rejected; open items flagged, not papered over

- **Delaware:** a DE LLC doing business in California must register as a foreign LLC in CA and **pays the same $800 + fee amounts anyway**; failure bars it from California courts and adds penalties (`library/ca_llc_franchise.md`). DE adds a second filing and DE-side costs (DE fees **not in library** — UNVERIFIED). No library-supported benefit for this business. Form in **California**.
- **Not resolved by the library (explicitly not advised on):** Mexican tax — now a **confirmed fact pattern**: Tomás lives in Monterrey, performs most work from Mexico, is married there with no prenup, and the client base is U.S.-wide. Mexican residency/worldwide-income taxation, U.S.–Mexico allocation of the partnership's income, U.S. withholding/reporting for a nonresident alien partner (the partnership's own obligations are not in the library), and Mexican community-property consequences all require Mexican/international counsel. TN-status work authorization for the days he works in the U.S.; whether the appraisal's "going-concern license basis" means Priya conveys title or licenses the tool (open item — see QUESTIONS.md).
- **Vesting vs "one class of stock" (§1361(b)(1)(D)):** moot for 2026 since the election is void anyway; if ever relevant, vesting mechanics would need re-checking under the library's §1361 text.

## 9. Alternatives considered and rejected

1. **LLC + S election (founders' plan):** void (NRA shareholder, §1361(b)(1)(C)); Watson recharacterization risk on $40k comp; no net saving. Rejected.
2. **C corporation:** §351 likely fails the 80% control test as structured (~57%) → Priya +$39,000 gain, Tomás +$50,000 ordinary income at formation, plus corporate-level tax (rate not in library) and no §199A at partner level. Rejected.
3. **Delaware LLC (+ CA foreign qualification):** same CA taxes, extra DE layer, no library-supported upside. Rejected.
4. **General partnership (no LLC):** same tax result, no liability shield, and the buy-sell/governance package we recommend is built on the LLC agreement (checklist is LLC-specific: `library/llc_buy_sell_checklist.md`). Rejected.
5. **50/50 capital at grant with no structure:** taxes Tomás on $50,000 now (and more if value rises and he waits for vesting without 83(b)). Rejected in favor of §4's profits-interest + vesting-capital design; if the client insists on straight 50/50, the 83(b) election within 30 days is mandatory, not optional.
