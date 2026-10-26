# STATUS

**COMPLETE WITH OPEN ITEMS** (all three sessions delivered; open items pending client answers)

## Deliverables in place

`deliverable/session1/`:
- `response_to_cfo.md` — written answers to the CFO email (Mesa February invoice — no, with
  §549(a)/§363(b) + DIP order ¶2 + Dkt. 48 analysis and the lawful fast path; netting — no, DIP
  order ¶3; Holland & Pierce $140k — no, §§330/331) plus the 2026-03-20 addendum declining the
  "call it a deposit" relabel and documenting the lawful alternative.
- `march_mor.json` — Parts 1/2/5/7 in the contract's shape (ending cash null pending Q1).
- `segregation.csv` — all ten invoices classified pre-/post-petition with authority.
- `march_mor_notes.md` — arithmetic and classification rules (companion).

`deliverable/session2/`:
- `april_mor.json` — Parts 1/2/5/7 in the contract's shape (ending cash null pending Q1).
- `professional_fees.md` — payability per professional under Dkt. 77: H&P $116,200 payable,
  $28,000 holdback; Corbin $0 payable until it serves the fee/expense split and the
  pre-/post-retention allocation (day-count placeholder flagged as assumption only).
- `april_mor_notes.md` — arithmetic and component build-up for Part 2 (companion).

`deliverable/session3/`:
- `cod_schedule.json` — contract shape. Discharged at the 9/30/2026 effective date: $5,460,000
  (= allowed GUC $8,400,000 − 35% plan recovery $2,940,000, undiscounted "balance discharged on
  the effective date" per the term sheet). COD income $5,460,000, excluded in full under
  26 U.S.C. §108(a)(1)(A) (library: irc_108.md). Attribute reduction under §108(b)(1): NOL
  $6,100,000 → $640,000; nothing left for attributes (B)–(G); fixed-asset basis $3,200,000
  preserved. §108(b)(5) election **declined** with reasoning (the default order fully absorbs the
  exclusion in the NOL; electing would wipe out all $3,200,000 of basis and — at best — swap
  certain near-term depreciation deductions for NOL of equal face amount; where the $2,260,000
  remainder would go once basis is exhausted is not covered by the library).
- `fresh_start.md` — ASC 852 two-part test: prong (a) **met** ($14,000,000 reorg value <
  $16,200,000 post-petition liabilities + allowed claims); prong (b) **not met** (old equity
  retains 60% of reorganized equity — treated as voting shares; ≥ 50%). Both required → **no
  fresh-start reporting**.
  Consequences applied: plan payables at present value of amounts to be paid; gain on discharge
  as a reorganization item in the income statement; no asset restatement or goodwill; LSTC
  presented separately during the case.
- `emergence_balance_sheet.md` — presentation of the discharged debt and the gain: LSTC
  $8,400,000 derecognized against plan payables $2,940,000 (undiscounted placeholder pending
  Q13) and gain $5,460,000 inside reorganization items (final = $8,400,000 − PV, so the gain
  rises as the payables fall); DIP repaid → exit facility recorded at its own terms; tax overlay
  pointer to the §108 schedule.

## Open items (QUESTIONS.md; none answered yet)

Sessions 1–2 (Q1–Q12, unchanged): ending cash (swept balance + $2,241,330; if H&P was paid in
April, +$2,125,130); UST fee base ($3,926.16 accrual is an estimate); H&P pre-3/10 services;
pre-petition liabilities beyond the documented $74,110 trades (Part 2 completeness); Apex
written trade terms (Dkt. 48 condition); 3/13 payroll pre-/post-petition split; March register
completeness; whether H&P's $116,200 was disbursed late April (would change Part 5, ending cash,
and Part 2); Corbin allocation and objection status (no Corbin payment allowed until served);
April register / Mesa $18,900 status / April payroll periods (Part 2 is a build-up pending
this); April DIP financing costs.

Session 3 (Q13–Q15, new):
- **Q13** — GUC installment calendar (incl. the first installment due on the 9/30 effective date,
  and confirmation it was paid) and discount rate → plan payables restated to PV (below
  $2,940,000) and the final gain (above $5,460,000);
  also current/long-term classification of the plan payables.
- **Q14** — 2026 discharge-year NOL, completeness of the §108(b) attribute list, and tax rates →
  finality of the attribute schedule and the tax footnote.
- **Q15** — exit financing principal/terms, final DIP payoff incl. fees, 9/30 asset carrying
  values, and the DIP-fee amount settled in the 40% equity issuance → needed only if a full
  pro-forma balance sheet is wanted beyond the discharge/gain presentation CONTRACT.md asks for.

## Conventions and honesty notes

- Tax measurement of the discharge uses undiscounted principal amounts, matching the term
  sheet's "balance discharged on the effective date." Present-value conventions for the *tax*
  computation are not covered by the library and were not relied on; the accounting PV restatement
  of the plan payables is a separate, pending step (Q13).
- Fresh-start prong (b) fails on the plan's own business terms (60% old-equity retention of
  reorganized equity, treated as voting shares); no presentation choice can change it. For prong
  (a) the record supplies one figure — Corbin's reorganization value $14,000,000 ("enterprise
  value," effective-date basis) — while the library's phrase is "the reorganization value of the
  assets" measured immediately before confirmation; both sides of the record comparison are
  effective-date figures. The record figure was used as the test value, the gaps are flagged in
  fresh_start.md, and on any convention prong (a) is not outcome-determinative because prong (b)
  fails.
- The record states the first GUC installment falls on the 9/30/2026 effective date; whether it
  was paid is not in the record — asked in Q13 (payment would also move 9/30 closing cash, the
  Q15(b) pro-forma input).
- Pre-delivery review pass: wording corrections only — (i) first GUC installment described as
  "due" on 9/30 rather than "paid," with payment confirmation moved into Q13; (ii) gain placement
  phrased strictly as the library's income-statement placement; (iii) prong (a) caveat expanded
  to flag the "enterprise value" vs "reorganization value of the assets" wording gap;
  (iv) NOL attribute tied to the library's "(the NOL for the year of discharge and carryovers)"
  definition; (v) a session-provenance claim ("term sheet read in Session 2") removed from
  fresh_start.md. No figures changed; no conclusions changed.
- Correction to the prior "Next" note: the §108 schedule's open dependency is the attribute/rate
  data (Q14), not the pre-petition liability detail (Q4); Q4 remains open for MOR Part 2
  completeness only.
- Arithmetic run in visible shell/python sessions (discharge math, attribute reduction, the
  two-part test, the election comparison, and a shape/arithmetic validation of the JSON);
  nothing was forced, and non-reconciling items were left open as questions.
- No deliverable required by CONTRACT.md is missing for any session; nothing was reported
  complete that is open.
