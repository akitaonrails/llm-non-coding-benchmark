All four deliverables and the source documents are re-verified. Now backing up and applying the audit fixes.

Backups are in place. Now I'll re-pull the exact strings for each edit target to make precise replacements.

Exact strings confirmed. Let me verify where the 65/35 weights are actually defined (§12.4 vs §12.3) before fixing those cross-references.

`STATUS.md` read. Now applying all remaining fixes across the four files in one batch — each targets a distinct, unique string.

Item 10 confirmed verbatim. Now appending the audit close-out note to `STATUS.md`.

Now the final validation battery: JSON parse + schema key match against CONTRACT.md, and stale-reference greps.

Top-level keys match. Let me verify nested keys/types against the template and check the CONTRACT.md wording on schema exactness.

Auditoria complete and all fixes applied. Here is the close-out report.

## What I audited

- **Arithmetic** — re-derived every number: 84 NFs × R$ 18.000 = 1.512.000; totals 722.424 / 738.992 / 882.583; base-12k scenarios 481.616 / 492.661 / 588.389 and floor 434.613; EV 652.776,15 × 0,85–0,95 = 554.860–620.137; nov/2021 boundary +11.928; resignation alternative −70.504 / −47.003; INSS band 232–349 mil; 51-day aviso (the library itself sets "30 + 3/ano completo, máx. 90" — Lei 12.506). **All core numbers verified correct.**
- **Authority** — every citation checked verbatim against the 7 files in `library/` (Res. 121/2003, Tema 608/ARE 709.212, Lei 14.905 wording, Súmulas 338/212, the three Tema 1.389 questions, "exigível pela RFB"). No cancelled Súmula 256 / OJ 191 invoked as current; unverified items (divisor 220, DSR/Súmula 171, art. 461, INSS administrative deadlines, Lei 14.905 rates) remain labeled as unverified.
- **Documents** — 135 HE hours (jan–jun/2025), 9.0–9.8 h/day logs, Slack/e-mail dates, 30/09/2026 notice, contract clauses 1–7 re-read via `pdftotext -layout`.
- **Schema** — `parecer.json` parses; all keys required by CONTRACT.md line 6 present with correct types; `verbas sum == total == 722.424`; 58 + 26 = 84.

## What I changed (10 fixes — no central number moved)

| # | File | Fix |
|---|------|-----|
| 1 | parecer.md:3 | "duas vezes" → **"três vezes"** (three revision rounds, not two) |
| 2 | parecer.md §6:84 | late-filing sensitivity: "~35 meses" → **~36 meses** (out/2023–set/2026, by the same month-boundary convention used throughout) |
| 3 | parecer.md §9:133 | "encargos §§ 5–8" → **"encargos do §8"** (correção/honorários/multas live only in §8) |
| 4 | parecer.md §12.3:178 | comparison-table column "(§6)" → **(§7)** (§6 is prescrição; the 722.424 figures are §7) |
| 5 | parecer.md §12.3:184 | divisor note "como no §6" → **"como no §7"** |
| 6 | parecer.md §10:142 | closed the per-R$1.000 savings math: added the **aviso-prévio scaling** (51 days × 1.000/30 ≈ 1.700) so 662,67 × 6 × 58 = 230.608 + 10.200 = **240.808** — exactly the table's 722.424 − 481.616 |
| 7 | parecer.md §10:138 | vague "≈65–80% do cenário mediano" → **exact ratios**: 67,7%–87,9% of 738.992 (56,7%–73,7% of 882.583) |
| 8 | parecer.md ×2 + parecer.json | weights 65/35 referenced "item 12.3" → **item 12.4**, where they are actually defined (0,65 × 738.992 + 0,35 × 492.661) |
| 9 | QUESTIONS.md:1 | header "rodada 3" → **"rodada 4"** (file now contains the round-4 item 10) |
| 10 | STATUS.md | QUESTIONS.md description aligned to rodada 4 (incl. the ARE 1.532.603 monitoring item); "três respostas" → "três rodadas de respostas" |

Plus: **STATUS.md now discloses** the four `obs` fields in `parecer.json` as transparency annotations *in addition to* the required schema (kept — they carry material caveats such as "remuneracao_base já paga, não reembolsável"), and a new **"Auditoria final de pré-entrega"** section records the audit itself.

Pre-audit backups are at `/tmp/opencode/*.bak2` if you want to diff or revert.

## Delivery status

**COMPLETE WITH OPEN ITEMS** — all four deliverables in `workspace/deliverable/` are internally reconciled (md ↔ json ↔ questions ↔ status) and every authority traces to the frozen library. The open items remain what the client could not answer (cause of termination, vacation records 2021–2024, timesheets outside 1H2025, employee headcount vs. Súmula 338, price-composition proof for the "18 mil cheios" thesis, CLT-peer benefits, RFB audit exposure, and the still-pending Tema 1.389 merit). Headline numbers unchanged and defensible: **vínculo alta (85%–95%)**, exposure **722.424 / 738.992 / 882.583**, provision **provável, R$ 740.000**, settlement band **R$ 500.000–650.000**.