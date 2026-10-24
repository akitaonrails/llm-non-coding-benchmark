# STATUS: COMPLETE WITH OPEN ITEMS

Deliverables entregues em `workspace/deliverable/`:

- `prazos.json` — datas-chave das duas intimações (conforme esquema do contrato)
- `memoria.md` — contagem dia a dia com fundamento de cada regra (seções 0–6)
- `QUESTIONS.md` — perguntas ao cliente (o `PERGUNTAS.md` opcional do contrato aponta para este arquivo)
- `STATUS.md` — este arquivo

Prazo em dobro: **não se aplica** (CPC art. 229, §2º — processo em autos eletrônicos/e-SAJ). A premissa do sócio está equivocada.

Datas para o calendário (Ferreira & Lima Transportes Ltda.) — válidas como contagem a partir das duas intimações fornecidas:

| Evento | Vencimento |
|---|---|
| Contestação (citação DJe 19/11/2026) | **15/12/2026 (terça)** |
| Embargos de declaração (sentença DJe 10/12/2026) | **18/12/2026 (sexta)** |
| Apelação | **03/02/2027 (quarta)** |

## Itens abertos (por que não COMPLETE)

1. **A sequência dos autos não fecha** (`memoria.md` §6): a intimação da sentença (disponibilização 10/12/2026) é **anterior** ao vencimento do prazo de contestação (15/12/2026), e os autos avançam de fls. 88 a fls. 212/219 em ~3 semanas. Não forçamos a reconciliação: as datas permanecem válidas *como contagem a partir das peças fornecidas*, mas se a sentença já alcança a Ferreira & Lima a contestação pode ter perdido utilidade prática (ou há defesa prévia, ou possível problema de citação — este último ponto **não verificável** com a biblioteca fechada). Pergunta 1 e 2 de `QUESTIONS.md`.
2. **Premissas declaradas** (`memoria.md` §4): (i) nenhuma indisponibilidade do DJe/e-SAJ nas janelas relevantes (art. 224, §1º) — perguntas 3; (ii) a intimação da sentença de 10/12/2026 alcançou a Ferreira & Lima — pergunta 2.

Se a Ferreira & Lima opuser embargos, o prazo de apelação **se interrompe** (art. 1.026, citado em `library/cpc_prazos_recursais.md`) e deve ser recalculado a partir do novo termo inicial, que não consta dos autos nem da biblioteca.

**Follow-up 23/10/2026:** sócio questionou o afastamento do prazo em dobro (CPC art. 229). Respondido na **seção 5 de `memoria.md`**: a confirmação está no próprio art. 229, §2º (biblioteca, *in force*) — autos eletrônicos (e-SAJ, conforme cabeçalho das duas intimações). As datas do calendário são as singelas, i.e., as mais conservadoras: mesmo que a tese do dobro estivesse certa, peticionar nessas datas não gera perda de prazo (margens embutidas: 52 dias na contestação; 23 dias na apelação). Datas hipotéticas do dobro (05/02/2027 e 26/02/2027) foram calculadas apenas como margem de referência e **não** devem ser usadas.

## Revisão pré-entrega (23/10/2026)

Contagens recomputadas por segunda implementação independente (datas, rótulos de dia da semana e tabelas conferidas item a item — tudo bateu). Auditoria de citações: todos os artigos citados constam da biblioteca; art. 1.026 existe apenas no corpo de `cpc_prazos_recursais.md` e é sempre atribuído a essa fonte. Correções aplicadas: (a) §3.2 — mecanismo de reabertura do prazo após embargos, que não está na biblioteca, foi reescrito e marcado como não verificado; (b) §5 — margem "7–8 semanas" corrigida para 52 dias (≈7,4 semanas, contestação) e 23 dias (≈3,3 semanas, apelação); (c) added §6 (nota de reconciliação) e `QUESTIONS.md`; (d) STATUS rebaixado de COMPLETE para **COMPLETE WITH OPEN ITEMS** pelo item aberto 1.
