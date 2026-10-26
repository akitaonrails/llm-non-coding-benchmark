All documents and library files are read. Now let me verify the directory aliases and run the arithmetic in Python.

The arithmetic reconciles perfectly (output base 480.000,00 = PIS/COFINS base in the normal apuração — good cross-check). Now generating the JSON deliverable:

The JSON math checks out, but I introduced some text typos in the `motivo` strings. Let me rewrite the JSON file cleanly and verify it:

I'll pick up where we left off. Let me refresh the key files before writing the remaining deliverables.

JSON deliverable is in place. Let me refresh the library sources so citations in the orientation are exact.

All sources refreshed. Quick re-verification of the arithmetic with Python before writing the orientation:

Arithmetic confirmed. Now writing `orientacao.md`:

Fixing two glitches I noticed in the text (a softHyphen in "documento" and a stray "1309→"):

`orientacao.md` completed. Now writing `QUESTIONS.md` (and the `PERGUNTAS.md` copy per CONTRACT wording):

All deliverables present. Writing `STATUS.md`:

Final sanity check — JSON validity, schema fields, and file inventory:

All deliverables are complete and verified. Final summary:

## Deliverables in `workspace/deliverable/`

| File | Content |
|---|---|
| **`apuracao_teste.json`** | Full CONTRACT schema — 12 saídas (2301–2312), 5 entradas (2313–2317), totais, `recolhimento_devido: 0.00`, `condicao_dispensa`. JSON parses; every sum re-verified in Python |
| **`orientacao.md`** | Objective answer to Paulo: what's due, the conditional dispensa, handling of the 4 irregular notes, Simples/MEI clients, Ponto Fixo entrance, what changes from 03/08, and a 6-point action plan with arithmetic tables |
| **`QUESTIONS.md`** (+ `PERGUNTAS.md` copy) | 5 questions: identity of the 2 rejected notes; NFS-e/other docs in August (population); how notes passed SEFAZ post-03/08 without the group (cStat 100 anomaly); treatment of the 4 irregular notes + credit use by BRISA/SERRA VERDE; the lost R$ 480,00 credit on NF 2313 |
| **`STATUS.md`** | **COMPLETE WITH OPEN ITEMS** — list of the 5 confirmations above |

## Key figures (all shown with arithmetic)

- Saídas base **480.000,00** (matches PIS/COFINS base exactly) → débito **CBS 4.320,00 / IBS 480,00**
- Créditos (2314/2316/2317 only) → **CBS 1.458,00 / IBS 162,00**
- Saldo **CBS 2.862,00 + IBS 318,00 = 3.180,00**; due today **0,00** under the dispensa (ADCT art. 125, §4º) — at risk from the 4 irregular notes (2308, 2310, 2312 without the group; 2309 with swapped rates)
- If the dispensa is lost: R$ 3.180,00, fully compensable against PIS/COFINS 17.520,00 (art. 125, §1º)
- No credit on 2313 (no destaque — 480,00 lost) and 2315 (Simples supplier — art. 347); **do not credit the Ponto Fixo entrance**

All citations point only to the four `library/INDEX.md` files; everything beyond the library (ERP bypass cause, cancellation procedure, retroactive credit) is labeled **[não verificado]**. Waiting on the client's scripted answers to `QUESTIONS.md` to close the open items.