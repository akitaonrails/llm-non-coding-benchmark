# Engajamento: Vetor Alimentos — pedido de dispensa por justa causa de Camila Rocha

Dê o parecer com cálculo de exposição e alternativas. Hoje é 11/10/2026.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.json` — `{"justa_causa_cabivel": true/false, "motivos": ["..."], "estabilidades": [{"tipo": "", "fundamento": "", "ate": "AAAA-MM-DD ou descrição"}], "exposicao_se_reverter": {"verbas_rescisorias": 0, "indenizacao_estabilidade": 0, "dano_moral_estimado": 0, "total": 0}, "alternativas": ["..."], "recomendacao": ""}`
2. `parecer.md` — análise de cada requisito da justa causa com as provas do arquivo; estabilidades; exposição; recomendação.
3. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
