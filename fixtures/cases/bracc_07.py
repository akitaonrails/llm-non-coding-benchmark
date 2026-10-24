"""BRACC-7 · L3 · Holding patrimonial — 'integraliza os imóveis, faz a doação, está resolvido'."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

ANO = 2026


def build():
    c = Case("bracc_07_holding_patrimonial", "bracc", "Holding patrimonial: ITBI, aluguéis PF × PJ, sucessão e legítima", "L3", cur="BRL")
    imoveis = [("Apto Jardins", 1800000, 520000, 7200), ("Apto Pinheiros", 1200000, 380000, 5200), ("Sala comercial Faria Lima 1", 1500000, 410000, 9800), ("Sala comercial Faria Lima 2", 1500000, 410000, 9800),
               ("Loja Rua Augusta", 2200000, 600000, 14000), ("Galpão Guarulhos", 3100000, 900000, 22000), ("Casa Campos do Jordão", 1400000, 350000, 0), ("Apto Moema", 950000, 300000, 4300),
               ("Apto Perdizes", 880000, 280000, 4100), ("Terreno Cotia", 600000, 150000, 0), ("Sala Berrini", 1300000, 420000, 8500)]
    vm = sum(D(x[1]) for x in imoveis); vd = sum(D(x[2]) for x in imoveis); alug_mes = sum(D(x[3]) for x in imoveis)
    alug_ano = alug_mes * 12
    # PF: carnê-leão 27,5% − dedução; simplificado: aluguel líquido de despesas; usar tabela progressiva anual aproximada → efetivamente ~25% marginal sobre esse volume
    irpf_pf = q2(alug_ano * D("0.275") - D("10432.32"))   # aprox. anual (parcela a deduzir anual da última faixa — verificar)
    # PJ Presumido: IRPJ 15% s/ 32% + adicional; CSLL 9% s/ 32%; PIS/COFINS 3,65%; sem ISS (locação); 2026: CBS/IBS teste; distribuição > 50k/mês → IRRF 10%
    base = q2(alug_ano * D("0.32"))
    irpj = q2(base * D("0.15") + max(D("0"), base - D("240000")) * D("0.10"))
    csll = q2(base * D("0.09"))
    piscofins = q2(alug_ano * D("0.0365"))
    pj_trib = irpj + csll + piscofins
    liquido_pj = alug_ano - pj_trib
    irrf_div = q2(liquido_pj * D("0.10"))  # distribuição mensal > 50k
    pj_total = pj_trib + irrf_div
    itbi = q2(vm * D("0.03"))  # SP 3%
    itcmd_quotas = q2(vd * D("0.04"))  # SP 4% sobre valor venal/declarado das quotas (simplificação)
    c.doc("relacao_imoveis.csv", "imovel,valor_mercado,valor_declaracao_ir,aluguel_mensal,uso\n" + "\n".join(f"{n},{m},{d},{a},{'locado' if a else 'uso proprio/ferias'}" for n, m, d, a in imoveis))
    c.doc("familia.md", f"""
# Situação familiar — Dona Helena Furtado, 71 anos, viúva (comunhão parcial, viúva desde 2019)
- Três filhos: **Ricardo** (48, médico), **Paula** (45, arquiteta) e **Marcos** (41) — com Marcos a relação está rompida há 6 anos; ela "não quer deixar nada para ele".
- Patrimônio: 11 imóveis (relação anexa; valor de mercado {money(vm, 'BRL')}; valor nas declarações {money(vd, 'BRL')}), aplicações R$ 2,1 mi.
- Renda: aluguéis {money(alug_mes, 'BRL')}/mês, declarados no carnê-leão.
- Saúde boa. Não há testamento.
""")
    c.doc("palestra_resumo.md", f"""
# "Holding familiar: pague 11% nos aluguéis e proteja seus herdeiros" — anotações da Dona Helena
1. Integralizar todos os imóveis numa holding **sem ITBI** (imunidade constitucional).
2. Aluguel na PJ paga "só 11,33%" em vez de 27,5% na PF.
3. Doar as quotas aos filhos **com reserva de usufruto**, pagando ITCMD de 4% sobre o valor contábil (baixo) — "sucessão resolvida, sem inventário".
4. "Quem você não quiser que herde, simplesmente não recebe quotas."
5. Cláusulas de incomunicabilidade, impenhorabilidade e inalienabilidade protegem contra genros e credores.
""")
    c.library("cf156_ctn37_tema796.md", "ITBI — imunidade na integralização; exceção; Tema 796", "CF art. 156, §2º, I; CTN art. 37; STF RE 796.376 (Tema 796, 2020)", "Imunidade na integralização de capital, **salvo se a atividade preponderante do adquirente for compra e venda, locação de bens imóveis ou arrendamento mercantil** (mais de 50% da receita operacional nos 2 anos anteriores e 2 posteriores; empresa nova: 3 anos seguintes — CTN 37 §§1º-2º). **Tema 796:** a imunidade não alcança o valor dos imóveis que **exceder o capital social integralizado**. Alíquota do ITBI no Município de São Paulo: **3%**. *Nota do bibliotecário: há repercussão geral pendente sobre o alcance da exceção na integralização (RE 1.495.108, Tema 1.348); esta biblioteca aplica a literalidade da CF e do CTN.*", verbatim=False)
    c.library("lei9249_art23.md", "Lei 9.249/95, art. 23 — integralização pelo valor da declaração", "Lei 9.249/95, art. 23", "Pessoas físicas podem integralizar bens **pelo valor da declaração ou pelo de mercado**; pelo valor da declaração não há ganho de capital; pelo de mercado, a diferença é tributável (GCAP, 15%-22,5%).", verbatim=True)
    c.library("cc_legitima_doacao.md", "Código Civil — legítima, doação inoficiosa, colação, cláusulas restritivas", "CC arts. 544, 549, 1.789, 1.845, 1.846, 1.848, 2.002-2.012", "**Art. 1.845/1.846.** São herdeiros necessários os descendentes, ascendentes e o cônjuge; **pertence-lhes, de pleno direito, a metade dos bens da herança (legítima)**. **Art. 549.** É **nula** a doação quanto à parte que exceder a de que o doador, no momento da liberalidade, poderia dispor em testamento (**doação inoficiosa**). **Art. 544.** A doação de ascendente a descendente importa **adiantamento da legítima** (sujeita a colação, art. 2.002). **Art. 1.848.** O testador **não pode** estabelecer cláusula de inalienabilidade, impenhorabilidade e incomunicabilidade sobre os bens da legítima, **salvo se houver justa causa declarada no testamento**. Consequência: um filho só pode ser excluído da legítima por **deserdação com causa legal** (arts. 1.961-1.965) ou indignidade; doar as quotas só a dois filhos é inoficiosa quanto ao que invade a legítima do terceiro (que pode pedir redução).", verbatim=False)
    c.library("itcmd_sp_lei10705.md", "ITCMD/SP — Lei 10.705/2000 (excertos) e EC 132/2023", "Lei estadual 10.705/2000, arts. 2º, 9º, 13, 16; EC 132/2023, art. 155 §1º VI CF", "Incide ITCMD na **doação de quotas**, inclusive com reserva de usufruto (base: valor das quotas — a SEFAZ/SP exige **valor patrimonial atualizado/valor de mercado dos bens da PJ**, não o valor contábil histórico, quando este for inferior — Decreto 46.655/2002, art. 14 §4º e jurisprudência do TJSP). Alíquota em SP: **4%** (projetos de lei de progressividade em tramitação; a EC 132/2023 tornou **obrigatória a progressividade** do ITCMD, pendente de lei estadual). Doação com reserva de usufruto: 2/3 na doação da nua-propriedade e 1/3 na extinção do usufruto (art. 9º §2º-ish — verificar), ou integral conforme opção.", verbatim=False, note="Verificar base de cálculo e regra 2/3–1/3 na legislação paulista vigente.")
    c.library("locacao_pf_vs_pj.md", "Tributação de aluguéis — PF (carnê-leão) × PJ (Presumido) — 2026", "Lei 9.250/95 (tabela progressiva); Lei 9.249/95 art. 15 §1º III c; Lei 15.270/2025; LC 214/2025 art. 251 ss. (locação)", f"**PF:** aluguéis recebidos de PF sujeitam-se ao carnê-leão pela tabela progressiva mensal (até 27,5%); deduções: IPTU, condomínio pagos pelo locador, comissão de administração. **PJ no Presumido:** presunção de **32%** sobre a receita de locação → IRPJ 15% + adicional 10% (acima de R$ 20 mil/mês); CSLL 9% sobre 32%; PIS/COFINS 3,65%; **sem ISS** (locação de imóvel não é serviço) → carga ≈ 11,33% até o limite do adicional, ≈ **14,53%** acima. **A partir de 2026 (Lei 15.270):** distribuição de lucros acima de R$ 50 mil/mês por PJ a uma PF → **IRRF 10%**, elevando a carga efetiva para o sócio. **LC 214/2025:** locação de imóveis por PJ entra no IBS/CBS com **redutor de 70% das alíquotas** (regra geral) no regime definitivo; em 2026 apenas apuração-teste.", verbatim=False, note="Verificar redutor e condições da LC 214 para locação.")
    c.contract(f"""
# Engajamento: planejamento patrimonial e sucessório — Dona Helena Furtado

Ela saiu de uma palestra convencida de cinco afirmações (ver `palestra_resumo.md`). Avalie cada uma
com números e proponha o que é possível.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.md` — cada afirmação da palestra: verdadeira/falsa/depende, com fundamento; estrutura recomendada; limites.
2. `numeros.json` — `{{"itbi": {{"devido": true/false, "estimativa": 0, "fundamento": ""}}, "aluguel_anual": 0, "pf": {{"ir_anual": 0}}, "pj_presumido": {{"irpj_csll_pis_cofins": 0, "irrf_distribuicao_2026": 0, "total": 0}}, "integralizacao": {{"valor_recomendado": 0, "gcap_evitado": 0}}, "itcmd_doacao_quotas": {{"estimativa": 0, "base": ""}}, "legitima": {{"parcela_indisponivel_pct": 50, "marcos_pode_ser_excluido": false}}}}`
3. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Dona Helena, 71; firme; magoada com Marcos; quer o que a palestra prometeu.", [
        {"id": "marcos", "trigger": ["Marcos", "excluir", "deserdar", "legítima", "terceiro filho"], "answer": "Ele não fala comigo há seis anos. Não quero que receba nada. Se a lei obriga, quero o mínimo possível e com as cláusulas de proteção.", "if_not_asked": "none"},
        {"id": "uso_proprio", "trigger": ["Campos do Jordão", "Cotia", "uso próprio", "moradia"], "answer": "A casa de Campos é da família, ninguém aluga. O terreno de Cotia é para os netos um dia. Eu moro no Jardins — ah não, o Jardins está alugado; moro em Higienópolis, que é alugado por mim.", "if_not_asked": "none"},
        {"id": "deducoes", "trigger": ["IPTU", "condomínio", "administradora", "despesas dos imóveis"], "answer": "A administradora cobra 8%; IPTU e condomínio dos vagos eu pago.", "if_not_asked": "none"},
    ], pushback=[{"when": "se o parecer disser que Marcos não pode ser excluído", "message": "Dona Helena: O palestrante disse que com a holding eu decido quem recebe quotas. Se eu doar tudo em vida para o Ricardo e a Paula, o que sobra para o Marcos herdar? Nada, certo?"}])
    ref = {"itbi": {"devido": True, "estimativa": itbi, "fundamento": "atividade preponderante = locação (todas as receitas); exceção do art. 156 §2º I; Tema 796 para o excedente"},
           "aluguel_anual": alug_ano, "pf": {"ir_anual_aprox": irpf_pf, "nota": "bruto; deduções (IPTU/condomínio/administração 8%) reduzem"},
           "pj_presumido": {"irpj_csll_pis_cofins": pj_trib, "irrf_distribuicao_2026": irrf_div, "total": pj_total, "carga_pct_sem_irrf": q2(pj_trib / alug_ano * 100), "carga_pct_com_irrf": q2(pj_total / alug_ano * 100)},
           "integralizacao": {"valor_recomendado": vd, "gcap_evitado": q2((vm - vd) * D("0.15"))},
           "itcmd_doacao_quotas": {"estimativa_4pct_valor_declaracao": itcmd_quotas, "base": "SEFAZ/SP tende a exigir valor de mercado dos bens → " + str(q2(vm * D('0.04')))},
           "legitima": {"parcela_indisponivel_pct": 50, "marcos_pode_ser_excluido": False, "nota": "doação só a Ricardo e Paula é adiantamento de legítima (colação) e inoficiosa no que exceder a parte disponível; Marcos pode pedir redução; cláusulas restritivas sobre a legítima exigem justa causa em testamento (CC 1.848)"},
           "afirmacoes": {"1_sem_itbi": "FALSA (atividade preponderante locação)", "2_11pct": "PARCIAL: ~11,3–14,5% na PJ antes da distribuição; +10% IRRF em 2026 na distribuição > 50k/mês; PF tem deduções — comparar líquido", "3_itcmd_valor_contabil": "FALSA/ARRISCADA: SP exige valor de mercado; usufruto 2/3-1/3", "4_excluir_filho": "FALSA: legítima de 50%; deserdação só com causa legal", "5_clausulas": "PARCIAL: válidas sobre a parte disponível; sobre a legítima só com justa causa (CC 1.848)"}}
    c.reference("reference.json", ref)
    c.trap(1, "Imunidade de ITBI", "Holding de locação 'sem ITBI'", f"Atividade preponderante = locação → ITBI devido ≈ {money(itbi, 'BRL')}; Tema 796 no excedente", "Relação de imóveis (todos locados); CF/CTN", "Autuação em 11 imóveis", "C", "CF 156 §2º I; CTN 37", "high")
    c.trap(2, "Excluir Marcos", "Doar quotas só a dois filhos", "Legítima 50% (CC 1.846); doação inoficiosa nula no excesso (CC 549); colação (CC 544); cláusulas sobre legítima só com justa causa (CC 1.848); pushback 'se eu doar tudo em vida não sobra nada' é exatamente a doação inoficiosa", "familia.md; script; pushback", "Plano anulado judicialmente após a morte; litígio entre irmãos", "C", "CC 549, 1.846, 1.848", "high")
    c.trap(3, "'Aluguel a 11%'", "Repetir o número da palestra", f"PJ {q2(pj_trib/alug_ano*100)}% antes da distribuição; com IRRF 10% (2026) {q2(pj_total/alug_ano*100)}%; PF tem deduções (adm 8%, IPTU) — comparar líquido; LC 214 muda a locação no regime definitivo", "Biblioteca", "Promessa falsa; decisão errada", "H", "Lei 15.270; Lei 9.249 art. 15", "high")
    c.trap(4, "Integralizar a valor de mercado", "Imóveis pela avaliação", f"Art. 23 Lei 9.249: pelo valor da declaração evita GCAP de ≈ {money(q2((vm - vd) * D('0.15')), 'BRL')}", "Relação (valor declaração)", "IR desnecessário", "H", "Lei 9.249 art. 23", "high")
    c.trap(5, "ITCMD sobre valor contábil", "4% sobre valor histórico", "SP exige valor de mercado dos bens; usufruto 2/3–1/3; progressividade obrigatória pendente", "Biblioteca", "Autuação ITCMD", "M", "Lei 10.705", "medium — verificar base")
    c.trap(6, "Imóveis de uso próprio na holding", "Integralizar Campos do Jordão e Cotia", "Sem receita; uso pela família gera DDL/aluguel ficto e complica; manter fora", "Script", "Complexidade e risco fiscal", "L", "", "medium")
    c.oracle("itbi.devido", "true", "exact", "numeros.json")
    c.oracle("legitima.marcos_pode_ser_excluido", "false", "exact", "")
    c.oracle("integralizacao.valor_recomendado", str(vd), "exact", "")
    c.oracle("pj_presumido.total inclui IRRF 2026 ≈", str(pj_total), "±3%", "")
    c.oracle("Parecer classifica as 5 afirmações", "true", "exact", "parecer.md")
    c.rubric("Pushback: explica doação inoficiosa/colação em linguagem simples")
    return c.finish()
