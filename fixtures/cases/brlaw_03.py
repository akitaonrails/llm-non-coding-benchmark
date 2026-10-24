"""BRLAW-3 · L3 · Pejotização — 'o STF liberou a terceirização, não há vínculo'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

INICIO = dt.date(2019, 10, 1)
FIM = dt.date(2026, 9, 30)          # notificação; contrato encerrado
AJUIZAMENTO = dt.date(2026, 11, 16)  # data provável da reclamação (e-mail)
VALOR_PJ = D("18000")


def build():
    c = Case("brlaw_03_pejotizacao", "brlaw", "Parecer trabalhista: risco de vínculo (pejotização), exposição e prescrição", "L3", cur="BRL")
    meses_total = (FIM.year - INICIO.year) * 12 + FIM.month - INICIO.month + 1  # 84
    corte = dt.date(AJUIZAMENTO.year - 5, AJUIZAMENTO.month, AJUIZAMENTO.day)      # 2021-11-16
    meses_prescritos = (corte.year - INICIO.year) * 12 + corte.month - INICIO.month  # out/2019..out/2021 → 25 meses (nov/21 parcial — simplificar: 25)
    meses_exigiveis = meses_total - meses_prescritos   # 59
    anos_exigiveis = D(meses_exigiveis) / 12
    # exposição (remuneração = valor da NF, premissa de referência)
    decimo = q2(VALOR_PJ * anos_exigiveis)
    ferias_terco = q2(VALOR_PJ * anos_exigiveis * D("4") / 3)
    base_fgts = VALOR_PJ * meses_exigiveis + decimo + ferias_terco
    fgts = q2(base_fgts * D("0.08"))
    multa_40 = q2(fgts * D("0.40"))
    aviso = q2(VALOR_PJ / 30 * (30 + 3 * 7))  # 51 dias (7 anos completos; aviso proporcional considera tempo total, não prescrito)
    inss_patronal = q2((VALOR_PJ * meses_exigiveis + decimo + ferias_terco) * D("0.28"))
    exposicao = decimo + ferias_terco + fgts + multa_40 + aviso + inss_patronal
    exposicao_84m_errada = q2(exposicao * D(meses_total) / D(meses_exigiveis))
    fgts_sem_13_ferias = q2(VALOR_PJ * meses_exigiveis * D("0.08"))

    c.doc_pdf("contrato_prestacao_servicos_pj.pdf", f"""
# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE DESENVOLVIMENTO DE SOFTWARE
**CONTRATANTE:** Solaris Tecnologia Ltda. · **CONTRATADA:** R.M. Desenvolvimento de Sistemas Ltda. (sócio único: Rafael Moreira) · **Início:** {INICIO:%d/%m/%Y}
1. Objeto: desenvolvimento e manutenção de sistemas conforme demandas da CONTRATANTE. 2. Remuneração: **R$ {VALOR_PJ:,.2f} mensais** contra nota fiscal, independentemente de entregas. 3. **Exclusividade:** a CONTRATADA não prestará serviços a terceiros durante a vigência. 4. **Horário:** a CONTRATADA disponibilizará seu sócio de segunda a sexta, das 9h às 18h, **nas dependências da CONTRATANTE ou em home office autorizado pelo gestor**. 5. A CONTRATADA reportar-se-á ao Gerente de Engenharia. 6. Férias: 20 dias por ano, a combinar. 7. Prazo indeterminado; rescisão com 30 dias.
""".replace(",", "X").replace(".", ",").replace("X", "."))
    c.doc("prints_mensagens.txt", """
[Slack #eng — 2024-03-12 09:04] Gerente (Carla): @rafael bom dia, vi que você logou 9h20. Lembra que o combinado é 9h. Marca no planilha de ponto.
[Slack DM — 2025-06-02] Carla: Rafael, preciso que você fique até 20h hoje e amanhã, release. — Rafael: ok.
[Slack DM — 2025-08-19] Rafael: posso tirar 3 dias semana que vem? — Carla: só se o Pedro cobrir. Me manda o pedido por email pro RH aprovar.
[E-mail RH — 2025-08-20] Assunto: Aprovação de ausência — Rafael Moreira (PJ) — aprovado, descontar do saldo de 20 dias.
[Slack #eng — 2026-01-05] Carla: avaliação de desempenho dos PJs semana que vem, mesmo formulário dos CLTs.
""")
    c.doc("escala_e_planilha_ponto.csv", "mes,dias_trabalhados,horas_medias_dia,horas_extras_registradas\n2025-01,21,9.1,18\n2025-02,19,9.3,22\n2025-03,21,9.0,15\n2025-04,20,9.4,26\n2025-05,21,9.2,20\n2025-06,21,9.8,34\n")
    c.doc("notificacao_e_email_diretoria.txt", f"""
[Notificação extrajudicial — {FIM:%d/%m/%Y}] Rafael Moreira, por advogado, comunica o encerramento da prestação e informa que ajuizará reclamação trabalhista pleiteando o reconhecimento de vínculo desde {INICIO:%d/%m/%Y}, com todas as verbas. Protocolo previsto para **{AJUIZAMENTO:%d/%m/%Y}**.

[E-mail — Diretor de Operações → jurídico] "O STF já liberou a terceirização e a pejotização (aquele Tema 725). Ele é PJ, assinou contrato, emitiu nota por 7 anos. Risco zero. Não vamos provisionar nada e não aceito acordo."
""")
    c.doc("notas_fiscais_resumo.csv", "ano,qtd_nf,valor_total\n2019,3,54000\n2020,12,216000\n2021,12,216000\n2022,12,216000\n2023,12,216000\n2024,12,216000\n2025,12,216000\n2026,9,162000\n")
    L = c.library
    L("clt_requisitos_vinculo.md", "CLT — arts. 2º, 3º, 9º, 442-B, 818", "CLT arts. 2º, 3º, 9º, 442-B, 818", "**Art. 3º.** Considera-se empregado toda pessoa física que prestar serviços de natureza **não eventual** a empregador, sob a **dependência** deste e mediante **salário**. (Requisitos: pessoalidade, não eventualidade, onerosidade, **subordinação**.) **Art. 9º.** Serão nulos de pleno direito os atos praticados com o objetivo de desvirtuar, impedir ou fraudar a aplicação dos preceitos desta Consolidação. **Art. 442-B.** A contratação do autônomo, cumpridas as formalidades legais, **com ou sem exclusividade**, de forma contínua ou não, afasta a qualidade de empregado — **desde que ausente a subordinação** (interpretação do TST/doutrina). **Art. 818.** Ônus da prova: ao reclamante quanto ao fato constitutivo; ao reclamado quanto ao fato impeditivo (a prestação de serviços admitida inverte o ônus de provar a autonomia).", verbatim=False)
    L("cf_art7_xxix_prescricao.md", "CF art. 7º, XXIX — prescrição trabalhista", "CF art. 7º, XXIX; CLT art. 11; Súmula 308 TST", "Ação quanto aos créditos resultantes das relações de trabalho, com prazo prescricional de **cinco anos** para os trabalhadores urbanos e rurais, **até o limite de dois anos após a extinção do contrato**. Súmula 308 TST: a prescrição quinquenal abrange os créditos anteriores aos cinco anos contados **da data do ajuizamento**. O FGTS segue a mesma prescrição quinquenal (STF ARE 709.212, Tema 608, com modulação). O **aviso-prévio proporcional** considera o tempo total de serviço (Lei 12.506/2011), ainda que parte das verbas esteja prescrita.", verbatim=False)
    L("stf_tema_725_adc48_adpf324.md", "STF — Tema 725, ADPF 324, ADC 48 (terceirização lícita)", "STF RE 958.252 (Tema 725, 2018); ADPF 324; ADC 48 (2020)", "Tese do Tema 725: 'É lícita a terceirização ou qualquer outra forma de divisão do trabalho entre pessoas jurídicas distintas, independentemente do objeto social das empresas envolvidas, mantida a responsabilidade subsidiária da empresa contratante.' A tese trata da **licitude da terceirização entre pessoas jurídicas**; **não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)** — o que a própria jurisprudência do STF em reclamações passou a discutir caso a caso. ADC 48: constitucionalidade da contratação de transportador autônomo (Lei 11.442).", kind="jurisprudência", verbatim=False)
    L("stf_tema_1389_pejotizacao.md", "STF — Tema 1.389 (ARE 1.532.603) — pejotização: repercussão geral e suspensão nacional", "STF, ARE 1.532.603/DF, rel. Min. Gilmar Mendes — repercussão geral reconhecida (abril/2025); decisão de **suspensão nacional** dos processos (14/04/2025)", "Questões submetidas: (i) licitude da contratação de pessoa jurídica ou trabalhador autônomo para prestação de serviços (pejotização), (ii) competência da Justiça do Trabalho, (iii) ônus da prova da fraude. **O relator determinou a suspensão nacional de todos os processos que tratem da licitude da contratação de PJ/autônomo**, até o julgamento de mérito. **Situação nesta biblioteca (congelada em out/2026): mérito pendente; suspensão mantida.** Efeito prático: reclamação ajuizada agora tende a ser **sobrestada** após a fase de instrução/antes da sentença conforme a prática de cada TRT; a exposição não desaparece — fica em aberto, com juros e correção correndo (Lei 14.905/2024: IPCA + SELIC-IPCA), e a decisão de mérito do STF poderá fixar tese sobre ônus da prova e critérios.", kind="jurisprudência", verbatim=False, note="Verificar o estágio real do Tema 1.389 na data de congelamento; a biblioteca é a autoridade do teste.")
    L("tst_sumulas_ojs.md", "TST — súmulas e OJs pertinentes (com status)", "Súmulas 331, 212, 338, 363; OJ SDI-1 nº 383; **OJ SDI-1 nº 191 (CANCELADA)**; **Súmula 256 (CANCELADA)**", "**Súmula 331** (terceirização; itens I, III, IV — responsabilidade subsidiária). **Súmula 212** (ônus da prova do término do contrato é do empregador). **Súmula 338** (controle de jornada; presunção com mais de 20 empregados). **Súmula 363** (contratação irregular pela administração pública — não aplicável). **OJ 383 SDI-1** (isonomia salarial em terceirização ilícita). **Súmula 256 — CANCELADA pela Res. 121/2003** (vedava a terceirização salvo trabalho temporário/vigilância — superada pela Súmula 331). **OJ SDI-1 nº 191 — CANCELADA/convertida (dono da obra) — não se aplica.** Citar a Súmula 256 ou a OJ 191 como vigentes é erro.", kind="jurisprudência", verbatim=False, planted="superseded", note="Súmula 256 e OJ 191 constam com status CANCELADA; usá-las como fundamento é falha.")
    L("verbas_e_calculo.md", "Verbas na reversão da pejotização — parâmetros de cálculo", "CLT arts. 457, 477, 487; Lei 8.036/90 arts. 15 e 18; Lei 8.212/91 art. 22; Lei 12.506/2011; Súmula 437 TST", "Reconhecido o vínculo, devem-se: anotação da CTPS; **13º salário** (1/12 por mês); **férias + 1/3** (dobradas se não concedidas no período concessivo — TST, Súmula 450/81; para simplificação desta tarefa, considerar simples); **FGTS de 8% sobre salário, 13º e férias gozadas/indenizadas (incide sobre 13º e férias; não incide sobre o terço? — incide sobre férias gozadas + 1/3; não sobre férias indenizadas)** — **para esta tarefa: FGTS sobre salários + 13º + férias com 1/3**; **multa de 40%** sobre o FGTS; **aviso-prévio proporcional** (30 dias + 3 por ano completo, máx. 90 — Lei 12.506); **INSS patronal** (20% + RAT + terceiros ≈ 28%) sobre a remuneração reconhecida (débito da empresa, exigível pela RFB); horas extras conforme prova (planilha). **Remuneração-base:** o valor pago à PJ (presunção usual na Justiça do Trabalho, salvo prova de que embutia tributos/custos — argumento de defesa).", verbatim=False, note="Simplificações declaradas: FGTS sobre férias+1/3; férias simples.")
    L("multa_477_e_honorarios.md", "Multas e honorários", "CLT arts. 467, 477 §8º, 791-A", "Multa do art. 477 §8º (um salário) e do art. 467 (50% sobre verbas incontroversas) — discutíveis na reversão de pejotização; honorários sucumbenciais 5–15% (art. 791-A).", verbatim=False)
    c.contract(f"""
# Engajamento: parecer — Solaris Tecnologia × Rafael Moreira (R.M. Desenvolvimento)

A diretoria considera "risco zero" por causa do Tema 725 e não quer provisionar. Dê o parecer com números.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.json` — `{{"probabilidade_vinculo": "baixa|media|alta (faixa %)", "fundamentos": ["..."], "prescricao": {{"data_ajuizamento": "", "corte_quinquenal": "", "meses_exigiveis": 0, "meses_prescritos": 0}}, "exposicao": {{"remuneracao_base": 0, "decimo_terceiro": 0, "ferias_terco": 0, "fgts": 0, "multa_40": 0, "aviso_previo": 0, "inss_patronal": 0, "horas_extras": "estimativa/a apurar", "total": 0}}, "tema_1389": {{"efeito_processual": "", "efeito_na_exposicao": ""}}, "provisao_recomendada": {{"classificacao_cpc25": "provavel|possivel|remota", "valor": 0}}, "acordo": {{"recomendado": true/false, "faixa": [0, 0]}}}}`
2. `parecer.md` — análise dos requisitos do art. 3º com as provas do arquivo; por que o Tema 725 não resolve; Tema 1389; prescrição; cálculo; estratégia; **sem usar súmulas/OJs canceladas**.
3. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Diretor de Operações (convicto do 'risco zero'); gerente Carla (cooperativa).", [
        {"id": "outros_clientes", "trigger": ["outros clientes", "exclusiv", "prestava para terceiros"], "answer": "Carla: Não. Ele era dedicado a nós, 7 anos. A PJ dele só tinha a gente.", "if_not_asked": "none"},
        {"id": "quem_decidia", "trigger": ["quem decidia", "férias", "horário", "aprovava", "subordina"], "answer": "Carla: Eu. Aprovava férias, cobrava horário, dava feedback. Igual aos CLTs.", "if_not_asked": "none"},
        {"id": "valor_embutia", "trigger": ["embutia", "tributos", "custo", "valor da nota", "remuneração-base"], "answer": "Diretor: Os 18 mil eram 'cheios' justamente porque ele era PJ. Um CLT equivalente ganharia uns 12 mil.", "if_not_asked": "none"},
    ], pushback=[{"when": "se o parecer classificar o risco como provável/alta", "message": "Diretor: O STF decidiu que pejotização é lícita, está em todo jornal. E o processo vai ficar parado por causa dessa suspensão — então não tem risco agora. Por que provisionar?"}])
    ref = {"probabilidade_vinculo": "alta (70–85%)", "fundamentos": ["subordinação: horário controlado, ponto, aprovação de ausências pelo RH, avaliação de desempenho com formulário de CLT", "pessoalidade: sócio único, dedicado", "não eventualidade: 7 anos", "onerosidade: valor fixo mensal independente de entregas", "exclusividade (indício, não decisivo — 442-B)", "fraude (art. 9º)"],
           "prescricao": {"data_ajuizamento": AJUIZAMENTO.isoformat(), "corte_quinquenal": corte.isoformat(), "meses_total": meses_total, "meses_prescritos": meses_prescritos, "meses_exigiveis": meses_exigiveis, "bienal": "ok — ajuizamento dentro de 2 anos do término"},
           "exposicao": {"remuneracao_base": VALOR_PJ, "decimo_terceiro": decimo, "ferias_terco": ferias_terco, "fgts": fgts, "multa_40": multa_40, "aviso_previo": aviso, "inss_patronal": inss_patronal, "total": exposicao, "nota": "horas extras adicionais conforme planilha (≈ 20h/mês) a apurar; juros/correção; honorários"},
           "caminho_errado": {"84_meses_sem_prescricao": exposicao_84m_errada, "fgts_sem_13_ferias": fgts_sem_13_ferias},
           "tema_1389": {"efeito_processual": "sobrestamento provável após instrução; não extingue nem reduz o passivo", "efeito_na_exposicao": "mantém-se; correção/juros correm (Lei 14.905/2024)"},
           "provisao": {"classificacao_cpc25": "provavel", "valor": exposicao, "nota": "CPC 25: provável → provisionar; o sobrestamento não altera a probabilidade de perda"},
           "acordo": {"recomendado": True, "faixa": [q2(exposicao * D("0.35")), q2(exposicao * D("0.55"))], "argumentos_de_defesa": ["remuneração-base: R$ 12 mil (CLT equivalente) em vez de R$ 18 mil — reduz ~1/3", "exclusividade não decisiva (442-B)", "Tema 1389 pode fixar ônus da prova favorável"]}}
    c.reference("reference.json", ref)
    c.trap(1, "Tema 725 = risco zero", "Probabilidade baixa; sem provisão", "Tema 725 trata de terceirização entre PJs; com subordinação provada (ponto, aprovação de férias pelo RH, avaliação), art. 3º + art. 9º → vínculo provável; Tema 1389 pendente com suspensão NÃO reduz a exposição (pushback)", "Prints; e-mail RH; planilha; biblioteca", "Passivo não provisionado; demonstrações erradas; acordo recusado", "C", "CLT 3º, 9º; Tema 725; Tema 1389", "high")
    c.trap(2, "Súmula/OJ cancelada", "Citar Súmula 256 ou OJ 191 como vigentes", "Status CANCELADA na biblioteca", "tst_sumulas_ojs.md", "Fundamento inexistente", "C", "", "high")
    c.trap(3, "Exposição de 84 meses", f"{money(exposicao_84m_errada, 'BRL')}", f"Prescrição quinquenal da data do ajuizamento ({AJUIZAMENTO}) → corte {corte}: {meses_exigiveis} meses exigíveis → {money(exposicao, 'BRL')}", "Notificação (data prevista)", "Exposição superestimada; acordo mal calibrado", "H", "CF 7º XXIX; Súmula 308", "high")
    c.trap(4, "FGTS só sobre salários", f"{money(fgts_sem_13_ferias, 'BRL')}", f"Incide também sobre 13º e férias: {money(fgts, 'BRL')}", "Biblioteca (parâmetros)", "Exposição a menor", "M", "Lei 8.036", "high")
    c.trap(5, "Exclusividade como prova decisiva", "Fundar o parecer na exclusividade", "442-B: exclusividade não caracteriza; o peso está na subordinação", "CLT 442-B", "Peso errado", "M", "", "high")
    c.oracle("prescricao.meses_exigiveis", str(meses_exigiveis), "±1", "parecer.json")
    c.oracle("exposicao.total", str(exposicao), "±3% (com remuneração-base 18.000; se usar 12.000, aceitar recomputo com método declarado)", "")
    c.oracle("probabilidade_vinculo = alta", "true", "exact", "")
    c.oracle("provisao.classificacao_cpc25 = provavel", "true", "exact", "")
    c.oracle("Nenhuma citação à Súmula 256 ou OJ 191 como vigentes", "true", "exact", "parecer.md")
    c.oracle("tema_1389 mencionado com efeito processual (suspensão) e sem redução de exposição", "true", "exact", "")
    c.rubric("Pushback respondido: suspensão ≠ ausência de risco; CPC 25")
    return c.finish()
