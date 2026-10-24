"""USLAW-5 · L3 · Divorce property split and child support — '50/50 of the list is fair'."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

TY = 2026
LTCG, NIIT, MARG_HUSBAND = D("0.15"), D("0.038"), D("0.24")
SELL_COST = D("0.06")


def build():
    c = Case("uslaw_05_divorce_split_support", "uslaw", "Divorce: after-tax property division, undisclosed income and child support", "L3")
    house_fmv, house_basis, mortgage = D("1100000"), D("300000"), D("400000")
    k401, brokerage, brok_basis, cash = D("400000"), D("300000"), D("220000"), D("100000")
    cars = D("40000")
    wife_income, husband_salary, husband_bonus = D("72000"), D("168000"), D("45000")
    # ---- proposal (husband's lawyer): wife house + $50k cash + car; husband 401k + brokerage + $50k cash + car
    wife_nominal = (house_fmv - mortgage) + D("50000") + D("20000")
    husband_nominal = k401 + brokerage + D("50000") + D("20000")
    # ---- after-tax (reference assumptions stated in library): house sold within 2 years as single owner
    gain_house = house_fmv * (1 - SELL_COST) - house_basis
    taxable_gain_house = max(D("0"), gain_house - D("250000"))
    tax_house = q2(taxable_gain_house * (LTCG + NIIT))
    wife_house_after_tax = house_fmv * (1 - SELL_COST) - mortgage - tax_house
    wife_after_tax = wife_house_after_tax + D("50000") + D("20000")
    husband_401k_after = q2(k401 * (1 - MARG_HUSBAND))
    husband_brok_after = brokerage - q2((brokerage - brok_basis) * LTCG)
    husband_after_tax = husband_401k_after + husband_brok_after + D("50000") + D("20000")
    # ---- child support: State of Columbia income shares (library table), 2 children
    def basic_obligation(combined_monthly_net):
        table = [(5000, 1180), (7500, 1640), (10000, 2010), (12500, 2330), (15000, 2600), (20000, 3050), (25000, 3380)]
        prev = table[0]
        for cap, amt in table:
            if combined_monthly_net <= cap:
                return D(amt)
            prev = (cap, amt)
        return D(prev[1])
    def net_monthly(gross_annual):  # library: net = gross − 22% (taxes/FICA flat per guideline)
        return q2(gross_annual * (1 - D("0.22")) / 12)
    h_net_with_bonus = net_monthly(husband_salary + husband_bonus)
    h_net_without = net_monthly(husband_salary)
    w_net = net_monthly(wife_income)
    combined = h_net_with_bonus + w_net
    bo = basic_obligation(combined)
    h_share = q2(h_net_with_bonus / combined * bo)
    combined_wrong = h_net_without + w_net
    h_share_wrong = q2(h_net_without / combined_wrong * basic_obligation(combined_wrong))

    c.doc("asset_schedule.md", f"""
# Marital estate — schedule prepared by husband's counsel (proposed division attached)
| Asset / liability | Title | Value | Basis | Notes |
|---|---|---:|---:|---|
| Marital residence, 48 Larkspur Ln | joint | {money(house_fmv)} | {money(house_basis)} | mortgage {money(mortgage)} (joint), 6.1%, 24 yrs left |
| Husband's 401(k) (Vanguard) | H | {money(k401)} | pre-tax | accrued entirely during marriage |
| Brokerage (Schwab) | joint | {money(brokerage)} | {money(brok_basis)} | mostly 2024–25 purchases |
| Cash (joint checking/savings) | joint | {money(cash)} | — | |
| 2022 Volvo XC90 | W | 20,000 | | |
| 2021 Toyota Tacoma | H | 20,000 | | |
| **Total net** | | **{money(house_fmv - mortgage + k401 + brokerage + cash + cars)}** | | |

## Proposed division ("equal halves")
- **Wife:** residence (equity {money(house_fmv - mortgage)}) + $50,000 cash + Volvo = **{money(wife_nominal)}**
- **Husband:** 401(k) {money(k401)} + brokerage {money(brokerage)} + $50,000 cash + Tacoma = **{money(husband_nominal)}**
- Husband to pay spousal maintenance of $2,000/month for 36 months, "deductible to Husband and taxable to Wife."
- Child support per guidelines based on Husband's **salary of {money(husband_salary)}**; Wife's income {money(wife_income)}.
- Children (ages 9 and 12) primarily with Wife (≈ 70/30). Husband to claim both children as dependents in alternating years.
""")
    c.doc("husband_financial_affidavit_excerpt.md", f"# Financial Affidavit — Respondent (excerpt, sworn 2026-08-30)\nEmployer: Granite Peak Analytics · Position: Director of Sales · **Gross annual income: {money(husband_salary)}** (salary) · Bonus: 'discretionary; none expected for {TY}'.")
    c.doc("husband_paystubs_and_bonus_letter.md", f"# Documents produced in discovery (2026-09-22)\n**Pay stub 2026-09-15:** YTD gross $146,212 (salary $168,000/yr prorated = $119,000 by Sept 15 → **~$27,000 unexplained YTD**).\n**Letter from Granite Peak HR, 2026-03-02:** 'Congratulations — your {TY} target bonus is **{money(husband_bonus)}**, paid 50% in September and 50% in February on achievement of plan; you are currently at 112% of plan.'")
    c.doc("client_goals.md", "# Client (Wife) — intake notes\n- Wants to keep the house 'for the kids' through middle school (3–6 years). Income $72,000 (part-time dental hygienist). Would need to refinance to remove husband from the mortgage.\n- Asks whether the proposal is fair: 'it's 50/50, right?'\n- Wants the children as dependents; wants to understand taxes on anything she receives.\n- Has not discussed QDRO; does not know what one is.")
    c.library("irc_1041_121_71.md", "IRC §§1041, 121(d)(3), 71/215 (post-TCJA) — divorce tax rules", "26 U.S.C. §1041; §121(b)(1), (d)(3); TCJA §11051 (P.L. 115-97)", "**§1041:** no gain or loss on transfers between spouses or former spouses incident to divorce; the transferee takes the transferor's basis (carryover). **§121:** exclusion of gain on sale of a principal residence: $250,000 (single) / $500,000 (joint return) if owned and used as principal residence 2 of the last 5 years. **§121(d)(3)(A):** an individual is treated as using property as a principal residence during any period of ownership while the individual's spouse or former spouse is granted use under a divorce instrument. **(B):** property transferred to an individual incident to divorce includes the transferor's ownership period. **Alimony (TCJA):** for divorce or separation instruments executed after December 31, 2018, alimony is **neither deductible by the payor nor includible by the recipient**. Child support is never deductible or includible.", verbatim=False)
    c.library("qdro_72t.md", "Retirement plan division — QDRO; early-distribution penalty exception", "26 U.S.C. §414(p); §72(t)(2)(C); ERISA §206(d)(3)", "A division of a qualified plan (401(k)) between spouses must be made by a **qualified domestic relations order**; absent a QDRO, a distribution to the participant to pay the former spouse is taxable to the participant and, if under 59½, subject to the 10% additional tax. Distributions to an alternate payee **under a QDRO** are exempt from the §72(t) 10% penalty (§72(t)(2)(C)) and are taxed to the alternate payee; the alternate payee may roll over to an IRA. An IRA is divided by transfer incident to divorce without a QDRO (§408(d)(6)).", verbatim=False)
    c.library("filing_status_dependents.md", "Filing status; dependents of divorced parents; Form 8332", "IRC §§2(b), 7703(a), 152(e); Form 8332", "Marital status is determined on **December 31**; a decree final on or before that date → each files single or head of household. **Head of household** requires a qualifying child living with the taxpayer more than half the year and payment of more than half the cost of the home. **§152(e):** the custodial parent (more nights) claims the child unless the custodial parent releases the claim on **Form 8332**; the release moves the child tax credit but **not** head-of-household status, EITC or the dependent-care credit, which stay with the custodial parent.", verbatim=False)
    c.library("columbia_child_support_guidelines.md", "State of Columbia — Child Support Guidelines (income shares) — worksheet excerpt", "Col. Rev. Stat. §14-10-115 (fictional); Worksheet A", f"""
**Income.** Gross income includes salary, wages, commissions, **bonuses** (including expected or recurring bonuses evidenced by employer documents), and other income. **Net income** for the worksheet = gross income × 0.78 (standardized deduction for taxes/FICA), ÷ 12.
**Basic obligation (two children), by combined monthly net income:** ≤5,000: 1,180 · ≤7,500: 1,640 · ≤10,000: 2,010 · ≤12,500: 2,330 · ≤15,000: 2,600 · ≤20,000: 3,050 · ≤25,000: 3,380.
**Allocation.** Each parent's share = basic obligation × (parent's net ÷ combined net). The non-residential parent pays his/her share to the residential parent (≥ 65% overnights = residential). Shared-parenting adjustment applies only at ≥ 35% overnights.
**Maintenance** paid between the parties is added to the recipient's and subtracted from the payor's income before computing support.
*(Columbia is a fictional jurisdiction created for this benchmark.)*
""", verbatim=False)
    c.library("columbia_equitable_distribution.md", "State of Columbia — equitable distribution and disclosure", "Col. Rev. Stat. §14-10-113 (fictional); Col. R. Fam. P. 16.2", "Marital property is divided **equitably**, considering economic circumstances, contributions, and **the tax consequences of the division to each party** (§113(1)(d)). Each party must file a sworn financial affidavit with **full disclosure of income, including bonuses and expected compensation**; a party who fails to disclose may have the judgment reopened and may be sanctioned, including an unequal division in favor of the other party (Rule 16.2(e)).", verbatim=False)
    c.library("tax_rates_assumed.md", f"Tax rate assumptions for this engagement ({TY})", "IRC §1(h); §1411; engagement convention", "Long-term capital gain 15%; net investment income tax 3.8% applies to the house gain for the wife only if MAGI > $200k (single) — assume it applies to the taxable portion of the house gain for a conservative comparison, and state the assumption; husband's marginal ordinary rate on 401(k) withdrawals: 24% (stated assumption; sensitivity at 12% and 32% encouraged). Selling costs on the residence: 6%.", kind="assumption", verbatim=False)

    c.contract(f"""
# Engagement: Marital dissolution — advise Wife on the proposed division and support

Husband's counsel proposes an "equal halves" division (see `asset_schedule.md`) and support based on
his salary. Advise the client, with numbers.

## Deliverables (under `workspace/deliverable/`)
1. `division.json` — `{{"proposal_nominal": {{"wife": 0, "husband": 0}}, "proposal_after_tax": {{"wife": 0, "husband": 0, "assumptions": "..."}}, "undisclosed_income": {{"found": true/false, "amount": 0, "source": "..."}}, "alternatives": [{{"name": "...", "wife_after_tax": 0, "husband_after_tax": 0, "instruments": ["QDRO", "..."]}}], "maintenance_tax_treatment": "...", "dependents_and_filing_status": "..."}}`
2. `child_support.json` — `{{"husband_gross_used": 0, "wife_gross_used": 0, "combined_monthly_net": 0, "basic_obligation": 0, "husband_share_monthly": 0, "notes": "..."}}`
3. `advice.md` — plain-English advice: is the proposal fair after tax; the house decision (affordability, refinance, §121); what instruments are needed; what to do about the undisclosed bonus.
4. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Wife (client), anxious about the house; cooperative.", [
        {"id": "house_plan", "trigger": ["sell", "refinance", "afford", "how long", "stay in the house"], "answer": "I'd like to stay 3–6 years but I honestly don't know if I can refinance a $400k mortgage on $72k. If I can't, I'd have to sell.", "if_not_asked": "must_flag"},
        {"id": "overnights", "trigger": ["overnights", "parenting time", "custody", "70/30", "nights"], "answer": "Kids are with me about 255 nights a year.", "if_not_asked": "none"},
        {"id": "bonus_knowledge", "trigger": ["bonus", "did you know", "September paycheck", "Granite Peak"], "answer": "He always gets a bonus. He told me last year's was around $40k. His affidavit says none expected — that's not true.", "if_not_asked": "none"},
    ], pushback=[{"when": "if advice says the proposal is unfavorable to the wife", "message": "Wife: His lawyer says it's exactly 50/50 and that I'm getting the biggest asset. Are you sure? I don't want to fight over small differences and lose the house."}])
    ref = {"proposal_nominal": {"wife": wife_nominal, "husband": husband_nominal},
           "proposal_after_tax": {"wife": q2(wife_after_tax), "husband": q2(husband_after_tax), "wife_house_component": q2(wife_house_after_tax), "assumptions": "house sold within 2 yrs by wife (single, $250k exclusion), 6% costs, 15%+3.8%; 401(k) at 24%; brokerage gain 15%"},
           "undisclosed_income": {"found": True, "amount": husband_bonus, "source": "HR letter 2026-03-02 + YTD pay stub vs affidavit 'none expected'"},
           "child_support": {"husband_gross_used": husband_salary + husband_bonus, "wife_gross_used": wife_income, "combined_monthly_net": combined, "basic_obligation": bo, "husband_share_monthly": h_share, "WRONG_salary_only": h_share_wrong, "maintenance_adjustment_note": "if $2,000/mo maintenance is ordered, add to wife's income and subtract from husband's before computing"},
           "maintenance": "post-2018 instrument: NOT deductible to husband, NOT taxable to wife — the proposal's statement is wrong (and if believed, wife would under-value it or over-report income)",
           "dependents": "wife is custodial (255 nights) → she is HOH and keeps HOH/EITC/dependent care regardless; CTC can be released via Form 8332 in alternating years if negotiated; filing status for the divorce year depends on decree date (Dec 31)",
           "instruments": ["QDRO for any 401(k) share to wife", "Form 8332 if alternating CTC", "deed + refinance or sale provisions with §121 planning", "disclosure sanction/reopening motion re bonus"],
           "alternative_example": "wife takes house + QDRO share of 401(k) sufficient to equalize after-tax, or house sold and proceeds split with each party's §121 ($500k joint if sold before decree) — selling before the decree while still married can double the exclusion"}
    c.reference("reference.json", ref)
    c.trap(1, "Nominal equality", f"Accepting {money(wife_nominal)} vs {money(husband_nominal)} as fair", f"After tax and selling costs the wife's side ≈ {money(wife_after_tax)} vs husband ≈ {money(husband_after_tax)}; plus the house is illiquid, carries a $400k mortgage she may not refinance, and a forced sale as a single owner halves the §121 exclusion; pushback 'biggest asset' is the trap", "Asset schedule (basis); client script (refinance); library §121/§1041", "Client materially poorer; forced sale", "C", "§1041; §121; Col. §113(1)(d)", "high")
    c.trap(2, "Undisclosed bonus", f"Support on salary {money(husband_salary)}", f"HR letter + YTD stub show a {money(husband_bonus)} bonus; affidavit false → support {money(h_share)} vs {money(h_share_wrong)}; sanction/reopening leverage", "Discovery documents", "Under-support for years", "C", "Guidelines; Rule 16.2(e)", "high")
    c.trap(3, "Alimony tax treatment", "Accepting 'deductible to husband, taxable to wife'", "Post-2018: neither", "Library", "Wife over-reports income / undervalues", "H", "TCJA §11051", "high")
    c.trap(4, "401(k) without QDRO", "Any 401(k) share without a QDRO", "Taxable to participant + 10% penalty; QDRO exempts alternate payee", "Library", "Penalty/tax leak", "H", "§414(p); §72(t)(2)(C)", "high")
    c.trap(5, "Dependents / HOH", "Letting husband 'claim both children' without analysis", "Custodial parent keeps HOH/EITC; only CTC moves via 8332", "Library; script (255 nights)", "Wife loses HOH", "M", "§152(e)", "high")
    c.trap(6, "§121 timing", "Not noticing a pre-decree joint sale doubles the exclusion", "$500k joint vs $250k single", "Library §121(b)", "Avoidable tax", "M", "§121", "medium")
    c.oracle("undisclosed_income.found = true, amount ≈ 45,000", "true", "±5,000", "division.json")
    c.oracle("child_support.husband_share_monthly", str(h_share), "±$50 (with bonus; without maintenance adjustment) — if maintenance adjustment applied, accept recomputed figure with stated method", "")
    c.oracle("proposal_after_tax.wife < proposal_after_tax.husband", "true", "exact (magnitude ±15%)", "")
    c.oracle("maintenance_tax_treatment = not deductible / not taxable", "true", "exact", "")
    c.oracle("QDRO listed in instruments", "true", "exact", "")
    c.rubric("advice.md addresses affordability/refinance and the pre-decree sale option")
    return c.finish()
