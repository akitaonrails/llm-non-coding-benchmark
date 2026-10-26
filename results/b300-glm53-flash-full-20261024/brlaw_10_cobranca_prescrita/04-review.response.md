Full re-read done; arithmetic reconciles (81.990 + 2.200 + 110.000 = 194.190 ✓, per-parcela juros all check out at R$ 10/day per 30k). Found real text errors though — fixing them now.

Now fixing the remaining issues. First let me check the library text on Súmulas 299/503 so the analogy is phrased against what it actually says.

A biblioteca confirma: ela traz Súmula 299 (monitória sobre cheque prescrito) e Súmula 503 (prazo quinquenal contra emitente de cheque), mas **sem texto para contratos** — então a extensão ao nosso contrato é analógica e deve ser rotulada como tal. Agoraılacak todas as correções do memorando:

Quatro de cinco aplicações. A primeira falhou porque omiti os marcadores de negrito — tentando novamente com a substring exata:

Memorando concluído. Agora, as correções do `analise.json`:

One edit I just made introduced a typo ("pagelas") — catching and fixing it right away, then validating the JSON and checking STATUS/QUESTIONS:

JSON validates, and the grep sweep confirms no leftover instances of "allí", "aza", "Rapidinha", "iate", "estimate", the "'a" artifact, or "pag." anywhere in the deliverables. Quick spot-check of the edited regions:

Review pass complete — all fixes are in, JSON re-validates (`_JSON OK_), and no stray artifacts remain. Here is the full change list:

## What the review found and what I fixed

**memorando.md**
1. **§4 — garbled multa sentence** (was a confusing contradiction: "abandone a leitura mais favorável... verso registrado aqui"): replaced with the clean variant note — if the P1 multa fell on the integral of the original mora (2% × 30.000 = R$ 600), encargos rise **+R$ 200,00** (total R$ 194.390,00); the adopted reading ("abatido o pagamento parcial") is the one supported by the documents.
2. **§5 — typo**: "REsp 1.438.263 **allí** citado" (Spanish) → "**ali** citado".
3. **§5 — tone**: "Rapidinha" → sober wording ("por ser ágil, viabiliza execução provisória").
4. **§5 — unsupported-sounding authority**: "monitória é meio de exercício, como nas Súmulas 299/503" presented the analogy as if textual. The library only covers **cheques** (Súmula 299: monitória sobre cheque prescrito; 503: prazo quinquenal contra o emitente). Now labeled "**extensão analógica** — o acervo não traz texto expresso para contratos".
5. **§7 — substantive overstatement**: the acordo section implied the new recognition buys extra time. Added the alert: **acordo-reconhecimento não cria nova interrupção** (CC 202, once-only; slot consumed 15/09/2022), so the settlement calendar must close the quitação **before 15/09/2027** (the example does: ago/2027); novação as the stronger theory is flagged as **not in the library** → moved to open items in `QUESTIONS.md`.
6. **§9/§10 — non-Portuguese word "aza"** ×2 → "útil para a defesa" / "suporte defensivo".

**analise.json**
7. "(pag. 5 e 6)" → "(parcelas 5 e 6)".
8. "apos 15/09/2027 se nada **interromper novamente**" → corrected: a new interruption **cannot occur** (CC 202 once-only, used 15/09/2022); the inscription must then be excluded in full.
9. "(iate ~R$ 194 mil sem IPCA)" → "(total ~R$ 194.190 sem IPCA)".
10. "estimate" → "estimativa"; "reconhece 'a parcela 1" → "reconhece a parcela 1".
11. The 02/08/2023 e-mail now described accurately as **pagamento parcial (que também é reconhecimento)**, not as a second recognition e-mail; accents normalized; "5 dias úteis" for the Serasa correction flagged as a practical strategy deadline, not normative.
12. Transparency: I caught and fixed a typo of my own mid-fix ("pagelas" → "parcelas").

**No changes needed**
- **Arithmetic re-verified end-to-end**: juros 10.260 + 7.780 + 21.620 + 21.320 + 21.010 = **81.990**; multa **2.200**; 110.000 + 81.990 + 2.200 = **194.190,00** ✓; reconciliation 110.000 + 60.000 + 10.000 = 180.000 ✓.
- **QUESTIONS.md / STATUS.md** were already consistent with the fixed wording and the same open items (IPCA not computable — no series in the library; CNPJ/endereço unknown; Serasa correction to be executed by the client).

**Final status:** `STATUS.md` remains **COMPLETE WITH OPEN ITEMS**, as listed above.