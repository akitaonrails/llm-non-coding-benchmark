The client answered Q1 — and it changes the numbers materially. Let me recompute carefully.

Now I'll update the question log (recording the answers, not repeating them) and the status file.

One number in the risk section was computed with the old INSS base — let me recheck the revenue crossover.

The bisection confirms it: with the corrected CPP base, the crossover is **≈ R$ 4,674,134 — below the R$ 4.8 mi ceiling**. Fixing the stale figure in all four files.

All stale figures are gone (the one remaining "5,03" mention is the explicit correction note in R3) and `comparativo.json` re-validates. The engagement is closed out as **COMPLETE WITH OPEN ITEMS**.

## Closing answer to the partner's request

**1. Stay in Simples Nacional for 2026/2027 — migration would cost more, not less.**

| Regime (2026, receita R$ 4,2 mi) | Custo total | Carga efetiva |
|---|---:|---:|
| **Simples Nacional** | **R$ 916.500** | 21,8% |
| Lucro Presumido | R$ 1.009.620 (+93.120) | 24,0% |
| Lucro Real | R$ 1.010.790 (+94.290) | 24,1% |

The friend's "credita tudo" argument fails on the arithmetic: the PIS/COFINS credits the Real would give (R$ 83.250 on the R$ 900 mil of insumos that qualify under the library's rules) recover far less than the Real's own IRPJ/CSLL on the actual R$ 756 mil profit costs — and the Simples DAS already embeds R$ 225.090 of CPP, so leaving Simples *adds* R$ 68.910 of INSS patronal on top.

**2. "Sair em dezembro" é impossível.** A opção do Simples é anual e irretratável (LC 123, art. 16, §2º); a exclusão comunicada até o último dia útil de janeiro vale desde 1º/01 daquele ano (§2º-A). A janela de 2026 fechou em 30/01/2026. **Próxima opção: comunicar até 29/01/2027, com efeitos em 1º/01/2027** — e a opção pelo Presumido/Real se manifesta na DARF de janeiro (janela exata não está na biblioteca, sinalizado).

**3. The margin is thinner than it looks — three open facts could flip it** (all flagged, none assumed):
- **Q6 (decisive):** if the R$ 294 mil of INSS patronal would be fully incremental *and* deductible in the Real base, Real drops to R$ 910.830 — R$ 5.670 **below** Simples. Note the R$ 250 mil "encargos" line can't contain that CPP (28% × folha = 294 mil > 250 mil, and an Anexo III company pays no separate CPP per `inss_patronal.md`).
- **Q7:** if more than **31,7% of the R$ 1,050 mil payroll** works on obras, the Anexo IV CPP exposure (outside the DAS) makes Presumido cheaper.
- **Fator R:** pure payroll is **25,0%** of revenue, not the 31% the balancete claimed — Anexo V exposure (rule unverified; DAS tolerance ceiling R$ 831.120).

**4. Corrected warning on growth:** with payroll fixed, Simples stops being cheapest at **≈ R$ 4.674.134 de receita** — *below* the R$ 4,8 mi ceiling. So if 2027 revenue grows ~11%, the Presumido wins while the company is still eligible for Simples; the ceiling is not the binding constraint. (The earlier ≈5,03 mi figure was computed with the old INSS base and is corrected in R3.)

Deliverables in `workspace/deliverable/`: `comparativo.json` (schema-validated), `memorando.md` (rev. 2, full arithmetic + sensitivity tables A–D + risks R1–R7), `QUESTIONS.md`/`PERGUNTAS.md` (answered questions recorded, not re-asked; Q3–Q5 stay open as flagged unknowns), `STATUS.md`. Nothing was forced to reconcile — the ~R$ 744 mil profit gap and the obra-margin anomaly (R$ 700 mil insumos vs R$ 630 mil obra revenue) remain openly flagged.