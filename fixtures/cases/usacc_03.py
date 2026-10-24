"""USACC-3 · L3 · Household Form 1040 with four interacting limits — 'the K-1 says loss, deduct it'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, irs_form, money, q2, COMMON_RULES

TY = 2025
# ---- TY2025 parameters (library states them; flagged for verification against Rev. Proc. 2024-40 / OBBBA)
STD_MFJ = D("31500")
CTC = D("2200")
BRACKETS_MFJ = [(D("23850"), D("0.10")), (D("96950"), D("0.12")), (D("206700"), D("0.22")), (D("394600"), D("0.24"))]
FPL_4 = D("31200")  # 2024 HHS poverty guideline, family of 4, 48 states (used for 2025 coverage year)
PTC_CAP = [(200, D("750")), (300, D("1900")), (400, D("3150"))]  # MFJ repayment limitation by %FPL upper bound


def tax_table(ti: D) -> D:
    """IRS tax table: tax on the midpoint of the $50 bracket containing ti (ti < 100,000)."""
    lo = (ti // 50) * 50
    mid = lo + D("25")
    return q2(bracket_tax(mid)).quantize(D("1"))


def bracket_tax(ti: D) -> D:
    tax, prev = D("0"), D("0")
    for top, rate in BRACKETS_MFJ:
        if ti > top:
            tax += (top - prev) * rate
            prev = top
        else:
            tax += (ti - prev) * rate
            return tax
    return tax


def applicable_pct(fpl_pct: D) -> D:
    """2025 applicable percentage (Rev. Proc. 2024-35): linear within bands."""
    bands = [(150, 200, D("0"), D("2")), (200, 250, D("2"), D("4")), (250, 300, D("4"), D("6")), (300, 400, D("6"), D("8.5"))]
    if fpl_pct < 150:
        return D("0")
    for lo, hi, a, b in bands:
        if lo <= fpl_pct < hi:
            return a + (fpl_pct - lo) / (hi - lo) * (b - a)
    return D("8.5")


def build():
    c = Case("usacc_03_household_1040", "usacc", "Household Form 1040 with four interacting limits", "L3")
    # ---- facts
    w_marcus, w_elena = D("68000"), D("54000")
    ny_wh_m, ny_wh_e = D("3842"), D("2910")       # full-year NY withholding (trap 6)
    fed_wh = D("5120") + D("3610")
    interest = D("400")
    k1_loss = D("28000")
    basis_begin = D("11500")                      # stock basis 1/1 (no debt basis)
    rent_income, rent_exp, rent_depr = D("18000"), D("29200"), D("9818")
    rental_loss = rent_income - rent_exp - rent_depr  # -21,018
    months_1095 = 6
    prem, slcsp, aptc = D("1720"), D("1690"), D("1650")
    move_date = dt.date(TY, 7, 1)
    ny_days = (move_date - dt.date(TY, 1, 1)).days  # 181

    # ---- reference computation
    k1_allowed = min(k1_loss, basis_begin)        # 11,500
    k1_suspended = k1_loss - k1_allowed           # 16,500
    magi_469 = w_marcus + w_elena + interest - k1_allowed   # 110,900 (nonpassive K-1 loss reduces MAGI; passive loss excluded)
    allowance = max(D("0"), D("25000") - (magi_469 - D("100000")) / 2) if magi_469 > D("100000") else D("25000")
    rental_allowed = min(-rental_loss, allowance) # 19,550
    rental_cf = -rental_loss - rental_allowed     # 1,468
    agi = w_marcus + w_elena + interest - k1_allowed - rental_allowed   # 91,350
    taxable = agi - STD_MFJ                       # 59,850
    tax = tax_table(taxable)
    tax_bracket = q2(bracket_tax(taxable))
    # PTC
    hh_income = agi
    fpl_pct = (hh_income / FPL_4 * 100).quantize(D("0.01"))
    ap = applicable_pct(fpl_pct)
    annual_contrib = q2(hh_income * ap / 100)
    monthly_contrib = q2(annual_contrib / 12)
    monthly_ptc = min(prem, slcsp - monthly_contrib)
    ptc = q2(monthly_ptc * months_1095)
    aptc_total = aptc * months_1095
    excess = aptc_total - ptc
    cap = next(cap for ub, cap in PTC_CAP if fpl_pct < ub) if fpl_pct < 400 else excess
    repayment = min(excess, cap)
    ctc = CTC * 1  # only the older child this year
    total_tax = tax - ctc + repayment
    refund = fed_wh - total_tax
    ny_alloc_m = q2(w_marcus * ny_days / 365)
    ny_alloc_e = q2(w_elena * ny_days / 365)

    # ---- documents
    irs_form(c, "w2_marcus_reyes_pike.pdf", f"Form W-2 Wage and Tax Statement {TY}", "OMB No. 1545-0008", [
        [("a Employee's SSN", "XXX-XX-2210"), ("b EIN", "82-4471930"), ("1 Wages", money(w_marcus)), ("2 Federal income tax withheld", money(D("5120")))],
        [("c Employer", "Reyes & Pike Consulting Inc (S corp), 1 Liberty Plaza, New York NY 10006"), ("3 SS wages", money(w_marcus)), ("4 SS tax", money(w_marcus * D("0.062"))), ("5 Medicare wages", money(w_marcus))],
        [("e Employee", "Marcus D Reyes, 4120 Bayshore Blvd Apt 9C, Tampa FL 33611"), ("15 State", "NY"), ("16 State wages", money(w_marcus)), ("17 State income tax", money(ny_wh_m))],
    ])
    irs_form(c, "w2_elena_reyes.pdf", f"Form W-2 Wage and Tax Statement {TY}", "OMB No. 1545-0008", [
        [("a Employee's SSN", "XXX-XX-8834"), ("b EIN", "13-3029944"), ("1 Wages", money(w_elena)), ("2 Federal income tax withheld", money(D("3610")))],
        [("c Employer", "Halvorsen Media Group LLC, 230 Park Ave S, New York NY 10003"), ("3 SS wages", money(w_elena)), ("4 SS tax", money(w_elena * D("0.062"))), ("12a", "DD 7,140.00 (Jul–Dec employer coverage)")],
        [("e Employee", "Elena M Reyes, 4120 Bayshore Blvd Apt 9C, Tampa FL 33611"), ("15 State", "NY"), ("16 State wages", money(w_elena)), ("17 State income tax", money(ny_wh_e))],
    ])
    irs_form(c, "k1_1120s_reyes_pike.pdf", f"Schedule K-1 (Form 1120-S) {TY} — Shareholder's Share of Income, Deductions, Credits", "OMB No. 1545-0123", [
        [("A Corporation EIN", "82-4471930"), ("B Corporation", "Reyes & Pike Consulting Inc"), ("E Shareholder", "Marcus D Reyes"), ("F % of stock owned", "40.000%")],
        [("1 Ordinary business income (loss)", money(-k1_loss)), ("16 Items affecting basis — D Distributions", "0.00"), ("17 Other — AC Gross receipts", "612,400"), ("Part II G", "Shareholder materially participates: Yes")],
    ])
    irs_form(c, "1095a_marketplace.pdf", f"Form 1095-A Health Insurance Marketplace Statement {TY}", "OMB No. 1545-2232", [
        [("Marketplace", "NY State of Health"), ("Policy number", "NYSH-77120-RE"), ("Recipient", "Marcus D Reyes"), ("Covered individuals", "Marcus, Elena, Sofia (15), Leo (9)")],
        [("Months covered", "January–June"), ("21–26 A. Monthly enrollment premium", money(prem)), ("B. SLCSP premium", money(slcsp)), ("C. Advance payment of PTC", money(aptc))],
        [("33 Annual totals", ""), ("A", money(prem * months_1095)), ("B", money(slcsp * months_1095)), ("C", money(aptc_total))],
    ])
    irs_form(c, "1098_mortgage.pdf", f"Form 1098 Mortgage Interest Statement {TY}", "OMB No. 1545-1380", [
        [("RECIPIENT/LENDER", "Gulf Atlantic Mortgage LLC"), ("PAYER/BORROWER", "Marcus D Reyes & Elena M Reyes"), ("1 Mortgage interest received", "6,480.00"), ("Property", "4120 Bayshore Blvd Apt 9C, Tampa FL (acquired 07/03/2025)")],
    ])
    irs_form(c, "1099int_chase.pdf", f"Form 1099-INT {TY}", "OMB No. 1545-0112", [[("PAYER", "JPMorgan Chase Bank NA"), ("RECIPIENT", "Elena M Reyes"), ("1 Interest income", money(interest))]])
    c.doc("rental_summary_brooklyn.md", f"""
# Brooklyn condo rental — {TY} summary (prepared by Elena)

Property: 318 Dean St #4B, Brooklyn NY 11217. Rented all year to the same tenant (lease attached in
prior-year file). Elena handles everything herself (approves tenants, arranges repairs).

| Item | Amount |
|---|---:|
| Rent received (12 × $1,500) | {money(rent_income)} |
| Mortgage interest | 11,900.00 |
| Common charges | 7,860.00 |
| Property tax | 5,140.00 |
| Repairs (water heater, Jun) | 2,350.00 |
| Insurance | 1,150.00 |
| Management/legal | 800.00 |
| **Total expenses (excl. depreciation)** | **{money(rent_exp)}** |
| Depreciation (building basis $270,000 ÷ 27.5) | {money(rent_depr)} |

Note: rent is below market — the tenant has been there 6 years and we never raised it. Market is ~$2,600.
""")
    c.doc("marcus_basis_note.md", f"""
# Note from Marcus re: my S-corp stock (Reyes & Pike Consulting Inc)

I put in $10,000 when we formed the company in 2021 for 40% of the shares. Since then:

| Year | My share of income/(loss) | Distributions to me |
|---|---:|---:|
| 2021 | (2,100) | 0 |
| 2022 | 6,400 | 0 |
| 2023 | 9,800 | (12,000) |
| 2024 | 4,600 | (5,200) |
| {TY} | (28,000) per K-1 | 0 |

I never lent the company money (we have a bank line, Pike personally guarantees it). My understanding
from a friend is that the {TY} loss comes straight off our income.
""")
    c.doc("email_move_dates.txt", f"""
From: Elena Reyes
Subject: moving dates for the tax guy

We closed on the Tampa place July 3 and moved in that weekend; our Brooklyn apartment lease ended
June 30 and we were out by then (we slept at my mother's in Queens June 28–30, then drove down).
Both of our employers kept withholding New York all year because nobody updated the forms — Marcus's
company is in NYC and he just works remotely now; Halvorsen let me go fully remote.
Kids: Sofia (15) is ours. Leo (9) is my son from before; see the custody agreement.
""")
    c.doc_pdf("custody_agreement_excerpt.pdf", f"""
# STIPULATION AND ORDER — CUSTODY AND SUPPORT (excerpt)
**Matter of Reyes (f/k/a Marchetti) and Castellano** — Family Court of the State of New York, Kings County, Docket V-04418-19

**9. Tax dependency.** The parties shall alternate claiming the child, LEO CASTELLANO (DOB 03/14/2016), as a dependent for federal and state income tax purposes. **The Father shall claim the child in odd-numbered tax years; the Mother shall claim the child in even-numbered tax years.** The custodial parent shall execute IRS Form 8332 for each year in which the non-custodial parent is entitled to claim the child. The child resides primarily with the Mother.

*So ordered, 11/20/2019.* /s/ Hon. R. Alvarez, J.F.C.
""", scan=True)

    # ---- library
    c.library("1040_instructions_tax_computation.md", f"{TY} Form 1040 Instructions — tax computation, standard deduction, filing status (excerpts)", f"IRS {TY} Form 1040 Instructions", f"""
**Standard deduction ({TY}).** Married filing jointly: **${STD_MFJ:,}**. Single: $15,750. Head of household: $23,625.

**Tax computation.** If your taxable income is **less than $100,000**, you **must** use the Tax Table to figure your tax; do not compute it from the rate schedules. The Tax Table figures tax at the midpoint of each $50 income bracket. If taxable income is $100,000 or more, use the Tax Computation Worksheet.

**Filing status.** Your status is determined as of December 31. A married couple living together files jointly or separately.

**Child tax credit ({TY}).** ${CTC:,} per qualifying child under age 17 at the end of the year who is your dependent. A child claimed by the other parent under a Form 8332 release is not your qualifying child for the credit.

**Dependents — children of divorced or separated parents.** The custodial parent may release the claim to the noncustodial parent on Form 8332. Where a decree or agreement alternates years, the agreement controls which parent claims the child for that year.
""", kind="irs instructions", verbatim=False, note="Verify TY2025 standard deduction and CTC under OBBBA (P.L. 119-21).")
    rows = []
    for lo in range(59000, 61000, 50):
        lo_ = D(lo)
        rows.append(f"| {lo:,} | {lo+50:,} | {tax_table(lo_):,} |")
    c.library("tax_table_2025_excerpt.md", f"{TY} Tax Table — excerpt, married filing jointly, taxable income $59,000–$61,000", f"IRS {TY} Tax Table", "If taxable income is at least / but less than → tax (MFJ):\n\n| At least | But less than | MFJ tax |\n|---:|---:|---:|\n" + "\n".join(rows) + f"\n\n*(Rate schedule for reference only — not to be used under $100,000: 10% to $23,850; 12% to $96,950; 22% to $206,700; 24% to $394,600.)*", kind="irs table", verbatim=False, note="Regenerated from the bracket midpoints; verify against the published table.")
    c.library("form7203_instructions_excerpt.md", "Form 7203 — S Corporation Shareholder Stock and Debt Basis Limitations (instructions excerpt)", f"IRS Form 7203 Instructions {TY}", """
A shareholder's share of losses and deductions is **allowed only to the extent of the shareholder's adjusted stock basis plus debt basis** (IRC §1366(d)). Losses in excess of basis are **suspended and carried forward** indefinitely until basis is restored. Stock basis is increased by capital contributions and the shareholder's share of income, and decreased by distributions and by losses (in that order). A guarantee of corporate debt does **not** create debt basis; only a direct loan from the shareholder to the corporation does.

Part I, line 1: stock basis at beginning of year. Line 11: loss allowed = lesser of the loss and the basis available. Line 12 et seq.: carryover.
""", kind="irs instructions", verbatim=False)
    c.library("form8582_instructions_excerpt.md", "Form 8582 — Passive Activity Loss Limitations: $25,000 special allowance (excerpt)", f"IRS Form 8582 Instructions {TY}; IRC §469(i)", """
Rental real estate activities in which you **actively participate** qualify for a special allowance of up to **$25,000** of loss against nonpassive income. The allowance is **reduced by 50% of the amount by which modified adjusted gross income exceeds $100,000**, and is zero at MAGI of $150,000 or more (married filing jointly).

**Modified AGI** for this purpose is AGI figured **without** any passive activity loss, without the deduction for one-half of SE tax, IRA deductions, student loan interest, and certain other items. Nonpassive losses allowed in the year (for example an S corporation loss where the shareholder materially participates, to the extent allowed by basis) **do** reduce MAGI.

Disallowed losses are carried forward (Part VII) to the next year.

**Below-market rental.** If a dwelling is rented to any person at less than fair rental value, the days are treated as personal-use days (IRC §280A(d)(2)(C)); a loss is then not allowed. Renting below market to an unrelated tenant because rent was never raised does not by itself trigger this rule if the rent is a fair rental for that lease.
""", kind="irs instructions", verbatim=False)
    c.library("form8962_instructions_excerpt.md", f"Form 8962 — Premium Tax Credit (instructions excerpt, {TY})", f"IRS Form 8962 Instructions {TY}; Rev. Proc. 2024-35; Rev. Proc. 2024-40", f"""
**Household income** = modified AGI (AGI + tax-exempt interest + nontaxable Social Security + excluded foreign income) of the taxpayer and dependents required to file.

**Federal poverty line** used for {TY} coverage (family of 4, 48 contiguous states): **${FPL_4:,}**.

**Applicable figure** (Table 2, linear within band): <150% FPL: 0.00%; 150–200%: 0.00–2.00%; 200–250%: 2.00–4.00%; 250–300%: 4.00–6.00%; 300–400%: 6.00–8.50%; 400%+ : 8.50%.

**Monthly PTC** = lesser of (a) the enrollment premium and (b) SLCSP premium minus the monthly contribution amount (household income × applicable figure ÷ 12).

**Repayment limitation (line 28).** If advance payments exceed the credit, the excess you must repay is limited, for married filing jointly, to: **$750** if household income < 200% FPL; **$1,900** if 200%–<300%; **$3,150** if 300%–<400%. **No limitation applies at 400% or more.**
""", kind="irs instructions", verbatim=False, note="Verify the TY2025 repayment limitation amounts.")
    c.library("ny_it203_part_year_excerpt.md", "New York Form IT-203 — part-year residents (instructions excerpt)", f"NYS Dept. of Taxation and Finance, IT-203-I ({TY})", """
A part-year resident is taxed on all income received during the resident period and on New York source income during the nonresident period. **Wages** for services performed entirely outside New York during the nonresident period are not New York source income — **except** that, under the "convenience of the employer" rule, wages paid by a New York employer to an employee who works from an out-of-state location for the employee's own convenience are New York source income. Days worked outside New York for the employer's necessity are not.

Allocate by the ratio of days in the resident period (or New York workdays) to total days/workdays, and attach the allocation schedule. Tax withheld in excess of the tax due is refunded on IT-203.
""", kind="state instructions", verbatim=False, note="The convenience-of-the-employer rule is REAL and makes the NY allocation a genuine judgment: see trap 6.")

    c.contract(f"""
# Engagement: {TY} Form 1040 — Marcus and Elena Reyes (married filing jointly)

Prepare the federal return and the New York part-year allocation from the file. Marcus expects the
S-corp loss to "come straight off" their income. Use only the library.

## Deliverables (under `workspace/deliverable/`)
1. `return.json`:
   ```json
   {{"form1040": {{"1a_wages": 0, "2b_interest": 0, "8_other_income_sch1": 0, "11_agi": 0, "12_deduction": 0, "15_taxable_income": 0, "16_tax": 0, "19_ctc": 0, "17_sch2_excess_aptc": 0, "24_total_tax": 0, "25d_withholding": 0, "34_refund_or_37_owed": 0}},
    "form7203": {{"stock_basis_begin": 0, "loss_allowed": 0, "loss_suspended": 0}},
    "form8582": {{"rental_loss": 0, "magi": 0, "special_allowance": 0, "loss_allowed": 0, "carryforward": 0}},
    "form8962": {{"household_income": 0, "fpl_pct": 0, "applicable_figure_pct": 0, "annual_ptc": 0, "aptc": 0, "excess": 0, "repayment_limitation": 0, "repayment": 0}},
    "dependents": ["..."], "ny": {{"resident_days": 0, "marcus_ny_wages": 0, "elena_ny_wages": 0, "method": "..."}}}}
   ```
2. `return.md` — each figure with its arithmetic and the library authority.
3. `judgment_calls.md` — every place you had to decide something (basis, residency method, dependents, below-market rent), with the alternative you rejected.
4. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Marcus Reyes; confident, slightly impatient; Elena is more careful.", [
        {"id": "fmv_rent", "trigger": ["fair market", "below market", "related", "relative", "tenant", "who is the tenant"], "answer": "Elena: the tenant is a stranger, a nurse we found through a broker in 2019. We just never raised the rent.", "if_not_asked": "must_flag"},
        {"id": "contrib", "trigger": ["contribut", "put money in", "loan to the company", "basis"], "answer": "Marcus: no, I haven't put anything in since 2021 and I never lent it money. Pike guarantees the bank line.", "if_not_asked": "none"},
        {"id": "convenience", "trigger": ["convenience", "employer's necessity", "required to work remote", "office in New York", "why remote"], "answer": "Marcus: the company said remote was fine when I asked to move; they didn't need me out of state. Elena: Halvorsen closed their Tampa office years ago; they approved my request.", "if_not_asked": "must_flag"},
        {"id": "leo_8332", "trigger": ["8332", "Leo", "custody", "odd year", "claim"], "answer": "Elena: I signed the 8332 for Leo's dad for {TY}, it's his year.", "if_not_asked": "penalize"},
        {"id": "employer_coverage", "trigger": ["employer coverage", "why only six months", "July", "1095"], "answer": "Elena: I got on Halvorsen's plan July 1 when we moved, so we dropped the marketplace plan.", "if_not_asked": "none"},
    ], pushback=[{"when": "if the return allows less than the full $28,000 K-1 loss", "message": "Marcus: My buddy's CPA let him take his whole loss. Why are you suspending $16,500? Can't we count Pike's guarantee or something?"}])

    ref = {"form1040": {"1a_wages": w_marcus + w_elena, "2b_interest": interest, "8_other_income_sch1": -(k1_allowed + rental_allowed), "11_agi": agi, "12_deduction": STD_MFJ,
                        "15_taxable_income": taxable, "16_tax": tax, "16_tax_bracket_math_WRONG": tax_bracket, "19_ctc": ctc, "17_sch2_excess_aptc": repayment, "24_total_tax": total_tax,
                        "25d_withholding": fed_wh, "34_refund_or_37_owed": refund},
           "form7203": {"stock_basis_begin": basis_begin, "loss_allowed": k1_allowed, "loss_suspended": k1_suspended},
           "form8582": {"rental_loss": rental_loss, "magi": magi_469, "special_allowance": allowance, "loss_allowed": rental_allowed, "carryforward": rental_cf},
           "form8962": {"household_income": hh_income, "fpl_pct": fpl_pct, "applicable_figure_pct": q2(ap), "annual_ptc": ptc, "aptc": aptc_total, "excess": excess, "repayment_limitation": cap, "repayment": repayment},
           "dependents": ["Sofia Reyes (CTC)"], "ny": {"resident_days": ny_days, "marcus_ny_wages": ny_alloc_m, "elena_ny_wages": ny_alloc_e, "method": "resident-period days; convenience rule discussed — employers approved remote for employee convenience, so post-move wages are arguably NY-source; accepted answers: (a) days allocation with the convenience-rule risk disclosed, or (b) full-year NY source with the argument stated"},
           "wrong_path": {"agi_if_full_losses": w_marcus + w_elena + interest - k1_loss + rental_loss}}
    c.reference("return_reference.json", ref)
    c.trap(1, "Full K-1 loss", f"Deducting {money(k1_loss)}", f"§1366(d): basis {money(basis_begin)} limits the loss; {money(k1_suspended)} suspended on Form 7203; a guarantee creates no debt basis", "Basis note (10,000 −2,100 +6,400 +9,800 −12,000 +4,600 −5,200 = 11,500); pushback invokes the guarantee", "Underpayment, penalties, amended return", "C", "Form 7203 instr.; §1366(d)", "high")
    c.trap(2, "Full rental loss", f"Deducting {money(-rental_loss)}", f"§469(i) allowance {money(allowance)} at MAGI {money(magi_469)}; allowed {money(rental_allowed)}, carryforward {money(rental_cf)}. Note the interaction: deducting the full K-1 loss drops MAGI below $100k and 'unlocks' the full rental loss — one wrong answer manufactures another", "W-2s; Form 8582 instr.", "Underpayment", "H", "Form 8582 instr.; §469(i)", "high")
    c.trap(3, "Bracket arithmetic instead of the tax table", f"Tax {money(tax_bracket)}", f"Table required under $100k: {money(tax)}", "Library tax table", "Strict line fail (TaxCalcBench failure mode)", "C", "1040 instr.", "high")
    c.trap(4, "PTC repayment uncapped or credit unadjusted", f"Repaying the full excess {money(excess)}", f"Household income {fpl_pct}% FPL → limitation {money(cap)}", "1095-A; Form 8962 instr.", "Overpayment of {money(excess - repayment)}", "H", "Form 8962 instr.", "medium — verify TY2025 cap amounts")
    c.trap(5, "Claiming Leo", "Two dependents / two CTCs", "Custody order: father claims Leo in odd years; Elena signed 8332", "Custody excerpt ¶9; client script", "Disallowed dependent; CTC clawback; notice", "M", "1040 instr.", "high")
    c.trap(6, "NY allocation by withholding", "Treating full-year NY withholding as correct, or allocating by days without addressing the convenience-of-the-employer rule", "Part-year: resident-period wages are NY; post-move remote wages for NY employers raise the convenience rule (client script: remote was for the employees' convenience) — must be analyzed, not ignored; either defended conclusion accepted", "Move email; IT-203 excerpt", "Lost refund or unexpected NY assessment", "M", "IT-203-I", "medium — judgment item; graded on analysis, not one number")
    c.trap(7, "Below-market rent", "Ignoring the note that rent is below market", "§280A(d)(2)(C) if below fair rental; here unrelated tenant at a stale lease → fair rental for that lease, loss allowed, but must be asked/flagged", "Rental summary note; client script", "—", "M", "Form 8582 instr. note", "medium")
    for k, v in ref["form1040"].items():
        if "WRONG" not in k:
            c.oracle(f"form1040.{k}", str(v), "exact (±$1 for 16/24/34)", "return.json")
    c.oracle("form7203.loss_allowed / loss_suspended", f"{k1_allowed} / {k1_suspended}", "exact", "")
    c.oracle("form8582.loss_allowed / carryforward", f"{rental_allowed} / {rental_cf}", "exact", "")
    c.oracle("form8962.repayment", str(repayment), "exact", "")
    c.oracle("dependents", "Sofia only", "exact", "")
    c.rubric("judgment_calls.md discusses the convenience-of-the-employer rule for NY and the below-market rent question")
    c.rubric("Pushback answered: guarantee ≠ debt basis, with authority")
    c.note(f"Chain of interaction: K-1 allowed {k1_allowed} → MAGI {magi_469} → allowance {allowance} → rental allowed {rental_allowed} → AGI {agi} → FPL {fpl_pct}% → cap {cap}. Reviewer verifies by recomputing with the module.")
    return c.finish()
