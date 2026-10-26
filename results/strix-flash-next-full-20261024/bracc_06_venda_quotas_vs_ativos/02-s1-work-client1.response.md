Now I'll integrate the round-2 answers into the memo. Starting with the header and facts table.

Now update §8 (item 2 revised for the ágio finding, plus new items 10–14) and fix cross-references:

The memo is now consistent. Next: restructure `QUESTIONS.md` (answered vs. converted-to-assumption, without re-asking):

Schema matches exactly. Now the round-2 rewrite of `STATUS.md`:

Read-through complete. This final pass fixed the last four defects and everything now checks out:

**Fixes in this pass**
- `memorando.md` §4.4 — new footnote ²: the R$ 50 mil/mês exemption is worded "**por PJ**" in `library/lei15270_dividendos_2026.md`, so the "1 vez pela PJ" row (IRRF 700.600) is the literal reading; the "2 fatias" row (695.600) is flagged as an interpretation **not verifiable in the library** worth only 5.000 more — irrelevant next to A's advantage.
- Earlier in this pass: typo "Fornecedor"→"fornecer" (§9), stale "dezenas de milhares" paragraph in §10 replaced by a pointer to the §9 register, §1 item 5 ref §8→§10, §3.3 table header now "Ganho tributado **por sócio**", "concentria"→"concentre", "Send P"→"Seja P", stale Q2/Q4 references re-pointed to §9 items 7 and 13.

**Verification results**
- Cross-references: all § targets exist; every "§9, item N" / "§8, item N" pointer matches the actual item (item 5 = garantias, item 7 = 50/50, item 10 = A a 9,6 mi, item 13 = ágio por escrito; §9 items 3, 7, 13, 16 as cited).
- Citations: the 6 files cited are exactly the 6 listed in `library/INDEX.md`; `Lei 14.973/2024 4%` and "não se admite atualização do custo" verified verbatim inside `lei7713_art21_parcelado.md`; Lei 8.137/90 + CTN 149 inside `crime_ordem_tributaria.md`.
- `comparativo.json`: schema keys/order exact per `CONTRACT.md`, 4 DARFs, all internal identities hold, A − B = 1.479.600.

**Final deliverable state** (`/work/workspace/deliverable/`)
| Arquivo | Estado |
|---|---|
| `comparativo.json` | validado, valores inalterados (recomendacao `pf`, retificar `nao`) |
| `memorando.md` | 508 linhas, §1–§11, sem referências órfãs |
| `QUESTIONS.md` | registro da rodada 2 — nada re-perguntado, premissas explícitas |
| `PERGUNTAS.md` | aponta para `QUESTIONS.md` |
| `STATUS.md` | **COMPLETE WITH OPEN ITEMS** |

O trabalho está fechado. O único fato capaz de inverter o ranking segue sinalizado: prejuízo fiscal/base negativa ≥ R$ 4.846.698 na Vértice (§9, item 10) — e a regra de compensação não está na biblioteca, portanto não foi assumida a favor da B.