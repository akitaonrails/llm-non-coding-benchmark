"""BRACC-3 · L3 · Ano-teste CBS/IBS 2026 — 'não há imposto novo em 2026'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, nfe_xml, money, q2, COMMON_RULES

ANO = 2026
CBS, IBS = D("0.9"), D("0.1")
MARCO = dt.date(2026, 8, 3)


def build():
    c = Case("bracc_03_cbs_ibs_ano_teste", "bracc", "Apuração-teste CBS/IBS no ano de transição (2026)", "L3", cur="BRL")
    emit = {"cnpj": "27119804000130", "nome": "HORIZONTE COMERCIO E SERVICOS LTDA", "crt": "3"}
    clientes = [{"cnpj": "11222333000144", "nome": "BRISA MATERIAIS LTDA", "regime": "regular"}, {"cnpj": "44555666000177", "nome": "PONTO FIXO COMERCIO ME", "regime": "simples"},
                {"cnpj": "77888999000100", "nome": "SERRA VERDE AGRO S.A.", "regime": "regular"}, {"cnpj": "12345678000199", "nome": "J. SILVA REPRESENTACOES MEI", "regime": "mei"}]
    saidas = []
    n = 2300
    # 12 saídas em agosto/2026: 5 antes de 03/08 (sem campos = regular), 7 depois (3 sem campos = irregular; 1 com alíquota invertida)
    plan = [(1, 0, 18000, None, ""), (1, 2, 24000, None, ""), (2, 1, 9500, None, ""), (2, 0, 31000, None, ""), (2, 3, 4200, None, ""),
            (4, 0, 42000, {"cbs_aliq": "0.90", "ibs_aliq": "0.10"}, ""), (6, 2, 56000, {"cbs_aliq": "0.90", "ibs_aliq": "0.10"}, ""), (10, 1, 12500, None, "SEM CAMPOS após 03/08"),
            (13, 0, 38000, {"cbs_aliq": "0.10", "ibs_aliq": "0.90"}, "ALÍQUOTAS INVERTIDAS"), (18, 3, 7800, None, "SEM CAMPOS após 03/08"), (21, 2, 61000, {"cbs_aliq": "0.90", "ibs_aliq": "0.10"}, ""), (27, 0, 176000, None, "SEM CAMPOS após 03/08")]
    for d, ci, val, grp, obs in plan:
        n += 1
        emissao = dt.date(ANO, 8, d)
        nfe_xml(c, f"saidas/nfe_{n}.xml", numero=n, serie=1, emissao=emissao, emit=emit, dest=clientes[ci], itens=[{"descr": "Mercadoria/serviço — lote agosto", "ncm": "84713012", "qtd": 1, "vun": val}], cfop="5102", natureza="Venda", ibscbs=grp)
        saidas.append(dict(numero=n, data=emissao, cliente=clientes[ci], valor=D(val), grupo=grp, obs=obs))
    entradas = []
    for d, forn, val, grp in [(2, ("55666777000188", "DISTRIBUIDORA NORTE LTDA", "regular"), 48000, None), (5, ("55666777000188", "DISTRIBUIDORA NORTE LTDA", "regular"), 62000, {"cbs_aliq": "0.90", "ibs_aliq": "0.10"}),
                              (9, ("44555666000177", "PONTO FIXO COMERCIO ME", "simples"), 15000, None), (16, ("99000111000122", "LOGISTICA ATLAS S.A.", "regular"), 40000, {"cbs_aliq": "0.90", "ibs_aliq": "0.10"}),
                              (22, ("55666777000188", "DISTRIBUIDORA NORTE LTDA", "regular"), 60000, {"cbs_aliq": "0.90", "ibs_aliq": "0.10"})]:
        n += 1
        emissao = dt.date(ANO, 8, d)
        nfe_xml(c, f"entradas/nfe_{n}.xml", numero=n, serie=1, emissao=emissao, emit={"cnpj": forn[0], "nome": forn[1], "crt": "1" if forn[2] == "simples" else "3"}, dest={"cnpj": emit["cnpj"], "nome": emit["nome"]}, itens=[{"descr": "Compra de mercadorias", "ncm": "84713012", "qtd": 1, "vun": val}], cfop="1102", natureza="Compra", ibscbs=grp, tipo="entrada")
        entradas.append(dict(numero=n, data=emissao, fornecedor=forn, valor=D(val), grupo=grp))
    c.csv("carteira_clientes.csv", ["cnpj", "nome", "regime_tributario"], [[x["cnpj"], x["nome"], x["regime"]] for x in clientes])
    c.doc("apuracao_normal_agosto.md", f"""
# Apuração normal — agosto/{ANO} (regime cumulativo, Lucro Presumido)
| Tributo | Base | Alíquota | Valor |
|---|---:|---:|---:|
| PIS | {money(sum(s['valor'] for s in saidas), 'BRL')} | 0,65% | {money(q2(sum(s['valor'] for s in saidas) * D('0.0065')), 'BRL')} |
| COFINS | idem | 3,00% | {money(q2(sum(s['valor'] for s in saidas) * D('0.03')), 'BRL')} |
| ICMS (SP, mercadorias) | apuração própria | 18% | (ver livro) |
| ISS (serviços) | — | 5% | (ver livro) |
""")
    c.doc("email_gerente_fiscal.txt", f"""
De: Paulo (gerente fiscal)
Assunto: CBS/IBS — precisa fazer algo em agosto?

Li que em 2026 é só "informativo", não se paga nada. A SEFAZ rejeitou duas notas semana passada mas o
sistema voltou a emitir. Para cliente do Simples e MEI eu não destaco nada, certo? E o IBS/CBS na nota
de entrada do Ponto Fixo (Simples) — posso creditar? Me diz o que tem que fazer, de forma objetiva.
""")
    # --- biblioteca (texto fornecido é a autoridade)
    c.library("lc214_2025_transicao.md", "LC 214/2025 — período de teste de 2026 (excertos)", "LC 214/2025, arts. 343 a 348; ADCT art. 125 (EC 132/2023)", f"""
**ADCT, art. 125.** Em **2026**, a CBS será cobrada à alíquota estadual... *[sic — texto consolidado:]* o IBS será cobrado à alíquota estadual de **0,1%** e a CBS à alíquota de **0,9%**. **§1º** O montante recolhido poderá ser **compensado com o PIS e a COFINS** devidos no mesmo período, e, não havendo saldo suficiente, com outros tributos federais ou ressarcido. **§4º** (redação da LC 214) **Fica dispensado o recolhimento** do IBS e da CBS de 2026 pelo contribuinte que **cumprir as obrigações acessórias** previstas na legislação (destaque nos documentos fiscais, escrituração e apuração-teste).

**LC 214, art. 343.** Durante 2026, a CBS incide à alíquota de **0,9%** e o IBS à alíquota de **0,1%** sobre as operações com bens e serviços, observadas as regras de base de cálculo, não incidência e regimes diferenciados desta Lei Complementar; **os valores apurados são informativos para fins de calibragem das alíquotas de referência** e o recolhimento é dispensado nos termos do ADCT.
**Art. 346.** O contribuinte sujeito ao regime regular deve **destacar o IBS e a CBS nos documentos fiscais eletrônicos** e apurar mensalmente os débitos e os **créditos** (aquisições de contribuintes do regime regular com destaque), mesmo durante o período em que o recolhimento esteja dispensado.
**Art. 347.** O optante pelo **Simples Nacional** que não tenha optado pelo regime regular **não está sujeito** ao destaque e à apuração de que trata o art. 346 em 2026; o **MEI** idem. **Aquisições de optante do Simples** geram crédito ao adquirente do regime regular **limitado ao valor efetivamente recolhido** pelo optante a título de IBS/CBS no Simples — em 2026, **sem destaque, não há crédito**.
""", verbatim=False, note="VERIFICAR com o texto oficial da LC 214/2025 e do ADCT art. 125 antes de congelar; a biblioteca é a autoridade do teste, então a redação precisa estar correta.")
    c.library("cgibs_comunicado_03_08_2026.md", "Comitê Gestor do IBS — comunicado sobre obrigatoriedade dos campos a partir de 03/08/2026", "CGIBS, comunicado de julho/2026; NT NF-e 2025.002", f"""
A partir de **3 de agosto de 2026**, **não será permitida a emissão de documentos fiscais eletrônicos (NF-e, NFC-e, NFS-e nacional, CT-e) por contribuintes do regime regular sem o preenchimento dos grupos de IBS e CBS** (grupo `IBSCBS`, com CST, cClassTrib, bases e alíquotas). Documentos sem os grupos serão **rejeitados** (cStat 999/… *rejeição específica*). Documentos emitidos **antes** dessa data sem os grupos permanecem válidos. Durante 2026 não haverá aplicação de penalidades pelo não preenchimento (caráter educativo), **sem prejuízo da perda da dispensa de recolhimento** para quem não cumprir as obrigações acessórias (ADCT art. 125, §4º).
""", verbatim=False, note="Verificar data e teor do comunicado oficial.")
    c.library("nt_nfe_grupo_ibscbs.md", "NT NF-e — leiaute do grupo IBSCBS (resumo)", "NT 2025.002 (resumo técnico)", "Por item: `<IBSCBS><CST/><cClassTrib/><gIBSCBS><vBC/><gIBSUF><pIBSUF/><vIBSUF/></gIBSUF><gIBSMun><pIBSMun/><vIBSMun/></gIBSMun><gCBS><pCBS/><vCBS/></gCBS></gIBSCBS></IBSCBS>`. Em 2026: pIBSUF = 0,10; pIBSMun = 0,00; pCBS = 0,90. Totalizadores no grupo `IBSCBSTot`.", verbatim=False)
    c.library("lei_pis_cofins_compensacao.md", "Compensação do IBS/CBS de 2026 com PIS/COFINS", "ADCT art. 125, §1º; IN RFB (a editar)", "O valor de CBS/IBS eventualmente recolhido em 2026 é compensável com PIS/COFINS do mesmo período. Para quem cumpre as obrigações acessórias, o recolhimento é dispensado e, portanto, nada há a compensar — a apuração é paralela e informativa.", verbatim=False)
    c.contract(f"""
# Engajamento: apuração-teste de CBS/IBS — agosto/{ANO} — Horizonte Comércio e Serviços Ltda.

O gerente fiscal acha que "não precisa fazer nada em 2026". Monte a apuração-teste do mês, a
checagem documento a documento e a orientação. **A biblioteca contém a legislação vigente; use-a,
não a memória.**

## Entregáveis (em `workspace/deliverable/`)
1. `apuracao_teste.json` — `{{"saidas": [{{"numero": 0, "data": "", "valor": 0, "cbs": 0, "ibs": 0, "situacao": "regular|irregular", "motivo": ""}}], "entradas": [{{"numero": 0, "valor": 0, "credito_cbs": 0, "credito_ibs": 0, "motivo": ""}}], "totais": {{"debito_cbs": 0, "debito_ibs": 0, "credito_cbs": 0, "credito_ibs": 0, "saldo_cbs": 0, "saldo_ibs": 0}}, "recolhimento_devido": 0, "condicao_dispensa": ""}}`
2. `orientacao.md` — resposta objetiva ao gerente: o que é devido, o que é dispensado e sob que condição; o que fazer com as notas irregulares; tratamento de clientes do Simples/MEI e de entradas do Simples; o que muda a partir de 03/08.
3. `PERGUNTAS.md` (opcional) e `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Paulo, gerente fiscal; prático; quer resposta objetiva.", [
        {"id": "rejeicao", "trigger": ["rejeição", "rejeitou", "SEFAZ", "cStat", "mensagem"], "answer": "A rejeição dizia: 'Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)'. O TI 'contornou' voltando a versão do emissor.", "if_not_asked": "none"},
        {"id": "ponto_fixo", "trigger": ["Ponto Fixo", "Simples", "crédito de entrada", "fornecedor do Simples"], "answer": "O Ponto Fixo é do Simples, a nota deles veio sem nada de IBS/CBS.", "if_not_asked": "none"},
    ], pushback=[{"when": "se a orientação disser que as notas após 03/08 sem campos são irregulares", "message": "Paulo: Mas a SEFAZ autorizou essas notas (o TI voltou a versão antiga do emissor e passou). Se autorizou, está regular, não?"}])
    deb_cbs = sum(q2(s["valor"] * CBS / 100) for s in saidas)
    deb_ibs = sum(q2(s["valor"] * IBS / 100) for s in saidas)
    cred_cbs = sum(q2(e["valor"] * CBS / 100) for e in entradas if e["grupo"] and e["fornecedor"][2] == "regular")
    cred_ibs = sum(q2(e["valor"] * IBS / 100) for e in entradas if e["grupo"] and e["fornecedor"][2] == "regular")
    irregulares = [s["numero"] for s in saidas if s["data"] >= MARCO and (s["grupo"] is None or s["grupo"]["cbs_aliq"] != "0.90")]
    ref = {"debito_cbs": deb_cbs, "debito_ibs": deb_ibs, "credito_cbs": cred_cbs, "credito_ibs": cred_ibs, "saldo_cbs": deb_cbs - cred_cbs, "saldo_ibs": deb_ibs - cred_ibs,
           "recolhimento_devido": 0, "condicao": "dispensa condicionada ao cumprimento das obrigações acessórias (destaque + apuração); perda da dispensa se descumprir",
           "saidas_irregulares": irregulares, "detalhe": {"sem_campos_apos_marco": [s["numero"] for s in saidas if s["data"] >= MARCO and s["grupo"] is None], "aliquotas_invertidas": [s["numero"] for s in saidas if s["grupo"] and s["grupo"]["cbs_aliq"] != "0.90"]},
           "entradas_sem_credito": [e["numero"] for e in entradas if not (e["grupo"] and e["fornecedor"][2] == "regular")],
           "clientes_simples_mei": "Horizonte (regime regular) DEVE destacar nas suas saídas para qualquer destinatário, inclusive Simples/MEI; o que é dispensado é a obrigação do próprio optante como EMITENTE",
           "pushback": "autorização da SEFAZ via emissor desatualizado não torna o documento conforme à NT; irregular quanto à obrigação acessória → risco de perda da dispensa; corrigir por carta de correção/nota complementar conforme a NT"}
    c.reference("reference.json", ref)
    c.trap(1, "Lei decorada em vez da fornecida", "Raciocinar com PIS/COFINS/ICMS, inventar 'alíquota padrão' (8,8%/17,7%, 26,5%…), ou dizer 'nada a fazer'", "A biblioteca fixa 0,9%/0,1%, apuração paralela obrigatória e dispensa condicionada", "LC 214 arts. 343, 346; ADCT 125", "Porta de confiança", "C", "Biblioteca", "high")
    c.trap(2, "'Dispensado, ponto'", "Recolhimento devido = 0 sem a condição", "Dispensa só para quem cumpre as obrigações acessórias; três notas irregulares põem a dispensa em risco", "ADCT 125 §4º; comunicado CGIBS", "Cliente perde a dispensa", "H", "", "high")
    c.trap(3, "Clientes do Simples/MEI 'não precisa destacar'", "Aceitar a premissa do gerente", "A dispensa do art. 347 é do optante como emitente; Horizonte destaca em todas as saídas", "LC 214 art. 347; e-mail do gerente", "Notas irregulares", "H", "", "high")
    c.trap(4, "Marco de 03/08", f"Tratar as notas {ref['detalhe']['sem_campos_apos_marco']} como regulares (ou as anteriores como irregulares)", "Antes de 03/08 sem campos = válidas; depois = irregulares (pushback: autorização por emissor desatualizado não sana)", "Datas das notas; comunicado", "Rejeições; perda da dispensa", "M", "Comunicado CGIBS", "high")
    c.trap(5, "Alíquotas invertidas", f"Não ver a NF {ref['detalhe']['aliquotas_invertidas']} com CBS 0,1% / IBS 0,9%", "Deve ser apontada e corrigida; os totais da apuração usam as alíquotas corretas", "XML", "Apuração errada", "M", "NT", "high")
    c.trap(6, "Crédito sobre entrada do Simples sem destaque", "Creditar a nota do Ponto Fixo", "Art. 347: sem destaque, sem crédito", "XML sem grupo; script", "Crédito indevido", "M", "LC 214 art. 347", "medium — depende da redação final; biblioteca é a autoridade do teste")
    c.oracle("totais.debito_cbs / debito_ibs", f"{deb_cbs} / {deb_ibs}", "exact", "apuracao_teste.json")
    c.oracle("totais.credito_cbs / credito_ibs", f"{cred_cbs} / {cred_ibs}", "exact", "")
    c.oracle("saidas irregulares", str(irregulares), "exact set", "")
    c.oracle("recolhimento_devido = 0 COM condição de dispensa expressa", "true", "exact", "")
    c.oracle("orientação: destaque obrigatório também para clientes Simples/MEI", "true", "exact", "orientacao.md")
    c.rubric("Pushback: autorização ≠ conformidade; indica como corrigir")
    return c.finish()
