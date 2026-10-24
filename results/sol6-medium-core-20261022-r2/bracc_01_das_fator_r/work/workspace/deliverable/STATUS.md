COMPLETE WITH OPEN ITEMS

- O DAS de maio/2026 foi calculado em R$ 15.188,84 **sob as premissas documentadas em `memoria.md`**. O valor da locação e o total dependem de o percentual de ISS de 32,50% da tabela inconsistente do Anexo III estar correto.
- A repartição por IRPJ, CSLL, COFINS, PIS, CPP e ISS não pode ser fechada com a biblioteca atual: faltam os percentuais da 4ª faixa do Anexo V e os percentuais da 4ª faixa do Anexo III somam 99,85%. Os campos correspondentes no JSON são `null`.
- O cliente confirmou pagamento do pró-labore de abril em 30/04/2026, mas o comprovante anunciado ainda não foi recebido. O resumo de folha está organizado por competência e não demonstra as datas de pagamento dos outros itens. A linha de março registra pró-labore zero e contém uma observação sobre abril; não há confirmação independente de eventuais pagamentos omitidos em março. O Fator R usa os totais informados como valores pagos na janela anterior a maio/2026; diferença de R$ 1.000,00 já alcançaria o limite de 28%.
- A classificação da consultoria de arquitetura e do treinamento como serviços de TI usa a premissa explicitada em `memoria.md`; a biblioteca não trata do treinamento isolado.
