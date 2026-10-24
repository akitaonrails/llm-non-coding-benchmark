"""USACC-5 · L2 · Entity choice for two founders — 'elect S-corp, pay a small salary, save SE tax'.
Absorbs the formation-law traps (profits interest, 83(b), buy-sell) formerly in USLAW-6."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

TY = 2026


def build():
    c = Case("usacc_05_entity_choice", "usacc", "Entity choice and S election for two founders", "L2")
    proj_income = D("260000")   # year-1 net before owner comp
    tool_fmv, tool_basis = D("120000"), D("31000")
    cash_tomas = D("20000")
    # substantial presence (2026 year): 2026 days 118, 2025 days 96, 2024 days 66 → 118 + 32 + 11 = 161 < 183 → NOT a US resident
    days = {"2026": 118, "2025": 96, "2024": 66}
    spt = days["2026"] + days["2025"] / 3 + days["2024"] / 6

    c.doc("founders_questionnaire.md", f"""
# New business intake — "Natarajan Herrera Advisory"

**Founders.** Priya Natarajan (US citizen, San Diego) and Tomás Herrera (Mexican citizen; see travel calendar; works from Monterrey and San Diego on a TN visa, no green card application pending).
**Business.** B2B consulting (pricing strategy) — services only. Expected year-1 net income before any owner compensation: **{money(proj_income)}**. Both work full time in the business.
**What each contributes.** Priya: her pricing-simulation software tool (independent appraisal **{money(tool_fmv)}**; she built it over three years, has deducted {money(tool_fmv - tool_basis)} of costs, remaining basis {money(tool_basis)}). Tomás: **{money(cash_tomas)}** cash and "the client relationships and all the selling".
**Ownership they want.** 50/50, with Tomás's share **vesting over 3 years** (1-year cliff) since he's putting in less money.
**What a friend told them.** "Form an LLC, elect S-corp, pay yourselves $40,000 each, take the rest as distributions — you'll save a fortune in self-employment tax."
**State.** They like the idea of forming in Delaware "like startups do". Operations are in California and Nuevo León.
**Other.** Tomás is married (community property, Mexico). Priya is single. They have not discussed what happens if one leaves, dies or divorces.
""")
    c.doc("tomas_travel_calendar.csv", "year,days_physically_in_US,notes\n2024,66,client visits\n2025,96,client visits + onboarding\n2026,118,projected (same pattern, plus Q4 push)\n")
    c.doc_pdf("tool_appraisal.pdf", f"""
# Valuation Report — "PriceLab" pricing-simulation software
**Prepared for:** Priya Natarajan · **Valuation date:** January 15, {TY} · **Prepared by:** Coastline Valuation Advisors (fictitious)

**Conclusion of value:** fair market value of the PriceLab codebase, models and documentation, on a going-concern license basis: **{money(tool_fmv)}**.

Method: relief-from-royalty, 5-year horizon, 18% discount rate. The asset is a self-created intangible; the owner reports cumulative development costs of $89,000 deducted as expenses in 2023–2025.
""")
    c.doc("projections.csv", "line,year1,year2\nrevenue,610000,820000\ncontractor_and_tool_costs,195000,260000\noverhead,155000,190000\nnet_before_owner_comp,260000,370000\n")

    # ---- library
    c.library("irc_1361_excerpt.md", "IRC §1361(b) — small business corporation defined", "26 U.S.C. §1361(b)(1)", """
(b)(1) In general. — For purposes of this subchapter, the term "small business corporation" means a domestic corporation which is not an ineligible corporation and which does not— (A) have more than 100 shareholders, (B) have as a shareholder a person (other than an estate, a trust described in subsection (c)(2), or an organization described in subsection (c)(6)) who is not an individual, **(C) have a nonresident alien as a shareholder**, and (D) have more than 1 class of stock.

*(§1362(d)(2): an election terminates on the day the corporation ceases to be a small business corporation; the corporation is then a C corporation.)*
""", verbatim=True)
    c.library("irc_7701b_substantial_presence.md", "IRC §7701(b)(3) — substantial presence test", "26 U.S.C. §7701(b)(3)(A)", """
An individual meets the substantial presence test for a calendar year if (i) the individual was present in the United States on at least 31 days during the calendar year, and (ii) the sum of the number of days present in the current year + **1/3** of the days in the first preceding year + **1/6** of the days in the second preceding year equals or exceeds **183**. An alien who does not hold a green card and does not meet the test is a nonresident alien for the year (absent a first-year election under §7701(b)(4)).
""", verbatim=False)
    c.library("irc_351_excerpt.md", "IRC §351 — transfer to corporation controlled by transferor", "26 U.S.C. §351(a), (d); §368(c)", """
(a) No gain or loss shall be recognized if property is transferred to a corporation by one or more persons solely in exchange for stock in such corporation and immediately after the exchange such person or persons are in control (as defined in section 368(c)) of the corporation. **(d) Services ... — For purposes of this section, stock issued for (1) services ... shall not be considered as issued in return for property.** §368(c): control means ownership of at least 80 percent of the total combined voting power and 80 percent of each other class.

*Stock issued for services is compensation income to the recipient at fair market value when substantially vested (§83).*
""", verbatim=False)
    c.library("irc_721_and_revproc_93-27.md", "IRC §721 and Rev. Proc. 93-27 — partnership contributions and profits interests", "26 U.S.C. §721; Rev. Proc. 93-27, 1993-2 C.B. 343; Rev. Proc. 2001-43", """
§721(a): No gain or loss shall be recognized to a partnership or to any of its partners in the case of a contribution of property to the partnership in exchange for an interest in the partnership. (No 80% control requirement.)

Rev. Proc. 93-27 §4.01: if a person receives a **profits interest** for the provision of services to or for the benefit of a partnership in a partner capacity, the IRS will not treat the receipt as a taxable event. A profits interest is one that would give the holder nothing on an immediate liquidation at fair market value. A **capital interest** (a share of existing capital) received for services is taxable compensation at receipt or vesting. Rev. Proc. 2001-43: an unvested profits interest is treated as held from grant if the holder is treated as a partner from grant; a protective §83(b) election within 30 days is customary.
""", verbatim=False)
    c.library("irc_83b.md", "IRC §83(b) election", "26 U.S.C. §83(b); Treas. Reg. §1.83-2", "A person who performs services in connection with which property is transferred may elect to include in gross income the excess of the fair market value at transfer over the amount paid, **by filing the election not later than 30 days after the date of transfer**. No extension is available. Absent the election, income is recognized as the property vests, at the value at each vesting date.", verbatim=False)
    c.library("irc_199a_sstb.md", "IRC §199A — qualified business income; specified service trade or business", "26 U.S.C. §199A(d)(2); (e)(2)", f"""
The 20% deduction is not available for a **specified service trade or business** (including **consulting**, health, law, accounting, financial services, and any business where the principal asset is the reputation or skill of its employees) once taxable income exceeds the threshold ({TY}: approximately $200,300 single / $400,600 joint; verify) plus the phase-in range ($75,000 / $150,000). Below the threshold the SSTB limitation does not apply. W-2 wages paid by an S corporation to its owner are **not** QBI; distributions are. Guaranteed payments from a partnership are not QBI.
""", verbatim=False, note="Verify TY threshold (OBBBA made §199A permanent and changed the phase-in range).")
    c.library("reasonable_compensation.md", "Reasonable compensation for S corporation shareholder-employees", "Rev. Rul. 74-44; *Watson v. Commissioner*, 668 F.3d 1008 (8th Cir. 2012); IRS Fact Sheet FS-2008-25", "An S corporation shareholder who performs substantial services must be paid reasonable compensation as wages before distributions. In a personal-services business where the shareholders generate essentially all of the revenue, courts have recharacterized distributions as wages where salary was set far below what comparable professionals earn (*Watson*: $24,000 salary vs. ~$200,000 of distributions recharacterized in large part). Payroll taxes, penalties and interest follow.", kind="case law / ruling", verbatim=False)
    c.library("form_2553_deadline.md", "Form 2553 — when to file", "IRS Form 2553 Instructions", "To be effective for a tax year, file no more than 2 months and 15 days after the beginning of that tax year, or at any time during the preceding year. Late-election relief under Rev. Proc. 2013-30 requires reasonable cause and that all shareholders were eligible for the entire period.", verbatim=False)
    c.library("ca_llc_franchise.md", "California LLC fee and franchise tax; foreign qualification", "Cal. Rev. & Tax. Code §§17941, 17942, 23153; Cal. Corp. Code §17708.02", "Every LLC doing business in California pays the $800 annual tax and a gross-receipts fee ($900 at $250k–$499,999; $2,500 at $500k–$999,999 ...). A Delaware LLC doing business in California must register as a foreign LLC and pays the same amounts; failure bars it from maintaining an action in California courts and incurs penalties.", verbatim=False)
    c.library("llc_buy_sell_checklist.md", "Operating agreement — buy-sell and governance checklist", "Practitioner checklist (ABA Business Law Section, paraphrased)", "Trigger events: death, disability, divorce (spousal interest), bankruptcy, voluntary departure, for-cause removal. Price: formula or appraisal; discounts. Payment terms. Vesting of founder units with repurchase at cost for unvested units. Deadlock resolution for 50/50 owners (mediation → buy-sell shotgun). Drag-along/tag-along. Transfer restrictions and spousal consent in community-property jurisdictions.", kind="practice aid")

    c.contract(f"""
# Engagement: entity and tax structure for Priya Natarajan and Tomás Herrera

The founders want an LLC with an S election, 50/50, $40,000 salaries, Delaware formation. Advise
them. Use the questionnaire, travel calendar, appraisal and projections; only the library is
authority.

## Deliverables (under `workspace/deliverable/`)
1. `recommendation.md` — entity, tax classification, ownership structure (how each founder's contribution becomes equity), and why; the alternatives you rejected and why.
2. `year1_comparison.json` — `{{"options": {{"<name>": {{"entity_level_tax": 0, "founder_tax_priya": 0, "founder_tax_tomas": 0, "payroll_taxes": 0, "total": 0, "assumptions": "..."}}}}}}` for at least: (a) the founders' plan as stated, (b) your recommendation, (c) one other.
3. `compliance_calendar.md` — every deadline with the date (formation, elections, 83(b), estimated taxes, state registrations).
4. `term_sheet.md` — operating/shareholder agreement terms: vesting, buy-sell triggers, deadlock, transfer restrictions.
5. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Priya (organized, asks good questions) and Tomás (enthusiastic, convinced by his friend).", [
        {"id": "green_card", "trigger": ["green card", "permanent resident", "immigration status", "resident alien", "substantial presence"], "answer": "Tomás: no green card, no application. TN visa. I'm in the US maybe a third of the year.", "if_not_asked": "must_flag"},
        {"id": "tool_prior_deductions", "trigger": ["deducted", "basis", "development costs", "capitalized"], "answer": "Priya: I expensed about $89k of it on my Schedule C over three years. Remaining basis is around $31k per my CPA.", "if_not_asked": "none"},
        {"id": "where_work", "trigger": ["where do you work", "operations", "California", "office"], "answer": "Priya: I work from San Diego. Tomás from Monterrey mostly. Clients are all over the US.", "if_not_asked": "none"},
        {"id": "marriage", "trigger": ["spouse", "married", "community property", "divorce"], "answer": "Tomás: married, in Mexico, no prenup. Priya: single.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the recommendation rejects the S election", "message": "Tomás: My friend's CPA does this for everyone. Are you sure we can't do the S-corp? What if we just list Priya as the only shareholder for now and add me later?"}])

    # ---- reference (first-year numbers, simplified; tolerance ±10%)
    # Option A (founders' plan): LLC + S election — INVALID (NRA shareholder) → taxed as C corp: 21% on 260k-80k=180k = 37.8k; dividends on remaining distributed... we present the exposure, not a clean number
    # Option B (recommended): LLC/partnership; Priya contributes tool (§721, carryover basis 31k), Tomás cash + PROFITS interest (vesting, 83(b)); guaranteed payments to both; SE tax on all.
    # Option C: C corp (if they want to build value / foreign owner); 21% + payroll.
    se_tax = lambda x: q2(min(x * D("0.9235"), D("184500")) * D("0.153") + max(D("0"), x * D("0.9235") - D("184500")) * D("0.029"))
    optB_se = se_tax(D("130000")) * 2
    ref = {"recommendation": "LLC taxed as a partnership (or a C corporation if they prioritize retained earnings/foreign-owner simplicity). NOT an S corporation while Tomás is a nonresident alien. Tomás receives a vested capital interest for his $20,000 cash plus a vesting PROFITS interest (Rev. Proc. 93-27) for services, with a protective 83(b) within 30 days. Priya contributes PriceLab under §721 (carryover basis $31,000; no gain). Form in California or register the Delaware LLC in California as a foreign LLC (CA tax applies either way).",
           "substantial_presence_days_weighted": spt, "tomas_status": "nonresident alien for 2026 (161 < 183, no green card)",
           "s_election_consequence": "Election invalid from inception (§1361(b)(1)(C)); entity is a C corporation by default; 'distributions' are dividends — double taxation; Form 2553 late-relief unavailable because a shareholder was ineligible.",
           "capital_interest_for_services": f"If Tomás took 50% of a ${int(tool_fmv + cash_tomas):,} capital account for services, ~${int((tool_fmv + cash_tomas) / 2 - cash_tomas):,} is compensation income at vesting (§83) — avoided with a profits interest.",
           "year1_estimate": {"founders_plan_if_it_worked": {"note": "shown only to expose the comparison the friend made", "payroll_taxes_on_80k": str(q2(D("80000") * D("0.153"))), "but": "invalid election"},
                              "recommended_partnership": {"self_employment_tax_both": str(optB_se), "entity_level_tax": "0 (CA LLC $800 + fee $2,500)", "assumptions": "guaranteed payments $130k each; §199A SSTB — below threshold year 1, so partially available"},
                              "c_corp": {"entity_level_tax": str(q2((proj_income - D("200000")) * D("0.21"))), "payroll_taxes_on_200k": str(q2(D("200000") * D("0.153"))), "assumptions": "salaries $100k each"}},
           "deadlines": {"form_2553_if_ever_eligible": "2 months 15 days after start of tax year", "83b": "30 days after grant of the profits interest — no extension", "CA_LLC_annual_tax": "15th day of 4th month", "estimated_taxes": "Apr 15 / Jun 15 / Sep 15 / Jan 15"},
           "term_sheet_required": ["3-year vesting, 1-year cliff, repurchase of unvested at cost", "buy-sell on death/disability/divorce/departure with valuation method", "spousal consent (Tomás, community property)", "deadlock mechanism for 50/50", "transfer restrictions", "IP assignment of PriceLab to the entity"]}
    c.reference("reference.json", ref)
    c.trap(1, "S election with a nonresident alien shareholder", "Recommending the LLC + S election", "§1361(b)(1)(C); Tomás fails substantial presence (161 weighted days) and has no green card → election invalid → C corporation by default → dividends, double tax. Pushback 'list Priya only and add me later' is a sham that also fails (beneficial ownership) and the later addition terminates the election", "Travel calendar; questionnaire (TN visa, no green card)", "Double taxation; back payroll taxes; cleanup cost", "C", "§1361(b)(1)(C); §7701(b)(3)", "high")
    c.trap(2, "Capital interest for services", "Issuing Tomás 50% of capital for $20k cash + services", "Services are not property (§351(d) / §83); the excess is compensation income now or at vesting. Profits interest under Rev. Proc. 93-27 avoids it", "Questionnaire", "Surprise tax bill to Tomás (~$50k of income)", "H", "Rev. Proc. 93-27; §83", "high")
    c.trap(3, "$40k salaries", "Adopting the friend's plan on compensation", "Reasonable-compensation doctrine for personal-service businesses (*Watson*)", "Projections: revenue is the founders' own services", "Recharacterization, payroll tax, penalties", "H", "Rev. Rul. 74-44; *Watson*", "high")
    c.trap(4, "Missing the 83(b) window", "Vesting interest without a timely 83(b)", "30 days, no extension", "Questionnaire (3-year vesting)", "Tax at each vesting date on appreciated value", "M", "§83(b)", "high")
    c.trap(5, "Delaware only", "Forming in Delaware and stopping there", "Doing business in CA → foreign registration, $800 + fee, inability to sue", "Questionnaire (San Diego)", "Penalties; unenforceable contracts in CA courts", "M", "Cal. Corp. Code §17708.02", "high")
    c.trap(6, "§199A assumed", "Promising the 20% QBI deduction on consulting income", "Consulting is an SSTB; phases out above the threshold; W-2 wages aren't QBI", "Projections", "Wrong comparison", "L", "§199A(d)(2)", "medium")
    c.oracle("Recommendation rejects S election while Tomás is NRA", "true", "exact", "recommendation.md")
    c.oracle("Tomás's service equity structured as a profits interest (or equivalent non-taxable grant)", "true", "exact", "")
    c.oracle("83(b) 30-day deadline listed", "true", "exact", "compliance_calendar.md")
    c.oracle("CA registration/tax addressed", "true", "exact", "")
    c.oracle("Substantial presence computation shown (≈161 < 183)", "true", "±2 days", "")
    c.rubric("Pushback refused with reasons (sham ownership; later admission terminates election)")
    c.rubric("Term sheet includes divorce/death buy-sell and spousal consent")
    return c.finish()
