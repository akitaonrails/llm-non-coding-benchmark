The PDF isn't readable directly, so I'll extract its text with Python.

The MSA PDF and markdown match, and there are no signature blocks in either. Now let me run the numbers.

Analysis is complete. Now I'll write the deliverables.

Engagement complete. Deliverables are in `/work/workspace/deliverable/`.

## What I did

Reviewed the GC's email, the RouteWise MSA v7.3 (all 3 pages, including Exhibits A–C), and the Cobalt playbook, checked every clause against rules A1–A5 and B1–B5, and validated the key readings against the three-library index (including extracting the playbook PDF's text, since PDF input isn't available to me).

## Findings — 6 issues (5 hard, 1 preferred)

1. **A1 (hard)** — §9.1's "NOTWITHSTANDING ANYTHING TO THE CONTRARY" cap swallows §10.1's "uncapped" IP indemnity. Per the interpretation library, "uncapped" elsewhere can't override a notwithstanding-cap unless the cap clause itself carves it out — and §9.3 doesn't. Effective cap ≈ $222,000 (12-month fees). Fixed via a carve-out inside §9.3 (plus conforming §10.1).
2. **A2 (hard)** — Exhibit C DPA is "[To be attached.]" with EU driver data going through the platform; per the Art. 28(3) excerpt, the controller is in breach from day one of processing. Signature blocker.
3. **A3 (hard)** — the mid-initial-term price increase and "greater of 8% or CPI" escalation live only in **Exhibit A ¶4** (the C1 order-form trap; §14.1 gives it priority). 8% × $222,000 = $17,760; playbook cap at CPI 3% = $6,660 — a $11,100/yr gap in that example (formulas shown, CPI not assumed).
4. **A5 (hard)** — Cobalt Freight Europe B.V. and Cobalt Brokerage LLC aren't covered by the license. Assumption flagged prominently; both playbook-compliant paths drafted; client question posted.
5. **A4 (hard)** — 24-month auto-renewal with a 90-day notice window (limits: 12 months / 30 days).
6. **B5 (preferred)** — SLA credits-as-sole-remedy with no chronic-failure termination right (credit ceiling $18,500 × 25% = $4,625/month).

Deliberately **not** raised: the 12-month cap, the mutual gross-negligence/fraud carve-outs, 30-day export, Delaware law/venue/jury waiver, and 15-day suspension notice — the playbook accepts those. The UCC Article 2 excerpt was reviewed and cited nowhere (it's a services agreement).

## Files
- `issues.json` — valid, ranked, only playbook-supported issues
- `redlines.md` — replacement text for all five hard-rule breaks + separated B5 redline
- `coo_onepager.md` — plain-English summary with the arithmetic
- `QUESTIONS.md` — 3 targeted questions (affiliate use, signature structure, DPA controller mapping)
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS** (affiliate facts and future CPI; all assumptions stated in the deliverables)