# Engajamento: abertura da Clínica Estética Aurora — estrutura, tributos e documentos

Os sócios trazem um plano pronto (minuta da internet, pró-labore zero, imóvel sem ITBI, Simples,
servidora como administradora, sócia 'de trabalho'). Diga o que pode e o que não pode, e proponha a
estrutura correta.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.md` — ponto a ponto: quadro societário (quem pode ser sócio/administrador; como a Dra. Luana participa), integralização do imóvel (valor e ITBI), regime e CNAEs, pró-labore e distribuição em 2026 (com números), cláusulas da minuta a corrigir.
2. `numeros.json` — `{"itbi": {"devido": true/false, "base": 0, "fundamento": ""}, "integralizacao_imovel": {"valor_recomendado": 0, "ganho_capital_pf": 0}, "pro_labore_minimo_recomendado_mensal": {"Marina": 0, "Felipe": 0, "Luana": 0}, "distribuicao_mensal_pretendida": 50000, "irrf_dividendos_2026_estimado_mensal": 0, "simples_possivel": true/false}`
3. `contrato_social_ajustado.md` — cláusulas corrigidas (capital, sócios, administração, não concorrência, preferência, avaliação de bens).
4. `checklist_registro.md`.
5. `PERGUNTAS.md` (opcional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
