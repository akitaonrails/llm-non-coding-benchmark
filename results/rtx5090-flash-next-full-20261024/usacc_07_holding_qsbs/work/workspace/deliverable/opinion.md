# Opinion — Proposed Oakline Holdings Restructuring (Nadia Oakline)

**Prepared:** 2026-10-26 · **Scope:** per `CONTRACT.md`. The only legal authorities relied on are the five items in `library/INDEX.md`. Any statement of law outside that library is expressly labeled **[unverified — not in library]**. No tax rate is applied to excluded/recognized gain because no rate authority is in the library; tax cost = (amount recognized) × (rate that applies).

---

## Executive summary

| Proposed step | Verdict |
|---|---|
| 1. Form Oakline Holdings LLC (WY; Nadia 99% / revocable trust 1%) | Acceptable **if modified**; the 1% trust partner must be examined, and Wyoming saves no income tax |
| 2. Contribute Services, Properties, Digital **and 30% of Helio Grid** to Holdings | **Contribution of Services/Properties/Digital: do, deferrable under §721(a)** (with liability mechanics checked). **Contribution of the Helio stock: DO NOT DO IT — it destroys a §1202 QSBS exclusion of approximately $9,388,000** |
| 3. Holdings makes interest-free loans among subsidiaries ("one bank account, one set of books") | **Do not do.** §7872 recharacterizes: ~$21,780/yr of imputed interest on the existing pattern, and the "one account, one set of books" posture is evidence of commingling that undermines the very liability protection being bought |
| 4. "Holdings files one return. No tax event — it's all a §721 contribution" | **Wrong as stated.** §721(a) defers *contribution* gain only; §752(b)/§731(a) must be tested (computed below: $0 gain, but only because outside basis happens to exceed the deemed distribution), and Colorado filings continue regardless of the Wyoming formation |

The advisor's single claimed benefit that actually works — "when Helio exits, the gain lands in the holding so you can reinvest without tax" — is **backwards**: contributing the Helio stock is precisely what forfeits the ~$9.4M tax-free exit. A *personal* holding of the stock keeps it tax-free under §1202.

---

## Facts relied on (from `documents/`)

- The advisor's proposal (`advisor_proposal.pdf`): **Summit Peak Wealth Advisors**, dated **2026-02-11**, who state on its face "(not a law or CPA firm)".
- Helio Grid Inc: Delaware **C corporation**; Nadia holds 30% founder common, bought **at original issuance** Feb 18 2020, 3,000,000 shares at $0.004 = **$12,000**; company represented gross assets **≤ $1,000,000** at issuance and that it is a domestic C corporation in an active qualified trade or business (SPA §2.3); 83(b) election filed Mar 2 2020. Current 409A value of her stake ≈ **$9.4M**.
- Oakline Services LLC (CO, SMLLC, ~$1.1M/yr profit), Oakline Properties LLC (CO, SMLLC; **$1.9M nonrecourse mortgage refinanced 2024**; owner's **tax capital $(380,000)**; $1.2M refi proceeds distributed to Nadia in 2024), Oakline Digital LLC (CO, SMLLC, losses).
- Intercompany advances, **no notes, no interest**: Properties → Services $250,000 (3/1/2024) + $150,000 (6/15/2025) = $400,000; Services → Digital $150,000 (9/1/2025, "email only").
- Properties balance-sheet line items do **not** foot to stated capital: assets $3,280,000 − mortgage $1,900,000 implies capital **+$1,380,000**, but stated capital is **$(380,000)** — an unreconciled **$1,760,000** difference. I do not force this to balance; see Open Items and QUESTIONS.md. I use the *stated* capital of $(380,000) as authoritative for the §752/§731 test.

---

## Step-by-step analysis

### Step 1 — Form Oakline Holdings LLC (Wyoming; Nadia 99%, her revocable trust 1%)

- **Consequence.** Wyoming has no income tax but requires an annual report; because Holdings is managed from Colorado it has Colorado nexus (commercial domicile) and files there, and holding membership interests in LLCs doing business in Colorado does not avoid Colorado filing for income flowing through — so the formation buys no income-tax savings. *(library: `state_nexus_summary.md`.)*
- **The 1% "partner" is her own revocable trust.** If a revocable trust is disregarded as an owner separate from its grantor, there may be only one owner for tax purposes and the partnership status itself — and the "one return" claim — is in question. **[unverified — grantor-trust rules are not in the library; flag to counsel before adopting the 99/1 split.]** The §752 computation below conservatively treats the trust as a real 1% partner.
- **Verdict: do, with modifications** — confirm the trust's tax status and the CO filing obligations; budget for WY annual report. The liability-protection benefit is real *only* if separateness is maintained (see Step 3).

### Step 2 — Contribute all four assets to Holdings

**(a) Services, Digital (clean).** No gain or loss on contribution of property for a partnership interest. *(§721(a) — `irc_721_and_752.md`.)* No liabilities attach to Services; Digital carries losses. Defer, carry over basis **[carryover basis is the standard corollary; not explicit in the library excerpt — treat as expected but verify]**. **Verdict: do.**

**(b) Properties — the §752(b)/§731(a) test the advisor skipped.**
- Pre-contribution: Nadia bears 100% of the $1,900,000 nonrecourse mortgage (§752). After contribution to a 99/1 partnership, **1% of the mortgage shifts to the other partner: $1,900,000 × 1% = $19,000**, treated as a distribution of money to her under §752(b). *(Mechanics spelled out in the library's own consequence note — `irc_721_and_752.md`.)*
- §731(a): gain only to the extent the deemed money distribution exceeds her basis in the partnership interest. Her basis at minimum equals the basis of the contributed Properties assets, implied by the stated capital: capital $(380,000) + liabilities $1,900,000 = **$1,520,000**. $19,000 deemed distribution < $1,520,000 basis → **gain at contribution ≈ $0**.
- Why the result is $0 is not why the advisor said $0: the contribution escapes tax only because her outside basis happens to clear the deemed distribution. The entity has **negative tax capital $(380,000)** — a standing trap. Any later reduction in her share of liabilities (paydown, refi change, allocation shift, redemption of the 1% partner) or any money distribution from Holdings is a §752(b)/§731(a) event and can produce real gain while capital is negative. *(Both citations: `irc_721_and_752.md`.)*
- **Verdict: do — after reconciling the $(1,760,000) balance-sheet discrepancy** (Open Items), with Holdings' distribution policy constrained so negative capital cannot be exacerbated.
- Note: if the revocable trust is disregarded (see Step 1), the shift is $0 and the deemed distribution disappears — same $0 answer, opposite mechanism.

**(c) The 30% of Helio Grid Inc — DO NOT CONTRIBUTE. This is the single most consequential item in the engagement.**
- Her stock is qualified small business stock on the documents' face: domestic **C corporation**, **originally issued** after Aug 10 1993, corporation was a **qualified small business at issuance** (gross assets ≤ $1M per SPA §2.3), acquired **at original issue** (directly, per SPA) **in exchange for money** ($12,000). *(§1202(c)(1) — `irc_1202_excerpt.md`.)* Acquired after Sept 27 2010 and held > 5 years → **100% exclusion** (holding period: 5.98 years as of the proposal date 2026-02-11; ≈6.7 years as of this memo 2026-10-26 — 2,185 / 2,442 days since 2/18/2020). *(§1202(a).)*
- Gain if sold today: $9,400,000 − $12,000 = **$9,388,000**. Per-issuer cap: greater of $10,000,000 or 10× basis ($120,000) → $10,000,000 > $9,388,000 → **the entire gain would be excluded** if she holds it personally.
- **Contributing it to Holdings destroys this.** The library is explicit: §1202(h) lists gift, death, and partnership *distributions to* a partner as transfers that preserve the prior treatment; **"a contribution of stock to a partnership is not among the listed transfers"; the partnership did not acquire the stock at original issue, and the stock ceases to qualify in its hands.** *(§1202(h) and editorial note — `irc_1202_excerpt.md`.)* §1202(g)'s partner flow-through only helps a partner when the **partnership itself acquired qualifying stock**; it cannot resurrect stock the partnership never qualified on.
- Quantified: **$9,388,000 of currently-excludable gain is at risk** — up to that amount becomes fully taxable gain at whatever rate applies (no rate authority in the library). That is the direct cost of the advisor's Step 2, before counting the $0 deferral myth (below).
- **Verdict: carve the Helio shares out of the contribution entirely.** Keep them titled personally (or in her own name; see "Do / Don't" section).

### Step 3 — Holdings makes interest-free loans among subsidiaries; "one bank account, one set of books"

- **Consequence 1 — §7872 recharacterization.** Interest-free or below-market loans between related entities are recharacterized: the lender is treated as receiving, and the borrower as paying, imputed interest at the AFR, with a corresponding distribution/contribution between commonly owned entities. *(§7872 — `irc_7872_afr.md`.)* The library's AFR for this engagement: short-term (≤3 yr) **3.96%**; mid-term **4.12%**; long-term 4.58%.
- Which AFR: the advances have **no notes and no repayment terms**, so they behave as demand obligations; applying the library table, the **short-term 3.96%** rate is the natural fit **[rate-selection convention for demand loans is not spelled out in the excerpt — labeled application of the table, verify]**. The excerpt also does not state a compounding convention; I compute simple annual **[semiannual compounding under the full statute would raise the figures slightly — not in library excerpt, unverified]**.
- **Arithmetic (shown):**
  - Properties → Services $250,000: 250,000 × 3.96% = **$9,900/yr**
  - Properties → Services $150,000: 150,000 × 3.96% = **$5,940/yr**
  - Services → Digital $150,000: 150,000 × 3.96% = **$5,940/yr**
  - Aggregate run-rate: $400,000 × 3.96% = **$15,840/yr** (Properties→Services) + **$5,940/yr** (Services→Digital) = **$21,780/yr**
  - Cumulative to 2026-10-26 (simple interest, days/365): $250,000 × 3.96% × 969/365 = $26,282; $150,000 × 3.96% × 498/365 = $8,104; $150,000 × 3.96% × 420/365 = $6,835 → **≈ $41,222 already accrued**.
  - The wash question: between commonly owned entities the deemed interest income and deduction can offset for a single owner, **but** Digital is loss-making (its deduction is added to losses, of unknown usability **[basis-at-risk/passive limits not in library — unverified]**), and each year the pattern continues, the accrued imputed income grows.
- **Consequence 2 — veil piercing.** The library states flatly: loans without notes, interest or repayment terms are **evidence of commingling that undermines separate-entity liability protection (veil piercing)** *(§7872 note — `irc_7872_afr.md`)*. "One bank account, one set of books" is worse than interest-free lending: it is the *elimination of separateness*, and its concrete cost here is that a tort or contract creditor of the 42-employee HVAC business (Services) could reach the real estate held in Properties — buildings and land carried at **$2,880,000 tax basis**, subject to the $1,900,000 mortgage (≈$980,000 book equity). The plan's flagship liability-protection benefit is destroyed by its own Step 3.
- **Verdict: do not implement Step 3 in any form.** Remediation of the *existing* advances is in its own section below.

### Step 4 — "Holdings files one return. No tax event — it's all a §721 contribution"

- §721(a) defers gain/loss **on the contribution step only**. It is not a deferral of exit gain, and the library contains **no authority for tax-free reinvestment at the partnership level** — the claimed benefit "when Helio exits, the gain lands in the holding so you can reinvest without tax" is unsupported by anything in the library, and for the Helio stock it is doubly wrong because the contribution itself breaks §1202 (Step 2(c)).
- "No tax event" skipped the required §752(b)/§731(a) test (Step 2(b): deemed distribution $19,000; $0 gain by basis, not by §721).
- One-return simplicity is overstated: Holdings will have a **Colorado filing obligation** (commercial domicile) plus the Wyoming annual report, and it does **not** avoid Colorado filing on income flowing through the subsidiary LLCs. *(`state_nexus_summary.md`.)* Federal return mechanics (e.g., an informational partnership return with pass-through to her own return) are outside the library **[unverified]**, but the claimed *state* simplification is affirmatively contradicted by the nexus summary.
- Watch the step-transaction/substance-over-form doctrine: a series of interdependent, pre-planned steps is collapsed into one transaction and tax follows **substance** — so e.g. contributing Helio stock to Holdings and then selling, or any "distribution then sale" choreography tied to this plan, will be read as what actually happened. *(`step_transaction.md`.)* This doctrine is a risk *against* clever Helio re-plumbing, not a tool for it.
- **Verdict: the §721 characterization of Steps 1–2 (ex-Helio) is correct but incomplete; the "one return / no tax event / tax-free reinvestment" framing is wrong and should not be relied on.**

---

## The Helio Grid stock — do and do not

**Do:**
1. **Keep the stock personally, untouched by this restructuring.** No contribution to Holdings or any other LLC/partnership — contribution is outside §1202(h)'s list and ends qualification in the entity's hands. *(§1202(h), (c)(1) — `irc_1202_excerpt.md`.)*
2. **Preserve the §1202 record now:** SPA with the ≤$1M gross-assets representation, proof of $12,000 payment at original issuance, 83(b) filing, share ledger. These are exactly the facts §1202(c)(1) turns on.
3. **Gifts and estate transfers of the Helio stock are QSBS-safe**: stock acquired by gift or at death is treated as acquired in the same manner as the transferor, with a tacked holding period. So estate-planning transfers of these shares by completed **gift** (to individuals or an irrevocable trust) or **at death** do not break §1202 — the *contribution* does. *(§1202(h).)* Note: a transfer to her **own revocable trust** is not the gift route — such a trust is likely disregarded, so moving the shares into it is probably a federal no-op that neither helps nor harms §1202 **[unverified — grantor-trust/disregarded-entity rules not in the library]**. Whether a donee gets a fresh per-issuer cap is governed by Treas. Reg. §1.1202-2 (referenced but not reproduced in the library) — **[unverified; confirm before gifting for cap-stacking.]**
4. Confirm the 5-year clock: >5 years already ran since 2/18/2020 (5.98 yrs as of the 2026-02-11 proposal; ≈6.7 yrs as of 2026-10-26), and 100% applies to stock acquired after 9/27/2010. *(§1202(a).)*
5. **For future** small-company stock she wants inside Holdings: that is workable — if a partnership **itself** acquires QSBS at original issue, partners who held the partnership interest when the stock was acquired and at all times after take the gain flow-through. *(§1202(g).)* New issuances after July 4 2025 get the higher cap ($15M) and tiered 50/75/100% at 3/4/5 years. *(§1202(a).)* Holdings is a fine vehicle for *new* QSBS; it is a poison vehicle for *this* QSBS.

**Do not:**
- Do not contribute the Helio shares to Holdings (or any LLC taxed as a partnership) — the $9,388,000 exclusion dies in the entity.
- Do not "swap" the shares into Holdings "and rely on §1202(g)": (g) only flows through stock the partnership validly acquired; a partnership is not an original-issue acquirer.
- Do not choreograph a distribution of the shares out of Holdings, or a contribution-then-sale, to chase the "reinvest without tax" claim: interdependent pre-planned steps collapse *(step-transaction doctrine, `step_transaction.md`)* and the contribution break is fatal before any choreography is even reached.
- Do not let the 409A stake drift into any "one bank account" arrangement or entity-level financing of Helio-related assets.
- Do not assume the exclusion survives any corporate action at Helio (redemption, merger/reorg of her shares) without advice **[the library excerpt does not address reorganizations/redemptions beyond what §1202(h)/(c) list — unverified]** — verify before any Helio exit term sheet binds.

**Timing note:** the exclusion does not improve by moving the stock — it is already fully vested (100%, under cap). The only winning move is non-action on this asset.

---

## Intercompany-loan remediation (needed now, independent of the restructuring)

1. **Identify what the advances are and fix the paper — pick one treatment per advance, documented:**
   - **Option A — bona fide debt:** execute a real promissory note per advance: stated principal, **interest at ≥ AFR** (short-term 3.96% for ≤3-yr terms, or mid-term 4.12% if a 3–9 yr term is chosen), scheduled payments, maturity, default terms; actually pay interest going forward. *(Rate table: §7872 — `irc_7872_afr.md`.)*
   - **Option B — capital:** recharacterize as capital contributions (Properties → Services $400,000; Services → Digital $150,000), documented by written contribution agreements and capital-account entries; the loans vanish and §7872 stops accruing on them. Watch the interaction with Properties' **negative capital**: contributing *out of* Properties reduces its equity further.
   - **Option C — repay:** Services repays $400,000 to Properties; Digital repays $150,000 — affordable given Services' ~$1.1M/yr profitability.
   - Whichever is chosen, the current "no note, no interest, email only" state is the worst option: it is simultaneously §7872 recharacterization exposure and veil-piercing evidence. *(both: `irc_7872_afr.md`.)*
2. **Catch-up for the past:** the imputed-interest recharacterization applies while the loans were outstanding — ≈ **$41,222 accrued through 2026-10-26** (arithmetic above), $21,780/yr run-rate. Between commonly owned entities the deemed income/expense largely mirrors, but it must be *recognized* and reported consistently, and Digital's side lands in a loss entity. **[Whether amended returns or current-year correction is the right mechanism is not addressed in the library — unverified; confirm with a CPA.]**
3. **Pre-closing clean-up before Step 2 closes:** resolve the two Properties↔Services and Services↔Digital advances (note, contribution, or repayment) **before** contributing the LLCs, so Holdings does not inherit undocumented cross-debt and so capital accounts at contribution are real.
4. **Under the revised plan, Holdings never "makes interest-free loans among subsidiaries."** Funding subsidiaries is done by **documented capital contributions to capital accounts** (partnership contributions, not interest-free debt) **[partnership debt vs. capital mechanics beyond the §752 excerpt are not in the library — unverified]**; genuine inter-entity funding gets a note at ≥ AFR. Separate bank accounts and books per entity — non-negotiable.

---

## Revised step plan

1. **Carve Helio Grid stock out of the restructuring.** Written instruction to the advisor: Step 2 excludes the Helio shares. Keep them personally held; preserve §1202 records; use gifts/death for estate transfers of these shares (QSBS tacks).
2. **Reconcile Oakline Properties' tax balance sheet first** — the $1,760,000 gap between line items (implied capital +$1,380,000) and stated capital $(380,000) must be identified (likely missing distributions/liabilities). Do not close Step 2 until it foots. (See QUESTIONS.md.)
3. **Clean up the three advances** (note / contribution / repayment — Option A/B/C above) before closing.
4. **Form Oakline Holdings LLC (CO or WY — either is fine; WY saves no income tax and adds an annual report; manage from CO and file CO).** Confirm with counsel whether the revocable trust can serve as the 1% partner given grantor-trust attribution **[unverified in library]**; a live non-trust 1% owner or counsel-approved alternative may be safer if true partnership status matters.
5. **Contribute Services, Properties, Digital** to Holdings via assignment/contribution agreements (§721(a)). Compute the §752(b) deemed distribution (1% × $1,900,000 = $19,000); no §731(a) gain at contribution because basis ($1,520,000+ from Properties alone) exceeds it. Obtain lender consent/confirm no due-on-sale if required by the 2024 refi documents **[not in file; ask]**.
6. **Ratify real separateness:** separate accounts and books per entity; keep the Properties→Services building leases as written related-party leases; annual WY report (if WY) and CO filings per nexus.
7. **Standing guardrails:** Holdings distribution policy tested against §731(a) while Properties carries $(380,000) negative capital; any future intercompany funding at ≥ AFR with notes; any Helio corporate action (redemption/exit) reviewed under §1202 **before** signing; *new* startup investments may go through Holdings to capture §1202(g) flow-through at original issue.
8. Have the plan implemented/reviewed by a licensed CPA and attorney — the proposal is from an advisor that is expressly "not a law or CPA firm" (Summit Peak Wealth Advisors, proposal dated 2026-02-11 — `advisor_proposal.pdf`).

---

## Numbers (detail in `numbers.json`)

| Item | Arithmetic | Result |
|---|---|---|
| QSBS exclusion at risk | $9,400,000 − $12,000 = $9,388,000; cap max($10,000,000, 10×$12,000=$120,000) = $10,000,000; $9,388,000 < cap | **$9,388,000** |
| Imputed interest, Properties→Services | ($250,000 + $150,000) × 3.96% | **$15,840/yr** |
| Imputed interest, Services→Digital | $150,000 × 3.96% | **$5,940/yr** |
| Cumulative imputed to 2026-10-26 | $26,282 + $8,104 + $6,835 (simple, days/365) | **≈ $41,222** |
| Properties contribution gain | §752(b) deemed dist. $1,900,000×1% = $19,000 vs. basis ≥ $1,520,000 → §731(a) gain | **$0** (with open items) |

**Does not reconcile / left open:** the $1,760,000 Properties balance-sheet discrepancy (line items imply capital +$1,380,000 vs. stated $(380,000)). It does not change the $0 contribution-gain conclusion under either reading (basis clears $19,000 on both), but it must be resolved before closing and it changes how much negative-capital exposure Holdings inherits.

---

## Assumptions (prominently stated)

1. Stated tax capital of $(380,000) on the Properties balance sheet is authoritative despite the footing discrepancy.
2. Nadia's outside basis in the Properties interest at minimum equals implied inside asset basis ($1,520,000); Helio stock basis = $12,000 paid (no adjustments evident); 409A value $9.4M used as the exit value proxy.
3. Helio's representation (gross assets ≤ $1M at issuance, domestic C corp, active qualified trade or business) is accurate; nothing in the file indicates any subsequent transfer of the shares or corporate redemption **[the library's §1202 excerpt does not enumerate every disqualifying event beyond those listed — flagged, see QUESTIONS]**.
4. The advances outstanding are exactly those in `intercompany_cash_flows.csv` with no repayments.
5. Demand-loan/short-term AFR (3.96%) applied to all advances; simple annual interest (compounding convention not in the excerpt).
6. Nadia is treated as Colorado-resident/managed-from-CO per the nexus summary's assumption for her structures.

## Addendum — effect of client responses (received 2026-10-26)

### A1. Helio sale realistic in 12–18 months; her stake ≈ $9–10M

- **The exclusion still covers the whole stated range.** Holding period at a sale between Oct 2027 and Apr 2028: ≈ 7.7–8.2 years > 5. Gain = exit value − $12,000: at $9.0M → **$8,988,000**; at $9.4M → **$9,388,000**; at $10.0M → **$9,988,000**. Cap = greater of $10,000,000 or 10× basis ($120,000) → **$10,000,000** (the $15M branch applies only to post-July 4 2025 issuances; hers is 2020). Every dollar in the $9–10M range is **fully excluded**. *(§1202(a), (c) — `irc_1202_excerpt.md`.)*
- **The cap goes live just above the range.** Cap binds at exit value > **$10,012,000** (where gain = $10M); at $10M exactly the headroom is only **$12,000**. Example: a $12M exit → $1,988,000 taxable. If diligence pushes the price past ~$10.01M, the only lever this library suggests is **pre-closing gifts of shares** under §1202(h) (gifted stock takes the transferor's manner of acquisition and tacked holding period). Whether each donee obtains a **separate per-issuer cap** turns on Treas. Reg. §1.1202-2 — referenced in the library but **not reproduced there → [unverified]**; a CPA must confirm **before** any gift is made, and any transfer must occur **before** closing mechanics fix — a post-signing transfer choreography invites step-transaction collapse *(`step_transaction.md`)*.
- **Hard rules until closing:** no contribution of the shares to Holdings or any entity; no pledge, swap, or re-titling (except counsel-cleared gifts); confirm the share ledger, any certificates, and Helio's escrow/paying-agent forms name Nadia personally. Give the advisor and Helio's deal team written notice that her shares are not subject to the restructuring.
- **Consideration structure caveat:** if the acquirer offers rollover equity, acquirer stock, options, earnout or escrow, §1202's treatment of exchanged/retained shares is **outside the library excerpt → [unverified]** — review the term sheet with a tax attorney **before signing**. The cash-out, >5-year-held posture is the clean one.
- **The advisor's "reinvest without tax" wish, done correctly:** sell personally with the gain excluded; **after** closing contribute the cash proceeds to Holdings (§721(a) covers money contributions for partnership interests, no gain); Holdings then invests, including new small-business stock it acquires **at original issue itself** — §1202(g) flows the exclusion to partners who held the partnership interest when the stock was acquired and at all times after, and post-July 4 2025 issuances carry the higher $15M cap and 50/75/100 tiering. *(`irc_721_and_752.md`, `irc_1202_excerpt.md`.)* Nothing about the Helio exit needs to be routed *through* an entity; the wrong sequence — contribute first, exit second — costs up to ~$9.4M of exclusion.

### A2. Mortgage nonrecourse to her personally; 2024 refi cash went to her brokerage account

- Confirms the §752 characterization used above (nonrecourse, $1.9M) — nonrecourse status does not exempt it from the §752(b) shift ($19,000 at 99/1). *(§752(b), §731(a) — `irc_721_and_752.md`.)*
- Confirms the $1.2M was a **money distribution to her personally in 2024** — consistent with the $(380,000) negative capital and reinforcing the standing distribution guardrail: any further distributions while capital is negative run the §731(a) test against her basis. No numeric change: contribution gain estimate stays **$0**.

### A3. The 1% partner is her own revocable living trust ("the advisor said we need two partners")

- Client-confirmed. Nothing in the library states or supports a "two partners required" rule, and whether a revocable (grantor) trust counts as an owner separate from its grantor — hence whether Nadia + her own revocable trust makes a **partnership** at all — is **[unverified: not in library]**. The 99/1-with-own-trust split looks engineered to paper over the single-owner problem. Consequences of the two possible answers:
  - Trust disregarded → Holdings has one owner → the advisor's own "taxed as a partnership / files one return" premise collapses; the $19,000 §752(b) shift disappears (deemed distribution $0); liability characterization of the entity changes.
  - Trust respected → the $19,000 shift stands; contribution gain still $0 (basis ≫ $19,000).
- Either way the contribution arithmetic is $0, but **formation is now gated**: a licensed tax practitioner must confirm the ownership design *before* Holdings is formed. Do not proceed on the advisor's "we need two partners" assertion alone.

### A4. "No paperwork. I just move money where it's needed."

- Confirms the §7872 exposure is **systematic and ongoing**, not historical: $21,780/yr run-rate, ≈ $41,222 accrued through 2026-10-26, accruing ≈ **$60/day** ($21,780 ÷ 365 ≈ $59.7). *(§7872 — `irc_7872_afr.md`.)*
- **New, larger consequence:** the imminent exit puts **$9–10M of liquid proceeds** into the same undocumented pool. The library's veil-piercing warning (loans without notes, interest, or terms = evidence of commingling undermining separate-entity protection) now guards the wrong risk: a creditor or employee claim against Services (42 employees) could reach the Properties real estate *and* the sale proceeds if they sit in a shared, unpapered pot. **Remediation deadline is set by the closing date: notes / capital-contribution paper / repayment and separate accounts per entity must be in place *before* Helio proceeds arrive** — and the proceeds themselves must come in as documented contributions (§721(a)), not "moved where needed."

### A5. Client Q&A: "The advisor says the LLC is how I avoid tax when Helio sells — the gain lands in the LLC" *(client question 2026-10-26)*

- **"The gain lands in the LLC" is literally true and legally irrelevant.** An LLC taxed as a partnership does not park or shelter gain: it is a conduit — items realized by the partnership are reported by, and taxed to, the partners (partnership-conduit principle; the library's excerpts tax partners directly — §731(a) — and its nexus file confirms state filings follow the owners' activities; the general conduit rule itself is not reproduced in the library → [general principle, not library-verified]). Moving the shares into Holdings changes *who reports* the gain (still Nadia) but not *whether* it is taxed.
- **It is worse than irrelevant — it is the one move that destroys the exclusion.** The library's §1202 excerpt is explicit: "A contribution of stock to a partnership is not among the listed transfers; the partnership did not acquire the stock at original issue, and **the stock ceases to qualify in its hands**." *(§1202(c)(1), (h) — `irc_1202_excerpt.md`.)* So a sale **by Holdings** produces gain with **no §1202 exclusion** — $8,988,000–$9,988,000 fully reportable — while a sale **by Nadia personally** is **entirely excluded** across her stated $9–10M range. The advisor has the direction of the only decisive rule backwards; the difference is worth the full exclusion (up to ~$9.99M excluded gain; tax cost otherwise = at-risk gain × her rate — no rate authority in this library).
- **Pre-empted maneuver — "contribute now, distribute the shares back before closing":** §1202(h) does list *distributions from a partnership to a partner* as a tacking transfer, so the advisor might propose a round trip. **Do not attempt it:** the excerpt says the stock "ceases to qualify" in the partnership's hands, and whether a contribute-then-distribute round trip revives qualification is Treas. Reg. §1.1202-2 territory — referenced but **not reproduced in the library → [unverified]** — and a pre-planned in-and-out is exactly the choreographed sequence the step-transaction doctrine collapses *(`step_transaction.md`)*. If anyone proposes this, it needs a written tax-attorney opinion first.
- **Yes — Holdings can hold the *sale proceeds* (not the shares) after the sale.** Post-closing the Helio stock no longer exists; what she owns is $9–10M of cash. Sequence that realizes the advisor's promise lawfully:
  1. Close personally → gain fully excluded (§1202(a)).
  2. Contribute proceeds to Holdings as a documented **money** capital contribution — §721(a): no gain or loss (no §752(b) issue on money). *(§721(a) — `irc_721_and_752.md`.)*
  3. Holdings reinvests. For **new** small-business stock Holdings acquires **at original issue itself**, §1202(g) flows the exclusion through to her **only if she held the Holdings interest when Holdings acquired the stock and at all times thereafter**; post-7/4/2025 issuances carry the $15M cap and 50/75/100 tiering. *(§1202(a), (g) — `irc_1202_excerpt.md`.)* One open clock question — whether her partnership-interest holding period satisfies the >5-year requirement for passthrough QSBS — is not resolved by the excerpt → [unverified], CPA to confirm before Holdings buys intended QSBS.
  4. What the LLC can never do: shelter *ordinary ongoing* returns. Inside Holdings, every future gain/dividend/interest passes through and is taxed to her in the year earned [conduit, as above]. "Reinvest without tax" is never true even inside the LLC — only the §1202 exclusion on specific qualifying stock is.

### Remaining unknowns (flagged explicitly; client has no further information)

1. **Properties balance sheet does not foot** — $1,760,000 gap (line items imply capital +$1,380,000 vs stated $(380,000)). Resolve from CPA workpapers, not recollection.
2. **Helio share/ledger history since 2/2020** (any transfer, pledge, redemption, recapitalization) and gross-asset records at issuance — the live deal is the chance to obtain the cap table and records; ask Helio's team in writing.
3. **Mortgage due-on-sale / change-of-control terms** — pull the 2024 closing binder (matters only if the restructuring proceeds).
4. **Prior-year reporting** of the $1.2M distribution and the advances — CPA workpapers.
5. **Professional (not client) questions left open:** grantor-trust attribution / whether a valid partnership exists; §1.1202-2 donee per-issuer cap stacking; §7872 compounding/AFR-selection convention for demand loans; §1202 treatment of non-cash merger/rollover consideration. All labeled unverified above because the library does not reach them.

---

## Authorities used (complete list; all in `library/INDEX.md`)

- `irc_1202_excerpt.md` — 26 U.S.C. §1202(a), (c), (g), (h)
- `irc_721_and_752.md` — 26 U.S.C. §721(a); §752(b); §731(a)
- `irc_7872_afr.md` — 26 U.S.C. §7872; Rev. Rul. 2026-4 (AFR table excerpt)
- `state_nexus_summary.md` — multistate nexus summary (practice aid)
- `step_transaction.md` — *Commissioner v. Court Holding Co.*, 324 U.S. 331 (1945); *Gregory v. Helvering*, 293 U.S. 465 (1935)

Anything else I said that sounds like law is labeled **[unverified]** above and must be confirmed by a licensed practitioner before implementation.
