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

- The client asked whether we are certain: opposing counsel ("experiente") guaranteed the double period per art. 229. **Answer: yes, no dobro** — the caput is expressly limited by §2º of the same article (`cpc_prazos.md`), and the case is indisputably electronic (DJe "PROCESSO ELETRÔNICO (e-SAJ)" in `documents/intimacao_citacao_dje.pdf`, electronic case number, engagement contract). Documented in `memoria.md` §6.
- Opposing counsel likely reads only the caput; the §2º in the same article excludes electronic files.
- A national controversy on art. 229 §2º exists outside the library — **UNVERIFIED, not cited** per engagement rules (memoria §6.2).
- For risk framing only, the hypothetical dobro term was computed with the same calendar rules: 30 dias úteis from 24/11/2026 would end **05/02/2027** — **reference only, NOT legally supported**, absent from `prazos.json`, and must not be relied on (memoria §6.4).
- Risk asymmetry explained: counting fewer days can never forfeit a deadline (filing early loses nothing legal); the only real risk is the opposite — relying on dobro and missing **15/12/2026**.
- Recommended internal work targets (management, not legal terms): contestação draft by 05/12/2026, filing 08–11/12/2026, legal term 15/12/2026; apelação draft target 22/01/2027, legal term 03/02/2027 (memoria §6.5).

## Questions to the client

None — all facts needed were in `documents/` (DJe dates, digital format, procurações). `QUESTIONS.md` not required (including after the follow-up: the only dispute is legal, not factual — the electronic nature of the case is documented).

## Open items / assumptions (none blocking)

1. Apelação date assumes **no embargos de declaração** are filed; should embargos be filed, the apelação deadline restarts (interruption, CPC art. 1.023/1.026 — `cpc_prazos_recursais.md`).
2. Disponibilização dates were read from the extracted text of the two DJe PDFs; recommend confirming in e-SAJ.
3. 25/01/2027 counted as a business day in Campinas per the calendar note (feriado municipal "APENAS na Capital").
4. No authority outside `library/INDEX.md` was used; everything else is marked as unverified/not cited.
