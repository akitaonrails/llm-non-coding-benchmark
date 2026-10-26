# Vértice — comparação das propostas de venda

**Conclusão.** Com o custo e o valor contábil informados, a venda das quotas por R$ 9 milhões deixa **R$ 7.830.000 nominais** aos dois sócios, depois do ganho de capital e ao longo do parcelamento. A venda do estabelecimento por R$ 9,6 milhões deixa **R$ 6.350.400** após IRPJ, CSLL e o IRRF **no cenário assumido abaixo**. A proposta das quotas supera a da PJ em **R$ 1.479.600 nominais**, embora seu preço bruto seja R$ 600.000 menor. Mesmo sem o IRRF projetado, o caixa da PJ depois de IRPJ/CSLL seria R$ 7.056.000, R$ 774.000 abaixo do líquido nominal da venda das quotas. Recomendo negociar a proposta de quotas, sujeito à avaliação do prazo e do risco de recebimento, e **não** elevar artificialmente o custo na DIRPF.

## Premissas e alcance dos números

- Cada sócio vende sua participação de 50% pelo mesmo preço, R$ 4,5 milhões. O custo de R$ 600.000 por pessoa é o declarado em suas DIRPFs. Não foi informada atualização monetária do preço parcelado.
- Para preencher o campo contratual `irrf_distribuicao_2026`, o cenário-base **supõe** fechamento e distribuição em 2026, retirada integral dos R$ 7.056.000 de caixa pós-tributos como dividendos, em **uma única distribuição**, metade para cada sócio, sem saldo de lucros anteriores com isenção preservada. **Não há balanço que demonstre que todo esse caixa pode ser distribuído como dividendos**; caixa e lucro distribuível não são necessariamente iguais. A resposta de Hélio disse apenas “em {ANO} mesmo”: o ano ficou literalmente indefinido; também não informou a forma nem as datas da retirada. Assim, o IRRF de R$ 705.600 e o líquido de R$ 6.350.400 são **condicionais**, não uma previsão fechada. `liquido_socios` é caixa após a retenção na fonte; a referência a qualifica como antecipação do IRPFM, cujo acerto final não foi quantificado. A biblioteca não traz regras sobre o limite societário de distribuição ou a tributação de uma eventual devolução de capital; esses efeitos permanecem **não verificados**. [Dividendos a partir de 2026](../library/lei15270_dividendos_2026.md).
- O adicional de IRPJ usa a faixa trimestral de R$ 60.000 inteira para o ganho da operação. Não há dados sobre outros resultados da PJ no trimestre, que podem consumir essa faixa e elevar o IRPJ aqui atribuído à venda em até R$ 6.000. A comparação também não inclui custos da transação ou tributos sem dados e sem regra na biblioteca.

## Proposta A — quotas vendidas pelas pessoas físicas

| Cálculo | Por sócio | Dois sócios |
|---|---:|---:|
| Preço | R$ 4.500.000 | R$ 9.000.000 |
| Custo declarado | R$ 600.000 | R$ 1.200.000 |
| Ganho: preço − custo | R$ 3.900.000 | R$ 7.800.000 |
| GCAP: ganho × 15% | R$ 585.000 | R$ 1.170.000 |
| Caixa após GCAP | R$ 3.915.000 | **R$ 7.830.000** |

Cada alienante tem ganho inferior a R$ 5 milhões; aplica-se a primeira faixa de 15% **por contribuinte e por alienação**, sem somar os ganhos de Hélio e Beatriz para escolher a alíquota. [Ganho de capital da pessoa física](../library/lei13259_gcap.md).

O imposto é apurado sobre o ganho total e recolhido proporcionalmente a cada parcela recebida. Não se reaplica a tabela progressiva como se cada parcela fosse uma nova alienação. [Venda a prazo](../library/lei7713_art21_parcelado.md).

| Recebimento | Preço recebido, total | DARF total | DARF por sócio |
|---|---:|---:|---:|
| Fechamento, 40% | R$ 3.600.000 | R$ 468.000 = 40% × 1.170.000 | R$ 234.000 |
| 1ª parcela anual, 20% | R$ 1.800.000 | R$ 234.000 | R$ 117.000 |
| 2ª parcela anual, 20% | R$ 1.800.000 | R$ 234.000 | R$ 117.000 |
| 3ª parcela anual, 20% | R$ 1.800.000 | R$ 234.000 | R$ 117.000 |

Cada DARF vence no último dia útil do mês seguinte ao respectivo recebimento. Não há datas de fechamento ou parcelas para indicar dias de calendário. Se o contrato introduzir correção monetária, o tratamento das parcelas deve ser revisto. [Ganho de capital da pessoa física](../library/lei13259_gcap.md); [venda a prazo](../library/lei7713_art21_parcelado.md).

## Proposta B — estabelecimento vendido pela PJ

O ganho é **R$ 9.600.000 − R$ 2.100.000 = R$ 7.500.000**. A presunção de 32% se aplica à receita de serviços indicada no histórico, mas **não** a esse ganho na alienação de ativos: ele entra integralmente nas bases do IRPJ e da CSLL. [Lucro Presumido e ganho de capital](../library/lei9430_art25_presumido_gcap.md).

| Cálculo | Valor |
|---|---:|
| IRPJ básico: 15% × R$ 7.500.000 | R$ 1.125.000 |
| Adicional: 10% × (R$ 7.500.000 − R$ 60.000) | R$ 744.000 |
| **IRPJ** | **R$ 1.869.000** |
| CSLL: 9% × R$ 7.500.000 | R$ 675.000 |
| **IRPJ + CSLL** | **R$ 2.544.000** |
| Caixa na PJ: R$ 9.600.000 − R$ 2.544.000 | R$ 7.056.000 |
| Dividendo hipotético por sócio | R$ 3.528.000 |
| IRRF hipotético: 10% × R$ 7.056.000 | R$ 705.600 |
| **Caixa aos sócios após IRRF** | **R$ 6.350.400** |

Na distribuição única assumida, cada pagamento de R$ 3.528.000 excede R$ 50.000 no mês, sujeitando o valor a IRRF de 10% pela regra fornecida. Distribuições em outros meses ou lucros até 2025 com aprovação tempestiva podem mudar a retenção; não há fatos suficientes para quantificar essas alternativas. Uma eventual devolução de capital exigiria análise própria, para a qual a biblioteca não fornece regra tributária. [Dividendos a partir de 2026](../library/lei15270_dividendos_2026.md).

## Custo das quotas e resposta a Beatriz

**Não retificar para R$ 2 milhões por sócio.** O histórico mostra capital de R$ 200.000 na constituição, acrescido de R$ 600.000 por lucros capitalizados em 2018 e R$ 400.000 de aporte em 2021: R$ 1.200.000 no total, ou R$ 600.000 por pessoa, igual às DIRPFs. O valor de mercado maior da empresa não é um novo desembolso nem hipótese de atualização automática, integral ou parcial, do custo. A referência admite o custo da declaração de bens e não admite atualização fora de hipótese legal expressa. Ela menciona a opção da **Lei 14.973/2024**, com pagamento de 4%, mas afirma que seu prazo terminou. Não há comprovação de opção tempestiva, nem a biblioteca detalha sua aplicação a estas quotas; portanto, ela não fundamenta a retificação pedida agora. [Custo na venda a prazo](../library/lei7713_art21_parcelado.md).

Se o custo fosse alterado sem fato que o suporte, o ganho declarado cairia indevidamente de R$ 3.900.000 para R$ 2.500.000 por sócio e o GCAP de R$ 585.000 para R$ 375.000: redução artificial de **R$ 210.000 por sócio**, R$ 420.000 no total. A biblioteca enquadra a retificação artificial, feita para reduzir tributo mediante declaração falsa, como risco de crime contra a ordem tributária, além de revisão fiscal. Uma correção só seria defensável com fato e documentos que comprovem custo efetivamente omitido; nenhum foi informado. [Declaração falsa](../library/crime_ordem_tributaria.md).

## Alegação do comprador sobre ágio e negociação

O prêmio bruto de R$ 600.000 pela compra do estabelecimento não comprova um benefício fiscal específico ao comprador. A amortização fiscal de ágio por rentabilidade futura tratada na referência é ligada à **aquisição de participação societária** seguida de absorção patrimonial por incorporação, fusão ou cisão, com laudo independente e registro tempestivo; o prazo mínimo é de 60 meses. A compra de ativos não produz esse mesmo ágio societário nem a amortização acelerada alegada. Nela, ativos adquiridos são registrados a valor justo e intangíveis/imobilizado seguem suas vidas úteis. [Ágio na aquisição](../library/lei12973_agio.md).

Peçam ao comprador a alocação de preço e a avaliação que sustentam a oferta de R$ 9,6 milhões e qualquer benefício fiscal que alegue. Para igualar **R$ 7.830.000 nominais após tributos**, mantendo o valor contábil de R$ 2,1 milhões, a faixa trimestral integral e a hipótese de IRRF de 10% sobre todo o caixa distribuído como dividendos, o preço do estabelecimento teria de ser aproximadamente **R$ 12.090.909,09**: para preço `P`, ganho `P − 2.100.000`, tributos da PJ `34% × (P − 2.100.000) − 6.000` e líquido `90% × [P − tributos]`; resolver para R$ 7.830.000 dá esse valor. É apenas um parâmetro de negociação, sensível às premissas de distribuição e ao uso da faixa de IRPJ. A proposta de quotas oferece preço parcelado, com risco de crédito do comprador; seu valor presente pode ser inferior ao total nominal aqui mostrado. Garantias das três parcelas e regras de correção/antecipação devem ser negociadas antes de assinar.
