No comprovante file was added to `documents/` (noted as an open item). Re-verifying the numbers with the corrected payment date (30/04 → within the 12-month window):

Now updating memoria.md §2 (the Fator R section):

Now the §10 last bullet (the 06/05 question resolved) and the locação classification bullet in §4:

Now let me check the current state of `apuracao.json` and add a cross-reference in §1:

`apuracao.json` is consistent. Now rewriting `QUESTIONS.md` as a status record (answers received + remaining unknowns) and updating `STATUS.md`:

Final consistency pass — validating JSON, recomputing every number, and scanning for stale references:

All verifications pass. The engagement is now finalized after the client's second-round reply.

## What the client's reply changed (and didn't)

- **Pró-labore de abril — resolved.** Paid **30/04/2026**, not 06/05 (that was just the PIX being *lançado* in the accounting system). Since 30/04 falls inside the RBT12 window mai/2025–abr/2026, the R$ 3.200 **stays in the Fator R base**: folha 12m = R$ 284.600 → **Fator R 27,90% < 28%** → Anexo V, faixa 4 confirmed.
- **Locação à Orla — clarified, still open.** Confirmed the rental is ongoing "por uns meses" and that NF-e (not NFS-e) is the right document — consistent with **[LOCACAO]**/SV 31. But only the May NF-e 000.512 is in `documents/`, so whether prior months' rental revenue is inside `faturamento_12_meses.csv` remains unconfirmed.
- **DAS de maio/2026: R$ 15.188,84 — unchanged** (serviços 14.682,35 + locação 506,49).

## Files updated

- `deliverable/apuracao.json` — `folha_12m` 284.600,00 / `fator_r` 0,2790; JSON validated.
- `deliverable/memoria.md` — §2 rewritten (paid 30/04, in-window, robustness 25,49–27,90% all < 28%); §3 Fator R line corrected; §4 estorno reference fixed to NFS-e 1188 and locação paragraph now cites the ongoing rental; §9 premises recast as answered/partial/unresolved.
- `deliverable/QUESTIONS.md` — now a status record: 1 answered, 1 partial, 2 unanswered (client has nothing more to add), plus an index of the five remaining unknowns. No new questions sent, per instruction.
- `deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS**, with quantified open items:
  1. Locação months in RBT12 unconfirmed — sensitivity: if 2–6 months × R$ 6.000 were outside the CSV, DAS rises to at most **R$ 15.238,24** (+0,3%); annex/faixa don't change in any scenario;
  2. Anexo V repartição not in the library → `reparticao` left zeroed, unvalidated (no effect on the DAS total);
  3. Comprovante de 30/04 claimed by the client but absent from `documents/`;
  4. Month-by-month folha payment mapping impossible without older extracts (robust: Fator R 25,49–27,90% under every reading);
  5. Extrato `.pdf` illegible → `.csv` mirror used and reconciled.