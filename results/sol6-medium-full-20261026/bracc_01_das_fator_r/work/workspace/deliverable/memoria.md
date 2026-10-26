# Memória de cálculo — DAS de maio/2026

## Base de 12 meses e Fator R

O período anterior é maio/2025 a abril/2026. O faturamento informado soma **R$ 1.020.000,00**: 78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000. A folha soma **R$ 284.600,00**: salários 193.000 + pró-labore 35.200 + encargos/FGTS 56.400. Os totais de folha mensais conferem com essas parcelas.

O cliente confirmou que o pró-labore de abril, R$ 3.200,00, foi **pago em 30/04/2026**, embora o PIX tenha sido registrado no sistema em maio. Assim, o valor informado na linha de abril integra os 12 meses anteriores. O comprovante prometido ainda não consta dos arquivos; a data usada depende da confirmação do cliente. A regra considera valores **pagos**, independentemente da competência. Fonte normativa: [lc123_art18_fator_r.md](../library/lc123_art18_fator_r.md), Resolução CGSN 140/2018, art. 26, §§1º-2º.

**Fator R = 284.600 / 1.020.000 = 0,279019607843 = 27,9019607843%.** Como é inferior a 28%, os serviços de TI ficam no **Anexo V**. A alíquota aplicável é a **efetiva**, calculada com RBT12 e parcela a deduzir, e não simplesmente a nominal da faixa. Fonte: [lc123_art18_fator_r.md](../library/lc123_art18_fator_r.md), LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K e 5º-M.

O limite de 28% corresponde a **R$ 285.600,00** de folha (1.020.000 × 28%): a folha informada está **R$ 1.000,00 abaixo**. A linha `2026-03` do resumo registra pró-labore zero, mas sua observação diz “pró-labore de abril: em aberto na data do resumo”, referência a outro mês. Isso não prova pagamento omitido em março; mantive o zero informado. Se houver ao menos R$ 1.000,00 de pagamentos elegíveis omitidos na janela de 12 meses, o enquadramento dos serviços mudará para o Anexo III. A completude da folha permanece uma limitação material.

## Receitas de maio

| Documento | Classificação | Receita considerada |
|---|---|---:|
| NFS-e 1181 — desenvolvimento de software | Serviço de TI, Anexo V | R$ 18.000,00 |
| NFS-e 1182 — sustentação mensal | Serviço de TI, Anexo V | R$ 12.500,00 |
| NFS-e 1183 — consultoria de arquitetura | **Arquitetura de TI assumida**, Anexo V; a descrição não explicita a especialidade | R$ 9.800,00 |
| NFS-e 1184 — desenvolvimento do módulo fiscal | Serviço de TI, Anexo V | R$ 22.000,00 |
| NFS-e 1185 — suporte técnico | Serviço de TI, Anexo V | R$ 6.700,00 |
| NFS-e 1186 — treinamento de equipe | **Anexo V assumido**, conforme o conjunto de notas; a biblioteca não define o enquadramento de treinamento | R$ 4.500,00 |
| NFS-e 1187 — desenvolvimento da integração | Serviço de TI, Anexo V | R$ 8.500,00 |
| NFS-e 1188 — estorno parcial da 1184 | Redução de serviço de maio | **(R$ 4.000,00)** |
| NF-e 000.512 — locação de 20 notebooks | Locação de bens móveis, Anexo III sem ISS | R$ 6.000,00 |

As sete notas positivas de serviços somam **R$ 82.000,00**. A 1188 cancela parcialmente a 1184, e a devolução de R$ 4.000,00 aparece no extrato em 29/05. Portanto, **serviços = 82.000 − 4.000 = R$ 78.000,00**. O estorno não foi tratado como despesa nem reduziu a locação. A regra de cancelamentos está em [lc123_art18_fator_r.md](../library/lc123_art18_fator_r.md), seção “Devoluções/cancelamentos”.

A locação de R$ 6.000,00 foi segregada dos serviços e tributada pelo Anexo III com exclusão da parcela de ISS. Fontes: [lc123_art18_fator_r.md](../library/lc123_art18_fator_r.md), art. 18, §4º, e [locacao_bens_moveis_iss.md](../library/locacao_bens_moveis_iss.md), LC 123/2006, art. 18, §5º-A e Súmula Vinculante 31. O XML da locação apresenta PIS de R$ 39,00 e COFINS de R$ 180,00; esses campos não foram abatidos do DAS, pois a biblioteca não prevê tal abatimento. O XML indica `tpAmb=2` e declara documento fictício sem validade fiscal; para uso fiscal real, falta comprovação de NF-e válida.

Os créditos do extrato somam R$ 88.000,00, correspondentes a serviços brutos de 82.000 + locação de 6.000. Após o estorno debitado de R$ 4.000,00, conferem com **R$ 84.000,00** de receitas líquidas apuradas. O saldo bancário também fecha: 41.280,55 + 88.000,00 − 43.180,22 = 86.100,33.

## DAS

O RBT12 de R$ 1.020.000,00 situa ambas as atividades na **4ª faixa** de seus anexos. Alíquotas, parcelas a deduzir e a repartição disponível constam de [anexos_iii_v_tabelas.md](../library/anexos_iii_v_tabelas.md), LC 123/2006, Anexos III e V. Fórmula da alíquota efetiva: [lc123_art18_fator_r.md](../library/lc123_art18_fator_r.md), art. 18, §1º-A.

| Receita | Aritmética | DAS |
|---|---|---:|
| Serviços, Anexo V | (1.020.000 × 20,50% − 17.100) / 1.020.000 = **18,8235294118%**; 78.000 × 18,8235294118% = 14.682,352941… | **R$ 14.682,35** |
| Locação, Anexo III | (1.020.000 × 16,00% − 35.640) / 1.020.000 = **12,5058823529%**; 6.000 × 12,5058823529% = 750,352941…; ISS excluído = 750,352941… × 32,50% = 243,864706…; saldo = 506,488235… | **R$ 506,49** |
| **Total** | 14.682,35 + 506,49 | **R$ 15.188,84** |

Cada atividade foi arredondada ao centavo depois do cálculo com a alíquota efetiva sem arredondamento intermediário. Os campos `anexo`, `faixa` e `aliquota_*` do JSON descrevem **serviços**; a conta da locação usa Anexo III.

**Sensibilidade da NFS-e 1186:** se o treinamento de R$ 4.500,00 devesse ser tratado pelo Anexo III, os serviços no Anexo V seriam R$ 73.500,00 × 18,8235294118% = R$ 13.835,29; o treinamento no Anexo III seria R$ 4.500,00 × 12,5058823529% = R$ 562,76; com a locação de R$ 506,49, o total seria **R$ 14.904,54**, R$ 284,30 abaixo da apuração principal. A biblioteca não permite decidir esse enquadramento com segurança. Essa hipótese alternativa não altera o JSON; a premissa do cálculo principal está documentada nesta memória.

**Sensibilidade do Fator R:** se a folha elegível comprovada alcançasse R$ 285.600,00, os R$ 78.000,00 de serviços, sob as mesmas premissas de classificação, seriam tributados pelo Anexo III: 78.000 × 12,5058823529% = R$ 9.754,59. Somados R$ 506,49 da locação, o DAS seria **R$ 10.261,08**. Não há suporte nos arquivos para acrescentar esse R$ 1.000,00; o cálculo principal usa R$ 284.600,00.

## Repartição em aberto

A biblioteca fornece a repartição da **4ª faixa do Anexo III**, mas não a da **4ª faixa do Anexo V**. Portanto, a repartição **consolidada** de R$ 15.188,84 por tributo é desconhecida. Cada campo de `reparticao` no JSON é `null`, em vez de um zero inventado. Os números exemplificados pelo contrato para esses campos não podem ser preenchidos com a fonte disponível.

Somente para a **locação**, a repartição do Anexo III permite calcular sobre R$ 750,352941…: IRPJ × 4,00% = R$ 30,01; CSLL × 3,50% = R$ 26,26; COFINS × 14,05% = R$ 105,42; PIS × 3,05% = R$ 22,89; CPP × 42,75% = R$ 320,78; ISS excluído × 32,50% = R$ 243,86. Os cinco tributos remanescentes somam **R$ 505,36**, abaixo dos R$ 506,49 de DAS da locação em **R$ 1,13**. Os percentuais fornecidos somam **99,85%** (4 + 3,5 + 14,05 + 3,05 + 42,75 + 32,5), deixando 0,15% sem atribuição. Não forcei o fechamento. Fonte: [anexos_iii_v_tabelas.md](../library/anexos_iii_v_tabelas.md), repartição da 4ª faixa do Anexo III.
