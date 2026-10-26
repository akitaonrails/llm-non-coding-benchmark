I'll do a full pre-delivery review. First, re-reading all deliverables and the authority gate (CONTRACT + INDEX) in parallel:

Now the remaining gate files — QUESTIONS.md and all four library sources (to verify every normative claim against them):

All four library files checked — normative claims verified against them. Now the comprehensive machine cross-check: JSON totals, schema fields, **and every document value re-parsed from the raw XML sources** (not trusting our own earlier extraction):

The first cross-check segment passed all internal arithmetic (all OK). The output truncated mid-way — let me re-run the document-level part to see the remaining saídas (2308–2312), entradas, and the PIS/COFINS reconciliation:

Wrong workdir — retrying with the correct path:

All 17 documents verified field-by-field against the raw XMLs — every number, date, cStat, and destaque matches (2309 inverted destaque vCBS 38,00/vIBSUF 342,00 confirmed; 2308/2310/2312 no group; 2315 CRT 1 no destaque). The 480.000 base reconciles exactly with PIS 3.120 + COFINS 14.400.

All numbers PASS. Now the text fixes. Let me get the exact current text of the passages to be corrected:

All numbers verified — now applying the text fixes. These are independent edits on unique strings, so I'll apply them together:

All 11 edits applied. Final validation sweep — JSON integrity + sums, byte-identity of the question files, and residual-pattern grep:

JSON is clean. cmp needs the right path:

All clean. One last traceability check — the remaining `Q4` references in STATUS.md/QUESTIONS.md need to be legitimately documented in the question file's crosswalk (they refer to the original question numbering, not stale references):

Traceability confirmed — remaining `Q4` mentions in `STATUS.md`/`QUESTIONS.md` are the documented crosswalk (`ex-Q4a/Q4b` → D3/D4), not stale references. Review complete.

## Pre-delivery review — results

**Verified, no changes needed (all machine-checked PASS):**
- **Arithmetic (11/11):** base 480.000,00; débito CBS 4.320/IBS 480; crédito 1.458/162; saldos 2.862 + 318 = 3.180; recolhimento devido 0; alíquota por documento 0,9%/0,1% em todos os 17 lançamentos.
- **Documento a documento vs. os XMLs brutos:** data, valor, cStat e destaque das 12 saídas + 5 entradas conferidos por script — inclui 2309 (destaque invertido vIBSUF 342,00 / vCBS 38,00; pIBSUF 0,90 / pCBS 0,10), 2308/2310/2312 (sem grupo, cStat 100) e 2315 (CRT 1, sem destaque).
- **Reconciliação externa:** base de 480.000,00 bate exatamente com PIS 3.120,00 + COFINS 14.400,00 da apuração normal.
- **Autoridade:** toda afirmação normativa linkeada aos 4 arquivos da biblioteca; não verificáveis marcados **[não verificado]**. Nenhuma citação fora do `INDEX.md`.
- **Integridade:** JSON parseia; schema conforme; 9 seções intactas; `PERGUNTAS.md` byte-idêntico a `QUESTIONS.md`.

## What I changed (11 fixes, all textual — zero numeric changes)

| # | File | Change |
|---|---|---|
| 1 | `apuracao_teste.json` | "registra **as** valores corretos" → "**os** valores" |
| 2 | `orientacao.md` §4 | referência obsoleta "(Q4)" → "D3 em `QUESTIONS.md`/`STATUS.md`" (o arquivo de perguntas usa D1–D6) |
| 3 | `orientacao.md` §4 | citação da rejeição ajustada à literal do cliente: "Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)" |
| 4 | `orientacao.md` §4 | "agosto dela é o exemplo em dobro" → "a NF-e 2309 de agosto é o exemplo em dose dupla" (referente solto) |
| 5 | `orientacao.md` §5 | "Pre-03/08" → "Pré-03/08" |
| 6 | `orientacao.md` §6 | negrito fechava no trecho errado — "**[não verificado]**." isolado, frase seguinte fora do bold |
| 7 | `orientacao.md` §8 | "(Q4)" → "(D3 em `QUESTIONS.md`)" |
| 8 | `orientacao.md` §8 | citação dupla precisada: apuração mensal → art. 346; escrituração → ADCT art. 125, §4º |
| 9 | `orientacao.md` §9 | "decisão interna Q4" → "decisão interna D3" |
| 10 | `orientacao.md` §9 | citação da rejeição padronizada ao literal (igual ao item 3) |
| 11 | `STATUS.md` | "grupo. incorporado" → "grupo. **I**ncorporado" (maiúscula pós-ponto) |

**Pós-correção, revalidado:** JSON parse + somatórios ALL OK; `cmp` idêntico; zero resíduos de "Q4" velho, "Pre-", versão errada da NT ("2025.02"), "1309" ou soft hyphen.

**STATUS.md permanece `COMPLETE WITH OPEN ITEMS`** — correto, pois D1–D6 são desconhecidos reais do cliente, já explicitados.

**GO** — `/work/workspace/deliverable/` está pronto para entrega.