I'll do a systematic review: re-verify every citation against the library, re-run the arithmetic, and check cross-document consistency. Starting with the full library:

INDEX confirms the permitted citation ranges. Now reading all four library files to verify every content claim:

CPC 25 and CPC 26 texts confirm the key phrases. Now the other two:

Sources verified. Now reading all six deliverables in full for the audit:

JSON and letter read. Now the remaining deliverables plus the CONTRACT schema spec:

Completing my read of the truncated files before applying fixes:

Now reading the remaining portions I need for exact edits — the letter's addenda and the full JSON:

All content verified. Now applying the review fixes — starting with the JSON (two citation-precision issues):

Now the five fixes in nota_explicativa.md:

Now the ten fixes in carta_diretoria.md:

Continuing with the remaining letter fixes:

Now the STATUS.md fix — reading it fully first:

All fixes applied. Running final validation — JSON parse + schema + arithmetic, plus a grep sweep for any leftover outdated references:

The only remaining grep hit is legitimate: QUESTIONS.md pins "ajustadas à melhor estimativa" to **item 59**, and the library excerpt itself explicitly labels that sentence "Item 59" — that pinpoint citation is supported, so I left it.

Validation passed: JSON parses, matches the CONTRACT.md schema exactly, and all ratios recompute (2.46 / 2.97 / 2.77; ceiling 26,950,000; excesses 150,000 and 2,150,000; gross debt 33,200,000).

## Review complete — list of changes

**1. Citation precision (over-specific pinpointing not supported by the library excerpt)**
The library explicitly labels only the *revision/reversal* sentence as "Item 59"; the specialist-opinion and first-instance-sentence sentences are unnumbered. I stopped pinning those to item 59:
- `classificacoes.json` (provisão): "(CPC 25, item 59)" → "(CPC 25, itens 14-16 e 59)" for the "sentença de 1º grau é forte indicador" point.
- `nota_explicativa.md` §7: the "oral testimony can't support reversal" line now cites CPC 25 collectively with the "conforme efetivamente emitida" wording instead of pinning to item 59.

**2. Tax claims labeled as not in the library (unsupported authority risk)**
- `classificacoes.json` (afac, efeitos_fiscais): "com reflexos de IRPJ/CSLL sobre os juros" → IRPJ/CSLL effects are **not detailed in the library — labeled não verificados**, quantification deferred to the tax team.
- `nota_explicativa.md` §3: same fix — "com impactos de IRPJ/CSLL" → explicitly flagged não verificado.

**3. Outdated cross-references to already-answered questions (internal inconsistency)**
- `nota_explicativa.md` §3: "a classificação final depende do teor do documento de origem (Q5)" → Q5 answered: nothing was ever formalized and no instrument was produced; classification stays circulante unless a ≥12-month instrument appears.
- `nota_explicativa.md` §7: the R$ 150k contribution figure now marked **illustrative** — January/2026 contributions do not change the 31/12/2025 test (was readable as if they could).
- `carta_diretoria.md` §1: Q2 request annotated "[Atualizado na rodada 2: não existe manifestação escrita posterior]".
- `carta_diretoria.md` Consequências item 1: "Se não houve waiver... (confirmar — Q4)" → "**Não houve waiver até 31/12/2025** (confirmado na rodada 2)" — matches the now-settled fact and the addendum.
- `STATUS.md` line 5: "QUESTIONS.md (rodadas 1–2)" → "(rodadas 1–3)".

**4. Net vs. gross debt errors in consequence passages (net debt is only the covenant metric)**
- `nota_explicativa.md` §5: "obrigação imediata de ~R$ 29,1 mi de dívida líquida" → gross exigible debt **R$ 33,2 mi** (31,2 + 2,0) vs cash 4,1.
- `carta_diretoria.md` item 3 and Adendo 2 item 5: same correction to R$ 33,2 mi gross — "dívida líquida contra caixa" was also double-counting cash.

**5. Wording/grammar errors**
- `carta_diretoria.md` Adendo 2 item 5: broken sentence "uma antecipação que o contrato já produziram os fatos" → "relata a antecipação que os fatos e o próprio contrato já produziram".
- `carta_diretoria.md` Adendo 2 item 4: "Se a auditoria testar a escritura sobre as demonstrações" → the covenant test is run **on the audited statements** (Cláusula 7.1(c)).
- `carta_diretoria.md` §3: PN CST 17/84 wording corrected to the library's text — "até a primeira AGE/alteração contratual após o recebimento ou em até 120 dias **do encerramento do exercício**" (was "120 dias após o exercício do recebimento").
- `carta_diretoria.md` table header: "≥ critério?" → "Dentro do limite (≤ 2,75)?" (the criterion is a maximum).
- `carta_diretoria.md` §1: "provisão que o advogado qualifica como provável" → "cuja **saída de recursos** o próprio advogado qualifica como provável" (the lawyer qualifies the outflow, not the provision).
- `carta_diretoria.md` Adendo 2 item 3: garbled "Mútuo de sócio é mutuário de pior qualidade fiscal" rephrased.
- `carta_diretoria.md` Adendo 2 table: label "(máximo favorável admissível)" → "(cenário pró-diretoria, sem a reversão)" — keeping the CCB non-current is *not* admissible, the label overstated it.

**Verified unchanged:** all figures (1,200,000 / 6,500,000 / 2,000,000; 27.1/29.1/33.2 debt; 9.8/11.0 EBITDA; 2.77/2.46/2.97; ceiling 26.95M) reconcile across JSON, note, and letter; every quoted authority phrase ("conforme efetivamente emitida", "forte indicador", item 73 rollover, "exclusivo critério do Credor", 75% waiver, "120 dias do encerramento do exercício", IOF "pessoa física/jurídica e PJ") matches the library text verbatim; schema keys and `cumprido: false` intact. Status remains **COMPLETE WITH OPEN ITEMS** (Q1 debentures, Q3 breakdown, Q6 cash encumbrances remain declared assumptions).