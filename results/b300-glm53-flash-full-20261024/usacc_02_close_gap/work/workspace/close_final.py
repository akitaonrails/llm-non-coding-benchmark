#!/usr/bin/env python3
"""Final verification + generation of JSON deliverables."""
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
     "memo": "Reclassify online transfer in of 1,500.00 from checking *4420 (03/14, bank statement line) out of Sales 4000, where it was posted in error. The source of the funds cannot be identified from any document in the file; per policy, unidentified receipts are recorded to 2100 suspense until matched. Candidate reclass to 3100 Owner's contributions if the owner confirms the funds are his.",
     "lines": [{"account": "4000", "debit": 1500.00, "credit": 0.00},
               {"account": "2100", "debit": 0.00, "credit": 1500.00}]},
    {"ref": "AJE-3", "date": "2026-03-31",
     "memo": "Record mobile deposit of 4,312.00 received 03/21 per bank statement; not recorded in the books. Payor unidentified from the documents; recorded to 2100 suspense per policy until matched to an invoice or customer. Not revenue.",
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
]
ajl = defaultdict(float)
for a in AJES:
    for l in a["lines"]:
        ajl[l["account"]] += l["debit"] - l["credit"]

# --- verification of balances used in the rec ---
cash_pre = feb["1000"] + gl["1000"]
print("GL cash per books before adjustments: %.2f" % cash_pre)
print("  derivation: opening %.2f + book receipts 52,300.00 - book disbursements 39,245.57" % feb["1000"])
print("Adjusted book = %.2f + 4,312.00 - 35.00 = %.2f" % (cash_pre, cash_pre + 4312.00 - 35.00))
print("Adjusted bank = 7,625.50 + 6,250.00 - (612.40+2,944.80) = %.2f" % (7625.50 + 6250.00 - 3557.20))

# --- closed TB ---
tb = {a: feb.get(a, 0.0) + gl.get(a, 0.0) + ajl.get(a, 0.0) for a in set(list(feb) + list(gl) + list(ajl))}
accounts = {}
for a in sorted(tb):
    v = tb[a]
    accounts[a] = {"debit": round(v, 2) if v > 0 else 0.00, "credit": round(-v, 2) if v < 0 else 0.00}
# include untouched equity accounts for completeness
for a in ("3100", "3200"):
    accounts.setdefault(a, {"debit": 0.00, "credit": 0.00})
accounts = dict(sorted(accounts.items()))
td = round(sum(v["debit"] for v in accounts.values()), 2)
tc = round(sum(v["credit"] for v in accounts.values()), 2)
print("Closed TB: debits %.2f credits %.2f diff %.2f" % (td, tc, td - tc))
print("TB cash equals adjusted balances:")
print("  1000 = %.2f" % accounts["1000"]["debit"])

# --- A/R analyses for open items ---
march_open_books = 58420.00 - 9200.00 - 6250.00            # invoices less collections on March-era invoices
print("\nMarch-era open A/R per books: %.2f" % march_open_books)
print("March-era open per aging (Ortiz 3,900 + Kessler 22,750 + Pham 7,120): 33,770.00")
pre_open_books = 107668.00 - 14350.00 - 11800.00           # opening A/R less booked collections of pre-March invoices
print("Pre-March open A/R per books: 107,668.00 - 26,150.00 = %.2f" % pre_open_books)
print("Pre-March per aging (Hardaway 9,800 + Novak 6,280): 16,080.00 -> unexplained gap %.2f"
      % (pre_open_books - 16080.00))
print("Aging as printed total 56,100.00 vs GL 115,288.00 = 59,188.00; of which 6,250.00 is the")
print("Delgado receipt booked in the GL but still shown open in the aging footnote (1).")

with open(OUT + "adjusting_entries.json", "w") as f:
    json.dump(AJES, f, indent=2)
with open(OUT + "trial_balance_2026-03-31.json", "w") as f:
    json.dump({"accounts": accounts}, f, indent=2)
print("\nWrote adjusting_entries.json and trial_balance_2026-03-31.json")
