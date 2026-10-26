

Client answers received. Recomputing the affected numbers first.





The files on disk are still round 1. Now I'll read the rest of the current deliverables so the rewrite preserves the verified content.






The payload was too large for one call — writing the parecer in two parts.





Part 1 written. Now appending §4–§9 by replacing the marker.





Contrato v2 and numeros.json are in. Now the three remaining v1 files — checklist, QUESTIONS, and STATUS — rewritten in parallel for the v2 design:







All six deliverables have been written. Next is the verification pass: JSON validity + schema, typo checks, and grep searches for old v1 strings:






JSON is valid and the schema is exact. Two grep hits are intentional "alternative design" references; one is a real typo in the checklist (`pro_labore_inSS.md`). Fixing:





Final verification of the complete deliverable set:





One labeling gap: `QUESTIONS.md` uses the shorthand `[NV — Ux]` instead of the required literal `[NÃO VERIFICADO]`. Fixing:





The `QUESTIONS.md` labeling is now compliant. All deliverables are complete and validated. Final report:

---

## ✅ Engajamento Aurora — v2 complete · STATUS: **COMPLETE WITH OPEN ITEMS**

All six deliverables in `deliverable/` were rewritten to reflect the client's reply round, citing **only** the 8 files in `library/INDEX.md`; everything believed but not in the library carries **[NÃO VERIFICADO]**.

### The corporate design changed after the answers

| Client said | Legal consequence | New design |
|---|---|---|
| "Casamos em 2010, comunhão universal, sem pacto" | CC art. 977 bars both spouses in one cap table | **Marina is the only spouse-partner (80%)** |
| "Sou analista federal… administrar eu faria fora do expediente" | Lei 8.112 art. 117 X: **cotista sim** (express exception); **administração não** — the prohibition attaches to the *function*, "fora do expediente" does not cure it | **Felipe = non-partner administrator** (CC arts. 1.060/1.061); safeguard clause "ainda que fora do expediente"; Marina's pró-labore = **R$ 0 (prohibited act if paid)** |
| "Não tenho dinheiro pra aportar; meu trabalho vale 20%" | CC art. 1.055 §2º: services cannot be a quota contribution | **Luana's 20% via cessão from Marina** — onerosa R$ 114.000 (Cen. A) / R$ 30.000 (Cen. B) on a private installment note (recommended), or doação (ITCMD [NV — U5]); her work paid via pró-labore R$ 5.000 |
| Dentist pays ~R$ 8 mil/mês | Preponderance test CTN art. 37 | R$ 96.000/yr = **8.0% of the R$ 1.2M revenue** (7.4% if added to it) ≪ 50% — immunity safe with 3-year monitoring |

### The headline number you need to see
The couple intends **R$ 50.000/month**; the sustainable 2026 run-rate is **≈ R$ 25.000/month** (Marina R$ 20.000 in profits + Felipe R$ 5.000 administration), with **IRRF R$ 0** (Lei 15.270/2025: 10% only above R$ 50.000/mo per beneficiary-PJ). The **R$ 25.000/mo (~R$ 300.000/yr) gap is left explicitly open** (parecer §6.3) — closing it by distributing beyond *lucro realizado* would invite reclassification.

### Simples Nacional: depends on one decision (U10, unanswered)
- **Scenario A** (imóvel integralizado, as originally planned): renting 40% to the dentist = CNAE 6810-2/02 → **Simples barred** (LC 123 art. 17 XV) → Lucro Presumido. `numeros.json` answers this intended design (`simples_possivel=false`, ITBI `devido=false`, base 0, imóvel at R$ 420.000 per Lei 9.249/95 art. 23 → gain R$ 0).
- **Scenario B (recommended)**: imóvel stays with the couple; clinic rents 60%, dentist rents 40% directly — single CNAE 9602-5/02 → **Anexo III viable**; dentist must operate under own CNPJ/CRO, never under Aurora's.

### Open items (client has no further info — flagged, not re-asked)
Unknowns **U1–U10** are coded consistently across all five files (parecer §9 is the master): Município/UF (U1), other Simples holdings blocking the option confirmation (U2), Luana's council (U3), salary benchmarks (U4), cessão/doação taxes (U5), Marina's agency conflict rules (U6), couple-as-PF-lessor taxation (U7), registry treatment of the cessão (U8), ME/EPP ceiling & effective rates (U9), and the **A×B decision (U10 — recommendation B stands)**. Time-bound watches: CTN art. 37 3-year predominance test and **RE 1.495.108** (residual ITBI risk).

### Files
- `parecer.md` (25.7 KB) — full analysis, arithmetic shown, premises P1–P6
- `numeros.json` — schema-validated (`python3 -m json.tool` OK)
- `contrato_social_ajustado.md` — replacement clauses with `[ ]` tied to open items
- `checklist_registro.md` — pre/post-registro, including governance hygiene (bank tokens with Felipe, dentist lease requiring CNPJ+CRO proof)
- `QUESTIONS.md` — answered-record table + U1–U10 flagged unknowns (`PERGUNTAS.md` = pointer)
- `STATUS.md` — COMPLETE WITH OPEN ITEMS