QUESTIONS.md e PERGUNTAS.md estão espelhados. Agora, atualizando o STATUS.md:

All five deliverables written. Final verification pass across every file:

A check has failed in the holiday list — inspecting the actual JSON content:

prazos.json está OK. A falha é outra falsa detecção do meu teste: `TODO` corresponde à palavra portuguesa "toDo**s**" dentro de `memoria.md`. Refazendo com detecção adequada de placeholder (`TODO:`/`{{`):

Bibliotecas OK. A falha do `conferir()` é apenas o cwd relativo — o módulo abre `library/...` em relação ao diretório de trabalho. Executando a partir de `/work`:

Entrega finalizada. Todos os cinco arquivos estão em `deliverable/` e passaram na verificação completa (JSON parse + schema, 97 pares data×dia‑da‑semana auditados por `conferir()`, sem placeholders, citações restritas aos 4 arquivos da biblioteca + INDEX).

## Respostas

**"Temos prazo em dobro?" — Não.** Há litisconsórcio com procuradores diversos (fls. 61 e 70), o que preencheria o art. 229, caput, mas o **art. 229, § 2º, CPC** afasta a regra "aos processos em autos eletrônicos" — e o processo é e‑SAJ. `prazo_em_dobro: false`. A hipótese de 30 dias (05/02/2027) ficou registrada apenas como controle rejeitado.

**Prazos calculados** (critério A — dia 1 = primeiro dia útil após a publicação):

| Marco | Disponibilização | Publicação | Início | Vencimento |
|---|---|---|---|---|
| Contestação (15 d. úteis) | 19/11/2026 | 23/11/2026 (20/11 é feriado) | 24/11/2026 | **15/12/2026 (ter)** — inclui‑se o feriado municipal de 08/12 |
| Embargos (5 dias) | 10/12/2026 | 11/12/2026 | 14/12/2026 | **18/12/2026 (sex)** |
| Apelação (15 d. úteis) | idem | idem | 14/12/2026 | **03/02/2027 (qua)** — recesso 20/12–20/01 suspende 23 dias; retomada 21/01 |

## Incógnitas sinalizadas (resposta do cliente: sem informações adicionais — perguntas não repetidas)

- **U1 — Certidão/AR de citação inexistente**: 15/12/2026 é a **data de trabalho segura**; certidão posterior empurraria o vencimento para mais tarde, anterior o anteciparia.
- **U2 — Telas de publicação e‑SAJ**: cadeia adotada é a que o próprio PDF invoca (art. 4º, § 3º, Lei 11.419/2006); risco residual ± 1 dia útil.
- **U3 — Embargos até 18/12/2026**: apelação de 03/02/2027 **só vale se não houver embargos tempestivos**; se opostos, os 15 dias recomeçam. Fronteira inferior teórica calculada: **apelação 15/02/2027**, com premissas rotuladas (4 dias úteis além da vigência da tabela de calendário; marco do art. 231 para intimação de julgamento fora da biblioteca).
- **U4 — Calendário após 09/02/2027**: irrelevante para as datas adotadas; só o cenário U3 exigiria novo extrato.
- **U5 — Feriados locais fora da tabela** (18/07, 11/08, 07/12/2026): **nenhum impacto** (07/12/2026 é domingo).

**STATUS: COMPLETE WITH OPEN ITEMS** — os itens em aberto são agora as incógnitas permanentes U1–U5, detalhadas em `QUESTIONS.md`/`PERGUNTAS.md` (idênticos) e `memoria.md` § 9.1, com a direção de impacto de cada uma. Nada foi reconciliado à força: o critério alternativo B (16/12, 21/01, 04/02) ficou apenas como contraprova no § 6.4 da memória.