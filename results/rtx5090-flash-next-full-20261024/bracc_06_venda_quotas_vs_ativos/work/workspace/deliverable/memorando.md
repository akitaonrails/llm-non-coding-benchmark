# Memorando — Venda da Vértice Engenharia Consultiva Ltda.
**Para:** Hélio Vértice e Beatriz (sócios, 50%/50%)
**Assunto:** Proposta A (venda de quotas, PF) × Proposta B (venda do estabelecimento pela PJ) — comparativo e resposta às dúvidas

## 0. Resumo (números)

| | Proposta A — PF vende quotas (R$ 9,0 mi) | Proposta B — PJ vende estabelecimento (R$ 9,6 mi) |
|---|---|---|
| Ganho de capital | R$ 3.900.000 por sócio | R$ 7.500.000 na PJ |
| Imposto na ponta vendedora | GCAP R$ 585.000/sócio → **R$ 1.170.000** | IRPJ+CSLL **R$ 2.544.000** |
| Imposto na distribuição | — | IRRF 10% (2026): **R$ 705.600** |
| **Carga total** | **R$ 1.170.000 (13,0% de 9,0 mi)** | **R$ 3.249.600 (33,9% de 9,6 mi)** |
| **Líquido nos sócios** | **R$ 7.830.000** | **R$ 6.350.400** |

**Recomendação: Proposta A (PF, quotas)** — mesmo com preço R$ 600 mil menor, sobra R$ **1.479.600** a mais para os sócios na Proposta A. A premissa do Hélio está errada (seção 2) e o argumento do comprador sobre ágio não se sustenta na Proposta B como estruturada (seção 5). **Não retificar a DIRPF** para inflar o custo (seção 4) — além de indevido, é crime.

## Premissas (relevem se algo divergir)
**O cliente confirmou não ter informações adicionais sobre os itens de `QUESTIONS.md`.** As premissas abaixo passam a **assunções finais**, e o impacto de cada incerteza está dimensionado na seção 7 — nenhuma delas altera a recomendação.
- Fechamento e primeira parcela em 2026; parcelas anuais sem atualização monetária (Lei 7.713/88, art. 21 tributa também a atualização, se houver — `library/lei7713_art21_parcelado.md`).
- Vértice não tem lucros apurados até 2025 com distribuição aprovada até 31/12/2025 que venham a ser distribuídos no contexto da operação (ver QUESTIONS). Se houver, parte da distribuição da Proposta B poderia ficar fora do IRRF de 10% (Lei 15.270/2025 — `library/lei15270_dividendos_2026.md`), melhorando levemente a B, sem fechar o gap de R$ 1,48 mi.
- Venda do estabelecimento pela PJ gera ganho de capital contábil no trimestre do fechamento; Presumido apurado por trimestre, adicional devido (ganho >> R$ 60 mil/trimestre).
- Custo de aquisição das quotas = R$ 600.000/sócio, conforme DIRPFs (documents/contrato_social_historico.md).

---

## 1. Proposta A — cada sócio (PF) vende suas quotas: R$ 9.000.000
Cada sócio recebe 50% = **R$ 4.500.000**; custo (DIRPF) = **R$ 600.000**.

**Ganho por sócio = 4.500.000 − 600.000 = R$ 3.900.000** (ganho total R$ 7.800.000).

GCAP progressivo (Lei 8.981/95, art. 21, redação Lei 13.259/2016 — `library/lei13259_gcap.md`): 15% até R$ 5 mi. Como as **faixas valem por contribuinte e por alienação**, cada um tributa 3,9 mi — tudo na 1ª faixa:

- GCAP por sócio = 3.900.000 × 15% = **R$ 585.000**
- GCAP total dos dois = **R$ 1.170.000**

Contrafactual útil: se um único contribuinte tivesse o ganho inteiro de 7,8 mi, pagaria 5.000.000×15% + 2.800.000×17,5% = 750.000 + 490.000 = **R$ 1.240.000** — a divisão 50/50 economiza R$ 70.000. Atenção: bens da **mesma natureza** alienados em partes **no mesmo ano** são somados; Hélio e Beatriz são contribuintes distintos, então cada um fica só com 3,9 mi.

**Venda a prazo (40% + 3×20%)** — Lei 7.713/88, art. 21 (`library/lei7713_art21_parcelado.md`): o ganho é tributado na proporção das parcelas recebidas. Como a alíquota efetiva é 15% e não muda entre parcelas (cada parcela de ganho por sócio: 1.560.000, 780.000, 780.000, 780.000 — sempre ≤ 5 mi no cômputo anual de cada um, somadas: 3,9 mi), o DARF por sócio acompanha o caixa:

| Momento | Parcela recebida (sócio) | Ganho tributável (sócio) | DARF GCAP (sócio) | DARF dos 2 sócios |
|---|---|---|---|---|
| Fechamento (2026) | 40% = 1.800.000 | 1.560.000 | **234.000** | **468.000** |
| +12m (2027) | 20% = 900.000 | 780.000 | **117.000** | **234.000** |
| +24m (2028) | 20% = 900.000 | 780.000 | **117.000** | **234.000** |
| +36m (2029) | 20% = 900.000 | 780.000 | **117.000** | **234.000** |
| | | 3.900.000 | **585.000** | **1.170.000** |

(no `comparativo.json`, `cronograma_darf` = DARF **dos dois somados** por vencimento; soma = gcap_total.) Pagamento via DARF até o último dia útil do mês seguinte ao recebimento (Lei 8.981/95, art. 21, redação da Lei 13.259/2016 — `library/lei13259_gcap.md`).

**Líquido dos sócios (A) = 9.000.000 − 1.170.000 = R$ 7.830.000** (R$ 3.915.000 cada).

## 2. Por que o Hélio está errado: no Presumido, ganho de capital NÃO passa por 32%
A conta "32% do faturamento" é a presunção sobre **receita bruta de serviços** (o percentual de 32% vem dos documentos do cliente — `documents/contrato_social_historico.md` e e-mail do Hélio; a biblioteca menciona os percentuais de presunção mas não especifica este — e nada nos cálculos depende dele, pois o ganho entra integral na base). Ganho de capital na alienação de ativos (inclusive estabelecimento) **não entra na presunção**: entra **integralmente** na base do IRPJ, pela diferença entre valor de alienação e valor contábil, com IRPJ 15% + adicional de 10% e CSLL 9% (Lei 9.430/96, art. 25, II; Lei 9.249/95, art. 20; IN RFB 1.700/2017, art. 215, §3º — `library/lei9430_art25_presumido_gcap.md`).

Ou seja, a PJ é tributada por dentro a ~**34%** sobre o ganho (15% + 10% adicional + 9% CSLL) — alíquota muito pior que os 15% de GCAP de cada sócio — e depois o caixa ainda sofre **IRRF 10%** ao descer para os sócios (Lei 15.270/2025, vigente desde 2026 — `library/lei15270_dividendos_2026.md`). A Presunção de 32% (que geraria IRPJ/CSLL sobre 32% de 9,6 mi) nem seria o pior cenário: aqui o ganho real de 7,5 mi é que é tributado integralmente.

### Cálculo da Proposta B
Ganho na PJ = 9.600.000 − 2.100.000 (valor contábil) = **R$ 7.500.000**.

- IRPJ: 7.500.000 × 15% = 1.125.000; adicional: (7.500.000 − 60.000) × 10% = 744.000 → **1.869.000**
- CSLL: 7.500.000 × 9% = **675.000**
- Tributo PJ = **R$ 2.544.000** (34% do ganho, menos o adicional não devido sobre os R$ 60 mil/trimestre)
- Caixa distribuível: 9.600.000 − 2.544.000 = 7.056.000
- Distribuição em 2026 → acima de R$ 50 mil/mês por PJ a PF: **IRRF 10%** = **705.600** (Lei 15.270/2025). O texto da biblioteca não diz se os 10% incidem sobre o excedente dos R$ 50 mil/mês ou sobre o valor total quando a faixa é ultrapassada; adotei conservadoramente 10% sobre a distribuição inteira (o bound contrário — IRRF zero por escalonamento — está na seção 3 e não inverte a conclusão). Como o IRRF é **antecipação do IRPFM**, o ajuste na pessoa física pode alterar o valor final conforme outros rendimentos de cada sócio — não estimado por falta de dados (QUESTIONS).

**Líquido dos sócios (B) = 7.056.000 − 705.600 = R$ 6.350.400** (R$ 3.175.200 cada).

## 3. Comparação e sensibilidade
- Vantagem da Proposta A: **7.830.000 − 6.350.400 = R$ 1.479.600** (o "pagamos mais" de R$ 600 mil é amplamente insuficiente).
- Carga efetiva: A = 13,0% do preço; B = 33,9% do preço.
- A Proposta B só empataria com a A se o preço fosse ≈ **R$ 12,09 milhões** (sob a hipótese conservadora do JSON, IRRF 10% na distribuição inteira): líquido_B(P) = 0,9 × (P − (0,34×(P − 2.100.000) − 6.000)) = 0,594P + 648.000 = 7.830.000 → P ≈ 12.090.909. No melhor caso extremo de B (distribuição inteira escalonada dentro da faixa de isenção, IRRF → 0), o preço de empate cairia para **P ≈ 10.772.727** (0,66P + 720.000 = 7.830.000) — ainda assim bem acima dos 9,6 mi oferecidos.
- Se a distribuição da PJ fosse escalonada, os pagamentos até R$ 50 mil/mês por sócio ficariam fora dos 10% (Lei 15.270/2025). O teto dessa economia **não é desprezível**: distribuindo 3.528.000 por sócio dentro da faixa (50 mil/mês), os 7.056.000 inteiros sairiam isentos de IRRF em ≈ 71 meses (~6 anos) — economia máxima de **R$ 705.600**, o IRRF inteiro. Mesmo nesse extremo, B fica em 7.056.000 e **A ainda vence por R$ 774.000** (mesmo bound da linha 3 da seção 7). No JSON usei a hipótese conservadora de IRRF sobre a distribuição inteira.

## 4. Beatriz: NÃO retificar a DIRPF para R$ 2 milhões por sócio

O custo de aquisição para o GCAP é **o constante da declaração de bens** (IN RFB 1.500/2014, art. 137, no texto de `library/lei7713_art21_parcelado.md`) — e não se admite atualização do custo fora das hipóteses legais expressas (a opção da Lei 14.973/2024 com 4% teve prazo encerrado, conforme o mesmo texto). O custo atual de R$ 600 mil/sócio está correto e é documentado pelo histórico: capital de 1.200.000 dividido por dois = 600.000, formados por 2014 (R$ 200 mil subscritos) + 2018 (capitalização de lucros, +600 mil) + 2021 (aporte em dinheiro, +400 mil). A capitalização de 2018 **já aumentou** o custo na forma da lei — "a empresa vale mais" não é fato que altere custo de aquisição.

Retificar para R$ 2 mi por sócio seria **prestar declaração falsa para reduzir tributo — crime contra a ordem tributária** (Lei 8.137/90, art. 1º, I e II), e a autoridade fiscal pode **revisar de ofício a declaração** (CTN, art. 149 — o artigo consta da linha de citação de `library/crime_ordem_tributaria.md`; o trecho disponível não detalha seu alcance, então a revisão é apontada como risco associado à citação, não como transcrição de texto normativo). Consequência prática além do risco penal: ganho reconstituído + multa + juros, com a venda sob os holofotes justamente pela operação em curso. O "benefício" aparente (menos 1,4 mi de ganho por sócio: 2.000.000 − 600.000 = 1.400.000 × 15% ≈ R$ 210 mil por sócio, R$ 420 mil no total) não compensa o risco criminal e de revisão. Resposta curta: **não dá pra fazer** — nem seria possível em segredo, porque a compra de quotas por grupo relevante tipicamente desperta malha/verificação.

### 4.1 Follow-up da Beatriz (turno 3): "outro contador disse que dá pra atualizar com a valorização — não existe lei de atualização de bens? Pelo menos uma parte?"

Resposta curta: **existe lei de atualização, mas ela é janela com pedágio pago antes — não ajuste grátis na venda; e não existe modalidade "parcial".**

1. **A regra geral proíbe exatamente o que foi proposto:** o custo do GCAP é **o constante da declaração de bens** e "**não se admite atualização do custo salvo nas hipóteses legais expressas**" (Lei 7.713/88, art. 21; IN RFB 1.500/2014, art. 137 — `library/lei7713_art21_parcelado.md`). Atualizar "pela valorização" no momento da venda é a hipótese vedada.
2. **A única hipótese legal de atualização listada na biblioteca é a Lei 14.973/2024** (opção mediante **pagamento de 4%**) — e o texto da biblioteca registra **prazo encerrado**. Era exatamente o caminho legítimo que o colega descreve: paga-se um pedágio **antes**, o custo sobe legalmente e o GCAP depois economiza. Contas por sócio daquela janela (se aplicada às quotas, 600 mil → 2 mi; o trecho da biblioteca não detalha a base de cálculo dos 4%, logo as contas são condicionais): pedágio 4% × 1.400.000 = **R$ 56.000**; economia de GCAP 15% × 1.400.000 = **R$ 210.000**; líquido ≈ **+R$ 154.000**. A janela passou — não há reabertura nem adesão retroativa no texto disponível. **Se o colega conhece outra lei de atualização, que aponte artigo e vigência**: fora do `library/INDEX.md` esse dispositivo é **não verificável** nesta contratação e não pode fundamentar a retificação.
3. "**Pelo menos uma parte**" não é uma terceira via: atualização parcial sem fato que a funde cai na mesma vedação do item 1 e no mesmo crime descrito no corpo da seção 4 (Lei 8.137/90, art. 1º, I e II) — o elemento "declaração falsa" existe quer o custo inventado seja 2,0 mi, 1,5 mi ou 1,0 mi; a única diferença é o tamanho da fraude. E a revisão de ofício continua possível (CTN, art. 149), com o cruzamento fácil: quotas vendidas a R$ 4,5 mi/sócio × histórico societário de R$ 600 mil em DIRPFs sucessivas.
4. **A "atualização" que a lei admite já foi feita pela via correta:** a capitalização de lucros de 2018 (+R$ 300 mil por sócio) e o aporte de 2021 (+R$ 200 mil) **já aumentaram** o custo — R$ 100 mil (2014) + R$ 300 mil + R$ 200 mil = **R$ 600 mil, hoje**. Valorização da empresa não é fato gerador de custo: custo vem de fato patrimonial documentado (subscrição, aporte, capitalização), registrado antes da venda.
5. Para o comparativo, nada muda: a Proposta A segue com ganho de R$ 3,9 mi/sócio e GCAP de R$ 585 mil/sócio; a resposta continua **não retificar** (`retificar_custo_dirpf: "nao"`).

## 5. A alegação do comprador sobre ágio
O comprador paga R$ 600 mil a mais na Proposta B "porque aproveita o ágio na estrutura dele". Pela lei, isso não fecha (Lei 12.973/2014, arts. 20–22; DL 1.598/77, art. 20 — `library/lei12973_agio.md`):

- O **ágio por rentabilidade futura (goodwill) dedutível** (amortização em no mínimo 60 meses, base em laudo de perito independente, protocolado/registrado tempestivamente) existe na **aquisição de participação societária seguida de incorporação/fusão/cisão da investida** — i.e., o comprador teria de **absorver o patrimônio da Vértice**.
- Na **compra de ativos/estabelecimento**, não há "ágio societário": o comprador registra os ativos a valor justo e deprecia/amortiza conforme vida útil; o goodwill da compra de ativos **não gera a amortização fiscal da Lei 12.973**.

Pontos de negociação:
1. Se o comprador quer ágio dedutível, a estrutura que o gera é ele **comprar as quotas e depois incorporar a Vértice** (estrutura da Proposta A, não da B). Se essa for a vontade dele, o valor que ele atribui ao benefício do ágio deve aparecer no preço da Proposta A — usar o argumento dele como alavanca para subir os R$ 9 mi.
2. Desconfiar do "R$ 9,6 mi à vista" da B: para o comprador pode ser indiferente ou vantajoso mesmo com o tratamento pior do goodwill — o ágio que ele imagina pode não ser dedutível; o preço maior não é prova de sinergia.
3. Na B, a Vértice sobrevive como "casca": riscos trabalhistas/fiscais/contratuais residuais ficam com os sócios via PJ (decisão societária, fora do escopo tributário deste comparativo), e a liquidação posterior da casca tem custos/prazos próprios. Na A, sócios saem do negócio inteiro.
4. Na A, as 3 parcelas anuais criam risco de crédito do comprador — exigir garantias (caução/penhor das próprias quotas ou alienação fiduciária, aval dos controladores). O parcelamento ajuda no fluxo do GCAP (tributo acompanha o caixa), mas o custo de eventual inadimplemento é dos sócios.
5. Alternativa a explorar: A com 100% à vista ou desconto menor no parcelado; e pedir ao comprador para formalizar laudo/estrutura que ele diz aproveitar (quotas + incorporação) — se ele tem laudo e laudo vale para ele, o preço pode subir.

## 6. Riscos e observações finais
- Presunção de 2026 sobre a Proposta A: a PJ continua prestando serviços normalmente até o fechamento; nada da operação A contamina o Presumido da Vértice.
- Na Proposta B, confirmar o valor contábil de cada ativo transferido: a base do ganho da PJ é contábil (IN RFB 1.700/2017, art. 215, §3º, via `library/lei9430_art25_presumido_gcap.md`); ativos com valor contábil baixo (marca interna, carteira gerada internamente) concentram o ganho de 7,5 mi na PJ.
- IR da distribuição (Lei 15.270/2025) é antecipação: se os sócios tiverem outros rendimentos, o ajuste anual pode exigir mais imposto (ou restituir). Sem dados, tratamos 10% como custo.
- Cálculos conferidos por script; nenhuma reconciliação forçada. Se o fechamento não ocorrer em 2026, o cronograma de DARFs e o IRRF da B se deslocam de ano, mas a conclusão (PF ≈ 13% vs PJ ≈ 34%) permanece.

---

## 7. Incertezas residuais — flag explícito e robustez da conclusão
O cliente não tem informações adicionais (turno 2). As perguntas de `QUESTIONS.md` foram encerradas como **assunções sinalizadas**, cada uma com o quanto poderia mover os números:

| # | Incógnita (não resolvida) | Assunção adotada | Pior impacto possível sobre a conclusão |
|---|---|---|---|
| 1 | Data do fechamento | 2026 | **Zero.** Mesmo que todo o preço fosse recebido num único ano, o ganho por sócio (R$ 3,9 mi) segue < R$ 5 mi → alíquota 15% (faixas por contribuinte e por alienação, `library/lei13259_gcap.md`). Só muda o rótulo dos anos do cronograma. |
| 2 | Correção monetária das parcelas (A) | nenhuma | **Favorável a A.** Cada R$ 1 de correção recebida soma ao ganho tributável proporcionalmente (`library/lei7713_art21_parcelado.md`) e é taxado a 15% → sócios ganham +R$ 0,85 líquidos. Para estourar a faixa de 15% no ano, a correção precisaria passar de ~R$ 3,4 mi por sócio no ano (impossível no prazo). |
| 3 | Lucros pré-2025 com distribuição aprovada até 31/12/2025 (B) | não existem | Só melhora B: cada R$ 1 distribuído como lucro pré-2025 aprovado economiza R$ 0,10 de IRRF (Lei 15.270/2025). Para B empatar com A, seriam necessários **R$ 14.796.000** de dividendos isentos (gap 1.479.600 ÷ 10%) — a Vértice não dispõe de semelhante valor. **No extremo de IRRF zero em toda a distribuição, B fica em R$ 7.056.000 e A ainda vence por R$ 774.000.** |
| 4 | Outros rendimentos dos sócios (ajuste do IRPFM sobre o IRRF de B) | IRRF 10% = custo final | O IRRF é **antecipação do IRPFM** (Lei 15.270/2025). A tabela do IRPFM **não consta da biblioteca**, portanto eventual adicional/restituição **não é verificável aqui** — não estimado. O bound de "0% efetivo" já está coberto na linha 3. |
| 5 | Residência fiscal dos sócios | residentes no Brasil | A biblioteca não cobre não residentes; se algum sócio não for residente, a análise da ponta PF da Proposta A **não pode ser sustentada com a autoridade disponível** — reavaliar antes de fechar. |
| 6 | Garantias das 3 parcelas anuais (A) | — | Não é tributo: é o principal risco da estrutura A. Sem garantia definida, o risco de crédito do comprador fica com os sócios (seção 5, item 4). |

**Conclusão robusta:** em todas as combinações das incógnitas acima, a carga da Proposta A (~13% do preço) permanece muito abaixo da da Proposta B (~34% na PJ + até 10% na distribuição), e a B precisaria de preço entre ≈ **R$ 10,77 mi** (melhor caso extremo: distribuição inteira escalonada isenta de IRRF) e ≈ **R$ 12,09 mi** (hipótese conservadora do JSON) para empatar — muito acima dos 9,6 mi. A recomendação (PF, quotas) e a resposta à Beatriz (não retificar) não dependem de nenhuma das informações faltantes.

*Todas as citações acima referem-se exclusivamente aos arquivos listados em `library/INDEX.md`.*
