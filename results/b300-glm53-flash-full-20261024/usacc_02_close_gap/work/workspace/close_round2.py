#!/usr/bin/env python3
"""Round 2: owner answered QUESTIONS.md. Applies AJE-1..AJE-8 (round 2 adds
AJE-6 owner-confirmed contribution reclass, AJE-7 Uchi dining reclass to draws,
AJE-8 Allied Q2 prepaid), regenerates adjusting_entries.json and
trial_balance_2026-03-31.json, and re-verifies every tie."""
import csv, json
from collections import defaultdict

BASE = "/work/workspace/documents/"
OUT = "/work/workspace/deliverable/"

feb = defaultdict(float); names = {}
with open(BASE + "trial_balance_2026-02-28.csv") as f:
    for row in csv.DictReader(f):
        names[row["account"]] = row["name"]
        feb[row["account"]] += float(row["debit"] or 0) - float(row["credit"] or 0)

gl = defaultdict(float)
with open(BASE + "general_ledger_2026-03.csv") as f:
    for row in csv.DictReader(f):
        names[row["account"]] = row["name"]
        if row["date"] < "2026-03":
            continue
        gl[row["account"]] += float(row["debit"] or 0) - float(row["credit"] or 0)

AJES = [
    {"ref": "AJE-1", "date": "2026-03-31",
     "memo": "Reverse duplicate posting of Cascade Hardwoods invoice CH-7731. Same invoice (dated 02/24/2026, total 4,860.00) posted twice: 2026-02-26 from the emailed copy and again 2026-03-09 from the mailed copy. Removed the March duplicate; the invoice remains recorded once (Feb posting) and was paid in full by check #2040 (cleared 03/22). Per policy, vendor bills are recorded once, keyed by vendor invoice number.",
     "lines": [{"account": "2000", "debit": 4860.00, "credit": 0.00},
               {"account": "5000", "debit": 0.00, "credit": 4860.00}]},
    {"ref": "AJE-2", "date": "2026-03-31",
     "memo": "Reclassify online transfer in of 1,500.00 from checking *4420 (03/14, bank statement line) out of Sales 4000, where it was posted in error. The source of the funds cannot be identified from any document in the file; per policy, unidentified receipts are recorded to 2100 suspense until matched. Completed by AJE-6 when the owner confirmed the funds are his.",
     "lines": [{"account": "4000", "debit": 1500.00, "credit": 0.00},
               {"account": "2100", "debit": 0.00, "credit": 1500.00}]},
    {"ref": "AJE-3", "date": "2026-03-31",
     "memo": "Record mobile deposit of 4,312.00 received 03/21 per bank statement; not recorded in the books. Payor unidentified from the documents; recorded to 2100 suspense per policy until matched to an invoice or customer. Not revenue. Owner and office manager could not identify the payor either (owner replies on file); remains in suspense.",
     "lines": [{"account": "1000", "debit": 4312.00, "credit": 0.00},
               {"account": "2100", "debit": 0.00, "credit": 4312.00}]},
    {"ref": "AJE-4", "date": "2026-03-31",
     "memo": "Record HCCB monthly service fee 35.00 charged 03/31/2026 per bank statement; not recorded in the books.",
     "lines": [{"account": "6700", "debit": 35.00, "credit": 0.00},
               {"account": "1000", "debit": 0.00, "credit": 35.00}]},
    {"ref": "AJE-5", "date": "2026-03-31",
     "memo": "Capitalize CabinetVision annual license 1,188.00 charged to the Summit card 03/11 and posted to Software & subscriptions. Card statement states coverage 04/2026-03/2027, so nothing is consumed at 03/31; per policy amounts covering more than one month are prepaid to 1300. Amortization 99.00/month begins April 2026.",
     "lines": [{"account": "1300", "debit": 1188.00, "credit": 0.00},
               {"account": "6400", "debit": 0.00, "credit": 1188.00}]},
    {"ref": "AJE-6", "date": "2026-03-31",
     "memo": "Owner confirmed the 1,500.00 transfer in from checking *4420 (03/14, bank statement line) is his own personal money moved into the business to fund payroll ('It's my money, not a sale'). Per close_policy.md owner personal funds through business accounts go to 3100 Owner's contributions, never revenue. Completes the reclassification started by AJE-2: 2100 suspense to 3100.",
     "lines": [{"account": "2100", "debit": 1500.00, "credit": 0.00},
               {"account": "3100", "debit": 0.00, "credit": 1500.00}]},
    {"ref": "AJE-7", "date": "2026-03-31",
     "memo": "Owner confirmed the Uchi dinner 212.00 (03/15, Summit card ending 0917, 4 guests) was his personal anniversary dinner charged to the wrong card. Per close_policy.md owner personal charges through business accounts are recorded to 3200 Owner's draws. Reclass from 6500 Meals. Card liability (2050) unchanged.",
     "lines": [{"account": "3200", "debit": 212.00, "credit": 0.00},
               {"account": "6500", "debit": 0.00, "credit": 212.00}]},
    {"ref": "AJE-8", "date": "2026-03-31",
     "memo": "Allied Insurance 1,150.00 keyed to A/P 03/20; the bill itself is not in the file. The only coverage wording anywhere in the file is the GL memo 'Allied Insurance — Q2 GL' (documents/general_ledger_2026-03.csv). We read 'GL' as general-liability coverage for Q2 2026 (the quarter runs 04/01-06/30) - our reading, to be confirmed against the policy declarations page. On any quarterly reading nothing is consumed at 03/31; per close_policy.md amounts covering more than one month are capitalized to 1300 prepaid. Treatment consistent with the CabinetVision license (AJE-5), whose coverage period is printed on its source document. Amortization 383.33/month from April 2026, pending the declarations page to confirm coverage type and exact dates. Liability (2000) unchanged; bill remains unpaid.",
     "lines": [{"account": "1300", "debit": 1150.00, "credit": 0.00},
               {"account": "6300", "debit": 0.00, "credit": 1150.00}]},
]
ajl = defaultdict(float)
for a in AJES:
    for l in a["lines"]:
        ajl[l["account"]] += l["debit"] - l["credit"]

# --- verification ---
cash_pre = feb["1000"] + gl["1000"]
assert round(cash_pre, 2) == 6041.30, cash_pre
adj_book = cash_pre + 4312.00 - 35.00
adj_bank = 7625.50 + 6250.00 - (612.40 + 2944.80)
assert round(adj_book, 2) == round(adj_bank, 2) == 10318.30

tb = {a: feb.get(a, 0.0) + gl.get(a, 0.0) + ajl.get(a, 0.0) for a in set(list(feb) + list(gl) + list(ajl))}
for a in ("3100", "3200"):
    tb.setdefault(a, 0.0)
accounts = {}
for a in sorted(tb):
    v = tb[a]
    accounts[a] = {"debit": round(v, 2) if v > 0 else 0.00, "credit": round(-v, 2) if v < 0 else 0.00}
accounts = dict(sorted(accounts.items()))
td = round(sum(v["debit"] for v in accounts.values()), 2)
tc = round(sum(v["credit"] for v in accounts.values()), 2)

checks = [
    ("TB debits", td, 424932.07), ("TB credits", tc, 424932.07), ("TB ties", td - tc, 0.0),
    ("cash 1000", accounts["1000"]["debit"], 10318.30),
    ("A/R 1100", accounts["1100"]["debit"], 115288.00),
    ("A/P 2000 credit", accounts["2000"]["credit"], 29505.40),
    ("card 2050 credit", accounts["2050"]["credit"], 2306.12),
    ("suspense 2100 credit", accounts["2100"]["credit"], 4312.00),
    ("contrib 3100 credit", accounts["3100"]["credit"], 1500.00),
    ("draws 3200 debit", accounts["3200"]["debit"], 212.00),
    ("prepaid 1300 debit", accounts["1300"]["debit"], 4738.00),
    ("insurance 6300 debit", accounts["6300"]["debit"], 1150.00),
    ("meals 6500 both 0", accounts["6500"]["debit"] + accounts["6500"]["credit"], 0.00),
    ("LOC 2200 credit", accounts["2200"]["credit"], 45000.00),
    ("sales tax 2300 credit", accounts["2300"]["credit"], 4121.55),
    ("revenue 4000 credit", accounts["4000"]["credit"], 138720.00),
    ("install 4100 credit", accounts["4100"]["credit"], 16200.00),
]
# implied net income for memo note
rev = accounts["4000"]["credit"] + accounts["4100"]["credit"]
exp = sum(accounts[a]["debit"] for a in ("5000","5100","6000","6050","6100","6200","6300","6400","6500","6600","6700","6800","6900"))
ni = round(rev - exp, 2)
print("Implied YTD net income after round-2 AJEs: %.2f (revenue %.2f - expenses %.2f)" % (ni, rev, exp))
ok = all(abs(g - w) < 1e-9 for _, g, w in checks)
for n, g, w in checks:
    print(("PASS" if abs(g - w) < 1e-9 else "FAIL"), n, "->", g, "expected", w)

with open(OUT + "adjusting_entries.json", "w") as f:
    json.dump(AJES, f, indent=2)
with open(OUT + "trial_balance_2026-03-31.json", "w") as f:
    json.dump({"accounts": accounts}, f, indent=2)
print("\nBank rec unchanged: adjusted bank %.2f = adjusted book %.2f" % (adj_bank, adj_book))
print("Wrote adjusting_entries.json (8 AJEs) and trial_balance_2026-03-31.json")
assert ok
