#!/usr/bin/env python3
"""
Cálculo dos prazos processuais — Ferreira & Lima Transportes Ltda.
Processo Digital nº 1044712-38.2026.8.26.0114 — 7ª Vara Cível de Campinas/SP (e-SAJ).

Regras aplicadas (fontes fechadas — ver library/INDEX.md):
  * Publicação no DJe = primeiro dia útil seguinte à disponibilização
    (Lei 11.419/2006, art. 4º, §3º, e CPC art. 224, §2º) — lei11419_art4.md, cpc_prazos.md.
  * Início da contagem = primeiro dia útil após a publicação
    (CPC art. 224, §3º, e art. 231, VII) — cpc_prazos.md.
  * Contagem em dias úteis (CPC art. 219) — cpc_prazos.md.
  * Exclui-se o dia do começo; inclui-se o dia do vencimento (CPC art. 224, caput) — cpc_prazos.md.
  * Recesso forense de 20/12 a 20/01, ambos inclusive, suspende o curso do prazo
    (CPC art. 220) — cpc_prazos.md.
  * Dias não úteis = fins de semana + feriados do calendário forense de Campinas
    (calendario_forense_campinas.md) + recesso.
  * Prazo em dobro (CPC art. 229, caput) NÃO se aplica: processo em autos eletrônicos
    (CPC art. 229, §2º) — cpc_prazos.md.

Dias não úteis usados (transcritos de calendario_forense_campinas.md):
  - Fins de semana (sáb/dom).
  - Feriados: 01/01, Carnaval (16-18/02/2026; 08-09/02/2027), 03/04, 21/04, 01/05,
    04/06, 09/07, 07/09, 12/10, 28/10, 02/11, 15/11, 20/11/2026 (Zumbi e
    Consciência Negra — Lei 14.759/2023), 08/12/2026 (N. Sra. da Conceição,
    feriado municipal de Campinas), 24/12, 25/12, 31/12, 01/01/2027.
  - 25/01/2027 (Aniversário de SP) é PROPOSITIVAMENTE dia útil: feriado apenas
    na Capital, não em Campinas (calendario_forense_campinas.md).
"""
import datetime as dt

D = dt.date

FERIADOS = {
    D(2026, 1, 1), D(2026, 2, 16), D(2026, 2, 17), D(2026, 2, 18),
    D(2026, 4, 3), D(2026, 4, 21), D(2026, 5, 1), D(2026, 6, 4),
    D(2026, 7, 9), D(2026, 9, 7), D(2026, 10, 12), D(2026, 10, 28),
    D(2026, 11, 2), D(2026, 11, 15), D(2026, 11, 20), D(2026, 12, 8),
    D(2026, 12, 24), D(2026, 12, 25), D(2026, 12, 31), D(2027, 1, 1),
    D(2027, 2, 8), D(2027, 2, 9),  # Carnaval 2027
}

RECESSO_INI = D(2026, 12, 20)   # CPC art. 220: "entre 20 de dezembro e 20 de janeiro, inclusive"
RECESSO_FIM = D(2027, 1, 20)


def dia_util(d: D) -> bool:
    return d.weekday() < 5 and d not in FERIADOS and not (RECESSO_INI <= d <= RECESSO_FIM)


def primeiro_dia_util_apos(d: D) -> D:
    d += dt.timedelta(days=1)
    while not dia_util(d):
        d += dt.timedelta(days=1)
    return d


def vencimento(inicio: D, n_dias: int) -> D:
    """Exclui o dia do começo (inicio); inclui o dia do vencimento (CPC art. 224, caput)."""
    d, c = inicio, 0
    while c < n_dias:
        d += dt.timedelta(days=1)
        if dia_util(d):
            c += 1
    return d


def fmt(d: D) -> str:
    return f"{d.isoformat()} ({d.strftime('%A')})"


# ---------------- CITAÇÃO (disponibilização 19/11/2026) ----------------
DISP_CIT = D(2026, 11, 19)
pub_cit = primeiro_dia_util_apos(DISP_CIT)          # Lei 11.419/2006 art. 4º §3º / CPC 224 §2º
ini_cit = primeiro_dia_util_apos(pub_cit)           # CPC 224 §3º / 231 VII
contestacao = vencimento(ini_cit, 15)               # CPC art. 335

# ---------------- SENTENÇA (disponibilização 10/12/2026) ----------------
DISP_SEN = D(2026, 12, 10)
pub_sen = primeiro_dia_util_apos(DISP_SEN)
ini_sen = primeiro_dia_util_apos(pub_sen)
embargos = vencimento(ini_sen, 5)                   # CPC art. 1.023
apelacao = vencimento(ini_sen, 15)                  # CPC art. 1.003 §5º

# ---------------- HIPOTÉTICO: prazo em dobro (NÃO aplicável — CPC art. 229 §2º) ----------------
hip_contestacao = vencimento(ini_cit, 30)
hip_embargos = vencimento(ini_sen, 10)
hip_apelacao = vencimento(ini_sen, 30)

print("=== PRAZOS REAIS (prazo em dobro NÃO se aplica — CPC art. 229, §2º) ===")
print(f"  Citação  — disponibilização: {fmt(DISP_CIT)}")
print(f"             publicação:       {fmt(pub_cit)}")
print(f"             início contagem:  {fmt(ini_cit)}")
print(f"             CONTESTAÇÃO (15 d.u.):   {fmt(contestacao)}")
print(f"  Sentença — disponibilização: {fmt(DISP_SEN)}")
print(f"             publicação:       {fmt(pub_sen)}")
print(f"             início contagem:  {fmt(ini_sen)}")
print(f"             EMBARGOS (5 d.u.):       {fmt(embargos)}")
print(f"             APELAÇÃO (15 d.u.):      {fmt(apelacao)}")
print()
print("=== HIPOTÉTICO (dobro — NÃO aplicável, somente para referência) ===")
print(f"  contestação (30 d.u.): {fmt(hip_contestacao)}")
print(f"  embargos (10 d.u.):    {fmt(hip_embargos)}")
print(f"  apelação (30 d.u.):    {fmt(hip_apelacao)}")

# ---------------- Dias não úteis no intervalo da sentença (14/12/2026 a 04/02/2027) ----------------
print()
print("=== DIAS NÃO ÚTEIS no intervalo da sentença ===")
d, fim = ini_sen, apelacao
while d < fim:
    d += dt.timedelta(days=1)
    if not dia_util(d):
        motivo = "recesso" if RECESSO_INI <= d <= RECESSO_FIM else (
            "feriado" if d in FERIADOS else "fim de semana")
        print(f"  {fmt(d)} — {motivo}")
