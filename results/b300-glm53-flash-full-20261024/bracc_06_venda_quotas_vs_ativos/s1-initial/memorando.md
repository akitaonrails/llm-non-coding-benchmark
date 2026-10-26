# Memorando — Venda da Vértice: PF (quotas) × PJ (estabelecimento)

**Para:** Hélio Vértice e Beatriz Vértice — Vértice Engenharia Consultiva Ltda.
**Assunto:** Comparação tributária entre as duas propostas do Grupo Meridiano; resposta às questões levantadas no e-mail do Hélio.
**Fontes:** exclusivamente os arquivos de `library/INDEX.md`. Não houve acesso a fontes externas. Toda a aritmética abaixo é reproduzível.

---

## 1. Premissas e fatos utilizados

Fatos do cliente (em `documents/`):

- Proposta A: venda de **100% das quotas** por **R$ 9.000.000,00** — 40% à vista no fechamento + 3 parcelas anuais de 20% (40% + 60% = 100%).
- Proposta B: venda do **estabelecimento** (ativos, contratos, marca, carteira) à **PJ** do comprador por **R$ 9.600.000,00** à vista; a Vértice permanece como casca para distribuir o caixa aos sócios.
- Sócios: Hélio 50% / Beatriz 50%. Capital: R$ 1.200.000 (2014: R$ 200.000; 2018: capitalização de lucros até R$ 800.000; 2021: aporte em dinheiro até R$ 1.200.000). **Custo de aquisição declarado nas DIRPFs: R$ 600.000 por sócio.**
- Valor contábil do estabelecimento (ativos − passivos a transferir): **R$ 2.100.000,00**.
- Regime: Lucro Presumido (serviços, 32%).
- Data de referência: outubro de 2026 → a distribuição de caixa da Proposta B ocorreria **em 2026**, sujeita à Lei 15.270/2025.

Premissas declaradas (não confirmadas pelo cliente; se mudarem, os números mudam):

1. **Custo de aquisição = R$ 600.000/sócio**, conforme constante da DIRPF. A regra da biblioteca é que o custo é o da declaração de bens (`lei7713_art21_parcelado.md`). O histórico informado (100 k inicial + 300 k de capitalização em 2018 + 200 k de aporte em 2021, por sócio) soma exatamente R$ 600.000 por sócio, coerente com o documento do cliente. *Item de diligência 6.1* sobre a documentação da capitalização de 2018.
2. **Sem atualização monetária ou juros sobre as parcelas anuais** da Proposta A (nenhuma cláusula informada). A regra do parcelamento prevê tributação "considerando-se a respectiva atualização monetária, **se houver**" (`lei7713_art21_parcelado.md`); como nada foi informado, calculo sobre valores nominais.
3. **Nenhuma outra alienação de bens da mesma natureza no ano** pelos sócios (a regra soma bens da mesma natureza alienados no mesmo ano para as faixas — `lei13259_gcap.md`).
4. **Venda da Proposta B concluída e ganho reconhecido em um único trimestre** (preço à vista), e o valor recebido líquido de tributos é o lucro/passivo distribuível da casca (não há outras receitas/despesas informadas).
5. Distribuição da Proposta B **em pagamento único no mês** da conclusão. Alternativas de calendário em §3.4.
6. A PJ adquire os ativos pelo preço ajustado; não calculo eventual imposto sobre a transferência além dos previstos na biblioteca — ver risco 6.3 (PIS/COFINS/ISS não constam da biblioteca).

---

## 2. Proposta A — venda de quotas (tributação na pessoa física)

### 2.1 Ganho de capital

- Preço por sócio: R$ 9.000.000 × 50% = **R$ 4.500.000**.
- Custo declarado: **R$ 600.000** por sócio.
- **Ganho por sócio: R$ 4.500.000 − R$ 600.000 = R$ 3.900.000**; ganho total dos dois: **R$ 7.800.000**.

### 2.2 Alíquota

Faixas por contribuinte **e por alienação** (`lei13259_gcap.md`): 15% até R$ 5 mi; 17,5% de R$ 5 a 10 mi; 20% de R$ 10 a 30 mi; 22,5% acima de R$ 30 mi.

- Ganho por sócio = R$ 3.900.000 < R$ 5.000.000 → **toda a parcela em 15%**. As faixas superiores não são atingidas: o ganho total da alienação, por contribuinte, é R$ 3,9 mi (< R$ 5 mi), e não há outras alienações da mesma natureza no ano (premissa 3).
- **GCAP por sócio: 15% × 3.900.000 = R$ 585.000.** Total: 2 × 585.000 = **R$ 1.170.000**.

### 2.3 Venda a prazo — cronograma de DARF

Em alienação a prazo, o imposto incide **na proporção das parcelas recebidas em cada mês**, devido até o último dia útil do mês seguinte ao do recebimento, por DARF (`lei7713_art21_parcelado.md`; `lei13259_gcap.md`).

| Evento | Recebido | % do preço | Ganho realizado/sócio (3,9 mi × %) | DARF/sócio (15%) | DARF total (2 sócios) | Prazo |
|---|---|---|---|---|---|---|
| Fechamento | 1.800.000 | 40% | 1.560.000 | 234.000 | 468.000 | último dia útil do mês seguinte ao fechamento |
| Parcela 1 (12 meses) | 900.000 | 20% | 780.000 | 117.000 | 234.000 | mês seguinte ao 1º recebimento anual |
| Parcela 2 (24 meses) | 900.000 | 20% | 780.000 | 117.000 | 234.000 | idem, 2º recebimento |
| Parcela 3 (36 meses) | 900.000 | 20% | 780.000 | 117.000 | 234.000 | idem, 3º recebimento |
| **Total** | 9.000.000 | 100% | 3.900.000 | **585.000** | **1.170.000** | |

Em `comparativo.json`, `cronograma_darf = [468000, 234000, 234000, 234000]` (eventos: fechamento + 3 parcelas; valores dos **dois sócios somados**; por sócio é a metade). Cada sócio paga o próprio DARF (contribuinte é o alienante — `lei13259_gcap.md`).

### 2.4 Líquido

- **Líquido aos sócios: R$ 9.000.000 − R$ 1.170.000 = R$ 7.830.000** (R$ 3.915.000 por sócio).
- Carga efetiva: 1.170.000 / 9.000.000 = **13,0% do preço**, e note-se: 15% do ganho, diluída no tempo conforme o recebimento.

---

## 3. Proposta B — venda do estabelecimento pela PJ

### 3.1 O erro de premissa do Hélio

No Lucro Presumido, a presunção de 32% incide sobre a **receita bruta da atividade**. A alienação de bens do ativo permanente segue outra regra: o **ganho de capital** (valor da alienação − valor contábil) é **acrescido integralmente** à base do IRPJ, sem presunção; idem para a CSLL, que incide 9% sobre a base integral (`lei9430_art25_presumido_gcap.md`). Portanto a conta "32% × faturamento × alíquota" **não descreve o imposto desta venda**.

### 3.2 Memória de cálculo

- Preço da alienação: **R$ 9.600.000**; valor contábil do estabelecimento: **R$ 2.100.000**.
- **Ganho PJ: R$ 9.600.000 − R$ 2.100.000 = R$ 7.500.000** (integralmente somado à base — `lei9430_art25_presumido_gcap.md`).
- IRPJ: 15% × 7.500.000 = **1.125.000**; adicional de 10% sobre o que excede R$ 60 mil/trimestre: 10% × (7.500.000 − 60.000) = **744.000** (o ganho inteiro cai em um único trimestre, preço à vista). **IRPJ total: R$ 1.869.000**.
- CSLL: 9% × 7.500.000 = **R$ 675.000**.
- **Tributo da PJ: 1.869.000 + 675.000 = R$ 2.544.000**.
- Sobrando na casca para distribuir: 9.600.000 − 2.544.000 = **R$ 7.056.000** (R$ 3.528.000 por sócio).

### 3.3 Distribuição aos sócios em 2026 — IRRF de dividendos

Lucros e dividendos pagos por PJ a pessoa física **acima de R$ 50.000/mês** sujeitam-se a **IRRF de 10%**, a partir de 2026; e o valor retido é nessa condição **antecipação** (`lei15270_dividendos_2026.md`). Os lucros aqui seriam apurados em 2026, de modo que a isenção de lucros "apurados até 2025 com distribuição aprovada até 31/12/2025" **não se aplica** (`lei15270_dividendos_2026.md`).

- Pagamento único no mês, por sócio: R$ 3.528.000 > R$ 50.000.
- **Leitura adotada** (coerente com o estilo da própria biblioteca, que trata "acima de R$ 60 mil/trimestre" como parcela excedente no adicional do IRPJ e as faixas do GCAP como intervalos): o imposto incide sobre a **parcela mensal que excede** R$ 50.000 por fonte: 10% × (3.528.000 − 50.000) = **R$ 347.800 por sócio → R$ 695.600 no total**.
- **Leitura alternativa** (10% sobre o montante mensal integral quando o pagamento supera o limite): 10% × 7.056.000 = **R$ 705.600** — diferença de apenas **R$ 10.000** (5.000 por sócio). A biblioteca **não fixa expressamente** qual leitura vale; assinalei a divergência e não forcei a escolha de um terceiro número. Tudo o que se segue fica numericamente inalterado em termos de conclusão (impacto ≤ 0,104% do preço).
- O IRRF é antecipação do imposto mínimo anual (IRPFM); as regras anuais de compensação do IRPFM **não estão detalhadas na biblioteca** — não foi modelado crédito/ressarcimento posterior (item 6.5).
- **Líquido aos sócios: R$ 9.600.000 − 2.544.000 − 695.600 = R$ 6.360.400** (R$ 3.180.200 por sócio).
- Carga efetiva: (2.544.000 + 695.600) / 9.600.000 = **33,7% do preço**.

### 3.4 Variação de calendário (planejamento condicional)

Se a distribuição puder ocorrer em **12 pagamentos mensais de R$ 588.000 por sócio**, cada mês conserva a faixa abrangida pelo limite: isenção de até R$ 50.000 por fonte/mês e 10% sobre o excedente — 10% × (7.056.000 − 2 × 12 × 50.000) = **R$ 585.600** de IRRF (economia de R$ 110.000 frente ao pagamento único). Isso pressupõe que a casca tenha lucro apurado mês a mês disponível para distribuir; a biblioteca não descreve a periodicidade de apuração/distribuição no Presumido, então é **planejamento condicional, não calculado como cenário-base**.

---

## 4. Comparativo

| | **A — PF (quotas)** | **B — PJ (estabelecimento)** |
|---|---:|---:|
| Preço | 9.000.000 | 9.600.000 |
| Tributos na esfera de venda | GCAP total 1.170.000 | IRPJ 1.869.000 + CSLL 675.000 = 2.544.000 |
| IRRF distribuição 2026 | — (não há dividendos) | 695.600 |
| **Líquido aos sócios** | **7.830.000** | **6.360.400** |
| Líquido por sócio | 3.915.000 | 3.180.200 |
| Carga efetiva sobre o preço | 13,0% | 33,7% |

**Diferença: a Proposta A deixa R$ 1.469.600 a mais nos bolsos dos sócios.** Controlando pelo preço (ambas a 9,6 mi): PF líquido 8.340.000 (ganho/sócio 4.200.000 × 15% = 630.000/sócio) × PJ líquido 6.360.400 — o PJ perde R$ 1.979.600 mesmo com o preço mais caro.

**Recomendação: vender as quotas (Proposta A), retenção do custo na DIRPF como está.** `recomendacao = "pf"`; `retificar_custo_dirpf = "nao"`.

### 4.1 Resposta ao Hélio (e-mail)

Sua frase "imposto é 32% do faturamento vezes a alíquota" está tecnicamente errada para este evento: na venda do estabelecimento a base é o **ganho integral** (9.600.000 − 2.100.000 = 7.500.000), não a receita presumida (`lei9430_art25_presumido_gcap.md`). Com a base certa, a PJ paga **R$ 2.544.000** de IRPJ/CSLL — **mais que os R$ 1.170.000 das duas vendas na PF somadas** — e ainda há o IRRF de 2026 sobre a distribuição (R$ 695.600). "Menos imposto pela PJ" **não se confirma; é o oposto**: 1.469.600 menos no bolso, embora o preço seja 600 mil maior.

### 4.2 Resposta à Beatriz (retificação do custo na DIRPF)

**Não.** O custo de aquisição é o constante da declaração de bens; não se admite elevá-lo senão por fato real (`lei7713_art21_parcelado.md`). O histórico social mostra capital de R$ 1.200.000 (600.000 por sócia) — nenhum aporte ou evento legitima custo de R$ 2.000.000 por sócia; "a empresa vale muito mais que o capital" é argumento de **valor de mercado, não de custo fiscal**. Alterar a DIRPF para inflar o custo **sem fato que o fundamente é declaração falsa — crime contra a ordem tributária** (suprimir/reduzir tributo mediante declaração falsa ou inserção de elementos inexatos; `crime_ordem_tributaria.md`), com lançamento de ofício/censo pela fiscalização como conseqência tributária (`crime_ordem_tributaria.md` — CTN art. 149). A economia ilícita visada seria 15% × (2.000.000 − 600.000) × 2 = **R$ 420.000** — expor-se a processo criminal e autuação por 420 mil é ruim negócio, além de contaminar também a venda (o GCAP do parcelamento usaria o custo falso).

Nenhuma alternativa legal identificada na biblioteca aumenta o custo; a própria biblioteca nega a atualização do custo fora das hipóteses legais expressas e a janela da Lei 14.973/2024 (4%) **está encerrada** (`lei7713_art21_parcelado.md`).

---

## 5. A alegação do comprador sobre "ágio"

O Grupo Meridiano diz pagar R$ 600 mil a mais (9,6 mi vs. 9,0 mi) porque "aproveita o ágio na nossa estrutura". Pela biblioteca, **em compra de ativos (estabelecimento) não há "ágio" societário**: o ágio por rentabilidade futura dedutível — amortização fiscal em no mínimo 60 meses — existe na aquisição de **participação societária** e, ainda assim, **só quando a investidora absorve o patrimônio da investida (incorporação, fusão ou cisão)**, mediante laudo de avaliação por perito independente, protocolado/registrado tempestivamente (`lei12973_agio.md`).

Na compra do estabelecimento, o comprador registra os ativos a valor justo e amortiza/deprecia intangíveis e imobilizado conforme a vida útil; o goodwill na compra de ativos tem tratamento próprio e **não gera a amortização fiscal acelerada da Lei 12.973** (`lei12973_agio.md`). Logo, **a justificativa do comprador não encontra amparo na regra da biblioteca para o formato oferecido** (PJ comprando estabelecimento). Do ponto de vista de vocês, o argumento é irrelevante: quem paga os tributos da Proposta B são a Vértice e os sócios; o eventual "benefício do ágio" pertenceria à compradora — e, como demonstrado, nem ele existe no formato proposto.

Duas leituras possíveis (não confirmáveis por falta de dados): (i) o comprador tem estrutura que convergiria para incorporação posterior — aí laudo e prazos importam, e o prêmio pode ser real para ele, não para vocês; (ii) o prêmio é mídia de negociação. Em qualquer caso: **peçam por escrito a razão econômica do prêmio e tratem-no como disputável** — o patamar que ele precisaria atingir está no item 7.

---

## 6. Riscos e pontos de diligência

1. **Custo de aquisição na GCAP (Proposta A).** O custo adotado é o da DIRPF (600 mil/sócio), que coincide com o capital e com a soma dos eventos do histórico (100 inicial + 300 de capitalização + 200 de aporte). **Item em aberto:** obter com o contador a documentação da capitalização de 2018 e a consistência das DIRPFs daqueles anos. A biblioteca **não contém regra** sobre o efeito da capitalização de lucros na base de GCAP da pessoa física — por isso **não afirma** nada sobre isso além do que a biblioteca dá: o custo é o da declaração (`lei7713_art21_parcelado.md`). Se a capitalização de 2018 não for sustentável, restaria no mínimo custo de R$ 300.000/sócio (100 + 200): ganho 4.200.000/sócio, GCAP 630.000/sócio (ainda na faixa de 15%), total 1.260.000, líquido 7.740.000. A diferença é de R$ 90.000 sobre o total de imposto (R$ 1,17 mi) e **não altera a recomendação**, mas deve ser fechada antes da assinatura.
2. **Atualização monetária das parcelas.** Se o contrato final trouxer correção das 3 parcelas anuais, a regra exige considerá-la na tributação proporcional (`lei7713_art21_parcelado.md`). Informem a fórmula para recalcular.
3. **Tributos sobre a transferência não cobertos pela biblioteca.** PIS/COFINS/ISS sobre a alienação do estabelecimento **não constam da biblioteca** — não foram calculados e **não posso afirmar se são devidos** com base no que posso citar. Se devidos na Proposta B, aumentariam a carga da PJ e **reforçam** a recomendação pela PF. ITBI/ITCD também não constam; incidentam sobre o comprador e não foram computados.
4. **Caixa da Proposta A.** Os sócios recebem R$ 3,6 mi no fechamento e R$ 1,8 mi/ano em 3 anos; o DARF acompanha o recebimento, sem desembolso antecipado. Não há, na biblioteca, mecanismo de antecipar o imposto integral na assinatura — o regime é o proporcional ao recebido.
5. **IRPFM.** O IRRF de 10% é antecipação (`lei15270_dividendos_2026.md`); as regras anuais do imposto mínimo (limites, compensação, restituição) **não estão na biblioteca** — não houve modelagem de crédito posterior.
6. **Rendas pessoais dos sócios** (outras fontes, outros dividendos em 2026) não foram informadas; afetariam a declaração anual, não a escolha entre as propostas.

---

## 7. Pontos de negociação

- **Prêmio insuficiente.** A Proposta B paga R$ 600.000 a mais e deixa **R$ 1.469.600** a menos de líquido que a Proposta A. Para empate, o preço da venda à PJ teria de subir para **≈ R$ 12.074.074** (+R$ 3.074.074 sobre 9,0 mi; +R$ 2.474.074 sobre a oferta atual). Derivação: ganho g = P − 2.100.000; IRPJ+CSLL = 0,34·g − 6.000; distribuição d = P − tributo; IRRF = 0,10·(d − 100.000); líquido = 0,594·P + 658.000; igualando a 7.830.000 → P ≈ 12.074.074. Verificação numérica: tributo 3.385.185,19; d = 8.688.888,89; IRRF 858.888,89; líquido = 7.830.000,00 ✔.
- **Mesmo preço, veículo diferente.** Vendendo **quotas a 9,6 mi** (mesmo valor da proposta B, tributação da PF): ganho 4.800.000 − 600.000 = 4.200.000/sócio; GCAP 630.000/sócio; líquido **8.340.000**. Se o comprador prefere estabelecimento por razões próprias, o custo dessa preferência deve aparecer no preço dele — não no bolso de vocês.
- **Agenda do comprador.** Exigir, por escrito, a justificativa do "ágio" (§5); fechamento com quitação expressa do passivo a transferir (base do valor contábil de R$ 2,1 mi) e declarações sobre contencioso/reclamações na casca.
- **Calendário da Proposta A:** 40% na assinatura; antecipar vencimentos das parcelas melhora liquidez e não muda o imposto (proporcional ao recebido).

---

## 8. Conclusão

- **Proposta A (quotas): líquido R$ 7.830.000** (R$ 3.915.000/sócio); imposto total R$ 1.170.000 em 4 DARFs proporcionais aos recebimentos (468.000; 234.000; 234.000; 234.000 — soma dos dois sócios).
- **Proposta B (estabelecimento/PJ): líquido R$ 6.360.400** (R$ 3.180.200/sócio); tributos da PJ R$ 2.544.000 + IRRF da distribuição 2026 R$ 695.600 (leitura alternativa: R$ 705.600 → líquido R$ 6.350.400).
- **Recomendação: Proposta A (PF)** — 1.469.600 a mais no bolso; o prêmio de 600 mil da proposta B não reverte isso (seriam necessários ≈ 12,07 mi pela PJ para empate).
- **Retificar a DIRPF para custo de R$ 2 mi/sócio: não fazer.** Não há fato que o fundamente e a prática configura declaração falsa — crime contra a ordem tributária (`crime_ordem_tributaria.md`).

*Out/2026. Valores em reais, arredondados a centavos. Nada foi forçado a bater: as divergências identificadas (base do IRRF, documentação da capitalização de 2018, tributos não cobertos pela biblioteca) foram mantidas em aberto e assinaladas no item 6 e em STATUS.md.*
