# Engajamento: Controller — Atlas Distribuidora S.A. em recuperação judicial

Três sessões: mês do pedido; análise do plano; homologação. O diretor financeiro quer pagar um
credor concursal por fora, incluir a União no plano e aplicar a trava de 30% ao ganho do deságio.

## Sessão 1 (`deliverable/sessao1/`)
1. `resposta_diretor.md`; 2. `classificacao_creditos.json` — `[{"credor": "", "valor": 0, "classe": "trabalhista|garantia_real|quirografario|me_epp|extraconcursal_fiduciario|extraconcursal_pos_pedido|nao_sujeito_tributario", "sujeito_ao_plano": true/false, "fundamento": ""}]`; 3. `demonstrativo_mensal_aj.md` (estrutura: caixa, obrigações pós-pedido, concursais, UPI).
## Sessão 2 (`deliverable/sessao2/`)
4. `analise_plano.md` — cada cláusula: legal/ilegal e por quê; 5. `efeito_tributario_desagio.json` — `{"ganho_desagio": 0, "pis_cofins_sobre_ganho": 0, "prejuizo_fiscal": 0, "compensacao": 0, "base_irpj_csll": 0, "irpj_csll": 0, "trava_30_aplicavel": true/false}`.
## Sessão 3 (`deliverable/sessao3/`)
6. `lancamentos_novacao.json`; 7. `passivo_fiscal_solucao.md` — via para a União (parcelamento/transação), com prazos e valores.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
