"""BRLAW-8 · L3 · Venda da Vértice — due diligence e minuta do comprador (sessão única)."""
from generators.core import Case, COMMON_RULES


def build():
    c = Case("brlaw_08_ma_diligencia", "brlaw", "Venda de controle: achados de diligência e redline do contrato de compra e venda de quotas", "L3", cur="BRL")
    c.doc_pdf("data_room_indice_e_extratos.pdf", """
# Vértice Engenharia Consultiva Ltda. — Data room (sell-side) — índice e extratos

## 1. Contratos relevantes
**1.1 Contrato de prestação de serviços — Construtora Horizonte Azul S.A. (31% da receita), 2024–2028.** Cláusula 19 — *"A alteração do controle societário da CONTRATADA, direta ou indireta, sem prévia e expressa anuência da CONTRATANTE, constitui causa de rescisão imediata, com multa de 20% do saldo contratual."*
**1.2 Contrato administrativo nº 044/2025 — Município de Sorocaba (obra de drenagem; 12% da receita)** — Lei 14.133/2021. Cláusula de subcontratação/cessão: *"vedada a cessão total; alteração societária admitida desde que mantidas as condições de habilitação, com comunicação prévia à Administração."*
**1.3** Demais contratos privados: silentes quanto a mudança de controle.

## 2. Trabalhista
**2.1** 46 empregados CLT. **2.2** 11 engenheiros contratados como **PJ** (exclusivos, horário, subordinação — mesmo perfil do caso Solaris). **2.3** 3 reclamações trabalhistas em curso (valor de causa total R$ 1,4 mi; provisão contábil R$ 380 mil, classificadas 'possível').

## 3. Fiscal / regulatório
**3.1** Certidões: **CND federal — POSITIVA** (débito de R$ 310 mil de IRPJ 2023 em cobrança, sem parcelamento); CRF/FGTS regular; estadual/municipal regulares.
**3.2** Regime: Simples Nacional (sublimite ultrapassado em 2025 — ISS por fora).
**3.3** CREA: registro da empresa regular; responsável técnico = sócio Hélio (que sai com a venda).

## 4. Societário
**4.1** Contrato social: cláusula de **preferência** dos sócios na cessão de quotas (30 dias); sem acordo de sócios.
**4.2** Faturamento 2025: R$ 4,2 mi. Grupo comprador (Meridiano): faturamento consolidado Brasil 2025 R$ 390 mi.
""")
    c.doc_pdf("minuta_comprador_cpv_quotas.pdf", """
# CONTRATO DE COMPRA E VENDA DE QUOTAS — minuta do COMPRADOR (Grupo Meridiano Participações S.A.) — cláusulas relevantes

**2.3 Earn-out.** O Comprador pagará aos Vendedores 35% do valor em que o **EBITDA** dos 12 meses seguintes ao fechamento exceder R$ 1.100.000,00, limitado a R$ 1.500.000,00. *"EBITDA" significa o lucro antes de juros, impostos, depreciação e amortização, **apurado pelo Comprador segundo suas práticas contábeis**, podendo incluir rateio de despesas corporativas do grupo.*
**3.2 Condições precedentes.** Obtenção das anuências listadas no **Anexo 3.2** *(Anexo 3.2: "não aplicável")*. **Aprovação do CADE**, nos termos da Lei 12.529/2011.
**5.7 Declarações dos Vendedores — Trabalhista.** *"Todos os prestadores de serviços da Sociedade estão regularmente contratados, inexistindo risco de reconhecimento de vínculo empregatício."*
**5.9 Declarações — Tributária.** *"A Sociedade encontra-se em situação fiscal regular, com certidões negativas vigentes."*
**8.1 Indenização pelos Vendedores.** Perdas decorrentes de violação de declarações. **8.4 Limites.** (a) franquia (*basket*) de R$ 150.000,00, **não dedutível** (*tipping*); (b) limite global de 15% do preço, **exceto para as matérias das cláusulas 5.7 e 5.9, cujo limite será o Preço Total**; (c) **"O conhecimento do Comprador sobre qualquer fato, antes ou depois da assinatura, não afasta nem reduz o direito à indenização"**; (d) prazo: 5 anos para 5.7 e 5.9; 2 anos demais.
**9.1 Não concorrência.** Vendedores: **10 anos, território nacional**.
**10.2 Conta-garantia (escrow).** 20% do preço por 5 anos.
**Carta do advogado do comprador:** "Minuta padrão de mercado. A 8.4(c) é apenas a redação usual de *sandbagging*. Não vemos necessidade de anuências (Anexo 3.2). Confirmem a notificação ao CADE para não atrasar."
""")
    c.doc("email_socios.txt", "De: Hélio e Beatriz Vértice\n\nA minuta do Meridiano parece normal, o advogado deles disse que é padrão. Só não entendemos por que precisa do CADE — isso demora meses? Queremos fechar em 45 dias. Os engenheiros PJ sempre foram PJ. Diz o que muda.")
    L = c.library
    L("ctn_133_sucessao.md", "CTN art. 133 — sucessão tributária na aquisição de estabelecimento; cessão de quotas", "CTN arts. 132, 133; Lei 11.101 art. 141", "**Art. 133.** A pessoa natural ou jurídica que adquirir de outra, por qualquer título, **fundo de comércio ou estabelecimento** e continuar a exploração responde pelos tributos relativos ao fundo ou estabelecimento adquirido: **I – integralmente, se o alienante cessar a exploração**; **II – subsidiariamente**, se o alienante prosseguir na exploração ou iniciar, dentro de 6 meses, nova atividade. **Na compra de QUOTAS a pessoa jurídica permanece a mesma — não há sucessão: o passivo tributário continua sendo da própria sociedade adquirida** (e, por isso, é precificado/indenizado); a CND positiva impede a emissão de certidões necessárias a licitações e pode travar operações (alteração contratual de sociedade com débito federal: JUCESP não exige CND; mas contratos públicos exigem regularidade — Lei 14.133 art. 92 XVI).", verbatim=False)
    L("clt_10_448_sucessao_trabalhista.md", "CLT arts. 10, 448, 448-A — sucessão trabalhista", "CLT arts. 10, 448, 448-A", "**Art. 10.** Qualquer alteração na estrutura jurídica da empresa não afetará os direitos adquiridos por seus empregados. **Art. 448.** A mudança na propriedade ou na estrutura jurídica da empresa não afetará os contratos de trabalho dos respectivos empregados. **Art. 448-A.** Caracterizada a sucessão empresarial ou de empregadores, **as obrigações trabalhistas, inclusive as contraídas à época em que os empregados trabalhavam para a empresa sucedida, são de responsabilidade do sucessor**; parágrafo único: a empresa sucedida responde solidariamente quando ficar comprovada fraude. Na cessão de quotas, a empregadora é a mesma; o passivo (inclusive o risco de pejotização dos 11 engenheiros) permanece na sociedade e é objeto de preço/indenização.", verbatim=False)
    L("cade_limiares.md", "CADE — notificação obrigatória: limiares", "Lei 12.529/2011, art. 88; Portaria Interministerial 994/2012", "É obrigatória a notificação ao CADE de atos de concentração em que, cumulativamente: **I – pelo menos um dos grupos envolvidos tenha registrado faturamento bruto anual no Brasil, no ano anterior, igual ou superior a R$ 750 milhões; e II – pelo menos um outro grupo envolvido tenha registrado faturamento bruto anual no Brasil igual ou superior a R$ 75 milhões.** Fora dos limiares, não há notificação obrigatória (o CADE pode, excepcionalmente, requerer análise em até 1 ano — art. 88 §7º). Grupo Meridiano R$ 390 mi (< 750 mi) e Vértice R$ 4,2 mi (< 75 mi) → **não notificável**.", verbatim=False)
    L("lei14133_alteracao_societaria.md", "Lei 14.133/2021 — alteração societária do contratado; regularidade fiscal", "Lei 14.133/2021, arts. 92 XVI, 124 II, 137 VI; art. 91 (habilitação mantida)", "A alteração social do contratado **não** é causa de extinção se mantidas as condições de habilitação e não houver prejuízo à execução (interpretação do art. 137, VI, a contrario); exige **comunicação** à Administração e manutenção de regularidade fiscal durante a execução (art. 92, XVI) — **CND positiva pode ensejar retenção de pagamentos/sanções**. Responsável técnico que sai: substituir perante o CREA e a Administração.", verbatim=False)
    L("cc_1147_nao_concorrencia.md", "Código Civil art. 1.147 — não concorrência na alienação de estabelecimento", "CC art. 1.147", "Não havendo autorização expressa, o alienante do estabelecimento não pode fazer concorrência ao adquirente, **nos cinco anos subsequentes à transferência**. Aplicado por analogia à cessão de controle; prazos muito superiores a 5 anos e território nacional sem relação com a atuação regional tendem a ser reduzidos (razoabilidade; STJ).", verbatim=False)
    L("sandbagging_franquia_mercado.md", "Declarações e garantias — sandbagging, franquia, limites (prática brasileira)", "Doutrina de M&A; precedentes arbitrais (CAM-CCBC); pesquisa de mercado", "**Pro-sandbagging** (8.4(c)): o comprador indeniza-se mesmo pelo que já conhecia — combinado com declaração 'limpa' (5.7, 5.9) sobre matéria **revelada no data room** (PJs; CND positiva) e **limite igual ao preço**, transfere ao vendedor um risco conhecido e precificável, de forma integral e por 5 anos. Proteções do vendedor: **anexo de exceções (disclosure schedule)** qualificando 5.7 e 5.9; **indenização específica** para os PJs e para o débito de IRPJ, com teto dimensionado e escrow dedicado; franquia dedutível; limite geral de 10–20% do preço; prazo 2–3 anos (fiscal/trabalhista: prescrição + 6 meses é defensável).", kind="prática", verbatim=False)
    L("earnout_pratica.md", "Earn-out — definição de EBITDA e controle do comprador", "Prática de M&A; precedentes arbitrais", "EBITDA 'apurado pelo Comprador segundo suas práticas' com 'rateio de despesas corporativas' permite zerar o earn-out. Proteções: princípios contábeis históricos da sociedade (ou CPC consistentemente aplicados), exclusão de rateios do grupo e custos de integração, obrigação de conduzir o negócio no curso normal sem atos para frustrar o earn-out, acesso a informações, perito independente para divergências, aceleração em caso de revenda.", kind="prática", verbatim=False)
    c.contract("""
# Engajamento: venda do controle da Vértice — diligência (lado vendedor) e redline da minuta do Meridiano

Os sócios querem fechar em 45 dias e acham a minuta 'padrão'. Diga o que os atinge.

## Entregáveis (em `workspace/deliverable/`)
1. `achados.json` — `[{"achado": "", "onde": "data room §", "por_que_importa": "", "efeito": "anuencia|preco|indenizacao|prazo|nenhum", "solucao": ""}]`
2. `redline.md` — para as cláusulas 2.3, 3.2 (Anexo 3.2 e CADE), 5.7, 5.9, 8.4(a)-(d), 9.1, 10.2: manter/alterar, redação e motivo.
3. `resposta_advogado_comprador.md` — Anexo 3.2, CADE e 8.4(c).
4. `nota_socios.md` — em linguagem simples, as três coisas que custam dinheiro depois do fechamento.
5. `PERGUNTAS.md` (opcional), `STATUS.md`.
""" + COMMON_RULES)
    c.client_script("Hélio e Beatriz Vértice; querem fechar rápido; honestos.", [
        {"id": "horizonte", "trigger": ["Horizonte Azul", "anuência", "mudança de controle", "31%"], "answer": "Hélio: a Horizonte Azul é nosso maior cliente; o diretor deles é meu amigo, mas o jurídico deles é duro. Não contamos da venda ainda.", "if_not_asked": "none"},
        {"id": "pjs", "trigger": ["PJ", "engenheiros", "vínculo", "horário", "exclusiv"], "answer": "Beatriz: os 11 engenheiros PJ trabalham 9h-18h aqui, exclusivos, com gestor. Sempre foi assim.", "if_not_asked": "none"},
        {"id": "cnd", "trigger": ["CND", "certidão", "IRPJ 2023", "parcel", "débito"], "answer": "Hélio: tem um débito de IRPJ de 2023 em cobrança, uns 310 mil; não parcelamos porque discordamos.", "if_not_asked": "none"},
        {"id": "revelado", "trigger": ["mostrou", "data room", "comprador viu", "sabe dos PJ"], "answer": "Beatriz: o Meridiano viu tudo no data room, inclusive a lista dos PJs e a certidão positiva. Não reclamaram.", "if_not_asked": "none"},
    ], pushback=[{"when": "se o redline alterar 8.4(c) ou 5.7/5.9", "message": "Advogado do comprador (retransmitido): 8.4(c) é padrão de mercado; 5.7 e 5.9 são declarações de conformidade básicas — se está tudo certo, qual o problema? Hélio: podemos só assinar?"}])
    ref = {"achados": [
        {"achado": "Cláusula 19 do contrato Horizonte Azul — mudança de controle sem anuência = rescisão + multa 20%", "efeito": "anuencia", "solucao": "Anexo 3.2 deve listar a Horizonte Azul; condição precedente ou ajuste de preço; abordar o cliente antes da assinatura"},
        {"achado": "11 engenheiros PJ com subordinação — risco de vínculo (pejotização); provisão insuficiente", "efeito": "indenizacao/preco", "solucao": "anexo de exceções à 5.7; indenização específica com teto dimensionado e escrow dedicado; não dar declaração limpa"},
        {"achado": "CND federal positiva (IRPJ 2023, R$ 310 mil) — declaração 5.9 falsa se assinada; risco em contrato público (regularidade fiscal)", "efeito": "indenizacao/prazo", "solucao": "exceção à 5.9; parcelamento/garantia antes do fechamento para obter CPEN; indenização específica"},
        {"achado": "8.4(c) pro-sandbagging + 5.7/5.9 limpas + limite = preço total + 5 anos = vendedor indeniza risco conhecido integralmente", "efeito": "indenizacao", "solucao": "anti-sandbagging quanto a matérias reveladas; limites 10–20%; prazo 2–3 anos; franquia dedutível"},
        {"achado": "CADE — não notificável (390 mi < 750 mi; 4,2 mi < 75 mi)", "efeito": "nenhum", "solucao": "retirar a condição precedente; responder ao advogado do comprador que a notificação é indevida e atrasaria 45–90 dias sem necessidade"},
        {"achado": "Contrato público Sorocaba — alteração societária admitida com comunicação; responsável técnico sai → substituir no CREA/Administração", "efeito": "prazo", "solucao": "plano de transição do RT"},
        {"achado": "2.3 earn-out: EBITDA apurado pelo comprador com rateios do grupo", "efeito": "preco", "solucao": "práticas históricas; excluir rateios/integração; covenant de curso normal; perito"},
        {"achado": "9.1 não concorrência 10 anos / nacional", "efeito": "nenhum para quem se aposenta, mas desproporcional (CC 1.147: 5 anos)", "solucao": "5 anos, área de atuação"},
        {"achado": "Preferência dos sócios (30 dias) no contrato social", "efeito": "prazo", "solucao": "renúncia formal pelos sócios no fechamento"},
        {"achado": "Sucessão: na compra de quotas não há sucessão (CTN 133 / CLT 448-A são sobre a mesma PJ) — o passivo fica na sociedade e por isso o comprador exige indenização; vendedor precisa de limites", "efeito": "indenizacao", "solucao": "dimensionar tetos por matéria"}],
        "falso_positivo": "CADE — não exigir/aceitar notificação", "resposta_ao_comprador": "Anexo 3.2 não é 'não aplicável' (Horizonte Azul); CADE não se aplica; 8.4(c) recusada quanto a matérias reveladas; 5.7/5.9 qualificadas por anexo"}
    c.reference("reference.json", ref)
    c.trap(1, "Anexo 3.2 'não aplicável'", "Aceitar", "Cláusula 19 Horizonte Azul (31% da receita): mudança de controle sem anuência = rescisão + multa", "Data room 1.1", "Perda do maior cliente após o fechamento; indenização", "C", "", "high")
    c.trap(2, "Declarações limpas + sandbagging + teto = preço", "Assinar 5.7, 5.9 e 8.4 como estão", "PJs e CND positiva foram revelados; o comprador indeniza-se por risco conhecido até o preço total por 5 anos; pushback chama de 'padrão'", "Data room 2.2, 3.1; minuta 8.4(b)(c); script 'revelado'", "Vendedores devolvem boa parte do preço", "C", "Prática de M&A", "high")
    c.trap(3, "CADE", "Notificar ou aceitar como condição precedente", "Limiares não atingidos (art. 88)", "Data room 4.2; biblioteca", "Atraso de meses; custo", "M", "Lei 12.529 art. 88", "high")
    c.trap(4, "Earn-out", "Deixar a definição de EBITDA do comprador", "Pode zerar o earn-out", "2.3", "R$ 1,5 mi em risco", "H", "", "high")
    c.trap(5, "Não ver a CND positiva como problema de contrato público", "Tratar o débito só como passivo", "Regularidade fiscal exigida na execução de contratos administrativos; CPEN via parcelamento/garantia", "3.1; Lei 14.133", "Retenção de pagamentos/sanção", "M", "Lei 14.133 art. 92 XVI", "high")
    c.oracle("achados inclui Horizonte Azul cl. 19 (anuência)", "true", "exact", "achados.json")
    c.oracle("achados inclui PJs (pejotização) e CND positiva como exceções às declarações", "true", "exact", "")
    c.oracle("redline: 8.4(c) limitada quanto a matérias reveladas; 5.7 e 5.9 qualificadas; limites/prazos reduzidos", "true", "exact", "")
    c.oracle("CADE: não notificável (resposta ao comprador)", "true", "exact", "")
    c.oracle("earn-out: definição de EBITDA corrigida", "true", "exact", "")
    c.rubric("nota_socios.md: três itens de dinheiro; pushback respondido")
    return c.finish()
