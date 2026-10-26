# Status

**COMPLETE WITH OPEN ITEMS**

## Client input received (this cycle)
- Both affiliates **will** use the platform: Europe B.V. (Rotterdam/Hamburg), Brokerage LLC (carrier routing).
- Signing structure chosen: **Holdings signs** on behalf of itself and the affiliates (A5 signing path).
- DPA scope confirmed: driver names, locations, hours, EU customer addresses — real GDPR processing.

## Deliverables updated in this cycle
- `issues.json` — rank 2 (A2) now records the confirmed data categories and requires the DPA to name the Customer parties as controllers; rank 4 (A5) rewritten: no longer an assumption, the redline implements the client's chosen Holdings-on-behalf signing plus two conforming edits (§2.2 clarifying sentence, §1.6 Users extension) so affiliate use is both licensed and authorized.
- `redlines.md` — items 2 and 4 updated to match.
- `coo_onepager.md` — items 2 and 4 updated; the affiliate item is now "implement the signing structure on the paper," not "confirm with client."
- `QUESTIONS.md` — answered questions archived (not re-asked); open unknowns listed.

## Explicit open unknowns (client has no further information)
1. **DPA controller mapping** — which entity is controller for which data (Europe B.V. separately, or Holdings for all). DPA drafting default stated (each Customer party as controller for its own data); flagged in issues.json rank 2, QUESTIONS.md, and here.
2. **Brokerage GDPR footprint** — whether any EU/UK personal data flows through Brokerage's use; DPA default covers GDPR/UK-GDPR processing wherever it occurs under §5.3.
3. **CPI-U actuals** (rank 3) — future index values unknown; gap expressed as formulas + one worked example (CPI 3% → $11,100/yr); nothing forced to balance.
4. **Signature pages** — none exist in the delivered set; the agreed Holdings-on-behalf block must appear in the execution version. Failure to do so leaves A5 unsatisfied.
5. **How obligations bind the three signing entities** — with Holdings signing on behalf of itself and both affiliates, three Cobalt entities become Customer parties; neither the playbook nor the closed library states whether Customer obligations (fees §4, data §5, Customer's indemnity §10.2, Users' compliance §11.2) bind them jointly, severally, or jointly and severally. No default invented — the execution version should state this expressly. Flagged in issues.json rank 4, redlines.md item 4, and QUESTIONS.md.

## Assumptions removed / remaining
- The rank-4 affiliate assumption is **withdrawn** — replaced by client-confirmed facts.
- Remaining interpretive assumption (unchanged): §9.1 cap figures — $18,500 × 12 = $222,000 rolling; $247,000 at most in year 1 if the one-time $25,000 implementation fee counts as "fees paid"; both shown, neither forced. Shown in issues.json rank 1.

## Scope notes (unchanged)
- UCC Article 2 excerpt (`ucc_2_distractor.md`): reviewed, **not cited anywhere** — by its own text, hosted-software subscriptions are services, not goods.
- Not raised (playbook accepts per B1–B5, or the playbook is silent): 12-month cap level; mutual §9.3 carve-outs; 30-day export window; Delaware law/Wilmington venue/jury waiver; 15-day suspension notice (the notice period is the window to pay before suspension — §8.1 has no express "cure" word, substance accepted under B4); 99.5% SLA with credits (except the B5 chronic-failure termination right, ranked 6); interest, confidentiality term, §5.4 de-identified data use, §8.2 security suspension, §7.2 remedy exclusivity (playbook silent — not real issues).
- DPA content limited to the library's Art. 28(3) element list (`gdpr_art28.md`); anything beyond it would be outside the closed library and, if mentioned at all, is labeled unverified/pending client confirmation.

## Citation check
Every supporting citation points to `library/INDEX.md` files: `gdpr_art28.md` (Regulation (EU) 2016/679, Art. 28(3)) and `contract_interpretation_notwithstanding.md` (Restatement (Second) of Contracts / Delaware 'notwithstanding' cases). No outside authorities cited.

## Calculation log (shown in deliverables)
$18,500 × 12 = $222,000; year 1 = $222,000 + $25,000 = $247,000; playbook applicability $222,000 ≥ $100,000; provider max mid-term jump $222,000 × 8% = $17,760 → $239,760; playbook renewal cap: lesser of $11,100 (5%) or CPI change (e.g., 3% = $6,660) → $6,660; example delta $11,100/yr; SLA credit ceiling $18,500 × 25% = $4,625/month; missed-window renewal total $239,760 × 2 = $479,520 (24-month renewal at an 8% increase, issues.json rank 5).

## Pre-delivery QA pass
Reviewed all five deliverables against the MSA, the playbook extraction, and the library. Fixed:
- `issues.json` rank 1: citation corrected to "Restatement (Second) of Contracts §203" (was a dangling "§§") — now matches the library's citation line.
- `issues.json` rank 2: "is a Customer party" made forward-looking (the entities become Customer parties only once the chosen signing structure is on the paper); the controller label is grounded in §5.3 (Provider processes personal data on Customer's behalf); DPA execution now required by "Provider and the Customer parties."
- `issues.json` rank 4: removed the unsupported "joint and several … per the playbook" claim (playbook and library are silent); grammar fixed; allocation of obligations among the three signing entities flagged as open unknown 5.
- `issues.json` rank 5: missed-window economics clarified — renewal repricing *could* be at least 8% ($222,000 × 8% = $17,760 → $239,760/yr; ×2 = $479,520 over the 24-month renewal); "would" softened to "could" (Exhibit A ¶4 permits, but does not itself mandate, the increase).
- `issues.json` rank 6: added the caveat that general §12.1 material-breach termination is, at best, a disputed route against Exhibit B's express sole-remedy language — not presented as a clean exit.
- `redlines.md`: stale "(client, this turn)" / "(this turn)" phrasing removed; §5.3 mirror edit for the three-party DPA execution; A5 section carries the obligation-allocation note; B5 lead-in garble fixed.
- `coo_onepager.md`: B4 "with cure" corrected (§8.1 gives 15 days' notice; the notice period is the window to pay — the MSA has no express cure language); residual signing-structure point added to item 4.
- Re-verified every restated contract quote and all arithmetic against `routewise_msa_v7.3.md`, `playbook.txt`, and the two library files; `issues.json` re-validated (6 issues: A1, A2, A3, A5, A4 hard; B5 preferred).

## Deliverable inventory
`issues.json` (6 ranked issues: A1, A2, A3, A5, A4 hard; B5 preferred) · `redlines.md` · `coo_onepager.md` · `QUESTIONS.md` · this `STATUS.md`.
