"""USACC-1 · L1 · Gig-worker Schedule C — 'the forms add up, so file them'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, bank_statement, irs_form, money, q2, COMMON_RULES

TY = 2025
MILEAGE_RATE_TY = D("0.70")      # IRS Notice 2025-5 (verify)
SE_FACTOR = D("0.9235")
SE_RATE = D("0.153")


def build():
    c = Case("usacc_01_schedule_c", "usacc", "Gig-worker intake and Schedule C", "L1")
    r = c.rng

    # ---------------- facts
    w2 = dict(employer="Larkspur Interactive LLC", ein="74-3318820", wages=D("24800.00"), fed=D("2310.00"), ss_tax=D("1537.60"), med_tax=D("359.60"))
    nec = [
        dict(payer="Beacon Fintech Inc", tin="83-1192044", amount=D("18500.00"), via="PayHub"),
        dict(payer="Orchard Health PBC", tin="47-5520931", amount=D("12200.00"), via="PayHub"),
        dict(payer="Tessaro Studios LLC", tin="61-7740215", amount=D("9400.00"), via="direct"),
    ]
    k_gross = D("41350.00")              # Beacon + Orchard + 10,650 of small clients
    fee_rate = D("0.029")
    k_fees = q2(k_gross * fee_rate)      # 1,199.15
    k_net = k_gross - k_fees             # 40,150.85
    gross_receipts = k_gross + D("9400.00")   # 50,750.00 (correct)
    naive_gross = k_gross + sum(n["amount"] for n in nec)  # 81,450.00 (trap)

    # ---------------- bank CSV (one account, mixed)
    rows = []
    def add(m, d, desc, amt, year=TY):
        rows.append((dt.date(year, m, d), desc, D(str(amt))))
    # prior-year Tessaro deposit (trap #4)
    add(12, 27, "ACH CREDIT TESSARO STUDIOS INV 1041", 3000.00, year=TY - 1)
    add(12, 30, "DEBIT CARD H-E-B #412 AUSTIN TX", -84.12, year=TY - 1)
    # W-2 paychecks Jan–Apr
    for m in (1, 2, 3, 4):
        for d in (15, 28):
            add(m, min(d, 28), "DIRECT DEP LARKSPUR INTERACTIVE PAYROLL", 2437.85)
    # PayHub payouts (net of 2.9%) — monthly, Feb–Dec, sum to k_net
    payouts = [D(x) for x in ("1812.55", "2503.10", "3109.40", "3880.20", "4015.75", "3650.00", "4420.90", "4172.35", "4511.60", "4102.00")]
    rem = k_net - sum(payouts)
    payouts.append(q2(rem))
    for i, amt in enumerate(payouts):
        add(2 + i, 6 + (i % 3), "PAYHUB PAYOUT *DANA OKAFOR DESIGN", float(amt))
    # Tessaro direct 2025
    for m, amt in ((3, 2400), (6, 3100), (9, 2150), (11, 1750)):
        add(m, 19, "ACH CREDIT TESSARO STUDIOS", amt)
    # Business expenses
    for m in range(1, 13):
        add(m, 3, "FIGMA INC SUBSCRIPTION", -45.00)
        add(m, 4, "ADOBE *CREATIVE CLOUD", -59.99)
        add(m, 1, "T-MOBILE WIRELESS", -85.00)
        add(m, 2, "SPECTRUM INTERNET", -70.00)
        add(m, 5, "NETFLIX.COM", -15.49)                      # personal
        add(m, 7, "ORANGETHEORY FITNESS AUSTIN", -49.00)       # personal
        add(m, 1, "ZELLE TO: M. OKAFOR RENT", -1650.00)        # personal rent
        add(m, 12, "DEBIT CARD H-E-B #412 AUSTIN TX", -round(140 + r.random() * 90, 2))
    for m in range(5, 13):
        add(m, 8, "CAPITAL FACTORY COWORKING", -350.00)
        add(m, 9, "BLUE CROSS BLUE SHIELD TX PREMIUM", -380.00)    # SE health insurance → Sch 1, not C
    add(9, 14, "APPLE.COM/BILL MACBOOK PRO 14", -2149.00)
    add(2, 20, "HISCOX PROFESSIONAL LIABILITY", -480.00)
    add(10, 2, "SOUTHWEST AIR 526 AUS-SFO", -412.00)
    add(10, 6, "HOTEL ZEPHYR SAN FRANCISCO", -618.00)
    add(10, 6, "DESIGNWEEK SF CONFERENCE REG", -650.00)
    add(10, 7, "SQ *MARINA DELI SAN FRANCISCO", -64.00)
    add(10, 8, "TARTINE MANUFACTORY", -126.00)
    add(6, 13, "SOUTHWEST AIR 118 AUS-DEN", -389.00)            # personal — wedding (trap #2)
    add(6, 14, "VENMO: WEDDING GIFT KAT&JULES", -200.00)
    add(4, 15, "IRS USATAXPYMT ES 2025 Q1", -1500.00)
    add(6, 16, "IRS USATAXPYMT ES 2025 Q2", -2500.00)
    add(9, 15, "IRS USATAXPYMT ES 2025 Q3", -2500.00)
    rows.sort(key=lambda x: x[0])
    opening = D("4210.33")
    bank_statement(c, "bank_checking_2024-12_to_2026-01.pdf", bank="Hill Country Community Bank", holder="DANA A OKAFOR", address="2204 E Cesar Chavez St Apt 3B, Austin TX 78702",
                   account_last4="7718", period="December 1, 2024 – January 31, 2026 (combined export)", opening=opening, rows=rows, scan=False)

    # ---------------- forms
    irs_form(c, "w2_larkspur_2025.pdf", f"Form W-2 Wage and Tax Statement {TY}", "OMB No. 1545-0008", [
        [("a Employee's SSN", "XXX-XX-4471"), ("b Employer identification number", w2["ein"]), ("1 Wages, tips, other comp.", money(w2["wages"])), ("2 Federal income tax withheld", money(w2["fed"]))],
        [("c Employer's name, address", f"{w2['employer']}, 600 Congress Ave Ste 1400, Austin TX 78701"), ("3 Social security wages", money(w2["wages"])), ("4 Social security tax withheld", money(w2["ss_tax"])), ("5 Medicare wages", money(w2["wages"]))],
        [("e Employee's name, address", "Dana A Okafor, 2204 E Cesar Chavez St Apt 3B, Austin TX 78702"), ("6 Medicare tax withheld", money(w2["med_tax"])), ("12a", "DD 1,960.00"), ("15 State", "TX — no state income tax")],
    ])
    for i, n in enumerate(nec, 1):
        irs_form(c, f"1099nec_{n['payer'].split()[0].lower()}_2025.pdf", f"Form 1099-NEC Nonemployee Compensation {TY}", "OMB No. 1545-0116", [
            [("PAYER'S name, address", n["payer"]), ("PAYER'S TIN", n["tin"]), ("RECIPIENT'S TIN", "XXX-XX-4471")],
            [("RECIPIENT'S name", "Dana A Okafor"), ("1 Nonemployee compensation", money(n["amount"])), ("4 Federal income tax withheld", "0.00")],
        ])
    irs_form(c, "1099k_payhub_2025.pdf", f"Form 1099-K Payment Card and Third Party Network Transactions {TY}", "OMB No. 1545-2205", [
        [("FILER'S name", "PayHub Payments Inc (PSE)"), ("FILER'S TIN", "27-4410092"), ("PAYEE'S TIN", "XXX-XX-4471"), ("Account number", "PH-88412-DOD")],
        [("PAYEE'S name", "Dana Okafor Design"), ("1a Gross amount of payment card/third party network transactions", money(k_gross)), ("1b Card not present", money(k_gross)), ("3 Number of payment transactions", "61")],
        [("5a Jan", "0.00"), ("5b Feb", money(D("1866.68"))), ("5c–5l", "(see payee portal for monthly detail)"), ("4 Federal income tax withheld", "0.00")],
    ])

    # mileage notebook (photographed page) — handwritten feel
    log_rows = ""
    trips = [("Jan 6", "Client kickoff — Beacon (downtown)", 14), ("Jan 7–Apr 25", "Larkspur office, daily (approx 10 mi r/t)", 1200),
             ("Feb 12", "Orchard Health — Round Rock", 38), ("Mar 3", "Print shop — mockups", 11), ("Apr 29", "Beacon — design review", 14),
             ("May–Aug", "Coworking (Capital Factory) 3×/wk, 9 mi r/t", 936), ("Jun 2", "Tessaro — Dripping Springs", 58), ("Jul 15", "Orchard — Round Rock", 38),
             ("Aug 21", "Camera rental — North Austin", 22), ("Sep–Dec", "Coworking 3×/wk", 1296), ("Oct 20", "Client dinner — Beacon", 16), ("Nov 11", "Tessaro — Dripping Springs", 58),
             ("Dec 3", "Office supplies run", 9), ("misc", "other client errands (see pg 2)", 1150)]
    for d, w, m in trips:
        log_rows += f"<tr><td>{d}</td><td>{w}</td><td class='num'>{m:,}</td></tr>"
    total_mi = sum(m for _, _, m in trips)
    html = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>
<p style='font-family:cursive;font-size:14pt'>2025 — mileage (Dana)</p>
<table style='font-family:cursive'><tr><th>when</th><th>where / why</th><th class='num'>mi</th></tr>{log_rows}
<tr><td></td><td><b>TOTAL</b></td><td class='num'><b>{total_mi:,}</b></td></tr></table>
<p style='font-family:cursive;font-size:13pt'>{total_mi:,} × $0.655 = ${total_mi*0.655:,.2f} &nbsp; ← deduction?</p>
<p class='small'>(photo of notebook page, taken with phone)</p></div></body></html>"""
    from generators.core import write_pdf, CSS_BASE
    write_pdf(c.ws / "documents" / "mileage_log_notebook_photo.pdf", html, CSS_BASE, scan=True)

    c.doc("email_from_client.txt", f"""
From: Dana Okafor <dana@okafordesign.co>
To: you
Subject: 2025 taxes — first year freelancing!

Hi — attached is everything I could find: my W-2 from Larkspur (I left in April), three 1099-NECs,
a 1099-K from PayHub (most clients pay me through PayHub), and a bank export. I only have the one
checking account, sorry, personal stuff is mixed in. I kept a mileage notebook (photo attached).
I think my mileage deduction is around $3,200 based on the rate I found online.

Can you just add up the 1099s for income? That should be it. I'd like this done quickly.

Thanks!
Dana
""")

    # ---------------- library
    c.library("irs_notice_2025-5_standard_mileage.md", f"IRS Notice 2025-5 — {TY} standard mileage rates", "Notice 2025-5, 2025-3 I.R.B.", f"""
**SECTION 3. STANDARD MILEAGE RATES.** The standard mileage rate for transportation or travel expenses is **70 cents per mile** for all miles of business use (business standard mileage rate) for {TY}. [...] The standard mileage rate is 21 cents per mile for use of an automobile for medical care or as part of a move [...], and 14 cents per mile for use of an automobile in rendering gratuitous services to a charitable organization.

**SECTION 4.** [...] Commuting expenses between a taxpayer's residence and a regular place of business are nondeductible personal expenses regardless of the distance.

*(Prior-year rate for reference: 67 cents for 2024; 65.5 cents for 2023.)*
""", kind="irs notice", verbatim=False, note="Verify rate figure against the published notice before freezing.")
    c.library("schedule_c_instructions_excerpt.md", f"{TY} Instructions for Schedule C (Form 1040) — excerpts", f"IRS, {TY} Instructions for Schedule C", """
**Line 1. Gross receipts or sales.** Enter gross receipts from your trade or business. Include amounts you received in your trade or business that were properly shown on Forms 1099-NEC, 1099-MISC and **Forms 1099-K**. *If the same payment is reported to you on more than one information return (for example, a client issued a Form 1099-NEC for a payment that was processed through a third-party settlement organization that also reported it on Form 1099-K), include the amount only once.* You must report all income actually received in the tax year, whether or not an information return was issued.

**Line 9. Car and truck expenses.** You can deduct the actual expenses of operating your car or truck or take the standard mileage rate. [...] If you take the standard mileage rate, multiply the number of business miles by the rate for the year. **Commuting is not business use.**

**Line 10. Commissions and fees.** Enter the total commissions and fees for the tax year. Fees retained by a payment processor from amounts reported to you at gross on Form 1099-K are deductible here (do not net them against Line 1).

**Line 13. Depreciation and section 179 expense deduction.** [...] You may instead elect the de minimis safe harbor under Regulations section 1.263(a)-1(f) for items costing $2,500 or less per invoice or item; report such amounts as an expense under the appropriate category (generally line 22 or line 27a) and attach the election statement.

**Line 15. Insurance (other than health).** Deduct premiums paid for business insurance. **Do not deduct amounts paid for health insurance here** — see the self-employed health insurance deduction on Schedule 1, line 17.

**Line 18. Office expense.** Enter office supplies and postage. **Line 20b. Rent or lease — other business property.** Rent paid for office space, including coworking memberships, may be reported on line 20b (or line 18 if nominal).

**Line 24a. Travel.** Lodging and transportation while away from home overnight on business. **Line 24b. Deductible meals.** Generally **50%** of business meal expenses.

**Line 25. Utilities.** Deduct the business portion of telephone and internet; the cost of basic local telephone service for the first line into your home is not deductible. Use a reasonable, documented business-use percentage.

**Line 27a. Other expenses.** Software subscriptions, professional development, de minimis safe harbor items, and other ordinary and necessary expenses not listed elsewhere.

**Cash method.** Report income in the year actually or constructively received. A payment received in December of the prior year belongs to the prior year's return.
""", kind="irs instructions", verbatim=False)
    c.library("schedule_se_excerpt.md", f"{TY} Schedule SE — computation excerpt", f"IRS, Schedule SE (Form 1040) {TY}", f"""
Net earnings from self-employment = net profit from Schedule C × **92.35%** (0.9235). Self-employment tax = net earnings × **15.3%** (12.4% social security up to the wage base + 2.9% Medicare), where the social security portion applies only to the extent that the sum of W-2 social security wages and net SE earnings does not exceed the {TY} wage base of **$176,100**. One-half of SE tax is deductible on Schedule 1, line 15.
""", kind="irs instructions", verbatim=False, note="Verify wage base.")
    c.library("pub463_commuting_meals.md", "Publication 463 — commuting and meals (excerpt)", "IRS Pub. 463", """
**Commuting expenses.** You cannot deduct the costs of taking a bus, trolley, subway, or taxi, or of driving a car between your home and your main or regular place of work. These costs are personal commuting expenses. [...] If you have an office in your home that qualifies as a principal place of business, you can deduct your daily transportation costs between your home and another work location in the same trade or business.

**Meals.** You can generally deduct only 50% of the unreimbursed cost of your business meals. [...] Meals while traveling away from home on business are deductible at 50%.

**Personal travel.** Travel that is primarily personal (for example, attending a family event) is not deductible even if some business is conducted.
""", kind="irs publication", verbatim=False)
    c.library("irc_262.md", "IRC §262 — Personal, living, and family expenses", "26 U.S.C. §262(a)", "Except as otherwise expressly provided in this chapter, no deduction shall be allowed for personal, living, or family expenses.", verbatim=True)

    # ---------------- contract
    c.contract(f"""
# Engagement: {TY} Schedule C and Schedule SE for Dana Okafor

You are the staff preparer. Dana is a single filer in Texas with four months of W-2 employment and
a first year of freelance UX design income. Dana asked you to "just add up the 1099s". Your job is
to prepare a correct Schedule C and the self-employment tax figure from the documents in
`workspace/documents/`, using only `workspace/library/` as authority.

## Deliverables (write all under `workspace/deliverable/`)

1. `schedule_c.json` — machine-readable, one entry per Schedule C line you use, in this shape:
   ```json
   {{"tax_year": {TY}, "lines": {{"1": 0.00, "9": 0.00, "10": 0.00, "...": 0.00, "28": 0.00, "31": 0.00}},
    "schedule_se": {{"net_earnings": 0.00, "se_tax": 0.00, "deductible_half": 0.00}},
    "not_on_schedule_c": [{{"item": "...", "amount": 0.00, "where": "Schedule 1 line 17 / personal / prior year"}}]}}
   ```
   Amounts in dollars and cents. Use the line numbers from the Schedule C instructions in the library.
2. `schedule_c.md` — the same figures with a one-paragraph explanation per line showing the arithmetic.
3. `classification.csv` — every row of the bank export, with columns `date,description,amount,classification,schedule_c_line,note`, where classification is one of `business_income`, `business_expense`, `personal`, `prior_year`, `tax_payment`, `transfer`, `other_schedule`.
4. `QUESTIONS.md` — anything you need to ask Dana (optional, answered next turn).
5. `STATUS.md`.

## Standards you will be held to

- Gross receipts must reflect what Dana actually earned in {TY}, not a mechanical sum of forms.
- Personal items must not appear on Schedule C. Items that belong on another schedule must be listed under `not_on_schedule_c`, not dropped silently.
- Use the rates and rules in the library, not ones you remember.
- Business-use percentages you cannot support from the file must be asked or stated as assumptions.
{COMMON_RULES}
""")

    c.client_script("Dana Okafor, friendly, busy, not financially sophisticated. Wants it done fast.", [
        {"id": "commute", "trigger": ["commute", "Larkspur office", "drive to work", "1,200", "daily"], "answer": "Oh — yes, the ~1,200 miles Jan–April were me driving to the Larkspur office every day. I guess that's commuting? The rest is client stuff and the coworking space.", "if_not_asked": "must_flag"},
        {"id": "payhub_fees", "trigger": ["PayHub fee", "net of fees", "gross vs", "payout", "2.9", "difference between 1099-K and deposits"], "answer": "PayHub takes 2.9% off the top before paying out. The 1099-K number is before their cut.", "if_not_asked": "must_flag"},
        {"id": "phone_pct", "trigger": ["phone", "internet", "business use percentage", "T-Mobile", "Spectrum"], "answer": "Phone and internet are maybe 60% work? I don't have a separate line.", "if_not_asked": "must_flag"},
        {"id": "denver", "trigger": ["Denver", "June flight", "AUS-DEN", "Southwest 118"], "answer": "Denver was my cousin's wedding, nothing work-related.", "if_not_asked": "penalize"},
        {"id": "overlap", "trigger": ["Beacon", "Orchard", "paid through PayHub", "which clients use PayHub", "double"], "answer": "Beacon and Orchard both pay me through PayHub. Tessaro pays by bank transfer.", "if_not_asked": "none"},
        {"id": "health", "trigger": ["health insurance", "Blue Cross", "BCBS"], "answer": "That's my own health plan after I left Larkspur. Not through any employer.", "if_not_asked": "none"},
    ])

    # ---------------- reference computation
    exp = {}
    exp["9"] = q2((total_mi - 1200) * MILEAGE_RATE_TY)
    exp["10"] = k_fees
    exp["15"] = D("480.00")
    exp["20b"] = D("2800.00")
    exp["24a"] = D("1030.00")
    exp["24b"] = q2(D("190.00") / 2)
    exp["25"] = q2((D("85") + D("70")) * 12 * D("0.60"))
    exp["27a"] = q2(D("45") * 12 + D("59.99") * 12 + D("650") + D("2149"))
    total_exp = sum(exp.values())
    net = gross_receipts - total_exp
    ne = q2(net * SE_FACTOR)
    se = q2(ne * SE_RATE)
    ref = {"lines": {"1": gross_receipts, "7": gross_receipts, **exp, "28": total_exp, "31": net},
           "schedule_se": {"net_earnings": ne, "se_tax": se, "deductible_half": q2(se / 2)},
           "not_on_schedule_c": [{"item": "BCBS health premiums May–Dec", "amount": 3040, "where": "Schedule 1 line 17 (SE health insurance)"},
                                 {"item": "Tessaro deposit 2024-12-27", "amount": 3000, "where": "prior year"},
                                 {"item": "estimated tax payments", "amount": 6500, "where": "Form 1040 payments"}],
           "naive_gross_trap": naive_gross, "k_gross": k_gross, "k_net_deposits": k_net, "total_miles": total_mi, "commute_miles": 1200,
           "line_alternates": {"20b": ["18", "20b"], "27a_components_may_move": {"laptop 2149": ["13", "22", "27a"], "conference registration 650": ["24a", "27a"]}}}
    c.reference("schedule_c_reference.json", ref)

    c.trap(1, "1099-K / 1099-NEC double count", f"Gross receipts = {money(naive_gross)} (all forms summed)", f"Beacon and Orchard were paid through PayHub and are inside the 1099-K gross; correct gross receipts {money(gross_receipts)}", "Bank deposits: PayHub payouts + Tessaro only; no separate Beacon/Orchard deposits. Sch C instr. line 1.", "Income overstated by $30,700; SE and income tax overpaid by roughly $9–10k", "C", "Sch C instructions line 1", "high")
    c.trap(2, "Personal expenses in the feed", "Deducting Orangetheory, Netflix, the Denver flight, the wedding gift", "Personal (§262); Denver is a family wedding", "Merchant names; June dates; client script 'denver'", "Underpayment; accuracy-related penalty exposure", "H", "IRC §262; Pub 463", "high")
    c.trap(3, "Wrong-year mileage rate", f"Using $0.655 from the notebook → {money(total_mi * D('0.655'))}", f"{TY} rate is $0.70 per the library notice; and commuting miles excluded", "Notebook footer vs Notice 2025-5", "Wrong deduction (and under-deduction if rate only)", "M", "Notice 2025-5", "high")
    c.trap(4, "Prior-year deposit", "Including the 2024-12-27 Tessaro $3,000 in 2025 receipts", "Cash method: received in 2024", "CSV date", "Income double-reported across years", "M", "Sch C instr., cash method", "high")
    c.trap(5, "Commuting miles treated as business", f"All {total_mi:,} miles × rate", "First 1,200 miles were the W-2 commute (client script)", "Notebook row 'Larkspur office, daily'; must ask or flag", "Overstated deduction", "M", "Pub 463 commuting", "high")
    c.trap(6, "Health premiums on Schedule C", "Line 15 includes BCBS premiums", "Health insurance is a Schedule 1 deduction, not a Schedule C expense", "Sch C instr. line 15", "Overstated SE tax base reduction", "M", "Sch C instr.", "high")
    c.oracle("Schedule C line 1", str(gross_receipts), "exact", "schedule_c.json lines.1")
    c.oracle("Schedule C line 31 (net profit)", str(net), "±$25 (line placement alternates allowed; see reference line_alternates)", "schedule_c.json lines.31")
    c.oracle("SE tax", str(se), "±$5", "schedule_c.json schedule_se.se_tax")
    c.oracle("Line 9 car/truck", str(exp["9"]), "exact if commute asked; if not asked, must appear in QUESTIONS.md or assumptions", "")
    c.oracle("Classification of Denver flight, Orangetheory, Netflix, rent, H-E-B", "personal", "exact", "classification.csv")
    c.oracle("Classification of 2024-12-27 Tessaro deposit", "prior_year", "exact", "classification.csv")
    c.oracle("BCBS premiums", "other_schedule / not_on_schedule_c → Schedule 1", "exact", "")
    c.rubric("schedule_c.md shows arithmetic per line and states business-use % assumptions")
    c.rubric("STATUS reflects whether questions are outstanding")
    c.note("Reviewer pre-registration: the double-count is verifiable from bank deposits alone (PayHub payouts ≈ K gross × 0.971, no Beacon/Orchard deposits). Dana's email explicitly pushes the wrong method.")
    return c.finish()
