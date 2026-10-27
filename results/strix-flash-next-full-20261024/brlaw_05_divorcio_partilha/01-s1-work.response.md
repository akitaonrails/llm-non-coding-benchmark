I've read the contract, the case file, and the entire library. This is a Brazilian divorce case (partial community property regime / *comunhão parcial*), and I need to analyze Fernanda's proposal and present a settlement proposal. I'll verify all the calculations in Python first, then produce the deliverables.

All deliverables validate and cross-check. Writing the status file:

Engajamento concluído. Todos os entregáveis estão em `deliverable/` (`partilha.json`, `alimentos.json`, `proposta_acordo.md`, `QUESTIONS.md`, `PERGUNTAS.md`, `STATUS.md` = **COMPLETE WITH OPEN ITEMS**), com todos os números conferidos por script e as somas fechando.

**Resultados-chave**

| | R$ |
|---|---:|
| Patrimônio bruto / dívidas / líquido | 3.850.000 / 360.000 / 3.490.000 |
| Total partilhável (comum líquido) | **2.290.000** → meação de cada: **1.145.000** |
| Equalização: Marcelo paga a Fernanda | **995.000** (450k apto + 70k FGTS + 550k quotas, −30k carro −45k PGBL retidos por ela) |

- **Atibaia (800k): bem particular** — herdada em 2019 (CC 1.659, I + formal de partilha). A pretensão de metade da casa é infundada.
- **Quotas: bem misto** — quotas particulares (2011), mas a valorização da constância (1.500.000 − 400.000 = 1.100.000) comunica: Fernanda recebe **550.000 por apuração de haveres, sem entrar na sociedade** (REsp 1.595.775).
- **FGTS (140k) é partilhável** (REsp 1.399.199) — a proposta dela abre mão disso; entra na equalização mesmo assim.
- **PGBL dela (90k) foi omitido da proposta dela** — também é partilhável: 45.000 para Marcelo.
- **Alimentos:** rejeitados os 30% sobre o bruto+FGTS+rescisórias. Base correta = líquidos (salário 24k + 13º + férias = 28.666,67/mês; FGTS e verbas indenizatórias fora). Sugerido **25% = 7.166,67/mês**.
- **Guarda:** unilateral rejeitada — compartilhada é a regra legal (CC 1.584, §2º); residência de referência materna com alimentos pagos por Marcelo.
- **Tributos:** partilha equalizada = sem excesso de meação (sem ITCMD/ITBI por excesso); bens escriturados pelos valores de declaração para evitar ganho de capital (IN 84/2001).

**Abertos** (listados em `STATUS.md` e perguntados em `QUESTIONS.md`): data da separação de fato, valores de declaração de IR, pró-labore/PLR, liquidez para a equalização, e 2 pontos marcados como NÃO VERIFICADOS na biblioteca (valorização natural de Atibaia; base do ITBI na compensação em dinheiro).