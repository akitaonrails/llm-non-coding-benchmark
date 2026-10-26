Good — a full pre-delivery QA pass. Let me re-read every authority source and the contract rules, then re-verify the arithmetic independently.

Contract reference moved — let me locate it and audit every source document, deliverable, and extraction:

Contract and sources confirmed. Notice: CONTRACT itself names the optional questions file `PERGUNTAS.md` (line 9) while working rule says `QUESTIONS.md` — moot since no questions arose, but worth recording. Also `/tmp/opencode` was wiped, so I'll re-extract the PDFs and re-verify all arithmetic with a **fresh, independent** script:

/tmp/opencode was wiped and all three outputs confirmed; now the full memoria audit and an independent re-count in parallel:

Path slip — the workspace root is `/work`:

⚠️ **Interesting — my fresh script disagrees with the deliverable (16/12 vs 15/12; 21/01 vs 18/12; 04/02 vs 03/02).** Before touching anything I must settle which is right, and the difference is exactly the "which day is the excluded começo" question. Everything hinges on the verbatim text of art. 224 §§2–3 and art. 231, VII — let me read the full library files:

**Root cause found — the deliverable is right, my verification script was wrong.** The library says:

- **Art. 231, VII**: dia do começo = **a data de publicação** (23/11 fase 1; 11/12 fase 2)
- **Art. 224 caput**: esse dia do começo é **excluído**
- **Art. 224 §3º**/**Lei 11.419 §4º**: a contagem **terá início** no 1º dia útil seguinte à publicação → 24/11 e 14/12 **são contados como dia 1**

My script wrongly double-excluded, treating 24/11 as the começo as well. Correcting the script and reading STATUS:

Both verifications converged: **deliverable dates are correct** (15/12/2026 · 18/12/2026 · 03/02/2027 · dobro hipotético 05/02/2027), and the script bug was double-excluding `inicio_contagem`. Now I need the exact verbatim text of the sections I'm about to fix — reading the memoria's remaining middle section (§3–§6) and the rest of STATUS.md in parallel:

STATUS.md is fully in hand. Now the rest of memoria §6 (lines 180–271), which got truncated earlier:

All targets are now verbatim in hand. Quick safety net first (one grep for any stray buggy-date residue + a final read of `prazos.json`), then I'll apply the fix batch:

No stray dates — all five grep hits sit in correct contexts (apelação day 3 & 6; dobro days 16, 19, 29 — all matching the verified count), and `prazos.json` is fully schema-conformant with correct dates. Two final verbatim checks before editing — the linchpin art. 231 text and the exact art. 1.023 wording my §3 rewrite will quote:

Both linchpins confirmed verbatim: art. 231, VII = "a data de publicação, quando a intimação se der pelo Diário da Justiça impresso ou eletrônico", and art. 1.023 with the parenthetical "(art. 1.026)" but **no rule on when the count restarts** — so the §3 softening is warranted and my quoting will be exact. Applying the complete fix batch (memoria + STATUS):

All 14 edits landed. One last verification sweep — confirming the removed phrases are actually gone and `STATUS.md` still declares exactly one status token:

Path typo on my part (dropped the `/work` prefix). Retrying:

Verification clean: the only remaining occurrences of the removed phrasings are inside STATUS.md's changelog (describing the removals), and `STATUS.md` declares exactly one status token — `COMPLETE`. QA fechado. Segue o relatório:

## Resultado do QA final (pré-entrega)

**1. Datas: todas corretas — nenhuma alterada.** Recontagem independente (script novo) confirmou contra o texto verbatim da biblioteca:

| Prazo | Resultado |
|---|---|
| Contestação (15 úteis, art. 335 III + 231 VII) | **15/12/2026 (ter)** |
| Embargos de declaração (5 úteis, art. 1.023) | **18/12/2026 (sex)** |
| Apelação (15 úteis, art. 1.003 §5º) | **03/02/2027 (qua)** |
| Dobro hipotético (30 úteis) — só referência | 05/02/2027 (sex) |

Convenção reconfirmada no texto literal: começo = data de publicação (art. 231, VII), **excluído** (art. 224 caput); `inicio_contagem` (24/11, 14/12) é o **1º dia contado** (art. 224 §3º / Lei 11.419 §4º). Dias 1–5 da apelação = 14–18/12; recesso 20/12–20/01; dias 6–15 = 21/01→03/02, com 25/01 contado (feriado só na Capital). Obs.: uma primeira versão do meu script de verificação excluía `inicio_contagem` duas vezes e devolvia datas +1 dia (16/12, 21/01, 04/02, 08/02) — bug do script, corrigido; **os entregáveis estavam certos desde o início**.

**2. Sete correções na `memoria.md`** (questões de suporte/autoridade, não de datas):

1. **§3** — removida a afirmação sem base na biblioteca de que o prazo "será computado de novo a partir da intimação da decisão dos embargos". O art. 1.023 (`cpc_prazos_recursais.md`) dá a **interrupção** verbatim (com a remissão "(art. 1.026)"), mas a regra de **quando o prazo volta a correr não está na biblioteca** — a nova data agora está marcada como não calculável a partir de `library/`, operational rule: monitorar o e-SAJ.
2. **§5, item 2** — alinhado ao §3 amaciado.
3. **§6.1 e §7** — agora citam **os dois DJes** para os rótulos "PROCESSO ELETRÔNICO (e-SAJ)" / "Processo Digital" (antes só o PDF da citação, embora os dois PDFs tragam os rótulos).
4. **§6.2** — parêntese truncado reescrito; a memória **não afirma mais que existe** controvérsia externa sobre o art. 229 §2º — a alegação do dobro ficou atribuída ao relato do cliente e marcada como não verificável.
5. **§6.3** — removida a assertiva sem sustentação "não há penalidade por agir antes do termo"; substituída por linguagem de planejamento (protocolar antes do termo não altera a contagem — o termo 15/12/2026 permanece); fechamento reescrito (a biblioteca não traz as consequências da falta de contestação — sinalizado, não citado).
6. **§6.4** — linha faltante da tabela do dobro adicionada: 23–24/01/2027 (sáb–dom), não conta.
7. **§6.5** — linhas duplicadas ("Monitorar e-SAJ" / defesa da outra ré) fundidas em uma.

**3. `STATUS.md` atualizado** — 4 parágrafos reformulados para casar com as correções acima (citação dos dois PDFs; controvérsia externa; assimetria de risco; item aberto 1 reescrito para interrupção × recontagem) + seção nova **"Final QA (pre-delivery)"** documentando a reverificação, o bug do script e as 7 correções. **Status mantido: `COMPLETE`** (token único, conferido).

**4. `prazos.json` — intocado.** Schema conforme o contrato, datas corretas, aritmética exposta nos campos `fundamento`.

**5. Observação (sem impacto):** o `CONTRACT.md` chama o arquivo opcional de perguntas de `PERGUNTAS.md` na linha 9 e `QUESTIONS.md` no restante — controvérsia interna do contrato, mas muda: nenhuma pergunta foi necessária, nada a entregar nesse ponto.

Pronto para entrega: `deliverable/prazos.json`, `deliverable/memoria.md`, `deliverable/STATUS.md`.