Now let me run the calculations with Python.

Calculation done. Now let me write the deliverables.

Entrega fechada. Os quatro arquivos estão em `workspace/deliverable/`:

- **`apuracao.json`** — RBT12 1.020.000 · folha 284.600 · Fator R **27,9020% < 28% → Anexo V**, 4ª faixa, efetiva 18,823529% · serviços 78.000 → **14.682,35** · locação 6.000 → **506,49** (Anexo III sem ISS, 8,4415%) · **DAS total 15.188,84** · `reparticao` em `null` (tabela do Anexo V ausente na biblioteca) — JSON validado, aritmética confere.
- **`memoria.md`** — memória de cálculo com as 3 fontes da `library/INDEX.md`, classificação nota a nota, tratamento do estorno (reduz mai/2026) e da locação (segregada), conciliação com o extrato e a sensibilidade do Fator R.
- **`QUESTIONS.md`** — Q1–Q8 para o cliente responder na próxima rodada, com impacto de cada uma. O ponto crítico: **Q1–Q3**, datas de *pagamento* da folha — faltam **R$ 1.000** para o limiar de 28% (285.600); se confirmado folha paga ≥ esse valor, o anexo vira **III** e o DAS cai para **10.261,08** (−4.927,76). Também: pró-labore de mar/2026 (linha zerada) e abr/2026 (e-mail diz 06/05, extrato não mostra), mecânica da dedução do ISS (diferença de 68,14), tabela de repartição do Anexo V ausente e a linha do Anexo III que soma 99,85%.
- **`STATUS.md`** — `COMPLETE WITH OPEN ITEMS` com a lista; **`PERGUNTAS.md`** (opcional) como ponteiro para `QUESTIONS.md` para não divergir.

Nada foi forçado para fechar: o descasamento de 1,13 na repartição da locação (505,36 × 506,49) e o DAS de abril (10.480,22 ≈ Anexo III, contra a lembrança do sócio de Anexo V) ficaram registrados como abertos. Aguardo as respostas do cliente (Q1–Q3 principalmente) para re-rodar o teste do Fator R e preencher `reparticao` se vier a tabela do Anexo V.