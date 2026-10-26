Boa prática antes de entregar. Vou auditar em três frentes: (1) base de autoridade — toda citação precisa existir na biblioteca fechada; (2) aritmética e conciliação de números entre arquivos; (3) consistência de fatos (CDA, DARFs, datas).

Confirming the current state of the two S5 files before applying the fixes:

All confirmed. Applying the fixes now — first the JSON (fixes 1–2) and the note (fixes 3–4):

Now the reconciliation fix (5) in the control files — reading QUESTIONS.md to get the exact P1 line:

Both target lines identified. Applying the reconciliation fix:

Auditoria concluída e revalidada. Resumo da revisão pré-entrega:

## Corrigido (5 pontos)

1. **`sessao5/garantia.json` — afirmação sem suporte na biblioteca.** Dizia que a fiança "cobraria só de fiador idôneo com bens". A LEF (art. 9º, II, na biblioteca) prevê **fiança bancária** — não fiador pessoal. Reescrito: a fiança da LEF é a bancária, custa "o dobro do seguro ou mais" nas faixas da biblioteca (0,8→2% e 1,5→3% — conferido) e sua disponibilidade é marcada explicitamente como **condição de mercado, não regra dos autos**.
2. **`sessao5/garantia.json` — imprecisão aritmética.** "O seguro custa menos da metade": nos tetos é exatamente a metade (11.524,50 = 23.049 × 0,5). Corrigido para **"metade ou menos"**.
3. **`sessao5/nota_ao_cliente.md` (tabela da §4).** Rótulo "Fiança bancária/seguro-fiança" — "seguro-fiança" não é termo da biblioteca. Corrigido para **"Fiança bancária (LEF art. 9º, II)"**.
4. **`sessao5/nota_ao_cliente.md` (§8).** Citação truncada "(Lei 13.988/2020 + edital da fixtures)" — corrigida para **"(Lei 13.988/2020; Portaria PGFN 6.757/2022 e edital vigente)"**, exatamente como consta na linha de citação do INDEX.
5. **Conciliação 145.000 × 84.000** (STATUS.md item 1 + QUESTIONS.md, linha da P1 sem resposta). O valor "até R$ 145.000,00" (DARF 61 mil + 84 mil) é da época das quatro lavraturas; reconhecida a decadência do 4T/2020, **só o DARF de 84 mil (1T/2021) alcança os créditos vivos** — os 61 mil referem-se a período decaído. Anotado nos dois arquivos de controle como "contagem da Sessão 5", preservando o número histórico e eliminando a aparente contradição com os 84.000 usados na S5.

## Verificado como sólido (sem mudança)

- **Base de autoridade**: todas as citações da S5 existem na biblioteca fechada — LEF art. 16 ("não são admissíveis sem garantia"), LEF art. 9º, II, Portaria PGFN 164/2014 art. 3º (+30%), Lei 9.430 art. 61 §3º, Lei 13.988/2020 (65/70%, 120 meses, confissão irrevogável, vedação a débito decaído). Premissas de mercado (prêmio sobre o valor garantido, ~3 anos de litígio) já estavam rotuladas como premissas/estimativas.
- **Aritmética**: as 591.000 × 1,30 = 768.300; faixas de custo (6.146,40/11.524,50 e 15.366/23.049); transação (283.680 descontáveis < limite 307.320; desconto 184.392 → saldo 406.608; 70% → 392.424); cenários de vitória (360.510; 276.510) — todas reconciliam, e o JSON foi revalidado (schema exato, chaves e valores).
- **Consistência cruzada**: quebras por período (157.040/117.780/27.180 e 150.280/112.710/26.010) batem entre S1, S2 e S5; CDA nº 80.4.26.001234-55 uniforme; Tema 981 continua fora de qualquer peça de juízo.

O pacote das cinco sessões está pronto para entrega, com os itens em aberto documentados (P13–P15 aguardando o cliente; SELIC superveniente dependente da planilha da PGFN).