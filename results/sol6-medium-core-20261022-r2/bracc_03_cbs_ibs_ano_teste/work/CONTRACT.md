# Engajamento: apuração-teste de CBS/IBS — agosto/2026 — Horizonte Comércio e Serviços Ltda.

O gerente fiscal acha que "não precisa fazer nada em 2026". Monte a apuração-teste do mês, a
checagem documento a documento e a orientação. **A biblioteca contém a legislação vigente; use-a,
não a memória.**

## Entregáveis (em `workspace/deliverable/`)
1. `apuracao_teste.json` — `{"saidas": [{"numero": 0, "data": "", "valor": 0, "cbs": 0, "ibs": 0, "situacao": "regular|irregular", "motivo": ""}], "entradas": [{"numero": 0, "valor": 0, "credito_cbs": 0, "credito_ibs": 0, "motivo": ""}], "totais": {"debito_cbs": 0, "debito_ibs": 0, "credito_cbs": 0, "credito_ibs": 0, "saldo_cbs": 0, "saldo_ibs": 0}, "recolhimento_devido": 0, "condicao_dispensa": ""}`
2. `orientacao.md` — resposta objetiva ao gerente: o que é devido, o que é dispensado e sob que condição; o que fazer com as notas irregulares; tratamento de clientes do Simples/MEI e de entradas do Simples; o que muda a partir de 03/08.
3. `PERGUNTAS.md` (opcional) e `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
