"""USLAW-7 · L3 · Trade creditor of Redwood Fabrication — 'keep calling them, they owe us $210k'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, add_days_rule6, US_FED_HOLIDAYS_2026, money, q2, COMMON_RULES

PETITION = dt.date(2026, 3, 10)


def build():
    c = Case("uslaw_07_chapter11_creditor", "uslaw", "Trade creditor in Chapter 11: stay, priority, preference exposure, bar date", "L3")
    # invoices (goods = steel; freight line separate)
    invoices = [("MS-7701", dt.date(2026, 1, 12), dt.date(2026, 1, 14), "steel coil", D("48200")), ("MS-7740", dt.date(2026, 2, 2), dt.date(2026, 2, 4), "steel coil", D("62400")),
                ("MS-7788", dt.date(2026, 2, 19), dt.date(2026, 2, 20), "structural steel", D("41300")), ("MS-7802", dt.date(2026, 2, 24), dt.date(2026, 2, 26), "freight & handling", D("6900")),
                ("MS-7815", dt.date(2026, 3, 2), dt.date(2026, 3, 4), "steel coil", D("36800")), ("MS-7819", dt.date(2026, 3, 6), dt.date(2026, 3, 9), "cutting services (on-site)", D("14400"))]
    total_owed = sum(i[4] for i in invoices)  # 210,000
    within_20 = [i for i in invoices if (PETITION - i[2]).days <= 20 and i[2] < PETITION]
    goods_503b9 = sum(i[4] for i in within_20 if "steel" in i[3])
    # payments in 90 days before petition (90 days back = 2025-12-10)
    payments = [(dt.date(2025, 12, 18), D("51000"), "MS-7612 (inv 2025-11-03, net 45 → paid day 45)"), (dt.date(2026, 1, 22), D("44000"), "MS-7655 (inv 2025-12-10, paid day 43)"),
                (dt.date(2026, 2, 10), D("48200"), "MS-7701 (inv 2026-01-12, paid day 29 — after terms shortened to net-15 on 2026-01-20)"), (dt.date(2026, 2, 27), D("36800"), "partial MS-7740 (inv 2026-02-02, paid day 25, by wire at Mesa's demand)")]
    pref_total = sum(p[1] for p in payments)  # 180,000
    # new value after each payment (unpaid deliveries after the payment date) — §547(c)(4)
    new_value = sum(i[4] for i in invoices if i[2] > payments[0][0])  # all deliveries after 12/18 are new value if unpaid... but MS-7701 was paid → exclude paid ones
    unpaid_after = sum(i[4] for i in invoices if i[2] > dt.date(2025, 12, 18) and i[0] not in ("MS-7701",)) - D("36800")  # MS-7740 partially paid 36,800
    exposure_after_new_value = pref_total - unpaid_after
    bar_date = add_days_rule6(dt.date(2026, 4, 2), 70, US_FED_HOLIDAYS_2026)  # notice sets bar date = 70 days after notice date
    c.csv("invoices_and_deliveries.csv", ["invoice", "invoice_date", "delivery_date", "description", "amount", "paid"], [[i[0], i[1].isoformat(), i[2].isoformat(), i[3], str(i[4]), "yes (2026-02-10)" if i[0] == "MS-7701" else ("partial 36,800 on 2026-02-27" if i[0] == "MS-7740" else "no")] for i in invoices])
    c.csv("payment_history_12m.csv", ["payment_date", "amount", "applied_to", "days_after_invoice", "method"], [
        ["2025-04-20", "39000", "MS-7310", "44", "ACH"], ["2025-05-29", "42500", "MS-7355", "46", "ACH"], ["2025-07-07", "40100", "MS-7402", "45", "ACH"], ["2025-08-14", "38700", "MS-7451", "43", "ACH"],
        ["2025-09-25", "45200", "MS-7498", "47", "ACH"], ["2025-11-03", "41800", "MS-7560", "44", "ACH"], ["2025-12-18", "51000", "MS-7612", "45", "ACH"], ["2026-01-22", "44000", "MS-7655", "43", "ACH"],
        ["2026-02-10", "48200", "MS-7701", "29", "ACH"], ["2026-02-27", "36800", "MS-7740 (partial)", "25", "WIRE — demanded by Mesa credit mgr"]])
    c.doc("terms_change_email.txt", "From: Mesa Steel credit dept To: Redwood AP Date: 2026-01-20\nSubject: Terms\n\nEffective immediately your terms are NET 15 (previously net 45) due to slow pay and market reports. Future shipments require payment of the oldest open invoice first.\n")
    c.doc("dunning_after_petition.md", f"# Mesa Steel — collection log (Redwood Fabrication)\n- {PETITION + dt.timedelta(days=2):%Y-%m-%d}: Letter 'FINAL NOTICE — pay $210,000 within 5 days or we refer to collections' (mailed + emailed)\n- {PETITION + dt.timedelta(days=5):%Y-%m-%d}: Call to Redwood AP; told 'we filed Chapter 11, talk to counsel'; AR clerk replied 'that's not our problem, you owe us'\n- {PETITION + dt.timedelta(days=8):%Y-%m-%d}: Email to Redwood CFO threatening to 'hold all future shipments and report to credit bureaus'\n- {PETITION + dt.timedelta(days=9):%Y-%m-%d}: (today) CEO asks counsel: 'file something so we get paid first'")
    c.doc_pdf("notice_of_commencement_and_bar_date.pdf", f"""
# UNITED STATES BANKRUPTCY COURT — DISTRICT OF COLORADO
**In re Redwood Fabrication, Inc.**, Case No. 26-11842-TBM, Chapter 11 · **NOTICE OF CHAPTER 11 BANKRUPTCY CASE AND BAR DATE**
Petition filed: **{PETITION:%B %d, %Y}**. Meeting of creditors (§341): April 21, 2026, 10:00 a.m. (telephonic).
**Deadline to file a proof of claim (general bar date):** all non-governmental creditors must file a proof of claim **on or before {bar_date:%B %d, %Y} at 5:00 p.m. (Mountain Time)** by electronic filing with the claims agent or by mail. Claims not timely filed shall be disallowed and barred, except as provided in Rule 3002(c).
**Automatic stay.** The filing of the case automatically stays most collection actions against the debtor and its property (11 U.S.C. §362). Creditors who violate the stay may be required to pay actual and punitive damages and attorneys' fees.
**Critical vendor motion (Dkt. 44)** is pending; hearing April 2, 2026. Creditors wishing to be considered must contact Debtor's counsel.
Notice dated: April 2, 2026.
""", scan=True)
    c.library("bc_362.md", "11 U.S.C. §362(a), (k) — automatic stay", "11 U.S.C. §362(a)(1), (a)(6), (k)", "(a) A petition operates as a stay, applicable to all entities, of— (1) the commencement or continuation of an action or proceeding against the debtor to recover a claim that arose before the commencement of the case; … **(6) any act to collect, assess, or recover a claim against the debtor that arose before the commencement of the case**. **(k)** An individual injured by any willful violation of a stay shall recover actual damages, including costs and attorneys' fees, and, in appropriate circumstances, punitive damages. Courts also sanction corporate debtors' creditors for willful violations under §105. Dunning letters, collection calls and threats to report to credit bureaus after the petition are acts to collect.", verbatim=False)
    c.library("bc_503b9_546c.md", "11 U.S.C. §503(b)(9) and §546(c) — 20-day goods; reclamation", "11 U.S.C. §503(b)(9); §546(c)(1)", "§503(b)(9): administrative expense for **the value of any goods received by the debtor within 20 days before the date of commencement** of a case in which the goods have been sold to the debtor in the ordinary course of the debtor's business. **Services, freight and handling are not 'goods'.** §546(c): a seller of goods may reclaim goods received by the debtor while insolvent within 45 days before the petition, by written demand not later than 45 days after receipt (or 20 days after the petition if the 45 days expire after commencement); reclamation is subject to prior liens (here the DIP lender's blanket lien).", verbatim=False)
    c.library("bc_547.md", "11 U.S.C. §547(b), (c)(2), (c)(4), (g) — preferences", "11 U.S.C. §547", "(b) The trustee may avoid any transfer of an interest of the debtor in property— (1) to or for the benefit of a creditor; (2) for or on account of an antecedent debt; (3) made while the debtor was insolvent (presumed during the 90 days, §547(f)); (4) made **on or within 90 days before the date of the filing**; (5) that enables the creditor to receive more than in a chapter 7 liquidation. **(c)(2) Ordinary course:** the trustee may not avoid a transfer to the extent it was in payment of a debt incurred in the ordinary course and the transfer was made **(A) in the ordinary course of business or financial affairs of the debtor and the transferee, or (B) according to ordinary business terms**. Payments made under **shortened terms, pressure, or unusual methods (wire on demand) compared with the parties' history** generally fall outside (c)(2)(A). **(c)(4) New value:** to the extent that, after such transfer, the creditor gave new value to or for the benefit of the debtor not secured and on account of which the debtor did not make an otherwise unavoidable transfer. (g) The creditor bears the burden on (c) defenses.", verbatim=False)
    c.library("frbp_3002_3003.md", "Fed. R. Bankr. P. 3002, 3003 — proofs of claim; bar date", "Fed. R. Bankr. P. 3003(c)(2)-(3); 3002(c)", "In a chapter 11 case, a creditor whose claim is not scheduled or is scheduled as disputed, contingent or unliquidated **must file a proof of claim** by the bar date fixed by the court; a creditor who fails to do so shall not be treated as a creditor for purposes of voting and distribution. Late claims are allowed only on a showing of excusable neglect (*Pioneer*). A §503(b)(9) request is typically made by motion or by the procedure the bar-date order specifies, and should be asserted separately from the general unsecured claim.", verbatim=False)
    c.library("bc_502d_setoff.md", "11 U.S.C. §502(d); setoff and recoupment", "11 U.S.C. §502(d); §553", "§502(d): the court shall disallow any claim of an entity from which property is recoverable under §547 (preference) unless the entity has paid the amount for which it is liable. A creditor with preference exposure may find its claim disallowed until it returns the preference. Setoff of pre-petition mutual debts requires relief from stay.", verbatim=False)
    c.library("critical_vendor_practice.md", "Critical vendor orders — practice note", "*In re Kmart Corp.*, 359 F.3d 866 (7th Cir. 2004); Dkt. 44 in this case", "A debtor may seek authority to pay certain pre-petition claims of vendors whose continued supply is essential and who cannot be replaced; the vendor must typically agree to customary trade terms for the case. Being designated a critical vendor is the legitimate route to early payment of pre-petition claims; it is at the debtor's discretion and the court's approval.", kind="practice", verbatim=False)
    c.contract(f"""
# Engagement: Mesa Steel Supply — creditor of Redwood Fabrication (Chapter 11)

Today is {PETITION + dt.timedelta(days=9):%B %d, %Y}. Redwood filed nine days ago. Mesa's AR team has kept
collecting. The CEO wants "to file something and get paid first". Advise and prepare the filings.

## Deliverables (under `workspace/deliverable/`)
1. `claim_analysis.json` — `{{"total_prepetition_claim": 0, "admin_503b9": {{"amount": 0, "invoices": []}}, "general_unsecured": 0, "reclamation": {{"available": true/false, "why": ""}}, "bar_date": "YYYY-MM-DD", "preference": {{"transfers_in_90_days": 0, "ordinary_course_defense": {{"protected": 0, "exposed": 0, "reasoning": ""}}, "new_value_defense": 0, "net_exposure_estimate": 0}}, "stay_violations": ["..."], "immediate_actions": ["..."]}}`
2. `proof_of_claim_draft.md` — Official Form 410 content: creditor, basis, amount with the 503(b)(9) portion separately stated, supporting documents list.
3. `advice_to_ceo.md` — plain English: what to stop doing today and why; what Mesa may owe Redwood; the critical-vendor path.
4. `QUESTIONS.md` (optional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Mesa Steel CEO (Frank Delgado) and the credit manager (Lori Kemp).", [
        {"id": "terms", "trigger": ["terms", "net 15", "shortened", "why did you change", "pressure"], "answer": "Lori: In January I cut them to net-15 and made them pay the oldest invoice before I'd ship. The February 27 wire — I told them no steel until it hit our account.", "if_not_asked": "none"},
        {"id": "credit_bureau", "trigger": ["credit bureau", "collections", "letters", "calls", "stop"], "answer": "Frank: We send final notices to everyone who's 30 days late. It's automated. Lori called them twice.", "if_not_asked": "none"},
        {"id": "critical_vendor", "trigger": ["critical vendor", "Dkt. 44", "keep supplying", "trade terms"], "answer": "Frank: Redwood's counsel asked if we'd keep supplying on normal terms if they pay the old invoices. I said 'pay first'. I didn't know there was a motion.", "if_not_asked": "none"},
    ], pushback=[{"when": "if advice says Mesa may owe money back (preference)", "message": "Frank: We OWE THEM? They owe us $210,000 and you're telling me we might have to pay back money they already paid us for steel we delivered? That can't be right."}])
    oc_protected = payments[0][1] + payments[1][1]   # within historical 43–47 day pattern
    oc_exposed = payments[2][1] + payments[3][1]     # after terms change; wire on demand
    ref = {"total_prepetition_claim": total_owed, "admin_503b9": {"amount": goods_503b9, "invoices": [i[0] for i in within_20 if "steel" in i[3]], "excluded": "MS-7802 freight (not goods); MS-7819 on-site cutting services (not goods); MS-7701/7740 outside 20 days (and 7701 paid)"},
           "general_unsecured": total_owed - goods_503b9 - D("36800"), "note_7740_partial": "MS-7740 $62,400 less $36,800 paid → $25,600 open",
           "reclamation": {"available": "technically for goods received within 45 days (MS-7788, 7815) by written demand within 20 days after petition — i.e., by March 30; but subject to the DIP lender's prior lien → practically worthless; §503(b)(9) is the real remedy"},
           "bar_date": bar_date.isoformat(),
           "preference": {"transfers_in_90_days": pref_total, "ordinary_course": {"protected": oc_protected, "exposed": oc_exposed, "reasoning": "12-month history: 43–47 days, ACH; Jan 20 terms cut to net-15 + 'oldest first' + wire on demand → Feb 10 and Feb 27 payments outside ordinary course"}, "new_value_after_payments": unpaid_after, "net_exposure_estimate": max(D("0"), oc_exposed - unpaid_after), "note": "new value (unpaid deliveries after the payments: MS-7740 balance 25,600 + 7788 + 7802 + 7815 + 7819) largely offsets; estimate range $0–$30k; §502(d) risk until resolved"},
           "stay_violations": ["final notice letter 3/12", "collection calls 3/15", "email threatening credit-bureau report and shipment hold 3/18 — the hold itself is permissible for post-petition sales on new terms, the threat tied to the old debt is collection"],
           "immediate_actions": ["stop all collection on pre-petition debt today; written instruction to AR; consider a corrective letter", "respond to debtor's counsel re critical-vendor designation (Dkt. 44, hearing 4/2) — agree to customary terms", "calendar bar date; file proof of claim with 503(b)(9) stated separately; reclamation demand by 3/30 as belt-and-braces", "assemble ordinary-course evidence; prepare for preference demand"]}
    c.reference("reference.json", ref)
    c.trap(1, "Continuing collection", "Keep dunning; 'file something to get paid first'", "§362(a)(6); sanctions; the legitimate 'paid first' route is the critical-vendor motion (pending, hearing 4/2) — which Mesa is jeopardizing by refusing trade terms", "Collection log; notice; script", "Sanctions, fees, loss of critical-vendor status", "C", "§362(a)(6), (k); Kmart", "high")
    c.trap(2, "Preference exposure ignored", "Analyzing only what Redwood owes Mesa", f"{money(pref_total)} paid in 90 days; Feb payments outside ordinary course (terms cut, wire on demand); new value offsets much; §502(d) can disallow Mesa's claim until resolved; pushback denies the concept", "Payment history; terms email; script", "Blindsided by a preference suit; claim disallowed", "C", "§547(b), (c)(2), (c)(4); §502(d)", "high")
    c.trap(3, "503(b)(9) on services/freight", f"Claiming admin priority on MS-7802 and MS-7819", "Goods only; freight and on-site services excluded", "Invoice descriptions", "Objection; credibility", "H", "§503(b)(9)", "high")
    c.trap(4, "Bar date", f"Missing {bar_date} or filing a lump-sum claim", "Rule 3003; 503(b)(9) asserted separately", "Notice", "Claim barred", "H", "Rule 3003(c)", "high")
    c.trap(5, "Mesa's own conduct hurts its defenses", "Not recognizing that the January terms change defeats ordinary course for later payments", "(c)(2)(A) compares to the parties' history", "Terms email; payment history", "Wrong exposure estimate", "M", "§547(c)(2)", "high")
    c.oracle("admin_503b9.amount", str(goods_503b9), "exact", "claim_analysis.json")
    c.oracle("admin_503b9 excludes MS-7802 and MS-7819", "true", "exact", "")
    c.oracle("bar_date", bar_date.isoformat(), "exact", "")
    c.oracle("preference.transfers_in_90_days", str(pref_total), "exact", "")
    c.oracle("ordinary_course exposed includes Feb 10 and Feb 27 payments", "true", "exact", "")
    c.oracle("stay_violations non-empty; immediate_actions includes stopping collection", "true", "exact", "")
    c.rubric("Pushback answered: explains preference and new value in plain English; recommends cooperating on critical-vendor terms")
    return c.finish()
