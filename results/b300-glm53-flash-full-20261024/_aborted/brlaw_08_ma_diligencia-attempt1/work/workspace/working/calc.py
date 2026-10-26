rev = 4_200_000
merid = 390_000_000
# Revenue shares
hz = rev*0.31
sor = rev*0.12
print(f"Horizonte Azul 31% x 4.2mi = {hz:,.2f}")
print(f"Sorocaba 12% x 4.2mi      = {sor:,.2f}")
print(f"Combine                   = {hz+sor:,.2f}")
# Labor gap
gap = 1_400_000 - 380_000
print(f"Labor gap = 1.4mi - 0.38mi = {gap:,}; share of revenue = {gap/rev:.4f}")
# Earn-out cap threshold
excess_cap = 1_500_000/0.35
print(f"Cap threshold = 1.5M/0.35 = {excess_cap:,.2f}; EBITDA to hit cap = {excess_cap+1_100_000:,.2f}")
print(f"EBITDA margin needed vs revenue 4.2mi = {(excess_cap+1_100_000)/rev:.2%}")
for rateio in (100_000,200_000):
    print(f"rateio {rateio:,} -> earn-out loss = {0.35*rateio:,.2f}")
# Fine formula, cap, escrow (price unknown -> symbol)
print("Multa HA = 0.20 x S (saldo contratual, unknowable)")
print("Cap geral 8.4(b) = 0.15 x P; carve-out 5.7/5.9 = P; escrow 10.2 = 0.20 x P")

# ---- 25/10 client-answers arithmetic ----
# IRPJ 2023 contested, parcelamento refused: route locked = qualification + specific
# indemnity (cap R$ 310k + encargos) + dedicated escrow released per dispute outcome.
print("IRPJ 2023 (contested): cap base = R$ 310,000 + encargos (unknown); dedicated escrow")

# PJ specific-cap interim anchor: known claims of the 3 reclamatórias (R$ 1.4M)
mean_claim = 1_400_000 / 3
print(f"Mean known claim = 1,400,000 / 3 = {mean_claim:,.2f}")
mech = 11 * mean_claim
print(f"Mechanical extrapolation 11 x mean = {mech:,.2f}")
print(f"Mechanical extrapolation vs revenue = {mech/rev:.4%}")
print("NOTE: extrapolation shown for calibration only - NOT an estimate of loss,")
print("NOT the cap basis (Solaris parameter unknown); specific cap open in STATUS.md")
# Anuencia HA not requested (25/10): pedido formal por escrito = day 0 of the 45-day clock
print("Anuencia HA: not requested -> written request = day 0 critical path")
# Labor gap kept open (not reconciled with provision basis)
print(f"Labor gap check: 1,400,000 - 380,000 = {1_400_000 - 380_000:,} (open, unreconciled)")
