# STATUS

**COMPLETE WITH OPEN ITEMS**

## Entregáveis (todos em `deliverable/`)
- `prazos.json` — criado; validado (JSON parse ok); datas confirmadas por script Python 3.
- `memoria.md` — contagem dia a dia com fundamentos (apenas arquivos de `library/INDEX.md`).
- `PERGUNTAS.md` — **não criada**: nenhum fato ausente exigiu pergunta ao cliente; as intimações,
  procurações e o e-mail do sócio estavam completos.

## Resultados
| Prazo | Vencimento |
|---|---|
| Contestação | **15/12/2026 (ter)** |
| Embargos de declaração | **18/12/2026 (sex)** |
| Apelação (sem embargos) | **03/02/2027 (qua)** |
| Prazo em dobro | **Não se aplica** — CPC art. 229, §2º (processo em autos eletrônicos/e-SAJ) |

## Itens abertos (não bloqueantes)
1. **Apelação condicionada a embargos:** se embargos de declaração forem interpostos (vencem em
   18/12/2026), o prazo de apelação é interrompido e reinicia com a publicação da sentença que os
   julgar (CPC arts. 1.023/1.026, na `library/cpc_prazos_recursais.md`). Termo inicial exato somente
   com a publicação no DJe dessa sentença. Referência bruta: 12/02/2027 (ver `memoria.md` §3.5).
2. **Alcance/jurisprudência do art. 229, §2º CPC** não constam da biblioteca; não há internet no
   ambiente. A conclusão de ausência de prazo em dobro segue o texto vigente tal como
   reproduzido na biblioteca — marcado como não verificado externamente. Mitigação: independentemente
   da interpretação, **entregar no prazo simples (curto) é tempestivo em qualquer cenário**; o risco
   só existiria se se esperasse o prazo em dobro (ver `memoria.md` §1.1).
3. **Expediente de 18/12/2026** (último dia útil antes do recesso): a biblioteca não registra
    comunicado de suspensão ou antecipação de expediente para essa data. Se houvesse, o art. 224,
    §1º CPC protrairia o vencimento dos embargos — hipótese aberta, não verificável aqui.

## Cálculos
Arithmetic executada via Python 3 (dois passes independentes, resultados idênticos): fins de semana,
feriados do calendário de `library/calendario_forense_campinas.md` (incluindo 20/11/2026, 08/12/2026,
24/12, 25/12, 31/12, 01/01, Carnaval 08–09/02/2027) e recesso 20/12/2026–20/01/2027 (32 dias, CPC
art. 220). Nada forçado a balancear; todos os dias contados estão listados na `memoria.md`.
