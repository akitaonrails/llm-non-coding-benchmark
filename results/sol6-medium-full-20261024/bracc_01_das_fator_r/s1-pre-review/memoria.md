# Apuração do DAS — maio/2026 — Lumen Soluções Digitais ME

## Resultado e premissas

**DAS calculado: R$ 15.188,84**, dos quais R$ 14.682,35 dos serviços de TI pelo Anexo V e R$ 506,49 da locação de bens móveis pelo Anexo III sem ISS. É uma apuração **com itens em aberto**: não há demonstração completa de pagamentos da folha de 01/05/2025 a 30/04/2026; a biblioteca não contém a repartição do Anexo V; e a tabela disponível para a 4ª faixa do Anexo III soma 99,85%, não 100%.

Para fechar o valor, adotei como premissa que os totais do resumo de folha são os valores pagos no período de referência, sem pagamentos adicionais omitidos ou valores lançados mas não pagos. O cliente informou nesta conversa que os R$ 3.200,00 de pró-labore de abril foram pagos em 30/04/2026. Eles **já constam** na linha de abril (R$ 3.200,00 de pró-labore; R$ 24.600,00 de folha total) e, portanto, não foram somados outra vez. O comprovante prometido não consta dos arquivos recebidos. O relato anterior de pagamento em 06/05 e a ausência dessa saída no extrato de maio continuam sem conciliação documental. O cliente não tem informação adicional sobre os demais pagamentos da folha. A linha de março tem pró-labore zero; não presumi um pagamento não documentado.

Também considerei o treinamento da NFS-e 1186 como serviço de TI relacionado às demais atividades, pois a descrição isolada não identifica seu objeto técnico. Se não for uma atividade sujeita ao Fator R, sua classificação deve ser revista. A biblioteca descreve o Fator R para serviços de TI, entre outros, mas não dá regra específica para este treinamento (`library/lc123_art18_fator_r.md`).

## Fontes normativas da biblioteca

- `library/lc123_art18_fator_r.md` — RBT12 dos 12 meses anteriores; Fator R com folha **paga** nos 12 meses anteriores, incluindo pró-labore, encargos e FGTS; corte de 28%; fórmula da alíquota efetiva; segregação de receitas e estornos.
- `library/anexos_iii_v_tabelas.md` — faixas, alíquotas nominais, parcelas a deduzir e repartição disponível da 4ª faixa do Anexo III.
- `library/locacao_bens_moveis_iss.md` — locação de bens móveis pelo Anexo III com dedução da parcela de ISS.

Base factual: faturamento e resumo de folha dos 12 meses anteriores, relação de notas de maio, XML da NF-e 000.512, extrato bancário de maio em CSV e PDF, e mensagem do sócio; todos estão em `documents/`. A confirmação posterior do cliente sobre 30/04/2026 foi fornecida na conversa.

## RBT12 e Fator R

O faturamento de 05/2025 a 04/2026 soma **R$ 1.020.000,00**: 78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000. Isso coloca ambas as atividades na **4ª faixa** das tabelas (`library/lc123_art18_fator_r.md`; `library/anexos_iii_v_tabelas.md`).

O resumo de folha soma salários R$ 193.000,00 + pró-labore R$ 35.200,00 + contribuições patronais e FGTS R$ 56.400,00 = **R$ 284.600,00**. Fator R = 284.600 / 1.020.000 = **0,279019607843 = 27,9019607843%**. O corte de 28% corresponde a R$ 285.600,00, diferença de **R$ 1.000,00**. Sob a premissa de folha acima, os serviços de TI ficam no **Anexo V** (`library/lc123_art18_fator_r.md`). Se houver ao menos R$ 1.000,00 de pagamentos elegíveis adicionais no período, sem compensações, os serviços passam ao Anexo III. Nesse cenário ilustrativo, mantendo as demais premissas, o DAS dos serviços seria R$ 9.754,59 e o total R$ 10.261,08 (`library/anexos_iii_v_tabelas.md`; `library/locacao_bens_moveis_iss.md`). Esse risco permanece aberto.

O pagamento informado para abril ocorreu em 30/04, dentro dos 12 meses anteriores a maio, e coincide com o valor já lançado na linha de abril. Um pagamento em 06/05, caso tivesse ocorrido, pertenceria ao mês de maio e não entraria no Fator R desta apuração (`library/lc123_art18_fator_r.md`).

## Classificação das notas e receitas de maio

| Documento | Operação | Valor (R$) | Tratamento |
|---|---|---:|---|
| NFS-e 1181 | Desenvolvimento de software | 18.000,00 | Serviço de TI, Anexo V |
| NFS-e 1182 | Sustentação mensal | 12.500,00 | Serviço de TI, Anexo V |
| NFS-e 1183 | Consultoria de arquitetura | 9.800,00 | Serviço de TI, Anexo V; arquitetura entendida como de sistemas pelo contexto, sujeito a confirmação |
| NFS-e 1184 | Desenvolvimento de módulo fiscal | 22.000,00 | Serviço de TI, Anexo V; reduzido pelo estorno parcial da 1188 |
| NFS-e 1185 | Suporte técnico | 6.700,00 | Serviço de TI, Anexo V |
| NFS-e 1186 | Treinamento de equipe | 4.500,00 | Serviço de TI, Anexo V, sob a premissa acima |
| NFS-e 1187 | Desenvolvimento de integração | 8.500,00 | Serviço de TI, Anexo V |
| NFS-e 1188 | Estorno parcial da 1184 | (4.000,00) | Redução da receita de serviços em maio |
| NF-e 000.512 | Locação de 20 notebooks | 6.000,00 | Locação de bens móveis, Anexo III sem ISS |

Serviços brutos = 18.000 + 12.500 + 9.800 + 22.000 + 6.700 + 4.500 + 8.500 = **R$ 82.000,00**. A NFS-e 1188 registra cancelamento parcial de R$ 4.000,00; o extrato confirma a devolução de R$ 4.000,00 em 29/05. Serviços líquidos tributáveis = **R$ 78.000,00**. O extrato mostra créditos de R$ 88.000,00 (R$ 82.000,00 de serviços brutos + R$ 6.000,00 de locação) e o estorno como débito; portanto, a entrada líquida dessas operações é R$ 84.000,00. O estorno não é despesa dedutível adicional (`library/lc123_art18_fator_r.md`).

A NF-e 000.512 descreve locação de notebooks por R$ 6.000,00. Segreguei essa receita dos serviços e retirei a parcela de ISS do Anexo III, conforme `library/locacao_bens_moveis_iss.md` e a regra de segregação em `library/lc123_art18_fator_r.md`. Os valores de PIS e COFINS destacados no XML não foram tratados como pagamentos ou descontos do DAS: a biblioteca não traz regra para compensá-los. Sua consistência fiscal é um item separado a verificar.

## Alíquotas e DAS

**Serviços, Anexo V, 4ª faixa:** (1.020.000 × 20,50% − 17.100) / 1.020.000 = 192.000 / 1.020.000 = **18,8235294118%**. DAS dos serviços = 78.000 × 192.000 / 1.020.000 = R$ 14.682,352941… = **R$ 14.682,35** (`library/lc123_art18_fator_r.md`; `library/anexos_iii_v_tabelas.md`). A alíquota nominal de 20,50% não é aplicada diretamente à receita do mês.

**Locação, Anexo III, 4ª faixa:** (1.020.000 × 16,00% − 35.640) / 1.020.000 = 127.560 / 1.020.000 = **12,5058823529%**. Parcela integral antes da dedução do ISS = 6.000 × 127.560 / 1.020.000 = R$ 750,352941…. Parcela de ISS = 32,50% × R$ 750,352941… = R$ 243,864705…. DAS da locação = 750,352941… − 243,864705… = R$ 506,488235… = **R$ 506,49** (`library/anexos_iii_v_tabelas.md`; `library/locacao_bens_moveis_iss.md`).

**Total:** R$ 14.682,35 + R$ 506,49 = **R$ 15.188,84**. Usei precisão integral nas fórmulas e arredondamento a centavos para cada segmento.

## Repartição e itens em aberto

O campo `reparticao` em `apuracao.json` está como `null` para cada tributo: o total por tributo não pode ser calculado com a biblioteca disponível. A tabela do Anexo V contém alíquotas e deduções, mas **não contém percentuais de repartição**. A repartição do Anexo III da 4ª faixa lista IRPJ 4,00%, CSLL 3,50%, COFINS 14,05%, PIS 3,05%, CPP 42,75% e ISS 32,50%. Esses percentuais somam **99,85%**. Na parcela integral da locação, isso deixa 0,15% = **R$ 1,125529…** sem destino, antes do arredondamento; não distribuí a diferença por conta própria (`library/anexos_iii_v_tabelas.md`). A parcela de ISS da locação foi excluída integralmente conforme `library/locacao_bens_moveis_iss.md`.

Permanecem sem comprovação: (1) se todos os demais valores do resumo foram efetivamente pagos no intervalo exigido e se houve outros pagamentos elegíveis; (2) o comprovante de 30/04 prometido e a conciliação com o relato anterior de 06/05; (3) a natureza técnica da consultoria de arquitetura e do treinamento; (4) a repartição do Anexo V e a diferença de 0,15% na tabela do Anexo III; (5) a consistência dos destaques de PIS/COFINS no XML da locação. Não há autorização na biblioteca para preencher essas lacunas com percentuais ou regras externos.
