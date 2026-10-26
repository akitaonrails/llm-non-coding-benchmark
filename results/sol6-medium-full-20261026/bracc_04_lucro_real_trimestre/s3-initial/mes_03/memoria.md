# Memória de cálculo — IRPJ/CSLL do 1º trimestre de 2026

**Regime:** Lucro Real trimestral. Apuração preparada com os balancetes e razões recebidos e com a premissa contábil de que o valor devido na NF 8812 é R$ 120.000,00. Essa premissa ainda depende de confirmação; veja a sensibilidade ao final.

## Resultado contábil e Parte A do e-LALUR/e-LACS

| Etapa | Cálculo | R$ |
|---|---:|---:|
| Resultado de janeiro antes de IRPJ/CSLL | Conforme fechamento de janeiro | 139.583,00 |
| Resultado de fevereiro antes de IRPJ/CSLL | Conforme fechamento de fevereiro | 193.083,00 |
| Resultado de março antes de IRPJ/CSLL | Conforme razão de março | 282.583,00 |
| Resultado trimestral antes de IRPJ/CSLL | 139.583,00 + 193.083,00 + 282.583,00 | **615.249,00** |
| Provisão de IRPJ | 72.791,15 + 42.527,43 | (115.318,58) |
| Provisão de CSLL | 9% × 485.274,30, arredondado | (43.674,69) |
| Lucro líquido contábil após provisões | 615.249,00 − 158.993,27 | **456.255,73** |
| Adição: reversão das provisões de IRPJ/CSLL | 115.318,58 + 43.674,69 | 158.993,27 |
| Adição: brindes | NF 4410, 400 kits para clientes | 48.000,00 |
| Adição: doação | Associação Beneficente Luz | 30.000,00 |
| Exclusões | Nenhuma identificada | 0,00 |
| Lucro/base antes de compensações | 456.255,73 + 158.993,27 + 48.000,00 + 30.000,00 | **693.249,00** |
| Compensação de prejuízo fiscal | Mínimo entre 900.000,00 e 30% × 693.249,00 | (207.974,70) |
| Lucro real | 693.249,00 − 207.974,70 | **485.274,30** |
| Compensação de base negativa da CSLL | Mínimo entre 900.000,00 e 30% × 693.249,00 | (207.974,70) |
| Base da CSLL | 693.249,00 − 207.974,70 | **485.274,30** |

Os brindes são indedutíveis no IRPJ e na CSLL pelo art. 13, VII, de [lei9249_art13.md](../../library/lei9249_art13.md), mesmo classificados contabilmente como despesa comercial. A doação não se enquadra na exceção documentada do art. 13, § 2º, II: o recibo informa ausência de OSCIP e de reconhecimento de utilidade pública federal, e não há indicação de outra exceção. Por isso, adicionam-se os R$ 30.000,00 conforme art. 13, VI e § 2º, de [lei9249_art13.md](../../library/lei9249_art13.md). A Parte A registra essas adições sem estornar as despesas na contabilidade, conforme [irpj_csll_trimestral.md](../../library/irpj_csll_trimestral.md).

A provisão trimestral foi lançada em março. Sua reversão de R$ 158.993,27 na Parte A reconcilia o lucro contábil **após** a provisão (R$ 456.255,73) com o resultado **antes** dela (R$ 615.249,00), utilizado para calcular os próprios tributos. A biblioteca não traz fundamento específico sobre a indedutibilidade fiscal das provisões de IRPJ/CSLL; esse enquadramento legal está **não verificado** e requer revisão antes da ECF. A base e os tributos calculados não dependem de arredondamento intermediário oculto.

## IRPJ e CSLL

O limite de 30% vale tanto para o prejuízo fiscal como para a base negativa de CSLL, conforme [lei9065_art15_trava.md](../../library/lei9065_art15_trava.md). Assim, o pedido de compensar os R$ 900.000,00 integralmente não cabe neste trimestre.

| Tributo | Cálculo | R$ |
|---|---:|---:|
| IRPJ 15% | 485.274,30 × 15% = 72.791,145; arredondado a centavos | **72.791,15** |
| Adicional de IRPJ 10% | (485.274,30 − 60.000,00) × 10% | **42.527,43** |
| IRPJ total | 72.791,15 + 42.527,43 | **115.318,58** |
| CSLL 9% | 485.274,30 × 9% = 43.674,687; arredondado a centavos | **43.674,69** |
| IRPJ + CSLL | 115.318,58 + 43.674,69 | **158.993,27** |

Alíquotas e limite trimestral do adicional: [irpj_csll_trimestral.md](../../library/irpj_csll_trimestral.md). Valores monetários arredondados a centavos pelo critério comercial.

## Parte B — controle para períodos seguintes

| Controle | Saldo inicial | Utilizado no trimestre | Saldo final |
|---|---:|---:|---:|
| Prejuízo fiscal | R$ 900.000,00 | R$ 207.974,70 | **R$ 692.025,30** |
| Base negativa da CSLL | R$ 900.000,00 | R$ 207.974,70 | **R$ 692.025,30** |

Cada saldo final é R$ 900.000,00 − R$ 207.974,70. A origem dos saldos iniciais está no demonstrativo fiscal de abertura recebido; o controle dos saldos na Parte B consta de [irpj_csll_trimestral.md](../../library/irpj_csll_trimestral.md).

## Sensibilidade da NF 8812 e itens em aberto

O documento disponível informa R$ 120.000,00 de itens, mas o razão lançou R$ 131.100,00 em Fornecedores. O cliente confirmou uso administrativo, suficiente para estornar o crédito de PIS/COFINS, mas não confirmou o valor total devido. **Se** forem devidos R$ 131.100,00 e os R$ 11.100,00 adicionais forem despesa dedutível de uso e consumo, o lucro antes da provisão cai a R$ 604.149,00; a base antes de compensações passa a R$ 682.149,00; 30% = R$ 204.644,70; base após compensações = R$ 477.504,30. Nesse cenário, IRPJ de 15% = R$ 71.625,65; adicional = R$ 41.750,43; CSLL = R$ 42.975,39; tributos totais = R$ 156.351,47; Parte B final = R$ 695.355,30 para cada saldo. **A dedutibilidade dessa despesa adicional não é tratada expressamente na biblioteca e essa sensibilidade, portanto, não está verificada como apuração alternativa definitiva.**

Também não há informação sobre transmissão da EFD-Contribuições de janeiro ou pagamento com o crédito indevido; eventual diferença de PIS/COFINS e acréscimos dependem dessa confirmação, conforme [pis_cofins_uso_consumo.md](../../library/pis_cofins_uso_consumo.md).
