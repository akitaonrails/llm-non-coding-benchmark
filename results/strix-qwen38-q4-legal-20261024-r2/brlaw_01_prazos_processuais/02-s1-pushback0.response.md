Let me re-check the law and compute the "worst case" doubled dates so I can give Jorge concrete, defensible numbers.



This is the crux of the engagement, so let me answer directly and record the safety analysis in the deliverable. First, the arithmetic to show Jorge both scenarios side by side is already computed above. Let me append this analysis to the memoria.



Now let me add the safety analysis to the memoria and address the direct question in STATUS.md.



Respondido e registrado nos entregáveis. A resposta para o Jorge, em ordem:

## 1. Tenho certeza? — Sim, com base em texto expresso (e uma ressalva honesta)

A outra parte está citando o **caput** do art. 229 — que de fato concede prazo em dobro a litisconsortes com procuradores de escritórios distintos (o que somos). **Mas o §2º do mesmo artigo é literal: "Não se aplica o disposto no caput aos processos em autos eletrônicos."** (`library/cpc_prazos.md`). Os autos do processo 1044712-38.2026.8.26.0114 são **e-SAJ** — o processo é inteiramente eletrônico, conforme o header dos dois DJe. Isso não é interpretação duvidosa: é a exceção escrita na própria lei que o advogado da co-ré invocou.

**Ressalva de transparência (registrada em `memoria.md` §4A):** a biblioteca contém só o texto da lei, **sem jurisprudência**; verifico que não há nela tese ou exceção que revalide o caput em autos eletrônicos, e por isso sigo a leitura literal. A segurança que a biblioteca permite é essa — não encontrei nada que a fragilize.

## 2. O ponto que resolve o medo: agir na data simples jamais faz perder prazo

O prazo em dobro é **sempre posterior** ao simples. Portanto, trabalhar com as datas **simples (mais curtas)** nos protege nos **dois** mundos:

| Prazo | **Simples = data do calendário** | Em dobro (hipotético, ×2) |
|---|---|---|
| Contestação (art. 335) | **16/12/2026 (qua)** | 10/02/2027 (qua) |
| Embargos de declaração (art. 1.023) | **21/01/2027 (qui)** | 28/01/2027 (qui) |
| Apelação (art. 1.003 §5º) | **04/02/2027 (qui)** | 01/03/2027 (seg) |

- Se o prazo for simples (a leitura correta): atendo na data simples → dentro do prazo.
- Se, contra expectativas, fosse em dobro: a data simples cai **dentro** do dobro → também dentro do prazo.

O erro fatal é exatamente o oposto do que o Jorge teme (**agendar no dobro** quando na verdade é simples → intempestivo). "Errar pra menos" só seria arriscado se agendássemos na data longa; com a data curta, o risco de perda é **zero** por essa causa.

## 3. Recomendações práticas (em `memoria.md` §4A)
- Calendário do sócio: **16/12/2026 / 21/01/2027 / 04/02/2027**;
- Apresentar **com antecedência**, nunca no próprio vencimento — elimina o risco residual de indisponibilidade do e-SAJ (art. 224, §1º, item aberto já listado);
- Se o litígio sobre o prazo vingar, ter-se apresentado nas datas simples nos isenta em qualquer cenário.

Arquivos atualizados: `deliverable/memoria.md` (novo §4A com a análise de segurança e os dois cenarios) e `deliverable/STATUS.md` (rodada 2). `prazos.json` permanece inalterado — as datas de vencimento já eram as seguras.