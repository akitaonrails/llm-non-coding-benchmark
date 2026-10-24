I've reviewed the PDFs and confirmed the two notifications (citation published 11/19/2026, judgment published 12/10/2026). Now I'll compute the deadlines according to the forensic calendar.



I've verified the calculation and identified two critical issues: the "prazo em dobro (double time limit)" doesn't apply under CPC art. 229 §2º since this is an electronic case (e-SAJ), and the deadline for filing the appeal (apelação) crosses the judicial recess period (20/12–20/01), suspending the count. Now I'll draft the deliverables.



Fixing a typo in the JSON:



Now the memory file with the full day-by-day count:



I'm verifying the script output and found that the correct sequence for the apelação is 14–18/12, 21–22/01, 25–29/01, 01–03/02, with Carnival falling after the 15th day. I'll now write this as a clean, reproducible record.



Fixing two typos in the section I just wrote:



Now let me review the full memory file for consistency and check the JSON for typos:



Two small typos to fix (line 39 "tribunals", JSON "primerio"):



The quick cross-check script had a bug — I omitted the 20/11/2026 holiday from its set. Re-running with the complete holiday list from the calendar:



All figures reconcile with the independent script. Now the STATUS file:



Let me do a final verification of all deliverables:



Engagement complete. Summary of the work:

## Findings

**Key question — "prazo em dobro" (double deadlines): does NOT apply.** The two defendants do have lawyers from different firms (Ribeiro & Castanho × Sampaio Advocacia), which under CPC art. 229 caput would trigger double deadlines — **but art. 229, §2º expressly excludes electronic case files (autos eletrônicos)**, and this is a Processo Digital (e-SAJ). All deadlines are computed as simple (15 days / 5 days), based solely on the library texts.

## Calculated deadlines (all verified by independent Python passes)

| Event | Date |
|---|---|
| **Citation** — publication (1º dia útil after 19/11 provision; 20/11 is a holiday, 21–22/11 weekend) | 23/11/2026 (Mon) |
| **Answer (contestação)** — 15 business days from 24/11/2026, skipping weekends + 08/12 (municipal holiday) | **15/12/2026 (Tue)** |
| **Judgment** — publication (1º dia útil after 10/12 provision) | 11/12/2026 (Fri) |
| **Motion for clarification (embargos)** — 5 business days from 14/12/2026 | **18/12/2026 (Fri)** |
| **Appeal (apelação)** — 15 business days from 14/12/2026, **interrupted by the 12/20–01/20 recess** (CPC art. 220; 32 suspended days) → resumes 21/01/2027 | **03/02/2027 (Wed)** |

Notable call: **25/01/2027 was counted as a business day** — the library calendar lists it as a municipal holiday only in São Paulo Capital, not Campinas. The Carnival holidays (08–09/02/2027) fall after the 15th day and don't affect the appeal (they would affect the conditional scenario).

## Deliverables (in `workspace/deliverable/`)
- **`prazos.json`** — valid JSON, schema per contract, with legal basis
- **`memoria.md`** — day-by-day counts with the rule basis for each step (publication, commencement, business days, holidays, recess, double-deadline analysis); every citation points to a file in `library/INDEX.md`
- **`STATUS.md`** — `COMPLETE WITH OPEN ITEMS`: (1) if clarification motions are filed, the appeal clock resets upon publication of the ruling on them (exact date unknown yet); (2) case-law on art. 229 §2º not in the library — flagged as unverified; (3) no library record of a special court hours notice for 18/12/2026 — open assumption.
- **`PERGUNTAS.md`** — not needed; the client file (DJe notices, powers of attorney, partner's email) was complete, so no facts required asking.