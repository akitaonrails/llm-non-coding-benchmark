# Vértice Engenharia Consultiva — comparação de regimes para 2026

**Conclusão de planejamento.** Com os valores e premissas abaixo, manter o Simples é a alternativa de menor desembolso tributário: **R$ 975.600**, contra **R$ 1.111.120** no Lucro Presumido e **R$ 1.112.290** no Lucro Real. A vantagem estimada do Simples é de R$ 135.520 frente ao Presumido e R$ 136.690 frente ao Real. **Não é possível trocar de regime apenas para dezembro.** Como a data corrente é outubro de 2026, a próxima exclusão voluntária do Simples pode produzir efeitos em **1º de janeiro de 2027**, se comunicada até **29 de janeiro de 2027**. O prazo correspondente para produzir efeitos em 2026 foi **30 de janeiro de 2026**. A conclusão numérica é condicional: a biblioteca não contém a tabela do Anexo IV e faltam a base exata da contribuição patronal, a segregação da folha e dados de calendário.

## Base e premissas

| Item | Valor usado | Base da conta / ressalva |
|---|---:|---|
| Receita anual | R$ 4.200.000 | Projeção estável de 2026, sem mudança de mix |
| Obras com material | R$ 630.000 | 15% × R$ 4.200.000; confirmação do cliente |
| Consultoria | R$ 3.570.000 | 85% × R$ 4.200.000 |
| Lucro antes de IRPJ/CSLL | R$ 756.000 | 18% × R$ 4.200.000; assumido como base tributável de IRPJ e CSLL no Real, sem ajustes ou prejuízos compensáveis |
| Folha usada como base provisória | R$ 1.300.000 | **Proxy, não base apurada**: valor recebido inclui pró-labore, encargos e FGTS; a remuneração sujeita à contribuição pode ser menor |
| Folha de obras no Simples | R$ 195.000 | Proxy de 15% da folha, por falta de apontamento de pessoal por atividade |
| ISS fora do DAS | 5% da receita integral | Hipótese de R$ 210.000 em cada regime; faltam período de início do recolhimento fora do Simples e eventual redução de base de obras |

Para o Simples, tratamos as obras com materiais como construção enquadrada no Anexo IV e a consultoria como Anexo III, seguindo a segregação indicada em [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md). A descrição recebida permite apenas esse **cenário preliminar**; o enquadramento final depende dos contratos. Assumimos RBT12 constante de R$ 4,2 milhões durante 2026; a receita mensal efetiva não foi fornecida. **Premissa jurídica não verificada:** para Anexo IV na 6ª faixa, usamos alíquota nominal de **33%** e parcela a deduzir de **R$ 828.000**. A tabela do Anexo IV **não está na biblioteca autorizada**, portanto essa parcela do DAS não tem fonte verificável aqui e deve ser confirmada antes de qualquer decisão definitiva.

## Simples Nacional

A 6ª faixa do Anexo III usa 33% e parcela a deduzir de R$ 648.000; o ISS nessa faixa é recolhido fora do DAS, segundo [anexo_iii_faixa6.md](../library/anexo_iii_faixa6.md). O sublimite de ISS é R$ 3,6 milhões, com regras de início de efeitos que dependem do excesso e do calendário, segundo [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md).

**Limite e sublimite são diferentes:** R$ 4,2 milhões projetados ficam **R$ 600.000 abaixo** do limite anual de R$ 4,8 milhões para EPP; ultrapassar R$ 3,6 milhões afeta o recolhimento de ISS, não implica por si só saída do Simples. O gatilho de excesso superior a 20% sobre o sublimite seria **R$ 4,32 milhões** (3,6 milhões × 1,20), acima da projeção. Como falta a receita de cada ano e mês, o início efetivo do ISS fora em 2026 não está demonstrado. A biblioteca descreve ISS zerado na 6ª faixa do Anexo III; não fornece elementos suficientes para reconciliar essa regra de repartição com um possível diferimento dos efeitos do sublimite neste caso. Por isso, o ISS de R$ 210.000 fora do DAS é **hipótese de cenário, não apuração confirmada** ([anexo_iii_faixa6.md](../library/anexo_iii_faixa6.md); [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md)).

| Parcela | Aritmética | Valor |
|---|---:|---:|
| Alíquota efetiva Anexo III | (4.200.000 × 33% − 648.000) ÷ 4.200.000 | 17,5714286% |
| DAS consultoria | 3.570.000 × 17,5714286% | R$ 627.300 |
| Alíquota efetiva Anexo IV, **não verificada** | (4.200.000 × 33% − 828.000) ÷ 4.200.000 | 13,2857143% |
| DAS obras, **não verificado** | 630.000 × 13,2857143% | R$ 83.700 |
| DAS total | 627.300 + 83.700 | **R$ 711.000** |
| ISS fora do DAS, assumido | 4.200.000 × 5% | R$ 210.000 |
| INSS patronal das obras, provisório | 1.300.000 × 15% × 28% | R$ 54.600 |
| **Total** | 711.000 + 210.000 + 54.600 | **R$ 975.600** |

A CPP de Anexo III integra o DAS; para Anexo IV, a contribuição patronal é recolhida à parte. A alíquota de 28% é somente o total **típico** de 20% + RAT/FAP + terceiros; as alíquotas específicas e a folha bruta não foram informadas ([inss_patronal.md](../library/inss_patronal.md)). O ISS foi somado sobre toda a receita por hipótese; o momento em que o sublimite produz efeitos para a empresa em 2026 permanece aberto.

**A base previdenciária não reconcilia com o resumo recebido:** R$ 1,3 milhão já contém encargos e FGTS, mas não há abertura que permita subtrair esses valores para chegar à remuneração bruta. Os R$ 54.600 acima são apenas o resultado de aplicar a hipótese de 28% a um proxy de R$ 195.000, não a contribuição apurada.

## Lucro Presumido

Para IRPJ, presumimos 8% sobre obras com materiais e 32% sobre consultoria; para CSLL, 12% e 32%, respectivamente. O adicional de IRPJ é 10% acima de R$ 60.000 por trimestre. Assumimos quatro trimestres iguais, pois não há série mensal: base de IRPJ de R$ 1.192.800 ÷ 4 = R$ 298.200 por trimestre; adicional de (R$ 298.200 − R$ 60.000) × 10% × 4 = R$ 95.280. Uma distribuição desigual pode alterar o adicional; a apuração efetiva é trimestral. PIS/COFINS cumulativos somam 3,65% sem crédito ([lei9249_9430_presumido.md](../library/lei9249_9430_presumido.md)).

| Parcela | Aritmética | Valor |
|---|---:|---:|
| Base IRPJ | 630.000 × 8% + 3.570.000 × 32% | R$ 1.192.800 |
| IRPJ normal | 1.192.800 × 15% | R$ 178.920 |
| Adicional IRPJ | (1.192.800 − 240.000) × 10% | R$ 95.280 |
| **IRPJ** | 178.920 + 95.280 | **R$ 274.200** |
| Base CSLL | 630.000 × 12% + 3.570.000 × 32% | R$ 1.218.000 |
| **CSLL** | 1.218.000 × 9% | **R$ 109.620** |
| **PIS/COFINS** | 4.200.000 × (0,65% + 3%) | **R$ 153.300** |
| **ISS, assumido** | 4.200.000 × 5% | **R$ 210.000** |
| **INSS patronal, provisório** | 1.300.000 × 28% | **R$ 364.000** |
| **Total** | 274.200 + 109.620 + 153.300 + 210.000 + 364.000 | **R$ 1.111.120** |

## Lucro Real

Assumimos que o lucro contábil de R$ 756.000 já reflete todos os custos operacionais e contribuições patronais e coincide com as bases fiscais de IRPJ e CSLL. **A biblioteca fechada não traz as regras de apuração do Lucro Real nem as alíquotas de IRPJ/CSLL desse regime**; aplicamos, como hipótese **não verificada para o Real**, as alíquotas de 15% + adicional de 10% acima de R$ 240.000/ano e 9% para CSLL que constam da referência do Presumido. A ausência de adições, exclusões e prejuízos fiscais também é hipótese não confirmada.

PIS/COFINS não cumulativos somam 9,25% sobre receita. A biblioteca admite créditos de insumos essenciais ou relevantes e exclui uso/consumo administrativo, mobiliário e veículos administrativos ([pis_cofins_nao_cumulativo.md](../library/pis_cofins_nao_cumulativo.md)). As seis compras recebidas reconciliam com os R$ 1,4 milhão: **R$ 420.000 + R$ 280.000 + R$ 200.000 = R$ 900.000** de materiais de obras e licenças CAD/BIM tratados como insumos provisórios; **R$ 180.000 + R$ 220.000 + R$ 100.000 = R$ 500.000** de mobiliário, veículos administrativos e papelaria excluídos. A indicação de ICMS-ST nas notas **não prova crédito de PIS/COFINS**; a biblioteca não esclarece eventual ajuste da base de crédito por ICMS-ST. A elegibilidade das licenças e o valor efetivo dos créditos dependem da documentação e do uso.

| Parcela | Aritmética | Valor |
|---|---:|---:|
| IRPJ normal, hipótese não verificada para o Real | 756.000 × 15% | R$ 113.400 |
| Adicional IRPJ, hipótese não verificada para o Real | (756.000 − 240.000) × 10% | R$ 51.600 |
| **IRPJ** | 113.400 + 51.600 | **R$ 165.000** |
| **CSLL**, hipótese não verificada para o Real | 756.000 × 9% | **R$ 68.040** |
| **PIS/COFINS débito** | 4.200.000 × 9,25% | **R$ 388.500** |
| **Créditos provisórios** | 900.000 × 9,25% | **R$ 83.250** |
| PIS/COFINS líquido | 388.500 − 83.250 | R$ 305.250 |
| **ISS, assumido** | 4.200.000 × 5% | **R$ 210.000** |
| **INSS patronal, provisório** | 1.300.000 × 28% | **R$ 364.000** |
| **Total** | 165.000 + 68.040 + 305.250 + 210.000 + 364.000 | **R$ 1.112.290** |

Creditar indevidamente **todas** as compras geraria R$ 1.400.000 × 9,25% = R$ 129.500, ou **R$ 46.250 a mais** que o crédito provisório. Se as licenças de R$ 200.000 não forem aceitas como insumo, o crédito cai R$ 18.500 e o total do Real sobe para **R$ 1.130.790**. A diferença de apenas R$ 1.170 entre Presumido e Real no cenário principal não é robusta diante dessas incertezas.

## Decisão, prazos e pontos em aberto

1. **Para 2026:** manter o Simples no cenário calculado. A opção pelo Simples é anual e irretratável no ano; a exclusão voluntária comunicada após janeiro só produz efeitos em 1º de janeiro do ano seguinte. Logo, **não há troca válida apenas em dezembro de 2026** para reduzir a alíquota desse mês ([lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md)). A mesma lógica impediria uma troca apenas em dezembro de 2025. A biblioteca não descreve mecanismo de opção pelo Lucro Real para o ano em curso; qualquer afirmação adicional sobre ele seria não verificada.
2. **Se a empresa decidir sair do Simples em 2027:** confirmar o regime com dados atualizados, então comunicar a exclusão por opção até o último dia útil de janeiro de 2027, **29/01/2027**, para efeitos desde 01/01/2027. A data registrada em `comparativo.json` é o **prazo da exclusão voluntária do Simples**, não um prazo verificado de opção pelo Lucro Real. Se optar pelo Presumido, a opção se manifesta no pagamento da primeira quota do primeiro período de apuração e vale pelo ano inteiro ([lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md); [lei9249_9430_presumido.md](../library/lei9249_9430_presumido.md)). O procedimento operacional e o calendário de pagamentos não estão na biblioteca e devem ser confirmados antes de protocolar.
3. **Antes de qualquer mudança:** obter os contratos para validar a classificação das obras; a tabela oficial do Anexo IV para fundamentar o DAS; receita mensal e histórico do sublimite; folha bruta sujeita à contribuição e sua alocação entre atividades; RAT/FAP e terceiros efetivos; bases tributáveis do Real; e comprovação de créditos de insumos. Sem esses dados, os valores são **estimativas**, não apuração para recolhimento.

**Sensibilidade decisiva:** mantendo os demais pressupostos e os 15% de folha alocados às obras, o Presumido ultrapassa o Simples em R$ 135.520 quando se usa R$ 1,3 milhão como base previdenciária. Com uma base bruta efetiva abaixo de aproximadamente **R$ 730.588**, a ordem entre esses dois regimes se inverteria: a diferença é `−173.880 + 28% × 85% × folha bruta`. Portanto, a recomendação depende de confirmar a folha. O DAS do Anexo IV também é decisivo: mantidas as demais hipóteses, teria de exceder **R$ 219.220** para o Presumido ficar abaixo do Simples; a estimativa não verificada usada é R$ 83.700. Não há informação suficiente para transformar essas sensibilidades em valores definitivos.

## Resposta ao pedido de dezembro e à hipótese de outra empresa

**Pedido de exclusão no portal em dezembro de 2026.** Mesmo que o portal aceite a comunicação em dezembro, a **data de envio não é a data de eficácia**. Para a exclusão *voluntária*, a regra disponível diz que a comunicação feita depois do último dia útil de janeiro somente produz efeitos em **1º de janeiro do ano seguinte**. Portanto, um pedido enviado em dezembro de 2026 produziria efeitos em **01/01/2027**, não permitiria tributar a receita de dezembro de 2026 pelo Lucro Real da própria Vértice ([lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md)). Isso não examina alguma causa de exclusão obrigatória, para a qual não foram apresentados fatos nem regras completas na biblioteca.

**Abrir outra pessoa jurídica.** O cenário de faturamento por uma empresa nova exigiria verificar **quem efetivamente contratou e prestou** as atividades, com contratos, execução, recursos, notas e recebimentos coerentes. A mera emissão de nota por outra empresa por serviços prestados pela Vértice não demonstra transferência da operação. A biblioteca fechada não contém regras para decidir a atribuição legal da receita, a validade contratual, eventuais regras antielisivas ou o enquadramento fiscal de uma nova empresa; **nenhuma conclusão jurídica sobre a viabilidade do arranjo foi verificada**.

A biblioteca também não cobre a opção inicial de uma empresa nova pelo Lucro Real, requisitos de funcionamento, contratos entre partes relacionadas ou eventual efeito da participação dos mesmos sócios sobre a permanência da Vértice no Simples. **Não é possível afirmar que a empresa nova poderia iniciar no Lucro Real em dezembro nem quantificar economia** com os dados recebidos. Seria preciso examinar quem contrata e presta os serviços de dezembro, a estrutura operacional da nova empresa, o vínculo societário, receitas de ambas e os custos próprios da operação. O comparativo anual de 2026 permanece relativo **à Vértice**, sem transferência de faturamento.
