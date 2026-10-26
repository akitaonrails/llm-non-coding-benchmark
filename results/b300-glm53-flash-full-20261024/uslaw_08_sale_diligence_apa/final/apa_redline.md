# APA Redline — Brightline Cabinetry asset sale (seller side)

Buyer's draft: Lone Star Millwork Holdings LLC "standard form," received with cover email from J. Whitaker.
Sections redlined per engagement scope: §§2.4, 3.3, 4.12, 7.4(a)–(c), 8.2, 9.3.

**Price inference used throughout:** price is not stated anywhere in the client file; escrow is "$310,000 (10%)" (§9.3) ⇒ $310,000 ÷ 0.10 = **$3,100,000**. Treat as inferred, and confirm against §2.1 of the full APA (not provided).
**Citations:** all authorities are from `library/INDEX.md`, cited as `library/<file>.md`.

---

## Assumption and arithmetic block (shown, per the working rules)

1. Implied price = 310,000 / 0.10 = **$3,100,000**. General-rep cap = 10% × 3,100,000 = **$310,000** (equals escrow). Basket = 75,000 / 3,100,000 = **2.42%** of price.
2. Installer exposure (the upper end of what Buyer will calculate):
   - Employer FICA at 7.65% (upper-bound payroll figure; **not stated in the library — verify**; library notes IRC §3509 reduced rates if non-willful): 612,000 × 7.65% = **$46,818/yr**; × 3.4-yr average tenure = **$159,181**.
   - Overtime premium, half-time extra on hours over 40 (method is standard payroll arithmetic, **not stated in the library — verify**): rate midpoint (34+41)/2 = $37.50 ⇒ $18.75 per OT hour.
     - Scenario A (Ray: 45–50 hrs/wk in busy season; length unknown — **assumed 12 weeks**): 10 OT-hrs/wk × 12 wks = 120 OT-hrs/yr ⇒ 18.75 × 120 × 9 workers = **$20,250/yr** ⇒ × 3.4 yrs = **$68,850**.
     - Scenario B, conservative (buyer's likely model, 45 hrs/wk all year — "all year" taken literally as 52 paid weeks, no unpaid-vacation assumption): 5 OT-hrs/wk × 52 wks = 260 OT-hrs/yr ⇒ 18.75 × 260 × 9 = **$43,875/yr** ⇒ × 3.4 yrs = **$149,175**.
   - Bracketed indicative total: **$228,031 (7.4% of price) to $308,356 (9.9% of price)** vs. escrow of $310,000. Prior-year 1099 totals were not provided (client answered no additional info); 2025 is used as the annual run-rate proxy. The FLSA recovery period is **not in the library**, so 3.4 years (census average tenure) is used as the exposure window rather than a limitations-based period.
3. Earn-out gate arithmetic: full $400,000 requires EBITDA of 700,000 + 400,000/0.40 = **$1,700,000**. Clean 2025 EBITDA = 740,000 − 180,000 − 42,000 = **$518,000**; with a replacement manager at Ray's comp: 518,000 − 180,000 = **$338,000**. Buyer-measured post-closing: earn-out **$0** in both cases; even unchanged seller-prepared basis yields 0.40 × (740,000 − 700,000) = **$16,000**.
4. WARN: 14 W-2 employees; even adding the 9 installers as employees = 23, under the 100-employee threshold.

---

## §2.4 Earn-Out — **CHANGE**

**Buyer's draft (as received):** 40% of EBITDA (12 months post-closing) above $700,000, max $400,000; "EBITDA" determined by Buyer in good faith under Buyer's accounting policies, consistently applied.

**Replacement language:**

> "§2.4 Earn-Out. In addition to the Closing Payment, Buyer shall pay Seller 40% of the excess of EBITDA of the Business for the twelve (12) months following Closing over $700,000, up to a maximum Earn-Out payment of $400,000.
> (a) 'EBITDA' means earnings of the Business before interest, taxes, depreciation and amortization, determined in accordance with GAAP, consistently applied, and consistent with the Seller's historical accounting practices reflected in the 2025 financial statements, provided that:
>   (i) there shall be added back owner's compensation for the pre-Closing period, offset by a deduction for compensation actually paid by Buyer to operate the Business in lieu of owner compensation (up to $180,000 per annum);
>   (ii) non-recurring legal fees of $42,000 incurred pre-Closing are excluded;
>   (iii) there shall be excluded any corporate overhead, management fees, allocation charges, transaction, integration or purchase-accounting costs attributable to Buyer or its Affiliates; and
>   (iv) no charge shall reduce EBITDA to the extent attributable to changes Buyer makes to pricing or contract terms contrary to pre-Closing practice.
> (b) Buyer shall operate the Business in the ordinary course consistent with past practice. If Buyer fails to do so with the purpose of avoiding or delaying payment, EBITDA shall be calculated as if Buyer had so operated.
> (c) Buyer shall deliver quarterly statements of EBITDA with supporting detail; Seller may audit Buyer's calculation on reasonable notice; disputes resolved by an independent accountant whose fees Buyer bears unless Seller's error exceeds 5%.
> (d) If Buyer sells the Business or substantially all its assets during the Earn-Out period, the unpaid Earn-Out accelerates, calculated on EBITDA through the closing date of such sale annualized."

**Why:** the as-received definition — "EBITDA" determined by Buyer in good faith under Buyer's accounting policies — is the classic buyer-control formulation that lets overhead allocations, management fees, integration costs and purchase-accounting adjustments zero the earn-out; seller protections are exactly the set in `library/earnout_definitions.md` (*Lazard Technology Partners v. Qinetiq*, 114 A.3d 193 (Del. 2015)). Separately, the $700k gate sits above every realistic post-closing figure in the arithmetic block (clean base $518k; $338k if buyer pays a replacement manager), so as drafted the earn-out is worth ~$0 — see deal-impact note in `diligence_findings.json` (item 8). If buyer refuses the definition, the fallback is negotiation of the gate toward achievable EBITDA or payment in cash/holdback instead.

## §3.3 Required Consents + Schedule 3.3 — **CHANGE**

**Buyer's draft:** "Seller shall use commercially reasonable efforts to obtain the consents listed on Schedule 3.3 prior to Closing. (Schedule 3.3, as drafted by Buyer: 'None.')"

**Replacement language:**

> "§3.3 Required Consents. Seller shall use commercially reasonable efforts to obtain, prior to Closing, the consents listed on **Schedule 3.3 (Required Consents)**, and Buyer shall cooperate. Failure to obtain a consent listed on Schedule 3.3 shall not excuse Buyer from Closing provided Seller has used commercially reasonable efforts, except in the case of the Hensley Homes Master Supply Agreement consent, which shall be a condition precedent to Closing (with a drop-dead date to be agreed). Seller and Buyer shall cooperate on the reapplication process described on Schedule 3.3 for the spray-booth permit."

**Proposed Schedule 3.3 (to attach):**

| # | Contract/Permit | Consent? | Standard | Data room source |
|---|---|---|---|---|
| 1 | Master Supply Agreement — Hensley Homes (38% of revenue = $1,748,000) §18 | Yes — consent required, **void** without it | Consent may be withheld **in Hensley's sole discretion** (the counterparty's right, not Seller's); **not yet sought**; owner is a friend who does not yet know of the sale | data room §1.1 |
| 2 | Shop lease, 7700 Burleson Rd (through 2029), §22 | Yes — landlord consent | Not unreasonably withheld | data room §3.1 |
| 3 | City of Austin spray-booth permit | Not assignable — **new permit required**; reapply 30–60 days | City processing time controls closing calendar | data room §4.1 |
| 4 | Framework agreement — Cascade Builders (11%) | No consent — assignment permitted on notice | Notice to counterparty | data room §1.2 |
| 5 | 22 residential contracts <$40k each | No consent required — clauses silent | Rights assignable per library (`library/anti_assignment_change_of_control.md`); buyer assumes obligations at closing | data room §1.3 |

**Why:** Buyer's "None" is simply wrong for this business — the Hensley MSA chokes assignment "by operation of law, merger, sale of assets, change of control or otherwise" and voids transfers without consent; enforcement follows the contract's terms and violation of an anti-assignment clause by asset sale is a breach with the transfer void where the clause so provides (`library/anti_assignment_change_of_control.md`, citing *SQL Solutions v. Oracle*; Restatement (Second) of Contracts §§317, 322). A "sole discretion" consent standard gives Hensley negotiation leverage (`library/anti_assignment_change_of_control.md`). Strategy and facts (consent not sought; owner unaware) from the client's answer to question 1: a personal approach from Ray is the highest-probability path and should happen **before signing**. The condition-precedent mechanic in the replacement language reflects that.

## §4.12 Employees and Contractors — **CHANGE**

**Buyer's draft:** Clean rep: all individuals properly classified; all required taxes withheld/paid.

**Replacement language:**

> "§4.12 Employees and Contractors. Schedule 4.12 lists the nine (9) individuals who have been treated as independent contractors ("Installers") during the three (3) years prior to the date hereof; except as set forth on Schedule 4.12, Seller represents that all individuals providing services to the Business have been properly classified as employees or independent contractors under applicable law and that Seller has withheld and paid all required taxes."

Add to §7.1 (or as §7.1A):

> "§7.1A Special Indemnity (Worker Classification: Installers). Buyer shall be indemnified for Losses arising out of (a) classification of any individual listed on Schedule 4.12 as an independent contractor, including employer payroll taxes, state unemployment contributions, wages and overtime premiums, penalties, interest and reasonable attorneys' fees, and (b) costs reasonably incurred by Buyer to reclassify the individuals listed on Schedule 4.12 and place them on Buyer's payroll. Seller's aggregate liability under this §7.1A shall not exceed **$275,000** (the 'Special Indemnity Cap'). §7.1A is the sole source of Buyer indemnification for matters arising from the classification of individuals on Schedule 4.12 to the extent provided thereon, other than for Buyer's knowing fraud or a Fundamental Representation breach."

**Why:** (i) The underlying facts (exclusivity, Brightline trucks/tools, foreman-driven daily scheduling, hourly pay, years of tenure) meet the common-law control test — employees regardless of the 1099 label; "everyone in the industry does it" is not a defense (`library/worker_classification_tx_irs.md`, IRS Rev. Rul. 87-41; Treas. Reg. §31.3121(d)-1). The rep is false as written. (ii) Indicative exposure brackets $228k–$308k (arithmetic block above; Texas unemployment contributions and §3509 reduced-rate magnitudes are not quantifiable from the library, hence a modest buffer to a $275k cap, ~8.9% of inferred price). (iii) Buyers price classification risk and demand indemnity, per the same library note. A disclosure-schedule exception plus a sized special indemnity is the seller's protection listed in `library/sandbagging.md`. (Client declined to choose option (b) converting installers to W-2 pre-closing — cash cost now would be roughly the same FICA dollars minus the historical lookback; the disclosed-plus-capped-indemnity route is recommended here.)

## §7.4(a) Basket — **KEEP**

**Buyer's draft:** Seller liability only until aggregate Losses exceed $75,000, then losses in excess (deductible basket).

**Verdict:** Keep. This is a standard **deductible** basket — seller pays only losses above the threshold — one of the two basket structures described in `library/baskets_caps.md` (ABA Deal Points Study private targets). That library states a market norm for the *cap* (~10% of price) but none for basket size, so no market-range comparison is asserted for the $75,000 figure; on our own arithmetic $75,000 = 2.42% of inferred price. The items most likely to sit inside it — Hardaway $9,800, warranty log $23,000 — fall below it, and scheduling them removes arguing about them under the anti-sandbagging regime. Optional trade if something else concedes: ask for a tipping basket, but I would spend that leverage on 7.4(c).

## §7.4(b) Cap — **CHANGE**

**Buyer's draft:** Cap 10% except Fundamental Representations **and §4.12**, capped at full Purchase Price.

**Replacement language:**

> "§7.4(b) Seller's aggregate liability under §7.1 shall not exceed 10% of the Purchase Price (the 'Cap'), except for (i) Fundamental Representations, (ii) indemnification for taxes (other than the Special Indemnity in §7.1A), and (iii) Buyer's knowing fraud, which shall not be subject to the Cap. §4.12 is subject to the Cap, subject to the Special Indemnity Cap in §7.1A."

**Why:** Carving a specific operational rep (worker classification) out to a full-price cap is off-market and should be resisted or replaced with a sized special indemnity — this exact situation (`library/baskets_caps.md`). With the amended §4.12 and §7.1A, buyer keeps what it actually needs (a bounded classification remedy) and Ray stops writing a $3.1M blank check for a ~$228k–$308k item. Fundamental reps unaffected, as market (same library file).

## §7.4(c) Knowledge / Sandbagging — **CHANGE**

**Buyer's draft:** Indemnification not affected by any knowledge Buyer "acquired (or capable of being acquired) at any time," before or after execution.

**Replacement language:**

> "§7.4(c) Buyer's right to indemnification shall not be affected by Buyer's or any Affiliate's knowledge of the accuracy or inaccuracy of any representation acquired at or prior to Closing; provided that this §7.4(c) shall not apply to (i) Fundamental Representations, (ii) matters stated on a disclosure schedule, or (iii) Buyer's knowing fraud."

**Why:** As drafted this is the broadest pro-sandbagging formulation — it applies to breaches buyer only *could have* discovered, and even post-signing. A seller who discloses a known issue and then gives a clean rep under a pro-sandbagging clause has effectively agreed to indemnify for the disclosed issue; the seller's protection is anti-sandbagging, a schedule exception, or a capped special indemnity — we are engineering all three (`library/sandbagging.md`, citing Delaware/Texas practice; *Akorn v. Fresenius* (Del. Ch. 2018) (dicta); ABA Private Target Deal Points Study). In this deal's specific posture, this clause plus the clean §4.12 rep makes Ray the insurer for an issue the buyer is about to learn about in diligence. Fraud and Fundamental Reps are the buyer-friendly carve-outs that make the anti-sandbagging answer acceptable.

## §8.2 Non-Competition — **CHANGE**

**Buyer's draft:** Seller and Ray Brightline shall not compete in custom cabinetry within 500 miles of Austin for 7 years.

**Replacement language:**

> "§8.2 Non-Competition. For three (3) years from Closing, Seller and Ray Brightline shall not directly or indirectly own (other than passive investment of less than 2% of a public company), manage, operate, or engage in the custom cabinetry business within a seventy-five (75) mile radius of the Business's premises at 7700 Burleson Road, Austin, Texas (the 'Restricted Area'). Nothing herein restricts any passive economic interest."

**Why:** Seven years and 500 miles is overbroad on both time and area for this business; sale-of-business covenants are reviewed more leniently but must remain within reasonable time/area/scope, and courts reform unreasonable covenants (Tex. Bus. & Com. Code §15.50; reformation under §15.51(c)); 3–5 years within the trade area is typical per `library/tx_noncompete_sale_of_business.md` (*Marsh USA v. Cook*, 354 S.W.3d 764 (Tex. 2011)). The reformation risk is really the buyer's enforcement risk, and this reformat is the free win in the deal — but the *real* seller-side risk is tax: an overbroad covenant with allocated price invites scrutiny of the purchase price allocation (`library/tx_noncompete_sale_of_business.md`), and we have no PPA in the data room, so we cannot rule that out; a tight covenant keeps the allocation argument clean. The 75-mile radius is a placeholder pending Ray's confirmation of his customer footprint (open item).

## §9.3 Escrow — **KEEP (with a release schedule)**

**Buyer's draft:** $310,000 (10%) held for 18 months.

**Verdict:** Keep the amount and duration; the 18-month term matches the general survival period in §7.4(d) and 10% of price equals the general cap (§7.4(b)) — a consistent package. The bracketed classification exposure ($228k–$308k) nearly equals the escrow ($310,000; excess over Scenario B = $1,644), so buyer will insist escrow backstops the Special Indemnity in §7.1A; accept a cap-backstop as long as the indemnity itself is capped. Propose a negotiated release schedule (e.g., staged releases with a 50% holdback until the classification lookback closes if buyer requires) as deal mechanics rather than redline, per the escrow-survival alignment noted in `library/baskets_caps.md` (survival 12–24 months market; 18 months is within it).

---

## Items outside redline scope flagged for the negotiation, and unverified items

- Schedule 3.1(c) (Assigned Contracts) was not provided; if the Hensley MSA sits on it, consent pressure increases. Open.
- §7.4(d): §4.12 and tax rep survival at statute-of-limitations-plus-60-days versus 18 months general — once §4.12 is scheduled and capped per §7.1A, push for the tax survival to function only for the Special Indemnity (raise in negotiation).
- §6.1 of the data room: seller-prepared EBITDA with add-backs ($180k owner salary; $42k "one-time" legal). Quotation marks around 'one-time' are buyer-skeptical; the redlined earn-out definition (§2.4(a)(ii)) treats only the specified items as add-backs.
- Unverified (not in `library/INDEX.md` and therefore not relied on as law): the 7.65% employer FICA figure and the half-time overtime-presentation method used in the exposure arithmetic (standard payroll arithmetic, flagged above); FLSA limitations periods (we used census tenure instead); IRC §3509 reduced-rate percentages and Texas unemployment contribution rates (library mentions the regimes but not the numbers, so they are excluded, treated as buffer rather than quantified).
