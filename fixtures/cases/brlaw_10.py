"""BRLAW-10 · L3 · Cobrança de dívida antiga — 'executa e negativa'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

HOJE = dt.date(2026, 10, 12)
RECONHECIMENTO = dt.date(2022, 9, 15)   # e-mail reconhecendo parcelas 1-4
PAGAMENTO_PARCIAL = dt.date(2023, 8, 2)  # R$ 10.000 sobre a parcela 1


def build():
    c = Case("brlaw_10_cobranca_prescrita", "brlaw", "Cobrança de dívida antiga: via processual, prescrição parcela a parcela, negativação", "L3", cur="BRL")
    boletos = [(1, dt.date(2020, 10, 10)), (2, dt.date(2020, 11, 10)), (3, dt.date(2020, 12, 10)), (4, dt.date(2021, 1, 10)), (5, dt.date(2021, 2, 10)), (6, dt.date(2021, 3, 10))]
    valor = D("30000")
    analise = []
    for n, venc in boletos:
        prazo_original = venc.replace(year=venc.year + 5)
        if n <= 4:  # reconhecidas no e-mail → interrupção única em 15/09/2022, recomeça do zero
            novo = RECONHECIMENTO.replace(year=RECONHECIMENTO.year + 5)
            prescrita = HOJE > novo
            analise.append(dict(parcela=n, vencimento=venc.isoformat(), prazo_original=prazo_original.isoformat(), interrompida_em=RECONHECIMENTO.isoformat(), novo_termo=novo.isoformat(), prescrita=prescrita, nota="pagamento parcial de 02/08/2023 NÃO interrompe de novo (CC 202 caput: uma única vez)" if n == 1 else ""))
        else:
            prescrita = HOJE > prazo_original
            analise.append(dict(parcela=n, vencimento=venc.isoformat(), prazo_original=prazo_original.isoformat(), interrompida_em=None, novo_termo=prazo_original.isoformat(), prescrita=prescrita, nota="não reconhecida no e-mail (contestada)"))
    exigivel = sum(valor for a in analise if not a["prescrita"]) - D("10000")
    prescrito = sum(valor for a in analise if a["prescrita"])
    c.doc("contrato_prestacao_servicos.md", "# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE MANUTENÇÃO INDUSTRIAL — Técnica Forte Ltda. (contratada) × Metalúrgica Boa Vista Ltda. (contratante)\nAssinado em 01/09/2020. Preço: 6 parcelas mensais de R$ 30.000,00, vencíveis todo dia 10, de outubro/2020 a março/2021, mediante boleto. Multa 2%, juros 1% a.m., correção IPCA. Foro: Comarca de Sorocaba/SP.\n**Assinaturas:** representante da contratada; representante da contratante. **Sem testemunhas.**")
    c.doc("boletos_e_comprovantes.csv", "parcela,vencimento,valor,comprovante_execucao_servico\n" + "\n".join(f"{n},{v.isoformat()},30000,relatório de serviço assinado pelo encarregado da Boa Vista" for n, v in boletos))
    c.doc("emails_reconhecimento.txt", f"""
De: financeiro@boavista (Metalúrgica Boa Vista) Para: cobranca@tecnicaforte Data: {RECONHECIMENTO:%d/%m/%Y}
Assunto: RE: parcelas em aberto
Reconhecemos as **parcelas 1 a 4 (out/2020 a jan/2021)**, total R$ 120.000, e pretendemos quitá-las assim que o caixa permitir. **As parcelas 5 e 6 nós contestamos** — o serviço de fevereiro e março foi interrompido pela greve e não foi concluído; não reconhecemos.

De: financeiro@boavista Data: {PAGAMENTO_PARCIAL:%d/%m/%Y}
Assunto: pagamento parcial
Segue comprovante de PIX de R$ 10.000,00 por conta da parcela 1. Restante em breve.
""")
    c.doc("negativacao_e_consulta.md", f"# Negativação e consulta\n- **{HOJE - dt.timedelta(days=61):%d/%m/%Y}** — Técnica Forte incluiu a Boa Vista no Serasa por **R$ 180.000,00** (as seis parcelas).\n- Consulta Serasa da Boa Vista (hoje): **3 outras negativações anteriores** (fornecedores diversos, 2024–2025), não contestadas.")
    c.doc("email_cliente.txt", "De: Sérgio (Técnica Forte)\n\nA Boa Vista nos deve R$ 180 mil desde 2020/2021. Quero EXECUTAR o contrato e, se não pagarem, PROTESTAR. Eles reconheceram a dívida por e-mail e até pagaram um pouco em 2023, então não prescreveu nada, certo? Já negativei no Serasa mês passado.")
    L = c.library
    L("cc_prescricao_202_206.md", "Código Civil — prescrição: arts. 189, 202, 206 §5º I", "CC arts. 189, 202 (caput e inc. VI, parágrafo único), 206 §5º I", "**Art. 202.** A interrupção da prescrição, **que somente poderá ocorrer uma vez**, dar-se-á: I – por despacho do juiz que ordenar a citação; … **VI – por qualquer ato inequívoco, ainda que extrajudicial, que importe reconhecimento do direito pelo devedor**. **Parágrafo único.** A prescrição interrompida recomeça a correr da data do ato que a interrompeu, ou do último ato do processo para a interromper. **Art. 206 §5º.** Prescreve em **cinco anos: I – a pretensão de cobrança de dívidas líquidas constantes de instrumento público ou particular**. *Reconhecimento parcial interrompe apenas quanto às parcelas reconhecidas; o pagamento parcial posterior é novo reconhecimento, mas **não interrompe novamente** (uma única vez).*", verbatim=False)
    L("cpc_titulo_executivo_monitoria.md", "CPC — título executivo extrajudicial (art. 784) e ação monitória (art. 700)", "CPC arts. 700, 784 III; STJ Súmula 299, 503; REsp 1.438.263 (contrato sem testemunhas)", "**Art. 784.** São títulos executivos extrajudiciais: … **III – o documento particular assinado pelo devedor e por 2 (duas) testemunhas**; … **Contrato particular sem duas testemunhas não é título executivo** (salvo exceções, p. ex. contrato eletrônico com assinatura digital — Tema 1.247/STJ, não aplicável aqui); **boleto bancário não é título executivo**. **Art. 700.** A ação monitória pode ser proposta por aquele que afirmar, com base em **prova escrita sem eficácia de título executivo**, ter direito de exigir do devedor capaz o pagamento de quantia em dinheiro. **Súmula 299:** é admissível a ação monitória fundada em cheque prescrito; **Súmula 503:** o prazo para ajuizamento de ação monitória em face do emitente de cheque sem força executiva é quinquenal. Alternativa: ação de cobrança pelo procedimento comum.", verbatim=False)
    L("negativacao_prescrita_sumula385.md", "Negativação de dívida prescrita; Súmula 385 STJ; protesto", "STJ Súmula 385; REsp 1.792.700; Lei 9.492/97; CDC art. 43 §5º (por analogia); STJ Tema 1.264 (dívida prescrita e cadastros)", "A **inscrição em cadastro de inadimplentes de dívida prescrita é indevida** (a pretensão está extinta; o registro não pode ultrapassar o prazo prescricional — CC/CDC 43 §5º por analogia; entendimento do STJ), ensejando exclusão e, em tese, dano moral; **Súmula 385:** 'Da anotação irregular em cadastro de proteção ao crédito, não cabe indenização por dano moral, quando preexistente legítima inscrição, ressalvado o direito ao cancelamento.' O **protesto** (Lei 9.492) de título/documento de dívida prescrita é igualmente indevido e gera responsabilidade. Protesto de **documento de dívida** sem força executiva é admitido (art. 1º), mas sempre quanto a dívida exigível.", verbatim=False)
    L("juros_correcao.md", "Encargos — multa, juros, correção; Lei 14.905/2024", "CC arts. 389, 406 (Lei 14.905/2024); contrato", "Multa contratual 2%; juros de mora 1% a.m. (contratuais) desde o vencimento; correção pelo índice contratual (IPCA). Cálculo parcela a parcela, apenas das parcelas exigíveis, abatido o pagamento parcial.", verbatim=False)
    c.contract(f"""
# Engajamento: Técnica Forte × Metalúrgica Boa Vista — cobrança de R$ 180 mil (2020/2021)

Hoje é {HOJE:%d/%m/%Y}. O cliente quer executar e protestar e já negativou. Analise.

## Entregáveis (em `workspace/deliverable/`)
1. `analise.json` — `{{"via_processual": "execucao|monitoria|cobranca", "por_que": "", "prescricao": [{{"parcela": 1, "vencimento": "", "interrompida_em": "", "novo_termo": "", "prescrita": true/false}}], "valor_principal_exigivel": 0, "valor_prescrito": 0, "negativacao": {{"regular_quanto_a": 0, "indevida_quanto_a": 0, "risco_dano_moral": "", "acao": ""}}, "protesto": "recomendado|nao", "recomendacao": ""}}`
2. `memorando.md` — raciocínio parcela a parcela (datas), via processual, negativação/protesto, estratégia (ação × acordo) com números (principal exigível + encargos estimados).
3. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Sérgio, sócio da Técnica Forte; irritado; quer agir.", [
        {"id": "testemunhas", "trigger": ["testemunha", "assinatura", "título executivo", "quem assinou"], "answer": "O contrato foi assinado só pelos dois representantes, sem testemunhas. Foi tudo meio informal.", "if_not_asked": "none"},
        {"id": "pagamento", "trigger": ["pagamento parcial", "10 mil", "2023", "PIX"], "answer": "Pagaram R$ 10 mil em agosto de 2023 por conta da primeira parcela. Depois sumiram.", "if_not_asked": "none"},
        {"id": "greve", "trigger": ["greve", "parcelas 5 e 6", "serviço concluído", "fevereiro", "março"], "answer": "Teve uma greve lá em fev/2021, mas nosso pessoal fez o que deu. Temos relatórios assinados pelo encarregado deles.", "if_not_asked": "none"},
    ], pushback=[{"when": "se analise.json disser que as parcelas 5 e 6 prescreveram", "message": "Sérgio: Mas eles pagaram em 2023! Pagamento interrompe a prescrição, qualquer um sabe. E eu tenho relatório assinado das parcelas 5 e 6. Como pode ter prescrito?"}])
    ref = {"via_processual": "monitoria (ou cobrança)", "por_que": "contrato sem duas testemunhas + boletos ≠ título executivo (CPC 784 III); prova escrita → monitória (CPC 700)",
           "prescricao": analise, "valor_principal_exigivel": exigivel, "valor_prescrito": prescrito,
           "negativacao": {"regular_quanto_a": exigivel, "indevida_quanto_a": prescrito, "risco_dano_moral": "mitigado pela Súmula 385 (3 inscrições legítimas preexistentes) — mas cancelamento devido e risco de improcedência/reconvenção quanto à parte prescrita", "acao": "retificar imediatamente a negativação para o valor exigível"},
           "protesto": "não quanto às parcelas 5-6 (prescritas); possível quanto ao exigível, com cautela (documento de dívida)",
           "pushback": "o pagamento de 2023 é reconhecimento, mas a interrupção só ocorre UMA vez (CC 202 caput) e já ocorreu em 15/09/2022 — e apenas quanto às parcelas 1-4; para 5 e 6 nunca houve reconhecimento (foram contestadas) → prescreveram em fev/mar de 2026. Relatório assinado prova o serviço, não interrompe prescrição.",
           "recomendacao": f"monitória pelas parcelas 1-4 (principal {money(exigivel, 'BRL')} + encargos) antes de 15/09/2027; retificar negativação; não protestar as prescritas; propor acordo"}
    c.reference("reference.json", ref)
    c.trap(1, "Execução", "Ajuizar execução de título extrajudicial", "Contrato sem 2 testemunhas; boleto não é título → monitória/cobrança", "Contrato (sem testemunhas); CPC 784 III", "Extinção da execução; sucumbência", "C", "CPC 784 III; 700", "high")
    c.trap(2, "'Nada prescreveu'", "Cobrar as 6 parcelas", "Reconhecimento de 15/09/2022 alcança só as parcelas 1-4 (interrupção única; recomeça); parcelas 5-6 contestadas prescreveram em 10/02/2026 e 10/03/2026; pagamento de 2023 não interrompe de novo (pushback)", "E-mails; CC 202", "Cobrança de dívida prescrita → improcedência parcial, reconvenção", "C", "CC 202 caput e VI; 206 §5º I", "high")
    c.trap(3, "Negativação pelo total", "Manter R$ 180 mil no Serasa", f"Indevida quanto a {money(prescrito, 'BRL')}; retificar; Súmula 385 mitiga dano moral mas não a irregularidade", "Negativação; consulta", "Dano moral (mitigado) + cancelamento", "H", "Súmula 385; STJ", "high")
    c.trap(4, "Protestar tudo", "Protesto das 6 parcelas", "Protesto de dívida prescrita gera responsabilidade", "Lei 9.492", "Indenização", "H", "", "high")
    c.trap(5, "Ignorar a Súmula 385 (ou superestimar o risco)", "Dizer que há dano moral certo / ou que não há risco algum", "3 inscrições legítimas preexistentes → sem dano moral, mas cancelamento devido", "Consulta Serasa", "Risco mal calibrado", "M", "Súmula 385", "high")
    c.oracle("via_processual = monitoria ou cobranca (não execução)", "true", "exact", "analise.json")
    c.oracle("prescricao: parcelas 5 e 6 prescritas; 1-4 não (novo termo 2027-09-15)", "true", "exact", "")
    c.oracle("valor_principal_exigivel", str(exigivel), "exact", "")
    c.oracle("negativacao.indevida_quanto_a", str(prescrito), "exact", "")
    c.oracle("protesto: não para as prescritas", "true", "exact", "")
    c.rubric("Memorando explica interrupção única (CC 202) no pushback")
    return c.finish()
