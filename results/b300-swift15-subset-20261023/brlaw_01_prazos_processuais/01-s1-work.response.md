

I have the full picture now. Let me verify the workspace alias structure and run the date arithmetic in Python.






All calculations have been verified. Key finding: the case is a **Processo Digital (e-SAJ)** — an electronic record, and therefore, pursuant to CPC art. 229 §2º (which is in the library), the "double deadline" that the partner is claiming does **not apply**. Now I'll create the deliverable.





Engagement complete. All deliverables are in `workspace/deliverable/` (visible via the root `deliverable/` alias), validated and cross-checked in Python.

## Summary of findings

**The partner is wrong about the double deadline.** The case is a **Processo Digital (e-SAJ)** — electronic records — and CPC art. 229 §2º (in the library) expressly excludes double deadlines for electronic proceedings. The two-defendants/different-law-firms premise of the caput is present (Ribeiro & Castanho × Sampaio Advocacia), but §2º defeats it.

| Deadline | Publication | Counting starts | **Due** |
|---|---|---|---|
| Contestação (15 d.u., art. 335) | 23/11/2026 (20/11 is a holiday — Zumbi/Consciência Negra) | 24/11/2026 | **16/12/2026 (Wed)** |
| Embargos de declaração (5 d.u., art. 1.023) | 11/12/2026 | 14/12/2026 | **21/01/2027 (Thu)** |
| Apelação (15 d.u., art. 1.003 §5º) | 11/12/2026 | 14/12/2026 | **04/02/2027 (Thu)** |

Key calendar effects handled:
- **08/12/2026** — Campinas municipal holiday (N. Sra. da Conceição), skipped in the contestação count.
- **Recesso (art. 220)** — 21/12/2026 to 20/01/2027 inclusive suspends the count, pushing the 5th and 15th business days into January/February.
- **25/01/2027** — São Paulo's anniversary is a holiday *only in the capital*, **not** in Campinas, so it counts as a business day.
- **Caveat flagged in the memoria:** if embargos de declaração are filed by 21/01/2027, they interrupt the appeal period (arts. 1.023/1.026) and the apelação date restarts from the intimation of their judgment.

**Deliverables:**
- `deliverable/prazos.json` — all dates + `prazo_em_dobro: false` with full fundamento
- `deliverable/memoria.md` — day-by-day counts, rule-by-rule citations (all to `library/INDEX.md` files), arithmetic shown
- `deliverable/STATUS.md` — **COMPLETE** (no client questions were needed; all facts were in `documents/`)