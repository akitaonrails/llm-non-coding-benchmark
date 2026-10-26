# Fechamento de janeiro de 2026 — Atlas Distribuidora S.A.

## Apuração de PIS/COFINS

- Débito sobre vendas: R$ 2.540.000,00 × 9,25% = **R$ 234.950,00**, conforme razão e balancete.
- Crédito contabilizado em compras de mercadorias: R$ 1.676.400,00 × 9,25% = **R$ 155.067,00**.
- Crédito contabilizado na NF 8812: R$ 120.000,00 × 9,25% = **R$ 11.100,00**. A NF descreve papel, toners e materiais para áreas administrativas, com CFOP 1556 (uso ou consumo). Esse crédito é indevido e deve ser estornado, com retificação da EFD-Contribuições de janeiro. Fundamento: [PIS/COFINS não cumulativos — uso e consumo não gera crédito](../../library/pis_cofins_uso_consumo.md), citado em `library/INDEX.md`.
- Crédito originalmente registrado: R$ 155.067,00 + R$ 11.100,00 = **R$ 166.167,00**. Crédito após estorno: R$ 166.167,00 − R$ 11.100,00 = **R$ 155.067,00**. Valor a recolher: R$ 234.950,00 − R$ 155.067,00 = **R$ 79.883,00**. O valor anterior ao estorno seria R$ 68.783,00; a diferença é R$ 11.100,00.

## Resultado contábil e conciliação

O balancete e o razão de janeiro conciliam antes do ajuste: débitos = créditos = **R$ 19.880.584,00** no balancete. O lucro contábil antes do ajuste é R$ 2.540.000,00 − R$ 234.950,00 − R$ 177.800,00 − R$ 1.397.000,00 − R$ 210.000,00 − R$ 85.000,00 − R$ 96.000,00 − R$ 120.000,00 − R$ 51.667,00 − R$ 28.000,00 = **R$ 139.583,00**. Sob o lançamento provisório em `ajustes.json`, a despesa aumenta R$ 11.100,00 e o lucro passa a **R$ 128.483,00**. A compensação de prejuízos fiscais e a apuração de IRPJ/CSLL cabem ao encerramento trimestral, conforme [IRPJ/CSLL — Lucro Real trimestral](../../library/irpj_csll_trimestral.md), citado em `library/INDEX.md`.

## Pendência documental e efeito no ajuste

**Premissa provisória:** o lançamento proposto em `ajustes.json` considera válida a obrigação de **R$ 131.100,00** em Fornecedores registrada para a NF 8812; assim, a contrapartida do estorno fiscal é despesa de material de uso e consumo. O cliente informou não possuir esclarecimento adicional. A NF recebida apresenta um item de **R$ 120.000,00**, mas não informa expressamente o valor total da nota nem se os tributos destacados já estão incluídos nesse item. Portanto, o valor devido ao fornecedor permanece **sem conciliação documental**.

Se o total efetivamente devido for **R$ 120.000,00**, a contrapartida correta do crédito em Tributos a recuperar será débito em **Fornecedores (2.1.01)** de R$ 11.100,00, em lugar de débito em despesa. Nesse cenário, o lucro contábil de janeiro permanece R$ 139.583,00. O estorno fiscal de R$ 11.100,00 e o PIS/COFINS a recolher de R$ 79.883,00 não mudam. Solicitar a NF completa ou confirmação do contas a pagar antes de tornar definitivo o lançamento contábil.

Não foram fornecidos comprovantes de transmissão da EFD-Contribuições nem de pagamento. A necessidade de retificação está identificada; data, acréscimos e eventual diferença efetivamente devida após pagamentos dependem desses dados.
