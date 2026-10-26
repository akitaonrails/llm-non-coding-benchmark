# Engajamento: regime tributário de 2026 — Vértice Engenharia Consultiva Ltda.

O sócio quer sair do Simples **em dezembro** e ir para o Lucro Real porque "credita tudo". Faça a
conta dos três regimes para 2026 e responda ao pedido.

## Entregáveis (em `workspace/deliverable/`)
1. `comparativo.json` — `{"simples": {"das": 0, "iss_fora": 0, "inss_patronal": 0, "total": 0}, "presumido": {"irpj": 0, "csll": 0, "pis_cofins": 0, "iss": 0, "inss_patronal": 0, "total": 0}, "real": {"irpj": 0, "csll": 0, "pis_cofins_debito": 0, "creditos": 0, "iss": 0, "inss_patronal": 0, "total": 0}, "recomendacao": "simples|presumido|real", "mudanca_em_dezembro": "possivel|impossivel", "prazo_opcao": "AAAA-MM-DD"}`
2. `memorando.md` — memória de cálculo com fontes, premissas, riscos e o passo a passo para a opção (se houver mudança).
3. `PERGUNTAS.md` (opcional) e `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
