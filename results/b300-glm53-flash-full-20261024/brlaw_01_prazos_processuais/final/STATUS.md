# STATUS

**Engagement:** Ferreira & Lima Transportes Ltda. — prazos (7ª Vara Cível de Campinas, proc. 1044712-38.2026.8.26.0114)

`COMPLETE`

## Deliverables made

| File | Content |
|---|---|
| `deliverable/prazos.json` | Required schema for citacao and sentenca phases |
| `deliverable/memoria.md` | Day-by-day count with the legal ground for each rule, all cited to `library/INDEX.md` files |

## Results

- **Citation (DJe 19/11/2026):** publication 23/11/2026 · count starts 24/11/2026 · **contestação vencimento 15/12/2026** (terça-feira)
- **Sentence (DJe 10/12/2026):** publication 11/12/2026 · count starts 14/12/2026 · **embargos vencimento 18/12/2026** (sex) · **apelação vencimento 03/02/2027** (qua, recesso 20/12/2026–20/01/2027 suspended and skipped; 25/01/2027 counted as a business day in Campinas)

## Prazo em dobro

- O entendimento do sócio não se sustenta: o processo corre em **autos eletrônicos** e **CPC art. 229 §2** veda o dobro nesse caso (`cpc_prazos.md`). `prazo_em_dobro` = `false`.
- Nota contextual (art. 229): o caput pressupõe autos físicos; o §1º (com 2 réus, defesa por apenas um) é acessório aqui, já afastado pelo §2º — registrado na memória.

## Client follow-up (turno 2) — challenge to "no dobro"

- The client asked whether we are certain: opposing counsel ("experiente") guaranteed the double period per art. 229. **Answer: yes, no dobro** — the caput is expressly limited by §2º of the same article (`cpc_prazos.md`), and the case is indisputably electronic (DJe "PROCESSO ELETRÔNICO (e-SAJ)" in both DJe notices, `documents/intimacao_citacao_dje.pdf` and `documents/intimacao_sentenca_dje.pdf`, electronic case number, engagement contract). Documented in `memoria.md` §6.
- Opposing counsel likely reads only the caput; the §2º in the same article excludes electronic files.
- If any controversy on art. 229 §2º exists outside the library, it cannot be verified in this engagement — **UNVERIFIED, not cited** — and memoria §6.2 deliberately does not assert that one exists (the "dobro" claim is only a client-reported statement by opposing counsel).
- For risk framing only, the hypothetical dobro term was computed with the same calendar rules: 30 dias úteis from 24/11/2026 would end **05/02/2027** — **reference only, NOT legally supported**, absent from `prazos.json`, and must not be relied on (memoria §6.4).
- Risk asymmetry (memoria §6.3): with the library's count, the legal term stays 15/12/2026 even if we file before it; the only real risk is the opposite — relying on dobro and missing **15/12/2026**. (Consequences of a missed contestação are not stated in the library — flagged, not cited.)
- Recommended internal work targets (management, not legal terms): contestação draft by 05/12/2026, filing 08–11/12/2026, legal term 15/12/2026; apelação draft target 22/01/2027, legal term 03/02/2027 (memoria §6.5).

## Questions to the client

None — all facts needed were in `documents/` (DJe dates, digital format, procurações). `QUESTIONS.md` not required (including after the follow-up: the only dispute is legal, not factual — the electronic nature of the case is documented).

## Open items / assumptions (none blocking)

1. Apelação date assumes **no embargos de declaração** are filed. Should embargos be filed, the apelação prazo is **interrupted** — CPC art. 1.023, verbatim (`cpc_prazos_recursais.md`); the rule on when the count restarts is NOT in the library, so the new deadline cannot be precalculated from `library/` — monitor e-SAJ (memoria §3).
2. Disponibilização dates were read from the extracted text of the two DJe PDFs; recommend confirming in e-SAJ.
3. 25/01/2027 counted as a business day in Campinas per the calendar note (feriado municipal "APENAS na Capital").
4. No authority outside `library/INDEX.md` was used; everything else is marked as unverified/not cited.

## Final QA (pre-delivery)

- **Recount confirmed every date.** Fresh independent script (começo = data de publicação, excluído — art. 231, VII + art. 224 caput; `inicio_contagem` contado como dia 1 — art. 224 §3º / Lei 11.419 §4º; dias úteis art. 219; feriados 20/11 e 08/12; sem expediente 24/12; Natal 25/12; 01/01; recesso art. 220, 20/12–20/01 inclusive): contestação 15 úteis → **15/12/2026** · embargos 5 → **18/12/2026** · apelação 15 → **03/02/2027** (dias 1–5 = 14–18/12; 6–15 = 21/01→03/02) · dobro hipotético 30 → **05/02/2027** (reference only). Weekdays verified (19/11 qui, 20/11 sex feriado, 23/11 seg, 08/12 ter feriado, 25/01 seg).
- **A first QA script version double-excluded `inicio_contagem`** (treated it as the começo a excluir) and returned +1-business-day dates (16/12, 21/01, 04/02, 08/02) — script bug, corrected; the deliverables were right all along and no date changed.
- **Qué fixes were applied (memoria.md):**
  1. §3 — removed the unsupported restart-timing claim ("computado de novo a partir da intimação da decisão dos embargos"). The library's art. 1.023 gives the interrupção verbatim (with the cross-ref "(art. 1.026)"), but the rule on when the count restarts is NOT in the library; the new apelação date is now flagged as not precalculable from `library/`, with e-SAJ monitoring as the operational rule.
  2. §5 item 2 — aligned with the softened §3.
  3. §6.1 and §7 — both DJe PDFs now cited for the "PROCESSO ELETRÔNICO (e-SAJ)"/"Processo Digital" labels (previously only the citação PDF).
  4. §6.2 — garbled parenthetical rewritten; memoria no longer asserts that an external controversy exists; the "dobro" claim is attributed to the client's report and marked unverifiable.
  5. §6.3 — unsupported assertion "não há penalidade por agir antes do termo" removed (replaced with planning language: filing early does not change the calculated term); closing sentence rewritten (the library states no rule on the consequences of a missed contestação — flagged, not cited).
  6. §6.4 — weekend row 23–24/01/2027 added to the dobro table for completeness.
  7. §6.5 — duplicate "Monitorar e-SAJ"/"defesa da outra ré" rows merged into one.
- `prazos.json` untouched — schema-conformant, dates verified, arithmetic shown in its `fundamento` fields.
- Contract remark (moot): `CONTRACT.md` names the optional questions file `PERGUNTAS.md` at line 9 but refers to `QUESTIONS.md` elsewhere; neither applies — no questions were needed (see "Questions to the client" above).
