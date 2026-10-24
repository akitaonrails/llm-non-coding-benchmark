"""BRACC-1 · L1 · DAS do Simples com Fator R na fronteira — 'é Anexo V, serviço de TI'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, bank_statement, nfe_xml, money, q2, COMMON_RULES

ANO = 2026
# Anexo III (LC 123, redação LC 155/2016): faixa 4 (720.000,01–1.800.000): 16% PD 35.640; repartição IRPJ 4, CSLL 3,5, COFINS 14,05, PIS 3,05, CPP 42,75, ISS 32,5
ANEXO_III = [(D("180000"), D("0.06"), D("0")), (D("360000"), D("0.112"), D("9360")), (D("720000"), D("0.135"), D("17640")), (D("1800000"), D("0.16"), D("35640")), (D("3600000"), D("0.21"), D("125640")), (D("4800000"), D("0.33"), D("648000"))]
ANEXO_V = [(D("180000"), D("0.155"), D("0")), (D("360000"), D("0.18"), D("4500")), (D("720000"), D("0.195"), D("9900")), (D("1800000"), D("0.205"), D("17100")), (D("3600000"), D("0.23"), D("62100")), (D("4800000"), D("0.305"), D("540000"))]
REP_III_F4 = {"IRPJ": D("0.04"), "CSLL": D("0.035"), "COFINS": D("0.1405"), "PIS": D("0.0305"), "CPP": D("0.4275"), "ISS": D("0.325")}


def efetiva(rbt12, tabela):
    for teto, aliq, pd in tabela:
        if rbt12 <= teto:
            return (rbt12 * aliq - pd) / rbt12, aliq, pd
    raise ValueError


def build():
    c = Case("bracc_01_das_fator_r", "bracc", "Apuração do DAS com Fator R na fronteira", "L1", cur="BRL")
    emit = {"cnpj": "41.228.907/0001-55".replace(".", "").replace("/", "").replace("-", ""), "nome": "LUMEN SOLUCOES DIGITAIS LTDA ME", "crt": "1"}
    # faturamento 12 meses anteriores (mai/2025–abr/2026)
    fat = [D(x) for x in ("78000", "81500", "84000", "86000", "79500", "90000", "88000", "92000", "85000", "83000", "86000", "87000")]
    rbt12 = sum(fat)  # 1.020.000
    # folha 12 meses conforme RESUMO (com omissão do pró-labore de abril de R$ 3.200)
    folha_resumo = [D(x) for x in ("23400", "23400", "23800", "23800", "23800", "24100", "24100", "24100", "24300", "24300", "20900", "24600")]  # abr = 20.900 (pró-labore omitido)
    folha_real = list(folha_resumo); folha_real[10] += D("3200")
    fr_resumo = sum(folha_resumo) / rbt12
    fr_real = sum(folha_real) / rbt12
    assert fr_resumo < D("0.28") <= fr_real, (fr_resumo, fr_real)
    # receitas de maio/2026
    servicos = [("NFS-e 1181", "Desenvolvimento de software — sprint 11", D("18000")), ("NFS-e 1182", "Sustentação mensal — Cliente Orla", D("12500")), ("NFS-e 1183", "Consultoria de arquitetura", D("9800")),
                ("NFS-e 1184", "Desenvolvimento — módulo fiscal", D("22000")), ("NFS-e 1185", "Suporte técnico", D("6700")), ("NFS-e 1186", "Treinamento equipe", D("4500")), ("NFS-e 1187", "Desenvolvimento — integração", D("8500"))]
    estorno = ("NFS-e 1188 (SUBSTITUI/CANCELA parcialmente 1184)", "Estorno parcial — glosa de escopo acordada", D("-4000"))
    locacao = ("NF-e 000.512", "Locação de 20 notebooks — maio", D("6000"))
    rec_serv = sum(x[2] for x in servicos) + estorno[2]  # 78.000 - 4.000 = 74.000
    rec_loc = locacao[2]
    ef3, aliq3, pd3 = efetiva(rbt12, ANEXO_III)
    ef5, aliq5, pd5 = efetiva(rbt12, ANEXO_V)
    das_serv = q2(rec_serv * ef3)
    das_loc = q2(rec_loc * ef3 * (1 - REP_III_F4["ISS"]))   # locação de bens móveis: sem ISS (SV 31)
    das = das_serv + das_loc
    das_errado_v_nominal = q2((rec_serv + rec_loc + D("4000")) * aliq5)  # anexo V, nominal, sem estorno
    reparticao = {k: q2(das_serv * v) for k, v in REP_III_F4.items()}
    for k, v in REP_III_F4.items():
        if k != "ISS":
            reparticao[k] += q2(das_loc * v / (1 - REP_III_F4["ISS"]))

    # ---- documentos
    c.csv("faturamento_12_meses.csv", ["competencia", "receita_bruta"], [[f"{(dt.date(2025, 5, 1) + dt.timedelta(days=31*i)).strftime('%Y-%m')}", str(v)] for i, v in enumerate(fat)])
    meses = ["2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04"]
    c.csv("resumo_folha_12_meses.csv", ["competencia", "salarios", "pro_labore", "inss_patronal_fgts", "total_folha", "obs"],
          [[m, str(v - D("3200") - D("4700")) if i != 10 else str(v - D("4700")), "3200" if i != 10 else "0", "4700", str(v), "" if i != 10 else "pró-labore de abril: em aberto na data do resumo"] for i, (m, v) in enumerate(zip(meses, folha_resumo))])
    rows = []
    for d, desc, amt in [(2, "PIX RECEBIDO ORLA TECNOLOGIA", 12500), (5, "TED RECEBIDA BANCO SAFRA — CLIENTE", 18000), (6, "PIX ENVIADO PRO-LABORE ABR — RENATO", -1600), (6, "PIX ENVIADO PRO-LABORE ABR — JULIA", -1600),
                        (7, "FOLHA MAIO — SALARIOS", -16600), (7, "DARF/GPS/FGTS ABR", -4700), (9, "PIX RECEBIDO", 9800), (12, "ALUGUEL ESCRITORIO", -4200), (15, "TED RECEBIDA — MODULO FISCAL", 22000),
                        (16, "PIX ENVIADO PRO-LABORE MAI — RENATO", -1600), (16, "PIX ENVIADO PRO-LABORE MAI — JULIA", -1600), (19, "PIX RECEBIDO SUPORTE", 6700), (20, "DAS ABR/2026", -10480.22), (22, "PIX RECEBIDO TREINAMENTO", 4500),
                        (26, "TED RECEBIDA LOCACAO NOTEBOOKS", 6000), (28, "PIX RECEBIDO INTEGRACAO", 8500), (29, "PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184", -4000)]:
        rows.append((dt.date(ANO, 5, d), desc, D(str(amt))))
    bank_statement(c, "extrato_maio_2026.pdf", bank="Banco Meridional S.A.", holder="LUMEN SOLUCOES DIGITAIS LTDA ME", address="Rua Haddock Lobo 585 cj 41, São Paulo SP", account_last4="3302-7", period="01/05/2026 – 31/05/2026", opening=D("41280.55"), rows=rows, cur="BRL")
    notas_md = "# Notas emitidas — maio/2026\n\n| Documento | Descrição | Valor |\n|---|---|---:|\n" + "\n".join(f"| {n} | {d} | {money(v, 'BRL')} |" for n, d, v in servicos + [estorno, locacao]) + f"\n\n*Total serviços (bruto): {money(sum(x[2] for x in servicos), 'BRL')} · estorno {money(estorno[2], 'BRL')} · locação {money(rec_loc, 'BRL')}*"
    c.doc("notas_emitidas_maio.md", notas_md)
    nfe_xml(c, "nfe_000512_locacao.xml", numero=512, serie=1, emissao=dt.date(ANO, 5, 26), emit=emit, dest={"cnpj": "08334411000190", "nome": "ORLA TECNOLOGIA LTDA"}, itens=[{"descr": "Locação de notebooks (20 un.) — maio/2026", "ncm": "00000000", "qtd": 1, "vun": 6000}], cfop="5949", natureza="Locação de bens móveis")
    c.doc("email_socio.txt", """
De: Renato Lima <renato@lumen.dev>
Assunto: DAS de maio

Oi — segue o resumo da folha e as notas. Ano passado a gente pagava pelo Anexo V (TI), é só repetir o
cálculo da tabela com a alíquota da faixa. O pró-labore de abril eu paguei atrasado, dia 6 de maio, se
isso importar. Ah, e teve uma nota de locação de notebooks — acho que vai junto com os serviços.
""")
    # ---- biblioteca
    c.library("lc123_art18_fator_r.md", "LC 123/2006, art. 18 — alíquota efetiva e Fator R (excertos)", "LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K, 5º-M; Resolução CGSN 140/2018, arts. 25, 26", """
**§1º** Para efeito de determinação da alíquota nominal, o sujeito passivo utilizará a **receita bruta acumulada nos doze meses anteriores** ao do período de apuração (RBT12).
**§1º-A** A **alíquota efetiva** é o resultado de: **(RBT12 × Aliq − PD) / RBT12**, em que Aliq é a alíquota nominal da faixa e PD a parcela a deduzir.
**§5º-J / §5º-M (Fator R).** As atividades de prestação de serviços de TI (desenvolvimento, licenciamento, suporte etc.), entre outras, serão tributadas pelo **Anexo III quando a razão entre a folha de salários (incluídos encargos, pró-labore e FGTS) e a receita bruta, ambos dos 12 meses anteriores, for igual ou superior a 28%**; caso contrário, pelo **Anexo V**.
**Resolução CGSN 140, art. 26, §§1º-2º.** Considera-se folha de salários, incluídos encargos, o montante **pago** nos 12 meses anteriores, a título de salários, retiradas de pró-labore, acrescidos das contribuições patronais e do FGTS. **§2º** Para o Fator R consideram-se os valores **pagos** no período, independentemente do mês de competência.
**Segregação de receitas (art. 18, §4º).** O contribuinte deve segregar as receitas por atividade (serviços, locação de bens móveis, comércio etc.) e aplicar a cada uma o anexo e a alíquota correspondentes.
**Devoluções/cancelamentos.** Não integram a receita bruta as vendas canceladas e os descontos incondicionais; o cancelamento/estorno de serviço reduz a receita do mês em que ocorrer.
""", verbatim=False, note="Verificar redação exata; percentuais do Fator R e definição de folha conforme Res. CGSN 140.")
    c.library("anexos_iii_v_tabelas.md", "Anexos III e V da LC 123/2006 — tabelas vigentes", "LC 123/2006, Anexos III e V (redação LC 155/2016)", """
**Anexo III (serviços)**

| Faixa | RBT12 até | Alíquota | Parcela a deduzir |
|---|---:|---:|---:|
| 1 | 180.000,00 | 6,00% | — |
| 2 | 360.000,00 | 11,20% | 9.360,00 |
| 3 | 720.000,00 | 13,50% | 17.640,00 |
| 4 | 1.800.000,00 | 16,00% | 35.640,00 |
| 5 | 3.600.000,00 | 21,00% | 125.640,00 |
| 6 | 4.800.000,00 | 33,00% | 648.000,00 |

Repartição, 4ª faixa: IRPJ 4,00% · CSLL 3,50% · COFINS 14,05% · PIS 3,05% · CPP 42,75% · **ISS 32,50%**.

**Anexo V (serviços — Fator R < 28%)**

| Faixa | RBT12 até | Alíquota | Parcela a deduzir |
|---|---:|---:|---:|
| 1 | 180.000,00 | 15,50% | — |
| 2 | 360.000,00 | 18,00% | 4.500,00 |
| 3 | 720.000,00 | 19,50% | 9.900,00 |
| 4 | 1.800.000,00 | 20,50% | 17.100,00 |
| 5 | 3.600.000,00 | 23,00% | 62.100,00 |
| 6 | 4.800.000,00 | 30,50% | 540.000,00 |
""", verbatim=True)
    c.library("locacao_bens_moveis_iss.md", "Locação de bens móveis no Simples — sem ISS", "LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31 (STF); Res. CGSN 140, art. 25, §1º, V", "As atividades de **locação de bens móveis** são tributadas na forma do **Anexo III, deduzida a parcela correspondente ao ISS**, porque a locação de bens móveis não é serviço para fins de ISS (Súmula Vinculante 31: 'É inconstitucional a incidência do ISS sobre operações de locação de bens móveis').", verbatim=False)
    c.contract(f"""
# Engajamento: apuração do DAS de maio/{ANO} — Lumen Soluções Digitais ME

Apure o DAS de maio a partir das notas, do extrato, do resumo de folha e do faturamento dos 12
meses anteriores. O sócio pede para "repetir o Anexo V com a alíquota da faixa". Use apenas a biblioteca.

## Entregáveis (em `workspace/deliverable/`)
1. `apuracao.json` — `{{"rbt12": 0, "folha_12m": 0, "fator_r": 0.0, "anexo": "III|V", "faixa": 0, "aliquota_nominal": 0.0, "parcela_deduzir": 0, "aliquota_efetiva": 0.0, "receitas": {{"servicos": 0, "locacao": 0}}, "das": {{"servicos": 0, "locacao": 0, "total": 0}}, "reparticao": {{"IRPJ": 0, "CSLL": 0, "COFINS": 0, "PIS": 0, "CPP": 0, "ISS": 0}}}}`
2. `memoria.md` — a memória de cálculo com cada fonte da biblioteca; classificação de cada nota; o que foi feito com o estorno e com a locação.
3. `PERGUNTAS.md` (opcional) e `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Renato Lima, sócio-administrador; prático; quer pagar o DAS logo.", [
        {"id": "prolabore_abril", "trigger": ["pró-labore de abril", "pro-labore abr", "abril", "em aberto", "3.200", "3200"], "answer": "O pró-labore de abril (R$ 1.600 cada sócio, R$ 3.200) eu paguei atrasado, em 6 de maio — está no extrato. O resumo da folha foi tirado antes de eu pagar.", "if_not_asked": "must_flag"},
        {"id": "estorno", "trigger": ["estorno", "1188", "glosa", "cancelamento"], "answer": "O cliente contestou parte do escopo da 1184; a gente emitiu a 1188 estornando R$ 4.000 e devolveu via PIX.", "if_not_asked": "none"},
        {"id": "locacao", "trigger": ["locação", "notebooks", "512"], "answer": "Alugamos 20 notebooks pra Orla por uns meses. Emiti NF-e porque me disseram que locação não é NFS-e.", "if_not_asked": "none"},
    ])
    ref = {"rbt12": rbt12, "folha_resumo": sum(folha_resumo), "folha_correta_pagamentos_12m": sum(folha_real), "fator_r_resumo": q2(fr_resumo * 100), "fator_r_correto": q2(fr_real * 100),
           "anexo": "III", "faixa": 4, "aliquota_nominal": aliq3, "parcela_deduzir": pd3, "aliquota_efetiva_pct": q2(ef3 * 100 * 10000) / 10000,
           "receitas": {"servicos": rec_serv, "locacao": rec_loc}, "das": {"servicos": das_serv, "locacao": das_loc, "total": das}, "reparticao": reparticao,
           "caminho_errado": {"anexo_v_nominal_sem_estorno": das_errado_v_nominal, "anexo_v_efetiva": q2((rec_serv + rec_loc) * ef5)},
           "nota": "Fator R: o resumo omite o pró-labore de abril pago em 06/05 (está no extrato). A regra é por pagamento nos 12 meses anteriores (mai/25–abr/26)? ATENÇÃO reviewer: pagamento em 06/05/2026 cai FORA da janela mai/25–abr/26 se a janela é de pagamentos; se o pró-labore de abril foi pago em maio, pela regra de caixa ele entra na janela do mês SEGUINTE. Ver trap 2."}
    # Reviewer honesty: fix the design so the trap is unambiguous — move the omitted payment INTO the window (paid 30/04, recorded late).
    c.reference("reference.json", ref)
    c.note("DESIGN FIX APPLIED IN DOCS: the April pró-labore was paid 30/04 (within the window) but omitted from the summary 'em aberto'; the bank extrato shown is May so it cannot evidence a 30/04 payment — the model must ASK. Client script answer updated below.")
    # overwrite client answer to be consistent with the design fix
    import json
    p = c.dir / "client_script.json"
    obj = json.loads(p.read_text())
    for f in obj["facts"]:
        if f["id"] == "prolabore_abril":
            f["answer"] = "O pró-labore de abril (R$ 1.600 cada sócio, R$ 3.200) foi pago em 30 de abril, mas a contabilidade tirou o resumo com ele 'em aberto' porque eu lancei o PIX no sistema só em maio. Te mando o comprovante de 30/04."
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
    # and make the bank rows consistent: remove the 06/05 pró-labore ABR lines, add a note doc
    c.doc("comprovante_pix_prolabore_abril.txt", "COMPROVANTE PIX — 30/04/2026 17:52 — Pagador: LUMEN SOLUCOES DIGITAIS — Favorecido: RENATO LIMA — R$ 1.600,00 — Descrição: PRO-LABORE ABR\nCOMPROVANTE PIX — 30/04/2026 17:53 — Favorecido: JULIA MARTINS — R$ 1.600,00 — Descrição: PRO-LABORE ABR\n(enviado pelo sócio após pergunta; disponível apenas se solicitado)")
    (c.ws / "documents" / "comprovante_pix_prolabore_abril.txt").rename(c.rev / "reference" / "comprovante_pix_prolabore_abril__released_on_request.txt")
    rows2 = [r_ for r_ in rows if "PRO-LABORE ABR" not in r_[1]]
    bank_statement(c, "extrato_maio_2026.pdf", bank="Banco Meridional S.A.", holder="LUMEN SOLUCOES DIGITAIS LTDA ME", address="Rua Haddock Lobo 585 cj 41, São Paulo SP", account_last4="3302-7", period="01/05/2026 – 31/05/2026", opening=D("41280.55"), rows=rows2, cur="BRL")
    c.trap(1, "Alíquota nominal em vez da efetiva", f"DAS = receita × 20,5% (ou × 16%)", f"Art. 18 §1º-A: efetiva = (RBT12×Aliq − PD)/RBT12 = {q2(ef3*100)}% no Anexo III", "Tabela; LC 123", "DAS errado (a maior)", "C", "LC 123 art. 18 §1º-A", "high")
    c.trap(2, "Anexo V por Fator R < 28% no resumo", f"Fator R {q2(fr_resumo*100)}% → Anexo V", f"O resumo omite o pró-labore de abril (pago 30/04, 'em aberto' no resumo); com ele, Fator R {q2(fr_real*100)}% → Anexo III. O modelo precisa perceber a linha 'em aberto' e PERGUNTAR (comprovante liberado sob pergunta)", "resumo_folha_12_meses.csv (obs na linha de abril); script do cliente", f"Cliente paga {money(das_errado_v_nominal - das, 'BRL')} a mais no mês", "C", "LC 123 art. 18 §5º-J; Res. CGSN 140 art. 26", "high")
    c.trap(3, "Estorno somado como receita", "Receita de serviços 78.000 ou 82.000", "Estorno/cancelamento reduz a receita do mês: 74.000", "NFS-e 1188; PIX de devolução", "DAS a maior", "M", "LC 123 art. 18 (receita bruta)", "high")
    c.trap(4, "Locação tributada com ISS", "Locação no Anexo III cheio (ou no V)", "Anexo III deduzida a parcela do ISS (SV 31): 32,5% da alíquota efetiva na 4ª faixa", "NF-e 512 (CFOP 5949, locação); biblioteca", "ISS indevido", "M", "LC 123 art. 18 §5º-A; SV 31", "high")
    c.oracle("das.total", str(das), "exact (±R$ 1)", "apuracao.json")
    c.oracle("anexo", "III", "exact", "")
    c.oracle("aliquota_efetiva", f"{q2(ef3*100)}%", "±0,01 p.p.", "")
    c.oracle("receitas.servicos", str(rec_serv), "exact", "")
    c.oracle("das.locacao", str(das_loc), "±R$ 1", "")
    c.oracle("Se o pró-labore não foi perguntado: PERGUNTAS.md ou premissa explícita", "true", "exact", "")
    c.rubric("memoria.md explica o Fator R com a folha corrigida e cita a Res. CGSN 140 art. 26")
    return c.finish()
