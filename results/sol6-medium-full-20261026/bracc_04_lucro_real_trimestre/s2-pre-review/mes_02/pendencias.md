# Fechamento de fevereiro/2026 — conciliação e pendências

## Resultado e tributos do mês

Receita de R$ 2.580.000,00 − PIS/COFINS sobre vendas de R$ 238.650,00 − ICMS de R$ 180.600,00 − CMV de R$ 1.419.000,00 − pessoal de R$ 210.000,00 − despesas comerciais de R$ 163.000,00 − administração de R$ 96.000,00 − depreciação de R$ 51.667,00 − juros de R$ 28.000,00 = **lucro contábil de fevereiro de R$ 193.083,00**. As despesas comerciais de R$ 163.000,00 são R$ 85.000,00 ordinárias + R$ 48.000,00 de brindes + R$ 30.000,00 de doação antes da reclassificação. Após ela, despesas comerciais ficam em R$ 133.000,00 e doações em R$ 30.000,00; o lucro não muda.

PIS/COFINS de fevereiro: R$ 2.580.000,00 × 9,25% = R$ 238.650,00; menos créditos sobre mercadorias de R$ 157.509,00 = **R$ 81.141,00 a recolher**. Não há crédito nem estorno novo relativo aos brindes ou à doação no razão de fevereiro. O tratamento do crédito da NF 8812 de janeiro continua fundamentado em [pis_cofins_uso_consumo.md](../../library/pis_cofins_uso_consumo.md).

## Itens para a apuração fiscal do trimestre

- Os 400 kits para clientes da NF 4410 custaram **R$ 48.000,00** e são brindes. A classificação contábil como despesa comercial pode permanecer; registrar **adição fiscal de R$ 48.000,00** na Parte A do e-LALUR/e-LACS do trimestre. Fundamento: [lei9249_art13.md](../../library/lei9249_art13.md), art. 13, VII; tratamento de adições na [irpj_csll_trimestral.md](../../library/irpj_csll_trimestral.md).
- A doação à Associação Beneficente Luz foi de **R$ 30.000,00**. O recibo informa que a entidade não possui título de OSCIP nem reconhecimento de utilidade pública federal. O documento não indica enquadramento nas demais exceções do art. 13, § 2º. Registrar **adição fiscal de R$ 30.000,00** no trimestre para IRPJ e CSLL, conforme [lei9249_art13.md](../../library/lei9249_art13.md), art. 13, VI e § 2º. O ajuste contábil apenas separa a despesa em conta própria.
- Adições fiscais identificadas em fevereiro: R$ 48.000,00 + R$ 30.000,00 = **R$ 78.000,00**. Não se reconhece despesa adicional por essas adições na contabilidade societária; a apuração do IRPJ/CSLL será trimestral, conforme [irpj_csll_trimestral.md](../../library/irpj_csll_trimestral.md).

## Conciliação do balancete acumulado

O balancete bruto de fevereiro contém os saldos de janeiro **sem** os ajustes do fechamento anterior: tributos a recuperar de R$ 323.676,00 = R$ 166.167,00 de janeiro + R$ 157.509,00 de fevereiro; tributos a recolher de R$ 1.572.000,00 = R$ 1.152.750,00 de janeiro + R$ 419.250,00 de fevereiro. Por isso `ajustes.json` traz, identificados como transposição, os dois ajustes de janeiro e os lançamentos de fevereiro. Aplicá-los somente uma vez.

- Balancete bruto: débitos = créditos = R$ 23.299.010,00. Os ajustes que reduzem saldos existentes somam R$ 11.100,00 + R$ 155.067,00 + R$ 157.509,00 = R$ 323.676,00 em cada lado. A reclassificação da doação de R$ 30.000,00 muda apenas contas devedoras. Balancete ajustado: débitos = créditos = **R$ 22.975.334,00**.
- Tributos a recuperar (PIS/COFINS): R$ 323.676,00 − R$ 11.100,00 − R$ 155.067,00 − R$ 157.509,00 = **R$ 0,00**.
- Fornecedores: R$ 3.593.676,00 − R$ 11.100,00 = **R$ 3.582.576,00**, sujeito à premissa da NF 8812.
- Tributos a recolher: R$ 1.572.000,00 − R$ 155.067,00 − R$ 157.509,00 = **R$ 1.259.424,00**. Composição: abertura R$ 740.000,00 + ICMS acumulado R$ 358.400,00 + PIS/COFINS janeiro R$ 79.883,00 + fevereiro R$ 81.141,00 = R$ 1.259.424,00. O razão não apresenta pagamentos de tributos.
- Lucro contábil acumulado: R$ 139.583,00 de janeiro + R$ 193.083,00 de fevereiro = **R$ 332.666,00**, sob a premissa usada no fechamento de janeiro.

## Itens em aberto

Permanece desconhecido o valor total devido na NF 8812: o documento recebido mostra item de R$ 120.000,00, enquanto o razão lançou R$ 131.100,00 a pagar. Mantida a premissa de R$ 120.000,00 do fechamento de janeiro. Se confirmado total de R$ 131.100,00, substituir o débito de R$ 11.100,00 em Fornecedores por débito em despesa de uso e consumo; o lucro acumulado até fevereiro passará de R$ 332.666,00 a R$ 321.566,00. Também falta confirmar transmissão da EFD-Contribuições de janeiro e eventual recolhimento com o crédito indevido, para executar a retificação e quantificar acréscimos. Fundamento do estorno: [pis_cofins_uso_consumo.md](../../library/pis_cofins_uso_consumo.md).
