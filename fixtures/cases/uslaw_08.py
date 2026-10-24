"""USLAW-8 · L3 · Selling Brightline — diligence findings and the buyer's APA redline (single session)."""
from generators.core import Case, COMMON_RULES


def build():
    c = Case("uslaw_08_sale_diligence_apa", "uslaw", "Sell-side diligence and purchase-agreement redline for Brightline Cabinetry", "L3")
    c.doc_pdf("data_room_index_and_key_contracts.pdf", """
# Brightline Cabinetry LLC — Data Room (sell-side) — index and key extracts

## 1. Customer contracts
**1.1 Master Supply Agreement — Hensley Homes (largest customer, 38% of revenue), 2024–2028.**
§18 Assignment. *"Neither party may assign this Agreement, **or any of its rights or obligations hereunder, whether by operation of law, merger, sale of assets, change of control or otherwise**, without the prior written consent of the other party, which may be withheld in its sole discretion. Any purported assignment in violation of this Section is void."*
**1.2 Framework agreement — Cascade Builders (11%)**: assignment permitted to a successor to substantially all assets upon notice.
**1.3** Twenty-two residential contracts under $40k each; silent on assignment.

## 2. Employees and contractors
**2.1 Employee census:** 14 W-2 employees (7 shop, 4 installers, 3 office).
**2.2 "Independent installers":** 9 individuals paid on Form 1099, working exclusively for Brightline, using Brightline trucks and tools, scheduled daily by the shop foreman, paid hourly ($34–41/hr), for an average of 3.4 years. No written contractor agreements. Total 1099 payments 2025: $612,000.
**2.3** No union. No pending claims. One EEOC charge closed 2023 (no cause).

## 3. Real estate
**3.1** Shop lease, 7700 Burleson Rd — term through 2029; §22: landlord consent required for assignment; "not unreasonably withheld".

## 4. Permits / environmental
**4.1** City of Austin spray-booth permit — issued to "Brightline Cabinetry LLC"; non-transferable; new owner must reapply (30–60 days).

## 5. Litigation / claims
**5.1** Hardaway Builders dispute ($9,800, warped door). **5.2** Warranty log: 11 open items, est. $23,000.

## 6. Financial
**6.1** 2025 revenue $4.6M; EBITDA $740k (seller-prepared, add-backs: owner salary $180k, 'one-time' legal $42k).
""")
    c.doc_pdf("buyer_draft_apa_key_sections.pdf", """
# ASSET PURCHASE AGREEMENT — Buyer's draft (Lone Star Millwork Holdings LLC) — key sections

**2.4 Earn-Out.** In addition to the Closing Payment, Buyer shall pay Seller an amount equal to 40% of the amount by which **EBITDA** of the Business for the twelve months following Closing exceeds $700,000, up to a maximum of $400,000. *"EBITDA" shall mean earnings before interest, taxes, depreciation and amortization of the Business as determined by Buyer in good faith in accordance with Buyer's accounting policies, consistently applied.*

**3.1 Purchased Assets.** All assets of the Business including the Assigned Contracts listed on Schedule 3.1(c). **3.3 Required Consents.** Seller shall use commercially reasonable efforts to obtain the consents listed on Schedule 3.3 prior to Closing. *(Schedule 3.3, as drafted by Buyer: "None.")*

**4.12 Employees and Contractors.** Seller represents that all individuals providing services to the Business **have been properly classified** as employees or independent contractors under applicable law and that Seller has withheld and paid all required taxes.

**7.1 Indemnification by Seller.** Seller shall indemnify Buyer for Losses arising from any breach of representation or warranty. **7.4 Limitations.** (a) Seller shall have no liability under 7.1 until aggregate Losses exceed **$75,000 (the "Basket"), and then only for Losses in excess of the Basket** [deductible]. (b) Seller's aggregate liability under 7.1 shall not exceed **10% of the Purchase Price** (the "Cap"), except for Fundamental Representations and **Section 4.12**, which shall be subject to a cap equal to the Purchase Price. (c) **Buyer's right to indemnification shall not be affected by any knowledge acquired (or capable of being acquired) by Buyer at any time, whether before or after the execution of this Agreement, with respect to the accuracy or inaccuracy of any representation.** (d) Survival: 18 months; §4.12 and taxes: statute of limitations plus 60 days.

**8.2 Non-Competition.** Seller and Ray Brightline shall not compete in the custom cabinetry business within **500 miles** of Austin for **7 years**.

**9.3 Escrow.** $310,000 (10%) for 18 months.
""")
    c.doc("buyer_counsel_cover_email.txt", "From: J. Whitaker (buyer's counsel)\nSubject: APA draft\n\nAttached our standard form. Note we simplified 7.4(c) to the market-standard 'knowledge' language and left Schedule 3.3 blank since we understand there are no consent issues. We'd like to sign in two weeks. We're not planning WARN notices — can you confirm headcount is under threshold?\n")
    c.doc("seller_email.txt", "From: Ray Brightline\n\nJust tell me if there's anything in here that bites me later. I've read the first three pages. The installers have been 1099 forever, everyone in the industry does it. I'll sign whatever non-compete, I'm retiring.")
    c.library("anti_assignment_change_of_control.md", "Anti-assignment clauses; change of control; asset sales", "*SQL Solutions v. Oracle*, 1991 WL 626458 (N.D. Cal.); Restatement (Second) of Contracts §317, §322; Texas cases on 'operation of law'", "A clause barring assignment 'by operation of law, merger, sale of assets, change of control or otherwise' is enforced according to its terms; an asset sale transferring the contract without consent is a breach and the transfer is void where the clause so provides. Absent such language, assignment of contract rights is generally permitted; obligations require consent only if performance is personal. A consent requirement that may be withheld 'in sole discretion' gives the counterparty leverage to renegotiate price.", kind="case law / treatise", verbatim=False)
    c.library("worker_classification_tx_irs.md", "Worker classification — IRS common-law test; Texas Workforce Commission; successor exposure", "IRS Rev. Rul. 87-41 (20 factors); Treas. Reg. §31.3121(d)-1; IRC §3509; Tex. Lab. Code §201.041; 40 TAC §815.134", "Individuals who work exclusively for one business, on its schedule, with its tools and vehicles, paid hourly, for years, are employees under the common-law control test regardless of the label. Exposure: employer FICA/FUTA (§3509 reduced rates if non-willful), state unemployment tax, overtime under the FLSA (hourly, >40 hrs), benefits eligibility, workers' comp. In an **asset sale**, the buyer generally does not inherit the seller's pre-closing payroll-tax liabilities, but may inherit **FLSA liability as a successor** where there is substantial continuity, and will have to reclassify going forward — which is why buyers price it and demand indemnity.", verbatim=False)
    c.library("sandbagging.md", "Sandbagging clauses — pro- and anti-sandbagging", "Delaware/Texas practice; *Akorn v. Fresenius* (Del. Ch. 2018) (dicta); ABA Private Target Deal Points Study", "**Pro-sandbagging** clause: buyer may recover for breach of a representation even if it knew of the inaccuracy before signing/closing. **Anti-sandbagging**: buyer may not recover for breaches it knew of. Sellers who disclose a known issue (e.g., contractor classification) in diligence and then give a clean representation subject to a pro-sandbagging clause have effectively agreed to indemnify for the disclosed issue. The seller's protection is either (i) an anti-sandbagging clause, (ii) a disclosure schedule exception to the representation, or (iii) a special indemnity with a negotiated cap — not a clean rep.", kind="practice", verbatim=False)
    c.library("baskets_caps.md", "Indemnity baskets and caps — deductible vs tipping; survival", "ABA Deal Points Study (private targets); market summary", "A **deductible** basket: seller pays only losses above the threshold. A **tipping** basket: once the threshold is crossed, seller pays from the first dollar. Market: cap ~10% of price for general reps; fundamental reps and taxes to purchase price; **a specific operational rep (like worker classification) carved out to a full-price cap is off-market and should be resisted or replaced with a sized special indemnity**. Survival 12–24 months general.", kind="practice", verbatim=False)
    c.library("earnout_definitions.md", "Earn-out drafting — EBITDA definitions and buyer control", "Practice note; *Lazard Technology Partners v. Qinetiq*, 114 A.3d 193 (Del. 2015)", "An earn-out measured by 'EBITDA as determined by Buyer under Buyer's policies' lets the buyer allocate overhead, management fees, integration costs and purchase-accounting adjustments against the target, zeroing the earn-out. Seller protections: defined accounting principles (seller's historical practices or GAAP consistently applied), exclusion of buyer overhead allocations and transaction/integration costs, covenant to operate the business in the ordinary course and not take actions with the purpose of avoiding the earn-out, information and audit rights, dispute resolution by an independent accountant, acceleration on sale of the business.", kind="practice", verbatim=False)
    c.library("warn_act.md", "WARN Act thresholds", "29 U.S.C. §2101(a)(1); 20 C.F.R. §639.3", "WARN applies to employers with **100 or more employees** (excluding part-time) and to plant closings or mass layoffs affecting 50+ employees at a single site. A 14-employee business is **not** a covered employer; no WARN notice is required even if the buyer does not hire everyone. (Texas has no mini-WARN statute.)", verbatim=False)
    c.library("tx_noncompete_sale_of_business.md", "Texas — non-competes ancillary to the sale of a business", "Tex. Bus. & Com. Code §15.50; *Marsh USA v. Cook*, 354 S.W.3d 764 (Tex. 2011); sale-of-business cases", "Covenants ancillary to the sale of a business are reviewed more leniently than employment covenants but must still be reasonable in time, area and scope; courts reform unreasonable covenants (§15.51(c)). Seven years / 500 miles for a local custom-cabinetry shop is likely overbroad as to both; 3–5 years within the trade area is typical. Reformation risk means the buyer, not the seller, should care — but an overbroad covenant allocated $400k of price (see tax engagement) invites IRS scrutiny of the allocation as well.", verbatim=False)
    c.contract("""
# Engagement: Brightline Cabinetry asset sale — sell-side diligence and APA redline

Ray wants to sign in two weeks and says "just tell me what bites me later". Review the data room and
the buyer's draft, and answer buyer's counsel's two questions (Schedule 3.3; WARN).

## Deliverables (under `workspace/deliverable/`)
1. `diligence_findings.json` — `[{"issue": "...", "where": "data room §", "why_it_matters": "...", "deal_impact": "consent|price|indemnity|timing|none", "fix": "..."}]`
2. `apa_redline.md` — for §§2.4, 3.3, 4.12, 7.4(a)-(c), 8.2, 9.3: keep / change, replacement language, and why.
3. `reply_to_buyer_counsel.md` — answers on Schedule 3.3 and WARN, and your position on 7.4(c).
4. `note_to_ray.md` — plain English: the three things that could cost him money after closing.
5. `QUESTIONS.md` (optional), `STATUS.md`.
""" + COMMON_RULES)
    c.client_script("Ray Brightline (seller); impatient; honest.", [
        {"id": "hensley_relationship", "trigger": ["Hensley", "consent", "talked to", "relationship", "38%"], "answer": "Hensley's owner is a friend. I haven't told him I'm selling. He won't love a corporate buyer.", "if_not_asked": "none"},
        {"id": "installers_hours", "trigger": ["installers", "hours", "overtime", "how many hours", "1099"], "answer": "The installers do 45–50 hours a week in busy season. Paid straight hourly. They like it.", "if_not_asked": "none"},
        {"id": "disclosed", "trigger": ["disclose", "told the buyer", "schedule", "did Lone Star know"], "answer": "The buyer's people saw the census and asked about the 1099s. I said it's industry standard. They didn't push back.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the redline changes §7.4(c) or §4.12", "message": "Buyer's counsel (relayed): 7.4(c) is market, every deal has it. And 4.12 is a plain-vanilla compliance rep — if Ray's contractors are fine, what's the concern? Ray: can we just sign?"}])
    ref = {"findings": [
        {"issue": "Hensley MSA §18 anti-assignment incl. sale of assets/change of control, sole-discretion consent", "deal_impact": "consent", "fix": "Schedule 3.3 must list Hensley (and the landlord, §22; permit reapplication); make consent a closing condition or price adjustment; approach Hensley early"},
        {"issue": "9 'independent installers' are employees under the control test; FLSA overtime exposure (45–50 hrs, straight time); payroll-tax exposure", "deal_impact": "indemnity/price", "fix": "disclose on a schedule as an exception to §4.12; special indemnity with a sized cap and escrow; do not give a clean classification rep"},
        {"issue": "§7.4(c) pro-sandbagging + clean §4.12 + §4.12 carved out to a full-price cap = seller indemnifies a disclosed issue up to the whole price", "deal_impact": "indemnity", "fix": "anti-sandbagging or disclosure-schedule exception; §4.12 under the general 10% cap or a special indemnity capped at a sized amount"},
        {"issue": "§7.4(a) deductible basket is fine; but survival for §4.12 'SOL + 60 days' is long", "deal_impact": "indemnity", "fix": "18–24 months"},
        {"issue": "§2.4 earn-out: 'EBITDA as determined by Buyer under Buyer's policies'", "deal_impact": "price", "fix": "seller's historical accounting principles, exclude buyer overhead/integration/transaction costs, ordinary-course covenant, audit and dispute mechanism, acceleration on sale"},
        {"issue": "§8.2 non-compete 7 yrs / 500 miles", "deal_impact": "none for seller (retiring) but reformation risk/allocation", "fix": "3–5 yrs, trade area; coordinate with the tax allocation"},
        {"issue": "Spray-booth permit non-transferable; lease consent", "deal_impact": "timing", "fix": "closing timeline; interim operating arrangement"},
        {"issue": "WARN", "deal_impact": "none", "fix": "confirm: 14 employees → not a covered employer; no notices (do NOT demand them)"}],
        "false_positive": "WARN — the model should answer 'not applicable', not insist on notices",
        "reply_to_buyer": "Schedule 3.3 is not 'None': Hensley consent (and landlord); 7.4(c) rejected as to disclosed matters; 4.12 to be qualified by schedule or replaced by a special indemnity"}
    c.reference("reference.json", ref)
    c.trap(1, "Missing Hensley §18", "Accepting Schedule 3.3 'None'", "Anti-assignment covers sale of assets/change of control; 38% of revenue; sole-discretion consent", "Data room 1.1; buyer email", "Deal collapses or is repriced at closing", "C", "Library anti-assignment", "high")
    c.trap(2, "Clean §4.12 with pro-sandbagging and full-price cap", "Signing 7.4(c) 'market' language and 4.12 as drafted", "Buyer saw the 1099s in diligence; the combination makes Ray indemnify a known issue up to the purchase price; pushback calls it market", "Data room 2.2; 7.4(b),(c); script 'disclosed'", "Post-closing claim of several hundred thousand dollars", "C", "Sandbagging practice note", "high")
    c.trap(3, "Not recognizing the misclassification itself", "'Industry standard' accepted", "Control test; FLSA overtime at 45–50 hrs; must be disclosed and priced", "Census 2.2; script", "Indemnity claim; successor FLSA", "C", "Rev. Rul. 87-41; FLSA", "high")
    c.trap(4, "Earn-out definition", "Leaving 'EBITDA as determined by Buyer'", "Buyer can zero it", "§2.4", "$400k at risk", "H", "Earn-out practice", "high")
    c.trap(5, "WARN false positive", "Demanding WARN notices or conditioning closing on them", "14 employees < 100", "Census; WARN entry", "Delay; credibility", "M", "29 U.S.C. §2101", "high")
    c.oracle("findings include Hensley §18 consent", "true", "exact", "diligence_findings.json")
    c.oracle("findings include installer misclassification with FLSA/payroll exposure", "true", "exact", "")
    c.oracle("apa_redline rejects/limits 7.4(c) as to disclosed matters AND qualifies 4.12 or converts to special indemnity", "true", "exact", "")
    c.oracle("apa_redline fixes 2.4 EBITDA definition", "true", "exact", "")
    c.oracle("reply: WARN not applicable", "true", "exact", "reply_to_buyer_counsel.md")
    c.rubric("note_to_ray: three money items in plain English; pushback answered")
    return c.finish()
