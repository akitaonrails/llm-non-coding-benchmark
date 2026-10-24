"""USLAW-2 · L2 · SaaS MSA review against the playbook — 'flag everything aggressive'."""
from generators.core import Case, COMMON_RULES


def build():
    c = Case("uslaw_02_msa_playbook", "uslaw", "SaaS master services agreement review against the client's playbook", "L2")
    msa = """
# MASTER SUBSCRIPTION AGREEMENT
**Between** RouteWise Technologies, Inc., a Delaware corporation ("Provider") **and** Cobalt Logistics Holdings LLC ("Customer"). Effective Date: the date of the last signature below. Version 7.3 (Provider form).

## 1. Definitions
1.1 "Services" means Provider's RouteWise routing and fleet-optimization platform, as described in an Order Form. 1.2 "Customer Data" means data submitted by Customer or its Users to the Services, including personal data of Customer's drivers and customers. 1.3 "Affiliate" means an entity controlling, controlled by or under common control with a party. 1.4 "Documentation" means Provider's then-current online user guides. 1.5 "Order Form" means an ordering document executed by the parties. 1.6 "Users" means Customer's employees and contractors authorized to use the Services.

## 2. Services and Access
2.1 Provider shall make the Services available to Customer and its Users during the Subscription Term in accordance with the Documentation and the Service Level Agreement attached as **Exhibit B**. 2.2 **The license granted hereunder is to Customer only and does not extend to Customer's Affiliates** unless named on an Order Form at additional fees. 2.3 Provider may modify the Services from time to time provided such modifications do not materially degrade functionality.

## 3. Term and Renewal
3.1 This Agreement commences on the Effective Date and continues until all Order Forms have expired or been terminated. 3.2 Each Subscription Term is stated in the Order Form. **3.3 Each Subscription Term shall automatically renew for successive renewal terms of twenty-four (24) months unless either party gives written notice of non-renewal at least ninety (90) days before the end of the then-current term.**

## 4. Fees and Payment
4.1 Customer shall pay the fees stated in each Order Form. 4.2 Fees are due net thirty (30) days from invoice. 4.3 Overdue amounts accrue interest at 1.5% per month. 4.4 Fees for renewal terms are as stated in the applicable Order Form. 4.5 All fees are exclusive of taxes.

## 5. Customer Data and Data Protection
5.1 Customer owns Customer Data. 5.2 Provider shall maintain commercially reasonable administrative, physical and technical safeguards. 5.3 **To the extent Provider processes personal data subject to the GDPR or UK GDPR on Customer's behalf, the parties shall enter into a data processing addendum in the form to be attached as Exhibit C.** 5.4 Provider may use aggregated, de-identified usage data for any purpose.

## 6. Confidentiality
6.1 Each party shall protect the other's Confidential Information with at least reasonable care and use it only to perform under this Agreement. 6.2 Obligations survive for five (5) years after termination; trade secrets survive as long as they remain trade secrets.

## 7. Warranties
7.1 Provider warrants that the Services will perform materially in accordance with the Documentation. 7.2 Customer's exclusive remedy for breach of 7.1 is correction of the non-conformity or, if Provider cannot correct it within sixty (60) days, termination of the affected Order Form and a refund of prepaid unused fees. 7.3 EXCEPT AS EXPRESSLY PROVIDED, THE SERVICES ARE PROVIDED "AS IS" AND PROVIDER DISCLAIMS ALL OTHER WARRANTIES.

## 8. Term of Order Forms; Suspension
8.1 Provider may suspend access for non-payment after fifteen (15) days' notice. 8.2 Provider may suspend immediately if Customer's use threatens the security or integrity of the Services.

## 9. Limitation of Liability
**9.1 NOTWITHSTANDING ANYTHING TO THE CONTRARY IN THIS AGREEMENT, IN NO EVENT SHALL EITHER PARTY'S AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT EXCEED THE FEES PAID OR PAYABLE BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING THE EVENT GIVING RISE TO THE CLAIM.** 9.2 IN NO EVENT SHALL EITHER PARTY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL OR CONSEQUENTIAL DAMAGES, OR LOST PROFITS, HOWEVER CAUSED. **9.3 The exclusions and limitations in this Section 9 shall not apply to a party's liability for its gross negligence, willful misconduct, or fraud, or to Customer's payment obligations.**

## 10. Indemnification
10.1 **Provider shall defend Customer against any third-party claim alleging that the Services infringe a patent, copyright or trademark or misappropriate a trade secret, and shall pay all damages, costs and attorneys' fees finally awarded or agreed in settlement; Provider's obligations under this Section 10.1 are uncapped.** 10.2 Customer shall defend Provider against third-party claims arising from Customer Data or Customer's breach of Section 11. 10.3 The indemnified party shall give prompt notice and reasonable cooperation; the indemnifying party controls the defense.

## 11. Acceptable Use
11.1 Customer shall not reverse engineer, resell, or use the Services to build a competing product. 11.2 Customer is responsible for its Users' compliance.

## 12. Termination
12.1 Either party may terminate for material breach uncured within thirty (30) days of notice. 12.2 Upon termination Customer may export Customer Data for thirty (30) days, after which Provider may delete it. 12.3 Sections 4, 5, 6, 9, 10, 13 and 14 survive.

## 13. Governing Law; Disputes
13.1 Delaware law governs, excluding conflict-of-laws rules. 13.2 Exclusive venue in the state and federal courts in Wilmington, Delaware. 13.3 Each party waives jury trial.

## 14. General
14.1 Entire agreement: this Agreement, its Exhibits and Order Forms; **in the event of conflict, an Order Form controls over this Agreement as to the subject matter of that Order Form.** 14.2 Assignment: neither party may assign without consent, except to a successor in a merger or sale of substantially all assets. 14.3 Notices in writing to the addresses on the signature page. 14.4 Force majeure. 14.5 Independent contractors. 14.6 Counterparts.

---
# EXHIBIT A — ORDER FORM No. 1
Customer: Cobalt Logistics Holdings LLC · Products: RouteWise Enterprise (up to 350 vehicles) · **Initial Subscription Term: 36 months** from the Service Start Date · Fees: **$18,500 per month**, billed annually in advance ($222,000 / year).
**4. Pricing adjustments.** Provider may increase the fees for any renewal term, and **once during the Initial Subscription Term upon sixty (60) days' notice, by up to the greater of 8% or the change in the CPI-U**.
Service Start Date: as notified by Provider upon provisioning. Implementation fee: $25,000 (one-time).

# EXHIBIT B — SERVICE LEVEL AGREEMENT
Availability target 99.5% monthly, excluding scheduled maintenance (up to 8 hours/month, 48 hours' notice). Credits: 5% of monthly fees for each full 0.5% below target, capped at 25%. Credits are the sole remedy for availability failures and must be claimed within 30 days.

# EXHIBIT C — DATA PROCESSING ADDENDUM
**[To be attached.]**
"""
    c.doc_pdf("routewise_msa_v7.3.pdf", msa, also_md=True)
    c.doc_pdf("cobalt_contract_playbook.pdf", """
# Cobalt Logistics — Vendor Contract Playbook (Legal, rev. 2026-03)
Applies to all SaaS/technology vendor agreements above $100k/year. Hard rules require GC sign-off to waive.

## A. Hard rules ("never accept without GC approval")
A1. **Uncapped IP infringement indemnity from the vendor**, with no carve-back through the limitation-of-liability clause. The indemnity must survive and must not be subject to the liability cap.
A2. **Data processing addendum executed at signing** whenever personal data of EU/UK residents is processed (Cobalt processes EU customer and driver data for its Rotterdam and Hamburg operations). "To be attached" is not acceptable.
A3. **No unilateral price increases during an initial term.** Renewal increases capped at 5% or CPI, whichever is lower, with 90 days' notice.
A4. **Auto-renewal terms no longer than 12 months, with non-renewal notice of 30 days or less.**
A5. **Affiliates** (Cobalt Freight Europe B.V. and Cobalt Brokerage LLC) must be covered by the license at no additional fee, or the agreement must be signed by Holdings on behalf of affiliates.

## B. Preferred positions (negotiate; may concede with Legal approval)
B1. Mutual limitation of liability at 12–24 months' fees is acceptable. **Carve-outs for gross negligence, willful misconduct and fraud are our preferred position and should be accepted when offered** (they cut both ways and protect Cobalt).
B2. Data export window: 60 days preferred; 30 days acceptable.
B3. Governing law: Delaware or New York acceptable; jury waiver acceptable.
B4. Suspension for non-payment: at least 30 days' notice preferred; 15 acceptable if cure is allowed.
B5. SLA: 99.5% with credits is acceptable; credits-as-sole-remedy acceptable if termination right exists for chronic failure (3 months in any 6).

## C. Drafting notes
C1. Always read the order form against the MSA: order forms often override the MSA (check the precedence clause).
C2. Check that "notwithstanding" clauses do not swallow protections elsewhere in the document.
""")
    c.doc("email_gc.txt", "From: Priya Raman (GC, Cobalt)\nSubject: RouteWise MSA — issues list by Thursday\n\nAttached is RouteWise's paper and our playbook. I need a ranked issues list, redlines for anything that breaks a hard rule, and a one-pager for the COO (who wants to sign this week). Don't bury me in nits — tell me what actually matters. We will run EU driver data through this.\n")
    c.library("gdpr_art28.md", "GDPR Article 28 — processor (excerpt)", "Regulation (EU) 2016/679, Art. 28(3)", "Processing by a processor shall be governed by a **contract or other legal act** under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects and the obligations and rights of the controller. That contract shall stipulate, in particular, that the processor: (a) processes only on documented instructions; (b) ensures confidentiality; (c) takes security measures; (d) respects sub-processor conditions; (e)-(f) assists the controller; (g) deletes or returns data; (h) makes available information and allows audits. **Absent such a contract, the controller is in breach of Art. 28 from the first day of processing.**", verbatim=False)
    c.library("ucc_2_distractor.md", "UCC Article 2 — scope (excerpt)", "U.C.C. §2-102; §2-316", "Article 2 applies to transactions in **goods**. Courts applying the predominant-purpose test generally hold that a subscription to hosted software (SaaS) is a **service**, not a sale of goods, so Article 2's implied warranties and gap-fillers do not apply directly (though some courts apply them by analogy to software licenses). *(Included as context; the MSA is a services agreement.)*", verbatim=False)
    c.library("contract_interpretation_notwithstanding.md", "Interpretation — 'notwithstanding' clauses and specific vs. general", "Restatement (Second) of Contracts §203; Delaware cases on 'notwithstanding anything to the contrary'", "Where a clause begins 'notwithstanding anything to the contrary in this Agreement,' courts give it **controlling effect over conflicting provisions**, including more specific ones, because the parties expressly resolved the conflict. A statement elsewhere that an obligation is 'uncapped' does not override a cap that is expressly made to apply 'notwithstanding anything to the contrary' unless the cap clause itself carves the obligation out. Delaware courts enforce contracts as written between sophisticated parties.", kind="treatise / case law", verbatim=False)
    c.contract("""
# Engagement: review the RouteWise MSA for Cobalt Logistics against the playbook

The GC wants what matters, ranked, with redlines for hard-rule breaks and a one-pager for the COO.

## Deliverables (under `workspace/deliverable/`)
1. `issues.json` — `[{"rank": 1, "clause": "§9.1/§10.1", "playbook_rule": "A1", "severity": "hard|preferred|note", "issue": "...", "why": "...", "redline": "replacement text or 'none'"}]` — include **only** real issues; flagging a clause the playbook accepts counts against you.
2. `redlines.md` — replacement clause text for each hard-rule violation.
3. `coo_onepager.md` — plain English: what the deal does, the 3–5 things that must change before signature, and business impact.
4. `QUESTIONS.md` (optional), `STATUS.md`.
""" + COMMON_RULES)
    c.client_script("Priya Raman, GC. Busy; values signal over noise.", [
        {"id": "affiliates", "trigger": ["affiliate", "Cobalt Freight Europe", "Brokerage", "who will use", "entities"], "answer": "Both affiliates will use it — Europe for Rotterdam/Hamburg, Brokerage for carrier routing. Holdings signs.", "if_not_asked": "penalize"},
        {"id": "eu_data", "trigger": ["EU", "GDPR", "personal data", "driver data", "Rotterdam"], "answer": "Yes — driver names, locations, hours, and customer addresses from the EU ops. Real GDPR scope.", "if_not_asked": "none"},
        {"id": "chronic", "trigger": ["chronic", "termination for SLA", "repeated outages"], "answer": "There is no chronic-failure termination right in their paper. Add one if you think it matters.", "if_not_asked": "none"},
    ], pushback=[{"when": "if issues.json flags §9.3 (the gross negligence carve-out) as a problem", "message": "Priya: Why is the gross-negligence carve-out on your list? That's our own preferred position in B1. Did you read the playbook?"}])
    ref = {"hard_rule_issues": [
        {"clause": "§9.1 + §10.1", "rule": "A1", "issue": "§9.1 cap applies 'notwithstanding anything to the contrary' and §9.3 carves out only gross negligence/willful misconduct/fraud/payment — NOT the §10.1 IP indemnity. §10.1's 'uncapped' language is overridden by §9.1. The indemnity is effectively capped at 12 months' fees ($222,000).", "redline": "Add to §9.3: '…or to Provider's obligations under Section 10.1 (IP Indemnification), which shall not be subject to the limitations in Section 9.1 or 9.2.'"},
        {"clause": "§5.3 / Exhibit C", "rule": "A2", "issue": "DPA 'to be attached' — no Art. 28 contract at signing while EU driver/customer data flows from day one.", "redline": "Attach executed DPA (incl. SCCs) as Exhibit C as a condition of effectiveness; add 'The DPA is incorporated and executed concurrently with this Agreement.'"},
        {"clause": "Order Form §4 (+ MSA §14.1 precedence)", "rule": "A3", "issue": "Unilateral mid-term increase up to greater of 8% or CPI on 60 days' notice, hidden in the order form, which controls over the MSA.", "redline": "Delete mid-term increase; renewal increases ≤ lesser of 5% or CPI with 90 days' notice."},
        {"clause": "§3.3", "rule": "A4", "issue": "24-month auto-renewal with 90-day notice window.", "redline": "12-month renewals; non-renewal notice 30 days."},
        {"clause": "§2.2", "rule": "A5", "issue": "Affiliates excluded unless paid for separately.", "redline": "License extends to Customer and its Affiliates at no additional fee; Holdings signs for affiliates."}],
        "false_positives": ["§9.3 carve-out (playbook B1 — preferred position)", "§13 Delaware law / jury waiver (B3 acceptable)", "§8.1 15-day suspension notice (B4 acceptable)", "§12.2 30-day export (B2 acceptable)"],
        "notes_ok_to_mention": ["SLA chronic-failure termination right (B5) — preferred, not hard", "§5.4 aggregated data — negotiate definition"]}
    c.reference("reference.json", ref)
    c.trap(1, "Missing that §9.1 swallows §10.1", "Reading §10.1 'uncapped' and ticking A1 as satisfied", "'Notwithstanding anything to the contrary' in §9.1 + §9.3 carve-outs omit §10.1 → the IP indemnity is capped at $222k", "§9.1, §9.3, §10.1; playbook C2; interpretation entry", "Client believes it has uncapped IP protection; a real infringement claim could cost millions", "C", "Playbook A1; Restatement §203", "high")
    c.trap(2, "Accepting 'DPA to be attached'", "Treating §5.3 as compliant", "No Art. 28 contract at signing; EU data flows immediately", "§5.3; Exhibit C; GC email", "GDPR breach from day one", "C", "Playbook A2; GDPR Art. 28(3)", "high")
    c.trap(3, "Missing the price-change right in the order form", "Reviewing only the MSA body", "Order form §4 + §14.1 precedence → mid-term increase", "Exhibit A §4; §14.1; playbook C1", "Budget risk ~$17.8k+/yr", "H", "Playbook A3", "high")
    c.trap(4, "Flagging the gross-negligence carve-out", "Listing §9.3 as a problem", "Playbook B1 says accept it; pushback tests whether the model read the playbook", "Playbook B1", "Credibility; wasted negotiation", "H", "Playbook B1", "high")
    c.trap(5, "Auto-renewal / affiliates", "Missing §3.3 (24/90) or §2.2 (affiliates excluded)", "A4 and A5 hard rules; affiliates confirmed by client", "§3.3; §2.2; script", "Lock-in; unlicensed affiliate use", "M", "Playbook A4, A5", "high")
    c.oracle("issues.json contains A1 (§9.1 vs §10.1 interaction), A2, A3 (order form), A4, A5", "all five present", "exact", "")
    c.oracle("issues.json does NOT flag §9.3 carve-out, Delaware law, jury waiver, 15-day suspension or 30-day export as issues", "true", "exact", "")
    c.oracle("A1 redline carves §10.1 out of §9.1/9.2", "true", "exact", "redlines.md")
    c.rubric("COO one-pager names the capped-indemnity problem in plain English")
    c.note("MSA is ~5 rendered pages rather than the 28 of the design doc; sufficient for the cross-clause trap. Modeled on EDGAR-style SaaS MSAs; names invented.")
    return c.finish()
