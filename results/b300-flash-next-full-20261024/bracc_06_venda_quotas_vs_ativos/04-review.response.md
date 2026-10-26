

I'll do a systematic self-review: re-verify all arithmetic, audit every citation against INDEX, and check the prose for unsupported claims or mistakes.






All errors confirmed. Applying the fixes now:







All fixes verified clean. Final consistency pass across the deliverable set:





Self-review complete. All arithmetic was independently re-derived in Python against the library's rates; every citation was audited against `workspace/library/INDEX.md`. Here is what the review found and changed:

## Errors found and fixed

**1. Arithmetic error in the IRRF alternative-reading delta (memorando §4.3, §8, STATUS item 7)** — the memo said the "tax the whole payment" reading of Lei 15.270 differs by **R$ 9,200**. Wrong: it's exactly 10% × 2 × R$ 50k = **R$ 10,000** (IRRF 705,600 vs 695,600; net 6,350,400 vs 6,360,400). Fixed in all three places.

**2. Wrong installment horizon (memorando §4.3)** — claimed stretching distributions to use the R$ 50k/month exemption "would take ~35 years." Actual: R$ 3.528.000 ÷ R$ 50.000 ≈ **71 monthly installments (~6 years) per partner** (~12 years if the cap is read per PJ-month). The conclusion (infeasible, and client already confirmed full 2026 cash-out) stands, but the number was off by 6×. Fixed.

**3. Unsupported figure in the ágio analysis (memorando §5)** — the potential goodwill under a Proposta A + incorporation read was stated as "R$ 7.5–8.4 mi" with no derivation. Correct estimate is **≈ R$ 6.9 mi** (R$ 9.0 mi paid − R$ 2.1 mi book equity, subject to the laudo). Replaced with the derived figure and its condition.

**4. New alternative reading added for completeness (memorando §4.3/§8, STATUS item 7)** — library wording "acima de R$ 50.000/mês **por PJ**" also supports a per-PJ-month cap reading: IRRF = R$ 700.600 (Δ R$ 5.000). Now flagged alongside the whole-payment reading; both immaterial.

**5. Grammar/typo fixes** — "na ajuste anual" → "no ajuste anual" (§4.3 and §8, two occurrences); "Dividir differently" → "Dividir de forma diferente" (QUESTIONS.md).

## Substantive additions (supportable, previously missing)

**6. Same-year aggregation caution (§3.2)** — the library rule "bens ou direitos da mesma natureza alienados em partes no mesmo ano são somados" (`lei13259_gcap.md`) wasn't flagged: if a sócio sells other same-nature assets in 2026, gains stack and the marginal bracket can reach 17,5%. Added as a caution.

**7. `comparativo.json` field-meaning note (§1)** — schema fields are ambiguous (e.g., `gcap_por_socio` is the **tax**, while `cronograma_darf` is per-sócio). Added a one-line reading key so the JSON can't be misparsed.

## What the audit confirmed clean

- **All core numbers reconcile** (re-verified fresh in Python): PF gain 3.9M/sócio → GCAP 585.000/sócio (585.000 = [234.000+3×117.000]); net 7.830.000. PJ: gain 7.5M → IRPJ 1.869.000 (1.125.000 + 744.000 adicional over the R$ 60k/trimestre, single-quarter assumption) + CSLL 675.000 → cash 7.056.000 → IRRF 695.600 → net 6.360.400; difference 1.469.600; break-even 0,594·P + 658.000 = 7.830.000 → R$ 12.074.074.
- **Citation audit passed**: every statute cited (Lei 8.981/95-art. 21/13.259, Lei 7.713/88 art. 21, Lei 9.430/96 art. 25-II, Lei 12.973/DL 1.598, Lei 15.270/2025, Lei 14.973/2024, Lei 8.137/90, CTN 149) is backed by an INDEX-listed file; nothing outside the library is cited; unverified items carry explicit flags.
- `comparativo.json` re-validated (schema, recommendation `pf`, `retificar_custo_dirpf: "nao"`, difference check).
- **No conclusion changed**: recommendation remains PF by R$ 1.469.600; STATUS remains **COMPLETE WITH OPEN ITEMS** (the open items are the client-unanswered unknowns, none of which moves the answer by more than R$ 10k).