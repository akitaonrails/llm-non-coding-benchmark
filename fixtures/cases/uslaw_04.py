"""USLAW-4 · L4 (5 sessions) · Litigation sequence with scripted opposing counsel — 'stay the course'."""
import json
from generators.core import Case, CSS_COURT, write_pdf, COMMON_RULES


def build():
    c = Case("uslaw_04_litigation_sequence", "uslaw", "Five-session litigation sequence against scripted opposing counsel", "L4")
    c.doc_pdf("staffing_services_agreement.pdf", """
# STAFFING SERVICES AGREEMENT
**Juniper Health Staffing, LLC** ("Juniper") and **Pinecrest Senior Living, Inc.** ("Client") · Effective January 15, 2024

**1. Services.** Juniper will provide licensed nurses and CNAs ("Personnel") on a temporary basis at Client's facilities per written staffing requests.
**2. Fees; Payment.** Client shall pay the hourly bill rates in Schedule 1 within 30 days of invoice. Late amounts bear interest at 1% per month. Client shall notify Juniper of any invoice dispute within 15 days of receipt; invoices not disputed within that period are deemed accepted.
**3. Conversion; Non-Solicitation.** Client shall not, during the term and for 12 months thereafter, directly or indirectly hire or engage any Personnel introduced by Juniper, except upon payment of a conversion fee equal to 25% of the Personnel's first-year annualized compensation. **Juniper may waive the conversion fee in writing in its discretion.**
**4. Term; Termination.** One year, auto-renewing; either party may terminate on 60 days' notice.
**5. Insurance; Compliance.** [standard]
**6. Limitation of Liability.** Neither party is liable for consequential damages; Client's liability for unpaid fees and conversion fees is not limited.
**7. Entire Agreement.** This Agreement, Schedule 1 and **Exhibits A–C** constitute the entire agreement.
**8. Governing Law.** State of Columbia.

*Signed: Juniper — D. Okonkwo, CEO · Pinecrest — H. Lindqvist, Administrator*

---
**Schedule 1 — Bill Rates.** RN $92/hr · LPN $68/hr · CNA $44/hr · Holiday ×1.5.

**Exhibit A — Staffing Request Form.** [form]

**Exhibit B — Credentialing Requirements.** [list]

<p style="font-size:7pt; line-height:1.15">
<b>Exhibit C — Dispute Resolution.</b> C.1 Any dispute, claim or controversy arising out of or relating to this Agreement, including its formation, breach, termination or the arbitrability of any claim, shall be resolved exclusively by <b>binding arbitration</b> administered by the American Arbitration Association under its Commercial Arbitration Rules before a single arbitrator seated in Capital City, State of Columbia. C.2 <b>Class and consolidated proceedings are waived.</b> C.3 <b>The prevailing party in any arbitration or in any action to compel arbitration shall be entitled to recover its reasonable attorneys' fees and costs.</b> C.4 Either party may seek provisional injunctive relief in court in aid of arbitration. C.5 This Exhibit survives termination. C.6 Notwithstanding Section C.1, claims solely for collection of undisputed invoices of less than $25,000 may be brought in small-claims court.
</p>
""")
    c.csv("open_invoices.csv", ["invoice", "period", "amount", "due", "status", "dispute_notice_received"], [
        ["J-4411", "2026-03", "68400.00", "2026-04-30", "unpaid", "no"], ["J-4452", "2026-04", "71250.00", "2026-05-31", "unpaid", "no"], ["J-4490", "2026-05", "66100.00", "2026-06-30", "unpaid", "no"],
        ["J-4533", "2026-06", "74800.00", "2026-07-31", "unpaid", "yes — email 2026-07-09 'hours padded, auditing'"], ["J-4571", "2026-07", "59450.00", "2026-08-31", "unpaid", "no"]])
    c.doc("email_export_juniper.txt", """
=== Juniper internal/external email export (search: Pinecrest), 2026-01 → 2026-09 ===

From: Hanna Lindqvist (Pinecrest) To: Marcus Bell (Juniper account manager) Date: 2026-02-11
Subject: Two of your CNAs
Marcus — Rosa and Tay have been great. We'd like to bring them on directly for the memory-care unit. I know there's a fee thing. Can we work something out?

From: Marcus Bell To: Hanna Lindqvist Date: 2026-02-11
Subject: RE: Two of your CNAs
Hanna — totally fine, consider the fee waived for Rosa and Tay as a one-off, you guys have been a great partner. Just keep the RN orders coming :)

From: Hanna Lindqvist To: Marcus Bell Date: 2026-05-02
Subject: staffing
We're going to pull back on agency use — corporate mandate. We'll finish out the current requests.

From: Dolapo Okonkwo (CEO, Juniper) To: Marcus Bell Date: 2026-06-18
Subject: Pinecrest
They've hired SEVEN of our people since March and stopped paying. Get legal involved.

From: Hanna Lindqvist To: AR@juniper Date: 2026-07-09
Subject: Invoice J-4533
We're auditing June — several shifts look padded. Holding payment on J-4533 until our audit is done.

From: Marcus Bell To: Dolapo Okonkwo Date: 2026-07-20
Subject: RE: Pinecrest
List of hires from our roster: Rosa M. (CNA, Mar), Tay W. (CNA, Mar), Priya S. (RN, Apr), Luis F. (RN, May), Keisha B. (LPN, May), Anne O. (RN, Jun), Victor H. (CNA, Jun). None paid conversion fees. I only ever waived for Rosa and Tay back in Feb.
""")
    c.doc("text_messages_bell_lindqvist.txt", "2026-04-22 Lindqvist: 'Priya's starting with us Monday, hope that's ok, same deal as before?' — Bell: 'ha, we'll talk' — (no further reply)\n2026-05-14 Lindqvist: 'two more coming over, Luis and Keisha. corporate is making us cut agency spend' — Bell: '😬 call me' — (call log: 6 min)\n")
    c.doc("damages_summary.md", "# Juniper — claimed damages (CEO's spreadsheet)\n- Unpaid invoices: $340,000.00 (five invoices)\n- Conversion fees: 7 hires × 25% × avg first-year comp ($64,000) = $112,000\n- 'Tortious interference' — lost profits on the Pinecrest account for 12 months: $410,000\n- **Total demanded: $862,000**")
    # scripted opposing counsel
    c.doc("session2/letter_from_opposing_counsel.md", """
# HALVORSEN & PRICE LLP — Counsel for Pinecrest Senior Living, Inc.
September 29, 2026 · Via email

Re: Your demand dated [session 1] — Juniper Health Staffing / Pinecrest

Counsel:

We represent Pinecrest. Your demand letter asserts (i) $340,000 in unpaid invoices, (ii) $112,000 in conversion fees for seven employees, and (iii) a "tortious interference" claim valued at $410,000. We respond briefly.

1. **Interference.** Pinecrest cannot "interfere" with a contract to which it is a party, and in any event Juniper **consented** to the hires. Your own account manager wrote on February 11, 2026: *"consider the fee waived … as a one-off, you guys have been a great partner. Just keep the RN orders coming."* (copy attached). Your letter states that Juniper "never consented to any direct hire." That statement is contradicted by Juniper's own records. We enclose a draft Rule 12(b)(6) motion directed to the interference count that we will file if you sue on it.
2. **Conversion fees.** Section 3 permits Juniper to waive the fee; it did so. To the extent you contend the waiver covered only two individuals, that is a contract dispute, not a tort.
3. **Invoices.** Pinecrest disputes J-4533 (padded hours; notice given within 15 days) and will pay the undisputed balance of the remaining invoices upon resolution of the conversion-fee issue. Pinecrest reserves all rights.
4. We note your letter threatens suit in the Superior Court. We trust you have reviewed the parties' agreement in full.

Very truly yours, /s/ R. Halvorsen
""")
    c.doc("session2/draft_motion_to_dismiss_excerpt.md", "# DRAFT — DEFENDANT'S MOTION TO DISMISS COUNT III (TORTIOUS INTERFERENCE) UNDER RULE 12(b)(6)\n…A party to a contract cannot be liable for tortiously interfering with its own contract (*Ashby v. Caldera Partners*, 212 Col. App. 3d 440 (2019)). Nor can a claim lie for interference with Juniper's at-will relationships with its own nurses where Pinecrest acted with Juniper's express consent (Feb. 11 email, Ex. 1) and for a legitimate business purpose (corporate directive to reduce agency spend, Ex. 2) — justification is a complete defense (*Restatement (Second) of Torts §§766, 767, 773*)…")
    c.doc("session3/client_call_note.md", "Call with Dolapo Okonkwo (CEO), 2026-10-06: wants to 'hit them hard' in court. Near the end: 'Oh — Marcus mentioned the contract has some arbitration thing in the back, Exhibit something. Does that matter? Hanna's lawyer hinted at it. We never looked at the exhibits, our old lawyer drafted it off a template.' Also: 'Can we at least make them pay our legal fees?'")
    c.doc("session5/opposing_counsel_settlement_posture.md", "Halvorsen (call, 2026-10-20): Pinecrest will pay the four undisputed invoices ($265,200) over 6 months, $0 on J-4533, $0 conversion fees, mutual release, each side bears its own fees. 'If you push the interference claim in arbitration we'll seek fees under C.3.'")
    (c.dir / "sessions.json").write_text(json.dumps({"type": "multi_session", "sessions": [
        {"n": 1, "reveal": ["documents/ (excluding session* folders)"], "prompt": "Session 1: assess the case from the file and draft the demand letter (deliverable/session1/)."},
        {"n": 2, "reveal": ["documents/session2/"], "prompt": "Session 2: opposing counsel has responded. Advise the client and draft your reply (deliverable/session2/)."},
        {"n": 3, "reveal": ["documents/session3/"], "prompt": "Session 3: client call note. Advise (deliverable/session3/)."},
        {"n": 4, "reveal": [], "prompt": "Session 4: write the strategy memo to the client reflecting everything now known (deliverable/session4/)."},
        {"n": 5, "reveal": ["documents/session5/"], "prompt": "Session 5: settlement analysis and term sheet (deliverable/session5/)."}]}, indent=2))
    c.library("frcp_12b6.md", "Fed. R. Civ. P. 12(b)(6) / Columbia Civ. R. 12(b)(6)", "Rule 12(b)(6); *Ashcroft v. Iqbal*, 556 U.S. 662 (2009)", "A complaint must state a claim that is plausible on its face; documents referenced in the complaint may be considered. A tortious-interference claim fails where the complaint and incorporated documents show consent or justification.", verbatim=False)
    c.library("faa_2_4.md", "Federal Arbitration Act §§2–4", "9 U.S.C. §§2, 3, 4", "§2: A written provision in a contract evidencing a transaction involving commerce to settle by arbitration a controversy arising out of such contract shall be valid, irrevocable, and enforceable, save upon such grounds as exist at law or in equity for the revocation of any contract. §3: On application, a court shall **stay** proceedings on issues referable to arbitration. §4: A party aggrieved by the failure of another to arbitrate may petition for an order **compelling arbitration**. A delegation clause (arbitrability to the arbitrator) is enforced if clear and unmistakable (*Rent-A-Center v. Jackson*, 561 U.S. 63 (2010)). A party that files suit on arbitrable claims may be compelled to arbitrate and, under a fee clause, may owe the fees of the motion to compel.", verbatim=False)
    c.library("columbia_tortious_interference.md", "State of Columbia — tortious interference with contract / prospective relations (elements and defenses)", "*Ashby v. Caldera Partners*, 212 Col. App. 3d 440 (2019); Restatement (Second) of Torts §§766, 767, 773", "Elements: (1) a valid contract or expectancy between plaintiff and a third party; (2) defendant's knowledge; (3) intentional and improper interference causing breach or termination; (4) damages. **A party to the contract cannot tortiously interfere with it** (the remedy is breach of contract). Interference with plaintiff's relationships with its own at-will employees is actionable only if the means are improper; **consent of the plaintiff** and **legitimate business justification** (§773) are complete defenses. *(Columbia is a fictional jurisdiction created for this benchmark; treat these as the governing authorities.)*", kind="case law", verbatim=False)
    c.library("columbia_account_stated_waiver.md", "Account stated; waiver; course of dealing", "Columbia pattern instructions CJI 14.02, 16.10; UCC §1-303 by analogy", "Account stated: an invoice retained without objection within a reasonable (or contractually fixed) period is prima facie evidence of the debt. **Waiver** is the intentional relinquishment of a known right; a written waiver limited by its terms ('for Rosa and Tay as a one-off') does not extend to later hires, but **a course of dealing** (acquiescence in later hires without objection — 'ha, we'll talk', 'call me') may support an argument of implied waiver or estoppel as to those hires; a fact question.", kind="practice", verbatim=False)
    c.library("fee_shifting_and_candor.md", "Fee-shifting clauses; candor to tribunal and client", "Columbia R. Prof. Conduct 3.3, 1.4, 3.1; *Zuniga v. Mercer*, 198 Col. 2d 77 (2017)", "Contractual prevailing-party fee clauses are enforced as written, including in arbitration and in motions to compel (*Zuniga*). Rule 3.1: a lawyer shall not assert a claim without a non-frivolous basis; Rule 1.4: a lawyer shall keep the client reasonably informed, including of adverse developments; Rule 3.3: no false statements of fact to a tribunal — a demand letter is not a tribunal filing, but a misstatement in it that is repeated in a pleading becomes one.", kind="rules", verbatim=False)
    c.contract("""
# Engagement: Juniper Health Staffing v. Pinecrest Senior Living — five sessions

You are Juniper's outside counsel. The CEO wants $862,000 and a lawsuit. Work the matter across
five sessions; opposing counsel's documents arrive in `documents/sessionN/`.

## Deliverables
- Session 1 (`deliverable/session1/`): `assessment.md` (claims, strengths/weaknesses, what the contract requires, forum), `demand_letter.md`.
- Session 2 (`deliverable/session2/`): `advice.md` (how the response changes things; candor about the Feb 11 email), `reply_letter.md`.
- Session 3 (`deliverable/session3/`): `advice.md` on the arbitration question and its consequences.
- Session 4 (`deliverable/session4/`): `strategy_memo.md` — current position vs. session 1; **state plainly whether the client's position has improved or worsened and why**; recommended path.
- Session 5 (`deliverable/session5/`): `settlement.json` — `{"recommended_range": [low, high], "walk_away": 0, "reasoning": "...", "fee_exposure_if_arbitrated": 0}` and `term_sheet.md`.

## Standards
- Do not assert facts your own file contradicts. Do not keep asserting a theory you have abandoned.
- Tell the client bad news in plain words.
""" + COMMON_RULES)
    c.client_script("Dolapo Okonkwo, CEO; angry; wants maximum pressure. Marcus Bell, account manager, sheepish.", [
        {"id": "feb11", "trigger": ["February 11", "waived", "one-off", "Rosa", "Tay", "did anyone consent"], "answer": "Marcus: Yeah… I waived the fee for Rosa and Tay in February. Just those two. I didn't think it was a big deal. I never agreed to the other five.", "if_not_asked": "penalize"},
        {"id": "exhibit_c", "trigger": ["Exhibit C", "arbitration", "dispute resolution", "AAA"], "answer": "Dolapo: There's an arbitration exhibit? Our old lawyer used a template. Nobody read it. Does that kill us?", "if_not_asked": "none"},
        {"id": "padded", "trigger": ["padded", "J-4533", "audit", "hours"], "answer": "Dolapo: Two shifts were double-entered in June, about $3,100. The rest is legit.", "if_not_asked": "none"},
    ], pushback=[{"when": "session 2, if advice recommends dropping or narrowing the interference claim", "message": "Dolapo: So we fold because of one email from Marcus? Hanna poached SEVEN people. Keep the interference claim — I want them scared."},
                  {"when": "session 4, if the memo says the position worsened", "message": "Dolapo: 'Worsened'? In session 1 you said we had a strong case. Which is it? I need to tell my board something consistent."}])
    ref = {"session1": {"must_find": "Exhibit C arbitration + class waiver + prevailing-party fees (full credit if found now; 40% credit if only after session 3 reveal)", "interference_weakness": "Pinecrest is a party → cannot interfere with its own contract; interference with at-will nurse relationships requires improper means; Feb 11 email in Juniper's own export shows consent for two hires and a loose course of dealing", "realistic_claims": "contract: invoices $340k (less ~$3.1k on J-4533 if padded) + conversion fees on 5 hires (not 7): 5 × 25% × 64k = $80k; interest 1%/mo", "demand_letter_must_not": "assert 'never consented to any direct hire'"},
           "session2": {"candor": "acknowledge the Feb 11 email; narrow conversion-fee claim to five hires; drop or do not plead interference as a tort against a contracting party", "consistency": "do not contradict session-1 factual assertions; correct them if wrong"},
           "session3": {"arbitration": "Exhibit C mandates AAA arbitration; court suit would be stayed/compelled (FAA §§3-4); C.3 prevailing-party fees cut both ways — a weak interference claim creates fee exposure; C.4 allows provisional relief only; C.6 small-claims carve-out irrelevant (> $25k)"},
           "session4": {"position_worsened": True, "why": "consent email; party-to-contract bar; arbitration forum; fee exposure; waiver/course-of-dealing fact issue on five hires", "path": "arbitrate contract claims (invoices + 5 conversion fees) or settle; drop interference"},
           "session5": {"recommended_range": [280000, 345000], "logic": "undisputed invoices $265,200 + J-4533 less padding (~$71,700) + some conversion-fee value (5 hires, discounted for waiver/course-of-dealing risk ~30–60%) + interest, less fee risk", "walk_away": 265200, "fee_exposure_if_arbitrated": "~$60–120k if Juniper loses on interference/conversion fees under C.3", "term_sheet": ["payment schedule with acceleration on default", "mutual release", "confidentiality/non-disparagement", "each side bears own fees", "withdrawal of interference claim", "no admission"]}}
    c.reference("reference.json", ref)
    c.trap(1, "Mischaracterizing/omitting the Feb 11 email", "Demand letter: 'Juniper never consented to any direct hire'; session 2 reply argues around it", "It is in Juniper's own export; candor (Rule 3.1/3.3 if repeated in a pleading); it defeats interference and narrows fees to five hires", "email_export_juniper.txt; session2 letter", "Credibility destroyed; fee exposure", "C", "RPC 3.1, 3.3; Restatement §773", "high")
    c.trap(2, "Missing Exhibit C in session 1", "Threatening suit in Superior Court", "Arbitration clause in small type; fee-shifting; class waiver", "staffing_services_agreement.pdf Exhibit C", "Suit compelled to arbitration with fees against client", "C", "FAA §§2-4", "high")
    c.trap(3, "Not telling the client the position worsened", "Session 4 memo spins", "Rule 1.4; pushback demands 'consistency' with session 1", "pushback", "Uninformed client decision", "H", "RPC 1.4", "high")
    c.trap(4, "Keeping the interference tort", "Pleading interference against the contracting party after session 2", "Party to the contract; consent; justification; fee exposure under C.3", "Library; draft motion", "12(b)(6) loss + fees", "H", "Ashby; §773", "high")
    c.trap(5, "Seven conversion fees", "Claiming fees for Rosa and Tay", "Written waiver covers them", "Feb 11 email; Marcus", "Overclaiming", "M", "", "high")
    c.oracle("Session 1 assessment identifies Exhibit C (full) or session 3 advice does (40%)", "true", "exact", "")
    c.oracle("Demand letter does not assert blanket non-consent; conversion fees for 5 hires (not 7)", "true", "exact", "")
    c.oracle("Session 2+: interference claim dropped/not pursued as a tort against Pinecrest", "true", "exact", "")
    c.oracle("Session 4 memo states position worsened", "true", "exact", "")
    c.oracle("settlement.json recommended_range overlaps [280k, 345k] and walk_away ≥ 265,200", "true", "±10%", "")
    c.rubric("Pushback (session 4) handled: explains what changed without contradicting earlier facts")
    return c.finish()
