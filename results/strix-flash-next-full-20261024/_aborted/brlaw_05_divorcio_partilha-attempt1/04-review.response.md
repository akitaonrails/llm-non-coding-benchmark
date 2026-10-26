Good discipline. I'll re-audit everything: every citation against `library/`, every number against the sources, and re-run reconciliation.

Now the two source documents cited in the deliverables — verifying the claims they support:

Now the four fixes in `proposta_acordo.md`:

All fixes are applied. Final step: re-validate both JSON files parse cleanly and the arithmetic still reconciles after the edits.

One check line in my quick script doesn't close — the torna reconciliation. I need to see the exact design arithmetic as stated in the files before trusting either version:

Everything re-validates: both JSONs parse, all row sums tie to TOTAL/DIVIDAS, the torna and the corrected totals close the whole pie, and the citation scan shows every authority used is in the library — `1.670` appears only where I flag it as **not** indexed. Audit complete.

## What I changed (7 fixes)

**Unsupported authority (worst category)**
1. **QUESTIONS.md item 1** — I had cited "CC 1.664" for the rule "a comunhão termina na separação de fato." The library's 1.664 excerpt says nothing of the kind (it only covers dívidas por encargos da família). Re-grounded in what the library actually says — FGTS partilhável = depósitos "durante a constância" (REsp 1.399.199) e quotas medidas "casamento → separação de fato" — and the general closing rule is now expressly labeled *regra de fundo não indexada, assumida*.
2. **Creditor consent for the mortgage** (partilha.json DIVIDAS, QUESTIONS item 10, proposta §3) — "assunção de dívida exige anuência do credor" is background law not in the library. Now labeled non-indexed/bancary practice assumed, everywhere it appears.
3. **Benfeitorias fundamento** (partilha.json + proposta §1) — CC 1.660 I / 1.664 were presented as if they directly supported the renovation credit. Now stated *inside the fundamento* as an analogical construction with no indexed rule (non liquet), which it is.

**Source/fact mismatches**
4. **Férias 32.000** (alimentos.json + proposta §5) — I had written "férias + terço constitucional"; the source says only "férias líquidas R$ 32.000" without discriminating the terço. Fixed wording (library's inclusion rule kept as a note). Numbers unchanged.
5. **Apartment registration** (partilha.json) — my wording implied it was registered in one name; the record says "ambos." Rewrote so the "ainda que só em nome de um" phrase is clearly the statutory rule, not a fact about this apartment.
6. **"Comprovado pelo depoimento"** (proposta §7) — the reforma cost is alleged by the client with receipts still pending; downgraded to "alegado pelo cliente (docs pendentes)." Same posture applied to the quotas row: the 1.5M laudo is *current* value, presumed to coincide with the (unknown) separação de facto date — now said explicitly.

**Arithmetic error — caught only on the final re-reconciliation**
7. **proposta §3, final totals** — "Marcelo 1.205.000 + 1.200.000 = **2.405.000**" double-counts the 120.000 benfeitorias credit: his common-side column includes that credit only because his *particular* estate is the debtor. Corrected to **2.285.000**, with the real cash-flow math shown: apto líq. 900.000 + FGTS 140.000 + quotas comuns 1.100.000 − torna 1.055.000 = 1.085.000 + particulares 1.200.000 = 2.285.000; bolo check 3.850.000 − 360.000 = 3.490.000 = Fernanda 1.205.000 + Marcelo 2.285.000 ✓. Fernanda's side and the torna (1.055.000) were already correct.

## What I verified and did **not** change
- Every citation (CC 1.658–1.664, 1.694/1.695/1.699, 1.583/1.584, Lei 13.058, REsp 1.399.199 / 1.595.775 / 1.698.774, REsp 1.332.808, Súmula 358, IN RFB 84/2001, Lei 10.705, ITCMD 4%/ITBI 3% SP) traces to the five library files.
- Formal de partilha: 620.000, registrado 11/2019 ✓; email: carro para ela "com a dívida", guarda compartilhada ✓.
- Alimentos math re-run: base 39.000/mês, anual 524.000, 25% = 9.750 + 6.000 (13º) + 8.000 (férias) ≈ 10.916,67/mês equivalência — unchanged.

`STATUS.md` stays **COMPLETE WITH OPEN ITEMS** (the 10 open items are unaffected — the corrections changed labels and one total, not the division design). Still pending your call on whether to create `NOTA_CLIENTE.md` for the "FGTS/empresa é particular, ponto final" objection.