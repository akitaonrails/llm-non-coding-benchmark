# Opinion — Proposed Oakline Holdings restructuring (Nadia Oakline)

Prepared from the client file (`documents/`) and the closed reference library (`library/INDEX.md`).
Every citation below is to a library file. Where I believe a point of law matters but the rule is
**not in the library**, I say so and label it **UNVERIFIED — not in library**; I do not cite it as authority.

**Headline:** the plan is built on one false premise ("no tax event — it's all a §721 contribution")
and one catastrophic step (contributing the Helio Grid stock). Two of the four steps should be modified
and the Helio contribution should be dropped entirely. Done correctly, a holding structure is workable;
as proposed it destroys a ~$9.39M tax-free exit and recharacterizes the "interest-free" intercompany
lending each year.

---

## 1. Step-by-step analysis

### Step 1 — Form Oakline Holdings LLC (Wyoming; taxed as a partnership; Nadia 99%, her revocable trust 1%)

**Tax consequence.** None from formation itself. But the Wyoming situs buys almost nothing: an entity
formed in Wyoming but *managed from Colorado* has Colorado nexus via commercial domicile and must file
in Colorado; holding interests in LLCs doing business in Colorado "does not avoid Colorado filing for
income flowing through." Wyoming adds only a no-income-tax state plus an annual report fee.
*Authority:* `library/state_nexus_summary.md` (practitioner summary).

**Two further concerns.**

- *Is it even a partnership?* The plan's partnership status rests on the 1% grantor-trust member.
  Whether a revocable (grantor) trust whose deemed owner is the 99% member counts as a second owner,
  and whether the arrangement is a partnership for federal tax purposes, turns on the grantor-trust
  and partnership-classification rules, which are **not in the library — UNVERIFIED**. The whole
  structure (and the §752 analysis in Step 2) hangs on this; it must be confirmed before relying on it.
- *Estate-planning claim.* Placing interests in an LLC can help with gifting/transfer mechanics, but the
  library contains nothing supporting a substantive estate-tax benefit; the revocable trust is already
  the estate-planning vehicle. Treat "estate planning" as an administrative benefit, not a tax one.

**Verdict: Do it only in modified form.** If a holding entity is wanted, expect to file in Colorado
anyway; Wyoming vs. Colorado is a non-tax choice. Resolve the grantor-trust/partnership question first.

### Step 2 — Contribute all four interests to Holdings for membership interests

**General rule.** No gain or loss on contribution of property to a partnership in exchange for a
partnership interest. *Authority:* §721(a), `library/irc_721_and_752.md`. So the advisor is *partly*
right — for Oakline Services LLC and Oakline Digital LLC (positive or modest bases, no debt shifts),
a contribution is generally tax-free.

**But the blanket claim "no tax event" is wrong, for two reasons.**

**(a) Oakline Properties LLC has negative tax capital and a $1.9M nonrecourse mortgage.**
A decrease in a partner's share of partnership liabilities is treated as a distribution of money
(§752(b)), and a distribution of money in excess of the partner's basis is gain (§731(a)).
*Authority:* §752(b), §731(a), `library/irc_721_and_752.md`. Contributing Properties shifts **1% of the
mortgage to the 1% trust partner**: 1% × $1,900,000 = **$19,000 deemed distribution**. Nadia's outside
basis in Properties is tax capital −$380,000 + her 100% share of the $1.9M liability = **$1,520,000**,
which exceeds the $19,000 deemed distribution, so **no §731(a) gain results on these numbers**
(see `numbers.json`). The advisor's conclusion survives here only by accident of the 99/1 split —
with a meaningfully smaller outside basis or a wider minority split it would not. Also open, and
**not in the library — UNVERIFIED**: allocation of nonrecourse-liability shares among partners
(we follow the library's stated "1% of the mortgage shifts" consequence), and any built-in-gain
allocation rules for the contributed buildings.

*Separate check (not part of the proposal, done because the file flagged it):* the 2024 distribution
of $1.2M of refinancing proceeds was **not** a §731(a) gain event — basis at distribution ≈
(-$380,000 + $1,200,000 distributed) + $1,900,000 liability = $2,720,000 > $1,200,000. Shown in `numbers.json`.

*Reconciliation note (does not reconcile — flagged, not forced):* the stated tax capital does not tie
to the balance sheet's own asset side: 3,400,000 − 1,120,000 + 600,000 + 400,000 = 3,280,000, less the
1,900,000 mortgage, implies capital **+$1,380,000**, yet stated tax capital is **−$380,000** — a
**$1,760,000 gap** the file does not explain (plausibly tax depreciation exceeding the $1,120,000
shown, or unshown tax items; depreciation rules are not in the library — UNVERIFIED). We do not force
the numbers to fit. The $0-gain conclusion above survives either reading: outside basis is $1,520,000
as stated or $3,280,000 on the asset-side reading, and both dwarf the $19,000 deemed distribution. The
gap goes to the return preparer (QUESTIONS.md R7); it also suggests the buildings' true tax basis is
lower than the sheet implies, which matters for future depreciation and any eventual sale.

**(b) The Helio Grid stock contribution is the one step that must not be done (see §3 below).**

**Verdict: Do, in part.** Contributing Services, Properties and Digital is workable with the §752/§731
computation documented (result: $0 gain as of the 12/31/2025 balance sheet). **Exclude Helio.**

### Step 3 — Holdings makes interest-free loans among subsidiaries; "one bank account, one set of books"

**Tax consequence.** Interest-free loans between related entities are recharacterized under §7872:
the lender is treated as receiving imputed interest at the AFR and the borrower as paying it, with a
corresponding distribution/contribution between commonly owned entities. *Authority:* §7872 and the
engagement AFRs in `library/irc_7872_afr.md`. On the current balances, at the mid-term AFR of 4.12%:
- Properties → Services, $400,000 × 4.12% = **$16,480/yr** imputed
- Services → Digital, $150,000 × 4.12% = **$6,180/yr** imputed
(Short-term-AFR sensitivity at 3.96%: $15,840 / $5,940 — see `numbers.json` assumptions.) Between
commonly-owned entities the income/expense largely nets at Nadia's level, but the recharacterization
is mandatory, applies to **past open years** as well (the loans date from 2024-03-01, 2025-06-15,
2025-09-01 with "none"/"email only" documentation), and mischaracterizes where income and losses sit
(e.g., Digital's losses vs. Services' operating income) for every year it continues.

*One classification nuance the library does not address:* all three LLCs are single-member entities
disregarded as separate from Nadia, so their internal transfers arguably are not "loans" between two
parties at all; disregarded-entity classification is **not in the library — UNVERIFIED**. The
library's directive governs the file's facts ("interest-free or below-market loans between related
entities are recharacterized"), and the liability-shield point below does not depend on it either way.

**Non-tax consequence — this is the worst clause in the proposal.** The library states directly that
loans without notes, interest or repayment terms are evidence of commingling that **undermines
separate-entity liability protection (veil piercing)**, and *Court Holding*/*Gregory* teach that
formally separate steps without substance are collapsed — consequences follow substance.
*Authorities:* `library/irc_7872_afr.md`; `library/step_transaction.md`. "One bank account, one set
of books" would **defeat the very liability-protection benefit the advisor lists as a payoff**: with
one bank account and one set of books, every creditor of any entity can pursue the whole group as a
single enterprise — the HVAC business's 42-employee premises/worker exposure would reach Properties'
real estate, and Properties' mortgage risk would reach Services' operating cash. (Helio Grid is
outside this problem entirely — it is never coming into the holding; see §3.)

**Verdict: Do not do.** No interest-free internal lending; no commingling. If the group wants internal
financing, do it as real loans — see the remediation plan in §4.

### Step 4 — Holdings files one return; "no tax event — it's all a §721 contribution"

**Consequence.** The "one return" slogan is misleading and the "no tax event" claim is refuted above
(§752/§731 mechanics; §7872 imputation). And no partnership-level shelter exists for the big asset:
Helio Grid is a **C corporation** and is separately taxed and files its own return — a rule so basic the
library does not bother to state it, so strictly speaking **UNVERIFIED — not in library**, though the
library's §1202 excerpts repeatedly presuppose C-corporation-level existence. Whatever Holdings files,
Helio's corporate return, the stock, and any dividends remain entirely outside it.

**Verdict: Do, in modified form** — Holdings (if formed) files one partnership return for the
contributed Colorado businesses, with Colorado (commercial-domicile) filings; this is an
administrative simplification, not tax avoidance.

---

## 2. Revised step plan

1. **Fix the paper first (this quarter).** Document or clean up the three intercompany loans per §4.
   This is independent of the restructuring and is currently generating §7872 exposure and
   veil-piercing evidence every month it stays undocumented.
2. **Form the holding entity — but as a single-member, disregarded Colorado holding LLC** (100% Nadia;
   use the existing revocable trust for *transfer-on-death/estate* mechanics at the membership-interest
   level, not as a 1% partner). A single member means: no partnership return, no §752/§731 debt-shift
   math at contribution, no grantor-trust/partnership-classification risk. *Caveat, UNVERIFIED — not
   in the library:* classification of a single-member LLC as disregarded, and the treatment of a
   disregarded entity holding LLC interests, are not library-covered; confirm with a CPA/lawyer.
   If Nadia genuinely wants gifting of minority LP interests now (creating a real partnership),
   re-run the §752 computation above with the actual split before any contribution.
3. **Contribute Oakline Services, Oakline Properties, Oakline Digital** to the holding LLC.
   §721(a) applies (to the extent a partnership is formed at all); on the 12/31/2025 numbers the
   §752(b)/§731(a) computation yields **$0 gain** even under the 99/1 plan; under a single-member
   holding LLC no liability share shifts away from Nadia at all. Keep the entities' books, bank
   accounts and records **separate** inside the structure.
4. **Do NOT contribute the Helio Grid stock** — keep it titled in Nadia's own name (see §3).
5. **File where the law requires:** the businesses keep their Colorado filings; the holding entity files
   in Colorado by commercial domicile; Wyoming adds nothing (skip it, or if formed for asset-protection
   reasons, expect full Colorado filing anyway). *Authority:* `library/state_nexus_summary.md`.
6. **Internal funding policy in place of "one bank account":** real notes at ≥ AFR, real interest
   payments, or capitalization (see §4).

## 3. The Helio Grid stock — what to do, and never do

**Why it is special.** Nadia bought 3,000,000 shares at $0.004 ($12,000) on **2020-02-18**, in an
original issuance directly from the company, for cash, from a domestic C corporation represented to
have ≤ $1M gross assets and an active qualified trade or business (Common Stock Purchase Agreement,
§2.3, and recitals). That is the fact pattern §1202(c)(1) rewards: stock **originally issued** and
acquired **at original issue** for money, from a qualified small business. *Authority:*
`library/irc_1202_excerpt.md`; `documents/helio_grid_stock_purchase_agreement_excerpt.pdf`.
Held more than five years (Feb 2020 → any sale from Feb 2025 onward) for stock acquired after
Sept. 27, 2010 → **100% exclusion**, subject to the per-issuer cap of the greater of $10M or 10× basis
(here $10M > $120,000). Current value ≈ $9.4M, basis $12,000 → gain ≈ **$9,388,000 < $10,000,000**:
**on a direct sale, the entire gain should be federally tax-free.**

**What NOT to do:**

- **Never contribute the Helio stock to Oakline Holdings (or any partnership).** Under §1202(h), the
  transfers that preserve the transferor's acquisition status are gift, death, and partnership
  *distributions to* a partner — **"a contribution of stock to a partnership is not among the listed
  transfers; the partnership did not acquire the stock at original issue, and the stock ceases to
  qualify in its hands."** *Authority:* `library/irc_1202_excerpt.md` (§1202(h), citing §1202(h)(2) and
  Treas. Reg. §1.1202-2 (proposed)). One signature converts up to **$9,388,000 of excludable gain into
  fully taxable gain.** The advisor's advertised benefit — "the gain lands in the holding so you can
  reinvest without tax" — is wrong twice over: the exclusion dies on contribution, and even inside a
  partnership there is no "reinvest without tax" mechanic — a partnership's sale passes gain out to
  the partners in the year of sale regardless of what they do with the cash (the general pass-through
  timing rule is not itself stated in the library — UNVERIFIED, see the §6 flag). And what flows
  through carries no §1202 benefit: §1202(g) conditions a partner's share of the exclusion on having
  held the partnership interest when the partnership acquired the QSBS and at all times thereafter —
  and contributed stock never becomes qualified stock in the partnership's hands at all (§1202(h)).
  *Authority:* `library/irc_1202_excerpt.md`.
- **Do not sell any tranche before modeling the cap** — now urgent: with a live exit at $9–10M and a
  shared $10M per-issuer cap, **any prior Helio sale/exchange/redemption you've had reduces the cap**
  and headroom at $10M is only $12,000 (QUESTIONS.md R2, unanswered).
- **Do not let a well-meaning estate planner "move it into the trust" without analysis.** §1202(h)
  *does* preserve tacked treatment for acquisitions **by gift or at death**, so transfers by gift/bequest
  to the trust or heirs are the safe family-transfer route; a contribution to an entity taxed as a
  partnership is not. *Authority:* `library/irc_1202_excerpt.md`. (How the $10M per-issuer cap is
  shared among donees is **not in the library — UNVERIFIED** — plan gifts with an adviser.)

**What TO do:**

- Keep the stock in Nadia's own name until an exit; the QSBS clock and "original issue" status are
  already perfect and self-maintaining.
- Preserve the §1202 evidence file: the Feb 2020 purchase agreement (original issuance, ≤$1M gross
  assets representation), proof of the $12,000 payment, and the March 2, 2020 83(b) filing.
  *Authority for reliance on issuance facts:* `library/irc_1202_excerpt.md` (§1202(c)(1)).
  (Whether Helio met the QSB *gross-assets test continuously* after issuance cannot be verified from
  the file — remaining unknowns listed in QUESTIONS.md; client has no additional information on this.)
- On exit, check the $10M per-issuer cap against the actual exit price: gain is excluded
  dollar-for-dollar up to the cap — fully excluded through a stake value of **$10,012,000**
  (gain $10,000,000 + the $12,000 basis), every dollar above taxable (see §5.1 and `numbers.json`).
  The >5-year hold is already satisfied; the 50/75/100% tiers apply only to post-July 4, 2025
  issuances, not this stock.
- Estate plan around it (gift/death transfers tack) rather than through it.

## 4. Intercompany-loan remediation (as amended by client response §5.3)

Current state (org chart + cash-flow file): **no notes, no interest, one "email only"**; dates
2024-03-01 ($250k), 2025-06-15 ($150k), 2025-09-01 ($150k). Exposure: §7872 imputation every year,
in both directions of characterization, plus veil-piercing evidence. *Authorities:*
`library/irc_7872_afr.md`; `library/step_transaction.md`.

Per loan, pick one of three clean-ups and execute within 60 days:

| Loan | Balance | Preferred fix | Alternative |
|---|---:|---|---|
| Properties → Services | $400,000 | Repay in full (Services is profitable, ~$1.1M/yr); if Properties needs support instead, **capitalize**: Services distributes/Properties contributes, retire the loan | Genuine note: term ≥ 3–9 yr, interest **≥ 4.12%** (mid-term AFR), amortizing schedule, actual payments booked |
| Services → Digital | $150,000 | **Capitalize** into Digital (it runs losses; debt it can't service invites recharacterization anyway) — treat as contribution to Digital's capital | Note at ≥ 4.12% with real payments only if Digital's plan shows capacity to pay |

For every option:
1. **Catch up §7872 for past years** — compute imputed interest from each loan date to the clean-up
   date (annual run-rate on current balances: $16,480 + $6,180 = $22,660/yr at 4.12%; see
   `numbers.json`), book the offsetting interest income/expense and contribution/distribution, and
   assess whether amended returns or an accounting-method change agreement is needed — a tax-return
   detail **outside the library's scope; flag to the CPA**.
2. **Separate bank accounts and books per entity, permanently.** No "one bank account" at any point.
3. **Adopt a written treasury policy**: intercompany funding only via documented notes at ≥ then-current
   AFR (§7872), with board/member consent minutes — see `agreements_required.md`.

## 5. Client-response update (turn 2) — what changed

Client answers: (i) Helio is talking to acquirers, exit in **12–18 months**, stake ≈ **$9–10M**;
(ii) the 1% member is her **revocable living trust** ("advisor said we need two partners");
(iii) intercompany transfers will stay undocumented — "no paperwork, I just move money where it's needed."

### 5.1 Exit timing makes the "never contribute the Helio stock" advice time-critical

- **Holding period is safe.** Acquired 2020-02-18; a sale in 12–18 months (late 2027 → mid-2028) means
  ~7–8 years of holding — comfortably past the >5-year / 100% tier for post-Sept-27-2010 acquisitions.
  *Authority:* §1202(a), `library/irc_1202_excerpt.md`.
- **The $9–10M stake sits exactly on the per-issuer cap cliff.** Cap = greater of $10M or 10× basis
  ($120,000) = $10M. Excludable gain runs dollar-for-dollar until stake value **$10,012,000**
  (gain = value − $12,000 = $10M); at a $9.4M stake, headroom to the cap is only **$612,000**, and at
  a $10M stake, **$12,000**. Above the breakpoint the excess is not excluded (e.g., $10.5M stake →
  $488,000 taxable). *Authority:* §1202(a) cap language, `library/irc_1202_excerpt.md`; table in
  `numbers.json` assumptions.
- **Action points created by the live deal:**
  1. The shares must still be titled in **Nadia's own name at closing**. Any "while we're at it"
     retitling into Holdings before closing forfeits the entire exclusion on whatever does sell
     (§1202(h), `library/irc_1202_excerpt.md`). Freeze Step 2 for Helio permanently.
  2. **Any prior Helio sale/exchange/redemption eats the same $10M cap** — the unanswered question
     (QUESTIONS.md R2) is now high-stakes, not clerical, because headroom at $10M is $12,000.
  3. **Deal structure matters, and the library cannot adjudicate it:** whether a stock sale, a
     merger cashing out her shares, or an asset sale by Helio all yield §1202 gain is reorganization/
     recast question — **UNVERIFIED — nothing on reorganization mechanics is in the library**. Before
     signing a letter of intent, have a CPA/attorney confirm the structure preserves *her sale of
     stock*; asset-sale structures in C corps are the classic QSBS killer and are outside what this
     library lets me certify.
  4. Estate-gift planning for any expected over-cap proceeds (gifts before closing tack under
     §1202(h) gift/death rules — donees' caps interplay is **not in the library — UNVERIFIED**).

### 5.2 The trust answer settles the Step 1 question — in favor of the revised plan

The advisor's "we need two partners" is a premise, not a law: you only need two partners **if you
insist on a partnership**. A **single-member holding LLC** (100% Nadia, revocable trust reaching the
interest via death-transfer mechanics) avoids the question entirely. The trust being *hers* also
means: even in the 99/1 plan, the grantor-trust rules (not in the library — **UNVERIFIED**) likely
disregard the 1% entirely, so the "two partners" may create filing complexity without buying
substance. **Final recommendation unchanged and now firm: single-member holding LLC; Helio stays
outside it, in her own name.**

### 5.3 "No paperwork — I just move money where it's needed" — the law does not take client preferences

The client's stated practice does not change any consequence; it entrenches them. Under the library:
- Every transfer stays a §7872 below-market loan recharacterization ($22,660/yr run-rate on current
  balances; grows with every new transfer), for past and future years alike.
  *Authority:* `library/irc_7872_afr.md`.
- "No notes, no interest, no repayment terms" is the library's *verbatim* description of evidence
  undermining separate-entity protection, and *Court Holding*/*Gregory* collapse substance-over-form
  arrangements. With 42 employees at Services and two buildings at Properties, an uninsured
  veil-piercing event (an HVAC claim reaching Properties' real estate, or Holdings' plan making all
  entities one business) dwarfs the interest math. *Authorities:* `library/irc_7872_afr.md`;
  `library/step_transaction.md`.

**Minimum-viable path if she won't do notes** (presented as the floor, not the advice of preference):
at each year-end, sweep intercompany balances to zero — Services **repays** Properties what it can,
the rest is re-documented once as **contributions to capital** (Digital's $150k especially: it runs
losses and cannot service debt). A capital contribution is not a loan, so §7872 has nothing to
recharacterize going forward, and books show equity, not commingling. This is one form per event, not
a loan program. Full documentation remains the recommendation; zero transfers is the other clean
option.

## 6. Addendum (turn 3) — "the holding is how you avoid tax when Helio sells; the gain lands in the LLC." Who is right?

**The advisor is wrong on both halves of the claim.**

**(a) Contributing the stock before the sale does not defer or shelter the gain — it forfeits the shelter
you already have.** There is no mechanic by which "the gain lands in the LLC" untaxed:

- The library's own §1202 language describes gain from stock held by a partnership as *flowing out to
  the partners* (§1202(g)) — an LLC taxed as a partnership is not a container that keeps gain inside it.
  Whatever an LLC earns, the members are taxed on it in the year the LLC realizes it. The library states
  the QSBS flow-through instance of this; the general partnership pass-through principle itself is
  **UNVERIFIED — not separately stated in the library**. Either way, "park it in the LLC and reinvest
  without tax" has no support in anything in the library.
- Worse, the contribution *destroys* the exclusion you actually have. §1202(h) lists gift, death, and
  partnership distributions **to** a partner as transfers that preserve tacked treatment — a
  **contribution to a partnership is not among them**, the partnership never "acquired at original
  issue" (§1202(c)(1)), and the stock **ceases to qualify in its hands**
  (`library/irc_1202_excerpt.md`). Sold-from-inside-Holdings = fully taxable gain.

| Exit stake | Gain: stock sold **by Nadia** (this plan) → taxable | Gain: stock contributed then sold → taxable |
|---|---:|---:|
| $9.0M | $8,988,000 gain → **$0** (100% excluded, under cap) | **$8,988,000** |
| $9.4M | $9,388,000 gain → **$0** | **$9,388,000** |
| $10.0M | $9,988,000 gain → **$0** (cap headroom $12,000) | **$9,988,000** |

(Rates are not in the library, so the tax *dollars* forfeited cannot be computed here; the taxable-gain
spread is the whole story.) The irony worth saying out loud: **if the exclusion works, there is nothing
to defer** — the gain is never taxed in the first place. The advisor is selling a solution to a problem
his own step 2 creates.

**(b) Can the holding own "it" after the sale? Yes — but note what "it" becomes.**

- **After the sale there is no Helio stock anymore** — there is cash. That cash can be contributed to
  the holding LLC freely: a contribution of money for a partnership interest is a non-event under
  §721(a) (`library/irc_721_and_752.md`), and under the recommended single-member holding it is just a
  transfer between Nadia's own pockets. **Order matters, and the library is explicit about order:**
  §1202(h) makes the contribution-before-sale sequence the poison step, and *Court Holding*/*Gregory*
  collapse formally separate steps engineered toward one end
  (`library/step_transaction.md`). So: **no pre-closing, at-closing, or "days before the wires clear"
  racing of the clock.** Sell in Nadia's own name → proceeds land in Nadia's account → *then* move the
  cash into the holding whenever she likes. A genuinely later, unconditional cash contribution is a
  separate transaction; a contribution sequenced backwards poisons the sale.
- What the holding cannot do, before or after, is **defer the tax that the sale itself triggers**.
  Where cash sits after a sale does not change who was taxed on the sale.
- **Genuinely open deferral question, flagged UNVERIFIED — not in the library:** there are reported
  rollover regimes for QSBS gains (e.g., reinvestment into another qualified small business within a
  short window) that could matter for any gain **above the $10M cap** (R2/R3). Nothing in the closed
  library covers them, so I neither cite nor rely on them — raise with the CPA before the LOI if the
  expected price will exceed ~$10.012M. No rollover regime, if one exists, runs through "put it in my
  family holding LLC."

**Bottom line for Nadia:** the advisor gets it backwards twice. Before the sale, moving Helio into the
holding converts up to ~$9.99M of *tax-free* gain into *taxable* gain. After the sale, the holding can
absolutely own the proceeds — it just has nothing to save, because the exclusion (or the tax) was
already fixed by who held the stock at closing. Hold personally through closing; contribute cash after.


## 7. Assumptions and open items (stated prominently)
- **AFR tenor assumed mid-term (4.12%).** The loans have no stated term; the library's engagement AFR
  presents 4.12% for 3–9 years. If the loans are properly characterized as ≤ 3-yr demand/short-term,
  use 3.96%: imputed interest becomes $15,840 and $5,940. This is an assumption, not a verified fact.
- **§1202 relies on the company's Feb 2020 representations** (≤$1M gross assets at issuance, domestic
  C corp, active qualified trade or business, original issuance) and on Helio having remained a
  qualified small business — post-issuance QSB status is not in the file and the client cannot supply
  it (QUESTIONS.md R1).
- **QSBS gain uses the 409A value ≈ $9.4M as a value proxy** for an exit; actual gain will differ.
  The federal capital-gains *rates* are not in the library, so no tax-dollar figure is computed here.
- The revocable trust is assumed to be a **grantor trust deemed owned by Nadia**; classification
  rules are not in the library (UNVERIFIED).
- Outside basis in Properties is taken as capital + liabilities (−$380,000 + $1,900,000 = $1,520,000)
  per the library's own stated consequence framing. Other basis items could cut either way, but the
  deemed distribution is only $19,000 — a ~$1.5M cushion — so the $0 result is insensitive to them
  on any plausible reading of the file.
- **The Properties balance sheet does not internally reconcile — flagged, left unresolved.** Asset
  side 3,400,000 − 1,120,000 + 600,000 + 400,000 = 3,280,000; less the $1,900,000 mortgage implies
  capital **+$1,380,000**, yet stated tax capital is **−$380,000** — an unexplained **$1,760,000**
  gap (plausibly tax depreciation beyond the $1,120,000 shown, or unshown tax items; depreciation and
  recapture rules are not in the library — UNVERIFIED). The $0-gain conclusion holds under either
  reading (outside basis $1,520,000 as stated, or $3,280,000 on the asset-side reading). The
  preparer's tax-basis ledger is requested before any contribution or building sale (QUESTIONS.md
  R7; see the reconciliation note at Step 2(a)).
- Helio transfer restrictions: the excerpt provided contains **no** transfer/ROFR clause; a stockholders
  agreement almost certainly exists — not in the file (remaining unknowns in QUESTIONS.md; client has
  no additional information). We did not assume one; our advice — keep the stock in your own name
  through the exit — is indifferent to transfer restrictions, but the *deal itself* will surface them.
