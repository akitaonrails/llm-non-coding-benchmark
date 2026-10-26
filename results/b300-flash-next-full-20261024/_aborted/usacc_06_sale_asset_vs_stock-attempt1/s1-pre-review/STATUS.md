# STATUS — Brightline Cabinetry offer comparison

## COMPLETE WITH OPEN ITEMS

All four deliverables are complete on the documented facts; the open items below are facts the client
could not supply (see `QUESTIONS.md`) and structural limitations of the closed library — none blocks the
recommendation, and each is priced or bounded in the analysis.

## Deliverables (`workspace/deliverable/`)

| File | Content | State |
|---|---|---|
| `comparison.json` | Full model: A drafted / A counter / A best-case / B / Ray's naive estimate, each with ordinary_income, capital_gain, entity_level_tax, total_tax, net_after_tax; comparison, breakevens, sensitivities | Complete; JSON validated; every figure traces to the verification script (all scenario assertions pass; gain invariant $2,720,000 holds) |
| `memo.md` | Character-by-character analysis with library authority, §1374 exposure, installment/PV analysis of B's note, liability comparison (Hardaway/warranty/escrows), head-to-head tables, recommendation and negotiating points | Complete |
| `form_8594_counter.md` | Proposed class allocation (III $200k / IV $140k / V $650k itemized per-asset / VI $100k target 0 / VII $2,010,000 residual) with justification, Exhibit A defect list, 8594 notes | Complete |
| `QUESTIONS.md` | Client-response register: Q2 answered (Hardaway $9,800 + unquantified warranty); Q1/Q3/Q4 client-unanswerable — fallbacks stated prominently, each with who can resolve and why it matters | Complete |

## Headline

At a 2026 close, **Buyer B's $2,850,000 stock sale nets more present value ($2,348,289) than Buyer A's
$3,100,000 asset sale in every allocation** — drafted ($2,190,601), counter ($2,285,801), or best case
($2,302,801). The two levers that flip it: closing after 12/31/2027 (worth **$149,499**; A-counter then
leads by ≈ $87,000) or price ≈ **$3.16–3.18M** on corrected classes. Ray's naive $2,480,000 overstates
A by **$289,399**.

## Open items (flagged, bounded, none blocking)

1. **AR accounting method (Q1)** — cash/$0-basis fallback used. Accrual cuts each A scenario's sale-year
   tax $74,000 and **flips counter-A past B's PV by ≈ $11,512** — the one fact that could change the
   recommendation at a 2026 close. CPA + last Form 1120-S.
2. **Closing-date decision (Q3)** — 2026 assumed; post-2027 alternative fully priced. Ray's call + buyer
   flexibility.
3. **NIIT / material participation (Q4)** — participation assumed (no NIIT); if wrong, ≈ $7,600 more
   against A. The 3.8% rate is **outside the library [unverified]**.
4. **Warranty exposure** — client says "nothing big I know of," unquantified; not modeled. Every $1
   retained under A costs $0.63 after tax; under B it transfers if disclosed.
5. **A assumed-payables amount (Q2 remainder)** — no schedule in file; $0 fallback. Each assumed dollar
   is residual-method consideration taxed at the marginal class rate; cannot plausibly move the ranking.
6. **B's $0 covenant** — low-probability IRS reallocation argument (economic-reality language in
   `library/irc_197_and_noncompete.md`); labeled, not modeled.
7. **B post-closing S-election termination** — buyer-side issue that can resurface as a PSA price
   argument; S-eligibility rules are outside the library; flagged, not analyzed.
8. **Texas franchise tax** — structure-dependent effects not analyzed; not in the library **[unverified]**.
9. **Conventions (labeled, immaterial here):** BIG entity tax offsets ordinary income first (never binds
   — ordinary margin ≥ $372,700 in every scenario); taxes paid in year income received; 6% PV discount
   (8/10/12/15% shown); seller-note credit risk priced only through the discount rate.

## Citation discipline

Every authority cited is a file in `workspace/library/` (INDEX closed set). Statements not supported by
the library are marked **[unverified — outside library]** or labeled as modeling conventions. No facts
were invented: where the file is silent (payables schedule, warranty quantum, accounting method, closing
date, participation), a fallback is used and stated prominently in all four deliverables.
