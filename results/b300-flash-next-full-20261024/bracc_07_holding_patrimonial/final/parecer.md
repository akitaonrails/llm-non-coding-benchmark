# Parecer — as cinco afirmações da palestra vs. o caso Dona Helena Furtado

**Base de análise:** `documents/palestra_resumo.md`, `documents/familia.md`, `documents/relacao_imoveis.csv`.
**Autoridade:** somente os 5 arquivos listados em `library/INDEX.md` (todos com status *in force* nesta biblioteca). O que não estiver neles está explicitamente marcado como **não verificado** ou remetido a pergunta em `QUESTIONS.md`. Não houve consulta à internet nem a outras fontes.

## 0. Os números do caso (do CSV, conferidos com `familia.md`)

| Grandeza | Valor | Origem |
|---|---|---|
| Imóveis | 11 (9 `locado`, 2 `uso proprio/ferias`) | CSV |
| Valor de mercado — total | R$ 16.430.000 | CSV (soma) = familia.md ✔ |
| Valor em declaração IR — total | R$ 4.720.000 | CSV (soma) = familia.md ✔ |
| Aluguéis dos 9 locados | R$ 84.900/mês = **R$ 1.018.800/ano** | CSV (soma) = familia.md ✔ |
| 9 locados: mercado / declaração | R$ 14.430.000 / R$ 4.220.000 | CSV (soma) |
| 2 próprios (Casa CDJ, Terreno Cotia) | R$ 2.000.000 / R$ 500.000 | CSV (soma) |
| Aplicações financeiras | R$ 2.100.000 | familia.md |
| Rendimento dos locados sobre o mercado | 1.018.800 ÷ 14.430.000 = **7,06%/ano** | cálculo |

A coluna `aluguel_mensal` dos 2 imóveis de uso próprio é zero, portanto a renda de R$ 84.900/mês que Helena declara no carnê-leão corresponde exatamente aos 9 imóveis locados — CSV e `familia.md` **conferem**, sem divergência.

**Premissas assentadas (não constam dos documentos):** (i) o patrimônio acima é integralmente de Helena — não há notícia de inventário do falecido (viúva desde 2019, comunhão parcial); se houver meação do espólio, **todos os números sucessórios da seção 4 caem pela metade**; (ii) os imóveis estão em municípios cujas alíquotas de ITBI não estão na biblioteca (só SP capital = 3% é citável) — tratamos 3% como premissa, com sensibilidade para o Galpão em Guarulhos; (iii) a tabela progressiva do IRPF 2026 não está na biblioteca e os valores mensais de IPTU/condomínio pagos pelo locador não foram informados — a **comissão de administração, sim (8%, resposta da cliente)**; o custo em PF é apresentado como teto (já com a dedução conhecida), não como valor certo.

**Respostas mais recentes da cliente (24/10/2026) — fatos novos aplicados ao longo do parecer:** (a) comissão da administradora = **8% da receita de aluguéis** (8% × 84.900 = R$ 6.792/mês = R$ 81.504/ano) — aplicada em §2; (b) Helena **mora em apartamento alugado em Higienópolis** (ela é locatária; valor do aluguel não informado) e o apto dos Jardins está alugado (como no CSV) — o fluxo de caixa pessoal dela em §6 sai dessa premissa; (c) a **Casa CDJ é "da família, ninguém aluga"** e o **Terreno Cotia é "para os netos um dia"** — confirmam a decisão de mantermos os dois fora da PJ (§6 item 1) e indicam que **existem netos**; (d) ela "paga IPTU e condomínio dos vagos" — **não há imóvel vago no CSV** (9 locados + 2 de uso próprio), logo é preciso esclarecer a que imóveis se refere (`QUESTIONS.md` Q20); (e) o rompimento com Marcos vem de **~6 anos** (conforme `familia.md`) — consequências em §4/§5.

## 1. “Integralizar todos os imóveis numa holding **sem ITBI** (imunidade constitucional)” — **FALSA**

A regra e a exceção estão em `library/cf156_ctn37_tema796.md`: há imunidade na integralização de capital, **“salvo se a atividade preponderante do adquirente for compra e venda, locação de bens imóveis ou arrendamento mercantil (mais de 50% da receita operacional nos 2 anos anteriores e 2 posteriores; empresa nova: 3 anos seguintes — CTN 37 §§1º-2º)”**.

- Numa holding constituída **para deter imóveis alugados**, a locação será ~100% da receita operacional nos exercícios seguintes — e a library expressamente estende o teste às **empresas novas pelos 3 anos seguintes**. A exceção incide, portanto: **não há imunidade; o ITBI é devido**. (A ressalva da palestra — “imunidade constitucional” — existe na CF, mas não para este caso.)
- Base de cálculo: pelo **Tema 796** (RE 796.376), “a imunidade não alcança o valor dos imóveis que exceder o capital social integralizado” — ou seja, mesmo onde a imunidade valesse, subscrever quotas por valor inferior ao mercado não zera o imposto.
- Alíquotas citáveis: São Paulo capital **3%** (única listada na library). **Não verificado** para Guarulhos, Campos do Jordão e Cotia — as alíquotas desses municípios não estão na biblioteca (pergunta em `QUESTIONS.md`).

**Contas (premissa: 3% sobre o valor de mercado dos 9 locados, integralização a mercado):**

| Cenário | Cálculo | ITBI |
|---|---|---|
| Integralizar a mercado, sem imunidade (exceção da preponderância) | 3% × 14.430.000 | **R$ 432.900** |
| Integralizar pelo valor declarado (capital = 4.220.000) — pelo Tema 796 o valor da operação é o teto da base | 3% × 4.220.000 | **R$ 126.600** — mas a prefeitura tende a lançar 3% × mercado (432.900); **306.300** ficariam em discussão (Tema 1.348 pendente) |
| Sensibilidade: Galpão (Guarulhos) a 11% (alíquota **não verificada**) | 432.900 − 3%×3.100.000 + 11%×3.100.000 | até R$ 680.900 |

A promessa “sem ITBI” não se sustenta. Nota da biblioteca: há repercussão geral pendente sobre o alcance dessa exceção na integralização (RE 1.495.108, Tema 1.348); até lá a própria library aplica a literalidade do CTN. Planejar **pagamento**, não litígio.

**GCAP — o ponto importante que a palestra não menciona:** `library/lei9249_art23.md` permite integralizar **“pelo valor da declaração ou pelo de mercado; pelo valor da declaração não há ganho de capital; pelo de mercado, a diferença é tributável (GCAP, 15%-22,5%)”**. Integralizar a mercado geraria ganho de 14.430.000 − 4.220.000 = 10.210.000 → até 22,5% = **R$ 2.297.250** de GCAP. Logo: **integralizar pelo valor de declaração (R$ 4.220.000)** zera o GCAP; o ITBI continua devido de qualquer forma (Tema 796 e exceção da preponderância). É por isso que `numeros.json` traz `integralizacao.valor_recomendado = 4.220.000` e `gcap_evitado = 2.297.250`.

## 2. “Aluguel na PJ paga ‘só 11,33%’ em vez de 27,5% na PF” — **VERDADEIRO COMO MODELO, FALSA NESTE CASO (a carga real é 12,2%–14,3%)**

`library/locacao_pf_vs_pj.md` confirma o modelo: PJ no Presumido com presunção de 32% → IRPJ 15% + **adicional 10% acima de R$ 20 mil/mês**; CSLL 9% sobre 32%; PIS/COFINS 3,65%; sem ISS; **carga ≈ 11,33% “até o limite do adicional”, ≈ 14,53% acima**. E a partir de 2026 (Lei 15.270): distribuição de lucros acima de **R$ 50 mil/mês por PJ a uma PF → IRRF 10%**.

**Este caso estoura os dois limites:**

- Base presumida mensal = 32% × 84.900 = **R$ 27.168 > R$ 20.000** → há adicional.
  IRPJ 15% × 326.016 = 48.902,40 + CSLL 9% × 326.016 = 29.341,44 + PIS/COFINS 3,65% × 1.018.800 = 37.186,20 → **115.430,04 (11,33%)** ✔ modelo da palestra.
  Adicional IRPJ: 10% × (27.168 − 20.000) × 12 = **8.601,60** → **124.031,64 = 12,17% da receita**.
  *Divergência interna da library, registrada:* o resumo “≈14,53% acima” equivale a 32%×(15%+10%+9%)+3,65% = aplicar o adicional sobre **toda** a base, não sobre o excedente; a fórmula “adicional 10% (acima de R$ 20 mil/mês)” leva ao número menor (12,17%). Não consegui reconciliar — deixo aberto (STATUS). Banda federal: **12,17%–14,53%** (148.031,64 no extremo).
- **Comissão de administração 8%** (resposta da cliente) = R$ 6.792/mês = **81.504/ano**. No Presumido ela **não reduz** o tributo federal — a library presume 32% **sobre a receita de aluguel**, sem falar em dedução de despesas — então é custo de caixa que reduz o distribuível. Lucro distribuível = 1.018.800 − 124.031,64 − 81.504 = **813.264,36 → 67.772,03/mês**. Se tudo for distribuído a **uma única PF**, excede R$ 50 mil/mês → IRRF 10% × (67.772,03 − 50.000) × 12 = **21.326,44** → total **145.358,08 = 14,27% da receita bruta**. Com **2 ou mais PFs** recebendo ≤ 50 mil/mês cada (33.886/mês com 2), o IRRF é **zero** e a carga fica em 124.031,64 (12,17%) — mas na estrutura final do §6 (doação de todas as quotas + usufruto) a renda converge para a usufrutuária, logo **o cenário de planejamento é o com IRRF** (§6 item 3).

**PF (lado comparativo):** o teto citável é a tabela progressiva “até 27,5%” (`locacao_pf_vs_pj.md`). A mesma library admite deduzir IPTU e condomínio pagos pelo locador e a **comissão de administração** — esta agora conhecida (8%, resposta da cliente): 27,5% × (1.018.800 − 81.504) = **R$ 257.756,40/ano**. Os valores mensais de IPTU/condomínio não foram informados → pode haver redução adicional; a tabela 2026 não está na library. Por isso `numeros.json` traz `pf.ir_anual = 257.756,40` como **teto já com a única dedução conhecida**, e a economia real (0 a ~134 mil/ano) depende da tabela e das demais deduções (Q8/Q21 em `QUESTIONS.md`).

**Payback do ITBI:** pagando 432.900 e economizando **133.724,76/ano** (teto PF 257.756,40 − PJ 124.031,64), o retorno é de **~3,2 anos**; no cenário de planejamento com IRRF (PJ 145.358,08; economia 112.398,32), de **~3,9 anos**. Proporcionalmente, por imóvel: **2,7–4,8 anos** (no cenário com IRRF, 3,2–5,7) — melhor no Galpão (8,5% de rentabilidade), pior no Apto Jardins (4,8%). Registre-se a assimetria da comissão: na PJ (Presumido) ela é despesa pura de caixa; na PF ela **reduz** imposto — o que enfraquece um pouco a vantagem da PJ. E se IPTU/condomínio deduzíveis reduzirem muito o imposto atual de PF, o payback pode nunca vir (Q8/Q9/Q21).

**Riscos/limites (a library os registra):** LC 214/2025 traz a locação da PJ para IBS/CBS com **redutor de 70%** (em 2026 só apuração-teste; alíquotas não estão na library → sensibilidade futura não quantificável); e a própria biblioteca chama os percentuais de “modelo” — não há validação com guia real de recolhimento.

## 3. “Doar as quotas com reserva de usufruto, pagando ITCMD de 4% sobre o valor **contábil** (baixo) — sucessão resolvida, sem inventário” — **PARCIALMENTE VERDADEIRO: a alíquota sim, a base não**

`library/itcmd_sp_lei10705.md`: incide ITCMD na doação de quotas, inclusive com reserva de usufruto; **alíquota em SP = 4%** (correto na palestra) — **mas a base é o valor patrimonial atualizado / valor de mercado dos bens da PJ, não o contábil histórico**, quando este for inferior (Decreto 46.655/2002 art. 14 §4º e jurisprudência do TJSP, citados pela library). A economia prometida sobre o valor contábil (4% × 4.220.000 = 168.800) **não existe**:

- Doar **todas** as quotas (base ≈ mercado 14.430.000): 4% = **577.200**; com usufruto reservado, a library descreve **2/3 na doação da nua-propriedade (384.800) e 1/3 na extinção do usufruto (192.400)** (regra que a própria library marca “verificar”), total igual no longo prazo.
- Cenário alternativo — doar quotas apenas até o valor do **disponível** (9.265.000 ≈ 64% das quotas): 4% = **370.600** (2/3 = 247.066,67 na doação). Custo colateral: deixaria ~R$ 5.165.000 de quotas no inventário, onde Marcos herdaria parte delas e entraria **na sociedade** — exatamente o que se quer evitar.
- EC 132/2023: progressividade do ITCMD tornou-se **obrigatória**, pendente lei estadual → risco de alíquota maior no futuro.

"Sucessão resolvida, sem inventário": **só em parte.** As quotas doadas saem do inventário, mas (i) os 2 imóveis de uso próprio e as aplicações (R$ 4,1 mi) continuarão sujeitos a inventário se mantidos em PF; (ii) a doação só funciona nos limites da legítima (§4); (iii) usufrutuária, Helena continua na posse e nos resultados até a extinção do usufruto — o que resolve a **liquidez do imposto**, não a eliminação do inventário.

## 4. “Tir Marcos da sucessão — com holding, cláusulas e doação antecipada ele não recebe nada” — **FALSA**

`library/cc_legitima_doacao.md`: filhos são **herdeiros necessários** (CC art. 1.845) e a legítima é **50% da herança** (art. 1.846), insuscetível de disposição. O arquivo é explícito: **o filho só é excluído por deserdação (justa causa legal, CC 1.961 ss.) ou indignidade (CC 1.814)** — vontade da mãe, rompimento familiar ou "já doei aos outros" não retiram legítima de ninguém. Doação em avanço de legítima imputa na parte do beneficiário (art. 544); doação que ultrapassa o disponível é **nula no excedente** (art. 549, redação literal da library).

**Números (premissa: patrimônio 100% de Helena, 3 filhos — Ricardo, Paula e Marcos, CC 1.829 cabeças):**

| Grandeza | Valor |
|---|---|
| Acervo hereditário (mercado 16.430.000 + aplicações 2.100.000) | R$ 18.530.000 |
| Legítima (50%, CC 1.846) | **R$ 9.265.000** |
| Parte disponível (a outra metade) | R$ 9.265.000 |
| Quinhão de cada filho na legítima (÷3) | **R$ 3.088.333,33** |
| Ativos fora da PJ (2 próprios 2.000.000 + aplicações 2.100.000) | R$ 4.100.000 ≥ 3.088.333,33 ✔ |

**Consequência prática — dá para dar TODAS as quotas a Ricardo e Paula sem tocar na legítima de Marcos.** A imputação, pela ordem dos arts. 544/549/2.002 da library (avanço de legítima imputa primeiro na quota do beneficiário, via colação; o excedente sai do disponível; é **nulo** o que invadir a legítima alheia):

| Passo da imputação | Valor |
|---|---|
| Doação de todas as quotas a Ricardo/Paula (mercado) | 14.430.000 |
| Imputa 1º às legítimas dos próprios donatários (2 × 3.088.333,33, art. 544/colação) | −6.176.666,67 |
| Sobra, que corre sobre a **parte disponível** (art. 549) | 8.253.333,33 |
| Parte disponível disponível (no momento da doação) | 9.265.000 ✔ (folga de **1.011.666,67**) |
| Legítima de Marcos, a cobrir com ativos fora da PJ | 3.088.333,33 ≤ 4.100.000 ✔ |

Nada invade a legítima de Marcos: ela é integralmente satisfeita pelos ativos que ficam fora da holding (casa + terreno + aplicações = 4,1 mi). A colação (arts. 2.002–2.012, citados pela library) conferirá essas contas ao final — se as quotas se valorizarem muito, o excedente de 8,25 mi pode crescer além da disponível, e a folga de 1,01 mi é o amortecedor (premissa: `STATUS.md`; verificação de valores atuais: `QUESTIONS.md`). O que **não** existe é mecanismo para Marcos *não receber nada* — o melhor realizável é ele receber **fora das quotas**. `numeros.json`: `legitima.marcos_pode_ser_excluido = false`.

**Resposta da cliente (24/10/2026):** “Ele não fala comigo há 6 anos. Não quero que ele receba nada. Se a lei obrigar, que seja o mínimo possível, com cláusulas de proteção.” A estrutura acima já realiza o **mínimo legal**: **0 quotas** para Marcos, e o quinhão dele (3.088.333,33 sob a premissa) satisfeito com **ativos fora da PJ**, não com a empresa. O que a lei não permite é zero. E registre-se: os 6 anos de afastamento **não estão listados na library** como justa causa de deserdação — ela menciona os CC 1.961 ss. sem transcrevê-los, logo **não é verificável aqui** se esse fato bastaria (advogado; Q18 em `QUESTIONS.md`).

## 5. “Cláusulas de inalienabilidade, impenhorabilidade e incomunicabilidade protegem as quotas dos credores e dos cônjuges” — **DEPENDE (justa causa) — e a parte “protege dos credores” não tem fonte na library**

`library/cc_legitima_doacao.md` (CC art. 1.848): o testador **não pode** estabelecer cláusulas de inalienabilidade, impenhorabilidade e incomunicabilidade sobre os bens da **legítima** sem **justa causa declarada no testamento** — sem justa causa expressa, não valem sobre a legítima. Sobre cláusulas que oneram só a **parte disponível** a library **não diz nada** (não verificado; pergunta em `QUESTIONS.md`). Pontos por cláusula:

- **Inalienabilidade / incomunicabilidade**: só com justa causa declarada quando o bem está na legítima; não são automáticas nem "de contrato social". Podem organizar a sucessão e o regime dos bens dos filhos, nesse limite. O fato apontado por Helena (rompimento de ~6 anos com Marcos) **não é transcrito na library** como hipótese de justa causa — qualificar esse fato é trabalho de advogado, não algo verificável nesta biblioteca.
- **Impenhorabilidade**: **nada na library sustenta** que ela afaste credores. O arquivo limita-se ao art. 1.848; não há nele nenhuma regra sobre eficácia da cláusula frente a credores — a "proteção contra credores trabalhista/fiscal" da palestra é **alegação sem fonte na biblioteca** (não verificado).
- **“Blindagem contra dívidas da holding”**: **a library não contém nada sobre responsabilidade do sócio, desconsideração da personalidade jurídica ou fraude contra credores** — portanto não há suporte para a promessa. O único risco de credores que a library toca é outro e funciona **contra** a doadora: doação que exceda o disponível é **nula** nesse excedente (art. 549). Se Helena se esvazia em favor dos filhos e depois tem dívidas, a biblioteca nada oferece que a proteja (e não verificamos as regras de fraude contra credores fora dela).

Veredito: cláusulas **podem** ser úteis (manter bens da legítima com justa causa; organizar partilha e regime dos filhos), mas **não** entregam a proteção anticredores vendida na palestra — isso simplesmente não tem fonte na biblioteca.

## 6. Estrutura que eu recomendaria (calibrada nos números acima)

1. **Constituir a PJ e integralizar SOMENTE os 9 locados, pelo valor de declaração IR (R$ 4.220.000)** — GCAP zero (Lei 9.249 art. 23); os 2 próprios (uso/ferias, sem renda) e as aplicações ficam na PF — **a cliente confirmou** a destinação da Casa CDJ (“da família”) e do Terreno Cotia (“para os netos”), o que reforça mantê-los fora da holding (24/10/2026).
2. **Provisionar ITBI de R$ 432.900** (3% × mercado, premissa) — não contar com imunidade; se o município aceitar a base do capital, cai para 126.600; confirmar alíquotas de Guarulhos/CDJ/Cotia antes de assinar. Verificar a **isenção/redução do Galpão** (a "redução" citada na palestra não está na biblioteca).
3. **Distribuir a 2 ou mais PFs**, se viável (Helena + filhos, cada uma ≤ R$ 50 mil/mês — com 2, 33.886/mês cada) → IRRF **zero**, carga **12,17%** (124.031,64/ano). Duas ressalvas honestas: (i) Helena é **viúva** — não existe opção “cônjuge”; (ii) na estrutura final dos itens 5–6 (todas as quotas doadas com usufruto reservado), a renda tende a convergir para ela como usufrutuária, e o IRRF de 10% sobre o excedente de R$ 50 mil/mês vira o cenário real (**21.326,44/ano**, carga total 145.358,08 = 14,27%) — a divisão só vale se os filhos já forem sócios plenos e receberem pelas próprias quotas, o que o contador deve validar (Q11).
4. **Não transferir a ponto de comprometer a renda própria e a legítima**: Helena **paga aluguel** (locatária em Higienópolis, valor não informado — Q19) e arca com os encargos dos bens sem renda. O plano distribui **67.772,03/mês brutos** (≈ **65.995 líquidos** após o IRRF do cenário de 1 PF), acima do caixa líquido atual estimado em PF (84.900 − comissão 6.792 − IRPF de até 21.480/mês ≈ **até 56.628**) — o fluxo melhora, mas o mínimo pessoal dela segue desconhecido (Q15/Q19). O teto legal é o art. 549 (nulidade do que excede o disponível): o desenho fecha com folga de **1.011.666,67** na parte disponível, folga que a valorização das quotas pode corroer até a colação final.
5. **Doar TODAS as quotas (nua-propriedade) a Ricardo e Paula, com usufruto reservado** — é o que mantém Marcos fora da sociedade; cláusulas restritivas, se desejadas, dependem de testamento com **justa causa** que o advogado julgue suficiente (a library não avalia se ~6 anos de rompimento bastam — §5, Q18). ITCMD com usufruto reservado: **384.800 agora** (2/3 × 14.430.000 × 4%) + **192.400** na extinção do usufruto (regra 2/3+1/3 marcada “verificar” na library; total de longo prazo 577.200). A imputação sucessória fecha sem tocar a legítima de Marcos (§4). A alternativa “doar só até o disponível” (370.600) só faria sentido se Helena quisesse deixar quotas a Marcos — o que ela não quer.
6. **Assegurar o quinhão de Marcos com ativos fora da PJ** (4,1 mi ≥ 3.088.333,33) — a vontade de "não deixar nada a ele" não é realizável; dá é **não dar a ele as quotas**.
7. **Fazer testamento** — hoje não há; é o que documenta a justa causa das cláusulas e organiza a partilha; a holding não o substitui.
8. **Reavaliar após a regulamentação do IBS/CBS** (redutor de 70% da locação PJ, LC 214/2025, alíquotas não publicadas na library) e da lei paulista de progressividade do ITCMD (EC 132/2023) — as duas contas mais baratas de hoje podem não ser as de amanhã.

## 7. Limites deste parecer (o que NÃO pude verificar)

- **`library/` se autodeclara "modelo"**, não validado com guia de recolhimento; e traz **divergência interna** na carga do Presumido: fórmula do adicional (adicional só sobre o excedente de 20k/mês) → 12,17% vs resumo "≈14,53% acima" (adicional sobre toda a base) → **deixei as duas bandas abertas**, sem reconciliar, como exige o contrato.
- **Alíquotas de ITBI de Guarulhos, Campos do Jordão e Cotia** não constam da biblioteca — 3% é premissa; o "11% de Guarulhos" da palestra **não** está na biblioteca (usado só como sensibilidade).
- **Tabela IRPF 2026** ausente → `pf.ir_anual` é teto (27,5% sobre a receita já com a única dedução conhecida — comissão 8% → **257.756,40**), não estimativa; **IPTU/condomínio mensais pagos pelo locador não informados** (Q21) — são dedutíveis pela library e reduziriam ainda mais o imposto de PF, encolhendo a vantagem da PJ.
- **ITCMD**: base "patrimonial atualizado" aceita pela library, mas o valor real depende do laudo/Balanço; a regra 2/3 + 1/3 do usufruto está marcada "verificar" na própria library; progressividade pendente.
- **Sem inventário do marido** na documentação: assumi 100% de Helena; se houver meação do espólio, legítima e disponível **caem à metade** e a cobertura do quinhão de Marcos pode apertar.
- **As respostas da cliente não trouxeram informação adicional** para várias perguntas (Q1, Q4–Q6, Q8–Q10, Q12–Q13, Q16–Q17 em `QUESTIONS.md`): partilha/meação, alíquotas municipais, declarações de IR, laudos, dívidas/fianças — permanecem como **premissas e riscos documentados**, dependentes de documentos e do trabalho de advogado/contador. Desconhecidos **novos** que surgiram das próprias respostas: o **aluguel mensal que ela paga** em Higienópolis (Q19); os **valores mensais de IPTU/condomínio** dos locados pagos pelo locador (Q21); os **“imóveis vagos”** cujos IPTU ela diz pagar — **não há imóvel vago no CSV** (Q20).
- **Nada fora da biblioteca foi usado** — inclusive deixei de checar na internet temas como Tema 1.348 (pendente, citado pelo próprio arquivo), LC 214/2025 (citada sem alíquotas) e Lei 15.270 (citada sem texto).
- Recomendação da palestra de "integralizar **todos** os 11 imóveis" foi rejeitada por falta de função (2 sem renda só adicionam ITBI/ITCMD e custo); a alternativa (só os 9) é recomendação técnica minha, não da biblioteca.

---

### Fontes citadas (todas em `library/INDEX.md`)
`cf156_ctn37_tema796.md` (ITBI, exceção da preponderância, Temas 796/1.348, SP 3%) · `lei9249_art23.md` (integralização por valor declarado, GCAP 15–22,5%) · `locacao_pf_vs_pj.md` (Presumido 32%, adicional 20k/mês, IRRF 2026, PF até 27,5%, IBS redutor 70%) · `itcmd_sp_lei10705.md` (4%, base de mercado, usufruto 2/3+1/3, EC 132) · `cc_legitima_doacao.md` (1.845/1.846, legítima 50%, deserdação/indignidade, doação inoficiosa nula no excedente [549], avanço de legítima/colação [544/2.002], 1.848 justa causa).
Documentos do caso: `palestra_resumo.md`, `familia.md`, `relacao_imoveis.csv`. Perguntas pendentes: `QUESTIONS.md` / `PERGUNTAS.md`; situação: `STATUS.md`.
