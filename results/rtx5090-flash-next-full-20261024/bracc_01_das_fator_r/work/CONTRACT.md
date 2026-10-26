# Engajamento: apuração do DAS de maio/2026 — Lumen Soluções Digitais ME

Apure o DAS de maio a partir das notas, do extrato, do resumo de folha e do faturamento dos 12
meses anteriores. O sócio pede para "repetir o Anexo V com a alíquota da faixa". Use apenas a biblioteca.

## Entregáveis (em `workspace/deliverable/`)
1. `apuracao.json` — `{"rbt12": 0, "folha_12m": 0, "fator_r": 0.0, "anexo": "III|V", "faixa": 0, "aliquota_nominal": 0.0, "parcela_deduzir": 0, "aliquota_efetiva": 0.0, "receitas": {"servicos": 0, "locacao": 0}, "das": {"servicos": 0, "locacao": 0, "total": 0}, "reparticao": {"IRPJ": 0, "CSLL": 0, "COFINS": 0, "PIS": 0, "CPP": 0, "ISS": 0}}`
2. `memoria.md` — a memória de cálculo com cada fonte da biblioteca; classificação de cada nota; o que foi feito com o estorno e com a locação.
3. `PERGUNTAS.md` (opcional) e `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
