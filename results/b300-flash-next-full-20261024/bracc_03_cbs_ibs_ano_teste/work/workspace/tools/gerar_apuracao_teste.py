#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apuração de teste CBS/IBS — Horizonte Comércio e Serviços Ltda — agosto/2026.

Gera deliverable/apuracao_teste.json no schema EXATO do CONTRACT.md:
  saidas[]   : numero, data, valor, cbs, ibs, situacao("regular"|"irregular"), motivo
  entradas[] : numero, valor, credito_cbs, credito_ibs, motivo
  totais     : debito_cbs, debito_ibs, credito_cbs, credito_ibs, saldo_cbs, saldo_ibs
  recolhimento_devido, condicao_dispensa
Chaves de acesso, grupo IBSCBS observado e a conta de cada linha vão dentro de
"motivo"/"condicao_dispensa" para não desviar do schema.

Regras (CONTRACT.md + library/):
  - Alíquotas de teste 2026 (LC 214/2025 art. 343): CBS 0,90% / IBS 0,10%
    (pCBS 0,90 / pIBSUF 0,10 / pIBSMun 0,00 — NT 2025.002).
  - Débito calculado sobre TODAS as saídas do mês; notas de emitente do regime
    regular SEM o grupo IBSCBS emitidas a partir de 03/08/2026, ou com destaque
    invertido, são "irregular" (Comunicado CGIBS 03/08/2026). Documentos
    anteriores a 03/08/2026 sem o grupo permanecem válidos.
  - Crédito (LC 214 art. 346): só aquisição de contribuinte do regime regular
    COM destaque; aquisição de optante do Simples limita-se ao valor efetivamente
    recolhido pelo optante e, em 2026, sem destaque não há crédito (art. 347).
Execução: python3 tools/gerar_apuracao_teste.py  ->  deliverable/apuracao_teste.json
"""
import csv
import glob
import json
import os
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PCT_CBS, PCT_IBS = 0.009, 0.001  # 0,90% e 0,10% — alíquotas de teste de 2026
CORTE_OBRIGATORIEDADE = "2026-08-03"  # Comunicado CGIBS

# Schema obrigatório do CONTRACT.md (verificação automática no final):
CAMPOS_SAIDA = {"numero", "data", "valor", "cbs", "ibs", "situacao", "motivo"}
CAMPOS_ENTRADA = {"numero", "valor", "credito_cbs", "credito_ibs", "motivo"}
CAMPOS_TOTAIS = {"debito_cbs", "debito_ibs", "credito_cbs", "credito_ibs",
                 "saldo_cbs", "saldo_ibs"}


def r2(x):
    return round(x + 1e-9, 2)


def fmt(x):
    """Número em formato brasileiro: 18000.0 -> '18.000,00'."""
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def cnpj_fmt(c):
    return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}" if len(c) == 14 else c


def data_pt(iso):  # '2026-08-10' -> '10/08/2026'
    a, m, d = iso.split("-")
    return f"{d}/{m}/{a}"


def strip_ns(el):
    if isinstance(el.tag, str) and "}" in el.tag:
        el.tag = el.tag.split("}", 1)[1]
    for c in el:
        strip_ns(c)


def parse(path):
    n = ET.parse(path).getroot()
    strip_ns(n)
    inf = n.find("NFe/infNFe")
    ide, emit, dest, det, tot = (inf.find(x) for x in
                                 ("ide", "emit", "dest", "det", "total/ICMSTot"))
    t = lambda parent, tag: (parent.find(tag).text.strip()
                             if parent is not None and parent.find(tag) is not None
                             and parent.find(tag).text else "")

    def grupo_ibs():
        g = det.find("imposto/IBSCBS")
        if g is None:
            return None
        gg = g.find("gIBSCBS")

        def f(path):
            el = gg.find(path) if gg is not None else None
            return float(el.text) if el is not None and el.text else 0.0

        return dict(cst=t(g, "CST"), cClassTrib=t(g, "cClassTrib"), base=f("vBC"),
                    p_cbs=f("gCBS/pCBS"), cbs=f("gCBS/vCBS"),
                    p_ibs_uf=f("gIBSUF/pIBSUF"), ibs_uf=f("gIBSUF/vIBSUF"),
                    p_ibs_mun=f("gIBSMun/pIBSMun"), ibs_mun=f("gIBSMun/vIBSMun"))

    ibs = grupo_ibs()
    return dict(
        arquivo=os.path.basename(path),
        chave=t(n.find("protNFe/infProt"), "chNFe"),
        numero=int(t(ide, "nNF")), data=t(ide, "dhEmi")[:10],
        tpNF=t(ide, "tpNF"), natop=t(ide, "natOp"),
        emit_cnpj=t(emit, "CNPJ"), emit_nome=t(emit, "xNome"), emit_CRT=t(emit, "CRT"),
        dest_cnpj=t(dest, "CNPJ"), dest_nome=t(dest, "xNome"),
        valor=float(t(tot, "vProd") or t(det / "prod", "vProd")),
        ibs=ibs,
    )


def main():
    carteira = {}
    with open(os.path.join(BASE, "documents/carteira_clientes.csv"), encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            carteira[row["cnpj"]] = dict(nome=row["nome"], regime=row["regime_tributario"].strip().lower())
    simples = {c for c, r in carteira.items() if r["regime"] in ("simples", "mei")}

    saidas = [parse(p) for p in sorted(glob.glob(os.path.join(BASE, "documents/saidas/*.xml")))]
    entradas = [parse(p) for p in sorted(glob.glob(os.path.join(BASE, "documents/entradas/*.xml")))]
    assert [s["numero"] for s in saidas] == list(range(2301, 2313)), "faltam notas de saída"
    assert [e["numero"] for e in entradas] == list(range(2313, 2318)), "faltam notas de entrada"
    forn_cnpj = {e["emit_cnpj"] for e in entradas}

    RESP = (" Causa-raiz confirmada pelo cliente em 25/10/2026: a rejeição da SEFAZ dizia 'Grupo IBSCBS não "
            "informado para emitente do regime regular (NT 2025.002)' e o TI reverteu a versão do emissor para "
            "'contornar' a checagem — workaround deliberado, desfeito por orientação nossa. ")
    ALIQ = "CBS 0,90% e IBS 0,10% (LC 214/2025 art. 343; NT 2025.002 — pCBS 0,90 / pIBSUF 0,10 / pIBSMun 0,00)"

    linhas_saida = []
    for s in saidas:
        v, n, d = s["valor"], s["numero"], s["data"]
        d_cbs, d_ibs = r2(v * PCT_CBS), r2(v * PCT_IBS)
        g = s["ibs"]
        conta = (f"Base = valor da nota, R$ {fmt(v)}. Débito de teste: CBS 0,90% × {fmt(v)} = {fmt(d_cbs)}; "
                 f"IBS 0,10% × {fmt(v)} = {fmt(d_ibs)}.")
        cliente = ("cliente da carteira (regime " + carteira[s["dest_cnpj"]]["regime"] + ")"
                   if s["dest_cnpj"] in carteira else
                   "fornecedor das entradas" if s["dest_cnpj"] in forn_cnpj else "destinatário não cadastrado")
        inicio = (f"NF-e {n}, emitida em {data_pt(d)} por Horizonte (CNPJ {cnpj_fmt(s['emit_cnpj'])}, CRT "
                  f"{s['emit_CRT']} — regime regular) para {s['dest_nome']} ({cnpj_fmt(s['dest_cnpj'])}), "
                  f"{s['natop']} — {cliente}. ")
        fim = f" Chave de acesso (protNFe): {s['chave']}."
        grupo = (f"Grupo IBSCBS presente no documento: CST {g['cst']}, cClassTrib {g['cClassTrib']}, "
                 f"vCBS {fmt(g['cbs'])}, vIBSUF {fmt(g['ibs_uf'])}, vIBSMun {fmt(g['ibs_mun'])}. "
                 if g else "Grupo IBSCBS não preenchido no documento. ")

        if g is None:
            if d < CORTE_OBRIGATORIEDADE:
                situacao = "regular"
                meio = (grupo + "Emissão anterior a 03/08/2026: o Comunicado CGIBS (jul/2026) torna o grupo "
                        "obrigatório para emitente do regime regular a partir de 03/08/2026 e os documentos "
                        "anteriores permanecem válidos.")
            else:
                situacao = "irregular"
                meio = (grupo + f"Emitida a partir de 03/08/2026 sem o grupo IBSCBS, obrigatório para emitente "
                        f"do regime regular (Comunicado CGIBS jul/2026; NT 2025.002) — descumprimento de "
                        f"obrigação acessória, com risco de perda da dispensa de recolhimento (ADCT art. 125, "
                        f"§4º). O débito de teste é lançado pelos valores corretos, {ALIQ}." + RESP)
        else:
            v_ibs = g["ibs_uf"] + g["ibs_mun"]
            ok = (abs(g["cbs"] - d_cbs) <= 0.01 and abs(v_ibs - d_ibs) <= 0.01
                  and g["p_cbs"] == 0.90 and g["p_ibs_uf"] == 0.10 and g["p_ibs_mun"] == 0.0)
            if ok:
                situacao = "regular"
                meio = (grupo + f"Destaque conferido: coincide com {ALIQ}.")
            else:
                situacao = "irregular"
                meio = (grupo + f"Destaque INVERTIDO no documento: destaca CBS {fmt(g['cbs'])} (pCBS "
                        f"{g['p_cbs']:.2f}%) e IBS {fmt(v_ibs)} (pIBSUF {g['p_ibs_uf']:.2f}%), quando as "
                        f"alíquotas de 2026 são {ALIQ}. O total destacado no documento ({fmt(g['cbs'] + v_ibs)}) "
                        f"até coincide com o total correto ({fmt(d_cbs + d_ibs)}), mas as rubricas estão trocadas; "
                        f"a apuração-teste lança os valores corretos por operação.")
        linhas_saida.append({"numero": n, "data": d, "valor": v, "cbs": d_cbs, "ibs": d_ibs,
                             "situacao": situacao, "motivo": inicio + meio + " " + conta + fim})

    linhas_entrada = []
    for e in entradas:
        v, n = e["valor"], e["numero"]
        simples_f = (carteira.get(e["emit_cnpj"], {}).get("regime") in ("simples", "mei")) or e["emit_CRT"] == "1"
        g = e["ibs"]
        destaque_ok = (g is not None and abs(g["cbs"] - r2(v * PCT_CBS)) <= 0.01
                       and abs(g["ibs_uf"] + g["ibs_mun"] - r2(v * PCT_IBS)) <= 0.01)
        credito = destaque_ok and not simples_f
        c_cbs, c_ibs = (r2(v * PCT_CBS), r2(v * PCT_IBS)) if credito else (0.0, 0.0)
        inicio = (f"NF-e {n}, emitida em {data_pt(e['data'])} por {e['emit_nome']} "
                  f"({cnpj_fmt(e['emit_cnpj'])}, CRT {e['emit_CRT']}) para Horizonte, valor R$ {fmt(v)}. ")
        fim = f" Chave de acesso (protNFe): {e['chave']}."
        if credito:
            motivo = (inicio + f"Fornecedor não consta da carteira de clientes; regime regular inferido do CRT "
                      f"{e['emit_CRT']} da própria NF-e. Destaque correto no documento: vCBS {fmt(g['cbs'])} = "
                      f"0,90% × {fmt(v)} e vIBS {fmt(g['ibs_uf'] + g['ibs_mun'])} = 0,10% × {fmt(v)}. Crédito de "
                      f"teste mantido: em 2026 geram crédito as aquisições de contribuintes do regime regular com "
                      f"destaque (LC 214/2025, art. 346)." + fim)
        elif simples_f and g is None:
            motivo = (inicio + "Optante do Simples Nacional (CRT 1), que em 2026 não está sujeito ao destaque "
                      "nem à apuração (LC 214/2025, art. 347). Documento SEM destaque de IBS/CBS. Crédito zero: "
                      "aquisições de optante do Simples geram crédito limitado ao valor efetivamente recolhido "
                      "pelo optante a título de IBS/CBS no Simples e, em 2026, sem destaque, não há crédito "
                      "(LC 214/2025, art. 347; art. 346)." + fim)
        elif g is None:
            antes = (f"Fornecedor de regime regular (CRT {e['emit_CRT']}); emissão em {data_pt(e['data'])}, "
                     "anterior a 03/08/2026, quando o grupo IBSCBS ainda não era obrigatório — documento válido "
                     "(Comunicado CGIBS), mas SEM destaque de IBS/CBS. "
                     if e["data"] < CORTE_OBRIGATORIEDADE else
                     f"Fornecedor de regime regular (CRT {e['emit_CRT']}) emitindo após 03/08/2026 sem o grupo "
                     "IBSCBS — documento não deveria ter sido autorizado; SEM destaque de IBS/CBS. ")
            motivo = (inicio + antes + "Crédito zero: o direito a crédito em 2026 pressupõe aquisição de "
                      "contribuinte do regime regular COM destaque (LC 214/2025, art. 346)." + fim)
        else:
            motivo = (inicio + "Destaque de IBS/CBS presente, porém incorreto — sem crédito em 2026 "
                      "(LC 214/2025, art. 346)." + fim)
        linhas_entrada.append({"numero": n, "valor": v, "credito_cbs": c_cbs,
                               "credito_ibs": c_ibs, "motivo": motivo})

    soma = lambda xs, k: r2(sum(x[k] for x in xs))
    totais = {
        "debito_cbs": soma(linhas_saida, "cbs"), "debito_ibs": soma(linhas_saida, "ibs"),
        "credito_cbs": soma(linhas_entrada, "credito_cbs"), "credito_ibs": soma(linhas_entrada, "credito_ibs"),
        "saldo_cbs": r2(soma(linhas_saida, "cbs") - soma(linhas_entrada, "credito_cbs")),
        "saldo_ibs": r2(soma(linhas_saida, "ibs") - soma(linhas_entrada, "credito_ibs")),
    }

    doc = {
        "saidas": linhas_saida,
        "entradas": linhas_entrada,
        "totais": totais,
        "recolhimento_devido": 0.0,
        "condicao_dispensa": (
            "Horizonte Comércio e Serviços Ltda. (CNPJ 27.119.804/0001-30, regime regular, CRT 3), período "
            "2026-08. Alíquotas do período de teste: CBS 0,90% e IBS 0,10% (LC 214/2025, art. 343; NT 2025.002). "
            "O recolhimento de IBS/CBS de 2026 está DISPENSADO nos termos do ADCT art. 125, §4º (redação da LC "
            "214/2025), CONDICIONADO ao cumprimento das obrigações acessórias previstas na legislação — destaque "
            "nos documentos fiscais, escrituração e apuração-teste (LC 214/2025, arts. 343 e 346). Em agosto/2026 "
            "a Horizonte NÃO cumpriu integralmente: NF-e 2308, 2310 e 2312 emitidas a partir de 03/08/2026 sem o "
            "grupo IBSCBS obrigatório e NF-e 2309 com alíquotas invertidas (Comunicado CGIBS jul/2026; NT "
            "2025.002) — risco de perda da dispensa (ADCT art. 125, §4º). Recolhimento devido informado como "
            "R$ 0,00 sob a dispensa vigente; se a dispensa for perdida, o saldo apurado do período seria exigível: "
            "CBS R$ 2.862,00 + IBS R$ 318,00 = R$ 3.180,00 (a extensão da perda — mês inteiro ou só operações "
            "irregulares — não está definida na biblioteca). Nada foi recolhido, portanto nada há a compensar com "
            "PIS/COFINS (ADCT art. 125, §1º). Base das saídas do mês, R$ 480.000,00, confere com a base PIS/COFINS "
            "de agosto do cliente (documents/apuracao_normal_agosto.md)."),
    }

    # Conferências automáticas (schema do CONTRACT + aritmética):
    assert all(set(x) == CAMPOS_SAIDA for x in doc["saidas"]), "saida fora do schema do CONTRACT"
    assert all(set(x) == CAMPOS_ENTRADA for x in doc["entradas"]), "entrada fora do schema do CONTRACT"
    assert set(doc["totais"]) == CAMPOS_TOTAIS, "totais fora do schema do CONTRACT"
    assert set(doc) == {"saidas", "entradas", "totais", "recolhimento_devido", "condicao_dispensa"}, \
        "raiz do JSON fora do schema do CONTRACT"
    assert all(x["situacao"] in ("regular", "irregular") for x in doc["saidas"])
    assert all(r2(x["cbs"] - x["valor"] * PCT_CBS) == 0.0 and r2(x["ibs"] - x["valor"] * PCT_IBS) == 0.0
               for x in doc["saidas"]), "débito por linha ≠ alíquota × base"
    assert soma(linhas_saida, "valor") == 480000.00, "base das saídas ≠ R$ 480.000,00 (PIS/COFINS)"
    assert totais == {"debito_cbs": 4320.00, "debito_ibs": 480.00, "credito_cbs": 1458.00,
                      "credito_ibs": 162.00, "saldo_cbs": 2862.00, "saldo_ibs": 318.00}, totais
    assert sum(1 for x in doc["entradas"] if x["credito_cbs"] > 0) == 3, "esperados 3 créditos (2314/2316/2317)"

    out = os.path.join(BASE, "deliverable/apuracao_teste.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("totais:", json.dumps(totais, ensure_ascii=False))
    print("irregulars:", [x["numero"] for x in doc["saidas"] if x["situacao"] == "irregular"])
    print("creditadas:", [x["numero"] for x in doc["entradas"] if x["credito_cbs"] > 0])
    print("base saidas:", fmt(soma(linhas_saida, "valor")), "| entradas:", fmt(soma(linhas_entrada, "valor")))
    print("gerado:", out)


if __name__ == "__main__":
    main()
