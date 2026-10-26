# Engajamento: distribuição de lucros de janeiro/2026 — Nexo Logística Ltda.

Os sócios querem R$ 800.000,00 "isentos" ou, alternativamente, um mútuo. Diga o que é possível.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.md` — pode distribuir? quanto, a que título, com que tributação em 2026? o auto de infração importa? o mútuo é alternativa?
2. `numeros.json` — `{"limite_presumido_liquido_teorico": 0, "lucro_contabil_2025": 0, "prejuizos_acumulados": 0, "lucro_distribuivel": 0, "distribuicao_recomendada": 0, "irrf_10pct_se_distribuir_800k": 0, "multa_art32_risco": 0, "mutuo": {"recomendado": true/false, "condicoes": ""}}`
3. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
