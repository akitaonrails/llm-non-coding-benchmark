Reviewing before delivery — I'll re-verify every citation against the library, re-check the arithmetic, and cross-check the deliverables for internal consistency.

Cross-checking library citations against tables now — everything matches so far (faixa 4 = up to 1,800,000; 20.50%/17,100 and 16.00%/35,640; repartição 99.85%; payment-basis Fator R rule; estorno rule). Next, a full end‑to‑end recomputation from the raw documents, including the per-line repartição rounding:

All numbers re-verified end-to-end (JSON matches the independent recomputation exactly). Now I'll read the current deliverables to apply the review fixes precisely.

Now let me read QUESTIONS.md and the full JSON `_notes` before editing.

One STATUS edit missed on indentation — let me re-check the exact lines and redo it.

All fixes applied. Final validation pass — JSON validity/schema, no stray external references, and re-confirm the numbers after edits:

Revisão pré‑entrega concluída. **Nenhum erro de aritmética foi encontrado** — recomput tudo de forma independente a partir dos CSVs/XML (Decimal, arredondamento centavo a centavo) e tudo bate com o `apuracao.json` e a memória, inclusive item a item da repartição.

## O que foi conferido (e fechou)

- **Autoridade**: cada citação dos deliverables foi confrontada com os 3 arquivos da biblioteca — RBT12 (§1º), alíquota efetiva §1º‑A, Fator R §§5º‑J/5º‑M (≥ 28% → III, senão V), folha paga (Res. CGSN 140, art. 26, §§1º‑2º), segregação §4º, regra do estorno, locação §5º‑A + SV 31 + art. 25 §1º V. Tudo existe na biblioteca, como citado.
- **Tabelas**: 1.020.000 cai na 4ª faixa (até 1.800.000); V: 20,50%/17.100 → efetiva 18,8235%; III: 16,00%/35.640 → 12,5059%; repartição III 4ª faixa soma 99,85% (gap de R$ 1,13 tratado como gap aberto, não forçado — correto).
- **Números**: RBT12 = 1.020.000; folha = 284.600; fator R = 27,90%; DAS 14.682,35 + 506,49 = **15.188,84**; linhas da repartição e soma 15.187,71; conciliação do extrato (88.000 − 4.000 = 84.000); cenário alternativo Anexo III (10.261,08) e armadilha da nominal 20,50% (+1.307,65) reconfirmados.
- **Schema**: todas as chaves exigidas pelo `CONTRACT.md` presentes.

## O que mudei na revisão

1. **`memoria.md` §7 — imprecisão de arredondamento**: a base da repartição da locação estava escrita como "750,35" (arredondada), mas os valores da tabela (CPP 320,78, soma 505,36, gap 1,13) usam a base cheia **750,3529…**. Reescrito para dizer exatamente isso; mesma precisão acrescentada ao `_notes` do JSON.
2. **Autoridade estrita — `memoria.md` §7, `STATUS.md` item 2, `QUESTIONS.md` item 2**: removidas as menções a "PGDAS‑DAS" (sistema que não tem fonte na biblioteca). Agora diz apenas "conferir a repartição exibida na guia de pagamento do Simples", com a ressalva de que nenhum sistema é citado por falta de fonte citável.
3. **Elemento do extrato que não estava tratado**: o débito **"DAS ABR/2026 −10.480,22"** (20/05) equivale a ~**12,05% da receita de abril** — patamar mais próximo de Anexo III que de Anexo V. Isso não altera maio (janela de abril própria, não está no acervo), mas é um sinal de que a folha de 2026‑03 (pró‑labore zerado, a R$ 1.000 do corte de 28%) merece conferência. Registrado como indício **não conclusivo e rotulado** no §2 da memória, no item 1 do `STATUS.md` e no `_notes` do JSON.
4. **`apuracao.json` — ambiguidade do campo único `anexo`**: o caso usa dois anexos (V para serviços, III para locação), mas o schema do contrato tem um só campo. Acrescentados `"anexo_locacao": "III"` e `"aliquota_efetiva_locacao": 0.0844147059` (validado: × 6.000 = 506,49) e o `_notes` agora explicita que `anexo`/`faixa`/alíquotas principais se referem à parte de serviços.

Entregáveis em `workspace/deliverable/`: `apuracao.json`, `memoria.md`, `QUESTIONS.md` (≡ `PERGUNTAS.md`), `STATUS.md` — **COMPLETE WITH OPEN ITEMS**, com os mesmos 6 itens abertos (crítico: margem de R$ 1.000 do Fator R), agora também ilustrado pelo indício do DAS de abril.