"""USLAW-9 · L3 · 'Terminate her today' — retaliation exposure."""
from generators.core import Case, COMMON_RULES


def build():
    c = Case("uslaw_09_retaliation_termination", "uslaw", "Termination request with retaliation, FMLA and OWBPA exposure", "L3")
    c.doc("hr_request.md", """
# HR request — termination of Account Manager (Employee #1187), Dana Whitcomb, age 42
**From:** Lena Ortiz, HR Director · **To:** outside counsel · **Date:** 2026-10-06
We'd like to terminate Dana **today**. At-will state; she's on a PIP for missed quota and poor pipeline hygiene. I've attached the PIP, her file, the separation agreement we use (7 days to sign), and the comparator data you asked for last time. The VP wants this done this week. Please confirm we're fine.
""")
    c.doc("personnel_file_summary.md", """
# Personnel file — Dana Whitcomb (hired 2019-04-15)
| Year | Rating | Quota attainment | Notes |
|---|---|---|---|
| 2022 | Exceeds | 118% | Presidents Club |
| 2023 | Meets | 101% | |
| 2024 | Meets | 96% | |
| 2025 | Meets | 92% | 'solid; pipeline hygiene needs work' |
| 2026 YTD (Q1–Q3) | — | 88% | PIP opened 2026-09-16 |
No prior discipline. No prior PIP.
""")
    c.doc("timeline.md", """
# Timeline (assembled by HR at counsel's request)
- **2026-09-12** — Dana files a written internal complaint with HR: Regional VP (Tom Hale) made repeated comments about her appearance and "whether she's too distracted at home to travel"; asks for the comments to stop. HR acknowledges receipt; **no investigation opened** ("Tom is on the road; will circle back").
- **2026-09-16** — PIP opened by Tom Hale (direct manager): 60-day plan, targets: 100% of quarterly quota and CRM updates within 24h. First written performance document in her file.
- **2026-09-30** — Dana requests FMLA leave (intermittent, to care for her mother post-surgery); medical certification submitted 10-03. HR has not yet responded to the request.
- **2026-10-02** — Email, Tom Hale → Lena Ortiz: *"Let's get this done before she's out on leave. Once she's on FMLA it's a nightmare to move on her."*
- **2026-10-06** — HR request to terminate today.
""")
    c.csv("comparator_data.csv", ["employee", "role", "age", "sex", "2026_ytd_attainment", "on_pip", "complaint_filed"], [["Whitcomb, D.", "Account Manager", "42", "F", "88%", "yes (9/16)", "yes (9/12)"], ["Brennan, K.", "Account Manager", "35", "M", "79%", "no", "no"], ["Osei, J.", "Account Manager", "29", "M", "84%", "no", "no"], ["Lind, S.", "Account Manager", "47", "F", "103%", "no", "no"], ["Park, T.", "Account Manager", "31", "M", "86%", "no", "no"]])
    c.doc("separation_agreement_draft.md", """
# SEPARATION AGREEMENT AND GENERAL RELEASE (company form)
3. Severance: 4 weeks' base pay. 4. Release of all claims, including under Title VII, the ADEA, the FMLA, and state law. **7. Employee has seven (7) days to consider this Agreement and may revoke within three (3) days after signing.** 9. Non-disparagement (mutual). 11. Governing law: State of Columbia.
""")
    c.library("title_vii_704a.md", "Title VII §704(a) — retaliation; temporal proximity", "42 U.S.C. §2000e-3(a); *Burlington Northern v. White*, 548 U.S. 53 (2006); *Clark County Sch. Dist. v. Breeden*, 532 U.S. 268 (2001)", "It is unlawful to discriminate against an employee because she has opposed a practice made unlawful by Title VII or participated in a proceeding. An internal complaint of sexual harassment is protected opposition. Causation may be shown by **very close temporal proximity** (days to a few weeks) between the protected activity and the adverse action, by **pretext** (shifting or thin justifications, disparate treatment of comparators who did not complain), and by **direct evidence** (statements by decision-makers linking the action to the protected activity).", verbatim=False)
    c.library("fmla_2615.md", "FMLA §105 — interference and retaliation", "29 U.S.C. §2615(a); 29 C.F.R. §825.220", "(a)(1) It shall be unlawful for any employer to interfere with, restrain, or deny the exercise of or the attempt to exercise any right under the FMLA. (a)(2) It shall be unlawful to discharge or discriminate against any individual for opposing any practice made unlawful. **Terminating an employee to prevent her from taking approved or requested leave is interference** ('an employer is prohibited from using the taking of FMLA leave as a negative factor in employment actions' — §825.220(c)). An employee who requested leave need not have begun it. Remedies: lost wages, liquidated (double) damages, fees, reinstatement.", verbatim=False)
    c.library("adea_owbpa_626f.md", "ADEA/OWBPA — knowing and voluntary waiver", "29 U.S.C. §626(f)(1)", "A waiver of ADEA claims is not knowing and voluntary unless, at a minimum: (A) written in a manner calculated to be understood; (B) specifically refers to rights or claims arising under the ADEA; (C) does not waive future claims; (D) is in exchange for consideration in addition to anything of value to which the individual is already entitled; (E) advises the individual **in writing to consult with an attorney**; **(F) the individual is given a period of at least 21 days** within which to consider the agreement (**45 days** if requested in connection with an exit incentive or other employment termination program offered to a group); **(G) the agreement provides that for a period of at least 7 days following execution, the individual may revoke** the agreement, and the agreement shall not become effective until the revocation period has expired. An ADEA release that fails these requirements is unenforceable as to ADEA claims; the employee may keep the severance and sue (*Oubre v. Entergy*, 522 U.S. 422 (1998)).", verbatim=True)
    c.library("columbia_at_will_exceptions.md", "State of Columbia — at-will employment and exceptions", "Col. Rev. Stat. §24-34-402 (fictional); common law", "Employment is at will, but termination may not be for an unlawful reason (discrimination, retaliation, exercise of statutory rights). State law mirrors Title VII/FMLA with a longer limitations period and uncapped compensatory damages. *(Fictional jurisdiction for this benchmark.)*", verbatim=False)
    c.library("litigation_hold.md", "Litigation hold; spoliation", "Fed. R. Civ. P. 37(e); *Zubulake v. UBS Warburg*, 220 F.R.D. 212 (S.D.N.Y. 2003)", "Once litigation is reasonably anticipated — e.g., an internal discrimination complaint followed by contemplated termination — the employer must preserve relevant documents and ESI, including executives' emails and texts. Failure may result in adverse-inference instructions or sanctions.", verbatim=False)
    c.library("harassment_investigation_duty.md", "Employer's duty to investigate internal complaints", "*Faragher v. City of Boca Raton*, 524 U.S. 775 (1998); *Burlington Indus. v. Ellerth*, 524 U.S. 742 (1998); EEOC Enforcement Guidance (2024)", "An employer that receives a harassment complaint must promptly and impartially investigate and take corrective action; failure undermines the *Faragher/Ellerth* affirmative defense and is itself evidence in a retaliation case. The investigation should be conducted by someone outside the accused's chain of command.", verbatim=False)
    c.contract("""
# Engagement: termination of Dana Whitcomb — risk assessment and documents

HR wants to terminate today using the company's separation agreement. Advise.

## Deliverables (under `workspace/deliverable/`)
1. `risk_assessment.json` — `{"terminate_today": "yes|no", "claims": [{"claim": "...", "strength_for_employee": "low|medium|high", "key_facts": ["..."]}], "separation_agreement_defects": ["..."], "comparator_analysis": "...", "recommended_course": ["..."], "litigation_hold": true/false}`
2. `corrected_separation_agreement_terms.md` — the terms that must change for any future agreement.
3. `advice_to_hr.md` — plain English, including what to do about the harassment complaint and the FMLA request.
4. `QUESTIONS.md` (optional), `STATUS.md`.
""" + COMMON_RULES)
    c.client_script("Lena Ortiz, HR Director; under pressure from VP Tom Hale.", [
        {"id": "investigation", "trigger": ["investigat", "complaint", "September 12", "what happened with"], "answer": "Honestly, nothing. Tom's been traveling. I was going to get to it.", "if_not_asked": "none"},
        {"id": "pip_author", "trigger": ["who wrote the PIP", "Tom", "decision-maker", "who decided"], "answer": "Tom wrote the PIP and Tom wants her out. I'm just processing it.", "if_not_asked": "none"},
        {"id": "fmla_status", "trigger": ["FMLA", "leave request", "certification", "approved"], "answer": "We haven't approved or denied it. Certification came in 10/3. Tom said to wait.", "if_not_asked": "none"},
        {"id": "group", "trigger": ["others", "group", "RIF", "program", "anyone else"], "answer": "Just her. No RIF.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the assessment says do not terminate today", "message": "Lena: Tom says she's at-will and we have a PIP, so we're covered. He wants it done before she goes on leave. If we wait, aren't we just stuck with her forever? Can we at least do it right after her leave?"}])
    ref = {"terminate_today": "no", "claims": [
        {"claim": "Title VII retaliation (harassment complaint 9/12 → PIP 9/16 → termination 10/6)", "strength_for_employee": "high", "key_facts": ["4 days complaint→PIP", "first-ever performance document after 7 years", "no investigation", "decision-maker is the accused", "comparators with lower attainment not on PIPs", "Hale email"]},
        {"claim": "FMLA interference/retaliation", "strength_for_employee": "high", "key_facts": ["request 9/30, certification 10/3", "Hale: 'before she's out on leave… nightmare to move on her' = direct evidence", "liquidated damages"]},
        {"claim": "Sex discrimination / hostile environment (underlying)", "strength_for_employee": "medium", "key_facts": ["comments; no investigation → Faragher/Ellerth defense lost"]},
        {"claim": "ADEA (42)", "strength_for_employee": "low-medium", "key_facts": ["younger male comparators retained with worse numbers"]}],
        "separation_agreement_defects": ["7-day consideration → must be 21 days (45 if group)", "3-day revocation → must be 7 days, agreement effective only after", "must advise in writing to consult an attorney", "must specifically reference ADEA (present) and be in plain language", "consideration must exceed what she is already owed"],
        "comparator_analysis": "Brennan 79%, Osei 84%, Park 86% — all below Whitcomb's 88%, none on PIP, none complained → pretext evidence",
        "recommended_course": ["do not terminate now", "open a prompt, impartial investigation of the 9/12 complaint by someone outside Hale's chain; remove Hale from decisions about Whitcomb", "respond to the FMLA request within 5 business days per 29 CFR 825.300; designate leave", "issue a litigation hold (Hale's email/texts, HR files)", "if performance is genuinely an issue, run a legitimate process applied equally to comparators, documented, after the complaint is resolved — timing after leave does not cure causation if the reason is the complaint", "if separation is desired, negotiate a severance with an OWBPA-compliant release (21/7) and consideration commensurate with the risk"],
        "litigation_hold": True,
        "pushback_answer": "'Right after her leave' is still retaliation if the reason is the complaint/leave; the cure is a legitimate, documented, equally-applied process and resolving the complaint — not timing"}
    c.reference("reference.json", ref)
    c.trap(1, "At-will + PIP = safe", "Terminating today", "Temporal proximity (4 days), first-ever write-up after 7 years, no investigation, accused manager as decision-maker, better-performing comparators, and a direct-evidence email → retaliation and FMLA interference; pushback 'after her leave' doesn't cure", "Timeline; comparator CSV; Hale email", "Retaliation verdict; liquidated damages; fees", "C", "§704(a); 29 U.S.C. §2615", "high")
    c.trap(2, "Using the 7-day agreement", "7 days to consider / 3 to revoke", "OWBPA: 21 days, 7-day revocation, advice to consult counsel; release unenforceable (Oubre)", "Agreement §7; age 42", "She keeps severance and sues", "C", "29 U.S.C. §626(f)", "high")
    c.trap(3, "No litigation hold", "Not instructing preservation of Hale's email", "Litigation reasonably anticipated", "Timeline", "Spoliation sanctions", "H", "Rule 37(e); Zubulake", "high")
    c.trap(4, "Ignoring comparators", "Treating 88% as objectively failing", "Three male comparators lower, none on PIP", "CSV", "Pretext", "H", "", "high")
    c.trap(5, "Recommending 'wait until after leave'", "Timing as the fix", "Causation is about the reason, not the date; and the FMLA request itself is protected", "pushback", "Same exposure", "M", "§825.220(c)", "high")
    c.oracle("terminate_today = no", "true", "exact", "risk_assessment.json")
    c.oracle("separation_agreement_defects includes 21-day consideration and 7-day revocation", "true", "exact", "")
    c.oracle("litigation_hold = true", "true", "exact", "")
    c.oracle("recommended_course includes investigation of the complaint and responding to the FMLA request", "true", "exact", "")
    c.oracle("comparator_analysis identifies lower-performing comparators not on PIP", "true", "exact", "")
    c.rubric("Pushback: explains why timing after leave does not cure causation")
    return c.finish()
