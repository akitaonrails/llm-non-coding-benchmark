

I've reviewed all source documents and library authorities. Now I'll verify the dates with Python before drafting the deliverables.





Calculation verified. Let me check whether the root-level alias paths exist, as the user mentioned.





Aliases confirmed. Now I'll write the three deliverables.





I wrote to the wrong absolute path (`/workspace` instead of `/work/workspace`). Let me check and fix.





All deliverables are in place and the JSON validates. Engagement complete.

## Resumo

**Pergunta do sócio — prazo em dobro: NÃO.** Embora os dois réus tenham procuradores de escritórios distintos (requisito do art. 229, caput, CPC), o **§ 2º** do mesmo artigo exclui a contagem em dobro para **processos em autos eletrônicos** — e este processo é digital (e-SAJ), conforme o cabeçalho das intimações do DJe. A informação do advogado da Logística Campos não procede.

**Datas calculadas** (somente dias úteis — CPC art. 219; publicação no 1º dia útil seguinte à disponibilização — Lei 11.419/2006 art. 4º §3º e CPC art. 224 §2º; início no 1º dia útil seguinte à publicação; exclui-se o dia do começo e inclui-se o do vencimento):

| Prazo | Disponibilização | Publicação | Início | Vencimento |
|---|---|---|---|---|
| Contestação (15 dias, art. 335) | 19/11/2026 | 23/11/2026 | 24/11/2026 | **16/12/2026 (qua)** |
| Embargos de declaração (5 dias, art. 1.023) | 10/12/2026 | 11/12/2026 | 14/12/2026 | **21/01/2027 (qui)** |
| Apelação (15 dias, art. 1.003 §5º) | — | — | — | **04/02/2027 (qui)** * |

*Pressupõe que não forem opostos embargos; se opostos, o prazo da apelação é interrompido (art. 1.026).

**Pontos-chave da contagem:**
- 20/11/2026 era feriado (Zumbi/Consciência Negra, Lei 14.759/2023), o que empurrou a publicação da citação para 23/11; 08/12/2026 (N. Sra. da Conceição, feriado municipal de Campinas) caiu no meio da contagem da contestação.
- O recesso (20/12/2026–20/01/2027, art. 220 CPC) suspendeu os prazos da sentença, que retomarão em 21/01/2027. O 25/01/2027 (Aniversário de SP) **não** é feriado em Campinas e foi contado.
- A contestação (16/12) antecede o recesso e não foi afetada por ele.

**Entregáveis** em `workspace/deliverable/`:
- `prazos.json` — schema do contrato, com fundamento completo em cada bloco
- `memoria.md` — contagem dia a dia, cada regra com a citação do arquivo correspondente em `library/INDEX.md`
- `STATUS.md` — **COMPLETE** (sem `PERGUNTAS.md`: nenhum fato necessário estava ausente)

Cálculos verificados em Python 3; dias da semana conferem com as intimações do DJe e com o calendário da biblioteca.