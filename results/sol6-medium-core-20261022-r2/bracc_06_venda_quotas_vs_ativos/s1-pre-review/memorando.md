# Venda da Vértice — comparação tributária

**Recomendação:** aceitar a estrutura de venda das quotas pela pessoa física como base da negociação. Com os preços ofertados e as premissas abaixo, os dois sócios receberiam R$ 7.830.000 líquidos, ante R$ 6.350.400 na venda do estabelecimento pela PJ: vantagem nominal de **R$ 1.479.600** para as quotas. A proposta da PJ paga à vista; a proposta das quotas paga 60% em três anos. Sem taxa de desconto e avaliação do risco de crédito do comprador, a diferença nominal não equivale a uma comparação de valor presente.

## Premissas do comparativo

- Cada sócio vende 50% das quotas e tem custo declarado de R$ 600.000. Não foram informados ajustes de preço, despesas de venda, correção das parcelas, outros resultados tributáveis da PJ no trimestre nem data de fechamento.
- Para preencher o campo de distribuição de 2026 do `comparativo.json`, foi simulada a **distribuição, no mesmo mês de 2026, de todo o caixa líquido da venda pela PJ como lucros/dividendos**, metade a cada sócio. É uma hipótese de cálculo, não uma conclusão de que todo o caixa pode juridicamente ser distribuído como dividendo. É preciso conferir balanço, lucros/reservas disponíveis, capital, passivos remanescentes e deliberações antes da operação. Os R$ 2.100.000 de valor contábil do estabelecimento não provam, por si, a natureza distribuível desse montante. Se parte sair por outra forma juridicamente válida, o IRRF e o líquido efetivos mudarão; a biblioteca não traz regras suficientes para calcular essa alternativa.
- O IRRF de 10% é **antecipação do IRPFM**, não necessariamente carga final. Não há na biblioteca parâmetros para quantificar eventual ajuste anual. A comparação é nominal e limitada aos tributos expressamente cobertos pela biblioteca; eventual tributação ou custo fora dela não foi quantificado.

## A. Venda de 100% das quotas por R$ 9.000.000

O preço de cada sócio é R$ 9.000.000 ÷ 2 = **R$ 4.500.000**. Seu ganho é R$ 4.500.000 − R$ 600.000 = **R$ 3.900.000**. Cada alienação fica inteira na faixa de 15% (até R$ 5 milhões por contribuinte e alienação): GCAP de R$ 3.900.000 × 15% = **R$ 585.000 por sócio**, ou **R$ 1.170.000** no total. Líquido conjunto: R$ 9.000.000 − R$ 1.170.000 = **R$ 7.830.000**. Não se somam os ganhos dos dois contribuintes para aplicar 17,5%. Fonte: [lei13259_gcap.md](../library/lei13259_gcap.md).

O ganho na venda a prazo é tributado proporcionalmente a cada recebimento. Sem atualização monetária informada, os DARFs **conjuntos dos dois sócios** seguem as proporções do preço; cada sócio recolhe metade dos valores abaixo. O vencimento de cada DARF é o último dia útil do mês seguinte ao respectivo recebimento; faltam as datas para indicar dias de calendário. Fontes: [lei7713_art21_parcelado.md](../library/lei7713_art21_parcelado.md) e [lei13259_gcap.md](../library/lei13259_gcap.md).

| Recebimento | Preço conjunto | GCAP/DARF conjunto | Líquido conjunto |
|---|---:|---:|---:|
| Fechamento, 40% | R$ 3.600.000 | R$ 468.000 | R$ 3.132.000 |
| Ano 1, 20% | R$ 1.800.000 | R$ 234.000 | R$ 1.566.000 |
| Ano 2, 20% | R$ 1.800.000 | R$ 234.000 | R$ 1.566.000 |
| Ano 3, 20% | R$ 1.800.000 | R$ 234.000 | R$ 1.566.000 |
| **Total** | **R$ 9.000.000** | **R$ 1.170.000** | **R$ 7.830.000** |

## B. Venda do estabelecimento pela PJ por R$ 9.600.000

Ganho contábil/fiscal considerado: R$ 9.600.000 − R$ 2.100.000 = **R$ 7.500.000**. No Lucro Presumido, esse ganho entra **integralmente** nas bases de IRPJ e CSLL; não se aplica o percentual de presunção de 32% dos serviços ao ganho. Para o adicional de IRPJ, pressupõe-se que a operação ocorra em um trimestre sem outros resultados que usem o limite de R$ 60.000. Fonte: [lei9430_art25_presumido_gcap.md](../library/lei9430_art25_presumido_gcap.md).

| Cálculo | Valor |
|---|---:|
| IRPJ básico: R$ 7.500.000 × 15% | R$ 1.125.000 |
| Adicional: (R$ 7.500.000 − R$ 60.000) × 10% | R$ 744.000 |
| **IRPJ** | **R$ 1.869.000** |
| CSLL: R$ 7.500.000 × 9% | R$ 675.000 |
| **Tributos da PJ sobre o ganho** | **R$ 2.544.000** |
| Caixa da venda após esses tributos: R$ 9.600.000 − R$ 2.544.000 | R$ 7.056.000 |
| IRRF hipotético: R$ 7.056.000 × 10% | R$ 705.600 |
| **Líquido conjunto simulado** | **R$ 6.350.400** |

Na hipótese de distribuição acima, cada sócio recebe R$ 3.528.000 brutos no mês, acima de R$ 50.000 por pessoa; o IRRF seria R$ 352.800 para cada um. A regra e a ressalva de que se trata de antecipação vêm de [lei15270_dividendos_2026.md](../library/lei15270_dividendos_2026.md). A diferença de R$ 1.479.600 em favor das quotas resulta de R$ 7.830.000 − R$ 6.350.400.

## Custo das quotas e pedido da Beatriz

**Não retificar para R$ 2 milhões por sócio apenas com base na valorização.** O histórico já explica os R$ 600.000 declarados por pessoa: R$ 100.000 da constituição (R$ 200.000 ÷ 2), mais R$ 300.000 da capitalização de lucros de 2018 (aumento de R$ 600.000 ÷ 2), mais R$ 200.000 do aporte de 2021 (aumento de R$ 400.000 ÷ 2). **Existe, sim, uma hipótese legal de atualização de bens:** a biblioteca menciona a opção da Lei 14.973/2024, condicionada a pagamento de 4%, mas informa que o prazo dessa opção está encerrado. Ela não autoriza escolher agora um aumento integral ou parcial do custo pela valorização. Se Beatriz alegar ter exercido tempestivamente a opção, será preciso verificar se as quotas eram elegíveis e documentar a opção, o pagamento e o valor atualizado antes de reavaliar o custo; a biblioteca não detalha a elegibilidade. Os documentos recebidos só mostram R$ 600.000 declarados e não comprovam tal exercício. Fora de hipótese legal efetivamente cumprida ou de custo histórico documentado, vale o custo declarado. Fonte: [lei7713_art21_parcelado.md](../library/lei7713_art21_parcelado.md).

Se fossem lançados R$ 2 milhões sem suporte, o ganho aparente cairia para R$ 2.500.000 por sócio, e o GCAP aparente para R$ 375.000: redução indevida de **R$ 210.000 por sócio** (R$ 420.000 no total). Uma retificação artificial configura declaração falsa segundo a biblioteca e expõe os sócios a autuação e risco penal. Fonte: [crime_ordem_tributaria.md](../library/crime_ordem_tributaria.md). Qualquer custo histórico adicional só deve ser considerado se houver fato e documentação que o sustentem; nenhum foi informado.

## Alegação de ágio e negociação

O preço maior da proposta B não demonstra benefício fiscal automático ao comprador. Na **compra do estabelecimento**, não surge o ágio societário amortizável em no mínimo 60 meses previsto para aquisição de participação seguida de incorporação, fusão ou cisão, sujeita a laudo independente e registro tempestivo. O comprador deve discriminar e sustentar a avaliação dos ativos e intangíveis adquiridos e seu tratamento segundo a vida útil; o goodwill de ativos tem tratamento próprio. Na **compra das quotas**, eventual dedução de ágio também dependeria dos requisitos citados, não bastando pagar acima do patrimônio líquido. Fonte: [lei12973_agio.md](../library/lei12973_agio.md).

Negociar (i) preço e garantias para as três parcelas da proposta A, (ii) eventual parcela maior no fechamento ou remuneração explícita do prazo e (iii) alocação documentada de preço, passivos e contratos na proposta B. Sob **as mesmas premissas fiscais da simulação**, para a proposta B igualar os R$ 7.830.000 líquidos nominais da A, o preço à vista teria de ser aproximadamente **R$ 12.090.909**: líquido da PJ = 90% × [P − 34% × (P − R$ 2.100.000) + R$ 6.000] = 0,594P + R$ 648.000; igualando a R$ 7.830.000, P = R$ 7.182.000 ÷ 0,594. O valor muda se a distribuição real tiver outra composição, se houver resultados adicionais no trimestre ou se for atribuído valor financeiro ao pagamento imediato.

**Pontos a fechar antes de assinar:** confirmar balanço e passivos da casca, capacidade e forma legal de entregar o caixa aos sócios, datas de fechamento e distribuição, resultados do trimestre, garantias das parcelas e documentação da avaliação do comprador. Não há, na biblioteca fechada, base para quantificar outros tributos da transferência de ativos/contratos ou o ajuste anual do IRPFM; esses efeitos permanecem não verificados nesta comparação.
