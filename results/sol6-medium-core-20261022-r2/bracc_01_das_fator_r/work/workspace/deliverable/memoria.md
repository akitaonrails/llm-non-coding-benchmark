# Apuração do DAS — maio/2026

**DAS calculado sob as premissas abaixo: R$ 15.188,84.** Esse valor depende, em especial, de o percentual de ISS de **32,50%** na tabela do Anexo III estar correto; a própria repartição dessa faixa não fecha. A repartição por tributo permanece indeterminada: a biblioteca não informa os percentuais do Anexo V, 4ª faixa, e os percentuais do Anexo III, 4ª faixa, publicados nela somam 99,85%. Por isso, os seis campos de `reparticao` em `apuracao.json` são `null` (desconhecidos), não zero. Os valores numéricos do JSON são cálculos condicionais, não uma validação da tabela inconsistente. Ver `STATUS.md`.

## Base de 12 meses e Fator R

Período anterior a maio/2026: maio/2025 a abril/2026. Soma das 12 receitas mensais do faturamento: **RBT12 = R$ 1.020.000,00**. Soma dos 12 totais mensais do resumo de folha: **R$ 284.600,00**. Em cada linha do resumo, salários + pró-labore + encargos/FGTS igualam o total informado. **Premissa de caixa:** o arquivo está organizado por *competência*, não traz datas de pagamento de todos os itens, e foi usado como aproximação dos valores pagos dentro da janela de 12 meses. O cliente confirmou que o pró-labore de abril, R$ 1.600,00 para cada sócio, foi pago em **30/04/2026**; os R$ 3.200,00 já constam no total da linha de abril e não foram somados novamente. A observação de “em aberto” no resumo decorreu, segundo o cliente, de registro tardio no sistema. A linha de março registra **R$ 0,00 de pró-labore** e contém essa observação sobre abril; a resposta do cliente não esclarece se houve algum pagamento em março omitido do resumo. Mantive o zero informado, sem criar pagamento. O comprovante de 30/04 foi anunciado, mas ainda não está entre os arquivos recebidos. O extrato de maio não mostra esse pagamento, o que é coerente com a data informada. A folha de maio e os pró-labores pagos em 16/05 ficam fora dos 12 meses anteriores.

Fator R = 284.600 ÷ 1.020.000 = **0,279019607843 = 27,9019607843%**. O limite de 28% equivaleria a R$ 285.600,00 de folha; o total usado fica R$ 1.000,00 abaixo. **Com a premissa de caixa acima**, os serviços de TI usam o **Anexo V**. Como a margem é de R$ 1.000,00, datas ou valores de pagamentos não refletidos no resumo podem alterar o anexo. O critério de caixa para folha e a regra dos 28% constam de [lc123_art18_fator_r.md](/work/workspace/library/lc123_art18_fator_r.md).

## Classificação das notas e conciliação

| Documento | Natureza | Valor na receita de maio |
|---|---|---:|
| NFS-e 1181 — desenvolvimento, sprint 11 | Serviço de TI, Anexo V | R$ 18.000,00 |
| NFS-e 1182 — sustentação mensal | Serviço de TI, Anexo V | R$ 12.500,00 |
| NFS-e 1183 — consultoria de arquitetura | Serviço, Anexo V pelo conjunto de atividades informado | R$ 9.800,00 |
| NFS-e 1184 — desenvolvimento, módulo fiscal | Serviço de TI, Anexo V | R$ 22.000,00 |
| NFS-e 1185 — suporte técnico | Serviço de TI, Anexo V | R$ 6.700,00 |
| NFS-e 1186 — treinamento da equipe | Serviço, Anexo V pelo conjunto de atividades informado | R$ 4.500,00 |
| NFS-e 1187 — desenvolvimento, integração | Serviço de TI, Anexo V | R$ 8.500,00 |
| NFS-e 1188 — cancelamento parcial da 1184 | Estorno dos serviços de maio | **(R$ 4.000,00)** |
| NF-e 000.512 — locação de 20 notebooks | Locação de bens móveis, Anexo III sem ISS | R$ 6.000,00 |

Serviços brutos: 18.000 + 12.500 + 9.800 + 22.000 + 6.700 + 4.500 + 8.500 = **R$ 82.000,00**. A NFS-e 1188 reduz a receita de serviços para **R$ 78.000,00**. A regra de cancelamentos e a segregação por atividade estão em [lc123_art18_fator_r.md](/work/workspace/library/lc123_art18_fator_r.md).

**Premissa de classificação:** as descrições “consultoria de arquitetura” e “treinamento equipe” foram tratadas como atividades ligadas à prestação de TI da empresa. A biblioteca não especifica o enquadramento de treinamento oferecido isoladamente; se essas notas representarem atividades autônomas de natureza diferente, sua classificação e o DAS precisarão de revisão.

A NF-e 000.512 identifica uma locação de bens móveis de R$ 6.000,00; ela não entra na receita dos serviços. A locação segue o Anexo III com dedução da parcela de ISS, conforme [locacao_bens_moveis_iss.md](/work/workspace/library/locacao_bens_moveis_iss.md). Os valores de PIS e COFINS exibidos no XML não foram tratados como abatimento do DAS: a biblioteca não fornece regra para esse abatimento. Os créditos do extrato de maio somam R$ 88.000,00, equivalentes aos serviços brutos de R$ 82.000,00 mais a locação de R$ 6.000,00; o débito de estorno de R$ 4.000,00 leva ao valor líquido de **R$ 84.000,00**, igual a 78.000 + 6.000. O saldo também fecha: R$ 41.280,55 iniciais + R$ 88.000,00 de créditos − R$ 43.180,22 de débitos = **R$ 86.100,33** finais. Isso concilia os lançamentos observados; não prova, por si só, o regime de reconhecimento das receitas.

## Alíquotas e DAS

O RBT12 de R$ 1.020.000,00 cai na **4ª faixa** dos Anexos V e III. Valores nominais e parcelas a deduzir: [anexos_iii_v_tabelas.md](/work/workspace/library/anexos_iii_v_tabelas.md). Fórmula de alíquota efetiva: [lc123_art18_fator_r.md](/work/workspace/library/lc123_art18_fator_r.md).

- **Serviços, Anexo V:** (1.020.000 × 20,50% − 17.100) ÷ 1.020.000 = 192.000 ÷ 1.020.000 = **18,8235294118%**. DAS dos serviços = 78.000 × 18,8235294118% = R$ 14.682,352941… → **R$ 14.682,35**.
- **Locação, Anexo III:** (1.020.000 × 16,00% − 35.640) ÷ 1.020.000 = 127.560 ÷ 1.020.000 = **12,5058823529%**. Parcela cheia = 6.000 × 12,5058823529% = R$ 750,352941…. ISS indicado na tabela para a 4ª faixa = 32,50% dessa parcela, ou R$ 243,864705…. DAS da locação sem ISS = 750,352941… − 243,864705… = R$ 506,488235… → **R$ 506,49**.
- **Total:** R$ 14.682,35 + R$ 506,49 = **R$ 15.188,84**. Os arredondamentos a centavos foram feitos por receita segregada ao final de cada cálculo.

## Repartição em aberto

A tabela de [anexos_iii_v_tabelas.md](/work/workspace/library/anexos_iii_v_tabelas.md) não traz a repartição do Anexo V, 4ª faixa, necessária para os R$ 14.682,35 de serviços. Para o Anexo III, 4ª faixa, os percentuais registrados são 4,00 + 3,50 + 14,05 + 3,05 + 42,75 + 32,50 = **99,85%**, faltando 0,15 ponto percentual. Após retirar os 32,50% de ISS da locação, as cinco quotas publicadas para os outros tributos somam 67,35% da parcela cheia: R$ 750,352941… × 67,35% = **R$ 505,36**, enquanto o DAS calculado da locação é **R$ 506,49**; a diferença é **R$ 1,13** após arredondamento. Não foi atribuída a nenhum tributo. **Não se sabe qual percentual da tabela está errado.** Se o percentual de ISS estiver errado, o DAS da locação e o total também mudarão; portanto, R$ 506,49 e R$ 15.188,84 são condicionais ao ISS publicado de 32,50%. O cliente informou que não dispõe dos percentuais adicionais ou corrigidos. Sem uma fonte na biblioteca, qualquer repartição total seria inventada.
