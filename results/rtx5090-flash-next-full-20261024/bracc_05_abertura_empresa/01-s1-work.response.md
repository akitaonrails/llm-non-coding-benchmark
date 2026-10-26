Now let me read the entire reference library — it's the only authority I may cite.

The library is fully mapped. Now let me run the arithmetic for the engagement (capital structure, pró-labore/INSS, 2026 dividend withholding, ITBI cap tests).

Let me fix a few encoding/typo glitches that slipped into the parecer.

Now the machine-readable numbers file (I'll generate it with Python to guarantee valid JSON):

Now the adjusted contract with corrected clauses:

Now the registration checklist and the client questions:

Final QA pass — verify all deliverables exist, JSON is valid, and every citation points to a file in `library/`:

Engagement complete. All deliverables are in `deliverable/`, every citation resolves to a file in `library/INDEX.md`, and the JSON validates against the required schema.

## What the engagement found

**Six blocking defects in the clients' plan:**

1. **Marina (federal public servant) cannot be administrator** — Lei 8.112 art. 117, X bars management of private companies; the exception permits her only as *cotista*. Clause 5 of the minuta is legally impossible.
2. **Community-property marriage (CC art. 977)** — Marina + Felipe cannot form the company "entre si ou com terceiros" while that regime persists. Resolution path (regime mutation vs. one-spouse risk) is flagged as the key client decision.
3. **Luana's "20% for work" is void** — service contributions are barred in a Ltda (CC art. 1.055 §2º). She must subscribe in cash: **R$ 142.500** against the corrected capital of **R$ 712.500** (150k + 420k + 142.5k).
4. **The 40% rental kills the Simples** — CNAE 6810-2/02 is an option impediment (LC 123 art. 17, XV) even without preponderance; the odontological CNAE also must go (no CRO technical head).
5. **Zero pró-labore is reclassified wholesale** — SC COSIT 120/2016 allows treating all R$ 600k/yr distributed to working partners as compensation. Recommended: Marina 0 / Felipe 10.000 / Luana 8.000 (labeled modeling assumptions; no legal floor in the library).
6. **The cash plan doesn't reconcile** — withdrawals of R$ 50k/month vs. average projected profit of R$ 35k/month (shortfall R$ 180k/yr before Luana's share); left open, not forced to balance.

**Tax positions (with arithmetic shown):** property contributed at **IR-declared value R$ 420.000** (Lei 9.249 art. 23) → capital gain **R$ 0** (market value would trigger R$ 480k gain); **ITBI not due** — immunity under CF 156 §2º I, fully within the share-capital cap (Theme 796/STF), rental share of 4.8–16.7% ≪ CTN art. 37's 50% threshold, with a 3-year monitoring covenant; **2026 dividend IRRF = R$ 0/month** (each partner at R$ 25k < R$ 50k/month, Lei 15.270), with the cliff effect on the full monthly amount flagged. `simples_possivel: false` reflects the plan as submitted — true only after the CNAE/property restructuring.

**Status:** `COMPLETE WITH OPEN ITEMS` — 6 questions logged in `deliverable/QUESTIONS.md` (regime de bens choice, rent value/owner, Luana's funds and credentials, other Simples companies, projection basis, non-compete scope) for the scripted client's next turn. Items unresolvable on the closed library (Simples × Lucro Presumido comparison, GC/ITBI rates, regime-mutation procedure) are explicitly labeled unverified rather than cited.