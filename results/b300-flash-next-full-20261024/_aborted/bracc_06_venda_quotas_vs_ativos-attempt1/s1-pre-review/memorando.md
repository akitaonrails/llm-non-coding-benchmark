# Memorando — Venda da Vértice: PF (quotas) × PJ (estabelecimento)

**Para:** Hélio Vértice e Beatriz Vértice (50% cada)
**Re:** Propostas A e B do Grupo Meridiano — comparativo tributário, retificação de DIRPF e alegação de ágio
**Data:** 24/10/2026

> **Premissas (declaradas por falta de informação no arquivo do cliente — ver PERGUNTAS.md):**
> (i) fechamento e pagamento em 2026 (o campo do comparativo indica distribuição do caixa da PJ em 2026, sob a Lei 15.270/2025);
> (ii) as 3 parcelas anuais da Proposta A pagas em 2027/2028/2029, sem atualização monetária informada (se houver juros, o ganho tributado cresce na proporção do recebido — Lei 7.713/88, art. 21);
> (iii) na Proposta B, todo o caixa líquido disponível na Vértice após o IRPJ/CSLL é distribuído como lucro aos sócios ainda em 2026;
> (iv) não há outros resultados (receitas operacionais, prejuízos acumulados, PIS/COFINS sobre a operação) — a biblioteca nada diz sobre PIS/COFINS na alienação de estabelecimento, pelo que **não foi possível verificar** esse ponto (item em aberto);
> (v) custo de aquisição das quotas = R$ 600.000,00 por sócio — **confirmado pela cliente na 2ª rodada** ("nas nossas declarações está R$ 600 mil cada"), valor que coincide com o capital de R$ 1.200.000 (50% cada).
> **Rodada 2 do cliente:** as demais premissas (datas, juros/garantias das parcelas, forma de distribuição do caixa da PJ) **não obtiveram resposta** — o cliente informa não ter mais informação; continuam como premissas declaradas e estão sinalizadas como desconhecidas em PERGUNTAS.md e STATUS.md.

**Conclusão: a Proposta A (venda das quotas pela PF) deixa os sócios com R$ 1.479.600,00 a mais que a Proposta B, mesmo pagando R$ 600.000,00 menos. A alegação do sócio está invertida: no Presumido, ganho de capital NÃO entra na presunção — é tributado por inteiro, e ainda há segunda camada no dividendo/IRRF ao distribuir. Não retificar a DIRPF.**

---

## 1. Proposta A — venda de 100% das quotas por R$ 9.000.000 (PF)

Preço: R$ 9.000.000 → R$ 4.500.000 por sócio (50%). Custo declarado: R$ 600.000 por sócio.

**Ganho de capital por sócio** (IN RFB 1.500/2014, arts. 128-141, citado em `library/lei13259_gcap.md`; custo conforme DIRPF, art. 137 citado em `library/lei7713_art21_parcelado.md`):

- 4.500.000 − 600.000 = **R$ 3.900.000 por sócio** (total R$ 7.800.000)

**GCAP — alíquotas progressivas por contribuinte e por alienação** (Lei 8.981/95, art. 21, redação da Lei 13.259/2016 — `library/lei13259_gcap.md`): como o ganho é **por contribuinte**, cada sócio tem R$ 3,9 mi, inteiro na 1ª faixa (≤ R$ 5 mi → 15%). A soma dos dois sócios (R$ 7,8 mi) não é tributada a 17,5%:

- GCAP por sócio: 3.900.000 × 15% = **R$ 585.000**
- GCAP total dos dois: **R$ 1.170.000** (alíquota efetiva 13% do preço)

**Venda a prazo — tributação proporcional** (Lei 7.713/88, art. 21; IN RFB 1.500/2014, art. 137 — `library/lei7713_art21_parcelado.md`): o imposto é pago na proporção das parcelas recebidas, via DARF até o último dia útil do mês seguinte (Lei 8.981/95, art. 21 — `library/lei13259_gcap.md`). Cronograma **por sócio**:

| Parcela | % | Recebe (R$) | DARF GCAP (R$) |
|---|---|---|---|
| Fechamento | 40% | 1.800.000 | 585.000 × 40% = **234.000** |
| Ano +1 | 20% | 900.000 | 585.000 × 20% = **117.000** |
| Ano +2 | 20% | 900.000 | **117.000** |
| Ano +3 | 20% | 900.000 | **117.000** |

(No `comparativo.json`, `cronograma_darf` está **por sócio** e soma `gcap_por_socio`; o caixa acompanha o recebimento — nenhum imposto é antecipado antes do dinheiro.)

**Líquido dos sócios:** 9.000.000 − 1.170.000 = **R$ 7.830.000** (R$ 3.915.000 cada).

## 2. Proposta B — venda do estabelecimento pela PJ por R$ 9.600.000 à vista

**Erro na conta do Hélio:** no Lucro Presumido a presunção de 32% serve para a receita de serviços; o ganho de capital na alienação de ativos (inclusive estabelecimento, carteira e intangíveis) é **acrescido integralmente** à base, sem presunção (Lei 9.430/96, art. 25, II; Lei 9.249/95, art. 20; IN RFB 1.700/2017, art. 215, §3º — `library/lei9430_art25_presumido_gcap.md`). Base do ganho: 9.600.000 − 2.100.000 (valor contábil) = **R$ 7.500.000**.

- IRPJ: 7.500.000 × 15% = 1.125.000; adicional de 10% sobre o que excede R$ 60 mil/trimestre: (7.500.000 − 60.000) × 10% = 744.000 → **R$ 1.869.000**
- CSLL 9% integral: 7.500.000 × 9% = **R$ 675.000**
- Tributos na PJ: **R$ 2.544.000** (33,9% do ganho — e não "32% × alíquota" sobre o faturamento)

Caixa na PJ: 9.600.000 − 2.544.000 = R$ 7.056.000. Para o dinheiro chegar aos sócios há a **segunda camada**: em 2026, lucros/dividendos pagos a PF acima de R$ 50 mil/mês por PJ sofrem **IRRF 10%** (Lei 15.270/2025 — `library/lei15270_dividendos_2026.md`; a isenção antiga só vale para lucros apurados até 2025 com distribuição aprovada até 31/12/2025 — não é o caso, o lucro nasce da venda em 2026):

- IRRF (premissa iii, distribuição em 2026): 7.056.000 × 10% = **R$ 705.600**
  - *Leitura alternativa da norma:* se os 10% incidirem só sobre a parcela que excede R$ 50 mil/mês por sócio, o IRRF cai para 2 × (3.528.000 − 50.000) × 10% = R$ 695.600 (diferença de R$ 10.000; não muda a conclusão). O texto da biblioteca não especifica qual das duas leituras vale — ponto em aberto. O IRRF é **antecipação do IRPFM** do sócio: pode haver ajuste na declaração anual (alíquota final potencialmente maior que 10%) — risco não quantificável com a biblioteca.

**Líquido dos sócios:** 7.056.000 − 705.600 = **R$ 6.350.400** (R$ 3.175.200 cada). Carga total combinada: 3.249.600 / 9.600.000 = **33,9%**, contra 13% na PF.

## 3. Comparativo e recomendação

| | A — PF (quotas) | B — PJ (estabelecimento) |
|---|---|---|
| Preço | 9.000.000 (parcelado) | 9.600.000 (à vista) |
| Tributos | 1.170.000 (GCAP 15%) | 2.544.000 (IRPJ+CSLL) + 705.600 (IRRF) = 3.249.600 |
| **Líquido aos sócios** | **7.830.000** | **6.350.400** |

**Recomendação: PF (Proposta A)** — vantagem de **R$ 1.479.600**, apesar de receber R$ 600 mil menos. Razão estrutural: na PF o ganho passa por **uma** camada a 15% (cada sócio fica na 1ª faixa); na PJ passam por **duas** (34% no ganho + 10% na distribuição). Pelo break-even, a Meridiano precisaria pagar ≈ **R$ 12.090.909** pela PJ para igualar o líquido da PF: 0,9 × (0,66X + 720.000) = 7.830.000 → X = (7.830.000 − 648.000) / 0,594 ≈ 12,09 mi. O prêmio de R$ 600 mil coberto pelo comprador está muito longe disso.

Contra-argumento de fluxo de caixa: a B paga à vista. Se isso pesar, negociar na A: (i) juros sobre as parcelas (aumentam o preço e o tributo só acompanha o recebido), (ii) garantias reais/aval sobre as parcelas, (iii) sinal maior. O custo do parcelamento (impostos a prazo, igual ritmo do caixa) não anula a diferença de R$ 1,48 mi.

## 4. Resposta à Beatriz — retificar a DIRPF para custo de R$ 2 milhões? **Não.**

- O custo de aquisição para o GCAP é **o constante da declaração de bens** do alienante; **não se admite atualização do custo** fora das hipóteses legais expressas (atualização da Lei 14.973/2024, opção de 4%, prazo encerrado) — Lei 7.713/88, art. 21; IN RFB 1.500/2014, art. 137 (`library/lei7713_art21_parcelado.md`). "A empresa vale mais que o capital" não é fato gerador de custo: valor de mercado ≠ custo histórico.
- O custo declarado (R$ 600 mil/sócio) **já coincide com o capital integralizado** (R$ 1.200.000: aumento de 2018 por capitalização de lucros + aporte de 2021 — `documents/contrato_social_historico.md`). Não há aporte nem fato novo que fundamente R$ 2 mi.
- Retificar para inflar custo, sem fato que o fundamente, é **declaração falsa — crime contra a ordem tributária** (Lei 8.137/90, art. 1º, I e II; e a fiscalização pode rever de ofício, CTN art. 149 — `library/crime_ordem_tributaria.md`). O "benefício" seria efêmero: a aquisição será registrada pela Meridiano e a divergência fica exposta. **Não fazer.** Custo correto: R$ 600.000 por sócio.
  - Observação: a biblioteca não contém regra específica sobre se a capitalização de lucros de 2018 aumentaria o custo do sócio além do valor declarado; como o custo declarado já espelha o capital total (inclusive 2018 e 2021), a questão é moot para o valor declarado hoje, mas deve ser verificada se houver discordância sobre o histórico (item em aberto).

### 4.1 Réplica à Beatriz (rodada 2) — "a empresa vale 9 milhões, não faz sentido pagar imposto sobre tudo isso"

Confirmado por ela o custo declarado de R$ 600 mil/sócio. Três respostas, com números:

1. **Vocês não pagam imposto "sobre tudo isso".** A base não é o preço; é o **ganho** = preço − custo. Por sócio: 4.500.000 recebidos − 600.000 de custo = 3.900.000 tributados a 15% = 585.000 de imposto. Cada sócio fica com **R$ 3.915.000 de um total de R$ 4.500.000 recebidos (87%)**; a carga é 15% do ganho e 13% do recebido — a alíquota mais baixa da tabela, porque o ganho de cada um cabe inteiro na 1ª faixa. O que o imposto alcança é exatamente a **valorização** (600 mil → 4,5 milhões): é isso que "a empresa valer 9 milhões" significa para o Fisco — crescimento de patrimônio do sócio. Não há, na biblioteca, regra que zere ou reduza essa base; tributar o ganho é o desenho da lei (Lei 8.981/95, art. 21 — `library/lei13259_gcap.md`).
2. **Não há caminho legal para aumentar o custo agora.** Custo é o da DIRPF e **não se admite atualização** fora de hipótese legal expressa; a única opção de atualização citada na biblioteca (Lei 14.973/2024, pagamento de 4%) teve **prazo encerrado** (`library/lei7713_art21_parcelado.md`). "Valer mais que o capital" não é hipótese legal de custo — é o fato que *gera* o ganho, não o que o elimina.
3. **A "economia" da retificação é pequena e o risco é criminal.** Custo 600 mil → 2 mi economizaria (2.000.000 − 600.000) × 15% = **R$ 210.000 por sócio** (R$ 420.000 no total, ≈5% do líquido). Em troca: declaração falsa (Lei 8.137/90, art. 1º, I/II), revisão de ofício (CTN, art. 149 — `library/crime_ordem_tributaria.md`) e contradição documental — o histórico societário (capital de 1,2 mi: 200 mil + lucros de 2018 + aporte de 2021) não sustenta custo de 4 mi nos dois sócios, e a aquisição será registrada pela Meridiano. Se a preocupação é pagar menos, o lever **lícito** está do lado do **preço** (negociação com a Meridiano — itens 5 e 6), não do custo.

Para comparação: a estrutura de "pagar menos" que ela imagina não existe — na PJ o mesmo ganho sofreria ~34% + 10% na distribuição (item 2). A rota PF é a de menor carga legal disponível nos dois cenários.

### 4.2 Réplica (rodada 3) — "outro contador diz que dá para 'atualizar' o custo pela valorização; existe lei de atualização de bens? Pelo menos uma parte?"

1. **A lei existe, mas está fechada — e não é gratuita.** A própria regra que fixa o custo reconhece "hipóteses legais expressas" de atualização e cita a única aplicável a bens de PF: **Lei 14.973/2024 — opção mediante pagamento de 4%, PRAZO ENCERRADO** (`library/lei7713_art21_parcelado.md`: "não se admite atualização do custo salvo nas hipóteses legais expressas (ex.: Lei 14.973/2024, opção com pagamento de 4% — prazo encerrado)"). Quem não aderiu dentro do prazo não a exerce depois — e as DIRPFs de vocês mostram custo de 600 mil, ou seja, **não houve adesão**. Fora dessa hipótese (e de outras expressas na lei, que a biblioteca não traz), vale o custo declarado: nada de "valor de mercado".
2. **A conta que torna a ideia tentadora — e que só funcionava dentro do programa.** Se o programa estivesse aberto, atualizar 600 mil → 2 milhões custaria 4% × 1.400.000 = R$ 56.000 e economizaria 15% × 1.400.000 = R$ 210.000 de GCAP → ganho líquido de **R$ 154.000 por sócio**. É por isso que a ideia circula. Mas o diferencial 15% − 4% só existe para quem paga os 4% **dentro do prazo legal**. Fazer isso hoje, por retificação de DIRPF, não é "atualização de bens" — é a mesma declaração falsa da rodada anterior (Lei 8.137/90, art. 1º, I/II), com revisão de ofício (CTN, art. 149 — `library/crime_ordem_tributaria.md`), só que agora documentada como recusa prévia: a primeira retificação (600 mil → 2 mi) já seria falsa; a segunda versão ("é atualização") não cria o fato gerador da atualização (adequação ao programa, pagamento dos 4%, tempestividade).
3. **"Pelo menos uma parte" não muda nada.** Fraude parcial é fraude: metade do caminho (600 mil → 1,3 mi, por exemplo) é declaração igualmente sem fundamento (Lei 8.137/90, art. 1º, I e II — o tipo não tem piso; cf. `library/crime_ordem_tributaria.md`). E a divergência fica exposta de qualquer tamanho: o histórico societário soma R$ 1,2 mi de capital e a Meridiano registrará a compra a 9 mi.
4. **Sobre a lei que o "outro contador" diga existir:** se ele citar outro dispositivo de atualização de custo de quotas para PF, **ele não está na nossa biblioteca e não posso confirmá-lo — tratado como não verificado**. Pedimos a indicação do artigo (PERGUNTAS, item 7); com o texto em mãos, analiso em uma página. Sem isso, o único estado do direito que posso afirmar com a biblioteca é: custo = DIRPF, atualização = só hipótese legal expressa, única citada está **encerrada**.

Numéricas do comparativo: inalteradas. O único "caminho de custo" lícito teria que ter sido exercido no prazo de 2024 e não foi; o lever lícito remanescente é o preço (itens 5 e 6).

## 5. Alegação do comprador sobre ágio

"Pagamos mais porque aproveitamos o ágio na nossa estrutura" **não se sustenta como benefício fiscal** na estrutura proposta. Na **compra de ativos/estabelecimento** (Proposta B) não há "ágio" societário: o comprador registra os ativos a valor justo e amortiza/deprecia conforme vida útil; o goodwill da compra de ativos tem tratamento próprio e **não gera a amortização fiscal acelerada da Lei 12.973** (amortização em ≥60 meses só existe no ágio por rentabilidade futura pago na aquisição de **participação societária** com incorporação/fusão/cisão da investida, laudo de perito independente e registro tempestivo — Lei 12.973/2014, arts. 20-22; DL 1.598/77, art. 20 — `library/lei12973_agio.md`). Ou seja, o raciocínio do comprador só faria sentido fiscal para ele na **compra das quotas (Proposta A)** — o que reforça a A na negociação: se o ágio vale para a Meridiano, ela deve pagar **mais** para comprar as quotas, não para comprar o estabelecimento. Ponto de negociação: usar a própria alegação para subir o preço da Proposta A em direção ao prêmio que ela ofereceu na B (e além). Não inventamos valor ao ágio: a biblioteca não permite mensurar o benefício para o comprador.

## 6. Riscos e pontos de negociação

1. **Risco de crédito (A):** 60% do preço em 3 parcelas anuais — exigir garantia (alienação fiduciária de quotas até a liquidação, imóveis, aval) e, se possível, juros; sem atualização informada, o parcelamento é de juro zero aparente (verificar — PERGUNTAS).
2. **Risco da "casca" (B):** a Vértice ficaria sem ativo operacional, com passivos residuais, custos de encerramento e responsabilidade por contratos/tributos pretéritos; e a distribuição do caixa em 2026 sujeita-se ao IRRF de 10% e ao IRPFM (antecipação).
3. **PIS/COFINS sobre a alienação do estabelecimento:** não há material na biblioteca; não verificável — pode piorar a Proposta B.
4. **IRRF do dividendo:** leitura da base de incidência (integral vs. excedente de R$ 50 mil/mês) ambígua na biblioteca — diferença de R$ 10 mil; e a tributação definitiva depende do IRPFM de cada sócio (não quantificável com a biblioteca).
5. **Datas:** premissa de fechamento em 2026; se a distribuição da PJ ocorresse em 2025 sob regra antiga, o IRRF não valeria — mas a venda e o lucro ainda não ocorreram, e a norma da biblioteca é a de 2026. Confirmar calendário (PERGUNTAS).
6. **Garantias do negócio (A):** representação sobre passivos ocultos, retenção/escrow de parte do sinal.
7. **Não retificar DIRPF** — risco criminal (item 4), sem ganho econômico durável.

*Tributos calculados com shell/Python; memória de cálculo acima. Nenhum valor foi "arredondado para fechar": divergências e pontos não verificáveis estão marcados como em aberto em STATUS.md.*
