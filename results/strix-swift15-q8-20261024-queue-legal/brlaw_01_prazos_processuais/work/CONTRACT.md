# Engajamento: prazos — Ferreira & Lima Transportes Ltda. (7ª Vara Cível de Campinas, processo eletrônico)

O sócio acredita ter prazo em dobro. Calcule os prazos a partir das duas intimações no DJe, com o
calendário forense da biblioteca.

## Entregáveis (em `workspace/deliverable/`)
1. `prazos.json` — `{"citacao": {"disponibilizacao": "AAAA-MM-DD", "publicacao": "AAAA-MM-DD", "inicio_contagem": "AAAA-MM-DD", "contestacao_vencimento": "AAAA-MM-DD", "prazo_em_dobro": true/false, "fundamento": ""}, "sentenca": {"disponibilizacao": "", "publicacao": "", "inicio_contagem": "", "embargos_vencimento": "", "apelacao_vencimento": "", "dias_suspensos_ou_feriados_considerados": ["..."]}}`
2. `memoria.md` — contagem dia a dia, com o fundamento de cada regra aplicada (publicação, início, dias úteis, feriados, recesso, prazo em dobro).
3. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
