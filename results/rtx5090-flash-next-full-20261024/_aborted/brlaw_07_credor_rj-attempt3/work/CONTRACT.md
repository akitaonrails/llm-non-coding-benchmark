# Engajamento: Fornecedor Sul S.A. (EPP) — credora da Atlas Distribuidora S.A. em recuperação judicial

Hoje é **20/04/2026**. O edital do art. 52 saiu em 10/04/2026. O cliente acha que não precisa se habilitar,
quer retomar as empilhadeiras e acredita que a homologação do plano extingue a fiança do sócio.

## Entregáveis (em `workspace/deliverable/`)
1. `estrategia.json` — `{"prazo_habilitacao_divergencia": "AAAA-MM-DD", "contagem": "corridos|uteis", "credito_fiduciario": {"valor": 0, "sujeito_ao_plano": true/false, "retomada_dos_bens_agora": true/false, "fundamento": ""}, "credito_quirografario": {"valor": 0, "classe": "III|IV", "fundamento": ""}, "divergencia_de_valor": {"listado": 0, "correto": 0}, "fianca_do_socio": {"extinta_pela_homologacao": true/false, "fundamento": ""}, "voto": {"classe": "", "criterio": ""}, "objecao_ao_plano_prazo": "descrever", "acoes_imediatas": ["..."]}`
2. `habilitacao_divergencia.md` — a peça ao AJ (art. 9º).
3. `resposta_cliente.md` — em linguagem simples, respondendo às três perguntas do e-mail.
4. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
