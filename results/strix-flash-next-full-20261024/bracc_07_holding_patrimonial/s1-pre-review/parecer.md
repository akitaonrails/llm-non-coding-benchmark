# Parecer — Planejamento patrimonial e sucessório
**Cliente:** Dona Helena Furtado, 71 anos, viúva (comunhão parcial, viúva desde 2019), 3 filhos (Ricardo, Paula, Marcos), sem testamento.
**Objeto:** avaliar as 5 afirmações da palestra "Holding familiar: pague 11% nos aluguéis e proteja seus herdeiros" (`documents/palestra_resumo.md`) e propor o que é possível.

**Base deste parecer:** somente a biblioteca fechada `library/` (índice em `library/INDEX.md`). O que eu saiba além dela está expressamente marcado como **[NÃO VERIFICADO NA BIBLIOTECA]**.

**Revisão (rodada 2):** esta versão incorpora as respostas da cliente (comissão de administração de 8%; IPTU/condomínio dos imóveis vagos pagos por ela, sem valores; e a diretriz sobre Marcos — "não quero que receba nada; se a lei obriga, o mínimo possível, com cláusulas de proteção"). Os números de PF/PJ e a análise da legítima foram recalculados; a pergunta 3 de `QUESTIONS.md` foi parcialmente respondida. As demais perguntas ficaram sem resposta e estão sinalizadas como **desconhecidos remanescentes** (não serão repetidas). **Rodada 3:** pergunta nova da cliente ("doar tudo a Ricardo e Paula zera Marcos?") respondida na seção final — sem perguntas de volta.

## Premissas (importantes — ver também `QUESTIONS.md`)
1. **P1.** Assumo que os 11 imóveis e as aplicações pertencem **100% a Helena**. Se os imóveis foram adquiridos na vigência do casamento em comunhão parcial e o **inventário do falecido esposo (2019) não foi feito**, metade deles já é, em parte, dos filhos — e Helena **não pode integralizar nem doar a totalidade** sem antes resolver esse inventário. Essa premissa pode derrubar o plano inteiro; foi perguntada à cliente.
2. **P2.** Assumo domicílio da futura PJ e residência em **São Paulo/SP** (ITCMD estadual a 4%; ITBI a 3% na capital). Guarulhos, Cotia e Campos do Jordão são **outros municípios**, cujas alíquotas de ITBI **não constam da biblioteca** — usei 3% como aproximação **[NÃO VERIFICADO NA BIBLIOTECA]**.
3. **P3.** Números de PF usam a tabela progressiva mensal; a biblioteca cita a existência da tabela (Lei 9.250/95) mas **não reproduz as faixas**. Usei a faixa top marginal 27,5% (esta, sim, na biblioteca) com parcela a deduzir mensal de R$ 908,73 — valor da tabela **[NÃO VERIFICADO NA BIBLIOTECA]**. O efeito dessa parcela é pequeno (~0,9% da renda); o erro da estimativa é marginal.
4. **P4.** Assumo 2026 (regras da biblioteca, ano "in force") e que a família **distribuiria todo o caixa disponível** mensalmente (relevante para o IRRF de 2026).
5. **P5 (resposta da cliente, rodada 2):** a administradora cobra **8% sobre os aluguéis** (R$ 6.792/mês = R$ 81.504/ano) — a biblioteca lista "comissão de administração" entre as deduções do aluguel na PF (`locacao_pf_vs_pj.md`), então esse valor **entra como dedução** nos cálculos de PF. O **IPTU e condomínio dos imóveis vagos são pagos por ela, mas sem valores informados** — ficam como desconhecido. Se e quanto desses IPTU/condomínio são dedutíveis (a biblioteca lista "IPTU, condomínio pagos pelo locador" sem delimitar a imóveis locados) **[NÃO VERIFICADO NA BIBLIOTECA]** — não computados; se forem dedutíveis, o imposto de PF cai um pouco mais (o cálculo de PF segue sendo um **teto**).

## Números de partida (aritmética em `documents/relacao_imoveis.csv`)
- Valor de mercado dos 11 imóveis: 1.800.000+1.200.000+1.500.000+1.500.000+2.200.000+3.100.000+1.400.000+950.000+880.000+600.000+1.300.000 = **R$ 16.430.000** ✓ (bate com `familia.md`).
- Valor nas declarações: 520+380+410+410+600+900+350+300+280+150+420 (mil) = **R$ 4.720.000** ✓.
- Aluguéis (9 imóveis locados): 7.200+5.200+9.800+9.800+14.000+22.000+4.300+4.100+8.500 = **R$ 84.900/mês** ✓ = **R$ 1.018.800/ano**.
- Mercado dos 9 locados: R$ 14.430.000. Imóveis próprios (fora da renda): Casa Campos do Jordão (R$ 1,4 mi) e Terreno Cotia (R$ 0,6 mi).
- patrimônio total ≈ 16.430.000 + 2.100.000 (aplicações) = **R$ 18.530.000**.

---

## Afirmação 1 — "Integralizar todos os imóveis na holding sem ITBI (imunidade constitucional)"
### Veredito: **FALSA para esta holding.**

Fundamento (`cf156_ctn37_tema796.md`):
- A imunidade do CF art. 156, §2º, I **não se aplica** "se a atividade preponderante do adquirente for compra e venda, **locação de bens imóveis** ou arrendamento mercantil" (CTN art. 37: >50% da receita operacional nos 2 anos anteriores e 2 posteriores; empresa nova: apura-se nos 3 anos seguintes).
- Uma holding que receba estes imóveis vive de **aluguel**: dos R$ 16,43 mi de patrimônio, 88% (mercado) e 100% da receita (R$ 1.018.800/ano) vêm de locação → atividade preponderante = locação → **exceção da CF → ITBI devido sobre a transmissão toda**. A biblioteca registra que há repercussão geral pendente sobre o alcance dessa exceção (RE 1.495.108, Tema 1.348), mas determina aplicar a literalidade — foi o que fiz.
- **Em nada adiantaria tentar escapar pela imunidade:** mesmo onde ela valesse, o **Tema 796** (STF RE 796.376) exclui da imunidade "o valor dos imóveis que exceder o capital social integralizado". Se integralizar pelo valor de declaração (R$ 4,72 mi) e o mercado é R$ 16,43 mi, o excedente R$ 11.710.000 seria tributado de qualquer forma (3% = R$ 351.300).

Quanto de ITBI (alíquota SP capital 3%, na biblioteca):
| Cenário | Base | ITBI |
|---|---|---|
| Integralizar os 11, Prefeitura arbitra valor de mercado | 16.430.000 | **R$ 492.900** |
| Integralizar só os 9 locados, base mercado | 14.430.000 | R$ 432.900 |
| Base aceita = valor integralizado (declaração) — 11 imóveis | 4.720.000 | R$ 141.600 |

A **base de cálculo do ITBI** (mercado vs. valor transmitido) **não está na biblioteca**; arbitrar por valor venal/de mercado é prática municipal comum **[NÃO VERIFICADO NA BIBLIOTECA]**. Por segurança orço o caso adverso: **R$ 492.900** (todo o plano custa ≈ R$ 0,5 mi de ITBI só para "criar" a holding). Alíquotas de Guarulhos/Cotia/Campos do Jordão: fora da biblioteca (P2).

## Afirmação 2 — "Aluguel na PJ paga só 11,33% em vez de 27,5% na PF"
### Veredito: **VERDADEIRA NO CONCEITO, FALSA NO NÚMERO, INCOMPLETA.**

Fundamento (`locacao_pf_vs_pj.md` — Presumido 2026): presunção 32%; IRPJ 15% + adicional de 10% sobre o que exceder R$ 20 mil/mês de base tributável; CSLL 9% sobre 32%; PIS/COFINS 3,65%; sem ISS. O "11,33%" da biblioteca vale **apenas até o limite do adicional**; acima, a carga de referência é ~14,53%.

Nela (receita R$ 84.900/mês → base presumida 32% = R$ 27.168/mês, já acima de R$ 20 mil):
- IRPJ: 15% × 27.168 = R$ 4.075,20 + adicional 10% × (27.168 − 20.000) = R$ 716,80 → **R$ 4.792,00/mês**
- CSLL: 9% × 27.168 = **R$ 2.445,12/mês**
- PIS/COFINS: 3,65% × 84.900 = **R$ 3.098,85/mês**
- **Total PJ: R$ 10.335,97/mês = R$ 124.031,64/ano → carga efetiva 12,17%** (não 11,33%; o adicional morde R$ 716,80/mês).

E falta o segundo andar — **Lei 15.270/2025, em vigor desde 2026**: distribuições de lucros acima de R$ 50 mil/mês da PJ para a PF sofrem **IRRF 10%**. Caixa distribuível (a comissão de 8% da administradora passa a ser despesa da PJ — sob Presumido **não reduz imposto**, pois a base é a receita presumida, mas reduz o caixa distribuível): 84.900 − 10.335,97 (impostos) − 6.792 (comissão) = **R$ 67.772,03/mês**:
- excedente: 67.772,03 − 50.000 = R$ 17.772,03 → IRRF 10% = R$ 1.777,20/mês = **R$ 21.326,44/ano**
  (interpreto a retenção sobre o **excedente** aos 50 mil — redação da biblioteca "acima de R$ 50 mil"; confirmar **[NÃO VERIFICADO NA BIBLIOTECA]**).
- **Custo total do ciclo PJ (empresa + sócia): 124.031,64 + 21.326,44 = R$ 145.358,08/ano = 14,27%** da receita — não 11,33%.

PF hoje (carnê-leão, tabela progressiva, top 27,5%; com a comissão de administração de 8% como dedução, por P5): 27,5% × (84.900 − 6.792 = 78.108) − 908,73 = R$ 20.570,97/mês → **≈ R$ 246.852/ano (24,23% dos R$ 1.018.800)**. [Faixas da tabela: P3, não verificadas. IPTU/condomínio dos vagos: valores desconhecidos, não computados.]

**Comparação honesta (ano):** PF ≈ 246.852 **vs** PJ ≈ 145.358 → **economia ≈ R$ 101.500/ano**. (Atenção: a comissão de 8% só ajuda na PF, porque no Presumido da PJ a despesa não abate imposto; isso **encurta** a vantagem antes estimada.) A troca continua vantajosa, mas:
- a economia (~R$ 101,5 mil/ano) paga o ITBI do cenário recomendado (~R$ 432,9 mil) em **≈ 4,3 anos** (no cenário adverso de ITBI 492,9 mil, **≈ 4,9 anos**) — e o ITCMD da doação vem depois;
- **LC 214/2025:** locação por PJ entra no IBS/CBS com redutor de 70%; 2026 é só apuração-teste, mas haverá **carga nova nos anos seguintes** que não atinge a PF — a biblioteca não quantifica **[NÃO VERIFICADO NA BIBLIOTECA]**;
- na PJ, venda futura de imóvel tende a ser receita da atividade (a biblioteca não trata o comparativo de venda PF × PJ **[NÃO VERIFICADO]**) — manter-se no **Presumido** exige não virar Imovenda (compra e venda) (consequência lógica da presunção de locação em `locacao_pf_vs_pj.md`).

## Afirmação 3 — "Doar as quotas com usufruto pagando ITCMD de 4% sobre o valor contábil (baixo) — sucessão resolvida, sem inventário"
### Veredito: **FALSA NA BASE, PARCIALMENTE VERDADEIRA NO EFEITO.**

- A alíquota de 4% em SP está na biblioteca (`itcmd_sp_lei10705.md`), mas a **base não é o contábil histórico**: a SEFAZ/SP exige o **valor patrimonial atualizado / valor de mercado dos bens da PJ** quando o contábil for inferior (Decreto 46.655/2002, art. 14, §4º e TJSP — conforme a biblioteca). Como a integralização será pelo valor de declaração (R$ 4,72 mi) e o mercado é R$ 16,43 mi, a base da doação será **~R$ 16,43 mi**, não o contábil:
  - ITCMD ≈ **4% × 16.430.000 = R$ 657.200** (se doar as quotas da PJ com todos os 11 imóveis; só locados: 4% × 14.430.000 = R$ 577.200).
  - No contábil seria só R$ 188.800 — a economia prometida pela palestra **não existe**.
  - A biblioteca registra regra de partição na doação com reserva de usufruto ("2/3 na doação da nua-propriedade e 1/3 na extinção do usufruto — verificar", ou integral de uma vez, conforme opção): o **total continua 4%**, apenas diluído no tempo; há também **ITCMD na extinção do usufruto** — a morte de Helena **não é fato gerador zero**.
  - **EC 132/2023:** progressividade do ITCMD passou a obrigatória, pendente de lei estadual em SP — a alíquota pode **subir** (projetos em tramitação, na biblioteca).
- "Sem inventário": **só em parte.** Se tudo entrasse na PJ e as quotas fossem doadas em vida, sim, não sobraria patrimônio societário a inventariar. Mas as **aplicações (R$ 2,1 mi)** — e os 2 imóveis próprios, se ficarem fora — continuam no CPF e **serão inventariados**. Usufruto + quotas doadas resolvem a **gestão e o fluxo** dos imóveis, não toda a sucessão.
- E a doação tem os limites da legítima (afirmação 4): doar as quotas **só a Ricardo e Paula** é inoficiosa quanto invade a legítima de Marcos, que pode exigir **redução** (`cc_legitima_doacao.md`), e doação de pai/mãe a filho é **adiantamento de legítima sujeita a colação** (CC arts. 544, 2.002).

## Afirmação 4 — "Quem você não quiser que herde, simplesmente não recebe quotas"
### Veredito: **FALSA.** Marcos não pode ser simplesmente cortado.

Fundamento (`cc_legitima_doacao.md`):
- CC arts. 1.845/1.846: filhos são **herdeiros necessários**; pertence-lhes "de pleno direito, a **metade** dos bens da herança" (legítima). Cuidado com a conta: essa **metade indisponível (50% ≈ R$ 9.265.000 de R$ 18,53 mi, se P1) é da CLASSE dos três filhos**; a legítima **individual de Marcos** é 1/3 dela = **1/6 do acervo ≈ R$ 3.088.333** (18.530.000 ÷ 6). O mesmo vale para Ricardo e Paula (≈ R$ 3.088.333 cada). (Correção em relação à primeira versão deste parecer, que atribuía a Marcos os 50% inteiros.)
- CC art. 549: doação é **nula** na parte que exceder o que se poderia dispor em testamento (parte disponível = a outra metade, ≈ R$ 9,265 mi). Excluir Marcos **abaixo do seu 1/6** não funciona: a doação aos outros dois será **reduzida** até recompor a legítima dele.
- CC art. 544 + arts. 2.002-2.012: doação de ascendente a descendente é **adiantamento de legítima**, sujeita a **colação** — na partilha, Ricardo e Paula terão que "trazer de volta" as doações para igualar Marcos contabilmente. **Consequência prática:** doar tudo a Ricardo+Paula não zera Marcos — no cômputo da colação (acervo ficto de R$ 18,53 mi), ele cobra o 1/6 dele ≈ **R$ 3,09 mi**, e ainda abre litígio.
- A própria biblioteca conclui: "doar as quotas só a dois filhos é inoficiosa quanto ao que invade a legítima do terceiro (que pode pedir redução)".
- **Caminhos que a lei admite (e que a palestra esconde):** só há duas formas de excluir um necessário — **deserdação por causa legal** (CC arts. 1.961-1.965, citados na biblioteca; exige **testamento** com a causa declarada — ela não tem testamento) ou **indignidade** (fato posterior ao falecimento, sentenciado). O rompimento de 6 anos, por si, não aparece como causa nas fontes disponíveis: as causas legais do art. 1.961 não estão reproduzidas na biblioteca **[NÃO VERIFICADO NA BIBLIOTECA]** — a cliente afirmou não ter outros fatos; na dúvida, o plano não pode contar com deserdação.
- **Resposta direta ao pedido da cliente ("o mínimo possível"):** o mínimo legal que Marcos pode receber é **exatamente a sua legítima individual: 1/6 do acervo ≈ R$ 3.088.333** (sob P1). Abaixo disso, a lei corrige. Acima disso é escolha dela. Recomendamos **pagar esse mínimo já, em vida** (doação de quotas no valor do 1/6, com usufruto reservado — ver Passo 2): trava o valor, evita redução/colação contenciosa e evita ITCMD futuro possivelmente progressivo (EC 132/2023).
- Atenção sucessória extra (premissa P1): se o inventário do esposo (†2019, comunhão parcial) não foi feito, os filhos **já são coproprietários** de parte dos imóveis — Marcos inclusive — e a integralização dependeria dele.

## Afirmação 5 — "Cláusulas de incomunicabilidade, impenhorabilidade e inalienabilidade protegem contra genros e credores"
### Veredito: **DEPENDE — muito mais fracas do que a palestra sugere.**

- CC art. 1.848 (`cc_legitima_doacao.md`): sobre os bens da **legítima** (metade do acervo), o doador/testador **NÃO pode** impor inalienabilidade/impenhorabilidade/incomunicabilidade, **"salvo se houver justa causa declarada"**. Cláusulas postas sobre o que toca à legítima, sem justa causa declarada, são ineficazes/elimináveis.
- **Aplicação ao pedido da cliente ("mínimo para Marcos, com as cláusulas"):** há um conflito estrutural entre os dois desejos. O mínimo de Marcos (1/6 ≈ R$ 3,09 mi — ver A4) é **legítima**; logo, as três cláusulas sobre essa fatia **só valem se houver justa causa declarada em testamento** (art. 1.848). Seis anos de silêncio, por si, **não aparecem na biblioteca como justa causa** — o padrão de justa causa não está reproduzido **[NÃO VERIFICADO NA BIBLIOTECA]**; imposto pelo juiz, a cláusula cai e a doação continua válida sem ela. Consequência prática: sobre o mínimo de Marcos, **cláusulas são risco de ineficácia**, não proteção. Onde as cláusulas são seguras é na **parte disponível** (≈ R$ 9,265 mi), que ela pode usar para Ricardo e Paula — ou para dar a Marcos um pouco acima do mínimo **e aí sim** amarrar o excedente com cláusulas (é a única forma de prendê-lo sem justa causa).
- Na **parte disponível** (a outra metade), as cláusulas são cabíveis — a biblioteca as trata apenas pela lente da legítima; os dispositivos gerais da doação (ex.: art. 1.911) **não estão na biblioteca** **[NÃO VERIFICADO NA BIBLIOTECA]**.
- "Contra genros": a incomunicabilidade pode, sim, impedir que quotas entrem na partilha de divórcio de um filho — efeito limitado às regras do casamento de cada filho (regime escolhido por eles; fora da biblioteca).
- "Contra credores": **não é escudo.** A impenhorabilidade contratual não alcança dívidas trabalhistas nem fraudes; constituir holding e doar quotas para fugir de credores existentes configura fraude (simulação/fraude contra credores e à execução) — **nenhum dispositivo sobre isso está na biblioteca**, registro como **não verificado**; o prudente é: se há dívidas/litígios em curso, o plano inteiro pode ser desfeito. Perguntei à cliente (QUESTIONS.md).
- Nota estrutural: as cláusulas pesam sobre **as quotas doadas**; se Marcos obtiver **redução** da doação (afirmação 4), os bens que a ele retornarem vêm **sem** essas amarras (fora da disponível).

---

## Estrutura recomendada (o que é possível, com números)

**Passo 1 — Constituir holding (Ltda, SP, regime Presumido), integralizando pelo VALOR DA DECLARAÇÃO.**
- Base: Lei 9.249/95, art. 23 (`lei9249_art23.md`): PF pode integralizar pelo valor de declaração **sem ganho de capital**; pelo valor de mercado, a diferença geraria GCAP de 15%–22,5%: 11 imóveis → 11,71 mi × 15–22,5% = **R$ 1.756.500 a R$ 2.634.750**; só os 9 locados (recomendado) → 10,21 mi × 15–22,5% = **R$ 1.531.500 a R$ 2.297.250** — a evitar.
- Recomendo integralizar **apenas os 9 imóveis locados (mercado R$ 14,43 mi / declaração R$ 4,22 mi)**: os 2 de uso próprio/ferias (Campos, Cotia) só geram ITBI de entrada e nenhuma receita. ITBI ≈ **R$ 432.900** (base mercado; R$ 141.600 se a base for o valor integralizado — ver A1). Custo de entrada é real: **orçar R$ 0,43–0,49 mi**.
- Economia tributária nos aluguéis: PF ≈ **R$ 246,9 mil/ano** (já com a comissão de 8% deduzida — P5) → PJ ≈ R$ 124 mil (PJ) + R$ 21,3 mil (IRRF 2026) = **≈ R$ 145,4 mil/ano**; **economia ≈ R$ 101,5 mil/ano**, pagando o ITBI (432,9 mil) em **~4,3 anos**. Manter **Presumido** (locação; não migrar para venda de imóveis — ver A2).

**Passo 2 — Marcos: pagar o mínimo legal já, e concentrar proteção na parte disponível (resposta ao pedido da cliente).**
- O "mínimo possível" de Marcos = sua legítima individual = **1/6 do acervo ≈ R$ 3.088.333** (ver A4; abaixo disso a lei corrige por redução/colação). Recomendado: **doar a Marcos, agora, quotas nesse valor** (nua-propriedade, com **usufruto vitalício reservado** a ela) — ≈ **21,40% das quotas** (3.088.333 ÷ 14.430.000 dos 9 locados). ITCMD da fatia dele: 4% × 3.088.333 ≈ **R$ 123.533**. Isso quita a legítima dele de forma transparente e elimina o risco de redução das doações feitas a Ricardo e Paula.
- **Amarra-lo com as três cláusulas sobre essa fatia mínima é juridicamente frágil**: art. 1.848 exige **justa causa declarada em testamento**, e o simples afastamento de 6 anos não consta da biblioteca como justa causa **[NÃO VERIFICADO NA BIBLIOTECA]** (ver A5). Se ela insistir em cláusulas sobre Marcos, os caminhos são: (i) testamento com justa causa declarada — risco de queda da cláusula se o juiz não a aceitar; ou (ii) dar-lhe um pouco **acima** do mínimo (da parte disponível) e cláusular **só o excedente**, que é seguro (A5).
- **Ricardo e Paula:** doar-lhes também as legítimas individuais (≈ 21,40% das quotas cada) e destinar a **parte disponível (≈ R$ 9,265 mi)** — quotas remanescentes (≈ 35,8% delas) + aplicações + imóveis próprios — a eles, por doação posterior ou testamento, **aí sim com as cláusulas de incomunicabilidade/impenhorabilidade/inalienabilidade**, que sobre a disponível são cabíveis. Efeito prático de governo: Marcos ficaria com ~21% das quotas nuas — minoria; os detalhes de administração/voto em quotas com usufruto reservado **não estão na biblioteca** **[NÃO VERIFICADO NA BIBLIOTECA]** — exigir ajuste contratual no contrato social.
- Ressalva honesta: a legítima é calculada **pelo valor do acervo na morte** (CC art. 1.846). Travar o mínimo agora é substancialmente melhor, mas se os imóveis valorizarem muito, Marcos ainda pode pleitear **complemento** de diferença — risco residual, não anulável por este plano.

**Passo 3 — ITCMD da doação: orçar sobre mercado.**
- 4% × mercado das quotas (R$ 16,43 mi ou R$ 14,43 mi c/ só locados) = **R$ 657.200 (ou R$ 577.200)** — a SEFAZ/SP não aceita o contábil histórico inferior (Decreto 46.655/2002, art. 14, §4º, via biblioteca). Possível diluição 2/3 + 1/3 (biblioteca sinaliza "verificar"). Risco de alta pela progressividade da EC 132/2023 pendente em SP: **quem pode doar logo, doa logo**.
- Custo total de entrada: cenário "tudo dentro" (11 imóveis): ITBI 492.900 + ITCMD 657.200 ≈ **R$ 1.150.100**; estrutura recomendada (9 locados): 432.900 + 577.200 ≈ **R$ 1.010.100** — esse é o preço verdadeiro da "sucessão resolvida", contra uma economia de ~R$ 101,5 mil/ano de aluguel. Distribuição desse ITCMD no plano do Passo 2: fatia de Marcos ≈ R$ 123.533 (21,40% de 577.200), Ricardo+Paula ≈ R$ 453.667.

**Passo 4 — Testamento + fechamento de pontas.**
- Fazer **testamento** (para a parte disponível; e para eventual deserdação fundamentada, se houver causa legal). Sem testamento hoje, nada disso existe.
- Resolver o **inventário do esposo (2019)** antes de qualquer integralização (premissa P1 — em consulta à cliente).
- As **aplicações de R$ 2,1 mi** e os imóveis próprios fora da holding ainda terão inventário; considerar doação em vida parcial (ITCMD 4%) ou testamento.

---

## Pergunta da cliente (rodada 3) — "Se eu doar tudo em vida para o Ricardo e a Paula, o que sobra para o Marcos herdar? Nada, certo?"
### Resposta direta: **Errado. Não vira "zero" — Marcos continuaria tendo direito a ≈ R$ 3.088.333 (1/6 do acervo), e a briga judicial seria certa.**

Em linguagem simples (fundamentos já demonstrados em A4, `cc_legitima_doacao.md`):

1. **A holding não muda o Código Civil.** Ela decide *quem administra* e *como o fluxo passa*; não decide *quem é herdeiro necessário*. Filhos são herdeiros necessários "de pleno direito" (CC arts. 1.845/1.846) — a legítima deles não depende de a doação ser em vida, na palestra ou em cartório.
2. **Doar em vida a filho não é presente definitivo — é adiantamento de herança** (CC art. 544): na abertura da sucessão, Ricardo e Paula são obrigados a **trazer as doações de volta para a contagem** (colação, CC arts. 2.002-2.012). O "acervo ficto" para essa conta é tudo o que Helena tinha: ≈ R$ 18.530.000 (P1).
3. **A conta:** legítima = metade do acervo = 18.530.000 ÷ 2 = R$ 9.265.000, dividida pelos 3 filhos → **1/6 de Marcos = 18.530.000 ÷ 6 = R$ 3.088.333**. Tendo ele recebido **R$ 0** na partilha de doações, falta-lhe o 1/6 inteiro.
4. **O que acontece na prática:** as doações feitas a Ricardo e Paula são **reduzidas até recompor** os R$ 3.088.333 de Marcos (CC art. 549 — doação inoficiosa). Ou seja, o palestrante prometeu "decidir quem recebe"; a realidade é que, doar tudo aos dois, **Helena estaria só escolhendo de qual bolso de quem ela gosta sairá a parte de Marcos** — com colação, ação de redução, custos de advogado e litígio entre irmãos (e Marcos cobraria **em juízo contra os próprios irmãos**).
5. **Pior ainda sob a premissa P1:** se o inventário do esposo (†2019) não foi feito, Marcos **já é coproprietário** de parte dos imóveis — Helena sequer conseguiria integralizar e doar "tudo" sem a anuência dele.
6. **A rota honesta para o objetivo dela ("o mínimo possível")** é a do Passo 2: **doar a Marcos agora, em vida, exatamente o 1/6 ≈ R$ 3.088.333** (≈ 21,40% das quotas, nua-propriedade com usufruto reservado; ITCMD ≈ R$ 123.533). Isso quita a legítima dele, trava o valor, blinda Ricardo e Paula de redução/colação contenciosa e mantém Helena no controle (usufruto + administração). "Cortar" Marcos por inteiro só é possível por **deserdação com causa legal em testamento** ou **indignidade** — e, com o que a cliente informou (apenas 6 anos de afastamento), não há base verificável para isso (A4).

## Desconhecidos remanescentes (cliente sem mais informações — não repetiremos perguntas)
- **P1 não respondida:** inventário do esposo (†2019) e titularidade real dos imóveis. Se parte já for dos filhos, os valores de ITBI/ITCMD/legítima mudam e a integralização exige anuência deles (Marcos incluído). **Risco material, permanece aberto.**
- Valores de **IPTU e condomínio dos imóveis vagos**: não informados. Se dedutáveis na PF, o imposto de PF cai (economia PJ um pouco menor); se não, neutro. Lacuna dupla (valor + regra) **[NÃO VERIFICADO NA BIBLIOTECA]**.
- **Justa causa** do art. 1.848 para cláusulas sobre a legítima de Marcos: a cliente não trouxe fatos além do afastamento de 6 anos; o padrão legal não está na biblioteca — viabilidade da estratégia de cláusulas sobre a fatia mínima permanece **em aberto**.
- Política de distribuição de lucros da PJ (P4): mantida a hipótese de distribuição integral mensal.
- Questões de credores/dívidas (QUESTIONS Q2): sem resposta — o alerta de fraude contra credores (A5) continua de pé.

## Limites deste parecer
- Autoridade exclusiva: `library/INDEX.md` (5 arquivos). Tudo marcado **[NÃO VERIFICADO NA BIBLIOTECA]** não pode ser sustentado em juízo com o material deste expediente.
- ITCMD doado em outro estado, ITBI de Guarulhos/Cotia/Campos, tabela exata do carnê-leão, base do ITBI, partição 2/3-1/3 do usufruto, fraude contra credores, causas de deserdação, dedutibilidade de IPTU/condomínio de imóveis não locados, governança de quotas com usufruto reservado: lacunas da biblioteca, sinalizadas acima.
- Pendência relevante citada pela própria biblioteca: **RE 1.495.108 (Tema 1.348, STF)** sobre o alcance da exceção da imunidade — se o STF restringir a exceção, o cenário de ITBI de A1 pode melhorar para o contribuinte; hoje vale a literalidade (ITBI devido).
- Prazo/regras: ano-base 2026 conforme biblioteca (Lei 15.270/2025 e LC 214/2025 "in force"; IBS/CBS em apuração-teste).
