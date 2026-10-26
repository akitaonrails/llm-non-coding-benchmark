Now the pre-delivery review pass: validate the JSON, recompute every number, verify every quotation and clause reference against the source documents, and check citations against the library index.

The .md/.pdf differences are markdown artifacts only (heading markers, "No. 1" sentence split) — the documents reconcile. Now fixing the real defect: adding the required `redline` field to each `issues.json` entry.

Now softening two unsupported factual assertions (the "orders of magnitude"/"routinely run above" claims are not backed by the library), then writing STATUS.md.

Engagement complete. All deliverables are in `deliverable/` and `STATUS.md` reports **COMPLETE**.

## What the review found (five issues)

| # | Clause | Rule | Issue |
|---|--------|------|-------|
| 1 | §9.1/§9.3/§10.1 | **A1 hard** | The "uncapped" IP indemnity is an illusion — §9.1's "notwithstanding anything to the contrary" cap swallows it (§9.3's carve-outs omit §10); effective cap 12 × $18,500 = **$222,000** |
| 2 | §5.3/Exhibit C | **A2 hard** | DPA says "[To be attached]" while GC confirms EU driver data — under Art. 28(3) (library) Cobalt, the controller, is in breach from day one of processing |
| 3 | Order Form ¶4 + §14.1 | **A3 hard** | Unilateral mid-term increase + "greater of 8% or CPI" renewals: +$1,480/mo, +$26,640 if used at month 18, +$17,760/yr at renewal vs a compliant 5% cap |
| 4 | §3.3 | **A4 hard** | 24-month auto-renewal / 90-day notice — missed date = $479,520 lock-in vs playbook's $233,100 max per cycle |
| 5 | §2.2 | **A5 hard** | Affiliates (incl. the EU entity generating the driver data) excluded from the license |
| 6 | Exhibit B | B5 preferred | Credits-as-sole-remedy without the chronic-failure termination right the playbook requires; max credit only $4,625/mo |

Playbook-compliant items (mutual cap with carve-outs, DE law, 30-day export, 15-day suspension, 99.5% SLA structure) were deliberately **not** flagged; the UCC library item is a distractor and was not cited.

## Changes made during the pre-delivery review

1. **issues.json schema defect** — every entry was missing the contract-required `redline` field; added replacement text to all 6 entries and re-validated the JSON (key order matches the contract's schema).
2. **Unsupported assertion, issues.json rank 1** — "would exceed the cap by orders of magnitude" is market commentary not backed by the library; rewritten to what the contract text itself supports (the §10.1 damages/costs/fees obligation competes for the same $222,000).
3. **Unsupported assertion, coo_onepager.md item 1** — "Patent cases routinely run far above that" replaced with the same arithmetic-based framing.
4. **Reconciliation check** — verified `routewise_msa_v7.3.pdf` ≡ `.md` via whitespace-normalized comparison (the apparent "8%/CPI" mismatch was a PDF line-wrap artifact, not a substantive difference); documented in STATUS.md.
5. **Unverified-law labeling** — GDPR fine magnitudes explicitly marked as outside the closed library and unverified; only the Art. 28 breach itself is asserted.
6. **All 15 dollar figures re-computed by script** — no mismatches; arithmetic shown in the deliverables.

One open *business* action (noted, not a deliverable gap): Cobalt must attach an executed DPA text to Exhibit C before signature — RL-2 forces that and locks in the Art. 28(3)(a)–(h) minimum content.