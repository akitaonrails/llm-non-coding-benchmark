# Engajamento: Técnica Forte × Metalúrgica Boa Vista — cobrança de R$ 180 mil (2020/2021)

Hoje é 12/10/2026. O cliente quer executar e protestar e já negativou. Analise.

## Entregáveis (em `workspace/deliverable/`)
1. `analise.json` — `{"via_processual": "execucao|monitoria|cobranca", "por_que": "", "prescricao": [{"parcela": 1, "vencimento": "", "interrompida_em": "", "novo_termo": "", "prescrita": true/false}], "valor_principal_exigivel": 0, "valor_prescrito": 0, "negativacao": {"regular_quanto_a": 0, "indevida_quanto_a": 0, "risco_dano_moral": "", "acao": ""}, "protesto": "recomendado|nao", "recomendacao": ""}`
2. `memorando.md` — raciocínio parcela a parcela (datas), via processual, negativação/protesto, estratégia (ação × acordo) com números (principal exigível + encargos estimados).
3. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
