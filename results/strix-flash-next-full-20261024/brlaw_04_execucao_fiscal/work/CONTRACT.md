# Engajamento: Execução Fiscal 5001234-56.2026.4.03.6182 — Marmoraria Pedra Viva Ltda. (cinco sessões)

Citação em 2026-09-14. A Fazenda executa R$ 1.100.000,00 (IRPJ/CSLL 3T/2020 a 2T/2021). Nas sessões
seguintes a Fazenda emenda a CDA e pede redirecionamento à ex-sócia. Sem internet; só a biblioteca.

## Sessão 1 (`deliverable/sessao1/`)
1. `analise.json` — `{"periodos": [{"periodo": "", "regra_decadencial": "CTN 150 §4º|CTN 173 I", "limite": "AAAA-MM-DD", "decaido": true/false, "valor": 0}], "valor_decaido": 0, "valor_remanescente": 0, "vicios_formais": ["..."], "veiculo": "exceção de pré-executividade|embargos", "por_que": ""}`; 2. `peca.md`.
## Sessão 2 (`deliverable/sessao2/`)
3. `manifestacao.md` — resposta à emenda e à tese da Fazenda sobre decadência.
## Sessões 3 e 4 (`deliverable/sessao3/`, `deliverable/sessao4/`)
4. `analise_redirecionamento.json` — `{"socio_pedido": "", "requisitos_435": "", "tema_962": "", "tema_981": "", "dissolucao_irregular_configurada": true/false, "socio_que_responderia_se_configurada": "", "conclusao": ""}`; 5. `defesa_redirecionamento.md` e `carta_aos_socios.md`.
## Sessão 5 (`deliverable/sessao5/`)
6. `garantia.json` — `{"valor_remanescente_atualizado": 0, "seguro_garantia": {"valor_garantido": 0, "custo_anual": 0}, "fianca": {"valor_garantido": 0, "custo_anual": 0}, "transacao": {"base": 0, "desconto_estimado": 0, "observacao": ""}, "recomendacao": ""}`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
