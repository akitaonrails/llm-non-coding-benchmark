# Tax review — proposed Oakline Holdings restructuring (Nadia Oakline)

**Prepared by:** reviewing tax advisor (response to Summit Peak Wealth Advisors proposal of 2026-02-11)
**For:** Nadia Oakline
**Date:** 2026-10-25
**Scope:** This opinion relies solely on the closed reference library in `workspace/library/` (see `library/INDEX.md`). There is no internet access. Anything not supported by the library is labeled **unverified**. Companion deliverables: `numbers.json` (all arithmetic), `agreements_required.md`, `QUESTIONS.md`, `STATUS.md`. **Updated 2026-10-25** to incorporate the client's responses and her follow-up question (see *Facts relied on* and the addenda at the end).

---

## Executive summary

The advisor's proposal is safe in name only. Of the four steps, two are acceptable with modifications, one is acceptable only in part, and one is rejected outright. The single most important point:

> **Do not contribute the Helio Grid Inc stock to the holding company.** Doing so would delete the §1202 (QSBS) exclusion on her stake — at current values, **$9,388,000 of otherwise excludable gain** would be put at risk — to chase a "reinvest without tax" benefit that the library does not support.

**Timing update (client, 2026-10-25):** a Helio Grid sale is realistic within **12–18 months**, with her stake worth roughly **$9–10M** at exit. The sequencing rule in the revised plan is therefore operative from day one: the shares never enter Holdings, and the sale happens outside the structure. Potential gain at exit: **$8,988,000–$9,988,000** ($9–10M less the $12,000 basis) — fully under the $10,000,000 per-issuer cap at both ends.

Summary verdicts:

| Proposed step | Verdict |
|---|---|
| 1. Form WY holding LLC taxed as partnership (Nadia 99% / revocable trust 1%) | **Do, with modifications** |
| 2. Contribute *all* interests, including the 30% of Helio Grid Inc | **Do in part; do NOT contribute the Helio Grid stock** |
| 3. Interest-free loans among subsidiaries; "one bank account, one set of books" | **Reject as proposed; substitute documented AFR-interest loans** |
| 4. "One return; no tax event — it's all a §721 contribution" | **Reject as stated**: the §721 claim is only partly true, and "one return" does not hold at the state level |

---

## Facts relied on

- `documents/org_chart.md` — four holdings: Oakline Services LLC (SMLLC, disregarded; HVAC, ~$1.1M/yr, 42 employees), Oakline Properties LLC (SMLLC; two buildings leased to Services; $1.9M nonrecourse mortgage; **negative tax capital $(380,000)**), Oakline Digital LLC (SMLLC; losses), and Helio Grid Inc (DE C corp; Nadia 30% founder common bought at incorporation for **$12,000**; current 409A value of her stake ≈ **$9.4M**).
- `documents/properties_balance_sheet.md` — buildings $3.4M, accumulated depreciation $(1.12M), land $0.6M, due-from-Services $400k, mortgage $(1.9M) (refinanced 2024; **$1.2M of refinancing proceeds distributed to Nadia in 2024**), owner's tax capital $(380,000).
- `documents/intercompany_cash_flows.csv` — undocumented loans: Properties → Services $250,000 (2024-03-01) and $150,000 (2025-06-15), total $400,000; Services → Digital $150,000 (2025-09-01, email only).
- `documents/helio_grid_stock_purchase_agreement_excerpt.pdf` — 3,000,000 shares of common at $0.004 = $12,000, **original issuance** directly from Helio Grid, Feb 18, 2020; company represented gross assets ≤ $1,000,000 and qualified-trade/business C-corp status; §83(b) election filed 2020-03-02.
- `documents/advisor_proposal.pdf` — the four steps and claimed benefits reviewed below.
- **Client responses (received 2026-10-25):** a Helio Grid sale is realistic in 12–18 months with her stake worth about $9–10M; the 1% member is her **revocable living trust**, added because the advisor said "we need two partners"; the intercompany advances were never papered — "No paperwork. I just move money where it's needed." She has no further information on the remaining open points; unresolved items are flagged explicitly below and in `QUESTIONS.md`/`STATUS.md`.

Where a fact is missing I state the assumption prominently rather than inventing one; open items are collected in `QUESTIONS.md`.

---

## Analysis of the proposed steps

### Step 1 — Form Oakline Holdings LLC (Wyoming, taxed as a partnership; Nadia 99% / revocable trust 1%)

**Consequence.** Forming a holding LLC and electing partnership tax treatment is, standing alone, not a taxable event, and §721(a) provides the general rule that no gain or loss is recognized on the contribution of property to a partnership for an interest (26 U.S.C. §721(a) — `library/irc_721_and_752.md`). The tax consequences that flow depend on *what* is contributed (Step 2) and *how* the entity is run (Step 3), not on the formation itself.

**State/multistate consequence.** A Wyoming holding entity that is managed from Colorado has Colorado nexus (commercial domicile) and files in Colorado; Wyoming has no income tax but requires an annual report; and holding membership interests in LLCs doing business in Colorado does not avoid Colorado filing for the income that flows through (Practitioner summary — `library/state_nexus_summary.md`). Forming in Wyoming therefore buys essentially **no** state tax benefit for her situation; it adds a second state's administrative obligation.

**Verdict: DO, with modifications.**
1. Fine to form, but choose the state for non-tax reasons; recognize Colorado filings cannot be avoided regardless (`state_nexus_summary.md`).
2. **The 1% member (client confirmed: her revocable living trust, added because the advisor said "we need two partners").** The trust's funding mechanism (gift vs. capital contribution) and its tax classification still have no authority in the library — **unverified** — so estate counsel must confirm them before the 1% is funded; see `QUESTIONS.md` (unresolved). Note the analytical consequence that should not be lost: the *mere existence* of the 1% member is what drops Nadia's share of the $1.9M mortgage from 100% to 99% and produces the ≈ $19,000 deemed-distribution/gain item in Step 2(b) — the advisor's "two partners" requirement and the tax trigger are the same fact.

### Step 2 — Contribute all interests, including the 30% of Helio Grid Inc

**General rule.** §721(a): no gain or loss on contribution of property for a partnership interest (26 U.S.C. §721(a) — `library/irc_721_and_752.md`). The advisor's "no tax event" is *partly* right — but there are two serious exceptions, one of them the costliest mistake in the proposal.

#### 2(a) Helio Grid stock — **the QSBS destruction problem**

Facts: Nadia bought 3,000,000 shares **at original issuance** for $12,000 on Feb 18, 2020; Helio Grid represented gross assets ≤ $1,000,000 and qualified-trade C-corp status at issuance; the stock has been held > 5 years (five-year mark: Feb 18, 2025).

Today, the stock is textbook QSBS for Nadia:
- §1202(c): stock of a C corporation originally issued after Aug 10, 1993, acquired at original issue — satisfied by the purchase-agreement representation (`library/irc_1202_excerpt.md`).
- §1202(a): 100% exclusion for stock acquired after Sept 27, 2010 held more than 5 years (ibid.).
- Per-issuer cap: greater of **$10,000,000** (pre-July 4, 2025 issuance) or 10× basis ($120,000) → cap = $10,000,000 (ibid.).

Current numbers (`numbers.json`):
| Item | Amount |
|---|---:|
| Basis (3,000,000 × $0.004) | $12,000 |
| 409A value of her 30% (approximate) | $9,400,000 |
| Potential gain | **$9,388,000** |
| Cap | $10,000,000 (greater of $10M vs 10 × $12,000 = $120,000) |
| Excludable today | **$9,388,000** |

If she contributes the stock to the 99/1 holding partnership:
- §1202(g) would be the partner-side gate for gain flowing out of a partnership-held QSBS — but it is moot here, because
- §1202(h)(2): **a contribution of stock to a partnership is not among the listed transfers that preserve treatment; the partnership did not acquire the stock at original issue, and the stock ceases to qualify in its hands** (`library/irc_1202_excerpt.md`). The exception in §1202(h) for distributions from a partnership to a partner (treated as acquired as the transferor, holding period tacked) only helps if the stock comes back out — and even that path is fragile, because a pre-planned contribute-then-distribute-then-sell sequence is exactly the kind of interdependent, single-purpose series that courts collapse into its substance (*Commissioner v. Court Holding Co.*, 324 U.S. 331 (1945); *Gregory v. Helvering*, 293 U.S. 465 (1935) — `library/step_transaction.md`).

**Verdict: DO NOT contribute the Helio Grid stock.** On the advisor's headline benefit — "when Helio exits, the gain lands in the holding so you can reinvest without tax" — there is no library authority for tax-deferred compounding inside a partnership; what the library shows is the opposite: income flows through to the owners and is exposed to their state filings (`state_nexus_summary.md`), and partnership-held QSBS gain flows to partners under §1202(g) only if the strict holding conditions are met (`irc_1202_excerpt.md`). The claim is **unsupported by the library** and is rejected.

#### 2(b) Properties LLC — §752(b) triggered gain

Facts: Properties has a $1.9M nonrecourse mortgage and **negative tax capital of $(380,000)**, depleted by depreciation and the 2024 distribution of $1.2M refinancing proceeds.

Consequence under the library's rule: contributing an interest whose liabilities exceed basis triggers gain under §752(b)/§731(a) to the extent liabilities shifted to other partners exceed the contributor's basis; with a 99/1 partnership, 1% of the mortgage shifts to the other partner (`library/irc_721_and_752.md`).

Arithmetic:
| Line | Amount |
|---|---:|
| Mortgage | $1,900,000 |
| Portion shifted to the other (1%) member: 1% × $1,900,000 | **$19,000 estimated gain** |

Because her tax capital is negative, there is no capital cushion to absorb the deemed distribution, so the shifted amount is taxable. **This reconciles only under the library's tax-capital framing**, and I will not force it to balance: a pure net-asset view of the same balance sheet (buildings $3.4M − acc. dep. $1.12M + land $0.6M + due-from-Services $0.4M − mortgage $1.9M = net basis $1,380,000) would suggest no gain, because detailed §752/§704(c) liability-sharing and basis-floor mechanics are **not in the library — unverified**. I report the conservative estimate **$19,000** per the library's explicit consequence and flag the open reconciliation.

Note also: the $1.2M refinancing proceeds distributed in 2024 are history — contributing Properties now does not and cannot "wash" that prior distribution; the negative capital simply carries into Holdings.

**Verdict: DO, accepting ≈ $19,000 of triggered gain (modest relative to the structure benefits), OR defer contributing Properties** until capital is rebuilt (e.g., retained earnings) or the mortgage amortizes below her capital contribution. If deferring, Properties simply stays out of Holdings until then.

#### 2(c) Services and Digital

Contribution of profitable Services and loss-making Digital is squarely §721(a) nonrecognition territory under the library's rule, and the library raises no impediment. **DO.**

### Step 3 — Interest-free intercompany loans; "one bank account, one set of books"

**Consequence.** Interest-free or below-market loans between related entities are recharacterized under §7872: the lender is treated as receiving imputed interest at the AFR and the borrower as paying it; between commonly owned entities, the deemed interest is offset by corresponding deemed distributions/contributions (`library/irc_7872_afr.md`). Separately, the library warns that loans without notes, interest, or repayment terms are evidence of commingling that undermines separate-entity liability protection — veil piercing (ibid.).

The existing loans are already in this posture (`intercompany_cash_flows.csv`: no documentation on the Properties → Services advances; email only for Services → Digital), and the client confirms it was by design: "No paperwork. I just move money where it's needed." That corroborates the demand/no-stated-terms character, and it makes the remediation urgent — the advisor's Step 3 would have made this commingling structural rather than incidental. Annual imputed interest under §7872 (`numbers.json` for arithmetic; **assumption:** no stated terms — the client confirms none ever existed — so demand-character treatment and the short-term AFR 3.96% apply; the library does not state the demand-loan rate-selection rule — **unverified**; mid-term 4.12% and long-term 4.58% shown below for reference):

| Loan | Principal | Annual imputed interest @ 3.96% (short-term) | @ 4.12% (mid-term) | @ 4.58% (long-term) |
|---|---:|---:|---:|---:|
| Properties → Services | $400,000 | **$15,840** | $16,480 | $18,320 |
| Services → Digital | $150,000 | **$5,940** | $6,180 | $6,870 |
| **Total, both loans** | | **$21,780** | $22,660 | $25,190 |

Because the entities are commonly owned and disregarded, the deemed interest generally nets to zero across the family — **but it must be recorded**, and the *real* cost is the one in the veil-piercing sentence: "one bank account, one set of books" would dissolve the liability separation that is the advisor's own headline benefit. Properties holds the family's real estate against a $1.9M mortgage and Services employs 42 people; their creditors must continue to meet *those* entities' separate books, not Nadia's.

**Verdict: REJECT as proposed ("interest-free," commingled banking/books); SUBSTITUTE documented loans with AFR interest and separate books/accounts. Remediation of the outstanding loans is required — see below.**

### Step 4 — "One return"; "no tax event — it's all a §721 contribution"

- **No tax event?** Only partially. §721(a) covers the Services/Digital contributions; the Properties contribution carries ≈ $19,000 of §752(b)/§731(a) triggered gain (`irc_721_and_752.md`); and the Helio Grid contribution would be a multi-million-dollar *economic* tax event even if it involves no current recognition — destruction of $9,388,000 of §1202 exclusion (`irc_1202_excerpt.md`). Calling the whole plan "no tax event" understates both.
- **One return?** Not at the state level: the Wyoming holding has Colorado commercial-domicile nexus and must file in Colorado, and Colorado income flowing through must still be filed there (`state_nexus_summary.md`). Wyoming adds an annual report. The library contains no authority that a single-entity wrapper reduces her aggregate filing burden; treat the claim as unverified at best.
- **Step-transaction alert.** If the real sequence is "contribute everything, then sell Helio from the holding," the series is interdependent and aimable at a single end and may be collapsed (*Court Holding Co.*; *Gregory* — `library/step_transaction.md`). Add the QSBS bite from §1202(h)(2) and the "deferral" benefit evaporates in both directions.

**Verdict: REJECT as stated.**

---

## Revised plan (recommended)

1. **Form Oakline Holdings LLC** taxed as a partnership. (State per her preference; do not rely on Wyoming for tax savings — Colorado filings follow the income regardless: `state_nexus_summary.md`.) From day one: separate bank accounts, separate books, no commingling (`irc_7872_afr.md`, veil-piercing note).
2. **Contribute Oakline Services LLC and Oakline Digital LLC** to Holdings under §721(a) (`irc_721_and_752.md`).
3. **Contribute Oakline Properties LLC** only with advised consent to the ≈ **$19,000** triggered gain (§752(b)/§731(a): 1% × $1,900,000), or defer until capital is positive (`irc_721_and_752.md`). Her choice; both are defensible. Recommendation: proceed with contribution if the estate objective is near-term, since $19,000 is modest, **or** rebuild capital first if she prefers no recognition.
4. **Do NOT contribute the Helio Grid Inc stock.** It stays directly titled to Nadia, outside Holdings (and outside any partnership). See the detailed guidance below.
5. **Fund the 99/1 split** for the revocable trust only after the mechanism (gift vs. contribution) is confirmed with estate counsel and the trust's tax status is settled — no authority for these points is in the library (unverified).
6. **Remediate the intercompany loans** (below), and thereafter run Holdings with documented, AFR-interest notes only (`irc_7872_afr.md`).
7. **File where required:** Colorado for the holding's pass-through income (commercial domicile) plus the Wyoming annual report; do not count on "one return" (`state_nexus_summary.md`).
8. **Sequencing rule (now operative — client expects a Helio sale in 12–18 months):** complete the restructuring of the operating businesses (steps 1–3, 5–7) on its own timeline while the Helio stock stays out of Holdings entirely; the exit then closes at Nadia's level, outside the structure, with proceeds paid directly to her. Never interleave — and never pre-plan — any step aimed at the sale alongside it (*step_transaction.md*); revisit Holdings-related planning for the proceeds only after closing, once the exclusion is banked.

## What to do — and not do — with the Helio Grid stock

**DO:**
- **With a sale realistic in 12–18 months (client), treat share hygiene as a closing condition.** The shares stay titled to Nadia, outside Holdings and outside any partnership, through signing and closing — no new paperwork, no pledges, no interim moves. The sale then occurs at her level directly, with nothing interposed for the substance-over-form doctrine to recharacter (`step_transaction.md`).
- Keep the shares titled to Nadia personally. No contribution to Holdings or any partnership while the QSBS exclusion matters (`irc_1202_excerpt.md`, §1202(h)(2) consequence).
- Keep the substantiation file intact: the SPA excerpt showing original issuance, the ≤ $1M gross-assets and qualified-business representations (§1202(c)), the 2020 §83(b) filing, and acquisition date Feb 18, 2020 (five-year mark met Feb 18, 2025; 100% tier per §1202(a)).
- Before any sale, re-verify: (i) holding period, (ii) the per-issuer cap room — at the client's $9–10M exit range, gain of $8,988,000–$9,988,000 stays under the $10,000,000 cap at both ends — and (iii) the eligibility tests, which the library shows as of issuance/holding conditions (`irc_1202_excerpt.md`). **Caution (unverified scope):** the library's §1202 excerpt covers only (a), (c), (g), (h); any additional eligibility conditions that could apply at sale are not in the library — unverified — and must be confirmed before relying on the exclusion at closing.
- If she insists on contributing later, understand the only library-recognized preserve path is **distribution from the partnership back out** (treated as acquired as the transferor, holding period tacked) — and that any pre-planned contribute-then-distribute-then-sell sequence risks being collapsed (*Court Holding Co.*; *Gregory* — `step_transaction.md`). This is fragile; do it only with specialist tax counsel, or simply wait and contribute after her gain is realized.
- After a full §1202-excluded disposition there is no benefit left to lose — contribution of any remaining interest to Holdings would then be harmless *as to §1202*.

**DO NOT:**
- Do not contribute, pledge, or otherwise place the shares inside Holdings (or any partnership) before the exclusion is banked (`irc_1202_excerpt.md`).
- Do not run the "one set of books" regime over the shares: Holdings must never hold itself out as owner of, or lend against, Nadia's Helio Grid stock.
- Do not rely on the advisor's "reinvest without tax" claim — unsupported by the library (see Step 4 analysis).

## Intercompany-loan remediation

Current exposures (`intercompany_cash_flows.csv`): Properties → Services $400,000 (two advances, no documentation), Services → Digital $150,000 (email only). Required:

1. **Execute dated promissory notes** for both loans (Ratification/consolidated note for Properties → Services covering the two advances; note for Services → Digital): principal, interest at AFR (recommend stating the applicable rate; if documented as demand, the library's short-term rate 3.96% applies on the assumption stated above — **unverified**: the library does not state the demand-loan selection rule), maturity/repayment schedule, subordination limits, and cure language.
2. **Accrue catch-up interest** from each advance date through the note date. Indicative amounts through 2026-10-25 at 3.96% simple, actual/365 (**assumption**: closing date; method; rate class as above):
   | Advance | Principal | From | Days to 2026-10-25 | Catch-up interest |
   |---|---:|---|---:|---:|
   | Properties → Services (A) | $250,000 | 2024-03-01 | 968 | $26,255.34 |
   | Properties → Services (B) | $150,000 | 2025-06-15 | 497 | $8,088.16 |
   | Services → Digital | $150,000 | 2025-09-01 | 419 | $6,818.79 |
   | **Total** | | | | **$41,162.30** |
   Total sums the unrounded accruals; the displayed (rounded) components add to $41,162.29 — a 1¢ rounding artifact, noted rather than forced.
   These amounts are booked as deemed interest income to the lender-side owner and deemed interest expense on the borrower side, offset by corresponding deemed distributions/contributions between the commonly owned entities (`irc_7872_afr.md`); actual dollars move only if the notes are paid down.
3. **Going forward:** no new undocumented advances; interest at not less than the AFR accrues and is actually paid (or formally capitalized per the notes) annually; both loans appear on a quarterly intercompany schedule; separate bank accounts per entity (`irc_7872_afr.md`).
4. **If any loan is instead forgiven**, §7872's deemed-interest and deemed distribution/contribution mechanics still apply first (`irc_7872_afr.md`); the basis/capital-account mechanics of forgiveness are **not in the library — unverified** — obtain specific advice before forgiving anything.

## Numbers summary

All arithmetic is in `numbers.json`. Headlines: QSBS exclusion at risk if contributed **$9,388,000** (409A-centered; **$8,988,000–$9,988,000** across the client's $9–10M exit range, still fully under the $10,000,000 cap at both ends); Properties contribution gain estimate **$19,000**; annual imputed interest **$15,840** (Properties → Services) and **$5,940** (Services → Digital) at the assumed short-term AFR; catch-up interest through 2026-10-25 **$41,162.30**.

## Assumptions, open items, and explicitly unverified points

- **Assumptions used in the numbers:** short-term AFR (3.96%) for both loans because no terms are documented (demand-letter character assumed); simple interest, actual/365; 409A value $9.4M is approximate; remediation date 2026-10-25; the Properties gain uses the library's 1% mortgage-shift rule against negative tax capital.
- **Unverified (raised above):** demand/term-loan AFR-selection rule; gift/grantor-trust mechanics for the 1% interest; partnership-level tax deferral ("reinvest without tax") claim; §752/§704(c) liability-sharing and basis-floor detail behind the Properties reconciliation; renewable/reforgiveness basis mechanics. None of these appears in `library/INDEX.md`, and each is labeled as such where used.
- **Remaining unknowns (client confirmed no further information, 2026-10-25):** Helio share transfer restrictions; Properties mortgage due-on-transfer covenant; the trust's funding mechanism and tax classification (no gift-tax/grantor-trust authority in the library — unverified); sale-time §1202 conditions beyond the library's (a)/(c)/(g)/(h) excerpt. All are logged in `QUESTIONS.md` and `STATUS.md`.

---

## Addendum — client responses incorporated (2026-10-25)

| Client statement | Effect on the analysis |
|---|---|
| "Helio is talking to acquirers; a sale in 12–18 months is realistic. My stake would be about $9–10M." | The sequencing rule (revised plan step 8) becomes operative: the restructuring proceeds for the operating businesses only, and the Helio stock stays outside Holdings through signing and closing, so the sale happens at her level with nothing interposed (*step_transaction.md*). Gain at exit: $8,988,000–$9,988,000 ($9–10M less the $12,000 basis) — under the $10,000,000 cap at both ends; `qsbs_exclusion_at_risk` scales with actual proceeds (base case $9,388,000 at the ≈$9.4M 409A). The core recommendations are unchanged — the exit horizon only makes them more time-sensitive. |
| "The 1% is my revocable living trust — the advisor said we need two partners." | Identifies the second member but not the funding mechanism or the trust's tax classification — both outside the library (**unverified**; estate counsel required). The §752(b) analysis is unchanged: it is the *existence* of the 1% member that produces the ≈ $19,000 item on the Properties contribution. One related benefit of keeping the stock out: with nothing Helio-related in the partnership, the §1202(g) partner-identity rules (share of a partner acquired/sold around a QSBS-holding partnership) never come into play at all. |
| "No paperwork. I just move money where it's needed." | Confirms the advances were never documented: demand character and the short-term AFR (3.96%) assumption stand (the demand-loan rate-selection rule itself is outside the library — **unverified**). Remediation is unchanged and more urgent: consolidated ratification notes, catch-up deemed interest ($41,162.30 through 2026-10-25), and a written loan policy that ends ad-hoc money movement once Holdings exists — Step 3's "one bank account" regime would have institutionalized exactly this habit. |
| "For questions not answered above, the client has no additional information." | Unresolved points are flagged as explicit unknowns rather than re-asked: share-transfer restrictions, mortgage due-on-transfer covenant, trust mechanics/tax status, sale-time QSBS conditions beyond the excerpt. See `QUESTIONS.md` (resolved/unresolved ledger) and `STATUS.md`. |

*Sequence-planning notes:* expect closing roughly November 2027–April 2028 given the 12–18 month horizon; recompute the loan catch-up interest through the actual note-signing date; do not fund the trust's 1% until its mechanism and tax classification are confirmed by estate counsel.

---

## Addendum 2 — client follow-up: "the gain lands in the LLC" (2026-10-25)

**Question put:** "The advisor specifically said the holding is how I avoid tax when Helio sells — 'the gain lands in the LLC.' Who's right, and can the holding at least own it after the sale?"

**Short answer.** On this point the advisor is wrong, and the error is not a nicety: the proposed mechanism converts a fully excludable gain into a fully taxable one. As for "after the sale" — there is no stock left to own; the issuer is acquired at closing and what she holds is cash. The proceeds can go into Holdings once the exclusion is banked, and doing so is harmless. The stock itself must never go in — before the sale or at any other time.

**Why "the gain lands in the LLC" fails (library-based).**

1. **Original-issuance requirement (§1202(c)(1)).** The exclusion belongs to a taxpayer who acquired the stock **at its original issue** from the issuer. Nadia did — February 18, 2020, $12,000. A partnership that receives contributed stock did not acquire it at original issue, and §1202(h) does not list contribution among the transfers that preserve treatment (gift, death, distributions *out of* a partnership to a partner): the stock **ceases to qualify in the partnership's hands** (`irc_1202_excerpt.md`). From the moment the stock enters Holdings there is no QSBS in the structure, so nothing "lands" intact.
2. **The pass-through gate is never reached (§1202(g)).** §1202(g) is the legitimate partnership rule the advisor is gesturing at, and it cannot save the structure because the stock that would flow through stopped qualifying at the contribution. Even on its own terms, (g) requires the partner to have held its partnership interest **when the partnership acquired the stock and at all times thereafter** — a posture a structure assembled by a 2026 contribution for a 2027–28 sale does not present, and the trust's 1% interest (created at the same closing as the contribution) could not straightforwardly show it either.
3. **There is no deferral pool in a partnership.** Whatever the character of the gain, partnership income flows through to the owners annually and is taxed at their level, with Colorado filing exposure for income flowing through (`state_nexus_summary.md`). The gain does not sit inside the LLC awaiting a tax-preferred exit — this restates the "reinvest without tax" claim rejected at Step 4.
4. **The step doctrine offers no rescue (`step_transaction.md`).** A pre-planned contribute → sell → distribute series is a collapse candidate (*Court Holding Co.*; *Gregory*). If the steps are collapsed, the result is the direct personal sale she could have done all along, with no paperwork and no structure cost — all the risk of the intermediate form and none of the promised benefit. If they are *not* collapsed, the exclusion is already destroyed at the partnership level. Either way the advisor's structure has no upside.

**Both paths, side by side** (figures from `numbers.json`; proceeds at the client's stated $9–10M range):

| | Sell personally (recommended) | Contribute now; sell inside Holdings 12–18 months later (advisor) |
|---|---|---|
| Proceeds | $9,000,000 – $10,000,000 | same |
| Basis | $12,000 | same |
| Gain | $8,988,000 – $9,988,000 | same |
| Stock qualifies in the holder's hands? (§1202(c)) | Yes — original issue | No — contribution; "ceases to qualify in its hands" (§1202(h)) |
| Excludable under §1202(a) (100% tier) | Full gain — within the $10,000,000 per-issuer cap at both ends — subject to the flagged sale-time conditions (**unverified** beyond the excerpt) | **$0** |
| Where tax lands | Excluded | Passes through and is taxed at her level (with 1% to the trust member), with state filings (`state_nexus_summary.md`) |
| Step-transaction posture | Nothing interposed | Collapse candidate; either outcome defeats the promised benefit |

**The delta is the entire exclusion: $8,988,000–$9,988,000.**

**Where the advisor's idea has a legitimate — much narrower — home.** §1202(g) really does let gain on QSBS flow through a partnership with the exclusion intact, but only when the **partnership itself acquired the stock at its original issue** and the **partner held its partnership interest when the partnership acquired the stock and at all times thereafter** (`irc_1202_excerpt.md`). That describes a vehicle that buys new-issue QSBS directly, from day one, with its membership already in place — not a vehicle that receives a member's existing personal position by contribution. The advisor's plan has the sequence backwards in time. Whether additional conditions beyond the library's excerpt apply to such a buy-at-issue vehicle is **unverified** and must be confirmed against the full statute before anyone relies on the pattern — and for Helio Grid specifically it is irrelevant, since after closing there is no stock and the exclusion will already have been banked at her level.

**"Can the holding at least own it after the sale?"**

- **The proceeds — yes.** Contributing cash to Holdings after closing is a nonrecognition contribution under §721(a) (`irc_721_and_752.md`), and it cannot damage §1202 because there is no longer any QSBS in play. Post-closing, fund Holdings with the proceeds if she wants pooled management.
- **Set expectations:** post-sale, Holdings is a normal investment vehicle, not a tax-avoidance device. Income it earns flows through to her annually, with Colorado filing exposure (`state_nexus_summary.md`). What becomes true at closing is "contribute without a tax event" (§721(a)) — never "reinvest without tax."
- **A future venture's stock:** the same rules run forward. A vehicle that wants §1202(g) pass-through must buy new-issue QSBS with all members' interests in place from acquisition (subject to the **unverified** full-statute check); personally held founder stock in a future company should likewise stay outside Holdings until its own exclusion is banked.
- **For Helio Grid itself, "after the sale" is moot:** at closing the stock ceases to exist as stock.

*No other deliverable changes on account of this addendum; every figure and recommendation in the main opinion and Addendum 1 stands.*
