# STATUS: COMPLETE WITH OPEN ITEMS

Engajamento: prazos — Ferreira & Lima Transportes Ltda. (7ª Vara Cível de Campinas, processo eletrônico).

## Entregáveis produzidos
- `prazos.json` — datas das duas intimações (disponibilização, publicação, início, vencimentos), prazo_em_dobro=false com fundamento, e feriados/suspensões considerados.
- `memoria.md` — contagem dia a dia com fundamento de cada regra (tudo citado de `library/INDEX.md`; nada de fora da biblioteca).
- `QUESTIONS.md` — registro de perguntas e respostas (2ª rodada): Q1 parcialmente respondida (a resposta não resolve a anomalia); Q2 e Q3 sem informação adicional do cliente — convertidas em premissa/condição sinalizadas, sem repetir perguntas já feitas. Nada altera as datas entregues.

## Resultado central
| Ato | Disponibilização | Publicação | Início | Vencimento |
|---|---|---|---|---|
| Citação → contestação (15 d) | 19/11/2026 | 23/11/2026 (20/11 é feriado — Lei 14.759/2023) | 24/11/2026 | **16/12/2026 (qua)** |
| Sentença → embargos (5 d) | 10/12/2026 | 11/12/2026 | 14/12/2026 | **21/01/2027 (qui)** — suspensão CPC art. 220 (20/12–20/01) |
| Sentença → apelação (15 d) | idem | idem | 14/12/2026 | **04/02/2027 (qui)** (sem embargos) |

- **Prazo em dobro: NÃO.** Art. 229, §2º, CPC: a dobra dos litisconsortes com procuradores de escritórios distintos (situação fática confirmada — fls. 61 e 70) não se aplica a autos eletrônicos; o feito é e-SAJ. A orientação ouvida do sócio estava errada. Reiterado na 2ª rodada (memoria.md, §0.1): o patrono da corré cita só o caput; o §2º do mesmo artigo (texto literal na biblioteca) afasta a dobra; e, de qualquer forma, as datas calculadas são as conservadoras — só há risco se a parte confiar na dobra inexistente.
- Ponto sensível tratado: 25/01/2027 (Aniversário de SP) é feriado só na Capital — computado como dia útil em Campinas.
- Alerta registrado: se opostos embargos tempestivamente, o prazo de apelação **recomeça** (art. 1.026) a partir da intimação da decisão — data não calculável hoje; fica como condição, não como pendência de informação.

## Itens abertos (por isso o status não é COMPLETE puro)
1. **Anomalia cronológica nos autos (memoria.md §4.1):** a sentença foi disponibilizada em 10/12/2026 e publicada em 11/12/2026 — 5 dias **antes** do vencimento do prazo de contestação (16/12/2026). Ou as rés contestaram antes de 10/12 (provável: a sentença condena "as rés" e há sucumbência recíproca), ou houve revelia/antecipação, ou alguma data está errada. Não há certidão de contestação nos documentos; **não forcei reconciliação**. Pergunta feita em `QUESTIONS.md`. Se as datas do DJe estiverem corretas, os vencimentos calculados não mudam. **2ª rodada:** o cliente respondeu apenas *"A Logística Campos vai contestar também, pelo que sei"* — relato indireto e no futuro, que não prova protocolo prévio e, ao pé da letra, **agrava** a anomalia; o cliente não tem mais dados. Item segue aberto (detalhes em memoria.md §4.1).
2. **Premissa (art. 224, §1º, CPC):** presume-se não ter havido indisponibilidade do DJe/e-SAJ nem expediente reduzido em 19/11, 23–24/11, 10–11/12/2026 e 14/12/2026 — nada nos autos indica o contrário; perguntado ao cliente. **2ª rodada: sem informação** — a premissa permanece como desconhecido sinalizado.
3. **Condição, não pendência:** se opostos tempestivamente, os embargos **interrompem** a apelação (art. 1.026) e o prazo recursal recomeça da intimação da decisão — a data 04/02/2027 vale apenas na hipótese de não opostos. **2ª rodada:** o cliente não informou decisão sobre embargos; recomendação: manter em calendário as duas datas (embargos 21/01/2027; apelação 04/02/2027 como plano B) e decidir os embargos até 21/01/2027.
4. Os documentos não comprovam a efetiva apresentação da contestação; o cálculo de 16/12/2026 é do prazo, não confirmação de cumprimento.

## Revisão final (esta rodada)
- Recálculo independente de todos os 10 marcos do `prazos.json` (script próprio lendo a tabela do calendário da biblioteca): **todas as datas conferem**; 0 rótulos de dia da semana incorretos em `memoria.md`/`STATUS.md`.
- Todas as citações verificadas contra `library/INDEX.md`; nada de fora da biblioteca.
- Correções feitas nesta revisão: alerta da §3 da memória reescrito (a versão anterior descrevia mal a ordem dos fatos); §4.1 nova (anomalia cronológica); ressalva nova sobre o excerto parcial do art. 231 na biblioteca (só a alínea VII); `QUESTIONS.md` criado; status alterado de COMPLETE para COMPLETE WITH OPEN ITEMS.

## Resposta do cliente (2ª rodada) — processada
- Respostas registradas em `QUESTIONS.md` e na memória (§§3, 4.1, 4.2). **Nenhuma data de `prazos.json` muda**: os prazos de embargos/apelação correm da intimação da sentença da própria Ferreira & Lima, independentemente da corré.
- Q1 parcialmente respondida (anomalia segue aberta, sem reconciliação forçada); Q2 e Q3 sem informação do cliente (viram premissa/condição sinalizadas). Perguntas já respondidas não foram repetidas.
- Desconhecidos restantes, sinalizados explicitamente: (a) efetivo protocolo e data das contestações e eventual revelia; (b) disponibilidade do DJe/e-SAJ nas datas-chave (premissa do art. 224 §1º); (c) decisão sobre embargos até 21/01/2027.
