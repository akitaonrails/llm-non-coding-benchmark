# STATUS

**COMPLETE WITH OPEN ITEMS**

Apuração do DAS de maio/2026 concluída conforme `apuracao.json` e `memoria.md`, usando exclusivamente a biblioteca. Itens em aberto:

1. **Repartição por tributo da parcela de serviços (Anexo V, R$ 14.682,35) não calculada** — a biblioteca não contém a tabela de repartição do Anexo V; apontar percentagens seria inventá-las. No JSON, os cinco tributos de `reparticao` representam apenas a parcela da locação (Anexo III, R$ 750,35 brutos) e `ISS: null`.
2. **Percentagens do Anexo III na biblioteca somam 99,85% (não 100%)** — diferença de R$ 1,13 na locação (sum 505,36 vs. 506,49 recolhidos) não alocada; não forcei equilíbrio.
3. **Premissas P1–P3 de `memoria.md`** (planilha de faturamento como receita total; encargos de 2025-04 constantes — neutro; treinamento classificado por analogia ao rol exemplificativo de TI). Nenhuma altera o DAS ou o anexo.
4. **Fator R informado com correção de regime de caixa (folha R$ 281.400,00 → 27,5882%)** por causa do pró-labore de abril pago em 06/05/2026 (fora da janela de 12 meses; entra em junho/2026). Sem a correção: folha R$ 284.600,00 → 27,9020%. **O anexo (V) e o DAS não mudam em nenhum dos casos** — ponto de corte: folha ≥ R$ 285.600,00.
5. **Anomalias nos dados de folha, sem efeito na apuração:** (a) o pagamento de 06/05/2026 informado pelo sócio não consta no extrato bancário de maio (tratado como feito por outra conta/canal); (b) a linha 2026-03 do resumo tem pró-labore = 0 com a observação sobre abril lançada nela — se for erro de preenchimento (pró-labore de março na realidade pago), a folha deixa de ser 281.400,00 e passa a 284.600,00 (27,9020%). Qualquer leitura mantém Anexo V, faixa 4 e o mesmo DAS.

Resultado: **DAS maio/2026 = R$ 15.188,84** (serviços R$ 14.682,35 + locação R$ 506,49 já deduzida a parcela de ISS R$ 243,86).
