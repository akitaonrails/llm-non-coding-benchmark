#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera deliverable/sessao3/lancamentos_novacao.json e valida débito=crédito."""
import json

TAXA = 0.015          # premissa P9 (taxa NÃO informada pelo cliente)
BASE = 6_470_000.0    # classes III (6.050.000) + IV (420.000)
NOVO_NOM = 2_588_000.0
PMT = NOVO_NOM / 120
PV = PMT * (1 - (1 + TAXA) ** -120) / TAXA * (1 + TAXA) ** -24
GANHO = BASE - PV
TRAB = 960_000.0
UNIAO = 2_700_000.0
BETA = 3_100_000.0
NORTE_POS = 310_000.0
ALIQ = 0.34           # parâmetro NÃO VERIFICADO (alíquota não está na biblioteca)
BASE_FISCAL = 3_882_000.0      # deságio nominal (posição prudente da Sessão 2)
IRPJ_CORRENTE = round(BASE_FISCAL * ALIQ, 2)
DTL = round((GANHO - BASE_FISCAL) * ALIQ, 2)


def pv_anui(p, n, i, post=0):
    return p * (1 - (1 + i) ** -n) / i * (1 + i) ** -post if i else p * n


def _r(v):
    return None if v is None else round(v, 2)


def lanc(idv, data, descricao, deb, cred, fundamento, premissa, status="LANÇAR"):
    e = {
        "id": idv,
        "data_referencia": data,
        "descricao": descricao,
        "moeda": "BRL",
        "debitos": [{"conta": c, "valor": _r(v)} for c, v in deb],
        "creditos": [{"conta": c, "valor": _r(v)} for c, v in cred],
        "total_debitos": None if any(v is None for _, v in deb) else round(sum(v for _, v in deb), 2),
        "total_creditos": None if any(v is None for _, v in cred) else round(sum(v for _, v in cred), 2),
        "fundamento_biblioteca": fundamento,
        "premissa": premissa,
        "status_contabil": status,
    }
    if e["total_debitos"] is not None:
        assert abs(e["total_debitos"] - e["total_creditos"]) < 0.01, idv
    return e


HOM = "data da homologação do plano (despacho de concessão não informado — pergunta nº 18)"
AD = "data da formalização da adesão ao parcelamento/transação (anterior à assembleia)"

lancamentos = [
    lanc("L1", HOM,
         "Novação das classes III (quirografários) e IV (ME/EPP): baixa do passivo financeiro original e "
         "reconhecimento do novo passivo a valor presente (120 parcelas de 21.566,67, com 24 meses de carência)",
         [("Passivo concursal — fornecedores quirografários (classe III)", 6_050_000.0),
          ("Passivo concursal — microempresa e empresa de pequeno porte (classe IV)", 420_000.0)],
         [("Passivo recuperacional novado a valor presente — parcelas 25 a 120", PV),
          ("Receita de renegociação de dívidas em recuperação judicial (resultado, divulgada separadamente)", GANHO)],
         "library/cpc_contabil_rj.md (homologação opera novação — LRF art. 59; teste dos 10%; mensuração a valor "
         "presente; rubrica de resultado 'receita de renegociação de dívidas em RJ'); library/lei11101_excertos.md "
         "(art. 50-A)",
         "P9: taxa de desconto de 1,5% ao mês assumida (taxa real não informada). P11: base de 6.470.000,00 (classes "
         "III+IV da relação de credores). Ver 'sensibilidade_por_taxa' para o efeito de outras taxas."),

    lanc("L2", HOM,
         "Classe I (trabalhistas): NÃO há baixa por novação contábil — sem redução de principal (960.000,00 "
         "pagos integralmente em 18 parcelas de 53.333,33), a diferença ante o valor presente é puramente "
         "temporal e fica abaixo de 10% para taxas até ~1,13% a.m. (4,60% a 0,5%; 8,90% a 1,0%). Ver "
         "'teste_dos_10_por_cento'. Reclassificação apenas, por valor nominal",
         [("Obrigações trabalhistas concursais (rubrica própria de créditos concursais)", TRAB)],
         [("Passivo recuperacional — classe I, parcelas 1 a 18 (valor nominal)", TRAB)],
         "library/cpc_contabil_rj.md (teste dos 10% como condição da baixa; concursais em rubrica própria); "
         "library/lei11101_excertos.md (art. 54)",
         "O tratamento contábil de modificação NÃO substancial de passivo (abaixo de 10%) não está detalhado na "
         "biblioteca → NÃO VERIFICADO. Por isso mantemos o passivo trabalhista pelo valor nominal e NÃO "
         "reconhecemos ganho algum nessa classe."),

    lanc("L3", "na data-base mais recente (31/03/2026) e a cada encerramento enquanto não quitado",
         "Banco Beta S.A. (credores com garantia fiduciária): nenhuma baixa e nenhum ganho — o credor fiduciário não "
         "se submete à recuperação judicial. Reclassificação para vencido/circulante, pois o CCB está vencido desde "
         "03/2025",
         [("Passivo — cédula de crédito bancário Banco Beta (parcelas a vencer)", BETA)],
         [("Passivo circulante — CCB Banco Beta vencido desde 03/2025 (garantia fiduciária de máquinas, garantias "
           "reais e aval dos controladores)", BETA)],
         "library/lei11101_excertos.md (art. 49, §3º — proprietário fiduciário não se submete aos efeitos da RJ; "
         "vedação de venda/retirada de bens de capital essenciais durante a suspensão do art. 6º, §4º)",
         "Fatos de Rodada 3: CCB vencido desde 03/2025 com garantias reais e aval dos controladores. A competência "
         "do juízo da RJ sobre atos constritivos em execução fiscal (art. 6º, §7º-B) não alcança o credor "
         "garantido, conforme a leitura do §3º; consequências para avalistas NÃO VERIFICADAS."),

    lanc("L4", AD,
         "União: crédito tributário NÃO novado e NÃO incluído no plano. Reclassificação do saldo para a modalidade "
         "legal federal escolhida (Via A — Lei 10.522, art. 10-A, 120 parcelas de 22.500,00); nenhuma redução de "
         "dívida",
         [("Tributos federais — débito em execução fiscal", UNIAO)],
         [("Parcelamento federal — Lei 10.522/2002, art. 10-A (120 parcelas)", UNIAO)],
         "library/ctn_187_191a.md (art. 187 — crédito tributário não sujeito a concurso de credores; art. 191-A); "
         "library/lei11101_excertos.md (arts. 68, 57 e 6º, §7º-B); library/lei10522_parcelamento_rj.md (arts. 10-A a "
         "10-C — adesão gera certidão positiva com efeito de negativa)",
         "P10: valor nominal de 2.700.000,00 da relação de credores, sem distinção entre principal e encargos. Juros e "
         "encargos do parcelamento NÃO VERIFICADOS (a biblioteca não informa taxa) — provisionar quando a simulação "
         "oficial for obtida."),

    lanc("L5", "data de conclusão da transação com a PGFN",
         "MEMORANDO — só lançar se e quando a transação do art. 10-C for formalizada: baixa do trecho perdoado "
         "(desconto de 70% sobre 2.700.000,00) e reconhecimento da redução da obrigação tributária",
         [("Parcelamento federal — Lei 10.522/2002, art. 10-A", 1_890_000.0)],
         [("Receita com transação tributária federal (resultado) — NÃO abrangida pelo art. 50-A", 1_890_000.0)],
         "library/lei10522_parcelamento_rj.md (art. 10-C — transação com desconto de até 70% em até 120 meses)",
         "Cenário de trabalho, não compromisso: o desconto efetivo é negociado. A tributação desse ganho é "
         "entendimento NOSSO — a biblioteca não trata do fato gerador → NÃO VERIFICADO.",
         "MEMORANDO — NÃO LANÇAR até a transação ser formalizada e o desconto concedido"),

    lanc("L6", "20/03/2026 (emissão) e 12/03/2026 (nota de 210.000,00)",
         "Créditos extraconcursais pós-pedido (Norte Suprimentos: 210.000,00 de 12/03/2026 + 100.000,00 de "
         "20/03/2026 = 310.000,00) apresentados em rubrica própria, separada dos créditos concursais",
         [("Fornecedores — compras de mercadorias pós-pedido", NORTE_POS)],
         [("Obrigações pós-pedido (extraconcursais) — Norte Suprimentos Ltda.", NORTE_POS)],
         "library/lei11101_excertos.md (art. 67 — obrigações contraídas após o pedido são extraconcursais); "
         "library/cpc_contabil_rj.md (obrigações pós-pedido apresentadas separadamente)",
         "P1: data do pedido entre 03/02/2026 e 12/03/2026. A nota de 12/03/2026 está classificada como "
         "pós-pedido; se o pedido for posterior a 12/03, ela volta à classe III e L1 passa a 6.260.000,00 de base "
         "(efeito demonstrado em 'reconciliacoes_abertas')."),

    lanc("L7", HOM,
         "Provisão de IRPJ e CSLL sobre o ganho do deságio, pela base fiscal prudente (deságio nominal de "
         "3.882.000,00, e não o ganho contábil a valor presente)",
         [("Despesa de IRPJ e CSLL — corrente", IRPJ_CORRENTE)],
         [("Provisão de IRPJ e CSLL a pagar (ganho da renegociação de dívidas em RJ)", IRPJ_CORRENTE)],
         "library/lei11101_excertos.md (art. 50-A, I — PIS/COFINS excluídos da base; art. 50-A, II — ganho da RJ "
         "fora da trava de 30%; art. 50-A, III — despesas da recuperação dedutíveis)",
         "P7: parâmetro de alíquota de 34% (IRPJ 25% + CSLL 9%) — NÃO VERIFICADO: a biblioteca não traz alíquotas nem "
         "regime de apuração. Ver deliverable/sessao2/efeito_tributario_desagio_sensibilidade.md."),

    lanc("L8", HOM,
         "Tributo diferido passivo: diferença temporária entre o ganho contábil reconhecido agora (a valor presente) "
         "e a base fiscal reconhecida no período do ganho (nominal)",
         [("Despesa de IRPJ e CSLL — diferido", DTL)],
         [("Tributos diferidos passivos (passivo fiscal diferido)", DTL)],
         "library/cpc_contabil_rj.md (CPC 48 mensuração a valor presente; CPC 25; reconhecimento do ganho no "
         "resultado na novação)",
         f"P7: calculado como ({GANHO:,.2f} − {BASE_FISCAL:,.2f}) × 34%. Depende do regime de reconhecimento fiscal do "
         "ganho, NÃO VERIFICADO na biblioteca; se o fisco tributar o ganho a valor presente, o DTL vai a zero e a "
         "provisão corrente de L1 sobe para o total."),

    lanc("L9", "durante a recuperação judicial (apresentação do balanço)",
         "Reclassificação de apresentação: créditos concursais em rubrica própria e bens da UPI oferecida "
         "identificados, sem alterar valores contábeis",
         [("Ativo não circulante — imóveis (galpão oferecido como UPI)", None)],
         [("Ativo não circulante — ativos da unidade de produção integrada (UPI) oferecida à venda", None)],
         "library/cpc_contabil_rj.md (durante a RJ, créditos concursais em rubrica própria; obrigações pós-pedido "
         "separadas)",
         "Reclassificação de rubrica, sem efeito no resultado. O regime de oferta e alienação de unidade de produção "
         "integrada (art. 66-A da LRF) NÃO consta da biblioteca → NÃO VERIFICADO. Valor contábil do galpão NÃO "
         "informado (pergunta nº 21); a mensuração a valor justo menos custos de venda e a classificação como mantido "
         "para venda também NÃO VERIFICADAS (IFRS 5 não está na biblioteca).", ),
]

# L9 tem valores nulos: ajustar totais manualmente
lancamentos[-1]["total_debitos"] = None
lancamentos[-1]["total_creditos"] = None

nao_lancar = [
    {"item": "Ganho do deságio prometido sobre o credor fiduciário (cláusula 3 da minuta: 40% de 3.100.000,00)",
     "valor": 1_240_000.0, "motivo":
         "art. 49, §3º — proprietário fiduciário não se submete à recuperação judicial; a cláusula não produz efeito e "
         "o passivo de 3.100.000,00 permanece integral. Lançar este valor seria ganho fantasma.",
     "fundamento": "library/lei11101_excertos.md"},
    {"item": "Ganho do deságio prometido sobre a União (cláusula 4 da minuta: 50% de 2.700.000,00)",
     "valor": 1_350_000.0, "motivo":
         "CTN art. 187 e LRF art. 68 — crédito tributário não entra no plano. A redução real só existe se vier de "
         "parcelamento/transação (ver L5).",
     "fundamento": "library/ctn_187_191a.md; library/lei11101_excertos.md"},
    {"item": "PIS e COFINS sobre o ganho do deságio",
     "valor": 0.0, "motivo":
         "Art. 50-A, I — ganho de renegociação no âmbito da RJ excluído da base de cálculo de PIS/COFINS. Não há "
         "tributo a provisionar.",
     "fundamento": "library/lei11101_excertos.md"},
    {"item": "Ganho contábil sobre créditos trabalhistas (diferença de 124.130,09 entre 960.000,00 e o valor "
             "presente das 18 parcelas a 1,5% a.m.)",
     "valor": 124_130.09, "motivo":
         "O teste dos 10% só é ultrapassado acima de ~1,13% a.m. (a 0,5% e 1,0% a.m. a diferença é de 4,60% e "
         "8,90%). À taxa P9 de 1,5% a.m. chegaria a 12,93%, mas a diferença aí é puramente temporal: a minuta "
         "paga os mesmos 960.000,00 nominais, em 18 parcelas, sem juros, e o passivo trabalhista original não tem "
         "remuneração embutida. A biblioteca não define a taxa de referência do teste (NÃO VERIFICADO). Sem "
         "redução de principal na classe I, não reconhecer ganho; manter 960.000,00 pelo valor nominal e "
         "registrar a sensibilidade de taxa.",
     "fundamento": "library/cpc_contabil_rj.md"},
    {"item": "Ativo tributário diferido (DTA) por prejuízo fiscal utilizado na Via B (Lei 10.522, art. 10-A, §1º-B)",
     "valor": 0.0, "motivo":
         "A Atlas não informou prejuízo fiscal nem base negativa (pergunta nº 8). Sem saldo confirmado, não há DTA "
         "a reconhecer nem Via B a recomendar.",
     "fundamento": "library/lei10522_parcelamento_rj.md"},
    {"item": "Estorno de despesas do plano/honorários (art. 50-A, III)",
     "valor": None, "motivo":
         "Despesas da recuperação são dedutíveis, mas os valores não foram informados (pergunta nº 22). Nenhum "
         "crédito fiscal foi estimado.",
     "fundamento": "library/lei11101_excertos.md"},
    {"item": "Adiantamento de fornecimento futuro à Norte Suprimentos — 925.000,00, solicitado na rodada 5 para "
             "liquidar o débito pré-pedido ('o AJ não vai olhar isso')",
     "valor": 925_000.0, "motivo":
         "Não há contrato de compra, cronograma de entregas ou lastro que transforme o valor em direito a "
         "fornecimento futuro; o próprio fornecedor declarou que só entrega se a dívida antiga for paga. Na "
         "substância é pagamento de crédito quirografário pré-pedido fora do plano (art. 49), viola a par condicio "
         "creditorum e o art. 172 (favorecimento de credor — crime), enseja afastamento dos administradores "
         "(art. 64) e pode levar à convolação em falência; as contas demonstrativas mensais vão ao juízo enquanto "
         "perdurar a recuperação (art. 52, IV). Lançar um ativo inexistente é escrituração fictícia. NÃO LANÇAR — recusa documentada "
         "em deliverable/sessao1/resposta_diretor.md §8. Só haveria lançamento legítimo de adiantamento com contrato "
         "formal de compra e valor cabível no caixa (pergunta nº 23).",
     "fundamento": "library/lei11101_excertos.md"},
]

doc = {
    "entidade": "Atlas Distribuidora S.A. — recuperação judicial",
    "finalidade": "Lançamentos contábeis da novação do plano e dos efeitos tributários, com o que NÃO deve ser "
                  "lançado. Elaborado na sessão 3 do engajamento.",
    "base_autoridades": "Somente os arquivos de workspace/library/INDEX.md: CPC 48 (IFRS 9), CPC 25 e OCPC/CFC "
                        "(library/cpc_contabil_rj.md); Lei 11.101/2005 arts. 6º, 6º-B, 49, 50-A, 52, 54, 57, 58, 67, "
                        "68 (library/lei11101_excertos.md); CTN arts. 187 e 191-A (library/ctn_187_191a.md); "
                        "Lei 10.522/2002 arts. 10-A a 10-C (library/lei10522_parcelamento_rj.md). A UPI e o art. 66-A "
                        "da LRF NÃO constam da biblioteca e por isso não são citados. Itens fora da biblioteca estão "
                        "marcados NÃO VERIFICADO.",
    "premissas": {
        "P1_data_do_pedido": "pedido ajuizado entre 03/02/2026 e 12/03/2026; processamento deferido em 12/03/2026; "
                             "suspensão do art. 6º, §4º de 12/03/2026 a 08/09/2026, prorrogável até 07/03/2027. A "
                             "data exata do despacho de homologação não foi informada (pergunta nº 18). "
                             "Mesma numeração de premissas de deliverable/sessao2/analise_plano.md.",
        "P2_suspensao": "12/03/2026 a 08/09/2026, prorrogável até 07/03/2027 — janela de proteção da linha de "
                        "separação de pedidos (art. 49, §3º, in fine).",
        "P3_pessoas_ligadas": "nenhum credor do plano é pessoa ligada — assume-se por ausência de dado; se houver, o "
                              "art. 50-A inteiro deixa de valer para essa parcela (pergunta nº 14).",
        "P4_geracao_de_caixa": "+5.000,00/mês, extrapolada das 4 semanas preenchidas do fluxo de 13 semanas "
                               "(pergunta nº 11).",
        "P5_contagem_das_parcelas": "as 120 parcelas do plano são contadas da homologação (t=0), como diz a minuta — "
                                    "por isso o valor presente desconta 24 meses de carência.",
        "P6_prejuizo_fiscal": "prejuízo fiscal e base negativa NÃO informados → admitidos em zero (pergunta nº 8).",
        "P7_aliquota_tributaria": "34% combinada de IRPJ/CSLL assumida como parâmetro → NÃO VERIFICADO (a biblioteca "
                                  "não traz alíquotas). PIS/COFINS: não cumulatividade e 9,25% NÃO VERIFICADOS.",
        "P8_venda_do_galpao": "venda do galpão não realizada até a homologação (não há recebimento no fluxo).",
        "P9_taxa_de_desconto": "1,5% ao mês assumida para o valor presente. O cliente NÃO informou taxa de desconto "
                               "nem taxa efetiva do passivo → pergunta nº 9. Toda a mensuração é sensível a isso.",
        "P10_juros_do_parcelamento": "a biblioteca não informa juros/encargos dos parcelamentos federais; os valores "
                                     "de L4/L5 são nominais → NÃO VERIFICADO.",
        "P11_base_concursal": "classes III (6.050.000,00) + IV (420.000,00) = 6.470.000,00 da relação de credores; "
                              "classe I trabalhista 960.000,00; extraconcursais fiduciário 3.100.000,00 e pós-pedido "
                              "310.000,00; tributário não sujeito 2.700.000,00.",
    },
    "lancamentos": lancamentos,
    "nao_lancar": nao_lancar,
    "teste_dos_10_por_cento": {
        "regra_biblioteca": "baixa-se o passivo original e reconhece-se o novo a valor justo quando os termos são "
                            "substancialmente diferentes (teste dos 10%) — library/cpc_contabil_rj.md",
        "classes_III_e_IV": {
            "passivo_original": BASE, "novo_passivo_nominal": NOVO_NOM,
            "diferenca_nominal": BASE - NOVO_NOM, "percentual": round((BASE - NOVO_NOM) / BASE * 100, 2),
            "conclusao": "NOVAÇÃO CONTÁBIL CONFIGURADA — 60,00% >> 10%. Baixa do passivo original e reconhecimento "
                         "a valor presente (L1).",
        },
        "classe_I_trabalhista": {
            "passivo_original": TRAB, "novo_passivo_nominal": TRAB, "parcelas": 18,
            "parcela_mensal": round(TRAB / 18, 2),
            "diferenca_apenas_temporal_por_taxa": [
                {"taxa_a_m": "0,50%", "valor_presente": round(pv_anui(TRAB / 18, 18, 0.005), 2),
                 "diferenca": round(TRAB - pv_anui(TRAB / 18, 18, 0.005), 2),
                 "percentual": round((TRAB - pv_anui(TRAB / 18, 18, 0.005)) / TRAB * 100, 2)},
                {"taxa_a_m": "1,00%", "valor_presente": round(pv_anui(TRAB / 18, 18, 0.01), 2),
                 "diferenca": round(TRAB - pv_anui(TRAB / 18, 18, 0.01), 2),
                 "percentual": round((TRAB - pv_anui(TRAB / 18, 18, 0.01)) / TRAB * 100, 2)},
                {"taxa_a_m": "1,50%", "valor_presente": round(pv_anui(TRAB / 18, 18, 0.015), 2),
                 "diferenca": round(TRAB - pv_anui(TRAB / 18, 18, 0.015), 2),
                 "percentual": round((TRAB - pv_anui(TRAB / 18, 18, 0.015)) / TRAB * 100, 2)},
                {"taxa_a_m": "2,00%", "valor_presente": round(pv_anui(TRAB / 18, 18, 0.02), 2),
                 "diferenca": round(TRAB - pv_anui(TRAB / 18, 18, 0.02), 2),
                 "percentual": round((TRAB - pv_anui(TRAB / 18, 18, 0.02)) / TRAB * 100, 2)},
            ],
            "conclusao": "TESTE DOS 10% NÃO ATENDIDO entre 0,5% e 1,0% ao mês (4,60% e 8,90%). Não há redução de "
                         "principal na classe I. NÃO reconhecer ganho nessa classe; registrar em nota que a "
                         "conclusão é sensível à taxa: acima de ~1,13% a.m. a diferença ultrapassa 10% (a 1,5% a.m. "
                         "chega a 12,93%), e a biblioteca não define a taxa de referência do teste (NÃO VERIFICADO). "
                         "Como a classe I não sofreu redução de principal, mantemos o valor nominal.",
        },
        "credor_fiduciario_e_uniao": "sem teste: não houve novação (art. 49, §3º; CTN art. 187).",
    },
    "sensibilidade_por_taxa": [
        {"taxa_a_m": f"{i * 100:.2f}%",
         "valor_presente_novo_passivo": round(pv_anui(PMT, 120, i, 24), 2),
         "ganho_contabil": round(BASE - pv_anui(PMT, 120, i, 24), 2),
         "teste_10_por_centos": round((BASE - pv_anui(PMT, 120, i, 24)) / BASE * 100, 1),
         "ganho_nominal_do_desagio": BASE - NOVO_NOM,
         "irpj_csll_corrente_sobre_ganho_nominal": round(BASE_FISCAL * ALIQ, 2),
         "passivo_fiscal_diferido": round(max(0.0, (BASE - pv_anui(PMT, 120, i, 24) - BASE_FISCAL) * ALIQ), 2)}
        for i in (0.0, 0.005, 0.01, 0.015, 0.02)
    ],
    "saldos_apos_homologacao": {
        "passivo_recuperacional_novado_a_valor_presente": round(PV, 2),
        "contrapartida_nominal_do_passivo_novado": NOVO_NOM,
        "passivo_trabalhista_classe_I": TRAB,
        "passivo_extraconcursal_fiduciario_Banco_Beta_vencido": BETA,
        "obrigacoes_pos_pedido_extraconcursais_Norte": NORTE_POS,
        "parcelamento_federal_Lei_10522": UNIAO,
        "provisao_IRPJ_CSLL_corrente": IRPJ_CORRENTE,
        "tributos_diferidos_passivos": DTL,
        "total_passivo_oneroso_pos_homologacao": round(PV + TRAB + BETA + NORTE_POS + UNIAO + IRPJ_CORRENTE + DTL, 2),
        "nota": "o total acima NÃO inclui garantias de aval dos controladores (passivo de terceiros), despesas da "
                "recuperação não informadas e juros do parcelamento federal (NÃO VERIFICADOS).",
    },
    "resultado_efeito_liquido": {
        "receita_de_renegociacao_de_dividas_em_RJ": round(GANHO, 2),
        "receita_com_transacao_tributaria_memo": 1_890_000.0,
        "despesa_de_IRPJ_CSLL_corrente": IRPJ_CORRENTE,
        "despesa_de_IRPJ_CSLL_diferida": DTL,
        "PIS_COFINS_sobre_o_ganho": 0.0,
        "ganho_nao_reconhecido_por_decisao": 2_590_000.0,
        "nota": "2.590.000,00 = 1.240.000,00 (deságio fiduciário) + 1.350.000,00 (deságio da União) prometidos pela "
                "minuta e juridicamente inexistentes.",
    },
    "reconciliacoes_abertas": [
        {"item": "gap de funding do plano",
         "valor": 630_400.0,
         "detalhe": "déficit de 5.130.400,00 em 120 meses (trabalhistas + parcelas do plano + federal 22.500,00/mês, "
                     "menos geração de 5.000,00/mês) contra 4.500.000,00 esperados da venda do galpão. Não lançável; "
                     "é evidência de continuidade."},
        {"item": "déficit em 120 meses servindo o CCB do Beta (3.100.000,00, em qualquer prazo)",
         "valor": 8_230_400.0,
         "detalhe": "gap contra o galpão de 3.730.400,00. Caixa de 840.000,00 esgota entre o mês 3 e o mês 12 "
                     "(deliverable/sessao2/analise_plano.md §6.3). Não lançável; requer divulgação de incerteza "
                     "significativa sobre continuidade — o requisito de divulgação não está na biblioteca (NÃO "
                     "VERIFICADO)."},
        {"item": "sinal prometido à Norte Suprimentos",
         "valor": 925_000.0,
         "detalhe": "supera o caixa de 840.000,00 de 31/03/2026 (110,1%) e se refere a débito pré-pedido — "
                     "pagamento fora do plano é ilegal (art. 49). Nenhum lançamento de provisão: é obrigação "
                     "concursal já incluída em L1."},
        {"item": "fornecedores extraconcursais de 1.480.000,00 no extrato de 31/03/2026",
         "valor": 1_170_000.0,
         "detalhe": "diferença entre 1.480.000,00 do extrato e os 310.000,00 de notas pós-pedido identificadas da "
                     "Norte. Composição não informada (pergunta nº 19): se for pré-pedido, pertence à classe III e "
                     "entra em L1; se for pós-pedido, fica fora. Não forçamos a conciliação."},
        {"item": "efeito da premissa P1 sobre L1",
         "valor": 210_000.0,
         "detalhe": "se o pedido for posterior a 12/03/2026, a nota de 210.000,00 volta à classe III: base de L1 "
                     "sobe para 6.260.000,00 e a parcela do plano muda."},
        {"item": "semanas 5 a 13 do fluxo de caixa",
         "valor": None,
         "detalhe": "arquivo com apenas 4 de 13 semanas. A projeção de caixa usada em L9 e nas divulgações não pode "
                     "ser fechada (pergunta nº 11)."},
    ],
    "perguntas_dependentes": [8, 9, 11, 14, 15, 16, 17, 18, 19, 21, 22, 23],
}

path = "deliverable/sessao3/lancamentos_novacao.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
    f.write("\n")

with open(path, encoding="utf-8") as f:
    back = json.load(f)
print("json ok;", len(back["lancamentos"]), "lancamentos;",
      len(back["nao_lancar"]), "nao_lancar;",
      len(back["reconciliacoes_abertas"]), "abertas")
for e in back["lancamentos"]:
    print(f"  {e['id']}: D {e['total_debitos']} == C {e['total_creditos']}  [{e['status_contabil']}]")
print("PV novo passivo:", round(PV, 2), "| ganho contábil:", round(GANHO, 2),
      "| IRPJ/CSLL corrente:", IRPJ_CORRENTE, "| DTL:", DTL)
print("total passivo pós:", back["saldos_apos_homologacao"]["total_passivo_oneroso_pos_homologacao"])
