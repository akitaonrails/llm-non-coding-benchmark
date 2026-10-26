# APA redline — Brightline Cabinetry / Lone Star Millwork Holdings LLC

Buyer's draft, key sections. Position is sell-side. **Internal working document:** the proposed clause language (block quotes) is what we would circulate; the "Why" notes and negotiation instructions (e.g., the $200,000-hold/$250,000-fallback range in §7.4(b)) are attorney work product and must be stripped before anything goes to buyer's counsel. **Assumption stated up front:** the excerpt does not state the Purchase Price; the escrow clause ($310,000 = "10%") implies **Purchase Price = $310,000 / 0.10 = $3,100,000**, so the 7.4(b) general cap = $310,000 and the §4.12 carve-out cap = $3,100,000. All percentages below use that figure; confirm (QUESTIONS.md, open assumption 3).

Citations are only to files in `library/INDEX.md`. Anything not in the library is labeled **UNVERIFIED**.

---

## §2.4 Earn-Out — **CHANGE**

**Problem (three layers):**
1. "EBITDA ... as determined by Buyer ... in accordance with Buyer's accounting policies" — the classic zero-out device. Buyer can allocate overhead, management fees, integration costs and purchase-accounting adjustments against the Business and pay nothing. See `library/earnout_definitions.md` (*Lazard Technology Partners v. Qinetiq*, 114 A.3d 193 (Del. 2015)).
2. The threshold is unreachable as drafted. Max payout requires 40% × (EBITDA − $700,000) = $400,000 → EBITDA = $700,000 + $400,000/0.40 = **$1,700,000**, vs. reported 2025 EBITDA of $740,000 — growth of ($1,700,000 − $740,000)/$740,000 = **129.7%**. Even if $740,000 were accepted unchanged, the payout is 0.40 × ($740,000 − $700,000) = **$16,000**.
3. The $740,000 itself is seller-prepared with $222,000 of add-backs (owner salary $180,000 + legal $42,000). Under any buyer policy that drops add-backs, run-rate EBITDA = $740,000 − $222,000 = **$518,000** — **$182,000 below the threshold**, so the earn-out is **$0** before Buyer allocates a dollar of overhead.

**Replacement language:**

> 2.4 Earn-Out. In addition to the Closing Payment, Buyer shall pay Seller an amount equal to 40% of the amount by which Adjusted EBITDA of the Business for the twelve (12) months following Closing exceeds $[518,000 / to be negotiated], up to a maximum of $400,000. "Adjusted EBITDA" means earnings before interest, taxes, depreciation and amortization of the Business, determined in accordance with GAAP consistently applied on a basis consistent with Seller's historical accounting practices as exhibited in Exhibit 2.4, and excluding: (i) any allocation of Buyer or Buyer-affiliate overhead, management fees, shared-service charges, or corporate costs to the Business; (ii) any transaction, integration, restructuring or purchase-accounting adjustment (including step-up depreciation/amortization) costs of Buyer; and (iii) [owner-salary and the identified one-time legal add-backs]. From and after the Closing, Buyer shall (x) operate the Business in the ordinary course consistent with past practice, (y) not take any action with the primary purpose of avoiding or reducing the Earn-Out, and (z) provide Seller monthly interim financial statements for the Business and audit rights on reasonable notice. Disputes under this Section shall be resolved by a mutually agreed independent accounting firm acting as expert, whose determination is binding, with costs allocated to the losing side. Upon a sale by Buyer of the Business or its relevant assets, the maximum Earn-Out amount becomes immediately due and payable. The Earn-Out shall be secured by [escrow/holdback note].

**Why:** `library/earnout_definitions.md` prescribes exactly this seller-protection set. Also tell Ray the commercial truth: as drafted this earn-out is worth approximately zero, so he should negotiate more closing cash rather than trade on the headline $400,000. If Buyer keeps a high threshold, the number alone (129.7% EBITDA growth required) is the argument.

---

## §3.3 Required Consents (and Schedule 3.3) — **CHANGE**

**Problem:** Schedule 3.3 says **"None."** That is false, and it is the most dangerous single word in the draft (see also the Schedule 3.3 answer in `reply_to_buyer_counsel.md`):
- **Hensley Homes MSA** (data room §1.1, 38% of revenue = 0.38 × $4.6M = **$1,748,000/yr**): §18 bars assignment "by operation of law, merger, sale of assets, change of control or otherwise" without prior written consent "withheld in its sole discretion," and makes any purported assignment **void**. Per `library/anti_assignment_change_of_control.md` (*SQL Solutions v. Oracle*, 1991 WL 626458 (N.D. Cal.); Restatement (Second) §§317, 322), such a clause is enforced according to its terms — the asset sale transfers this contract only with consent, and transferring without it is a breach and void. "Sole discretion" gives Hensley renegotiation leverage.
- **Cascade Builders** (data room §1.2, 11% = $506,000/yr): permitted to a successor to substantially all assets **upon notice** — still a required notice; APA 3.1 (all assets) should satisfy the "substantially all" condition.
- **Shop lease** (data room §3.1): §22 landlord consent, not unreasonably withheld.

**Replacement language:**

> 3.3 Required Consents. Schedule 3.3 lists each consent or notice required under the Assigned Contracts in connection with the transactions contemplated hereby, and Seller shall use commercially reasonable efforts to obtain such consents (or deliver such notices) prior to Closing. No representation or warranty in this Agreement shall be deemed breached, and no closing condition shall fail, solely by reason of the absence of any consent not expressly listed on Schedule 3.3 or by reason of the failure to obtain a listed consent, provided Seller has used such commercially reasonable efforts. [Negotiated bracket: if the Hensley consent is not obtained by the Outside Date, Buyer's sole remedy shall be [a purchase-price reduction equal to $[x] / termination], and Seller shall not be obligated to accept any modification of the Hensley MSA as a condition to consent.]

**Replacement Schedule 3.3:**

> Schedule 3.3 — Required Consents and Notices: (1) Hensley Homes — written consent to assignment of the Master Supply Agreement (§18) [approach to begin on signing]; (2) landlord at 7700 Burleson Rd — written consent to lease assignment (lease §22, not to be unreasonably withheld); (3) Cascade Builders — written notice of assignment to successor to substantially all assets (§ per framework agreement).

**Why:** keep "commercially reasonable efforts" (Seller can't guarantee Hensley's yes), but the schedule must be truthful or Ray signs a false rep on day one; and the Hensley consequence branch (walk vs. price cut) must be negotiated now, not after Hensley smells leverage.

**Hensley sequencing (client fact: the owner is Ray's personal friend, has not been told, and "won't love a corporate buyer"):** the friendship only helps if Ray tells Hensley first — in person, this week, before signing and before any buyer-side contact. Add to the APA:

> 3.4 Customer Contact. Prior to Closing, neither Buyer nor its representatives shall contact any customer of the Business regarding the transactions contemplated hereby without Seller's prior written consent and participation; Buyer shall treat the data room and all customer information as confidential.

And target **signed Hensley consent before signing** if the personal conversation goes well — a consent in hand converts the deal's biggest condition into a non-event. If Hensley's answer is slow or soft-no, the bracketed remedy branch above (defined price reduction tied to the $1,748,000 revenue share, or termination with an outside date) is what keeps Ray from being at the mercy of a sole-discretion veto after he has shopped his friend out of retirement plans.

---

## §4.12 Employees and Contractors — **CHANGE**

**Problem:** The rep as drafted ("all individuals ... properly classified ... and Seller has withheld and paid all required taxes") is **false at signing** — nine installers paid on 1099 work exclusively for Brightline, on its schedule, with its trucks and tools, hourly, averaging 3.4 years (data room §2.2). Under the common-law control test they are employees regardless of label (`library/worker_classification_tx_irs.md`: IRS Rev. Rul. 87-41; Treas. Reg. §31.3121(d)-1; IRC §3509; Tex. Lab. Code §201.041; 40 TAC §815.134). A clean rep on a known, disclosed problem, combined with pro-sandbagging 7.4(c) and the full-price carve-out in 7.4(b), is exactly the trap described in `library/sandbagging.md`.

**Replacement language:**

> 4.12 Employees and Contractors. Except as set forth on Schedule 4.12 (identifying nine individuals currently compensated on Form 1099 as installers and the 2025 amounts paid), Seller has properly classified all individuals providing services to the Business as employees or independent contractors under applicable law, and Seller has withheld and paid all required taxes with respect to all such individuals, except to the extent arising from the classification disclosed on Schedule 4.12. Buyer acknowledges the disclosures on Schedule 4.12 and agrees that matters so disclosed shall be addressed exclusively under Section 7.4(b) (Worker Classification Special Indemnity) and shall not constitute a breach of this Section 4.12.

**Why:** this is the load-bearing fix. It converts a rep that Ray would breach on day one into (a) a disclosure and (b) a **sized, escrow-backed special indemnity** (see 7.4(b)). `library/sandbagging.md`: the seller's protections are an anti-sandbagging clause, a disclosure-schedule exception, or a special indemnity with a negotiated cap — *not a clean rep*. Ray's belief that "1099 forever, everyone does it" is legally irrelevant under the control test — do not litigate this belief into the rep. **Client fact (round 2):** the installers work 45–50 hrs/week in busy season, paid straight hourly — no overtime premium. Schedule the hours too; whether "they like it" can waive FLSA overtime is outside the library (**UNVERIFIED**), but the library squarely attaches FLSA overtime liability to hourly employees >40 hrs, so worker preference is not a defense we can build on.

---

## §7.4(a) Basket — **KEEP**

Keep as drafted: $75,000 **deductible** (seller pays only above the threshold; `library/baskets_caps.md` explains deductible vs tipping; deductible is the seller-favorable form — do not let "market" drift to tipping). $75,000 / $3,100,000 = **2.42%** of the implied price — reasonable range (**UNVERIFIED as a market benchmark**: the library's summary gives cap and survival norms but no basket percentage). It also swallows the known small claims (Hardaway $9,800 + warranty log $23,000 = $32,800 < $75,000).

No replacement language needed. Guard against carve-outs that let specific reps escape the basket without also getting a negotiated cap.

---

## §7.4(b) Cap — **CHANGE**

**Problem:** general cap = 10% of price (market: cap ~10% for general reps — `library/baskets_caps.md`), but §4.12 is carved out to a cap equal to the **full Purchase Price** ($3,100,000 implied) alongside Fundamental Reps and taxes. The library calls this out almost verbatim: *"a specific operational rep (like worker classification) carved out to a full-price cap is off-market and should be resisted or replaced with a sized special indemnity."* Combined with 7.4(d) survival (SoL + 60 days for §4.12) and only $310,000 of escrow, Ray carries an unbacked tail of $3,100,000 − $310,000 = **$2,790,000** for years after escrow release.

**Replacement language:**

> (b) Seller's aggregate liability under Section 7.1 shall not exceed 10% of the Purchase Price (the "Cap"), except for Fundamental Representations and taxes, which shall be subject to a cap equal to the Purchase Price. Section 4.12 shall be subject to the Cap. Notwithstanding the foregoing, Seller's aggregate liability in respect of the reclassification of, and employment taxes, penalties, interest, overtime and wage-claim exposure attributable to, the individuals disclosed on Schedule 4.12 for periods prior to Closing (the "Worker Classification Special Indemnity") shall not exceed $200,000, which amount shall be secured first from the Employment Escrow Amount under Section 9.3, and shall be Buyer's exclusive remedy for such matters (absent fraud).

**Sizing the special indemnity (show the arithmetic; §3509 percentage rates flagged UNVERIFIED because the library cites §3509 but does not reproduce its percentage rates):**

*Taxes — sized as scenarios, not one point estimate (a pre-audit single figure mixed §3509(a) and §3509(b) rates on the wrong base and has been withdrawn; every percentage below is **UNVERIFIED** — the library cites §3509 as the reduced-rate mechanism but does not reproduce its rates).* 2025 payments to the nine = $612,000; FICA at 7.65% on that base = $46,818/yr per side. **Scenario 1 — non-willful, §3509(a) reduced rates, withholding-only reading:** 1.5% × $612,000 = $9,180 (income-tax portion) + 50% × $46,818 = $23,409 (half the employee FICA that should have been withheld) = **$32,589/yr**; ~4 open years (3.4-yr average tenure) ≈ **$130,356**. **Scenario 2 — same reduced rates but the employer's own FICA share is not abated** (the library does not answer this question): + $46,818/yr → $79,407/yr → ≈ **$317,628**. **Scenario 3 — negligent, §3509(b):** 20% × $612,000 = $122,400 + $23,409 = $145,809/yr → ≈ **$583,236**. **Willful disregard = no §3509 relief at all**, higher still (computable FICA alone: 15.3% × $612,000 = $93,636/yr). All scenarios before state unemployment (Tex. Lab. Code §201.041; 40 TAC §815.134 — rates not in library, not sized) and before penalties/interest.

*Overtime (client round 2: 45–50 hrs/week in busy season, paid straight hourly).* Average rate ($34 + $41)/2 = $37.50/hr; straight time was paid on all hours, so the FLSA gap is the half-time premium 0.5 × $37.50 = **$18.75/OT-hour**. Low case: 5 OT hrs/wk × 12 busy weeks = 60 hrs × $18.75 = $1,125/installer/yr → 9 installers = **$10,125/yr**. High case: 10 hrs × 20 wks = 200 hrs × $18.75 = $3,750/installer/yr → **$33,750/yr**. Over 4 open years: **$40,500–$135,000** (busy-season length assumed 12–20 weeks — open item).

*Total realistic pre-closing band (non-willful Scenarios 1–2):* tax $130,356–$317,628 + overtime $40,500–$135,000 = **≈ $170,000–$450,000**, before state UI and before any liquidated-damages doubling or 3-year willfulness window (both outside the library — **UNVERIFIED**); a negligent or willful posture is materially higher and is not conceded. **Negotiation instruction: hold at $200,000 (6.5% of price); go to $250,000 (8.1%) only if needed to close.** Be honest internally about what the cap buys: $200,000 covers Scenario 1 plus low-case overtime with margin — it does **not** cover the top of the band, and we should never assert in writing that it does; the cap is the negotiated limit, that is the point. Do not argue the numbers down to zero — the library says the classification is clear; argue the **cap**. Seller-side arguments that carry: (i) per `library/worker_classification_tx_irs.md`, the buyer may itself bear FLSA claims as a successor in a substantial-continuity asset deal — it cannot recover the same dollars twice; (ii) `library/baskets_caps.md` names worker classification **expressly** as the operational rep whose full-price carve-out is off-market — if Buyer invokes that same summary's "fundamental reps and taxes get full price" line, the answer is that §4.12 *is* the library's own named example, with the tax exposure flowing from classification, not a tax rep in itself; (iii) a full-price cap on a rep both sides know is breached invites a post-closing enforceability fight nobody needs — **advocacy framing only; whether a tribunal would reform or police such a carve-out is outside the library, UNVERIFIED** — lead with (i) and (ii), which are library-backed.

---

## §7.4(c) Sandbagging — **CHANGE** (position on this also goes to buyer's counsel)

**Problem:** as drafted this is **pro-sandbagging**: Buyer recovers "regardless of knowledge acquired ... before or after execution." Buyer already knows the classification facts from the data room. Per `library/sandbagging.md`: "Sellers who disclose a known issue (e.g., contractor classification) in diligence and then give a clean representation subject to a pro-sandbagging clause have effectively agreed to indemnify for the disclosed issue." Keep this clause *only if* §4.12 carries the schedule exception and sized cap above (then knowledge is moot). If the buyer refuses the schedule exception, this clause must go.

**Replacement language:**

> (c) Notwithstanding anything to the contrary, Seller shall have no liability under Section 7.1 in respect of any breach of any representation or warranty that Buyer actually knew, prior to the execution of this Agreement, to be inaccurate at the time the relevant representation was made, including any matter disclosed in the data room or on any disclosure schedule; and Buyer's indemnification rights shall in all events be subject to Sections 7.4(a) and (b), including the Worker Classification Special Indemnity.

**Why:** anti-sandbagging is one of the three recognized seller protections in the library. Fallback ladder: (i) schedule exception + special indemnity (best — then 7.4(c) barely matters); (ii) anti-sandbagging as above; (iii) at minimum, carve data-room-disclosed matters out of indemnification. Fallback **not** acceptable: clean rep + pro-sandbagging + full-price cap. Buyer's counsel calls this "market-standard knowledge language" — `library/sandbagging.md` shows it is one of two standard positions, and it is the buyer-favorable one.

*(§7.4(d) survival — outside the redline list, but note: 18 months general is inside the 12–24 month market range per `library/baskets_caps.md`; the SoL+60-days tail on §4.12 is another reason the §4.12 cap fix above matters more than the survival fight.)*

---

## §8.2 Non-Competition — **CHANGE**

**Problem:** 7 years / 500 miles of Austin, binding Ray personally, for a local custom-cabinetry shop. Per `library/tx_noncompete_sale_of_business.md` (Tex. Bus. & Com. Code §15.50; *Marsh USA v. Cook*, 354 S.W.3d 764 (Tex. 2011)): sale-of-business covenants get lenient review but must be reasonable in time, area and scope, and "seven years / 500 miles for a local custom-cabinetry shop is likely overbroad as to both; 3–5 years within the trade area is typical." Courts reform rather than strike (§15.51(c)), so Ray *will* end up bound to some reasonable version — "I'll sign whatever, I'm retiring" is not a legal strategy, and the library also flags the IRS allocation angle: an overbroad covenant loaded with a large price allocation invites scrutiny of the allocation (no allocation is in the file — QUESTIONS.md, open assumption 3).

**Replacement language:**

> 8.2 Non-Competition. During a period of three (3) years following the Closing, Seller and Ray Brightline shall not own, manage or operate a custom cabinetry fabrication business within Travis County, Texas and the counties contiguous thereto. Nothing herein restricts passive ownership of less than 1% of any publicly traded entity or employment in a non-competing capacity. If a court of competent jurisdiction determines this covenant exceeds the scope enforceable under Tex. Bus. & Com. Code §15.50, the covenant shall be reformed to the maximum enforceable scope and enforced as reformed.

**Why:** matches the library's stated typical range (3–5 years, trade area), preserves the buyer's legitimate goodwill protection, and stops Ray from inadvertently signing away a comeback or hobby-shop option five years from now. If Ray truly wants out of any non-compete, note for him: in a goodwill sale the buyer gets *some* covenant; the fight worth having is scope, not existence.

---

## §9.3 Escrow — **CHANGE (structure; amount keep)**

**Problem:** $310,000 (10%) for 18 months matches the general cap and general survival — fine for general reps. But with §4.12 uncapped to $3,100,000 and surviving to SoL + 60 days, a classification claim in year three would come personally at Ray beyond a dissolved escrow (unbacked gap: $3,100,000 − $310,000 = **$2,790,000**).

**Replacement language:**

> 9.3 Escrow. $310,000 (10% of the Purchase Price) shall be deposited in escrow for eighteen (18) months (the "General Escrow"), securing Seller's indemnification obligations under Section 7.1, and shall be the sole source of recovery therefor absent Fundamental Representations or fraud. Of that amount, $200,000 [or $250,000, if the Special Indemnity cap moves per the fallback in §7.4(b)] is designated the "Employment Escrow Amount" securing the Worker Classification Special Indemnity under Section 7.4(b), which shall be released on the [18]-month anniversary to the extent no claim has been noticed. No claim noticed in good faith before the applicable release date may be paid from escrow except as finally determined. Escrow fees are borne [equally / by Buyer].

**Why:** keeps buyer's 10% comfort where it belongs (the negotiated caps), makes escrow the primary recovery source so judgments can't run past it for general claims, and puts the agreed special-indemnity cap behind real money so buyer can accept the cap instead of demanding full-price coverage. The designated tranche must track the final 7.4(b) cap: at $200,000 it leaves $310,000 − $200,000 = $110,000 of general escrow; at the $250,000 fallback only $60,000 remains — so if the cap moves, ask Buyer to fund additional escrow (deferred cash — a price-timing point for Ray) or accept the thinner general cushion (under the sole-source sentence above, a thin cushion cuts Buyer's recovery, not Ray's exposure). The single change that makes this all work is the 7.4(b) cap fix; escrow structure follows it.
