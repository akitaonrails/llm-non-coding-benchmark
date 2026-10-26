

All math confirms the picture. Now writing the deliverables.





All checks pass. Writing the final status:





Engagement complete. Summary of what the file shows and what I concluded:

## The three "adjustments" — all rejected, each for a different reason

| Ask | Decision | Basis (library) |
|---|---|---|
| 1. Reverse R$ 1.2M labor provision ("lawyer now says remote") | **Maintain R$ 1,200,000** | The actual confirmation letter (18/12/2025) says *probable* for equiparação, merely *possible* for overtime — nothing says "remote". CPC 25 item 59: reversal only if outflow stops being probable; the expert opinion counts "as actually issued" |
| 2. Keep CCB Horizonte (due 31/08/2026) in long-term ("we always renew") | **Reclassify R$ 6.5M to current** | Renewal is "at the Creditor's sole discretion" (Clause 11) — no contractual right to defer; CPC 26 item 73: intent to refinance doesn't count |
| 3. AFAC R$ 2M "is capital, leave in equity" | **Reclassify to liabilities (shareholder loan)** | No capitalization in 3.75 years, no irrevocability/deadline → ITG 2000 / PN CST 17/84 treat it as a *mútuo*, triggering IOF-Crédito and presumed interest since Mar/2022 |

## The covenant doesn't survive the correct closing either

- **Management's math**: (9.8M + 1.2M reversal) → EBITDA 11.0M; DL 27.1M → **2.46** ✓ — but only because a probable obligation disappears from liabilities and enters profit; auditors would never let that pass.
- **Correct math**: EBITDA 9.8M (covenant explicitly computes "sem exclusão de provisões"); DL 31.2M − 4.1M = 27.1M → **2.77**, or **2.97** including the AFAC as debt — **breach in every reading** (max DL at 2.75 = 26.95M; excess R$ 150k–2.15M).
- **Consequence** (CPC 24): automatic acceleration of the debentures absent a waiver at balance-sheet date → debt to current liabilities + disclosure; a waiver/CCB addendum/AGE obtained in 2026 are non-adjusting events.

## Deliverables (in `deliverable/`)

- `classificacoes.json` — validated JSON in the contract's schema (`"cumprido": false`), with arithmetic and sensitivity both readings inside
- `nota_explicativa.md` — draft notes: contingencies, loans/maturities, AFAC, covenant, consequences
- `carta_diretoria.md` — refusal letter with the numbers plus a legitimate path forward (waiver with 75% debtholders, AGE to capitalize the AFAC, recalibrating the provision by legal thesis, liquidity plan)
- `QUESTIONS.md` / `PERGUNTAS.md` — 8 questions to the client (none blocking: the breach holds in every scenario)
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS** (detailed)

Notably, the CCB reclassification doesn't change the ratio (the definition sums current + non-current) — the breach is unavoidable honestly, which is why the letter pushes for a waiver rather than cosmetic accounting.