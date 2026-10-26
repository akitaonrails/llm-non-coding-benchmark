#!/usr/bin/env python3
"""March 2026 close calculations - Brightline Cabinetry LLC."""
import csv
from collections import defaultdict

BASE = "/work/workspace/documents/"

# ---------- Feb trial balance (opening balances, cumulative YTD) ----------
feb = defaultdict(float)
with open(BASE + "trial_balance_2026-02-28.csv") as f:
    for row in csv.DictReader(f):
        d = float(row["debit"] or 0)
        c = float(row["credit"] or 0)
        feb[row["account"]] += d - c  # positive = debit balance

fd = sum(v for v in feb.values() if v > 0)
fc = -sum(v for v in feb.values() if v < 0)
print("FEB TB  debits %10.2f  credits %10.2f  balanced: %s" % (fd, fc, abs(fd - fc) < 1e-9))

# ---------- March GL movements (rows dated 2026-03 only; 2026-02-26 rows are
# context for the duplicate-bill issue and are already inside the Feb TB) ----------
gl = defaultdict(float)
names = {}
with open(BASE + "general_ledger_2026-03.csv") as f:
    for row in csv.DictReader(f):
        names[row["account"]] = row["name"]
        if row["date"] < "2026-03":
            continue
        d = float(row["debit"] or 0)
        c = float(row["credit"] or 0)
        gl[row["account"]] += d - c

gd = sum(v for v in gl.values() if v > 0)
gc = -sum(v for v in gl.values() if v < 0)
print("MAR GL  debits %10.2f  credits %10.2f  balanced: %s" % (gd, gc, abs(gd - gc) < 1e-9))

# ---------- Adjusting entries ----------
AJES = {
    "AJE-1": [("2000", 4860.00, 0.0), ("5000", 0.0, 4860.00)],
    "AJE-2": [("4000", 1500.00, 0.0), ("2100", 0.0, 1500.00)],
    "AJE-3": [("1000", 4312.00, 0.0), ("2100", 0.0, 4312.00)],
    "AJE-4": [("6700", 35.00, 0.0), ("1000", 0.0, 35.00)],
    "AJE-5": [("1300", 1188.00, 0.0), ("6400", 0.0, 1188.00)],
}
for lines in AJES.values():
    for acct, d, c in lines:
        gl[acct] += d - c

# ---------- Closed trial balance ----------
tb = {a: feb.get(a, 0.0) + gl.get(a, 0.0) for a in set(list(feb) + list(gl))}
print("\nCLOSED TRIAL BALANCE 2026-03-31 (YTD)")
tdr = tcr = 0.0
for a in sorted(tb):
    d = tb[a] if tb[a] > 0 else 0.0
    c = -tb[a] if tb[a] < 0 else 0.0
    tdr += d
    tcr += c
    print("  %s %-38s %12.2f %12.2f" % (a, names.get(a, ""), d, c))
print("  %-41s %12.2f %12.2f   DIFF %.2f" % ("TOTAL", tdr, tcr, tdr - tcr))

# ---------- Bank reconciliation ----------
print("\nBANK RECONCILIATION")
stmt = 7625.50
dit = 6250.00                # Delgado check #4471 deposited 3/31, not on statement
ochk = 612.40 + 2944.80      # #2041 Austin Energy, #2044 Blum
adj_bank = stmt + dit - ochk
print("  stmt %.2f + DIT %.2f - outck %.2f = %.2f" % (stmt, dit, ochk, adj_bank))
gl_cash_before = feb["1000"] + gl["1000"]
# gl already includes AJE-3/AJE-4 cash lines above
mobil = 4312.00
svc = 35.00
adj_book = gl_cash_before + mobil - svc
print("  GL cash before AJEs %.2f + unrecorded deposit %.2f - fee %.2f = %.2f"
      % (gl_cash_before, mobil, svc, adj_book))
print("  difference: %.2f" % (adj_bank - adj_book))

# cash after AJEs should equal adjusted book balance
print("  GL cash after AJEs: %.2f" % tb["1000"])

# ---------- A/R tie ----------
print("\nA/R CHECK")
ar_open = feb["1100"]
inv = 18400 + 6250 + 3900 + 22750 + 7120
rec = 9200 + 14350 + 11800 + 9200 + 6250
print("  GL 1100 at 3/31 = %.2f + %.2f - %.2f = %.2f" % (ar_open, inv, rec, ar_open + inv - rec))
print("  aging total = 56,100.00 ; net of footnote-1 receipt (6,250 already in GL) = 49,850.00")
print("  GL 1100 - aging (as printed) = %.2f" % (115288.00 - 56100.00))
print("  GL 1100 - aging (net of footnote) = %.2f" % (115288.00 - 49850.00))
