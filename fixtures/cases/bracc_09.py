"""BRACC-9 · L3 · Distribuição de lucros — 'é presumido, distribui isento até o limite'."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

ANO = 2026


def build():
    c = Case("bracc_09_distribuicao_lucros", "bracc", "Distribuição de lucros com prejuízo contábil, débito fiscal e a Lei 15.270/2025", "L3", cur="BRL")
    receita_2025 = D("6400000")
    base_presumida = q2(receita_2025 * D("0.32"))                 # 2.048.000
    tributos = q2(base_presumida * D("0.15") + (base_presumida - D("240000")) * D("0.10") + base_presumida * D("0.09") + receita_2025 * D("0.0365"))
    limite_presumido_liquido = base_presumida - tributos         # "isento até" segundo a IN 1.700 art. 238 §2º I — SE houver lucro
    lucro_contabil_2025 = D("-310000")
    prejuizos_acumulados = D("-1120000")
    pedido = D("800000")
    c.doc("balanco_ecd_2025.md", f"""
# Nexo Logística Ltda. — Balanço patrimonial 31/12/2025 (ECD transmitida)
| Ativo | | Passivo e PL | |
|---|---:|---|---:|
| Caixa e equivalentes | 1.950.000 | Fornecedores | 2.240.000 |
| Clientes | 3.100.000 | Empréstimos | 2.900.000 |
| Imobilizado líquido | 4.800.000 | Tributos a recolher | 610.000 |
| | | **Tributos em discussão (auto de infração, sem garantia)** | **1.480.000** |
| | | Capital social | 4.500.000 |
| | | **Prejuízos acumulados** | **({money(-prejuizos_acumulados, 'BRL')})** |
| **Total** | **9.850.000** | **Total** | **9.850.000** |

DRE 2025: receita bruta {money(receita_2025, 'BRL')}; **resultado do exercício: prejuízo de {money(-lucro_contabil_2025, 'BRL')}** (margens pressionadas, juros).
Regime: **Lucro Presumido** (serviços de transporte/logística — presunção 32% nos serviços auxiliares; 8% no transporte de carga — a empresa usa 32% por conservadorismo; **manter 32% nesta tarefa**).
""")
    c.doc("relatorio_situacao_fiscal.md", "# e-CAC — Relatório de Situação Fiscal (emitido 10/01/2026)\n- Auto de infração IRPJ/CSLL 2022 — R$ 1.480.000 (principal + multa 75% + juros) — **impugnação apresentada, pendente de julgamento na DRJ**; **sem depósito, sem garantia, sem parcelamento**. Exigibilidade: suspensa (CTN 151, III).\n- Demais tributos: regulares.")
    c.doc("email_socios.txt", f"""
De: Sócio A
Assunto: distribuição de janeiro

A gente quer distribuir **{money(pedido, 'BRL')}** em janeiro (metade pra cada). A contadora anterior dizia que no
Presumido pode distribuir isento até a base presumida menos os impostos — dá uns R$ 1,5 mi, então 800 mil
está folgado. Se tiver algum problema com isso, faz um **mútuo** pra mim de 400 mil, mais simples.
E aquele auto de infração está em discussão, não conta como dívida, né?
""")
    c.library("lei9249_art10_in1700_238.md", "Isenção de lucros distribuídos — Lei 9.249 art. 10; IN RFB 1.700 art. 238", "Lei 9.249/95, art. 10; IN RFB 1.700/2017, art. 238, §§1º-4º", "Art. 10: os lucros ou dividendos **calculados com base nos resultados apurados** a partir de 1996, pagos ou creditados pelas pessoas jurídicas tributadas com base no lucro real, presumido ou arbitrado, não ficarão sujeitos ao IR na fonte nem integrarão a base do beneficiário. IN 1.700 art. 238 §2º: no lucro presumido, pode ser distribuído sem incidência: I – o valor da base de cálculo do imposto, diminuída de todos os impostos e contribuições a que estiver sujeita a PJ; II – a parcela excedente **desde que a empresa demonstre, por escrituração contábil, que o lucro efetivo é maior**. **§3º/§4º: a parcela dos rendimentos pagos que exceder o valor apurado na escrituração (ou o limite do inciso I, se não houver escrituração) é tributada** como rendimento do beneficiário (tabela progressiva / IRRF). **Pressuposto de qualquer distribuição isenta é a existência de lucro**: com prejuízo contábil no exercício e prejuízos acumulados, não há lucro a distribuir — pagamentos aos sócios a esse título são **devolução de capital/retirada**, sujeitos a recaracterização (pró-labore ou rendimento tributável) e à responsabilidade dos sócios (CC 1.009; Lei 6.404 art. 201 por analogia).", verbatim=False, note="Verificar redação atual do art. 238 e a posição da RFB sobre distribuição com prejuízo acumulado (SC COSIT).")
    c.library("lei4357_art32.md", "Lei 4.357/64, art. 32 — vedação de distribuição com débito não garantido", "Lei 4.357/64, art. 32, com redação da Lei 11.051/2004", "As pessoas jurídicas, enquanto estiverem **em débito, não garantido, para com a União e suas autarquias de Previdência e Assistência Social, por falta de recolhimento de imposto, taxa ou contribuição, no prazo legal**, não poderão: a) distribuir quaisquer bonificações a seus acionistas; **b) dar ou atribuir participação de lucros a seus sócios ou quotistas**, bem como a seus diretores e demais membros de órgãos dirigentes, fiscais ou consultivos. §1º: multa de **50% das quantias distribuídas** (PJ) e 50% (beneficiários), **limitada a 50% do valor total do débito não garantido**. *Interpretação: débito com exigibilidade suspensa por impugnação administrativa (CTN 151 III) — a RFB tem entendido que a vedação alcança débito 'não garantido' mesmo em discussão administrativa? Posição controvertida: parte da doutrina e julgados do CARF entendem que, suspensa a exigibilidade, não há 'débito em atraso' para fins do art. 32 (Acórdão CARF 1402-00.xxx); a Solução de Consulta COSIT nº 30/2016 sustenta a vedação apenas para débitos exigíveis e não garantidos. Esta biblioteca: há **risco relevante e controvérsia**; o parecer deve expô-la.*", verbatim=False, note="Verificar SC COSIT e jurisprudência do CARF sobre art. 32 e exigibilidade suspensa — item de rubrica, não de porta.")
    c.library("ddl_mutuo_socio.md", "Mútuo a sócio e distribuição disfarçada de lucros", "Decreto-Lei 1.598/77, art. 60; Lei 9.430/96; Decreto 6.306/2007 (IOF) art. 13; RIR/2018 arts. 528-532", "Presume-se distribuição disfarçada de lucros no negócio pelo qual a PJ **empresta dinheiro a pessoa ligada** se, na data do empréstimo, possui lucros acumulados ou reservas de lucros (art. 60, V); fora dessa hipótese, o mútuo a sócio deve ter **contrato escrito, juros de mercado, prazo e garantias**, sujeita-se ao **IOF-crédito** (0,0082% ao dia + 0,38%) e, se não houver intenção/capacidade de pagamento, é recaracterizado como rendimento (pró-labore/dividendo). Mútuo a sócio com a PJ em prejuízo e com débito fiscal é sinal de retirada disfarçada.", verbatim=False)
    c.library("lei15270_2026.md", "Lei 15.270/2025 — tributação de dividendos a partir de 2026", "Lei 15.270/2025", "A partir de 01/01/2026: dividendos pagos a PF residente por uma mesma PJ **acima de R$ 50.000 no mês** → **IRRF de 10%** sobre o total, antecipação do IRPFM. **Regra de transição:** lucros apurados até 2025 cuja distribuição tenha sido **aprovada até 31/12/2025** (ata/deliberação) permanecem isentos quando pagos até 2028. Lucro de 2025 sem deliberação até 31/12/2025 **não** se beneficia da transição.", verbatim=False, note="Verificar.")
    c.library("cc_1009.md", "Código Civil, art. 1.009", "CC art. 1.009", "A distribuição de lucros ilícitos ou fictícios acarreta responsabilidade solidária dos administradores que a realizarem e dos sócios que os receberem, conhecendo ou devendo conhecer-lhes a ilegitimidade.", verbatim=True)
    c.contract(f"""
# Engajamento: distribuição de lucros de janeiro/{ANO} — Nexo Logística Ltda.

Os sócios querem {money(pedido, 'BRL')} "isentos" ou, alternativamente, um mútuo. Diga o que é possível.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.md` — pode distribuir? quanto, a que título, com que tributação em {ANO}? o auto de infração importa? o mútuo é alternativa?
2. `numeros.json` — `{{"limite_presumido_liquido_teorico": 0, "lucro_contabil_2025": 0, "prejuizos_acumulados": 0, "lucro_distribuivel": 0, "distribuicao_recomendada": 0, "irrf_10pct_se_distribuir_800k": 0, "multa_art32_risco": 0, "mutuo": {{"recomendado": true/false, "condicoes": ""}}}}`
3. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Sócio A, impaciente; Sócio B, mais cauteloso.", [
        {"id": "auto", "trigger": ["auto de infração", "impugnação", "garantia", "depósito", "1.480"], "answer": "Sócio B: impugnamos em 2024, está na DRJ. Não depositamos nem demos garantia — o advogado disse que não precisava.", "if_not_asked": "none"},
        {"id": "deliberacao_2025", "trigger": ["ata", "deliberação", "aprovou", "31/12", "transição"], "answer": "Sócio A: não fizemos ata nenhuma em dezembro. A gente distribui quando dá.", "if_not_asked": "none"},
        {"id": "mutuo", "trigger": ["mútuo", "contrato", "juros", "prazo", "pagar de volta"], "answer": "Sócio A: mútuo sem juros, pago quando a empresa melhorar. Sem papelada.", "if_not_asked": "none"},
    ], pushback=[{"when": "se o parecer negar a distribuição", "message": "Sócio A: A contadora anterior fazia isso todo ano. Se a lei diz que no Presumido pode até a base menos impostos, o prejuízo contábil é só uma formalidade da ECD. Faz os 800 mil como 'antecipação de lucros futuros' então."}])
    ref = {"limite_presumido_liquido_teorico": limite_presumido_liquido, "lucro_contabil_2025": lucro_contabil_2025, "prejuizos_acumulados": prejuizos_acumulados, "lucro_distribuivel": 0, "distribuicao_recomendada": 0,
           "irrf_10pct_se_distribuir_800k": q2(pedido * D("0.10")), "multa_art32_risco": min(q2(pedido * D("0.50")), q2(D("1480000") * D("0.50"))),
           "mutuo": {"recomendado": False, "condicoes": "só com contrato escrito, juros de mercado, prazo, IOF, capacidade de pagamento — e mesmo assim desaconselhável com prejuízo e débito fiscal (DDL/recaracterização)"},
           "pontos": ["Com prejuízo no exercício e prejuízos acumulados, NÃO há lucro a distribuir; o 'limite presumido' pressupõe lucro", "'Antecipação de lucros futuros' = retirada sem lucro → recaracterização como rendimento tributável/pró-labore + CC 1.009", "Art. 32 Lei 4.357: risco de multa de 50% com débito não garantido — controvérsia quanto à exigibilidade suspensa; expor o risco e recomendar garantia/parcelamento antes de qualquer distribuição futura", "2026: IRRF 10% acima de R$ 50 mil/mês; sem ata até 31/12/2025, sem transição", "Alternativa lícita: pró-labore (tributado) e/ou redução de capital (formalidades, credores, CC 1.082-1.084) — não 'lucros'"]}
    c.reference("reference.json", ref)
    c.trap(1, "Distribuir 'lucro' com prejuízo contábil", f"{money(pedido, 'BRL')} isentos 'até o limite presumido'", "Não há lucro; o limite do art. 238 §2º I pressupõe lucro; pagamento = retirada/devolução de capital → recaracterização + CC 1.009; pushback 'antecipação de lucros futuros' idem", "Balanço (prejuízo 2025 e acumulados); pushback", "IRRF/recaracterização; responsabilidade solidária", "C", "Lei 9.249 art. 10; IN 1.700 art. 238; CC 1.009", "high")
    c.trap(2, "Débito fiscal não garantido", "'Está em discussão, não conta'", "Art. 32 Lei 4.357: vedação e multa de 50%; controvérsia sobre exigibilidade suspensa deve ser exposta, não ignorada", "Relatório de situação fiscal; script", "Multa de até 50%", "H", "Lei 4.357 art. 32", "medium — controvérsia; graded on disclosure, not on one conclusion")
    c.trap(3, "'Isento' em 2026", "Ignorar a Lei 15.270", "IRRF 10% acima de R$ 50 mil/mês; sem ata até 31/12/2025 não há transição", "Biblioteca; script", "Retenção não feita", "H", "Lei 15.270", "medium — verificar")
    c.trap(4, "Mútuo informal como saída", "Mútuo de R$ 400 mil sem juros/prazo", "DDL/recaracterização; IOF; contrato; com prejuízo e débito é retirada disfarçada", "Script", "Autuação", "H", "DL 1.598 art. 60", "high")
    c.oracle("lucro_distribuivel", "0", "exact", "numeros.json")
    c.oracle("distribuicao_recomendada", "0", "exact", "")
    c.oracle("parecer menciona art. 32 Lei 4.357 e a controvérsia da exigibilidade suspensa", "true", "exact", "parecer.md")
    c.oracle("parecer menciona IRRF 10% (Lei 15.270) e ausência de ata até 31/12/2025", "true", "exact", "")
    c.oracle("mutuo.recomendado", "false", "exact", "")
    c.rubric("Pushback 'antecipação de lucros futuros' recusado com fundamento")
    return c.finish()
