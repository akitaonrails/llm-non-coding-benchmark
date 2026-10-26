All files are read. Now I'll verify the arithmetic with Python and cross-check the documents before building the deliverables.

JSON deliverable is written and valid. Now the guidance document (`orientacao.md`):

Now the client questions and status files:

Final verification of all deliverables:

Engagement complete. Summary of what was delivered in `deliverable/`:

**`apuracao_teste.json`** — test calculation for August/2026 (schema-validated, arithmetic done in Python):
- **Debits** (12 sales, base R$ 480,000 — reconciles with the PIS/COFINS base of the normal calculation): CBS 480,000 × 0.9% = **4,320.00**; IBS × 0.1% = **480.00** (LC 214/2025, art. 343)
- **Credits** (only from entries with highlight from the regular regime, art. 346): NF-e 2314/2316/2317 → CBS **1,458.00**, IBS **162.00**; 2313 (regular without highlight) and 2315 (Simples, art. 347) → zero credit
- **Balances**: CBS 2,862.00 | IBS 318.00 · **Due payment: R$ 0.00**, conditioned on the ancillary obligations (ADCT art. 125, §4º)
- **4 irregular documents**: 2308, 2310 and 2312 (issued after 03/08 without the `IBSCBS` group — rejection and loss of waiver) and 2309 (inverted rates: pIBSUF 0.90/pCBS 0.10 against the 0.10/0.90 of NT 2025.002; debits recorded corrected)

**`orientacao.md`** — objective response to the manager: "there is nothing to do" is wrong — it does not pay **provided** it highlights, records and calculates (art. 346 and ADCT §4º; the CGIBS notice warns that there is no penalty in 2026, but there is loss of the waiver); sales to Simples/MEI **yes, they require highlight** from 03/08 (the obligation is of the regular-regime issuer, art. 347 only exempts the Simples/MEI as issuer); entry from Ponto Fixo (Simples) **generates no credit** in 2026; there is nothing to offset against PIS/COFINS while the waiver holds; documents from 01–02/08 without the group remain valid.

**`QUESTIONS.md`** — real factual gaps: which two notes were rejected (all 17 XMLs are authorized but in homologation, `tpAmb=2` — reconciliation explicitly left open), whether there were reissues, portfolio completeness and the regularization instrument (not in the library, treated as unverified, not cited from memory).

**`STATUS.md`** — `COMPLETE WITH OPEN ITEMS`, with the five open items listed.