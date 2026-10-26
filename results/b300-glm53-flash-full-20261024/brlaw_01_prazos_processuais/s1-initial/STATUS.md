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

## Questions to the client

None — all facts needed were in `documents/` (DJe dates, digital format, procurações). `QUESTIONS.md` not required.

## Open items / assumptions (none blocking)

1. Apelação date assumes **no embargos de declaração** are filed; should embargos be filed, the apelação deadline restarts (interruption, CPC art. 1.023/1.026 — `cpc_prazos_recursais.md`).
2. Disponibilização dates were read from the extracted text of the two DJe PDFs; recommend confirming in e-SAJ.
3. 25/01/2027 counted as a business day in Campinas per the calendar note (feriado municipal "APENAS na Capital").
4. No authority outside `library/INDEX.md` was used; everything else is marked as unverified/not cited.
