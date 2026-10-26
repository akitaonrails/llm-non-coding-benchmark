# Engajamento: parecer — Solaris Tecnologia × Rafael Moreira (R.M. Desenvolvimento)

A diretoria considera "risco zero" por causa do Tema 725 e não quer provisionar. Dê o parecer com números.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.json` — `{"probabilidade_vinculo": "baixa|media|alta (faixa %)", "fundamentos": ["..."], "prescricao": {"data_ajuizamento": "", "corte_quinquenal": "", "meses_exigiveis": 0, "meses_prescritos": 0}, "exposicao": {"remuneracao_base": 0, "decimo_terceiro": 0, "ferias_terco": 0, "fgts": 0, "multa_40": 0, "aviso_previo": 0, "inss_patronal": 0, "horas_extras": "estimativa/a apurar", "total": 0}, "tema_1389": {"efeito_processual": "", "efeito_na_exposicao": ""}, "provisao_recomendada": {"classificacao_cpc25": "provavel|possivel|remota", "valor": 0}, "acordo": {"recomendado": true/false, "faixa": [0, 0]}}`
2. `parecer.md` — análise dos requisitos do art. 3º com as provas do arquivo; por que o Tema 725 não resolve; Tema 1389; prescrição; cálculo; estratégia; **sem usar súmulas/OJs canceladas**.
3. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
