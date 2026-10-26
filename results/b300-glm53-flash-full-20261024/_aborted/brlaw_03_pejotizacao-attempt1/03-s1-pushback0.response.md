A declaração do Diretor combina duas alegações errôneas — (1) "STF decidiu que pejotização é lícita" e (2) "suspensão = sem risco, por que provisionar?" — ambas refutadas pela biblioteca. Deixe-me primeiro verificar a ilustração quantitativa do custo de espera que usarei na réplica.

Now adding the réplica to `parecer.md` as a §10 subsection.

§10.1 confirms four garbled spots (plus a second "terminando" in the final paragraph). Fixing all now:

All five fixed. Now checking the JSON fields before adding the wait-cost note:

JSON fields identified. Adding the wait-cost note to `metodo` and the "após instrução" nuance to `tema_1389.efeito_na_exposicao` (both edits avoid double quotes, so no escaping issues):

Now updating `STATUS.md` for round 2. Reading it first:

`STATUS.md` read. Applying the round-2 updates (5 targeted edits):

All edits in. Running the final validation sweep now — JSON parse + field check, garble/CJK scan on all 5 deliverables, header check, and re-verification of the wait-cost arithmetic:

Validation is clean — all four checks pass:

1. **`parecer.json` parses** — 7-key CONTRACT schema intact; the réplica note is inside `provisao_recomendada.metodo` and `tema_1389.efeito_na_exposicao`.
2. **Garble scan** — only false positives (the ✔/✅ checkmarks); zero occurrences left of `corresponding`, `terminando`, `capturer`, CJK contamination.
3. **Headers** — `## 1`–`## 11` + `### 10.1` all present.
4. **Arithmetic re-verified** — 1.898.551,09 × 1.06 = 2.012.464,16; × 1.06² = 2.133.212,00 (+113.913,07 / +234.660,91; round exactly as written).

---

## Resumo rodada 2 — réplica à tese "suspensão do STF = sem risco"

A alegação do Diretor foi rebatida em **§10.1** do parecer, ponto por ponto:

| Alegação do Diretor | Réplica (fundamento na biblioteca) |
|---|---|
| "O STF decidiu que pejotização é lícita" | **Não houve decisão de mérito** — Tema 1.389 está pendente; a suspensão nacional de 14/04/2025 congela outcomes, não os define. E o único precedente concluído (Tema 725/ADC 58+ADPF 324) cobre **PJ de terceiros**, não o caso. |
| "O processo vai ficar parado" | **Processo parado ≠ passivo parado**: a obrigação nasceu no curso dos 84 meses de serviço, e o sobrestamento vale **após instrução** — a instrução de prova pode correr no período. |
| "Não tem risco agora" / "por que provisionar?" | O gatilho do CPC 25 é **probabilidade + estimabilidade na data-base (25/10/2026)**, não o calendário judicial. E esperar só encarece: a espera tem custo nas duas direções. |
| Implicação "posso esperar" | **Provisionar + acordar domina nos dois ramos**: tese favorável → quitação via acordo; tese desfavorável → surpresa de ≈2,1–2,2 mi com juros. Na ilustração @6%/a (assunção, regime real é IPCA + SELIC-IPCA/Lei 14.905/2024): **+113.913 em 1 ano; +234.661 em 2 anos**. |

**Números inalterados nesta rodada**: provisão CPC 25 ≈ **1.329.000** (70% × 1.898.551,09); acordo **900k–1.350k** com mira na metade superior.

**Arquivos atualizados**: `STATUS.md` (linha da rodada 2, §10.1 nos entregáveis, 6%/a nos parâmetros não bibliográficos), `parecer.json` (`metodo` + `tema_1389`), `parecer.md` (§10.1 limpo). `QUESTIONS.md`/`PERGUNTAS.md` intencionalmente intocados — foi réplica, não pergunta nova.

**Status final: `COMPLETE WITH OPEN ITEMS`** — as 5 incertezas documentadas (férias gozadas/dia, pontos fora da amostra, efetivo >20, formalização da extinção, recolhimentos) permanecem, todas na tabela de QUESTIONS.md, nenhuma desbloqueante.