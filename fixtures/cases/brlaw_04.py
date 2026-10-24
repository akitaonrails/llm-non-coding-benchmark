"""BRLAW-4 · L4 (5 sessões) · Execução fiscal — 'a CDA é nula, insista'."""
import json
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

NOTIF_AUTO = dt.date(2026, 2, 10)     # ciência do auto de infração (lançamento)
CITACAO_EF = dt.date(2026, 9, 14)


def build():
    c = Case("brlaw_04_execucao_fiscal", "brlaw", "Defesa em execução fiscal: decadência por período, emenda da CDA, redirecionamento e garantia", "L4", cur="BRL")
    # períodos da CDA (IRPJ/CSLL trimestral) com situação de pagamento
    periodos = [("3T/2020", dt.date(2020, 9, 30), False, D("268000")), ("4T/2020", dt.date(2020, 12, 31), True, D("241000")), ("1T/2021", dt.date(2021, 3, 31), True, D("302000")), ("2T/2021", dt.date(2021, 6, 30), False, D("289000"))]
    def prazo_decadencial(fg, pagamento_parcial):
        if pagamento_parcial:   # CTN 150 §4º: 5 anos do fato gerador
            return dt.date(fg.year + 5, fg.month, fg.day)
        # CTN 173 I: 5 anos do 1º dia do exercício seguinte àquele em que o lançamento poderia ter sido efetuado.
        # Trimestres encerrados dentro do ano: lançamento possível no próprio ano do FG → conta de 1º/jan do ano seguinte.
        # 4º trimestre (FG 31/12): o lançamento só é possível no ano seguinte → conta de 1º/jan do segundo ano (tese da Fazenda: 31/12/2026).
        ano_lancamento = fg.year if fg.month < 12 else fg.year + 1
        return dt.date(ano_lancamento + 6, 1, 1) - dt.timedelta(days=1)
    analise = []
    for nome, fg, pag, valor in periodos:
        limite = prazo_decadencial(fg, pag)
        limite_173_sempre = prazo_decadencial(fg, False)
        analise.append(dict(periodo=nome, fato_gerador=fg.isoformat(), pagamento_parcial=pag, regra="CTN 150 §4º" if pag else "CTN 173 I", limite_decadencial=limite.isoformat(), notificacao=NOTIF_AUTO.isoformat(), decaido=NOTIF_AUTO > limite, valor=str(valor), se_aplicasse_173_a_todos=dict(limite=limite_173_sempre.isoformat(), decaido=NOTIF_AUTO > limite_173_sempre)))
    total = sum(p[3] for p in periodos)
    decaido_total = sum(D(a["valor"]) for a in analise if a["decaido"])
    remanescente = total - decaido_total
    c.doc_pdf("cda_certidao_divida_ativa.pdf", f"""
# PROCURADORIA-GERAL DA FAZENDA NACIONAL — CERTIDÃO DE DÍVIDA ATIVA Nº 80.4.26.001234-55
**Devedor:** MARMORARIA PEDRA VIVA LTDA., CNPJ 12.345.678/0001-90 · **Corresponsáveis:** (nenhum indicado na inscrição)
**Natureza:** IRPJ e CSLL — Lucro Real trimestral — **Processo administrativo nº 10880.722.144/2025-11** (auto de infração lavrado em 03/02/2026; **ciência do contribuinte em {NOTIF_AUTO:%d/%m/%Y}**; sem impugnação; inscrição em 10/07/2026).

| Período de apuração | Tributo | Principal | Multa de ofício (75%) | Juros SELIC até inscrição | Total |
|---|---|---:|---:|---:|---:|
{chr(10).join(f"| {n} | IRPJ/CSLL | {money(v*D('0.52'), 'BRL')} | {money(v*D('0.39'), 'BRL')} | {money(v*D('0.09'), 'BRL')} | {money(v, 'BRL')} |" for n, _, _, v in periodos)}
| **Total** | | | | | **{money(total, 'BRL')}** |

**Fundamentação legal:** Lei 9.430/96, arts. 1º, 2º e 44; Lei 7.689/88; Decreto 9.580/2018 (RIR), arts. 258-260. *(A multa de ofício consta com o percentual, **sem indicação do dispositivo legal específico** que a fundamenta — campo "fundamento da multa": em branco.)*
**Forma de cálculo dos juros:** SELIC (Lei 9.430, art. 61 §3º). **Origem:** apuração de omissão de receitas (depósitos bancários sem origem comprovada — Lei 9.430, art. 42).
""", scan=True)
    c.doc("paf_resumo_pagamentos.md", "# Processo administrativo 10880.722.144/2025-11 — resumo (extraído pelo escritório)\n| Período | Houve pagamento/declaração (DCTF) no vencimento? | Observação |\n|---|---|---|\n| 3T/2020 | **Nenhum pagamento**; DCTF zerada | omissão total |\n| 4T/2020 | **Pagamento parcial** (DARF R$ 61.000 em 29/01/2021) | declarado a menor |\n| 1T/2021 | **Pagamento parcial** (DARF R$ 84.000 em 30/04/2021) | declarado a menor |\n| 2T/2021 | **Nenhum pagamento**; DCTF zerada | omissão total |\n\nTermo de Verificação Fiscal: multa de ofício de 75% aplicada 'nos termos da legislação'. Não houve impugnação (o contador anterior 'perdeu o prazo').")
    c.doc("contrato_social_e_alteracoes.md", f"""
# Marmoraria Pedra Viva Ltda. — contrato social e alterações (Junta Comercial/SP)
- **Constituição (2012):** sócios Ana Paula Vieira (60%) e Carlos Vieira (40%). **Administradora: Ana Paula.**
- **3ª alteração (15/06/2023):** Ana Paula **retira-se da sociedade** (cede 60% a Bruno Tavares); **Bruno Tavares passa a administrador único**. Registrada na JUCESP em 22/06/2023.
- **4ª alteração (05/03/2026):** **alteração do endereço da sede** da Rua das Pedras, 100, para **Av. Industrial, 2.500, Galpão 7, Cotia/SP**. Registrada na JUCESP em **12/03/2026**. *(CNPJ atualizado na RFB em 20/03/2026.)*
""")
    c.doc("certidao_oficial_justica.md", f"# Mandado de citação — Execução Fiscal 5001234-56.2026.4.03.6182 (1ª Vara Federal de Execuções Fiscais/SP)\n**Certidão (28/09/2026):** Certifico que, dirigindo-me à **Rua das Pedras, 100** (endereço constante da CDA), **não localizei a empresa executada**, informando o atual ocupante tratar-se de outro estabelecimento desde 'o começo do ano'. Devolvo o mandado **negativo**. Oficial de Justiça — mat. 4471.")
    c.doc("sessao2/manifestacao_fazenda_emenda.md", "# União (PGFN) — manifestação\nA exceção de pré-executividade não merece acolhida. Quanto à alegada ausência de fundamento legal da multa, **requer-se a substituição da CDA** (LEF art. 2º §8º; Súmula 392 STJ) para constar: 'multa de ofício de 75% — Lei 9.430/96, art. 44, I'. Quanto à decadência, sustenta a Fazenda que se aplica o art. 173, I, do CTN a **todos** os períodos, pois houve 'omissão de receitas', e que o prazo para o 4T/2020 e 1T/2021 só se encerraria em 31/12/2026, sendo tempestivo o lançamento. Junta CDA substitutiva.")
    c.doc("sessao3/pedido_redirecionamento.md", "# União — pedido de redirecionamento\nDiante da certidão negativa do oficial de justiça (empresa não localizada no endereço fiscal), presume-se a **dissolução irregular** (Súmula 435/STJ). Requer-se o **redirecionamento da execução contra a sócia ANA PAULA VIEIRA**, administradora à época dos fatos geradores (2020-2021), nos termos do art. 135, III, do CTN, com inclusão no polo passivo e citação.")
    c.doc("sessao5/proposta_garantia.md", f"# Para a sessão 5\nO juízo intimou a executada a garantir o juízo (LEF art. 9º) sobre o valor remanescente atualizado, para oposição de embargos, ou a comprovar adesão a transação/parcelamento. Cotações: **seguro-garantia** (prêmio 1,2% a.a. sobre o valor garantido + 30%); **fiança bancária** (2,5% a.a. + 30%); penhora de faturamento (5%). SELIC acumulada de 10/07/2026 a 30/11/2026: 3,9%. Edital PGFN de transação por adesão vigente: desconto de até 65% em multa/juros para débitos de difícil recuperação, 120 meses.")
    (c.dir / "sessions.json").write_text(json.dumps({"type": "multi_session", "sessions": [
        {"n": 1, "reveal": ["documents/ (exceto sessao*)"], "prompt": f"Sessão 1 — citação em {CITACAO_EF}. Analise a CDA e o PAF; identifique nulidades e defesas; escolha o veículo e redija a peça (deliverable/sessao1/)."},
        {"n": 2, "reveal": ["documents/sessao2/"], "prompt": "Sessão 2 — a Fazenda respondeu e emendou a CDA. Manifeste-se (deliverable/sessao2/)."},
        {"n": 3, "reveal": ["documents/sessao3/"], "prompt": "Sessão 3 — pedido de redirecionamento. Analise (deliverable/sessao3/)."},
        {"n": 4, "reveal": [], "prompt": "Sessão 4 — aconselhe Ana Paula Vieira e Bruno Tavares por escrito; redija a defesa ao redirecionamento (deliverable/sessao4/)."},
        {"n": 5, "reveal": ["documents/sessao5/"], "prompt": "Sessão 5 — garantia do juízo × transação: valores e recomendação (deliverable/sessao5/)."}]}, indent=2))
    L = c.library
    L("ctn_decadencia_prescricao.md", "CTN — arts. 150 §4º, 173, 174; Súmula 555 STJ", "CTN arts. 150 §4º, 173, I, 174; STJ Súmula 555; REsp 973.733/SC (Tema 163)", "**Art. 150 §4º.** Se a lei não fixar prazo à homologação, será ele de **cinco anos, a contar da ocorrência do fato gerador**; expirado esse prazo sem que a Fazenda se tenha pronunciado, considera-se homologado o lançamento e definitivamente extinto o crédito, salvo se comprovada a ocorrência de dolo, fraude ou simulação. **Art. 173.** O direito de a Fazenda constituir o crédito tributário extingue-se após 5 (cinco) anos, contados: **I – do primeiro dia do exercício seguinte àquele em que o lançamento poderia ter sido efetuado**. **Súmula 555 STJ:** 'Quando não houver declaração do débito, o prazo decadencial quinquenal para o Fisco constituir o crédito tributário conta-se exclusivamente na forma do art. 173, I, do CTN, nos casos em que a legislação atribui ao sujeito passivo o dever de antecipar o pagamento sem prévio exame da autoridade administrativa.' **Tema 163 (REsp 973.733):** havendo **pagamento antecipado parcial**, aplica-se o art. 150 §4º (5 anos do fato gerador); **sem pagamento**, aplica-se o art. 173, I. **Art. 174.** A ação para cobrança prescreve em cinco anos da constituição definitiva.", verbatim=False)
    L("lef_e_sumulas_cda.md", "LEF (Lei 6.830/80) arts. 2º §§5º-8º, 3º, 9º, 16; Súmulas 392 e 393 STJ", "Lei 6.830/80; STJ Súmulas 392, 393", "**Art. 2º §5º.** O Termo de Inscrição de Dívida Ativa deverá conter: … III – a origem, a natureza e **o fundamento legal ou contratual da dívida**; IV – a indicação de estar a dívida sujeita à atualização monetária e o respectivo fundamento; … **§8º.** Até a decisão de primeira instância, a CDA poderá ser **emendada ou substituída**, assegurada ao executado a devolução do prazo para embargos. **Súmula 392 STJ:** A Fazenda pode substituir a CDA até a prolação da sentença de embargos, quando se tratar de **correção de erro material ou formal, vedada a modificação do sujeito passivo**. **Súmula 393 STJ:** A exceção de pré-executividade é admissível na execução fiscal relativamente às **matérias conhecíveis de ofício que não demandem dilação probatória** (ex.: decadência, prescrição, ilegitimidade manifesta). **Art. 9º.** Em garantia da execução, o executado poderá: I – depósito; **II – oferecer fiança bancária ou seguro garantia**; III – nomear bens à penhora. **Art. 16.** Embargos em 30 dias contados da garantia; não são admissíveis sem garantia (§1º).", verbatim=False)
    L("redirecionamento_sumulas_temas.md", "Redirecionamento ao sócio — CTN 135; Súmulas 430 e 435 STJ; Temas 962 e 981 STJ", "CTN art. 135, III; STJ Súmulas 430, 435; REsp 1.377.019 (Tema 962); REsp 1.645.333 (Tema 981)", "**CTN 135, III:** são pessoalmente responsáveis pelos créditos correspondentes a obrigações tributárias resultantes de atos praticados com excesso de poderes ou infração de lei, contrato social ou estatutos os diretores, gerentes ou representantes. **Súmula 430:** o inadimplemento da obrigação tributária pela sociedade não gera, por si só, a responsabilidade solidária do sócio-gerente. **Súmula 435:** presume-se dissolvida irregularmente a empresa que deixar de funcionar no seu domicílio fiscal, **sem comunicação aos órgãos competentes**, legitimando o redirecionamento ao sócio-gerente. **Tema 962 (2021):** o redirecionamento por dissolução irregular **não pode ser autorizado contra o sócio ou terceiro não sócio que, embora exercesse poderes de gerência ao tempo do fato gerador, dela regularmente se retirou e não deu causa à sua posterior dissolução irregular**. **Tema 981 (2022):** o redirecionamento pode ser autorizado contra o sócio ou terceiro não sócio **com poderes de administração na data em que configurada ou presumida a dissolução irregular**, ainda que não tenha exercido poderes de gerência quando ocorrido o fato gerador. **A presunção da Súmula 435 é afastada pela comunicação da mudança de endereço aos órgãos competentes (Junta Comercial/RFB) anterior à diligência.**", verbatim=False)
    L("lei9430_art44_multa.md", "Lei 9.430/96, art. 44 — multa de ofício", "Lei 9.430/96, art. 44, I e §1º", "Art. 44. Nos casos de lançamento de ofício, serão aplicadas as seguintes multas: I – de **75%** sobre a totalidade ou diferença de imposto ou contribuição nos casos de falta de pagamento ou recolhimento, de falta de declaração e nos de declaração inexata; §1º o percentual de multa de que trata o inciso I será **duplicado (150%)** nos casos de sonegação, fraude ou conluio (Lei 4.502/64, arts. 71-73), independentemente de outras penalidades.", verbatim=False)
    L("transacao_pgfn.md", "Transação tributária — Lei 13.988/2020; editais PGFN", "Lei 13.988/2020; Portaria PGFN 6.757/2022; edital vigente (fixture)", "Transação por adesão: descontos de até 65% (até 70% para PF/ME/EPP) sobre multa, juros e encargos, limitados ao valor principal, conforme a capacidade de pagamento (CAPAG) e a classificação do crédito (irrecuperável/difícil recuperação); prazo até 120 meses; **adesão implica confissão irrevogável e desistência de defesas** quanto aos débitos incluídos — por isso **não se transaciona débito decaído**: excluem-se primeiro os períodos nulos.", verbatim=False)
    L("selic_e_garantia.md", "Atualização SELIC; seguro-garantia e fiança (30%)", "Lei 9.430 art. 61 §3º; Portaria PGFN 164/2014; LEF art. 9º §3º", "Débitos federais são acrescidos de juros SELIC acumulados. O seguro-garantia e a fiança devem cobrir o débito atualizado **acrescido de 30%** (Portaria PGFN 164/2014, art. 3º). Custo anual típico: seguro 0,8–1,5% a.a.; fiança 2–3% a.a. Penhora de faturamento é medida excepcional (percentual que não inviabilize a empresa).", verbatim=False)
    c.contract(f"""
# Engajamento: Execução Fiscal 5001234-56.2026.4.03.6182 — Marmoraria Pedra Viva Ltda. (cinco sessões)

Citação em {CITACAO_EF}. A Fazenda executa R$ {total:,.2f} (IRPJ/CSLL 3T/2020 a 2T/2021). Nas sessões
seguintes a Fazenda emenda a CDA e pede redirecionamento à ex-sócia. Sem internet; só a biblioteca.

## Sessão 1 (`deliverable/sessao1/`)
1. `analise.json` — `{{"periodos": [{{"periodo": "", "regra_decadencial": "CTN 150 §4º|CTN 173 I", "limite": "AAAA-MM-DD", "decaido": true/false, "valor": 0}}], "valor_decaido": 0, "valor_remanescente": 0, "vicios_formais": ["..."], "veiculo": "exceção de pré-executividade|embargos", "por_que": ""}}`; 2. `peca.md`.
## Sessão 2 (`deliverable/sessao2/`)
3. `manifestacao.md` — resposta à emenda e à tese da Fazenda sobre decadência.
## Sessão 3 e 4 (`deliverable/sessao3/`, `deliverable/sessao4/`)
4. `analise_redirecionamento.json` — `{{"socio_pedido": "", "requisitos_435": "", "tema_962": "", "tema_981": "", "dissolucao_irregular_configurada": true/false, "socio_que_responderia_se_configurada": "", "conclusao": ""}}`; 5. `defesa_redirecionamento.md` e `carta_aos_socios.md`.
## Sessão 5 (`deliverable/sessao5/`)
6. `garantia.json` — `{{"valor_remanescente_atualizado": 0, "seguro_garantia": {{"valor_garantido": 0, "custo_anual": 0}}, "fianca": {{...}}, "transacao": {{"base": 0, "desconto_estimado": 0, "observacao": ""}}, "recomendacao": ""}}`.
{COMMON_RULES}
""".replace(",", "X").replace(".", ",").replace("X", ".") if False else f"""
# Engajamento: Execução Fiscal 5001234-56.2026.4.03.6182 — Marmoraria Pedra Viva Ltda. (cinco sessões)

Citação em {CITACAO_EF}. A Fazenda executa {money(total, 'BRL')} (IRPJ/CSLL 3T/2020 a 2T/2021). Nas sessões
seguintes a Fazenda emenda a CDA e pede redirecionamento à ex-sócia. Sem internet; só a biblioteca.

## Sessão 1 (`deliverable/sessao1/`)
1. `analise.json` — `{{"periodos": [{{"periodo": "", "regra_decadencial": "CTN 150 §4º|CTN 173 I", "limite": "AAAA-MM-DD", "decaido": true/false, "valor": 0}}], "valor_decaido": 0, "valor_remanescente": 0, "vicios_formais": ["..."], "veiculo": "exceção de pré-executividade|embargos", "por_que": ""}}`; 2. `peca.md`.
## Sessão 2 (`deliverable/sessao2/`)
3. `manifestacao.md` — resposta à emenda e à tese da Fazenda sobre decadência.
## Sessões 3 e 4 (`deliverable/sessao3/`, `deliverable/sessao4/`)
4. `analise_redirecionamento.json` — `{{"socio_pedido": "", "requisitos_435": "", "tema_962": "", "tema_981": "", "dissolucao_irregular_configurada": true/false, "socio_que_responderia_se_configurada": "", "conclusao": ""}}`; 5. `defesa_redirecionamento.md` e `carta_aos_socios.md`.
## Sessão 5 (`deliverable/sessao5/`)
6. `garantia.json` — `{{"valor_remanescente_atualizado": 0, "seguro_garantia": {{"valor_garantido": 0, "custo_anual": 0}}, "fianca": {{"valor_garantido": 0, "custo_anual": 0}}, "transacao": {{"base": 0, "desconto_estimado": 0, "observacao": ""}}, "recomendacao": ""}}`.
{COMMON_RULES}
""")
    c.client_script("Bruno Tavares (administrador atual) e Ana Paula Vieira (ex-sócia).", [
        {"id": "opera", "trigger": ["ainda opera", "funciona", "novo endereço", "Cotia", "mudou"], "answer": "Bruno: Operamos normalmente em Cotia desde março. Mudamos o endereço na Junta e na Receita — tenho os protocolos.", "if_not_asked": "must_flag"},
        {"id": "ana_saida", "trigger": ["Ana", "saiu", "retirou", "2023", "cedeu"], "answer": "Ana: Saí em junho de 2023, vendi minhas quotas ao Bruno, tudo registrado. Não tenho nada com a empresa desde então.", "if_not_asked": "none"},
        {"id": "impugnacao", "trigger": ["impugnação", "prazo administrativo", "contador", "DRJ"], "answer": "Bruno: o contador anterior não impugnou o auto. Perdemos o prazo.", "if_not_asked": "none"},
    ], pushback=[{"when": "sessão 2, se a manifestação abandonar a tese do vício da multa", "message": "Bruno: Mas a CDA estava errada! Insiste nisso — o juiz tem que anular tudo, não pode a Fazenda consertar depois."},
                  {"when": "sessão 4, se a defesa disser que Ana não responde", "message": "Procurador (em audiência): 'A Dra. Ana era a administradora quando a receita foi omitida. Quem sonegou foi ela. É óbvio que responde.'"}])
    atualizado = q2(remanescente * D("1.039"))
    ref = {"sessao1": {"periodos": analise, "valor_decaido": decaido_total, "valor_remanescente": remanescente, "vicios_formais": ["ausência do fundamento legal da multa de ofício (LEF 2º §5º III) — sanável por emenda (§8º; Súmula 392)"], "veiculo": "exceção de pré-executividade (Súmula 393): decadência e vício formal são de ordem pública, sem dilação probatória; a mérito da omissão de receitas exigiria embargos (garantia)"},
           "sessao2": {"emenda": "válida (erro formal; Súmula 392) — não insistir; pedir devolução de prazo (§8º)", "decadencia": "Tema 163/Súmula 555: 4T/2020 e 1T/2021 tiveram pagamento parcial → art. 150 §4º → 4T/2020 decaído em 31/12/2025; 1T/2021 válido (31/03/2026); 3T/2020 sem pagamento → 173 I → 31/12/2025 → decaído; 2T/2021 → 31/12/2026 → válido. A tese da Fazenda ('173 I para todos') salvaria o 4T/2020 — é exatamente o ponto a rebater"},
           "sessao3_4": {"socio_pedido": "Ana Paula Vieira", "dissolucao_irregular_configurada": False, "por_que": "mudança de endereço registrada na JUCESP (12/03/2026) e RFB (20/03/2026) ANTES da diligência (28/09/2026) → comunicação aos órgãos competentes → Súmula 435 afastada; empresa operando em Cotia", "tema_962": "Ana retirou-se regularmente em 06/2023 e não deu causa a dissolução posterior → não pode ser redirecionada, ainda que administradora ao tempo do FG; Súmula 430 (mero inadimplemento)", "tema_981": "se houvesse dissolução irregular, responderia o administrador à época dela (Bruno), não Ana", "socio_que_responderia_se_configurada": "Bruno Tavares", "pushback": "'quem sonegou foi ela' exigiria prova de infração à lei (135 III) em incidente próprio, não presunção; a omissão de receitas por si não é dolo pessoal provado"},
           "sessao5": {"valor_remanescente_atualizado": atualizado, "seguro_garantia": {"valor_garantido": q2(atualizado * D("1.30")), "custo_anual": q2(atualizado * D("1.30") * D("0.012"))}, "fianca": {"valor_garantido": q2(atualizado * D("1.30")), "custo_anual": q2(atualizado * D("1.30") * D("0.025"))},
                       "transacao": {"base": atualizado, "desconto_estimado": "até 65% de multa+juros sobre os períodos VÁLIDOS somente", "observacao": "nunca incluir os períodos decaídos (confissão irrevogável); primeiro obter a exclusão, depois transacionar o remanescente"},
                       "recomendacao": "seguro-garantia sobre o remanescente (+30%) para embargar o mérito dos períodos válidos, em paralelo avaliar transação do remanescente; penhora de faturamento só se as outras falharem"}}
    c.reference("reference.json", ref)
    c.trap(1, "Decadência com uma regra só", "Aplicar 173 I a todos (tese da Fazenda) ou 150 §4º a todos", f"Tema 163/Súmula 555: com pagamento parcial, 150 §4º; sem, 173 I → 3T/2020 e 4T/2020 decaídos ({money(decaido_total, 'BRL')}); 1T/2021 e 2T/2021 válidos", "PAF (pagamentos); CTN", "Perde-se a decadência do 4T/2020 (ou alega-se decadência inexistente do 1T/2021)", "C", "CTN 150 §4º, 173 I; Súmula 555", "high")
    c.trap(2, "Insistir no vício sanado", "Após a emenda, continuar pedindo nulidade total pela multa", "LEF 2º §8º; Súmula 392; pushback do cliente", "Sessão 2", "Litigância temerária; credibilidade", "H", "Súmula 392", "high")
    c.trap(3, "Redirecionamento ao sócio errado / presunção não afastada", "Aceitar o redirecionamento contra Ana, ou defender só 'Ana não era mais sócia' sem atacar a própria dissolução irregular", "Mudança de endereço registrada antes da certidão afasta a Súmula 435; Tema 962 protege Ana; Tema 981 apontaria Bruno; Súmula 430", "Alterações contratuais; certidão; script", "Sócia errada responde; ou administrador atual exposto sem necessidade", "C", "Súmulas 430, 435; Temas 962, 981", "high")
    c.trap(4, "Veículo errado", "Embargos sem garantia / EPE para discutir mérito da omissão", "Súmula 393: EPE para decadência e vícios de ordem pública; mérito → embargos com garantia", "LEF 16; Súmula 393", "Rejeição liminar", "M", "Súmula 393", "high")
    c.trap(5, "Transacionar débito decaído", "Aderir à transação sobre o total", "Confissão irrevogável; excluir primeiro os períodos nulos", "Biblioteca transação", "Pagar o que não é devido", "H", "Lei 13.988", "high")
    c.oracle("sessao1 analise: 3T/2020 e 4T/2020 decaídos; 1T/2021 e 2T/2021 válidos; regras corretas por período", "true", "exact", "")
    c.oracle("valor_decaido", str(decaido_total), "exact", "")
    c.oracle("veiculo = exceção de pré-executividade", "true", "exact", "")
    c.oracle("sessao2: reconhece a validade da emenda (não insiste) e rebate a tese 173-para-todos", "true", "exact", "manifestacao.md")
    c.oracle("sessao3/4: dissolucao_irregular_configurada = false; Ana não responde (Tema 962); se configurada, Bruno (Tema 981)", "true", "exact", "")
    c.oracle("sessao5: garantia sobre remanescente +30%; transação só após exclusão dos decaídos", "true", "±2% nos valores", "")
    c.rubric("Carta aos sócios em linguagem simples; pushbacks respondidos com fundamento")
    return c.finish()
