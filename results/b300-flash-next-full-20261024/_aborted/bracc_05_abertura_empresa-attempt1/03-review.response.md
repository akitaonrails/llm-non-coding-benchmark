

Now applying the audit fixes. Starting with `parecer.md`:






All edits are applied and re-verified. Here is the self-review result: what was wrong, what I changed, and what still needs the client.

## Errors found and fixed

**1. A number that didn't reconcile (the most serious one).** The plan pays out R$ 50.000/month (25k + 25k) but the projected profit is R$ 420.000/year — 50.000 × 12 = **600.000 > 420.000**, an excess of **R$ 180.000/year** that does not come from profit. Worse, the original plan was "pró-labore zero," so the payroll cost was likely never deducted: 420.000 − 96.000 (Luana's pró-labore) − 19.200 (20% patronal) = **R$ 304.800/ano ≈ 25.400/mês** distributable (80/20 → Felipe 243.840 / Luana 60.960). The deliverables previously stated "IRRF R$ 0" without flagging this. Fixed: `parecer.md` §4.2 now carries the full arithmetic and the sustainable-distribution ceiling (~25.4k–35k/month, not 50k); mirrored in `STATUS.md`, `checklist_registro.md` (as a ⚠ pre-payment reconciliation step) and `numeros.json` (`distribuicao_observacao`). I did **not** force the numbers to match — the R$ 420.000 base itself is now an open item.

**2. INSS stated as rates only, never computed.** Added: 11% × 8.000 = 880/month = **10.560/year** retained; 20% × 8.000 = 1.600/month = **19.200/year** patronal; total annual cost of the pró-labore **R$ 115.200** (96.000 + 19.200). The contribution ceiling is flagged as absent from the library. The old "25.000" figure is relabeled as a reclassification *illustration* (SC COSIT 120/2016), not a recommendation.

**3. Authority beyond the library / overreach in wording.** Four claims softened to what the cited texts actually say:
- CC 1.055 §2º clause is now "**vedada** / not registrable", not "nula" (the library gives the prohibition, not a nullity decree). Same correction in the checklist ("sem cláusulas vedadas").
- §1.4(c) now reads "recomenda-se que seja Felipe" rather than absolute impossibility, and the sub-rogação/comunhão point is labeled an **advertência, não conclusão** because CC arts. 1.667/1.668 are **not in the library** (added to all non-verified lists).
- §1.3/§1.1 administration/quotas wording aligned with the literal art. 977 and art. 117 X texts only.

**4. A check the Simples-alternative needed but lacked.** Added LC 123 art. 17 *caput* (PF sócia de **outra** optante / receita global somada) to `parecer.md` §3, checklist, STATUS, `numeros.json` (`simples_fundamento`) and QUESTIONS B.7 — quoting the library wording verbatim.

**5. A wrong fact in the checklist.** Outorga conjugal line said the property was from a "prior marriage"; the matrícula shows acquisition in **2016, inside the 2010 universal-communion marriage** → bem comum. Rewritten.

**6. Operational steps dressed as legal conclusions.** Junta procedures (FCN/DRE/CAP/REMP) and eSocial/EFD-Reinf are now explicitly labeled "não tratados na biblioteca — item operativo", since the library is silent on them.

**7. Missing annual-layer check on Lei 15.270.** Added the IRPFM reconciliation: Felipe 25.000 × 12 = 300.000 < 600.000 threshold; whether pró-labore enters the IRPFM base is **not in the library** → open item, not a conclusion.

Version bumped to **v2.1** with a note listing the audit additions; QUESTIONS gains **B.8** (profit base + sustainable withdrawal level).

## Verification passes
- Every cited file exists in `INDEX.md` (7 library files, nothing else cited); the art. 17 quotation matches `lc123_vedacoes.md` wording.
- All figures (304.800 / 25.400 / 243.840 / 60.960 / 115.200 / 19.200 / 10.560 / 180.000 / 7,41% / 1.296.000 / 525.000 / 105.000 / 480.000) recomputed in Python and consistent across all five files.
- `numeros.json` valid JSON, required schema keys unchanged (`itbi.devido=false`, `base=420000`, `pro_labore` {Marina 0, Felipe 0, Luana 8000}, `distribuicao=50000`, `irrf=0`, `simples_possivel=false`); explanation lives in added string fields only.
- Open-item count aligned: 7 in `parecer.md` §6, `STATUS.md` and `checklist_registro.md`.
- No leftover "nula" / "matrimônio anterior" phrasing; remaining "nulidade" hits are the explicit caveats themselves.

## Still needs the client (7 items, in `QUESTIONS.md` B)
1. Felipe's real role (passivo cotista × administrador — decides his pró-labore and who signs).
2. Luana's actual pró-labore (8.000/month is our assumption).
3. Fate of the R$ 150.000 Marina would contribute **and** of her R$ 25.000/month "lucro" (payment to a non-sócio is not a dividend).
4. Non-compete terms Luana accepts (validity itself is not sourced in the library).
5. Form of Luana's cash integralization and whether she is also administradora.
6. Informed regime choice now that renting inside this PJ kills Simples: (a) rent + Lucro Presumido, or (b) Simples without renting — plus the art. 17 *caput* check if (b).
7. Basis of the R$ 420.000 profit projection and the withdrawal level they actually want to sustain.

`STATUS.md` reads **COMPLETE WITH OPEN ITEMS**. Nothing to commit — the workspace is not a git repo, so all changes are plain file writes in `/work/workspace/deliverable/`.