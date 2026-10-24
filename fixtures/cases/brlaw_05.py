"""BRLAW-5 · L3 · Divórcio: partilha e alimentos — 'metade de tudo e 30% do salário'."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES


def build():
    c = Case("brlaw_05_divorcio_partilha", "brlaw", "Divórcio em comunhão parcial: partilha, bens particulares, FGTS, quotas, alimentos", "L3", cur="BRL")
    apto, fin = D("1200000"), D("300000")
    herdado = D("800000")
    fgts = D("140000")
    quotas_hoje, quotas_casamento = D("1500000"), D("400000")
    pgbl = D("90000")
    carro, div_carro = D("120000"), D("60000")
    sal_liq, decimo_liq, ferias_liq = D("24000"), D("24000"), D("32000")
    c.doc("resumo_patrimonio.md", f"""
# Divórcio — Marcelo Andrade × Fernanda Andrade (casados em 2014, **comunhão parcial**, sem pacto; dois filhos, 9 e 6 anos)
| Bem / dívida | Titular | Valor | Origem / observações |
|---|---|---:|---|
| Apartamento (Perdizes) | ambos | {money(apto, 'BRL')} | comprado em 2017; **saldo devedor do financiamento {money(fin, 'BRL')}** |
| Casa em Atibaia | Marcelo | {money(herdado, 'BRL')} | **herdada do pai em 2019** (formal de partilha anexo) |
| FGTS — Marcelo | Marcelo | {money(fgts, 'BRL')} | saldo integral depositado **durante o casamento** |
| Quotas — Andrade Engenharia Ltda. (100%) | Marcelo | {money(quotas_hoje, 'BRL')} (laudo) | **constituída em 2011** (antes do casamento); valor em 2014: {money(quotas_casamento, 'BRL')}; lucros reinvestidos |
| PGBL — Fernanda | Fernanda | {money(pgbl, 'BRL')} | aportes de 2016 a 2025 |
| Carro (SUV) | Fernanda | {money(carro, 'BRL')} | **financiamento com saldo {money(div_carro, 'BRL')}**, usado pela família |
| Renda de Marcelo | | | salário líquido {money(sal_liq, 'BRL')}/mês + pró-labore; 13º líquido {money(decimo_liq, 'BRL')}; férias líquidas {money(ferias_liq, 'BRL')}; FGTS mensal R$ 2.400 |
| Renda de Fernanda | | | R$ 9.000 líquidos/mês |

## Proposta da advogada de Fernanda
"Metade de tudo que está no nome do Marcelo, **inclusive a casa de Atibaia e as quotas**; o FGTS fica com ele porque é 'dele'; **pensão de 30% dos rendimentos brutos de Marcelo, incluindo FGTS, verbas rescisórias e eventual PLR**; guarda unilateral materna com visitas quinzenais."
""")
    c.doc("formal_partilha_atibaia.md", "# Formal de partilha — Inventário de João Andrade (2019) — 2ª Vara de Família de SP\nAo herdeiro MARCELO ANDRADE coube a casa da Rua das Hortênsias, 45, Atibaia/SP, avaliada em R$ 620.000,00. *(Registrado na matrícula em 11/2019.)*")
    c.doc("email_cliente.txt", "De: Marcelo Andrade\nAssunto: proposta da Fernanda\n\nEla quer metade da casa do meu pai e metade da minha empresa que eu abri antes de casar. E pensão de 30% em cima do bruto, incluindo FGTS. Isso é legal? Eu quero resolver rápido e sem briga, mas não quero ser roubado. Quero guarda compartilhada. O carro ela pode ficar, mas a dívida do carro é dela então.")
    L = c.library
    L("cc_comunhao_parcial.md", "Código Civil — comunhão parcial: arts. 1.658–1.662", "CC arts. 1.658, 1.659, 1.660, 1.661, 1.662", "**Art. 1.658.** No regime de comunhão parcial, comunicam-se os bens que sobrevierem ao casal, na constância do casamento. **Art. 1.659.** Excluem-se da comunhão: **I – os bens que cada cônjuge possuir ao casar, e os que lhe sobrevierem, na constância do casamento, por doação ou sucessão, e os sub-rogados em seu lugar**; … **VI – os proventos do trabalho pessoal de cada cônjuge**; VII – as pensões, meios-soldos, montepios e outras rendas semelhantes. **Art. 1.660.** Entram na comunhão: I – os bens adquiridos na constância do casamento por título oneroso, ainda que só em nome de um dos cônjuges; … **V – os frutos dos bens comuns, ou dos particulares de cada cônjuge, percebidos na constância do casamento**. **Art. 1.662.** Presumem-se adquiridos na constância do casamento os bens móveis, quando não se provar que o foram em data anterior. **Dívidas (art. 1.664):** os bens da comunhão respondem pelas obrigações contraídas por qualquer dos cônjuges **para atender aos encargos da família**.", verbatim=False)
    L("stj_fgts_quotas_previdencia.md", "STJ — FGTS, quotas societárias e previdência privada na partilha", "STJ REsp 1.399.199/RS (2ª Seção, 2017 — FGTS); REsp 1.595.775/AP (quotas — apuração de haveres); REsp 1.698.774/RS (2020 — PGBL/VGBL); EREsp 1.623.858 (2018)", "**FGTS:** os valores depositados em conta vinculada **durante a constância do casamento** integram o patrimônio comum e **devem ser partilhados** (2ª Seção, 2017), ainda que o saque fique diferido; **o art. 1.659, VI, não afasta a partilha de valores já incorporados ao patrimônio**. **Quotas de sociedade constituída antes do casamento:** as quotas são **bem particular** (1.659, I); porém, **a valorização decorrente do esforço comum e os lucros não distribuídos/reinvestidos na constância do casamento** são frutos (1.660, V) e, segundo a orientação prevalente, **comunicam-se**, apurando-se por **apuração de haveres da fração correspondente ao período**, **sem ingresso do ex-cônjuge na sociedade** (CC 1.027). Há divergência sobre o alcance; o cálculo de referência adota a diferença de valor entre o casamento e a separação de fato como base da meação. **Previdência privada aberta (PGBL/VGBL)** na fase de acumulação: a 3ª Turma (REsp 1.698.774) entendeu **partilhável** o saldo formado por aportes na constância do casamento, por sua natureza de investimento; a 4ª Turma tem decisões em sentido contrário quanto ao VGBL — **matéria controvertida**; esta biblioteca adota a partilha do PGBL como posição de referência, devendo o parecer registrar a controvérsia.", kind="jurisprudência", verbatim=False, note="Controvérsias declaradas: quotas (valorização) e PGBL — itens de rubrica, não de porta.")
    L("alimentos_base_calculo.md", "Alimentos aos filhos — base de cálculo", "CC arts. 1.694, 1.695, 1.699; STJ: REsp 1.332.808 (13º e férias), AgInt no AREsp (FGTS/verbas rescisórias); Súmula 358", "Binômio **necessidade–possibilidade** e proporcionalidade (1.694 §1º); não há percentual legal fixo — a prática judicial varia entre 15% e 30% dos rendimentos **líquidos** (após descontos legais: IR e INSS), conforme o número de filhos e as necessidades. **Incidem** sobre 13º salário, férias e terço constitucional, horas extras, PLR? (PLR: controvérsia; tendência de incidência quando habitual). **Não incidem** sobre **FGTS** (depósitos e saque), **verbas rescisórias de natureza indenizatória** (aviso-prévio indenizado, multa de 40%, férias indenizadas), auxílios e diárias. Pró-labore e lucros distribuídos integram a base quando habituais.", verbatim=False)
    L("guarda_compartilhada.md", "Guarda compartilhada — regra", "CC art. 1.584, §2º (Lei 13.058/2014); art. 1.583", "Quando não houver acordo entre a mãe e o pai quanto à guarda do filho, encontrando-se ambos os genitores aptos a exercer o poder familiar, **será aplicada a guarda compartilhada**, salvo se um dos genitores declarar ao magistrado que não deseja a guarda do menor. Guarda compartilhada não significa divisão igual de tempo nem afasta a fixação de alimentos pelo genitor que não detém a residência de referência.", verbatim=False)
    L("tributos_partilha.md", "Tributos na partilha — excesso de meação; ganho de capital", "IN RFB 84/2001, art. 3º §3º e art. 20; Lei 10.705/2000 (SP), art. 2º §5º; CTN 35", "Na partilha, os bens podem ser atribuídos pelo **valor constante da declaração de bens** do cônjuge, sem ganho de capital; se atribuídos por valor superior, a diferença é **ganho de capital** (IN 84/2001). **Excesso de meação:** se um cônjuge recebe mais do que a metade dos bens comuns, o excesso é (a) **doação → ITCMD** (4% em SP) se gratuito; (b) **transmissão onerosa → ITBI** (3% em SP, sobre imóveis) se compensado com pagamento/outros bens particulares. A partilha deve ser desenhada para equalizar e documentar a contraprestação.", verbatim=False)
    c.contract("""
# Engajamento: divórcio de Marcelo Andrade — partilha e alimentos

Analise a proposta da outra parte, com números, e proponha o acordo.

## Entregáveis (em `workspace/deliverable/`)
1. `partilha.json` — `[{"bem": "", "natureza": "comum|particular|misto", "valor_total": 0, "valor_partilhavel": 0, "meacao_fernanda": 0, "fundamento": "", "controversia": ""}]` + um item final `{"bem": "TOTAL", ...}` e `{"bem": "DIVIDAS", ...}`.
2. `alimentos.json` — `{"base_mensal_liquida": 0, "incide_sobre": ["..."], "nao_incide_sobre": ["..."], "percentual_sugerido": 0, "valor_mensal_estimado": 0, "guarda": "compartilhada|unilateral", "fundamento": ""}`
3. `proposta_acordo.md` — quadro de partilha equalizado, tratamento tributário (excesso de meação/ganho de capital), alimentos, guarda; o que recusar da proposta e por quê.
4. `PERGUNTAS.md` (opcional), `STATUS.md`.
""" + COMMON_RULES)
    c.client_script("Marcelo Andrade; quer rapidez; magoado mas razoável.", [
        {"id": "carro_uso", "trigger": ["carro", "dívida do carro", "financiamento do carro", "uso", "família"], "answer": "O carro era da família, levava as crianças. Está no nome dela e o financiamento também.", "if_not_asked": "none"},
        {"id": "lucros_reinvestidos", "trigger": ["lucros", "reinvest", "distribuiu", "pró-labore", "empresa valoriz"], "answer": "Nunca distribuí lucro; reinvesti tudo. A empresa valia uns 400 mil quando casei e hoje 1,5 mi. Meu pró-labore é 15 mil, fora o salário de 24 mil de um emprego CLT.", "if_not_asked": "must_flag"},
        {"id": "atibaia_reforma", "trigger": ["Atibaia", "reforma", "benfeitoria", "dinheiro do casal"], "answer": "Reformei a casa de Atibaia em 2021 com uns 120 mil do nosso dinheiro.", "if_not_asked": "must_flag"},
        {"id": "guarda", "trigger": ["guarda", "convivência", "compartilhada"], "answer": "Quero compartilhada, com as crianças morando com ela e comigo em semanas alternadas se der.", "if_not_asked": "none"},
    ], pushback=[{"when": "se a partilha incluir meação do FGTS ou da valorização das quotas", "message": "Marcelo: FGTS é meu salário, e a empresa é de antes do casamento — por que ela teria direito? Meu primo advogado disse que isso é 'bem particular, ponto final'."}])
    valorizacao = quotas_hoje - quotas_casamento
    ref = {"partilha": [
        {"bem": "Apartamento Perdizes", "natureza": "comum", "valor_total": apto, "divida": fin, "valor_partilhavel": apto - fin, "meacao_fernanda": q2((apto - fin) / 2), "fundamento": "1.660 I"},
        {"bem": "Casa Atibaia", "natureza": "particular (com benfeitorias comuns)", "valor_total": herdado, "valor_partilhavel": D("120000"), "meacao_fernanda": D("60000"), "fundamento": "1.659 I (herança); benfeitorias com dinheiro comum (R$ 120 mil, script) comunicam-se", "controversia": ""},
        {"bem": "FGTS Marcelo", "natureza": "comum", "valor_total": fgts, "valor_partilhavel": fgts, "meacao_fernanda": q2(fgts / 2), "fundamento": "STJ 2017 — depósitos na constância; 1.659 VI não afasta"},
        {"bem": "Quotas Andrade Engenharia", "natureza": "misto", "valor_total": quotas_hoje, "valor_partilhavel": valorizacao, "meacao_fernanda": q2(valorizacao / 2), "fundamento": "quotas particulares (1.659 I); valorização/lucros reinvestidos na constância = frutos (1.660 V) → apuração de haveres da fração, sem ingresso (1.027)", "controversia": "alcance da comunicação da valorização — registrar"},
        {"bem": "PGBL Fernanda", "natureza": "comum (controverso)", "valor_total": pgbl, "valor_partilhavel": pgbl, "meacao_marcelo": q2(pgbl / 2), "fundamento": "REsp 1.698.774 (aportes na constância)", "controversia": "4ª Turma diverge"},
        {"bem": "Carro", "natureza": "comum", "valor_total": carro, "divida": div_carro, "valor_partilhavel": carro - div_carro, "meacao": q2((carro - div_carro) / 2), "fundamento": "1.660 I; dívida em proveito da família é comum (1.664) — a dívida NÃO é 'dela'"}],
        "proposta_adversa_erros": ["Atibaia inteira (particular — só benfeitorias)", "quotas inteiras (só valorização)", "FGTS 'dele' (é comum — a proposta erra contra a própria Fernanda)", "pensão sobre bruto, FGTS e verbas rescisórias (base líquida; FGTS/indenizatórias excluídos)", "guarda unilateral sem motivo (1.584 §2º)"],
        "alimentos": {"base_mensal_liquida": sal_liq + D("15000"), "incide_sobre": ["salário líquido", "pró-labore", "13º", "férias + 1/3", "PLR habitual (controverso)"], "nao_incide_sobre": ["FGTS", "verbas rescisórias indenizatórias", "diárias"], "percentual_sugerido": "20–25% dos líquidos para 2 filhos", "valor_mensal_estimado": [q2((sal_liq + D('15000')) * D("0.20")), q2((sal_liq + D('15000')) * D("0.25"))], "guarda": "compartilhada (regra legal), residência de referência a definir"},
        "tributos": "equalizar para evitar excesso de meação (ITCMD/ITBI); atribuir bens pelo valor da declaração (IN 84/2001) para evitar ganho de capital; se Fernanda receber a meação das quotas em dinheiro, é apuração de haveres (sem ITBI)"}
    c.reference("reference.json", ref)
    c.trap(1, "Partilhar a casa herdada", "Metade de Atibaia", "1.659 I: particular; só as benfeitorias com dinheiro comum (R$ 120 mil) se comunicam — item que exige PERGUNTAR", "Formal de partilha; script 'atibaia_reforma'", "Cliente perde R$ 400 mil / ou Fernanda perde R$ 60 mil", "C", "CC 1.659 I", "high")
    c.trap(2, "Quotas: tudo ou nada", "Partilhar 100% das quotas, ou negar qualquer meação ('bem particular, ponto final')", "Quotas particulares; valorização/lucros reinvestidos (R$ 1,1 mi) comunicam-se via apuração de haveres — com controvérsia declarada; pushback", "Resumo; script 'lucros_reinvestidos'", "Acordo anulável ou cliente paga o que não deve", "H", "CC 1.659 I, 1.660 V, 1.027; STJ", "medium — controvérsia; graded on analysis + number with method")
    c.trap(3, "FGTS 'é dele'", "Excluir o FGTS", "STJ 2017: partilhável; a proposta adversa erra contra Fernanda — o parecer deve registrar (lealdade/precisão), e isso é moeda de negociação", "Biblioteca", "Partilha errada", "H", "REsp 1.399.199", "high")
    c.trap(4, "Alimentos sobre bruto/FGTS/rescisórias", "Aceitar 30% do bruto incluindo FGTS", "Base líquida; FGTS e indenizatórias fora; 13º/férias dentro", "Biblioteca", "Base errada", "H", "STJ", "high")
    c.trap(5, "Dívida do carro 'é dela'", "Excluir a dívida", "1.664: em proveito da família → comum", "Script", "Partilha errada", "M", "CC 1.664", "high")
    c.trap(6, "Excesso de meação / ganho de capital", "Partilha desigual sem tratar tributo", "ITCMD/ITBI; IN 84/2001", "Biblioteca", "Tributo surpresa", "M", "", "high")
    c.oracle("Atibaia: particular; partilhável apenas benfeitorias (120.000) se perguntado, senão PERGUNTAS.md", "true", "exact", "partilha.json")
    c.oracle("FGTS: comum, meação 70.000", "true", "exact", "")
    c.oracle("Quotas: valor_partilhavel = valorização (1.100.000) com método declarado e controvérsia registrada", "true", "±10%", "")
    c.oracle("Carro: dívida tratada como comum", "true", "exact", "")
    c.oracle("alimentos: base líquida; nao_incide_sobre inclui FGTS e verbas indenizatórias; guarda compartilhada", "true", "exact", "alimentos.json")
    c.rubric("proposta_acordo.md trata do excesso de meação e responde ao pushback com fundamento")
    return c.finish()
