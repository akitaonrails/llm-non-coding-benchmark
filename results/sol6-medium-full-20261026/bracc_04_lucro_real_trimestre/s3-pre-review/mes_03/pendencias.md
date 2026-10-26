# Fechamento de março/2026 — conciliação e pendências

## Março

Receita de R$ 2.620.000,00 − PIS/COFINS sobre vendas de R$ 242.350,00 − ICMS de R$ 183.400,00 − CMV de R$ 1.441.000,00 − pessoal de R$ 210.000,00 − despesas comerciais de R$ 85.000,00 − administração de R$ 96.000,00 − depreciação de R$ 51.667,00 − juros de R$ 28.000,00 = **resultado de março antes da provisão trimestral de IRPJ/CSLL de R$ 282.583,00**. A provisão do trimestre, reconhecida em março, é de R$ 115.318,58 de IRPJ + R$ 43.674,69 de CSLL = R$ 158.993,27. Resultado de março após a provisão: **R$ 123.589,73**.

PIS/COFINS de março: R$ 2.620.000,00 × 9,25% = R$ 242.350,00; menos R$ 159.951,00 de crédito sobre mercadorias = **R$ 82.399,00 a recolher**. O trimestre soma R$ 79.883,00 (janeiro) + R$ 81.141,00 (fevereiro) + R$ 82.399,00 (março) = **R$ 243.423,00**. O crédito indevido da NF 8812 foi estornado em janeiro conforme [pis_cofins_uso_consumo.md](../../library/pis_cofins_uso_consumo.md).

## Balancete acumulado

O balancete bruto de março ainda contém os ajustes de janeiro e fevereiro não incorporados no razão fornecido. As transposições em `ajustes.json` representam aqueles mesmos ajustes, sem novo efeito econômico; aplicar cada lançamento somente uma vez.

- Balancete bruto: débitos = créditos = R$ 26.766.378,00. Estorno do crédito indevido de janeiro e compensações dos créditos válidos: R$ 11.100,00 + R$ 155.067,00 + R$ 157.509,00 + R$ 159.951,00 = R$ 483.627,00 de redução de saldos em cada lado. Reclassificação da doação de R$ 30.000,00 sem alteração do total. Provisões de IRPJ/CSLL de R$ 158.993,27 adicionam o mesmo valor a cada lado. Balancete ajustado: R$ 26.766.378,00 − R$ 483.627,00 + R$ 158.993,27 = **R$ 26.441.744,27 de débitos e créditos**.
- Tributos a recuperar (PIS/COFINS): R$ 483.627,00 − R$ 11.100,00 − R$ 155.067,00 − R$ 157.509,00 − R$ 159.951,00 = **R$ 0,00**.
- Fornecedores: R$ 3.753.627,00 − R$ 11.100,00 = **R$ 3.742.527,00**, sujeito à premissa da NF 8812.
- Tributos a recolher: R$ 1.997.750,00 − R$ 155.067,00 − R$ 157.509,00 − R$ 159.951,00 + R$ 158.993,27 = **R$ 1.684.216,27**. Composição: abertura R$ 740.000,00 + ICMS trimestral R$ 541.800,00 + PIS/COFINS trimestral R$ 243.423,00 + IRPJ/CSLL R$ 158.993,27 = R$ 1.684.216,27. O razão não apresenta pagamentos de tributos.
- Resultado contábil trimestral antes das provisões de IRPJ/CSLL: R$ 139.583,00 + R$ 193.083,00 + R$ 282.583,00 = **R$ 615.249,00**. Após as provisões: R$ 615.249,00 − R$ 158.993,27 = **R$ 456.255,73**.

## Itens em aberto

O cliente não confirmou o valor total devido na NF 8812. Mantida a premissa explícita dos fechamentos anteriores de R$ 120.000,00, igual ao item mostrado no documento. Se o valor devido for R$ 131.100,00, substituir o débito em Fornecedores de R$ 11.100,00 por despesa de uso e consumo e recalcular lucro, compensação e IRPJ/CSLL; a sensibilidade está em `memoria.md`. Falta também confirmar transmissão da EFD-Contribuições de janeiro e pagamento com o crédito indevido para executar a retificação e quantificar acréscimos.

A biblioteca não contém fundamento específico para a indedutibilidade das provisões de IRPJ e CSLL. A reversão dessas provisões na Parte A foi usada como conciliação técnica entre o lucro após provisão e o resultado antes delas; o enquadramento fiscal específico está **não verificado** na biblioteca e deve ser revisado antes da entrega da ECF.
