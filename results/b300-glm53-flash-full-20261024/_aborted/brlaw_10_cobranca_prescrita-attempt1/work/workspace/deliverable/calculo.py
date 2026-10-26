#!/usr/bin/env python3
# Cálculo — Técnica Forte × Metalúrgica Boa Vista (contrato 01/09/2020)
# Dados: documents/contrato_prestacao_servicos.md (6 x R$ 30.000, venc. dia 10,
# multa 2%, juros 1% a.m., IPCA), documents/emails_reconhecimento.txt
# (reconhecimento das parcelas 1-4 em 15/09/2022; PIX de R$ 10.000 em 02/08/2023
# "por conta da parcela 1"), documents/negativacao_e_consulta.md (Serasa
# 12/08/2026 por R$ 180.000). Hoje: 12/10/2026.

import calendar
from datetime import date

HOJE = date(2026, 10, 12)

def add_months(d, n):
    y = d.year + (d.month - 1 + n) // 12
    m = (d.month - 1 + n) % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))

def meses_dias(inicio, fim):
    n = 0
    while add_months(inicio, n + 1) <= fim:
        n += 1
    resto = (fim - add_months(inicio, n)).days
    return n, resto

def br(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

parcelas = {
    1: date(2020, 10, 10), 2: date(2020, 11, 10), 3: date(2020, 12, 10),
    4: date(2021, 1, 10),  5: date(2021, 2, 10),  6: date(2021, 3, 10),
}
INTERRUPCAO = date(2022, 9, 15)  # e-mail de reconhecimento (parcelas 1 a 4)

print("== PRESCRICAO (CC 206 §5º I: 5 anos; interruptivo CC 202 VI, p.único) ==")
for p, venc in parcelas.items():
    termo = add_months(venc, 60)
    if p <= 4:
        novo = add_months(INTERRUPCAO, 60)
        ok = INTERRUPCAO < termo
        print(f"p{p}: venc {venc} | termo original {termo} | interrompida {INTERRUPCAO} "
              f"({'valida' if ok else 'INVALIDA'}) | novo termo {novo} | prescrita {HOJE > novo}")
    else:
        print(f"p{p}: venc {venc} | termo original {termo} | sem interruptivo (contestada) | "
              f"prescrita {HOJE > termo}")

print()
print("== PRINCIPAL EXIGIVEL (aceita parcial 02/08/2023 abate a parcela 1) ==")
resid = {p: (30000 - 10000) if p == 1 else 30000 for p in range(1, 5)}
for p, v in resid.items():
    formula = "30000 - 10000" if p == 1 else "30000"
    print(f"p{p}: {formula} = {v}")
principal = sum(resid.values())
print(f"principal exigivel = {principal}")
print(f"prescrito (p5+p6) = 30000 + 30000 = 60000")

print()
print("== JUROS SIMPLES 1% a.m. desde o vencimento ate 12/10/2026 (convencao 30 dias/mes) ==")
juros_total = 0.0
for p in range(1, 5):
    n, d = meses_dias(parcelas[p], HOJE)
    frac = n + d / 30
    j = resid[p] * 0.01 * frac
    juros_total += j
    print(f"p{p}: {resid[p]} x 0,01 x ({n} meses + {d}/30 = {frac:.4f}) = {br(j)}")
print(f"total juros = {br(juros_total)}")

print()
print("== MULTA 2% (base: saldo residual em mora; alternativa: parcela cheia) ==")
multa_res = sum(resid.values()) * 0.02
print(f"base residual: {principal} x 0,02 = {br(multa_res)}")
multa_cheia = 4 * 30000 * 0.02
print(f"(alternativa, parcela cheia: 4 x 30000 x 0,02 = {br(multa_cheia)})")

total = principal + juros_total + multa_res
print(f"TOTAL estimado hoje (juros base residual, sem IPCA) = {principal} + "
      f"{br(juros_total)} + {br(multa_res)} = {br(total)}")
print(f"(com multa sobre parcela cheia: {br(principal + juros_total + multa_cheia)})")
print(f"crescimento mensal esperado do placar (juros) ~ 0,01 x 110000 = {br(1100)}/mes")

print()
print("== CHEQUE DE CONGRUENCIA (contrato x pagamento x reconhecimento) ==")
print(f"contrato: 6 x 30000 = 180000 (base da inclusao Serasa de 12/08/2026)")
print(f"reconhecido em 15/09/2022 (p1-p4): 4 x 30000 = 120000")
print(f"pago em 02/08/2023: 10000  ->  exigivel de principal = 120000 - 10000 = {120000-10000}")
print(f"Serasa lançou 180000; correto seria {principal}; excesso = 180000 - {principal} = {180000-principal}")
print(f"  desdobramento do excesso: prescrito 60000 + ja pago 10000 = {60000+10000}")
