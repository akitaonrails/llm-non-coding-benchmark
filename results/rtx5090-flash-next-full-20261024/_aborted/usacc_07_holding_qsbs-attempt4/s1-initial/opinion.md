# Opinion — proposed Oakline Holdings restructuring

**For:** Nadia Oakline · **Re:** "PROPOSED RESTRUCTURING — Oakline Holdings," Summit Peak Wealth Advisors, 2026-02-11
**Prepared:** 2026-10-25

> **Scope and authority.** This engagement is a tax opinion only; it is not an entity-formation, estate, or securities
> work product. Per the engagement contract, the **only** authorities I may rely on are the five items listed in
> `library/INDEX.md`. Anything I say that is not supported by those five items is expressly labelled
> **[UNVERIFIED]** and should not be acted on until confirmed against primary law. Where I need a fact that the
> client file does not contain, I have asked in `QUESTIONS.md` rather than inventing it.
>
> **Available authorities (the complete universe for this opinion):**
> IRC §1202(a),(c),(g),(h) (`library/irc_1202_excerpt.md`); IRC §721(a), §752(b), §731(a) (`library/irc_721_and_752.md`);
> IRC §7872 and Rev. Rul. 2026-4 AFR table (`library/irc_7872_afr.md`); multistate nexus practice aid
> (`library/state_nexus_summary.md`); step transaction / substance over form, *Court Holding Co.* and *Gregory v.
> Helvering* (`library/step_transaction.md`).

---

## 1. Bottom line

The plan is **mostly harmless and mostly useless, except for Step 2 as to the Helio Grid stock, which is very
expensive.** The advisor's four claims do not survive examination:

| Advisor claim | Verdict | Why |
|---|---|---|
| "No tax event — it's all a §721 contribution" | **Half true** | §721(a) does block gain on the contribution of the LLC interests, but it does not address the §752(b)/§731(a) liability-shift consequence of contributing an entity with a $1.9M mortgage and **negative** tax capital, and it is silent on what a contribution does to §1202. (`irc_721_and_752.md`; `irc_1202_excerpt.md`) |
| "When Helio exits, the gain lands in the holding so you can reinvest without tax" | **False, and the most damaging sentence in the proposal** | Gain from stock held by a partnership **flows out to the partners** in the year of the sale (§1202(g) speaks of gain "flow[ing] to a partner"); there is no corporate-style reinvestment shelter. Worse, the contribution itself **disqualifies the stock** — §1202(c)(1) requires acquisition "at its original issue," and §1202(h) does **not** list a contribution to a partnership among the transfers that preserve tacking; the library states the stock "ceases to qualify in its hands." Estimated exclusion destroyed: **$9,388,000**. (`irc_1202_excerpt.md`) |
| "Liability protection" | **Self-defeating as proposed** | Step 3 ("one bank account, one set of books," interest-free loans with no notes) is, in the words of the §7872 material, "evidence of commingling that undermines separate-entity liability protection (veil piercing)." (`irc_7872_afr.md`) |
| "Simplicity / Holdings files one return" | **Not supported** | Nothing in the library supports the idea that one return means one tax outcome. The §1202(g) language shows partnership gain flowing **out** to partners; the nexus summary says holding LLC interests through a holding company "does not avoid Colorado filing for income flowing through," and Wyoming "has no income tax but requires an annual report" — i.e. a WY holding adds a filing and saves nothing. (`irc_1202_excerpt.md`; `state_nexus_summary.md`) |

**Recommendation: do Steps 1 and (a modified) 2 and 3, excluding the Helio stock; do not do Step 4 as written.**
Revised plan in §4. The single most important instruction in this opinion is: **do not put the Helio Grid stock
into Oakline Holdings LLC, or into any other LLC, partnership, or family entity.**

> **Update on the client's 2026-10-25 response (§8).** Three facts changed: Helio is talking to acquirers with a sale
> likely in **12–18 months** at a stake value of **$9–10M**; the 1% member is Nadia's **own revocable living trust**
> (so the proposed structure has **no second partner**); and the 2024 refinancing cash went into her **personal
> brokerage account**. Net effect: the §1202 exclusion ($8,988,000–$9,988,000 of gain, essentially the whole
> $10,000,000 cap) is now the dominant issue, the 99/1 partnership premise should be **abandoned**, and the
> restructuring should be **deferred until after the exit** while the loan/separateness cleanup is done now.
> Sections 2–7 remain the standing analysis; §8 governs where they differ on timing.

---

## 2. Step-by-step analysis

### Step 1 — Form Oakline Holdings LLC (Wyoming; taxed as a partnership; Nadia 99% / her revocable trust 1%)

**Tax consequence.** Formation of an LLC is not itself a taxable event. The classification is where the problem is:
the proposed 1% member is Nadia's **revocable** trust. A revocable trust is ordinarily treated as owned by the
grantor and is not a separate taxpayer, which puts in question whether Holdings has two *bona fide* partners at all.
If it does not, Holdings is a single-owner entity and — for federal income tax — disregarded: there is no
partnership return, no meaningful 99/1 allocation, and no partnership-level debt allocation. I flag this squarely:

> **[UNVERIFIED]** *Nothing in `library/INDEX.md` addresses grantor trusts, entity classification, or the
> "two bona fide partners" requirement.* I cannot cite authority for the proposition that the 1% revocable-trust
> member is not a partner for federal tax purposes. It is my professional judgment, not a cited conclusion, and it
> must be verified before Step 1 is executed.

**State consequence.** The Wyoming choice accomplishes nothing for income tax. Per the nexus practice aid, a
holding entity formed in Wyoming but managed from Colorado has **Colorado nexus (commercial domicile) and files
there**; Wyoming imposes no income tax but does require an annual report; and holding membership interests in LLCs
doing business in Colorado does not avoid Colorado filing for the income flowing through.
(`state_nexus_summary.md`) So the plan *adds* a Wyoming annual-report obligation and changes nothing about her
Colorado exposure.

**Recommendation: MODIFY.** Form the holding company only if there is a non-tax reason (control, succession
mechanics, centralized management). If formed: (a) form it in **Colorado**, or be prepared to file in Colorado
anyway; (b) do not rely on a revocable trust as the 1% member for partnership status — either qualify a real
second owner or accept single-member (disregarded) treatment and stop describing the structure as a partnership;
(c) budget the Wyoming annual report if WY is kept.

### Step 2 — Contribute Services, Properties, Digital **and the 30% of Helio Grid Inc**

Split this step in two. Its two halves have completely different consequences.

**2a — The three Oakline LLCs: generally fine, with a §752 trap to monitor.**

- §721(a): no gain or loss on contribution of property (here, the interests in the single-member LLCs, i.e. their
  assets) in exchange for a partnership interest. So the advisor's "no tax event" is correct **as far as §721 goes**.
  (`irc_721_and_752.md`)
- But Oakline Properties carries a **$1,900,000 nonrecourse mortgage and negative owner tax capital of $(380,000)**,
  and §752(b) treats a decrease in a partner's share of partnership liabilities as a **distribution of money**, with
  §731(a) turning that into **gain** to the extent money distributed exceeds outside basis. The library gives the
  arithmetic directly: "with a 99/1 partnership, **1% of the mortgage shifts to the other partner**."
  (`irc_721_and_752.md`)
- Arithmetic (see §6 and `numbers.json`): deemed distribution = 1% × $1,900,000 = **$19,000**. Nadia's outside
  basis is large enough on either reading of the balance sheet ($1.52M–$3.28M) that **§731(a) gain = $0 today.**
- Why it still matters: the same mechanism is a loaded gun. If the non-Nadia share of the debt ever grows
  (a real 5% partner → $95,000; 10% → $190,000; 30% gifted to family → **$570,000** deemed distribution), or if
  Holdings distributes leveraged refinancing proceeds while her basis is thin, the contribution *becomes* a gain
  event. The 2024 distribution of $1.2M of refinancing proceeds is exactly how her capital went negative.
  (`irc_721_and_752.md`; balance sheet in `documents/`.)

**Recommendation: DO (2a), with conditions** — no further debt-funded distributions out of Properties while her
tax capital is negative; keep the mortgage where it is; document the contributions with assignment instruments and
capital-account bookkeeping; and re-run the §752(b) arithmetic before **any** gift of Holdings interests or any
future refinancing distribution.

**2b — The 30% of Helio Grid Inc: do not do this.**

This is where real money is at stake, and the stock currently looks like a textbook §1202 holding:

| §1202 requirement (per `irc_1202_excerpt.md`) | Her facts (per `documents/`) | Status |
|---|---|---|
| Stock of a **C corporation** originally issued after Aug. 10, 1993 | Delaware C corp; issued 2020-02-18 (SPA) | Met on the file |
| Corporation was a **qualified small business at issuance** | SPA §2.3: gross assets ≤ $1,000,000 at issuance; domestic C corp; active qualified trade or business | Supported by the company's representation; obtain support (`QUESTIONS.md` R1(1)) |
| Acquired **at original issue**, directly, for money | SPA: "issued directly by the Company (original issuance)"; $12,000 cash | Met on the file |
| Holding period for the **100% tier** (acquired after 9/27/2010, held > 5 years) | Acquired 2020-02-18; 5 years ran on 2025-02-18 | Met today |
| Per-issuer cap: greater of **$10M** (the $15M figure applies only to issuances after 7/4/2025) or **10× basis** | Gain $9,388,000; 10 × $12,000 = $120,000 → cap = **$10,000,000** | Gain is **$612,000 under the cap** → the whole gain is excludable |

If she keeps the stock in her own name, the estimated **$9,388,000** of gain
($9,400,000 409A value − $12,000 basis) is fully excludable. If she contributes it to Holdings:

- §1202(c)(1) requires the taxpayer to acquire the stock "at its original issue." Holdings will not have done so.
- §1202(h) lists gift, death, and distribution **from** a partnership to a partner as transfers that carry over the
  original-acquisition characterization with a tacked holding period. The library is explicit: "**A contribution of
  stock to a partnership is not among the listed transfers**; the partnership did not acquire the stock at original
  issue, and the stock ceases to qualify in its hands (see §1202(h)(2); Treas. Reg. §1.1202-2 (proposed))."
- §1202(g) does not rescue her: partner-level tacking requires the partner to have held the partnership interest when
  "**the partnership acquired the stock**" — and here the partnership's stock is not QSBS in the first place.

Estimated cost of the contribution: **up to $9,388,000 of exclusion destroyed** — roughly **$1.9M–$2.3M** of
federal tax at customary long-term capital-gain rates. **[UNVERIFIED]** *No rate is in the library*; the 20% /
20%+3.8% figures below are stated as assumptions, not citations.

Do **not** try to out-think this by contributing the stock and taking it back out. A distribute-back is a listed
§1202(h) transfer, but the library's stated position is that the stock "ceases to qualify" in the partnership's
hands, and a contribute-then-distribute round trip planned in advance is precisely the kind of formally separate
set of steps that is "collapsed into a single transaction when they are interdependent or pre-planned toward a
single end," with tax consequences following substance. (`irc_1202_excerpt.md`; `step_transaction.md`) The safe
conclusion is: **never let the stock leave her name.**

**Recommendation: DO NOT (2b).** Helio stays titled in Nadia Oakline's individual name.

### Step 3 — Holdings makes interest-free loans among subsidiaries; "one bank account, one set of books"

Two independent problems.

**(a) §7872 imputed interest.** The library's statement is direct: interest-free or below-market loans between
related entities are recharacterized, with the lender treated as receiving imputed interest at the AFR and the
borrower as paying it, and, between commonly owned entities, a corresponding distribution/contribution is deemed to
occur. AFR for this engagement: short-term (≤3 yr) 3.96%; **mid-term (3–9 yr) 4.12%**; long-term 4.58%.
Annual imputed interest on the existing balances at 4.12%:

- Properties → Services, $400,000 × 4.12% = **$16,480**
- Services → Digital, $150,000 × 4.12% = **$6,180**
- Total = **$22,660** per year, with **no cash moving** — Properties' owner picks up taxable interest income and
  funds a deemed contribution to the borrower. (`irc_7872_afr.md`)

Sensitivity: at the 3.96% short-term rate the figures are $15,840 / $5,940 / $21,780 (a $880 difference).
**[UNVERIFIED]** *The library does not state which AFR term applies to an undocumented demand loan, nor the
accrual/compounding method (semi-annual vs. annual), nor any §7872 de minimis exception.* These figures are
therefore annual estimates on simple interest, and prior-year amounts would need day-count accruals from the loan
dates (2024-03-01 $250,000; 2025-06-15 $150,000; 2025-09-01 $150,000) — I have not attempted precise prior-year
numbers.

Note also what §7872 will *not* do for her: Digital is a loss business, so a deemed interest deduction there may
not be usable in the year it is deemed to arise. **[UNVERIFIED]** *No basis, at-risk, passive-activity, or
related-party limitation rules are in the library, so whether any of them would deny or defer a deemed deduction
cannot be determined from the material I was given.*

**(b) Veil piercing / commingling.** The same library entry records that "[l]oans without notes, interest or
repayment terms are also evidence of commingling that undermines separate-entity liability protection (veil
piercing)." Commingling cash into "one bank account, one set of books" would merge the HVAC business (42 employees,
real claim exposure) with the two buildings. That is the opposite of the "liability protection" Step 1 is supposed
to buy. (`irc_7872_afr.md`)

**Recommendation: DO NOT (3) as proposed.** Either eliminate the intercompany debt or fund it as equity, and run
separate bank accounts and separate books per entity (§5).

### Step 4 — "Holdings files one return… no tax event"

Do not adopt this framing. Two parts:

- **"One return."** A partnership return is not a substitute for the owners' returns; income and gain flow **out**
  to the partners (the §1202(g) language speaks of gain flowing "to a partner"), and the nexus summary confirms that
  routing LLC interests through a holding entity "does not avoid Colorado filing for income flowing through."
  (`irc_1202_excerpt.md`; `state_nexus_summary.md`) **[UNVERIFIED]** *the library does not contain the
  partnership-return or Colorado-return mechanics themselves*; my point is narrower: **nothing in the library
  supports the "one return" benefit, so it should not be relied on.**
- **"No tax event."** Right as to §721(a) on the LLC interests; incomplete as to §752(b)/§731(a) (§2, Step 2a); and
  wrong on the one asset that matters, the Helio stock (§2, Step 2b).

**Recommendation: DO NOT (4) as drafted.** Keep the §721 mechanics, drop the marketing claims, and plan filings
on the assumption that Colorado continues to matter and Wyoming adds a report.

---

## 3. What should and should not be done with the Helio Grid stock

**Do:**

1. **Leave it in Nadia's individual name.** Do not contribute it to Oakline Holdings LLC, to any other LLC or
   partnership, or to a "family LLC," in exchange for an interest. §1202(c)(1); §1202(h) as read in the library.
2. **Preserve the >5-year clock and the file.** She is already past five years, so the 100% tier applies; there is no
   reason to accelerate a sale for §1202 reasons, and no reason to delay one either. Keep permanently: the 2020
   Common Stock Purchase Agreement (SPA §2.3 gross-asset and C-corp representations; the "original issuance"
   recital), proof of the $12,000 payment, the 83(b) election (SPA recites it as filed 2020-03-02, 13 days
   after the 2020-02-18 grant, so timely on its face), though the underlying inclusion/basis facts are unknown,
   and each year's 409A.
3. **Use gift and death for the estate plan, not entity contribution.** §1202(h) expressly treats stock acquired
   "by gift, at death" as acquired in the same manner as the transferor, with a tacked holding period. So her
   estate-planning objective can be met by transferring the shares by gift (to an irrevocable trust or to family) or
   at death, without disturbing §1202 — provided the transferee relationship is documented. (`irc_1202_excerpt.md`)
   **[UNVERIFIED]** *whether a transfer to her own revocable trust is a non-event for §1202 is not addressed in the
   library; do not move the shares into the revocable trust without a specific determination.* The cheapest
   compliant answer is: leave the shares where they are and let the trust's beneficiaries take them.
4. **Insist that any exit be a sale of the shares** (stock sale), and confirm with securities/corporate counsel that
   the exit documents do not require the shares to be contributed, exchanged, rolled into an acquirer entity, or
   moved into a blockage/ESOP-type structure before closing. The §1202 exclusion here attaches to gain on **her
   stock**; anything that moves the stock into another holder before the sale risks the same disqualification as the
   Holdings contribution.
5. **Watch the cap on the way out.** Her gain is $612,000 below the $10,000,000 per-issuer cap today. If Helio's
   value rises materially, the excess over the cap becomes taxable — e.g. at a $12,000,000 stake value, gain of
   $11,988,000 would leave roughly **$1,988,000 taxable**. The cap is a per-issuer amount; partial sales consume it.
   **[UNVERIFIED]** *whether the cap is applied per-issuer per-life or per-sale is not stated in the library beyond
   "per-issuer cap"; confirm before sequencing partial sales.*
   → **Superseded in detail by §8.4:** the client now expects a $9–10M exit inside 12–18 months, so the cap is binding
   at any stake value above **$10,012,000**, and the cap-mechanics question is urgent rather than academic.

**Do not:**

1. Do not contribute the shares to Holdings or any other entity, at any time, "for simplicity" or "for estate
   planning." Estimated exclusion forfeited: $9,388,000.
2. Do not do a contribute-then-distribute or contribute-then-sell round trip to recover the tacking; the round trip
   is exactly what the step-transaction doctrine addresses. (`step_transaction.md`)
3. Do not let Holdings borrow against, purchase, or "reimburse" the stock, and do not let the shares be swapped,
   redeemed for an LLC interest, or dropped into a JV or holding vehicle for any Helio financing or M&A step
   without a §1202-specific determination.
4. Do not let the advisor's premise — "the gain lands in the holding so you can reinvest without tax" — drive the
   sale timing. Partnership gain flows out to her in the year of sale (§1202(g)); there is no entity-level
   reinvestment shelter, and the contribution costs her the exclusion.
5. Do not rely on the 409A figure as a transaction price; the exclusion is measured by real gain on a real sale.
6. Do not assume the QSB test is ongoing — §1202(c)(1) tests qualified-small-business status **at issuance**, so
   Helio's later growth does not hurt her; but do not let anyone tell her the exclusion is locked without the
   issuance-date documentation in hand. **[UNVERIFIED]** *the $50M gross-asset ceiling and the excluded-trade-or-
   business list that make up "qualified small business" and "qualified trade or business" are not reproduced in the
   library excerpt; the SPA representation is what I have.*

---

## 4. Revised step plan

> **Timing override (§8.6):** given the 12–18 month exit window the client reports, Phases 2 and 3 (forming Holdings
> and contributing the LLC interests) should be **deferred until after the Helio exit**. Phases 0, 1 and 4 (loan
> remediation, §1202 evidence file, and entity separateness) should proceed now. The 99/1 two-partner design should
> be abandoned — see §8.2.

**Phase 0 — Fix the intercompany balance sheet first (before forming anything).** See §5. Remediation of the
undocumented loans is the cheapest, most urgent item in this file.

**Phase 1 — Helio: quarantine and document.** Shares stay in Nadia's individual name. Assemble the §1202 file
(SPA, 83(b) and the basis/inclusion facts, proof of the $12,000 payment, gross-asset support for Feb 2020, annual
409As). Confirm transfer/ROFR/co-sale restrictions in the full Helio financing documents (`QUESTIONS.md` R1(4)) so no
future reorganization of *her* holdings accidentally trips them.

**Phase 2 — Optional holding company, correctly done.** Form Oakline Holdings **in Colorado** (or accept Colorado
filing anyway, plus the Wyoming annual report). Do **not** rely on the revocable trust's 1% for partnership status
— either use a real second owner/interest or accept disregarded status and describe the structure honestly. Fund it
only with Services, Properties and Digital.

**Phase 3 — Contributions (modified Step 2).** Documented contributions of the three Oakline LLC interests to
Holdings under §721(a), with: assignment instruments; capital accounts set from actual inside basis; the mortgage
staying at Properties; and a written confirmation that the §752(b) deemed distribution is $19,000 and produces no
§731(a) gain at her current basis. **The Helio shares are not on the contribution schedule.** Re-run the §752
arithmetic before any gift of Holdings interests (1% → 30% turns $19,000 into $570,000 of deemed distribution) and
before any further refinancing distribution.

**Phase 4 — Governance and separateness (replaces Step 3).** Separate bank accounts and separate books per entity.
Intercompany transactions only under signed written agreements at or above the AFR (mid-term 4.12% for this
engagement), with a payment schedule, actual payments, and member/manager consents. No cross-guarantees of the
Properties mortgage by the operating company without analysis. Consider keeping Properties out of Holdings, or in a
separate sister LLC, so an HVAC judgment cannot reach the buildings. **[UNVERIFIED]** *the library contains no
authority on how to structure against upstream/downstream piercing; that is a practice recommendation, not a cited
conclusion.*

**Phase 5 — Filing plan.** Assume continued Colorado filing for the flow-through income (commercial domicile, and
flow-through income of CO businesses stays CO-filing); Wyoming annual report if WY is kept; one 1065 if a real
partnership exists, plus her own 1040, and state returns as required. **[UNVERIFIED]** *state filing mechanics
beyond the nexus summary are not in the library.*

**Phase 6 — Exit planning for Helio.** Sell the shares personally. Sequence partial sales against the $10,000,000
per-issuer cap ($612,000 of headroom at today's valuation). Keep the sale a sale of stock.
**→ See §8.4–§8.5 for the updated cap numbers (headroom is only $12,000 at a $10M stake value) and the hard rules that
now apply between today and a signed deal.**

---

## 5. Intercompany-loan remediation

The file shows two loans with no notes and no interest: **Properties → Services $400,000** ($250,000 on 2024-03-01
and $150,000 on 2025-06-15, both "documentation: none") and **Services → Digital $150,000** (2025-09-01,
"documentation: email only").

**Consequence today.** While all three LLCs are single-member and disregarded, Nadia stands on both sides of each
loan, which is probably why no one has worried about them. The moment Holdings owns all three — or a real second
member/partner exists — they are loans **between related entities** squarely inside the §7872 description, with
imputed interest of **$16,480 + $6,180 = $22,660 a year** at the 4.12% mid-term AFR, deemed distributions and
contributions to close the loop, and, separately, documented evidence of commingling that weakens the liability
protection the restructuring is supposed to buy. (`irc_7872_afr.md`)

**Preferred fix — eliminate the debt rather than paper it:**

1. **Properties → Services, $400,000.** Either (a) Services repays in cash and Properties holds the cash or pays
   down the mortgage; or (b) Properties treats the $400,000 as a **capital contribution** to Services (no §7872
   issue thereafter; Services gets permanent capital, which also matters because Digital losses and Services'
   obligations may be constrained by capital — **[UNVERIFIED]**, no basis/at-risk rules in the library). Do not
   leave it as an undocumented demand note.
2. **Services → Digital, $150,000.** Digital is a loss business, so a loan is the wrong instrument: it cannot pay
   interest. Convert to a capital contribution (documented as such by the members) and write the $150,000 up on both
   books. If a loan is insisted on, execute a term note of 3–9 years at **≥ 4.12%** with a stated amortization
   schedule and *actually make* the payments.
3. **For the past (2024–2025).** Two options: (i) compute and report imputed interest for the open years, using
   day-count accruals from 2024-03-01, 2025-06-15 and 2025-09-01, and true up the returns; or (ii) where the
   economics support it, recharacterize as capital contributions and paper it contemporaneously, recognizing that
   recharacterization for prior years is a judgment call, not a filing trick. **Note the reconciliation problem in
   §6:** until the Properties balance sheet is understood, I will not guess what actually happened to $1.76M of
   value in these accounts — the "loans" may in substance be distributions.
4. **Going forward.** Any new intercompany funding requires (i) a written note at ≥ the applicable AFR, (ii) a
   stated maturity and amortization, (iii) evidence of payment, (iv) separate accounts and books, and (v) annual
   review with the AFR reset. A standing annual "true-up" entry should be made for imputed interest on any loan
   that is allowed to exist.
5. **Do not do the "one bank account, one set of books" step.** It converts a fixable paperwork problem into a
   veil-piercing problem. (`irc_7872_afr.md`)

---

## 6. Numbers, and one thing that does not reconcile

All arithmetic is reproduced in `numbers.json` and computed in Python.

**(a) §1202 exclusion at risk (Helio stock).**

```
409A value of Nadia's 30% stake    $  9,400,000   (documents/org_chart.md)
less basis                         $     12,000   (SPA: 3,000,000 sh × $0.004)
= gain                             $  9,388,000
100% tier (acquired 2020-02-18 > 9/27/2010, held > 5 yrs) → exclusion % = 100%
per-issuer cap = greater of $10,000,000 (issuance pre-7/4/2025)
                 or 10 × basis = 10 × $12,000 = $120,000          = $10,000,000
exclusion available = min($9,388,000, $10,000,000) × 100%         =   9,388,000
headroom under cap                                                =     612,000
```
**Exclusion destroyed if the stock is contributed to Holdings: $9,388,000.**
Illustrative federal tax cost **[rate UNVERIFIED — no rates in the library]**: at 20% = $1,877,600; at
23.8% (20% + 3.8%) = $2,234,344; at 40% = $3,755,200. Colorado tax on this gain would follow her Colorado filing
obligation (`state_nexus_summary.md`); the Colorado rate is not in the library, so it is not quantified.
If the stake is worth $12,000,000 instead of $9,400,000, the cap binds and about $1,988,000 of the gain is taxable
even with the stock held personally. **Updated for the client's $9–10M exit estimate in §8.4:** exclusion at risk runs
**$8,988,000 to $9,988,000** with taxable gain beginning at a stake value of **$10,012,000**; scenario table in
`numbers.json` → `qsbs_detail.exit_scenarios`.

**(b) §752(b) deemed distribution on contributing Oakline Properties.**

```
mortgage (nonrecourse)                       $1,900,000
share shifted to the 1% member per library   1% × 1,900,000  = $19,000  (§752(b) deemed money distribution)
outside basis, Reading A (inside asset basis)
   buildings 3,400,000 − accum dep 1,120,000 + land 600,000 + note 400,000 = 3,280,000
outside basis, Reading B (stated tax capital + debt)
   (380,000) + 1,900,000                                          = 1,520,000
§731(a) gain = max(0, 19,000 − basis)                            = $0   on either reading
sensitivity: 5% shifted = $95,000 · 10% = $190,000 · 30% = $570,000
```
So `properties_contribution_gain_estimate` = **$0**, and that conclusion is robust to which basis reading is right.
It is *not* robust to a future change in the ownership split or to further leveraged distributions.

**⚠ Open item — the Properties balance sheet does not reconcile, and I am not forcing it.**

```
assets: 3,400,000 − 1,120,000 + 600,000 + 400,000 = 3,280,000
liabilities:                                        (1,900,000)
implied owner's equity                              + 1,380,000
stated "Owner's tax capital"                          (  380,000)
difference                                            1,760,000   ← UNEXPLAINED
```
The 2024 distribution of $1.2M of refinancing proceeds helps explain why the stated capital line is **negative** —
money that left the entity reduces a capital account — but it does **not** explain the $1,760,000 difference set out
above. A distribution out of a disregarded entity moves cash out and reduces the capital account by the same amount;
it changes neither the inside basis of the assets nor the +$1,380,000 assets-minus-liabilities figure, so it cannot
close the gap at either end of it. What is still unexplained is the gap itself (prior operating losses or
distributions the sheet does not show? unrecorded liabilities? the $400,000 "Due from Services" being in substance a
distribution? a missing asset line?). Nothing is forced to balance. Only the CPA's records can answer it —
`QUESTIONS.md` R2(1); the client has confirmed she cannot resolve it from her own knowledge, and the item is
**not** being re-asked of her. Until it is answered, any precise outside-basis number — including a future §731(a)
gain — is provisional.

**(c) Imputed interest, annual, at the 4.12% mid-term AFR** (`irc_7872_afr.md`):

```
Properties → Services  $400,000 × 4.12% = $16,480
Services  → Digital    $150,000 × 4.12% =  $6,180
                              total     = $22,660 / yr
at 3.96% short-term:   $15,840 + $5,940 = $21,780 / yr   (difference $880)
```

**Assumptions carried through `numbers.json`** are restated in full there and in `STATUS.md`.

---

## 7. What is not verified and would change the analysis

1. Grantor-trust / two-partner classification of Holdings as proposed (**[UNVERIFIED]**, biggest structural risk
   after the Helio issue).
2. AFR term and accrual mechanics for undocumented demand loans; any §7872 exception (**[UNVERIFIED]**).
3. Basis, at-risk, passive-loss and related-party deduction limits for Digital's deemed interest expense and
   losses (**[UNVERIFIED]**).
4. Tax rates (capital-gain, NIIT, AMT on QSBS, Colorado) (**[UNVERIFIED]** — the library contains no rates).
5. The definition of "qualified small business" / "qualified trade or business" beyond the SPA's representation, and
   the exact per-issuer cap mechanics (**[UNVERIFIED]** beyond §1202(a) as excerpted).
6. The consequences of the 2020 §83(b) election recited in the SPA excerpt, for holding-period start and basis
   (**[UNVERIFIED]** — the provision governing that election is not in the library).
7. Assignment of the nonrecourse mortgage under §752 where the lender is a third party and Nadia is not personally
   liable: the library's 1%-shift arithmetic is the authority I am relying on; whether a different nonrecourse
   liability allocation would apply to a 99/1 partnership is **[UNVERIFIED]**. Under any allocation between 1% and
   30% the current gain is still $0 at her basis, so this does not change today's answer.
8. Everything about gift/estate tax, trust mechanics, and Helio securities restrictions: outside the library
   entirely; referred to counsel in `agreements_required.md`.
9. **Added after the client's response of 2026-10-25 (§8):** whether the exit will be a sale of her **stock** or an
   asset sale by Helio, a merger, a rollover or a blocker structure, and when escrow / holdback / earnout amounts
   become gain. The library is silent on M&A and installment mechanics, so each of those points is **[UNVERIFIED]**
   and must be answered before an LOI or term sheet is signed (§8.5; `agreements_required.md` items 37–41).
10. Whether the per-issuer cap is a per-issuer lifetime cap or a per-sale/per-year cap, and whether a **donee** of
    gifted shares holds a separate cap. The library says only "per-issuer cap" (**[UNVERIFIED]**, §8.4). On her own
    numbers this is worth up to $9,988,000, so it is the highest-value open question in the file.
11. **G1 — whether any step has already been executed.** `documents/org_chart.md` carries a "Step 1: Wyoming" note
    dated **2025-11-04**. If Holdings already exists, or if any Helio share has already been assigned, this opinion is
    remedial rather than prospective and must be re-issued on the executed facts (`QUESTIONS.md` G1).

---

## 8. Client response of 2026-10-25 — new facts, what changes, and the exit timeline

### 8.1 What the client confirmed

| # | Fact supplied by the client | Effect on this opinion |
|---|---|---|
| 1 | **Helio is in discussions with acquirers; a sale in 12–18 months is realistic; her stake would be about $9–10M.** | The §1202 question stops being theoretical. Exit-specific guidance is in §8.3 and §8.4. It also changes the recommended **sequence** of the restructuring (§8.6). |
| 2 | **The Properties mortgage is nonrecourse to her personally**, and the **2024 refinancing cash went into her personal brokerage account.** | Confirms the $1.2M left Properties as a **distribution to her**, which is consistent with the negative tax capital — see §8.7. It does not resolve the balance-sheet gap, and it does not resolve the lender consent/assignment question (G2). |
| 3 | **The 1% member is her revocable living trust, and the advisor's reason for the 1% was "we need two partners."** | This closes the question I flagged as the biggest structural risk (§7.1). The plan as drafted has **no second partner**. See §8.2. |
| 4 | For everything else, **the client has no additional information.** | The remaining unknowns are **not** re-asked of her. They are restated in `QUESTIONS.md` as (a) documents only third parties hold (Helio, the CPA, the lender) and (b) items carried as stated assumptions. |

### 8.2 The "two partners" premise is wrong, and it collapses the proposed 99/1 structure

The advisor's stated reason for putting 1% in Nadia's **own revocable living trust** — that "we need two partners" —
does not serve any purpose she actually needs served.

**Conclusion: as drafted, Oakline Holdings LLC will most likely have one owner, not two, for federal tax purposes.**
A revocable living trust whose grantor is Nadia is not a separate taxpayer from Nadia. **[UNVERIFIED]** *the grantor-trust
and two-bona-fide-partner rules are not in the library; this conclusion is professional judgment, not citation, and
must be confirmed against the primary authorities on grantor trusts and entity classification (none of which is in
`library/INDEX.md`) before anything is filed.*

What follows, by configuration:

| Configuration | Partnership for federal tax? | §752(b) deemed distribution on contribution | §7872 imputed interest | Form 1065? |
|---|---|---|---|---|
| Proposed: Nadia 99% + **her own revocable trust** 1% | **Probably not** — one owner **[UNVERIFIED]** | **$0** (no partner to shift 1% to) | **$0** while single-member **[UNVERIFIED]** | No (disregarded) |
| Nadia 100%, no trust member | No — disregarded | $0 | $0 | No |
| A **real** second owner (gift to an irrevocable trust or to family) | Yes | 1% = $19,000 · 5% = $95,000 · 10% = $190,000 · 30% = $570,000 | $22,660/yr | Yes |
| Holdings not formed at all (three single-member LLCs) | No | n/a | $0 today | No |

Three consequences worth stating plainly:

1. **She does not need a second partner for anything in the proposal.** Two partners are needed only to be a
   *partnership for federal tax purposes*. Limited liability is a state-law question about the LLC itself, and none of
   the four benefits the advisor promised require partnership status. **[UNVERIFIED]** *that an LLC's liability
   protection does not depend on having two members is not addressed in the library; confirm with entity counsel.*
2. **Buying a second partner to get partnership status would create tax cost, not avoid it.** Any genuine transfer of
   Holdings interests moves the §752 liability share with it (see §8.7), and starts the §7872 clock at $22,660 a year.
   It also raises gift-tax and valuation questions entirely outside the library.
3. **The estate-planning rationale does not need Holdings either.** The three Oakline LLC interests can be made part of
   her existing estate plan directly (the existing revocable trust), which is a far cheaper answer to the advisor's
   stated goal. **[UNVERIFIED]** *retitling LLC interests into her own revocable trust as an income-tax non-event is
   not addressed in the library; get a determination before doing it. The Helio-share version of this move remains a
   do-not, §3 Do-Not 1.*

**Recommendation:** abandon the 99/1 trust split. Either (a) keep all three LLCs as single-member entities and use a
single-member holding LLC purely as a state-law wrapper, describing it honestly as disregarded, or (b) make a real,
gift-tax-advised transfer of interests and re-run the §752 arithmetic first. Do not implement the trust's 1% and hope
the IRS treats it as a partnership.

### 8.3 An exit inside 12–18 months: what it does **not** change

Nothing about the timing threatens the exclusion:

- The 100% tier was secured on **2025-02-18**, five years after the 2020-02-18 acquisition (`irc_1202_excerpt.md`).
  A sale in 2027 or 2028 is comfortably in the 100% band; there is no reason to rush or delay a sale for §1202 reasons.
- §1202(c)(1) tests qualified-small-business status **at issuance**, so Helio's growth and the acquirer's size do not
  disqualify her stock. **[UNVERIFIED]** *the $50M gross-asset test itself is not reproduced in the library, so the
  issuance-date documentation remains the load-bearing evidence.*

### 8.4 What it does change: the cap is now the live number

Her own range ($9–10M) puts the gain almost exactly on the $10,000,000 per-issuer cap.

```
stake value     gain (value − $12,000 basis)   excluded (cap $10,000,000)   taxable
    $9,000,000              $8,988,000                    $8,988,000             $0
    $9,400,000              $9,388,000                    $9,388,000             $0   ← 409A figure on file
   $10,000,000              $9,988,000                    $9,988,000             $0   ← only $12,000 of headroom
   $10,012,000             $10,000,000                   $10,000,000             $0   ← cap starts binding here
   $10,500,000             $10,488,000                   $10,000,000        $488,000
   $11,000,000             $10,988,000                   $10,000,000        $988,000
   $12,000,000             $11,988,000                   $10,000,000      $1,988,000
```

- **The number to watch is $10,012,000 of stake value** (gain = $10,000,000). Below it, everything is excluded;
  above it, each additional dollar is taxable gain.
- Illustrative cost of the excess **[rate UNVERIFIED — no rates in the library]**: $488,000 of taxable gain ≈
  $116,144 at 23.8%; $988,000 ≈ $235,144; $1,988,000 ≈ $473,144.
- The alternative cap, 10 × basis, is $120,000 and is irrelevant unless her basis turns out to exceed $1,000,000 —
  which no document in the file supports. So the cap is $10,000,000 on any view.
- Because a real deal is now foreseeable, the **cap mechanics question becomes urgent**: whether the $10,000,000
  per-issuer cap is per-issuer per-life or per-sale/per-year is **[UNVERIFIED]** beyond the words "per-issuer cap" in
  `irc_1202_excerpt.md`. Do not structure partial sales, tranches, or escrowed closings to "use the cap twice" until
  that is confirmed by a §1202 specialist.
- The library contains nothing on installment sales, earnouts, holdbacks or escrows, so **when** gain is recognized in
  an acquisition that pays over time is **[UNVERIFIED]** and must be confirmed.

### 8.5 The 12–18 month runway: hard rules, and the one avenue to have verified

**Hard rules between today and a signed exit** (all §1202-driven; §3 applies with more force now that there is a real
transaction in view):

1. **Do not move the Helio shares anywhere.** Not into Holdings, not into a "cleanup" entity, not into a trust, not
   into a JV or blocker an acquirer proposes. The exclusion at stake is $9–10M; nothing an acquirer offers an
   individual seller is worth that.
2. **Do not accept rollover equity that requires her to contribute Helio shares into an acquirer LLC or partnership.**
   The rolled portion would be a contribution — not a §1202(h) listed transfer — and cannot be undone. If the deal
   requires a rollover, it must be structured so she holds **stock of a corporation** in her own name, and only after
   a §1202-specific determination. **[UNVERIFIED]** *the library does not address reorganizations, mergers, asset
   sales, or rollover structures at all; whether a given structure preserves §1202 on the cashed-out portion is a
   specialist question, and it is worth real money here.*
3. **Push for a sale of stock, not an asset sale by Helio.** She can only exclude gain on a sale or exchange measured
   by `irc_1202_excerpt.md` §1202(a) of stock **she** holds. If Helio sells its assets, she is not selling stock.
   **[UNVERIFIED]** *the library does not address asset-sale or merger mechanics; raise it with deal counsel early,
   before an LOI is signed.*
4. **Do not gift Helio shares to spread gain while a sale is being negotiated.** §1202(h) does keep gifted stock
   qualified in the donee's hands (tacked holding period, same manner of acquisition), so the *mechanism* is available
   in principle. But a gift made as part of a planned, negotiated sale is exactly the kind of formal step the
   substance-over-form and step-transaction authorities in `step_transaction.md` (*Court Holding*, *Gregory*) are aimed
   at. Any such planning would have to happen **now**, well before an LOI, with real transfer of dominion and
   independent (estate) purpose. **[UNVERIFIED]** and decisive: **whether each donee gets a separate $10,000,000
   per-issuer cap** — nothing in the library answers it. If the answer is yes, gifts made early could matter if the
   deal values her stake above $10,012,000; if no, the exercise is pointless and taxable-adjacent. Gift tax is outside
   the library: estate counsel only.
5. **Do not restructure the Oakline entities between now and closing beyond the cleanup work in §5.** A restructuring
   executed on the eve of a nine-figure-adjacent personal liquidity event invites examination of the steps as one
   planned transaction. **[UNVERIFIED]** *applying the doctrine to this fact pattern is my judgment, not a cited
   holding.*
6. **Get the estate documents to reach the shares without moving them.** §1202(h) covers stock acquired "by gift, at
   death" with a tacked holding period, so a will/trust that passes the shares at death preserves her acquisition
   character without any pre-sale transfer. Basis-at-death and estate-tax consequences are outside the library.

### 8.6 Sequencing: the restructuring should wait; the cleanup should not

Given the exit window, I now recommend deferring the entity work:

| Now (Q4 2026 – Q1 2027) | Before any LOI / signing | At or after closing |
|---|---|---|
| Separate bank accounts and books; stop the shared-treasury idea. | §1202 structure review of the deal (stock sale vs asset sale vs merger; rollover demands). | If desired, then do Steps 1–2 excluding Helio, with §752 re-run. |
| Paper or eliminate the $400,000 and $150,000 intercompany balances (§5). | Confirm lender consent/assignment position on the $1.9M mortgage. | Consider funding a capital contribution to Properties and retiring the mortgage (see §8.7). |
| Assemble the §1202 evidence file from **Helio's** records (gross assets at 2/18/2020, C-corp status, QTIB, 409As, SPA/83(b) file). | Deal counsel to reject or restructure any pre-closing share transfer, entity swap, or blocker. | Return to the 2024–2025 §7872 question with the CPA once separateness exists. |
| Do **not** form Holdings on the advisor's 99/1 terms. | Do not sequence partial sales until cap mechanics are confirmed. | Decide whether a holding wrapper is wanted at all (§8.2). |

### 8.7 The refinancing cash in her brokerage account — three consequences

1. **It helps explain why the stated tax capital line is negative — but not the $1,760,000 gap.** $1.2M of 2024
   mortgage proceeds went to her personally, and money that leaves an entity pushes a capital account down. But a
   distribution out of a disregarded entity changes neither the inside basis of the assets nor the
   assets-minus-liabilities figure, so it cannot close the gap at either end of it (§6(b)). That item stays open; the
   client cannot resolve it, so all precise outside-basis figures in this opinion are presented as the two readings
   (A: $3,280,000; B: $1,520,000) rather than forced to one number.
2. **It is a separateness problem.** Entity borrowing proceeds parked in a personal brokerage account is the same
   pattern the §7872 material calls commingling that "undermines separate-entity liability protection." Do not pay
   entity expenses from that account, do not relend the money to the entities without documents, and keep the
   account's ownership clear in writing. (`irc_7872_afr.md`)
3. **It gives her the cheapest fix: equity, not paper debt.** If she has the cash, the right move after an exit is to
   fund the businesses with **capital contributions** rather than new notes, and to retire the Properties mortgage
   with a contribution to Properties rather than another loan.

**Retiring the mortgage after the exit — arithmetic.** Her outside basis after a cash contribution of $1,900,000 to
Properties/Holdings would be $5,161,000 (Reading A) or $3,401,000 (Reading B). Retiring the debt shifts her whole
share of it away: on the partnership branch, a §752(b) deemed distribution of **$1,881,000** (99% × $1,900,000).
`max(0, 1,881,000 − 5,161,000) = $0`, and `max(0, 1,881,000 − 3,401,000) = $0`. **No §731(a) gain on either reading**
(§752(b) and §731(a) in `irc_721_and_752.md`).

On the disregarded branch (§8.2's likely answer — Holdings has one owner) §752 and §731 do not apply to her at all, so
there is no deemed distribution to test: she contributes cash, the mortgage is paid off, her basis in the underlying
business rises by the cash and falls by nothing taxable. Same answer — **no gain** — by a shorter route. Either way,
once the mortgage is gone the §752 trap in this structure is gone permanently.

**Two cautions on that plan:**

- **Do not fund the paydown by selling a building.** `properties_balance_sheet.md` shows **$1,120,000** of accumulated
  depreciation; a disposition puts that recapture and the remaining gain in issue, and the library contains **no**
  depreciation-recapture authority. **[UNVERIFIED]** — quantify with the CPA before choosing a funding path.
- **Do not do another leveraged distribution.** Negative tax capital plus debt-funded distributions is what makes the
  §731 trap live. Under the pessimistic basis reading the breakpoint is stark:

```
§752(b) deemed distribution from transferring g of the Holdings interests = g × $1,900,000

  transferred        shifted      gain, Reading A      gain, Reading B
      1%             $19,000            $0                    $0
     30%            $570,000            $0                    $0
     50%            $950,000            $0                    $0
   ~79%           $1,501,000            $0                    $0   ← Reading B basis is $1,501,000
     99%          $1,881,000            $0              $380,000   ← equals her negative tax capital
```

  On Reading A (basis $3,261,000 after contribution) no realistic transfer produces gain. On Reading B
  (basis $1,501,000) a gift of substantially all of Holdings to an irrevocable trust or family would generate about
  **$380,000** of §731(a) gain — precisely the amount by which her capital account is negative. **[UNVERIFIED]**
  *this illustration ignores gift-tax and capital-account mechanics outside the library; it is shown to size the risk,
  not to recommend a transfer.* This is why the unresolved $1,760,000 reconciliation gap is worth real money, and why
  the §752 arithmetic must be re-run before any transfer of Holdings interests.
