Client answers received — Q1/Q2/Q3 resolved (with significant consequences), Q4 remains structurally implied, Q5–Q9 unanswered. Let me re-read the current deliverables to update them precisely.

Continuing from the checkpoint: parecer.md is fully updated. Next per plan: `numeros.json`, `contrato_social_ajustado.md`, `checklist_registro.md`, `QUESTIONS.md`/`PERGUNTAS.md`, `STATUS.md`. Reading the full current contents first.

All current contents confirmed. Now applying updates: first `numeros.json` (full rewrite) and the first half of `contrato_social_ajustado.md` edits.

First half applied. Now reading the full `contrato_social_ajustado.md` to get exact text for the remaining clauses (6ª, 7ª, 10ª, 11ª):

Exact texts confirmed. Applying the four remaining clause edits:

All 9 contract clauses done. One consistency fix: cláusula 2ª still excludes 6810-2/02 from the object, but with the Simples definitively out, it is now a registrable secondary CNAE. Then reading `checklist_registro.md` in full:

Contract fully adjusted. Now applying all `checklist_registro.md` edits:

Fase 3 and Fase 4 edits:

Checklist done. Now rewriting `QUESTIONS.md` (canonical) and `STATUS.md`:

Both files written. Running QA: sync `PERGUNTAS.md`, validate JSON, check arithmetic, and scan for garbles:

All QA checks pass. Final consistency sweep for stale/phased-out mentions:

Turn complete. All deliverables now incorporate the client's answers from 25/10/2026, and QA passed.

## What was done this round

**`contrato_social_ajustado.md`** — finished the remaining edits:
- **Cláusula 6ª**: pró-labore só para Felipe (R$ 1.518, piso a confirmar — Q5); Luana remunerada como contratada, fora do contrato [forma UNVERIFIED].
- **Cláusula 7ª**: distribuição restrita a sócios (integralidade ao sócio único), gatilho de R$ 50 mil/mês com capacidade de R$ 35 mil (margem R$ 15 mil); pagamentos a não-sócios fora do escopo [UNVERIFIED — Q10].
- **Cláusula 10ª**: locação dos ≈ 40% ao dentista, R$ 8.000/mês = R$ 96.000/ano = **7,41%** (96.000 ÷ 1.296.000), folga 6,75× no limite de 50%, controle por 3 anos; Simples definitivamente descartado; sem serviços vinculados (Q12).
- **Cláusulas 2ª e 11ª**: 6810-2/02 passa a **CNAE secundário registrável** (a vedação permanece registrada como nota); assinaturas = Felipe (sócio) + Marina (cônjuge consentente); Luana **não assina**.

**`checklist_registro.md`** — Fase 0 reescrita com Q1–Q4 resolvidos `[x]` e Q6 aberto; Fases 1–4 ajustadas (Marina cônjuge consentente sem qualidade de sócia; Luana contratada; 6810-2/02 secundário; controle de ITBI quantificado; pró-labore só Felipe — INSS 166,98 / patronal 303,60; gatilho 2026 com margem; dentista locatário ≠ responsável técnico).

**`QUESTIONS.md` / `PERGUNTAS.md`** — reescritas: Q1–Q4 respondidas (respostas transcritas + definições), Q5–Q9 em aberto (Q8 com nota de escopo reduzido), **Q10–Q12 novas** (renda da Marina via PJ; condições da contratação da Luana; exceção ISS para o Simples). `diff` confirmou cópia idêntica.

**`STATUS.md`** — mantém **COMPLETE WITH OPEN ITEMS**; estrutura definitiva no bloco de citação; 8 open items listados; tabela de entregáveis atualizada.

## QA
- `numeros.json`: `json.load` OK (10 chaves).
- Aritmética verificada por script: 7,41% · 6,75× · 15.000 · 42,9% · 166,98 · 303,60 · 2.003,76 · 3.643,20 · 570.000. ✔️
- Sem garbles, sem resquícios de "se sócia"/"excluir 6810-2/02"/"25+25 como plano válido".

Nenhuma pergunta já respondida foi repetida. Aguardando próxima interação — pendências ativas: **Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12**.