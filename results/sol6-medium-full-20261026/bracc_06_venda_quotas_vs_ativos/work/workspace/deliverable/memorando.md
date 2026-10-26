# Vértice — comparação das propostas

**Recomendação:** negociar a venda das quotas pela pessoa física. Os sócios recebem **R$ 7.830.000 nominais após GCAP** na proposta de R$ 9 milhões. Na alternativa PJ, restam **R$ 7.056.000 de caixa após IRPJ e CSLL**, ainda dentro da sociedade; mesmo antes de tributar ou custear sua retirada, são R$ 774.000 a menos. O JSON traz uma **simulação ilustrativa** de R$ 6.350.400 aos sócios se todo esse caixa estivesse sujeito a IRRF de 10%; essa hipótese não foi reconciliada com a composição do patrimônio da PJ e não deve ser tomada como distribuição executável. A proposta das quotas é parcelada, e a preferência econômica depende também do risco e valor presente dos pagamentos. Não retificar a DIRPF para elevar artificialmente o custo das quotas.

## Premissas do cálculo

- Dois sócios com 50% cada, sem despesas de alienação informadas; custo declarado de R$ 600.000 por sócio. Não há atualização contratual das parcelas informada.
- Fechamento da alternativa PJ em 2026. Para preencher os campos numéricos do JSON, simula-se uma distribuição em um mesmo mês a dois sócios em partes iguais, aplicando 10% sobre todo o caixa após IRPJ e CSLL. **Essa incidência integral não está comprovada**: parte do caixa corresponde ao valor contábil transferido, cuja extração não foi documentada. Assim, `irrf_distribuicao_2026` e `liquido_socios` da PJ são apenas uma sensibilidade matemática, não valores fiscais apurados.
- Ganho da PJ calculado sobre o valor contábil líquido do estabelecimento informado, R$ 2.100.000. Para o adicional de IRPJ, considera-se um trimestre completo e base adicional zero antes da venda. Receitas, despesas e bases preexistentes do trimestre não foram fornecidas.
- Os valores líquidos não incluem outros tributos, custos de transação, ajustes contratuais, eventual IRPFM final, nem remuneração financeira das parcelas. A biblioteca não permite quantificá-los.

## Proposta A — quotas, R$ 9.000.000

Cada sócio vende por **R$ 4.500.000** e apura ganho de **R$ 4.500.000 − R$ 600.000 = R$ 3.900.000**. O ganho de cada alienante fica integralmente na faixa de 15%: **GCAP de R$ 585.000 por sócio**, ou **R$ 1.170.000** no total. Líquido conjunto: **R$ 9.000.000 − R$ 1.170.000 = R$ 7.830.000** (R$ 3.915.000 por sócio). A progressividade incide por contribuinte e alienação, não sobre R$ 9 milhões como se houvesse um único vendedor. [Ganho de capital da PF](../library/lei13259_gcap.md).

Na venda a prazo, o imposto acompanha a proporção de cada recebimento. O `cronograma_darf` do JSON mostra **o total dos dois sócios**, na ordem das quatro parcelas; cada sócio recolhe metade:

| Recebimento | Parcela conjunta | GCAP conjunto | GCAP por sócio |
|---|---:|---:|---:|
| Fechamento, 40% | R$ 3.600.000 | R$ 468.000 | R$ 234.000 |
| Ano 1, 20% | R$ 1.800.000 | R$ 234.000 | R$ 117.000 |
| Ano 2, 20% | R$ 1.800.000 | R$ 234.000 | R$ 117.000 |
| Ano 3, 20% | R$ 1.800.000 | R$ 234.000 | R$ 117.000 |

Em cada recebimento, recolher o DARF até o último dia útil do mês seguinte. Se houver atualização monetária das parcelas, a apuração deverá considerá-la; ela não foi quantificada. [Venda a prazo](../library/lei7713_art21_parcelado.md); [prazo do GCAP](../library/lei13259_gcap.md).

## Proposta B — estabelecimento, R$ 9.600.000

O ganho contábil/fiscal informado é **R$ 9.600.000 − R$ 2.100.000 = R$ 7.500.000**. O percentual de presunção de 32% para serviços **não** se aplica a esse ganho: ele é acrescido integralmente à base. IRPJ: **15% × R$ 7.500.000 = R$ 1.125.000**, mais adicional de **10% × (R$ 7.500.000 − R$ 60.000) = R$ 744.000**, total **R$ 1.869.000**. CSLL: **9% × R$ 7.500.000 = R$ 675.000**. Tributos da PJ: **R$ 2.544.000**. Caixa após esses tributos: **R$ 9.600.000 − R$ 2.544.000 = R$ 7.056.000**. [Ganho no Lucro Presumido](../library/lei9430_art25_presumido_gcap.md).

O caixa de R$ 7.056.000 se reconcilia como **R$ 4.956.000 de ganho após IRPJ/CSLL** (R$ 7.500.000 − R$ 2.544.000) **mais R$ 2.100.000 de valor contábil transferido**. Se somente os R$ 4.956.000 forem lucros de 2026 distribuídos em um mês, seriam R$ 2.478.000 por sócio e o IRRF calculado sobre essa parcela seria **R$ 495.600**; os outros R$ 2.100.000 continuariam na PJ até que sua natureza e forma de retirada fossem definidas. A biblioteca não permite determinar o tributo dessa retirada. [Dividendos a partir de 2026](../library/lei15270_dividendos_2026.md).

O JSON, por exigência de um único valor numérico, mostra a **sensibilidade de retenção integral**: R$ 3.528.000 por sócio em um mês de 2026, acima do limite mensal de R$ 50.000; **10% × R$ 7.056.000 = R$ 705.600** (R$ 352.800 por sócio), com resultado aritmético de **R$ 6.350.400**. Esse IRRF excede em R$ 210.000 o cálculo sobre o ganho após tributos, porque inclui os R$ 2.100.000 sem qualificação como dividendos. Portanto, **não é uma estimativa de IRRF devido** nem uma afirmação de que a distribuição integral seja legalmente disponível. Qualquer IRRF efetivo sobre dividendos é antecipação do IRPFM; seu ajuste final não é calculável com os dados recebidos. [Dividendos a partir de 2026](../library/lei15270_dividendos_2026.md).

**Ponto aberto na distribuição:** a sociedade tem capital de R$ 1.200.000 e não recebemos demonstrações que identifiquem reservas, lucros antigos, passivos remanescentes ou o tratamento de eventual redução de capital/liquidação. A retenção efetiva depende da origem contábil e do calendário de cada pagamento. A biblioteca prevê isenção condicionada para lucros apurados até 2025 com distribuição aprovada até 31/12/2025; não há prova de que parte do caixa satisfaça essa condição. [Dividendos a partir de 2026](../library/lei15270_dividendos_2026.md). Antes de executar a alternativa PJ, reconciliar balanço, deliberações e plano de distribuição; a tributação de devolução de capital não está documentada na biblioteca e permanece **não verificada**.

## Custo das quotas e alegação de ágio

**Beatriz:** o valor econômico da empresa não altera sozinho o custo de aquisição das quotas. O histórico recebido já leva o capital a R$ 1.200.000, com R$ 600.000 por sócio declarados, incluindo o aumento com lucros capitalizados e o aporte. Assim, os R$ 2 milhões propostos por sócio não têm fato de aquisição ou capitalização que os sustente. A atualização do custo na DIRPF depende de hipótese legal expressa; a opção de atualização citada na biblioteca tinha prazo encerrado. Não apresentar retificação artificial: além de cobrança/revisão fiscal, a declaração falsa para reduzir tributo é tratada pela biblioteca como crime contra a ordem tributária. [Custo na venda a prazo](../library/lei7713_art21_parcelado.md); [declaração falsa](../library/crime_ordem_tributaria.md).

**Sobre a lei de atualização de bens:** a biblioteca menciona expressamente a opção da **Lei 14.973/2024**, sujeita ao pagamento de **4%**, e informa que **o prazo para optar está encerrado**. Ela não autoriza exercer a opção agora por meio de uma retificação, nem atualizar apenas uma parte da valorização econômica fora de uma hipótese legal. Se surgisse prova de custo histórico real omitido, seria preciso examinar a declaração correspondente; os fatos recebidos não mostram tal omissão, pois os R$ 600.000 de cada sócio já coincidem com sua parcela do capital após os aumentos. A biblioteca não detalha outras condições da Lei 14.973/2024 nem regras de retificação por erro histórico, que permanecem **não verificadas**. [Custo e atualização](../library/lei7713_art21_parcelado.md).

O comprador afirma pagar R$ 600.000 a mais pelo estabelecimento porque aproveitaria “ágio”. Na **compra de ativos**, não existe ágio societário com a amortização fiscal em 60 meses prevista para aquisição de participação seguida de incorporação, fusão ou cisão. Os ativos e intangíveis adquiridos têm tratamento próprio conforme sua natureza e vida útil. Na compra de quotas, a dedutibilidade de goodwill exige, entre outros requisitos, absorção patrimonial e laudo independente tempestivo; a mera compra de quotas também não assegura o benefício. Portanto, pedir ao comprador memória do preço e da estrutura tributária, sem aceitar a alegação de ágio como benefício automático. [Ágio na aquisição](../library/lei12973_agio.md).

## Negociação e execução

O acréscimo de R$ 600.000 no preço da proposta B não compensa a diferença nominal de IRPJ/CSLL e GCAP, mesmo sem custo de distribuição. A proposta A entrega **R$ 3.600.000 no fechamento** antes do GCAP de R$ 468.000, ou **R$ 3.132.000 líquidos após esse DARF**, e depois **R$ 1.566.000 líquidos** em cada um dos três anos. Se essas parcelas ocorrerem exatamente em 1, 2 e 3 anos, sem correção ou inadimplência, a taxa anual de desconto que iguala o valor presente de A aos **R$ 7.056.000 de caixa da PJ antes da retirada** é **aproximadamente 9,57%**: R$ 3.132.000 + R$ 1.566.000/(1+r) + R$ 1.566.000/(1+r)² + R$ 1.566.000/(1+r)³ = R$ 7.056.000. Essa é apenas uma referência, pois o caixa da PJ ainda não pertence aos sócios e sua retirada pode ter ônus. Negociar garantias das parcelas, correção, vencimento antecipado em inadimplência e alocação dos riscos de contingências. Para uma comparação econômica final, trazer datas exatas, taxa de desconto e termos de garantia. Se a proposta B continuar, validar o balanço e a forma de extrair o caixa antes de fixar o preço líquido aos sócios.
