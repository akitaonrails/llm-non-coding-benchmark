Both intimations extracted. Now let me set up the calculation with the library's calendar rules.

All dates computed. Let me emit the JSON deliverable programmatically so the numbers are auditable.

Now let me fix one inaccurate figure in the JSON and generate the day-by-day tables for the memo.

This is the crux: I must pin down exactly which day counts as day 1. Let me re-read the library's rules and re-model the count.

O ambiente reverteu meu workspace para um instantâneo anterior (~06:12) — os arquivos posteriores desapareceram. Tenho todo o conteúdo; vou escrevê-lo novamente em um único passo e verificar a persistência.

Encontrei um bug real: converti incorretamente o feriado local de Campinas em 8 de dezembro em 8 de agosto. Corrigindo isso:

25/01/2027 é, de fato, um feriado estadual de SP (tabela do TJSP) — a apelação vence em 04/02. Agora corrigindo a verificação da janela:

Todas as verificações de aritmética passam. Números finais no critério adotado (A): contestação **15/12/2026**, embargos **18/12/2026**, apelação **04/02/2027**. Agora escrevendo o gerador de entregáveis:

Ajuste importante: a tabela diz que 25/01/2027 é feriado **apenas na capital, não em Campinas**. Corrigindo o conjunto de feriados exatamente conforme a biblioteca:

O patch por índice corrompeu o arquivo. Reescrevendo o mecanismo do zero e de forma limpa:

Trabalho concluído. Todos os entregáveis estão em `deliverable/` e validados (datas×dia-da-semana conferidas por script, JSON no schema do contrato, apenas as 4 fontes da biblioteca citadas).

## Resposta ao sócio: **não, não temos prazo em dobro**

Há dois réus com procuradores de escritórios distintos (fls. 61 — Ribeiro & Castanho; fls. 70 — Sampaio Advocacia), o que preencheria o art. 229, *caput*, do CPC. Só que o **art. 229, § 2º** (texto na biblioteca) diz: *"Não se aplica o disposto no caput aos processos em autos eletrônicos"* — e o processo é eletrônico (e‑SAJ, cabeçalho de ambas as intimações). Logo: **15 dias úteis** de contestação, não 30.

## Datas (contagem dia a dia na memória)

| Ato | Disponibilização | Publicação | Início | Vencimento |
|---|---|---|---|---|
| Contestação (15 d) | 19/11/2026 (qui) | 23/11/2026 — 20/11 é feriado (Zumbi) | 24/11/2026 | **15/12/2026 (ter)** — feriado municipal de 08/12 não computado |
| Embargos (5 d) | 10/12/2026 (qui) | 11/12/2026 (sex) | 14/12/2026 | **18/12/2026 (sex)** — véspera do recesso |
| Apelação (15 d) | idem | idem | 14/12/2026 | **03/02/2027 (qua)** — recesso 20/12–20/01 suspenso (art. 220), retomada 21/01; só vale se **não** houver embargos tempestivos (art. 1.026 interrompe) |

A hipótese do dobro (30 dias → 05/02/2027) foi calculada só como contraprova e está registrada como **rejeitada**.

## Arquivos

- `deliverable/prazos.json` — schema do contrato, `prazo_em_dobro: false`, 23 dias suspensos do recesso listados
- `deliverable/memoria.md` — contagem dia a dia com fundamento de cada regra (arts. 219, 220, 224 §§2º‑3º, 229 §2º, 231 VII, 335 III, 1.003 §5º, 1.023; Lei 11.419 art. 4º §§3º‑4º; calendário de Campinas), conferências aritméticas (23 = 1+15+1+6; 55 = 1+15+23+16) e armadilhas (20/11, 08/12, 25/01 só na Capital)
- `deliverable/QUESTIONS.md` (+ espelho `PERGUNTAS.md`) — 5 perguntas: certidão/AR de citação inexistente nos autos (premissa declarada), datas de publicação do e‑SAJ não impressas, intenção de embargos, calendário após 09/02/2027, feriados locais fora da tabela
- `deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS** (os itens acima)

Armazenado em memória: a pergunta do sócio já foi respondida.