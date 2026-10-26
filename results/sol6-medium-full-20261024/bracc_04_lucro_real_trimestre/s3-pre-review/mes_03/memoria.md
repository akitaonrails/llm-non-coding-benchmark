# Memória de cálculo — IRPJ/CSLL e e-LALUR, 1º trimestre de 2026

## Premissa e lucro contábil

O lucro contábil acumulado no balancete, **antes** da regularização da NF 8812 de janeiro, é R$ 7.740.000,00 de receita − R$ 715.950,00 de PIS/COFINS − R$ 541.800,00 de ICMS − R$ 4.257.000,00 de CMV − R$ 630.000,00 de pessoal − R$ 333.000,00 de despesas comerciais − R$ 288.000,00 de despesas administrativas − R$ 120.000,00 de material de uso e consumo − R$ 155.001,00 de depreciação − R$ 84.000,00 de despesas financeiras = **R$ 615.249,00**. Confere com R$ 139.583,00 (jan.) + R$ 193.083,00 (fev.) + R$ 282.583,00 (mar.).

**Premissa provisória usada na apuração principal:** o passivo registrado para a NF 8812, R$ 131.100,00, está correto. O estorno do crédito indevido de PIS/COFINS de R$ 11.100,00 debita a despesa de material de uso e consumo, conforme `mes_01/ajustes.json`. Assim, lucro contábil ajustado = R$ 615.249,00 − R$ 11.100,00 = **R$ 604.149,00**. A biblioteca [PIS/COFINS não cumulativos — uso e consumo](../../library/pis_cofins_uso_consumo.md) fundamenta o estorno do crédito, mas **não contém regra específica de dedutibilidade desse material para IRPJ/CSLL**. A apuração principal presume que a despesa contabilizada não exige adição fiscal por outro motivo; essa presunção permanece não verificada na biblioteca.

## Parte A — demonstração do lucro real e da base de CSLL

| Etapa | IRPJ (R$) | CSLL (R$) | Fundamento / cálculo |
|---|---:|---:|---|
| Lucro contábil ajustado | 604.149,00 | 604.149,00 | Balancete menos ajuste provisório da NF 8812. |
| Adição: brindes a clientes | 48.000,00 | 48.000,00 | NF 4410; [Lei 9.249/95, art. 13, VII](../../library/lei9249_art13.md). |
| Adição: doação | 30.000,00 | 30.000,00 | Associação sem OSCIP ou utilidade pública federal; [Lei 9.249/95, art. 13, VI e § 2º](../../library/lei9249_art13.md). |
| Exclusões | 0,00 | 0,00 | Nenhuma identificada nos documentos. |
| Lucro/base antes da compensação | **682.149,00** | **682.149,00** | 604.149,00 + 48.000,00 + 30.000,00. |
| Compensação de saldos anteriores | (204.644,70) | (204.644,70) | Menor entre R$ 900.000,00 disponíveis e 30% × R$ 682.149,00; [Lei 9.065/95, arts. 15 e 16](../../library/lei9065_art15_trava.md). |
| Lucro real/base de CSLL | **477.504,30** | **477.504,30** | 682.149,00 − 204.644,70. |

Os R$ 48.000,00 de brindes e os R$ 30.000,00 de doação permanecem contabilizados como despesa; a adição é exclusivamente fiscal, conforme [IRPJ/CSLL — Lucro Real trimestral](../../library/irpj_csll_trimestral.md). A intenção de usar todos os R$ 900.000,00 não supera a trava de 30%, que também se aplica à base negativa de CSLL, conforme [Lei 9.065/95, arts. 15 e 16](../../library/lei9065_art15_trava.md).

## Tributos do trimestre

IRPJ à alíquota básica: R$ 477.504,30 × 15% = R$ 71.625,645 → **R$ 71.625,65**. Adicional: (R$ 477.504,30 − R$ 60.000,00) × 10% = **R$ 41.750,43**. IRPJ total: **R$ 113.376,08**. CSLL: R$ 477.504,30 × 9% = R$ 42.975,387 → **R$ 42.975,39**. IRPJ + CSLL: **R$ 156.351,47**. O limite de R$ 60.000,00 para o adicional, as alíquotas e a apuração trimestral constam de [IRPJ/CSLL — Lucro Real trimestral](../../library/irpj_csll_trimestral.md). Valores em centavos arredondados ao final de cada tributo.

## Parte B — controle dos saldos fiscais

| Saldo | Abertura (R$) | Utilização no trimestre (R$) | Final (R$) |
|---|---:|---:|---:|
| Prejuízo fiscal de IRPJ | 900.000,00 | 204.644,70 | **695.355,30** |
| Base negativa de CSLL | 900.000,00 | 204.644,70 | **695.355,30** |

Os saldos iniciais provêm dos saldos fiscais de abertura fornecidos. A Parte B controla o saldo não utilizado, conforme [IRPJ/CSLL — Lucro Real trimestral](../../library/irpj_csll_trimestral.md).

## Sensibilidade à pendência da NF 8812

Se o total efetivamente devido ao fornecedor for **R$ 120.000,00**, o crédito indevido de R$ 11.100,00 deve ser estornado contra **Fornecedores**, sem elevar a despesa. Nesse caso, o lucro contábil do trimestre fica em **R$ 615.249,00**; lucro antes da compensação = R$ 615.249,00 + R$ 78.000,00 = **R$ 693.249,00**; limite de 30% = **R$ 207.974,70**; lucro real e base de CSLL = **R$ 485.274,30**. IRPJ de 15% = **R$ 72.791,15**; adicional de 10% = **R$ 42.527,43**; IRPJ total = **R$ 115.318,58**; CSLL de 9% = **R$ 43.674,69**; total = **R$ 158.993,27**. Na Parte B restariam **R$ 692.025,30** de prejuízo fiscal e **R$ 692.025,30** de base negativa de CSLL. A diferença de tributos entre os cenários é **R$ 2.641,80**. A NF completa ou a confirmação do contas a pagar é necessária para tornar definitiva a apuração.
