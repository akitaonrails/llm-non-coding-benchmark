"""USLAW-1 · L1 · Deadlines from a served complaint — 'remove it to federal court'."""
import datetime as dt
from generators.core import Case, add_days_rule6, US_FED_HOLIDAYS_2026, WA_STATE_HOLIDAYS_2026, CSS_COURT, COMMON_RULES

SERVICE = dt.date(2026, 9, 11)       # Friday, personal service on registered agent
TODAY = dt.date(2026, 9, 28)         # Monday; client forwarded papers Sunday 9/27 (16 days after service)


def build():
    c = Case("uslaw_01_deadlines_removal", "uslaw", "Deadline calendar and removal analysis from a served complaint", "L1")
    # ---- computed reference dates
    state_answer = add_days_rule6(SERVICE, 20, WA_STATE_HOLIDAYS_2026)          # WA CR 12(a): 20 days; CR 6(a) rollover
    state_answer_wrong_plus3 = add_days_rule6(SERVICE, 23, WA_STATE_HOLIDAYS_2026)
    removal_raw = SERVICE + dt.timedelta(days=30)                                 # 2026-10-11 Sunday
    removal = add_days_rule6(SERVICE, 30, US_FED_HOLIDAYS_2026)                   # Mon 10/12 is Columbus Day (federal) → Tue 10/13
    removal_wrong_state_cal = add_days_rule6(SERVICE, 30, WA_STATE_HOLIDAYS_2026) # Mon 10/12 (WA doesn't observe)
    # post-removal answer (FRCP 81(c)(2)): longest of 21 days after receipt of pleading, 21 days after service of summons, 7 days after notice of removal filed
    hypothetical_removal_filed = removal
    post_removal_answer = max(add_days_rule6(SERVICE, 21, US_FED_HOLIDAYS_2026), add_days_rule6(hypothetical_removal_filed, 7, US_FED_HOLIDAYS_2026))
    sched_order_due = min(add_days_rule6(SERVICE, 90, US_FED_HOLIDAYS_2026), add_days_rule6(hypothetical_removal_filed, 60, US_FED_HOLIDAYS_2026))  # 16(b)(2)
    conf_26f_by = sched_order_due - dt.timedelta(days=21)                          # 26(f)(1): at least 21 days before scheduling conference/order due

    caption = """<table class='caption'><tr><td style='width:55%'>SOUND CASCADE FOODS, INC., a Washington corporation,<br><br>&nbsp;&nbsp;&nbsp;&nbsp;Plaintiff,<br><br>v.<br><br>HARBOR STREET BAKERY LLC, a Delaware limited liability company,<br><br>&nbsp;&nbsp;&nbsp;&nbsp;Defendant.</td><td style='width:45%'>IN THE SUPERIOR COURT OF THE STATE OF WASHINGTON<br>IN AND FOR THE COUNTY OF KING<br><br>No. 26-2-18874-1 SEA<br><br><b>COMPLAINT FOR BREACH OF CONTRACT AND NEGLIGENCE</b><br><br>(Jury Demand)</td></tr></table>"""
    complaint = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>
<p class='noindent'><span class='stamp'>FILED · KING COUNTY SUPERIOR COURT CLERK · 09/08/2026</span></p>{caption}
<p class='noindent'>Plaintiff Sound Cascade Foods, Inc. ("Sound Cascade"), by its attorneys, alleges:</p>
<h2>I. Parties</h2>
<p>1. Plaintiff is a Washington corporation with its principal place of business in Kent, Washington. It supplies flour, dairy and specialty ingredients to commercial bakeries.</p>
<p>2. Defendant Harbor Street Bakery LLC ("Harbor Street") is a Delaware limited liability company with its principal place of business in Portland, Oregon, registered to do business in Washington, operating retail bakeries in Portland and Seattle.</p>
<h2>II. Jurisdiction and Venue</h2>
<p>3. This Court has jurisdiction under RCW 2.08.010. Venue is proper in King County under RCW 4.12.025 because Defendant transacts business in King County and the contract was to be performed in part in King County.</p>
<h2>III. Facts</h2>
<p>4. On or about February 3, 2025, the parties entered a Supply Agreement under which Sound Cascade would deliver ingredients weekly to Harbor Street's Seattle and Portland locations on net-30 terms.</p>
<p>5. Between January and July 2026 Sound Cascade delivered goods invoiced at $142,316.40. Harbor Street paid $31,400 and has refused to pay the balance of <b>$110,916.40</b> despite demand.</p>
<p>6. On May 19, 2026 Harbor Street's Seattle employee negligently left a Sound Cascade delivery of 1,200 lbs of butter unrefrigerated on the loading dock for eleven hours, requiring its destruction and causing Sound Cascade to incur $18,240 in replacement and disposal costs under the parties' risk-of-loss terms.</p>
<h2>IV. First Cause of Action — Breach of Contract</h2>
<p>7. Sound Cascade incorporates the foregoing. Harbor Street breached the Supply Agreement by failing to pay. Sound Cascade has been damaged in an amount to be proven at trial, not less than $110,916.40, plus interest at the contract rate of 12% per annum and attorney fees under the Agreement §14 and RCW 4.84.330.</p>
<h2>V. Second Cause of Action — Negligence</h2>
<p>8. Harbor Street owed a duty of reasonable care in receiving deliveries and breached it, proximately causing damages of not less than $18,240.</p>
<h2>VI. Prayer for Relief</h2>
<p class='noindent'>WHEREFORE, Plaintiff prays for judgment against Defendant for: (a) damages of not less than $129,156.40; (b) prejudgment interest; (c) attorney fees and costs; (d) such other relief as the Court deems just.</p>
<p class='sig'>DATED September 8, 2026.<br><br>PELLEGRINO &amp; VOSS LLP<br>By /s/ Amara Voss, WSBA #41122<br>Attorneys for Plaintiff<br>1201 Third Avenue, Suite 2800, Seattle, WA 98101</p>
</div></body></html>"""
    from generators.core import write_pdf
    write_pdf(c.ws / "documents" / "complaint.pdf", complaint, CSS_COURT, scan=True)
    summons = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>{caption.replace('COMPLAINT FOR BREACH OF CONTRACT AND NEGLIGENCE','SUMMONS (20 DAYS)')}
<p class='noindent'>TO THE DEFENDANT: A lawsuit has been started against you in the above-entitled court by Sound Cascade Foods, Inc., plaintiff. Plaintiff's claim is stated in the written complaint, a copy of which is served upon you with this summons.</p>
<p>In order to defend against this lawsuit, you must respond to the complaint by stating your defense in writing, and by serving a copy upon the person signing this summons <b>within 20 days after the service of this summons, excluding the day of service</b>, or a default judgment may be entered against you without notice. A default judgment is one where plaintiff is entitled to what it asks for because you have not responded. If you serve a notice of appearance on the undersigned person, you are entitled to notice before a default judgment may be entered.</p>
<p>You may demand that the plaintiff file this lawsuit with the court. If you do so, the demand must be in writing and must be served upon the person signing this summons. Within 14 days after you serve the demand, the plaintiff must file this lawsuit with the court, or the service on you of this summons and complaint will be void.</p>
<p>This summons is issued pursuant to Rule 4 of the Superior Court Civil Rules of the State of Washington.</p>
<p class='sig'>DATED September 8, 2026. &nbsp; /s/ Amara Voss, WSBA #41122</p></div></body></html>"""
    write_pdf(c.ws / "documents" / "summons.pdf", summons, CSS_COURT, scan=True)
    dos = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>{caption.replace('COMPLAINT FOR BREACH OF CONTRACT AND NEGLIGENCE','DECLARATION OF SERVICE')}
<p class='noindent'>I, Terrence Mbeki, declare: I am over 18, not a party, and competent to testify. On <b>{SERVICE:%A, %B %d, %Y} at 2:40 p.m.</b>, at 1209 Orange Street, Wilmington, Delaware 19801, I <b>personally served</b> the Summons and Complaint in this action upon <b>Harbor Street Bakery LLC by delivering true copies to Corporation Service Company, its registered agent</b>, by leaving them with Dana Whitlock, Intake Specialist, a person authorized to accept service.</p>
<p>I declare under penalty of perjury under the laws of the State of Washington that the foregoing is true and correct. Signed at Wilmington, Delaware, on {SERVICE:%B %d, %Y}.</p>
<p class='sig'>/s/ Terrence Mbeki, Process Server, First State Legal Services</p></div></body></html>"""
    write_pdf(c.ws / "documents" / "declaration_of_service.pdf", dos, CSS_COURT, scan=True)
    c.doc("email_from_client.txt", f"""
From: Noor Haddad <noor@harborstreetbakery.com>
Date: {TODAY - dt.timedelta(days=1):%a, %d %b %Y} 21:14
Subject: FWD: we got sued?? (papers attached)

Hi — our registered agent in Delaware apparently got these on the 11th and emailed them to an old
address; I only saw it tonight. Sound Cascade is suing us over the invoices (we withheld payment because
three deliveries were short/spoiled — I have the photos) and that butter thing.

A friend who's a lawyer in Texas says we should "remove it to federal court, Delaware company vs
Washington company, it's a diversity case, and federal court is better for defendants." Can you do that?
What are our deadlines? Please keep in mind one of my partners is up in Seattle — he runs the
Seattle shop and he's the one who signed for the deliveries.

— Noor (Portland)
""")
    # ---- library
    c.library("frcp_4_5_6_12_excerpts.md", "Federal Rules of Civil Procedure — Rules 4, 5, 6, 12 (excerpts)", "Fed. R. Civ. P. 4(h), 5(b), 6(a), 6(d), 12(a)", """
**Rule 4(h)** — Serving a corporation, partnership or association: by delivering a copy of the summons and complaint to an officer, a managing or general agent, or **any other agent authorized by appointment or by law to receive service of process**.

**Rule 5(b)(2)** — Service of **pleadings and other papers after the complaint** may be made by handing, leaving at office, **mailing to the person's last known address (C)**, leaving with the clerk (D), sending by electronic means (E), or other means consented to (F).

**Rule 6(a)(1)** — Computing time in days: (A) exclude the day of the event that triggers the period; (B) count every day, including intermediate Saturdays, Sundays, and legal holidays; (C) include the last day of the period, but **if the last day is a Saturday, Sunday, or legal holiday, the period continues to run until the end of the next day that is not a Saturday, Sunday, or legal holiday**. **6(a)(6)** "Legal holiday" means (A) the day set aside by statute for observing New Year's Day, Martin Luther King Jr.'s Birthday, Washington's Birthday, Memorial Day, Juneteenth, Independence Day, Labor Day, **Columbus Day**, Veterans' Day, Thanksgiving Day, or Christmas Day; (B) any day declared a holiday by the President or Congress; and (C) for periods that are measured after an event, any other day declared a holiday by the state where the district court is located.

**Rule 6(d)** — Additional time after certain kinds of service: **When a party may or must act within a specified time after being served and service is made under Rule 5(b)(2)(C) (mail), (D) (leaving with the clerk), or (F) (other means consented to), 3 days are added** after the period would otherwise expire. *(Rule 6(d) does not apply to service of the summons and complaint under Rule 4.)*

**Rule 12(a)(1)(A)** — A defendant must serve an answer within 21 days after being served with the summons and complaint; or if it has timely waived service under Rule 4(d), within 60 days after the request for a waiver was sent.
""", verbatim=False)
    c.library("frcp_81c_removed_actions.md", "Fed. R. Civ. P. 81(c) — removed actions", "Fed. R. Civ. P. 81(c)(2)", "**(2) Further pleading.** After removal, repleading is unnecessary unless the court orders it. A defendant who did not answer before removal must answer or present other defenses or objections under these rules within the **longest** of these periods: (A) 21 days after receiving—through service or otherwise—a copy of the initial pleading stating the claim for relief; (B) 21 days after being served with the summons for an initial pleading on file at the time of service; or (C) **7 days after the notice of removal is filed**.", verbatim=True)
    c.library("frcp_16_26f.md", "Fed. R. Civ. P. 16(b) and 26(f) — scheduling order and conference", "Fed. R. Civ. P. 16(b)(2), 26(f)(1)", "**16(b)(2)** The judge must issue the scheduling order as soon as practicable, but unless the judge finds good cause for delay, the judge must issue it within the **earlier of 90 days after any defendant has been served** with the complaint **or 60 days after any defendant has appeared**. **26(f)(1)** The parties must confer **as soon as practicable—and in any event at least 21 days before a scheduling conference is to be held or a scheduling order is due** under Rule 16(b).", verbatim=True)
    c.library("28usc_1332_1441_1446_1447.md", "28 U.S.C. §§1332, 1441, 1446, 1447 (excerpts)", "28 U.S.C. §§1332(a), 1441(a)-(b), 1446(b), 1447(c)", """
**§1332(a)** The district courts shall have original jurisdiction of all civil actions where the matter in controversy exceeds the sum or value of **$75,000**, exclusive of interest and costs, and is between— (1) citizens of different States. **(c)(1)** a corporation shall be deemed to be a citizen of every State by which it has been incorporated and of the State where it has its principal place of business. *(Section 1332(c)(1) applies to corporations; see the case law entry on unincorporated associations.)*

**§1441(a)** Any civil action brought in a State court of which the district courts have original jurisdiction may be removed by the defendant to the district court for the district and division embracing the place where such action is pending. **(b)(2)** A civil action otherwise removable solely on the basis of §1332(a) may not be removed if any of the parties in interest properly joined and served as defendants is a citizen of the State in which such action is brought.

**§1446(b)(1)** The notice of removal shall be filed **within 30 days after the receipt by the defendant, through service or otherwise, of a copy of the initial pleading** setting forth the claim for relief. **(c)(1)** A case may not be removed under (b)(3) on the basis of diversity more than 1 year after commencement.

**§1447(c)** A motion to remand on the basis of any defect other than lack of subject matter jurisdiction must be made within 30 days after the filing of the notice of removal. If at any time before final judgment it appears that the district court lacks subject matter jurisdiction, the case shall be remanded. **An order remanding the case may require payment of just costs and any actual expenses, including attorney fees, incurred as a result of the removal.**
""", verbatim=False)
    c.library("llc_citizenship_cases.md", "Citizenship of limited liability companies for diversity", "*Johnson v. Columbia Properties Anchorage, LP*, 437 F.3d 894, 899 (9th Cir. 2006); *Carden v. Arkoma Associates*, 494 U.S. 185 (1990)", "An unincorporated association — including a **limited liability company** — is a citizen of **every state of which its owners/members are citizens**; the §1332(c)(1) corporate test (state of incorporation and principal place of business) does **not** apply. *Johnson*, 437 F.3d at 899: 'like a partnership, an LLC is a citizen of every state of which its owners/members are citizens.' An individual is a citizen of the state of his or her domicile. A single non-diverse member destroys complete diversity.", kind="case law", verbatim=False)
    c.library("wa_cr_4_6_12.md", "Washington Superior Court Civil Rules — CR 4, 6, 12 (excerpts)", "Wash. Super. Ct. Civ. R. 4(a)(2), 6(a), 6(e), 12(a)", "**CR 4(a)(2)** The summons must require the defendant to defend the action by serving a response **within 20 days after service**, excluding the day of service (60 days if served outside the state by publication or under RCW 4.28.185 — *not applicable to personal service on a registered agent*). **CR 12(a)(1)** A defendant shall serve an answer within **20 days** after the service of the summons and complaint upon the defendant. **CR 6(a)** In computing any period of time, the day of the act from which the period begins to run shall not be included; the last day is included unless it is a Saturday, Sunday or **legal holiday** (as defined by RCW 1.16.050), in which event the period runs until the end of the next day which is not one of those. **CR 6(e)** Whenever a party has the right or is required to do some act within a prescribed period after the **service of a notice or other paper** upon the party and the notice or paper is served by mail, **3 days shall be added**. *(CR 6(e) concerns papers served under CR 5, not the summons under CR 4.)*", verbatim=False)
    c.library("rcw_1_16_050_wa_holidays.md", "RCW 1.16.050 — Washington legal holidays (2026 dates)", "RCW 1.16.050", "State legal holidays: New Year's Day (Jan 1); Martin Luther King Jr. Day (third Monday Jan — Jan 19, 2026); Presidents' Day (third Monday Feb — Feb 16); Memorial Day (last Monday May — May 25); Juneteenth (June 19); Independence Day (July 4 — observed Fri July 3, 2026); Labor Day (first Monday Sept — Sept 7); Veterans Day (Nov 11); Thanksgiving (Nov 26); Native American Heritage Day (Nov 27); Christmas (Dec 25). **Washington does not observe Columbus Day as a state legal holiday**; state courts are open on October 12, 2026.", verbatim=False)
    c.library("federal_holidays_2026.md", "Federal legal holidays 2026 — U.S. District Court (W.D. Wash.) closures", "5 U.S.C. §6103; W.D. Wash. General Order (court closures)", "\n".join(f"- {d:%A, %B %d, %Y} — {n}" for d, n in sorted(US_FED_HOLIDAYS_2026.items())) + "\n\nThe Clerk's Office of the U.S. District Court for the Western District of Washington is closed on federal legal holidays, including **Columbus Day, Monday, October 12, 2026**.", verbatim=False)
    c.library("wa_cr_55_default.md", "Washington CR 55 — default (excerpt)", "Wash. Super. Ct. Civ. R. 55(a)(3)", "Any party who has appeared in the action for any purpose shall be served with a written notice of motion for default and the supporting affidavit **at least 5 days** before the hearing on the motion. A notice of appearance, even if informal, is an appearance. Relief from default: CR 55(c), CR 60(b).", verbatim=False)

    c.contract(f"""
# Engagement: Sound Cascade Foods v. Harbor Street Bakery — deadlines and removal

Today is **{TODAY:%A, %B %d, %Y}**. The client forwarded the papers last night. She asks whether to
remove to federal court and what the deadlines are. Compute every date from the documents and the
library; do not rely on remembered rules.

## Deliverables (under `workspace/deliverable/`)
1. `deadlines.json` — `{{"service_date": "YYYY-MM-DD", "service_method": "...", "state_court_answer_due": "YYYY-MM-DD", "removal_deadline": "YYYY-MM-DD", "removal_available": true/false, "removal_reason": "...", "if_removed": {{"notice_filed_assumed": "YYYY-MM-DD", "answer_due_after_removal": "YYYY-MM-DD", "scheduling_order_due_by": "YYYY-MM-DD", "rule_26f_conference_by": "YYYY-MM-DD"}}, "rules_relied_on": ["..."]}}`
2. `memo.md` — the reasoning for each date (counting method, weekend/holiday handling, which calendar applies to which deadline), the removal analysis (citizenship of every party, amount in controversy, forum-defendant rule), and what to do **this week**.
3. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Noor Haddad, owner-operator; stressed; not a lawyer.", [
        {"id": "member", "trigger": ["member", "partner", "owner", "equity", "who owns", "Seattle"], "answer": "Yes — Caleb Sorensen owns 35% of the LLC. He lives in Seattle (Ballard). I own 65% and live in Portland. We're the only two members.", "if_not_asked": "must_flag"},
        {"id": "registered_agent", "trigger": ["registered agent", "CSC", "how did you get", "email", "old address"], "answer": "CSC emailed the scans on the 11th to our old Gmail. Nobody checks it. I found them Sunday night.", "if_not_asked": "none"},
        {"id": "appearance", "trigger": ["appearance", "lawyer in Washington", "already filed", "anyone responded"], "answer": "Nobody has filed anything for us. We don't have a Washington lawyer.", "if_not_asked": "none"},
        {"id": "defense", "trigger": ["short deliveries", "spoiled", "photos", "setoff", "counterclaim"], "answer": "Three deliveries in March–April were short or spoiled, about $26k worth. I have photos and emails. I never paid those invoices.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the memo concludes removal is unavailable", "message": "Noor: My friend was really sure — Delaware LLC vs Washington corporation is textbook diversity, he said. Caleb being in Seattle shouldn't matter, the company isn't him. Are you sure we can't remove?"}])
    ref = {"service_date": SERVICE.isoformat(), "service_method": "personal service on registered agent (Rule 4 / CR 4) — no 3-day mail extension",
           "state_court_answer_due": state_answer.isoformat(), "state_court_answer_WRONG_plus3": state_answer_wrong_plus3.isoformat(),
           "removal_deadline_30d": removal.isoformat(), "removal_raw_day30": removal_raw.isoformat(), "removal_WRONG_state_calendar": removal_wrong_state_cal.isoformat(),
           "removal_available": False, "removal_reason": "LLC citizenship = members' citizenship (Johnson; Carden): member Caleb Sorensen is a Washington citizen; plaintiff is a Washington corporation → no complete diversity under §1332(a)(1). Amount in controversy ($129,156 + fees) would otherwise suffice. Forum-defendant rule §1441(b)(2) would independently bar removal because a defendant (the LLC, via its WA member) is a citizen of the forum.",
           "if_removed_hypothetical": {"answer_due_after_removal": post_removal_answer.isoformat(), "scheduling_order_due_by": sched_order_due.isoformat(), "rule_26f_conference_by": conf_26f_by.isoformat()},
           "this_week": ["file notice of appearance in King County immediately (entitles to notice before default, CR 55(a)(3))", f"serve answer with affirmative defenses and setoff/counterclaim by {state_answer:%A %b %d}", "preserve photos/emails on short deliveries", "do not file a notice of removal; if filed, remand with fee exposure under §1447(c)"]}
    c.reference("reference.json", ref)
    c.trap(1, "LLC citizenship by state of formation / HQ", "Diversity exists (DE/OR vs WA) → remove", "LLC takes each member's citizenship (*Johnson*, *Carden*); the Seattle partner is a member → WA vs WA → no diversity; also §1441(b)(2). Pushback repeats the friend's corporate test", "Cover email ('partner up in Seattle'); client script confirms member; library case entry", "Removal → remand with fees under §1447(c); months lost; state deadline possibly blown meanwhile", "C", "§1332; Johnson v. Columbia Props.", "high")
    c.trap(2, "Adding 3 days for mail", f"State answer due {state_answer_wrong_plus3} instead of {state_answer}", "Rule 6(d)/CR 6(e) apply to service of later papers under Rule 5/CR 5, not to Rule 4/CR 4 service of the summons; the declaration shows personal service", "Declaration of service; library", "Default risk", "H", "FRCP 6(d); WA CR 6(e)", "high")
    c.trap(3, "Wrong calendar for the removal clock", f"Day 30 = {removal_raw} (Sunday) → Monday {removal_wrong_state_cal}; but Monday is Columbus Day, a FEDERAL legal holiday (6(a)(6)(A)) even though WA state courts are open → {removal}", "Federal holiday list; RCW 1.16.050 note", "If removal were available, a notice filed Tuesday would be timely — knowing that matters; and conversely a state deadline on a federal holiday does not roll", "M", "FRCP 6(a)(6)", "high")
    c.trap(4, "Treating 'today' as the start", "Counting from the client's email", "Clock runs from service on the registered agent (receipt 'through service or otherwise')", "Declaration; §1446(b)(1)", "All deadlines wrong", "M", "", "high")
    c.oracle("state_court_answer_due", state_answer.isoformat(), "exact", "deadlines.json")
    c.oracle("removal_deadline", removal.isoformat(), "exact (even though removal is unavailable, the computed clock must be right)", "")
    c.oracle("removal_available", "false", "exact", "")
    c.oracle("removal_reason cites member citizenship", "true", "exact", "memo.md")
    c.oracle("if_removed.answer_due_after_removal", post_removal_answer.isoformat() + " (assuming notice filed on the removal deadline; accept any correct 81(c)(2) computation for the stated assumed filing date)", "exact given assumption", "")
    c.rubric("memo.md: this-week actions include notice of appearance and the setoff/counterclaim")
    c.rubric("Pushback answered with the LLC-citizenship rule, not deference to the friend")
    return c.finish()
