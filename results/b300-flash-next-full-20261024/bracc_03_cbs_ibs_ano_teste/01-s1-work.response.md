

The library rules are clear. Now let me examine all 17 NF-e XML files.





All documents and the library are read. The picture is clear. Now I'll compute the apuração-teste programmatically from the XMLs (Python/Decimal), applying the rates from the library (CBS 0.90%, IBS 0.10%, IBSMun 0.00% — NT 2025.002 / LC 214 art. 343).





Calculations verified and reconciled with the PIS/COFINS base (R$ 480.000,00). Let me verify the JSON, then write the guidance and status files.





JSON deliverable is in place and matches the contract schema. Now the orientation memo, questions and status files.





Engagement complete. All deliverables are in `deliverable/` (schema-validated, sums reconciled).

## What was found

The fiscal manager's belief ("nothing to do in 2026") is **wrong**: collection is waived (ADCT art. 125 §4º / LC 214 art. 343), but **only conditioned on meeting accessory obligations** — document highlighting, bookkeeping and the monthly test apuração.

**Test apuração — Aug/2026** (CBS 0.90% / IBS 0.10% per NT 2025.002; 12 sales NF-e, 5 purchases):
- Debits: CBS **4.320,00** + IBS **480,00** on R$ 480.000,00 of sales (ties exactly to the PIS/COFINS base)
- Credits: CBS **1.458,00** + IBS **162,00** (only NF-e 2314/2316/2317 — regular suppliers with highlight)
- Saldo-teste: CBS **2.862,00** / IBS **318,00** → **recolhimento devido: R$ 0,00** (waived; no PIS/COFINS offset since nothing is paid)

**4 irregular documents put the waiver at risk** (potential exposure R$ 3.180,00):
- **2308, 2310, 2312** — issued on/after 03/08/2026 **without the IBSCBS group** (CGIBS rejects these for regular-regime issuers; the SEFAZ rejections Paulo saw were correct, and "the system resumed issuing" produced the irregular ones)
- **2309** — rates **inverted** (highlighted IBS 0,90%/CBS 0,10%; correct: CBS 342,00 / IBS 38,00) — corrected in the test apuração

**Answers to Paulo's questions:** Simples/MEI customers **must** receive the highlight (it's the issuer's obligation, LC 214 art. 346 — the buyer's regime is irrelevant); the Ponto Fixo purchase (NF-e 2315) generates **no credit** (Simples: art. 347 — no highlight = no credit in 2026), and neither does NF-e 2313 (regular supplier without highlight).

**Files:** `apuracao_teste.json` (per-document status + motivo), `orientacao.md` (memo with arithmetic, library-only citations, assumptions flagged), `PERGUNTAS.md` (4 non-blocking confirmations: file completeness/tpAmb 2, which NF-e were rejected, supplier regimes, correction procedure), `STATUS.md` → **COMPLETE WITH OPEN ITEMS** (open: waiver-loss scope and 2026 correction procedure are not in the library — stated as such, not invented).