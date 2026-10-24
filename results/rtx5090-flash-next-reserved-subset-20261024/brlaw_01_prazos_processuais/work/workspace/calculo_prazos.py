#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cálculo de prazos — autos 1044712-38.2026.8.26.0114 (7ª Vara Cível de Campinas/SP).

Biblioteca fechada: os feriados e o recesso são LIDOS DIRETAMENTE DA TABELA de
library/calendario_forense_campinas.md (nenhuma data é digitada neste script).

Regras aplicadas (todas com texto em library/):
- Lei 11.419/2006 art. 4º §§ 3º e 4º + CPC art. 224 §§ 2º e 3º: disponibilização
  às 24h do dia útil seguinte ao último dia do expediente do DJe.
- CPC art. 231, VII: dia do começo = data de publicação (prazo em DJe).
- CPC art. 224, caput: exclui-se o dia do começo, inclui-se o do vencimento.
- CPC art. 219: só dias úteis.
- CPC art. 220, caput: suspende-se o curso do prazo entre 20/12 e 20/01, inclusive.
- CPC art. 335, III: contestação 15 dias (prazo em dobro não aplicado — art. 229, § 2º).
- CPC art. 1.023: embargos de declaração 5 dias; a oposição de embargos interrompe o
  prazo para interpor recurso (texto do art. 1.026 transcrito na biblioteca).
- CPC art. 1.003, § 5º: apelação 15 dias.

Critério adotado (A): computa-se como dia 1 o primeiro dia útil seguinte ao da
publicação, porque a publicação é o "dia do começo" excluído pelo art. 231, VII
combinado com o caput do art. 224. Para controle, o critério (B) — excluir também
o primeiro dia útil — é calculado e demonstrado à parte.
"""
import json
import re
from datetime import date, datetime, timedelta

DIA_SEMANA = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
LIB = "library/calendario_forense_campinas.md"


def f(d):
    return d.strftime("%d/%m/%Y")


def fd(d):
    return f"{f(d)} ({DIA_SEMANA[d.weekday()]})"


# ---------------------------------------------------------------------------
# 1. dados do calendário: parseados da tabela da biblioteca
# ---------------------------------------------------------------------------
def ler_calendario(caminho=LIB):
    """Lê a tabela markdown e o comunicado de recesso da biblioteca."""
    texto = open(caminho, encoding="utf-8").read()
    feriados, so_capital, sem_expediente = set(), set(), set()
    observacoes = {}
    for linha in texto.splitlines():
        m = re.match(r"^\|\s*(\d{2}/\d{2}/\d{4})\s*\((\w{3})\)\s*\|\s*(.+?)\s*\|$", linha)
        if not m:
            continue
        d = datetime.strptime(m.group(1), "%d/%m/%Y").date()
        ocorrencia = m.group(3)
        if d.weekday() >= 5:  # já é fim de semana
            observacoes.setdefault(d, []).append(ocorrencia)
            continue
        if "APENAS na Capital" in ocorrencia:
            # a própria biblioteca afasta o feriado em Campinas
            so_capital.add(d)
            observacoes[d] = [ocorrencia + " → dia útil em Campinas"]
        elif "sem expediente" in ocorrencia or "sem prazo" in ocorrencia:
            sem_expediente.add(d)
            observacoes[d] = [ocorrencia]
        else:
            feriados.add(d)
            observacoes[d] = [ocorrencia]
    m = re.search(r"(\d{2}/\d{2}/\d{4})\s*a\s*(\d{2}/\d{2}/\d{4})\s*,\s*inclusive", texto)
    recesso = (
        datetime.strptime(m.group(1), "%d/%m/%Y").date(),
        datetime.strptime(m.group(2), "%d/%m/%Y").date(),
    )
    return feriados, so_capital, sem_expediente, recesso, observacoes


FERIADOS, SO_CAPITAL, SEM_EXPEDIENTE, RECESSO, OBS = ler_calendario()


def em_recesso(d):
    return RECESSO[0] <= d <= RECESSO[1]


def util(d):
    """É dia de expediente forense em Campinas? (art. 219 + art. 220 + calendário)."""
    if d.weekday() >= 5:
        return False
    if em_recesso(d):
        return False
    return d not in (FERIADOS | SEM_EXPEDIENTE)


def motivo(d):
    if d.weekday() >= 5:
        return "fim de semana"
    if em_recesso(d):
        if d in FERIADOS or d in SEM_EXPEDIENTE:
            return "recesso + " + OBS[d][0]
        return "recesso forense (20/12–20/01)"
    if d in FERIADOS:
        return "feriado: " + OBS[d][0]
    if d in SEM_EXPEDIENTE:
        return "sem expediente forense: " + OBS[d][0]
    if d in SO_CAPITAL:
        return "dia útil em Campinas (feriado só na Capital)"
    return "dia útil"


def proximo_util(d):
    d += timedelta(days=1)
    while not util(d):
        d += timedelta(days=1)
    return d


def add_uteis(inicio, n):
    """`inicio` é o dia 1 quando é dia útil; devolve o dia de vencimento."""
    if not util(inicio):
        raise ValueError(f"{f(inicio)} não é dia útil")
    d, contados = inicio, 1
    while contados < n:
        d = proximo_util(d)
        contados += 1
    return d


# ---------------------------------------------------------------------------
# 2. intimação eletrônico-publicada (Lei 11.419/2006 art. 4º §§ 3º-4º; CPC 224 §§ 2º-3º)
# ---------------------------------------------------------------------------
def publicacao(disponibilizacao):
    """Data de publicação: primeiro dia útil seguinte ao da disponibilização
    (Lei 11.419/2006 art. 4º, §§ 3º e 4º; CPC art. 224, § 2º).

    A disponibilização considera-se efetivada às 24h do dia da publicação
    (art. 4º, § 4º, parte final; CPC art. 224, § 3º); por isso esse dia não gera
    prazo: é o "dia do começo" excluído pelo art. 231, VII c/c art. 224, caput.
    """
    return proximo_util(disponibilizacao)   # pula fins de semana e feriados


def dia_publicacao(disponibilizacao):
    return publicacao(disponibilizacao)


def janela_recesso():
    """Dias corridos e dias de semana dentro da janela de recesso da biblioteca.

    Todos os dias de semana da janela são suspensos pelo art. 220; alguns
    coincidem com feriado/sem expediente (dupla razão de suspensão).
    """
    d, corridos, semana, fer_dentro = RECESSO[0], 0, 0, []
    while d <= RECESSO[1]:
        corridos += 1
        if d.weekday() < 5:
            semana += 1
            if d in (FERIADOS | SEM_EXPEDIENTE):
                fer_dentro.append(d)
        d += timedelta(days=1)
    return corridos, semana, fer_dentro


# ---------------------------------------------------------------------------
# 3. cômputo dia a dia
# ---------------------------------------------------------------------------
def trilha(pub, n, dobro=False, rotulo=""):
    primeiro = proximo_util(pub)
    d, linhas = primeiro, []
    while d <= add_uteis(primeiro, n):
        linhas.append((d, util(d)))
        d += timedelta(days=1)
    venc = linhas[-1][0]
    return primeiro, venc, linhas


def calcular(criterio_B=False):
    """criterio_B=True: também exclui o 1º dia útil (tese minoritária, só para controle)."""
    out = {}
    for rotulo, disp, prazo in (
        ("citacao", date(2026, 11, 19), 15),
        ("citacao_dobro_hipotetico", date(2026, 11, 19), 30),
        ("sentenca", date(2026, 12, 10), 5),
        ("sentenca_apelacao", date(2026, 12, 10), 15),
    ):
        pub = dia_publicacao(disp)
        if criterio_B:
            primeiro = proximo_util(proximo_util(pub))
            venc = proximo_util(add_uteis(primeiro, prazo - 1))
        else:
            primeiro, venc, _ = trilha(pub, prazo)
        out[rotulo] = dict(disp=disp, pub=pub, primeiro=primeiro, venc=venc, prazo=prazo)
    return out


A, B = calcular(False), calcular(True)


def contabilidade(pub, venc):
    """Fechamento da janela [publicação .. vencimento]:

    corridos = 1 (dia do começo, excluído) + dias computados + suspensos + fins de semana.
    """
    d = pub
    corridos = computados = fds = 0
    comeco, suspensos = [], []
    while d <= venc:
        corridos += 1
        if d == pub:
            comeco.append(d)
        elif d.weekday() >= 5:
            fds += 1
        elif util(d):
            computados += 1
        else:
            suspensos.append((d, motivo(d)))
        d += timedelta(days=1)
    return dict(corridos=corridos, comeco=len(comeco), computados=computados,
                fds=fds, suspensos=suspensos)


def conferir():
    # art. 224, caput + art. 231, VII: nº de dias úteis do 1º dia ao vencimento = prazo
    for key, r in A.items():
        _, _, tr = trilha(r["pub"], r["prazo"])
        uteis = sum(1 for d, u in tr if u)
        assert uteis == r["prazo"], (key, uteis, r["prazo"])
        assert util(r["venc"]) and r["primeiro"] > r["pub"], key

    corridos, semana, fer_dentro = janela_recesso()
    print(f"janela_recesso: {f(RECESSO[0])} a {f(RECESSO[1])} = {corridos} corridos; "
          f"{semana} dias de semana (todos suspensos pelo art. 220, caput); os que também "
          f"são feriado/sem expediente: {[f(d) for d in fer_dentro]}")
    print(f"25/01/2027 feriado em Campinas? "
          f"{'NÃO — a tabela da biblioteca diz que é só na Capital' if date(2027,1,25) in SO_CAPITAL else 'sim'}")
    print(f"08/12/2026 feriado em Campinas? {'SIM' if date(2026,12,8) in FERIADOS else 'não'}")

    janelas = [("citacao→contestacao", A["citacao"], 15),
               ("citacao→contestacao (dobro hipotético)", A["citacao_dobro_hipotetico"], 30),
               ("sentenca→embargos", A["sentenca"], 5),
               ("sentenca→apelacao", A["sentenca_apelacao"], 15)]
    for rot, r, prazo in janelas:
        c = contabilidade(r["pub"], r["venc"])
        assert c["computados"] == prazo and c["comeco"] == 1, (rot, c)
        print(f"{rot}: {f(r['pub'])}→{f(r['venc'])} = {c['corridos']} corridos = "
              f"1 (dia do começo) + {c['computados']} computados (prazo {prazo}) + "
              f"{len(c['suspensos'])} suspensos + {c['fds']} fds")
        for d, m in c["suspensos"]:
            print(f"      - {fd(d)}: {m}")

    for key, r in A.items():
        print(f"  [A] {key:26s} pub={f(r['pub'])} 1ºdia={f(r['primeiro'])} "
              f"prazo={r['prazo']} venc={f(r['venc'])} ({DIA_SEMANA[r['venc'].weekday()]})")
    for key, r in B.items():
        print(f"  [B] {key:26s} pub={f(r['pub'])} 1ºdia={f(r['primeiro'])} "
              f"prazo={r['prazo']} venc={f(r['venc'])} ({DIA_SEMANA[r['venc'].weekday()]})")


if __name__ == "__main__":
    conferir()
    print(f"feriados/sem expediente usados (da tabela da biblioteca): "
          f"{sorted(f(d) for d in (FERIADOS | SEM_EXPEDIENTE))}")
