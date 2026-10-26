Client responses received — two questions closed (de facto exclusivity; base composition claim), rest unknown. Let me compute the sensitivity scenario for the director's R$ 12,000 base claim before updating the deliverables.

The responses change two things: (1) the "de facto exclusivity" question closes — in a direction **adverse** to the company (the PJ had only Solaris as a client); (2) the Director's "R$ 12k CLT equivalent" is the library's defense argument on the base, but it is an assertion without proof. The sensitivity scenario has already been calculated (R$ 593,285 vs 889,928). Updating the deliverables now.

Now `parecer.json` — add the client-admission fundament and the sensitivity to the calculation notes (main figures unchanged, since the base claim is asserted but unproven):

Now append the sensitivity note to `_notas_calculo`:

JSON validates. Now rewrite `QUESTIONS.md` (answers received + remaining unknowns, no re-asked questions) and `STATUS.md`:

Let me re-read the contract to make sure STATUS.md uses the right vocabulary and format:

Final consistency check across the deliverables:

All deliverables are now updated and consistent. Summary of this round:

**Client responses incorporated (25/10/2026)**

1. **Exclusivity closed — against the company.** Carla confirmed Rafael was dedicated to Solaris for 7 years and his PJ had no other clients. This eliminates the "genuine entrepreneur with multiple clients" defense and reinforces non-eventuality/economic dependence (parecer.md §1, parecer.json `fundamentos`). Probability stays **alta (75%–85%)**.

2. **Director's "R$ 18k were full / CLT equivalent ≈ 12k"** — this is exactly the base defense admitted by the library (`verbas_e_calculo.md`), but it works only "**salvo prova**": the burden is on the company (art. 818) and the client has no documentation. Treated as an assertion, not proof. Added a quantified sensitivity (§5.1 in parecer.md and `_notas_calculo` in parecer.json):

| Base | 13º | Férias+⅓ | FGTS | Multa 40% | Aviso | INSS | HE est. | **Total** |
|---|---|---|---|---|---|---|---|---|
| 18.000 (presunção) | 87.750 | 117.000 | 100.620 | 40.248 | 30.600 | 352.170 | ≈161.540 | **≈ 889.928** |
| 12.000 (se provado) | 58.500 | 78.000 | 67.080 | 26.832 | 20.400 | 234.780 | ≈107.693 | **≈ 593.285** |

The base argument, if proven, is worth **R$ 296.643** — locating that documentation (PJ tax returns, cost records, proposals) is the highest-value action before any settlement or provision decision. Without it, the R$ 18.000 presumption holds: **provision stays R$ 890.000 (provável, CPC 25)** and settlement **R$ 500–800 mil** stays recommended.

**Files**
- `deliverable/parecer.md` — §1 (client admission), §5.1 (sensitivity with arithmetic), §6.3 (base defense + burden), §7 (answers + flagged unknowns).
- `deliverable/parecer.json` — new fundament on the client's admission; sensitivity appended to `_notas_calculo`; re-validated (`json.tool` OK).
- `deliverable/QUESTIONS.md` — rewritten: answers recorded, no question repeated; remaining items listed as explicit unknowns (rescission modality, headcount/Súmula 338, time sheets beyond jan–jun/2025, base documentation, NFs during absences, other PJs, governance/provision).
- `deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS**, listing the irreducible unknowns and declared non-library premises (220h divisor, 50% adicional, "≥15 dias" rule).