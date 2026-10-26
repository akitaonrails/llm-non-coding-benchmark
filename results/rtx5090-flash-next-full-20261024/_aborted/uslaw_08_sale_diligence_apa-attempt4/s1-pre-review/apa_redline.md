# APA redline — Lone Star Millwork Holdings LLC draft, key sections

Client: Ray Brightline / Brightline Cabinetry LLC (seller). All legal citations are to files listed in
`library/INDEX.md`; anything not in that library is flagged **[unverified — not in library]**. Facts are
from the data room extract and the client's answers (2026-10-25); assumptions are flagged where used.

Deal size used throughout, derived from the draft itself because no price is stated anywhere in the file:
`9.3 Escrow. $310,000 (10%)` → **Purchase Price = 310,000 ÷ 0.10 = $3,100,000.**
General cap §7.4(b) = 10% × 3,100,000 = **$310,000**. Escrow = **$310,000** (1.0× the general cap).
This derivation is an assumption (Q1 in `QUESTIONS.md`); every cap number below moves with it.

| § | Verdict | One-line reason |
|---|---|---|
| 2.4 | **CHANGE (heavy)** | Buyer computes EBITDA under its own policies; the max needs $1.7M EBITDA (2.30× the adjusted 2025 figure) and the period is the 12 months after Closing, not calendar 2026 |
| 3.3 | **CHANGE** | Schedule 3.3 "None." is false on the data room's face; consents are efforts-only with no closing condition; add carve-out fallback |
| 4.12 | **CHANGE (schedule it)** | Rep is untrue on the seller's own data room facts, and the OT layer is now confirmed by the client, not hypothetical |
| 7.4(a) | **KEEP** | Deductible basket is seller-favorable; guard it against carve-outs |
| 7.4(b) | **CHANGE** | §4.12 carved to full-price cap — off-market per the library; restore the cap or trade a sized special indemnity |
| 7.4(c) | **CHANGE (flip or delete)** | Pro-sandbagging + clean 4.12 = agreed indemnity for the known classification issue |
| 7.4(d) | **TUNE** | Survival itself is market; the escrow-release/collection tail is the problem |
| 8.2 | **CHANGE (narrow)** | 7 years / 500 miles is likely overbroad for a local shop; client's "I'll sign anything" is not a reason to accept it |
| 9.3 | **KEEP (conform)** | Amount/term fine; escrow must be sole recourse for capped claims, tranching if 4.12 is separately sized |

---

## §2.4 Earn-Out — **CHANGE (heavy)**

**As drafted:** "In addition to the Closing Payment, Buyer shall pay Seller an amount equal to 40% of the
amount by which EBITDA of the Business for the twelve months following Closing exceeds $700,000, up to a
maximum of $400,000. 'EBITDA' shall mean earnings before interest, taxes, depreciation and amortization of
the Business as determined by Buyer in good faith in accordance with Buyer's accounting policies,
consistently applied."

**Arithmetic first — treat this earn-out as nearly worthless:**

- Maximum payout requires EBITDA of $700,000 + $400,000 ÷ 0.40 = **$1,700,000** —
  vs 2025 seller-prepared EBITDA $740,000 → 1,700,000 ÷ 740,000 = **2.30×** the adjusted figure. Unreachable.
- **Assumption, flagged:** the measurement period is "the twelve months following Closing." The closing date
  is not in the file, so 2025 actuals are used as a proxy throughout; this is a proxy, not a fact.
- Proxy, flat performance (adjusted): 0.40 × (740,000 − 700,000) = **$16,000**.
- Proxy, flat performance (unadjusted — buyer may disallow the $180,000 owner-salary and $42,000 "one-time"
  legal add-backs, data room §6.1): 740,000 − 180,000 − 42,000 = $518,000, below the floor → **$0**.
- If Hensley is lost (see §3.3): remaining EBITDA is $740,000 − $281,200 = **$458,800** (adjusted basis) or
  $518,000 − $196,840 = **$321,160** (unadjusted basis). Both are under $700,000 → earn-out **$0**.
  (Hensley EBITDA share: 0.38 × $4,600,000 = $1,748,000 revenue; × adjusted margin 740,000/4,600,000 = 16.09%
  → $281,200; × unadjusted margin 518,000/4,600,000 = 11.26% → $196,840.)

So plan on **$0–$16,000**, not $400,000. Do not give the earn-out value in allocation (Q6) or let it inflate
"total consideration" when caps are negotiated (Q1: check whether the defined "Purchase Price" includes it).

**Why the drafting is dangerous.** The library is squarely on point: an earn-out measured by "EBITDA as
determined by Buyer under Buyer's policies" lets the buyer allocate overhead, management fees, integration
costs and purchase-accounting adjustments against the target, zeroing the earn-out
(`library/earnout_definitions.md`; *Lazard Technology Partners v. Qinetiq*, 114 A.3d 193 (Del. 2015)). The
same memo lists the standard seller protections; the draft has none of them.

**Replacement language (core):**

> 2.4 Earn-Out. In addition to the Closing Payment, Buyer shall pay Seller an amount equal to 40% of the
> amount by which Adjusted EBITDA of the Business for the twelve (12) months following Closing exceeds
> $700,000, up to a maximum of $400,000. "Adjusted EBITDA" means EBITDA of the Business determined in
> accordance with the accounting principles, practices and policies used by Seller in preparing the
> Historical Financial Statements, consistently applied, excluding: (i) allocations of Buyer overhead,
> management or monitoring fees; (ii) transaction, integration and restructuring costs; and
> (iii) purchase-accounting adjustments and non-cash charges. The parties agree the add-backs on Schedule
> 2.4 (owner compensation of $180,000 and non-recurring legal fees of $42,000) are included. Buyer shall
> operate the Business after Closing in the ordinary course and shall not take any action with the purpose
> of avoiding or reducing the Earn-Out. Seller shall have information and audit rights, and disputes on
> Adjusted EBITDA shall be resolved by an independent accounting firm acting as expert, not arbitrator.
> The Earn-Out accelerates on a sale of the Business.

Bracketed for CPA work: the agreed add-back schedule (Schedule 2.4) must survive diligence; the seller's
own $740,000 is "seller-prepared" (data room §6.1) and is not audit-proof.

---

## §3.3 Required Consents — **CHANGE (schedule it; add a condition and a fallback)**

**As drafted:** "Seller shall use commercially reasonable efforts to obtain the consents listed on
Schedule 3.3 prior to Closing. (Schedule 3.3, as drafted by Buyer: 'None.')"

**"None." is false on the face of the data room.** Schedule 3.3 as we require it:

| # | Contract | Data room | Issue | Treatment |
|---|---|---|---|---|
| 1 | Hensley Homes Master Supply Agreement, 2024–2028, 38% of revenue | §1.1 | §18: assignment barred "by operation of law, merger, sale of assets, change of control or otherwise" without prior written consent, "withheld in its sole discretion"; purported assignment "void" | **Consent required — closing condition** (see (d)/(e) below) |
| 2 | Cascade Builders framework agreement, 11% of revenue | §1.2 | Assignment permitted to a successor to substantially all assets **upon notice** | Notice item, not consent; pre-closing notice obligation |
| 3 | 22 residential contracts, each under $40,000 | §1.3 | Silent on assignment | Assignable per the library default; list on Schedule 3.1(c); Q8 asks whether any is personal-services |
| 4 | Shop lease, 7700 Burleson Rd, through 2029 | §3.1 | §22: landlord consent required, "not unreasonably withheld" | Consent item; reasonableness standard; start now |

The library enforces the Hensley clause as written: a clause barring assignment "by operation of law,
merger, sale of assets, change of control or otherwise" is enforced according to its terms; the asset sale
transfer without consent is a breach and the transfer is **void** where the clause so provides; "sole
discretion" gives the counterparty leverage to renegotiate price
(`library/anti_assignment_change_of_control.md`: *SQL Solutions v. Oracle*, 1991 WL 626458 (N.D. Cal.);
Restatement (Second) of Contracts §317, §322).

**Value at stake (arithmetic shown):** 0.38 × $4,600,000 = $1,748,000 of revenue. Margin-consistent value:
$1,748,000 × 16.09% (adjusted margin) = $281,200 EBITDA × 4.19× (3,100,000 ÷ 740,000) = **$1,178,000**.
Cross-check on the unadjusted basis: $1,748,000 × 11.26% = $196,840 × 5.98× (3,100,000 ÷ 518,000) =
**$1,178,000**. Both bases converge — use ~$1.18M as the anchor for any carve-out repricing.

**Client status (answered 2026-10-25), and how it shapes the redline:** the consent has **not** been sought;
Hensley has not been told about the sale; the client and Hensley's owner have a long personal relationship
and the client expects a poor reaction to a corporate buyer. Sequencing consequence: the first approach must
be client-to-owner, before any formal letter or buyer contact. The redline therefore (i) keeps the consent
obligation on a seller-led, jointly-agreed script, and (ii) hard-codes a fallback so a hostile answer
cannot blow up the closing. Do **not** volunteer the client's expectation about Hensley's receptivity to
buyer's counsel (see `reply_to_buyer_counsel.md` — status only, no psychology).

**Replacement language:**

> 3.3 Required Consents. (a) Seller shall use commercially reasonable efforts to obtain the consents, and
> give the notices, listed on Schedule 3.3 prior to Closing. (b) The following are Required Consents and
> their receipt (or the fallback under clause (e)) is a condition to Closing: the written consent of
> Hensley Homes to assignment of the Master Supply Agreement (the "Hensley Consent"); and landlord consent
> under Section 22 of the lease of 7700 Burleson Rd (which may not be unreasonably withheld). (c) Seller
> shall give written notice of the Cascade Builders framework agreement assignment not later than the date
> required by that agreement. (d) Buyer shall reasonably cooperate with Seller in the consent process,
> including making Buyer's senior management available to the counterparty; neither party shall contact
> Hensley Homes regarding the transaction except as mutually agreed in writing. (e) If the Hensley Consent
> has not been obtained by the Outside Date, then, at Buyer's election: (i) Closing shall proceed, the
> Master Supply Agreement shall not be an Assigned Contract and shall not be a Purchased Asset, and the
> Purchase Price shall be reduced by the Carve-Out Adjustment of $[______] (the parties acknowledge the
> contract carries approximately $1,178,000 of value on the margin and multiple arithmetic set out in the
> disclosure memorandum, and the Carve-Out Adjustment is negotiated within $[500,000]–$[1,178,000]), with
> the §2.4 baseline reduced accordingly; or (ii) either party may terminate this Agreement if Buyer
> declines clause (e)(i). "Outside Date" means [______].

Drafting notes:

- The extract has **no closing-conditions article**, so the condition in (b) must be cross-referenced into
  whatever conditions article the full APA contains — flagged, not assumed.
- A holdback alternative was considered and is **disfavored**: it delays cash without resolving whether the
  buyer keeps the 38% customer; a price reduction is cleaner for the seller because it fixes the exposure at
  signing. If buyer insists on a holdback instead, cap it at the Carve-Out Adjustment and release on consent.
- For the 22 residential contracts the library default helps: absent anti-assignment language, assignment of
  rights is generally permitted; obligations need consent only if performance is personal
  (`anti_assignment_change_of_control.md`). Ceiling: 22 × $40,000 = $880,000 gross.

---

## §4.12 Employees and Contractors — **CHANGE (schedule the exception; do not sign a clean rep)**

**As drafted:** "Seller represents that all individuals providing services to the Business have been
properly classified as employees or independent contractors under applicable law and that Seller has
withheld and paid all required taxes."

**Why it is untrue on the seller's own file.** Data room §2.2: 9 installers on 1099, exclusive to
Brightline, Brightline trucks and tools, scheduled daily by the shop foreman, hourly $34–41, average 3.4
years, **no written contractor agreements**, $612,000 paid in 2025 (612,000 ÷ 9 = $68,000 per person). The
library: individuals who work exclusively for one business, on its schedule, with its tools and vehicles,
paid hourly, for years, are employees under the common-law control test regardless of the label
(`library/worker_classification_tx_irs.md`: IRS Rev. Rul. 87-41 (20 factors); Treas. Reg. §31.3121(d)-1).
The client's own email says "The installers have been 1099 forever, everyone in the industry does it" —
industry practice is not a defense under that test.

**The overtime layer is no longer hypothetical — the client confirmed the hours (2026-10-25): 45–50
hours/week in busy season, paid straight hourly.** The library lists exposure including "overtime under the
FLSA (hourly, >40 hrs)". The half-time premium computation (0.5 × rate × OT hours) is the standard
formulation but is **not spelled out in the library — [unverified; CPA must confirm]**.

Illustrative exposure — planning numbers, not advice. Assumptions, stated: 3-year lookback (the limitations
period is not in the library — Q10); FICA 7.65%; FUTA 0.6% on first $7,000/head after credit; the number of
busy-season **weeks** per year is unknown (client gave hours-per-busy-week) so three scenarios are run and
the 20-week case is the planning figure — **the week count is an assumption, not a found fact**.

| Component | Arithmetic | Per year | 3-year total |
|---|---|---|---|
| Employer FICA | 7.65% × $612,000 | $46,818 | $140,454 |
| FUTA | 9 × $7,000 × 0.6% | $378 | $1,134 |
| FLSA OT premium — 12 busy wks | (5–10 hrs/wk) × ($34–41) × 0.5 × 12 | $1,020–$2,460 | $3,060–$7,380 |
| FLSA OT premium — 20 busy wks | same, × 20 | $1,700–$4,100 | $5,100–$12,300 |
| FLSA OT premium — 26 busy wks | same, × 26 | $2,210–$5,330 | $6,630–$15,990 |
| **3-yr totals: 12 / 20 / 26 busy weeks** | FICA + FUTA + OT layer | — | **$144,648–$148,968 / $146,688–$153,888 / $148,218–$157,578** |

**Not included, and all additive:** TWC/state unemployment (cited in the library, rate not in it), §3509
income-tax gross-up (cited, rates not in it), penalties and interest, benefits eligibility and workers'
comp exposure (listed in the library, unquantified). A conservative gross-up — roughly doubling the tax
lines — still lands under ~$243,000 for the 26-week scenario. Even so, every scenario sits **inside the
$310,000 escrow**; the fight is not the size of the bill, it is the carve-out (see §7.4(b)) that converts a
~$145,000–$158,000 problem into a $3,100,000 one.

**Reconciliation — now closed.** The $68,000 average annual pay vs the confirmed 45–50 busy-week hours:
implied annual hours are 68,000 ÷ 41 = 1,659; ÷ 37.50 = 1,813; ÷ 34 = 2,000 → 33.2–50.0 hrs/wk over a
40–50-week working year. Consistent with strong seasonality: 45–50 in busy season, less the rest of the
year. The client's answer explains the data; nothing was forced.

**Client's "they like it" point:** worker satisfaction or consent is not in the library as a defense —
**[unverified — not in library]** — and this memo does not rely on it. Do not brief it to the buyer as a
defense.

**Replacement language:**

> 4.12 Employees and Contractors. Except as set forth on Schedule 4.12, Seller represents that all
> individuals providing services to the Business have been properly classified as employees or independent
> contractors under applicable law and that Seller has withheld and paid all required taxes. Schedule 4.12
> discloses: nine individuals engaged as independent contractors performing installation services (data
> room §2.2 facts: exclusive service, Company vehicles and tools, daily scheduling by Seller's foreman,
> hourly compensation of $34–$41 per hour, average engagement 3.4 years, no written contractor agreements,
> aggregate 2025 payments of $612,000); Seller does not represent that these individuals are properly
> classified.

That disclosure kills the rep's value to the buyer for this issue — which is why buyer will push back, and
why the paired fallback is:

**Fallback (if buyer refuses the exception):** keep the clean rep but (i) flip §7.4(c) to anti-sandbagging
and (ii) move §4.12 back inside the §7.4(b) cap, plus (iii) a single special indemnity:

> 7.5 Special Indemnity — Worker Classification. Notwithstanding §7.4, Seller shall indemnify Buyer for
> Losses arising from the classification of the individuals disclosed on Schedule 4.12 up to a maximum of
> $[250,000], and Buyer's sole recourse for such Losses shall be the Escrow.

Sizing, shown: 26-week scenario top $157,578; a ~50% gross-up for SUTA/§3509/penalties ≈ $236,000;
$[250,000] covers that with headroom; escrow-only recourse eliminates the tail. The $[250,000] is a
bracketed proposal, not a found fact. The library blesses exactly this trade: a specific operational rep
"carved out to a full-price cap is off-market and should be resisted or replaced with a sized special
indemnity" (`library/baskets_caps.md`); and the seller's protection against sandbagging is "an
anti-sandbagging clause, a disclosure schedule exception to the representation, or a special indemnity with
a negotiated cap — not a clean rep" (`library/sandbagging.md`).

**Buyer-side consequence to expect (and price):** the same library notes the buyer may inherit **FLSA
liability as a successor** where there is substantial continuity, and must reclassify going forward — the
buyer will argue this to keep the carve-out. It is a reason for the sized special indemnity, not for a
full-price cap.

---

## §7.4(a) Basket — **KEEP**

**As drafted:** "Seller shall have no liability under 7.1 until aggregate Losses exceed $75,000 (the
'Basket'), and then only for Losses in excess of the Basket [deductible]."

A **deductible**, not a tipping basket — the seller-favorable structure; the library draws the distinction
and this is the good side of it (`library/baskets_caps.md`). $75,000 ≈ 2.4% of the derived price
(75,000 ÷ 3,100,000), unremarkable. **Keep — and guard:** the real risk is buyer re-opening the basket by
carving claim types out of it ("no Basket for fraud, Fundamental Reps, §4.12 …"). Resist any Basket
carve-outs; a basket that exempted §4.12 would let the first dollar of a classification claim start the
clock against the escrow.

---

## §7.4(b) Cap — **CHANGE (the §4.12 carve-out is the whole fight)**

**As drafted:** "Seller's aggregate liability under 7.1 shall not exceed 10% of the Purchase Price (the
'Cap'), except for Fundamental Representations and Section 4.12, which shall be subject to a cap equal to
the Purchase Price."

**Arithmetic:** general Cap = 10% × $3,100,000 = **$310,000** = 1.0× escrow. §4.12 cap = **$3,100,000** →
money exposed **beyond** the escrow = 3,100,000 − 310,000 = **$2,790,000**. Illustrative §4.12 exposure on
the client-confirmed hours runs **$144,648–$157,578** (3-year scenarios, §4.12 note above; up to ~$243,000
grossed up) — the carve-out multiplies the realistic number by roughly **13×–21×**
(3,100,000 ÷ 157,578 ≈ 19.7; ÷ 144,648 ≈ 21.4; against the ~$243,000 grossed-up bound ≈ 12.8).

The library: cap ~10% for general reps is market; fundamental reps and taxes to purchase price is market;
**"a specific operational rep (like worker classification) carved out to a full-price cap is off-market and
should be resisted or replaced with a sized special indemnity"** (`library/baskets_caps.md`). "Fundamental
Representations" is **not defined in the extract** (Q3) — an undefined exception to the Cap is worse than a
defined one.

**Replacement language:**

> 7.4(b) Seller's aggregate liability under 7.1 shall not exceed 10% of the Purchase Price (the "Cap"),
> except that liability for breaches of Fundamental Representations (as defined in Section 1.x — definition
> to be provided and narrowed, see note) shall be subject to a cap equal to the Purchase Price. Section
> 4.12 is subject to the Cap. [Alternative, paired with §7.5 Special Indemnity: Section 4.12 is subject to
> the separate cap in Section 7.5 of $[250,000], recourse limited to the Escrow.]

Note: "Purchase Price" in the caps should be the **Closing Payment only** — if the full APA's definition
sweeps in the earn-out (up to $400,000 nominal, realistically $0–$16,000) it inflates every cap for paper
value (Q1).

---

## §7.4(c) Sandbagging — **CHANGE (flip or delete)**

**As drafted:** "Buyer's right to indemnification shall not be affected by any knowledge acquired (or
capable of being acquired) by Buyer at any time, whether before or after the execution of this Agreement,
with respect to the accuracy or inaccuracy of any representation."

This is a **pro-sandbagging** clause. The library's warning is this exact fact pattern: "Sellers who
disclose a known issue (e.g., contractor classification) in diligence and then give a clean representation
subject to a pro-sandbagging clause have effectively agreed to indemnify for the disclosed issue"
(`library/sandbagging.md`: Delaware/Texas practice; *Akorn v. Fresenius* (Del. Ch. 2018) (dicta); ABA
Private Target Deal Points Study). So our diligence disclosure of the installers does **not** protect us
under this clause — only the schedule exception, the anti-sandbagging flip, or the sized special indemnity
does.

**Replacement language:**

> 7.4(c) Buyer shall have no right to indemnification under Section 7.1 for any Losses arising from a
> breach of a representation (i) disclosed on the Disclosure Schedules, or (ii) actually known to Buyer as
> of Closing from the data room delivered before signing.

(Pro-sandbagging is a market position buyer's counsel may defend; the library supports the seller's three
protections, and the schedule exception in §4.12 works even if this clause survives.)

---

## §7.4(d) Survival — **TUNE (the tail is a collection risk, not a rep problem)**

**As drafted:** "Survival: 18 months; §4.12 and taxes: statute of limitations plus 60 days."

18 months general is within the library's market band (12–24 months, `library/baskets_caps.md`). The
§4.12/tax tail to SOL+60 days is longer than the 18-month escrow, and the extract does **not** say the
escrow is the buyer's sole recourse. So a year-3 IRS assessment is collectible outside the escrow — up to
the applicable Cap. Two conforming fixes (paired with whichever §4.12 structure is agreed):

- Sole-recourse language: for claims within the Cap/Escrow, the Escrow is Buyer's sole recourse until
  release.
- If §7.5 special indemnity is agreed: two escrow tranches — $60,000 releasing at 18 months, $250,000
  releasing on expiry of the §4.12 survival period (sum: 60,000 + 250,000 = $310,000 = the drafted escrow).

The actual SOL periods (limitation periods for payroll-tax and FLSA claims) are **not in the library —
[unverified]**; ask the CPA (Q10).

---

## §8.2 Non-Competition — **CHANGE (narrow it)**

**As drafted:** "Seller and Ray Brightline shall not compete in the custom cabinetry business within 500
miles of Austin for 7 years."

**Replacement language:**

> 8.2 Non-Competition. During the Restricted Period, Seller and Ray Brightline shall not **own or operate**
> a custom cabinetry fabrication business within the Restricted Area. "Restricted Period" means **five (5)
> years** (fallback: three) from Closing. "Restricted Area" means **Travis County and the counties
> contiguous to it, plus any county in which the Business performed work during the 24 months preceding
> Closing**. Nothing in this Section prohibits Ray Brightline from providing personal services as a
> consultant, or from holding a passive interest of less than 5%, to any person **outside** the Restricted
> Area, and does not prohibit employment by a supplier of materials.

**Why, even though Ray says he will sign anything.** The library: covenants ancillary to the sale of a
business are reviewed more leniently than employment covenants but must still be reasonable in time, area
and scope, and courts reform unreasonable covenants — "Seven years / 500 miles for a local custom-cabinetry
shop is likely overbroad as to both; 3–5 years within the trade area is typical"
(`library/tx_noncompete_sale_of_business.md`: Tex. Bus. & Com. Code §15.50; §15.51 reformation;
*Marsh USA v. Cook*, 354 S.W.3d 764 (Tex. 2011)). Two traps in accepting the drafted scope as-is:

1. The covenant binds **Ray personally for 7 years over a 500-mile radius**. DFW, San Antonio, Houston and
   Waco are within 500 miles of Austin (geometric observation — not a library fact). If "retiring" later
   means consulting or a small shop, he signed it away; do not rely on reformation to fix it.
2. **No separate payment and no allocation for §8.2 appears anywhere in the extract** — the covenant is
   bare. The client's answer to Q6 was that he has no additional information on allocation; the full APA
   must be checked. The library flags that an overbroad covenant *with* an allocation invites IRS scrutiny
   of the allocation; a bare covenant at full restraint is the worst combination for the seller (full
   restraint, zero allocated consideration). Whether §15.50's ancillarity requirement is satisfied by a
   bare covenant in the same agreement is not analyzed in the library — **[unverified]**; the safe fix is a
   narrower covenant plus an agreed allocation.

Client answer used (Q4): "I'll sign whatever non-compete, I'm retiring." That answers willingness, not
plans — the redline still narrows, and Q4 stays open on what "retiring" means (consulting? family entities
in the trade?).

---

## §9.3 Escrow — **KEEP (amount/term), CONFORM (recourse)**

**As drafted:** "$310,000 (10%) for 18 months."

Amount and term match the drafted cap (10%) and general survival (18 months) — keep them; they are the
library's market parameters (`baskets_caps.md`). **But:** (i) this caption is the *only* price figure in the
file — it is the basis of the $3,100,000 derivation used everywhere (Q1); (ii) as extracted, nothing says
the escrow is the buyer's **sole recourse** for capped claims — without that, post-release claims are
collectible directly (see §7.4(d) note); (iii) if the §7.5 special indemnity is agreed, tranche as
$60,000 + $250,000 with staggered releases. Full §9 text is not in the extract — conform once provided.

---

## Cross-cutting items (outside the six sections but load-bearing)

- **No closing-conditions article in the extract.** The §3.3(b) condition must be conformed into the full
  APA. Flagged, not assumed.
- **No allocation schedule anywhere in the file** (Q6 — client has no additional information). Earn-out is
  realistically $0–$16,000; §8.2 is bare. Get the full APA and CPA input before signature.
- **Schedule 3.1(c) (Assigned Contracts) is referenced but not provided.** The 22 residential contracts,
  Cascade and (subject to §3.3(e)) Hensley must appear consistently across Schedules 3.1(c) and 3.3.
- **Permit timing (data room §4.1):** the City of Austin spray-booth permit is non-transferable and must be
  reapplied for (30–60 days per the data room). That collides with "sign in two weeks" if closing follows
  signing immediately — raise in the reply and the note to Ray.
