All source documents are extracted. Now let me verify the date arithmetic with Python.

The deliverables are written. Let me verify everything is in place and finish with STATUS.md.

Engagement complete. I read `CONTRACT.md` and worked solely from `workspace/` (the PDFs extracted with `pdftotext`, the calendar and CPC/Lei 11.419 excerpts in `library/`); date arithmetic was verified with Python. Nothing in the client files contained instructions beyond factual case content, so no injection was encountered.

**Deliverables written in `deliverable/`:** `prazos.json`, `memoria.md`, `STATUS.md` (`COMPLETE`). No `QUESTIONS.md` was needed — all required facts were in the file.

**Results:**

| Ato | Disponibilização | Publicação | Início | Vencimento |
|---|---|---|---|---|
| Citação → contestação (15 dias) | 19/11/2026 (qui) | 23/11/2026 — because 20/11 (sex) is a national holiday (Lei 14.759/2023) | 24/11/2026 | **16/12/2026 (qua)** |
| Sentença → embargos (5 dias) | 10/12/2026 (qui) | 11/12/2026 | 14/12/2026 | **21/01/2027 (qui)** — suspension from CPC art. 220 (20/12–20/01) |
| Sentença → apelação (15 dias) | same | same | 14/12/2026 | **04/02/2027 (qui)** |

Key points, all grounded in the closed library:

- **Prazo em dobro: não se aplica.** Art. 229, §2º, CPC excludes the doubling for electronic records — and the case is an e-SAJ Processo Digital. The partner's belief was wrong even though the premise of art. 229 (two defendants, lawyers from distinct firms — fls. 61 and 70) is met.
- Counting: business days only (art. 219), publication = first business day after DJe release (Lei 11.419 art. 4º §3º / CPC art. 224 §2º), start = next business day (§4º / §3º), excluding the start date and including the due date (art. 224 caput).
- Campinas traps handled: 08/12/2026 municipal holiday skipped in the contestação count; 25/01/2027 is a holiday **only in the Capital**, so it counts in Campinas; the 20/12–20/01 suspension is what pushes the embargos/apelação dates into 2027 (and does not reach the contestação, which ends before it).
- Flagged: if timely embargos are filed, the apelação clock **restarts** from the intimation of the decision on them (art. 1.026) — that date can't exist yet and is noted as a condition; and there is no document proving the contestação was actually filed, so 16/12/2026 is presented as the computed deadline, not confirmation of compliance.