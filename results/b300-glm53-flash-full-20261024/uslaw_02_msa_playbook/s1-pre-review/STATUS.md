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

## Assumptions removed / remaining
- The rank-4 affiliate assumption is **withdrawn** — replaced by client-confirmed facts.
- Remaining interpretive assumption (unchanged): §9.1 cap figures — $18,500 × 12 = $222,000 rolling; $247,000 at most in year 1 if the one-time $25,000 implementation fee counts as "fees paid"; both shown, neither forced. Shown in issues.json rank 1.

## Scope notes (unchanged)
- UCC Article 2 excerpt (`ucc_2_distractor.md`): reviewed, **not cited anywhere** — by its own text, hosted-software subscriptions are services, not goods.
- Not raised (playbook accepts per B1–B5, or the playbook is silent): 12-month cap level; mutual §9.3 carve-outs; 30-day export window; Delaware law/Wilmington venue/jury waiver; 15-day suspension notice with cure; 99.5% SLA with credits (except the B5 chronic-failure termination right, ranked 6); interest, confidentiality term, §5.4 de-identified data use, §8.2 security suspension, §7.2 remedy exclusivity (playbook silent — not real issues).
- DPA content limited to the library's Art. 28(3) element list (`gdpr_art28.md`); anything beyond it would be outside the closed library and, if mentioned at all, is labeled unverified/pending client confirmation.

## Citation check
Every supporting citation points to `library/INDEX.md` files: `gdpr_art28.md` (Regulation (EU) 2016/679, Art. 28(3)) and `contract_interpretation_notwithstanding.md` (Restatement (Second) of Contracts / Delaware 'notwithstanding' cases). No outside authorities cited.

## Calculation log (shown in deliverables)
$18,500 × 12 = $222,000; year 1 = $222,000 + $25,000 = $247,000; playbook applicability $222,000 ≥ $100,000; provider max mid-term jump $222,000 × 8% = $17,760 → $239,760; playbook renewal cap: lesser of $11,100 (5%) or CPI change (e.g., 3% = $6,660) → $6,660; example delta $11,100/yr; SLA credit ceiling $18,500 × 25% = $4,625/month.

## Deliverable inventory
`issues.json` (6 ranked issues: A1, A2, A3, A5, A4 hard; B5 preferred) · `redlines.md` · `coo_onepager.md` · `QUESTIONS.md` · this `STATUS.md`.
