# STATUS: COMPLETE WITH OPEN ITEMS

Engagement: RouteWise MSA v7.3 review against the Cobalt playbook (CONTRACT.md).

## Deliverables (all present under `deliverable/`)
- `issues.json` — 8 ranked items: 5 hard-rule breaks (A2, A1, A3, A4, A5), 1 preferred (B5),
  2 notes (B4 clarification, §5.4 de-identified data). Validated as parseable JSON.
- `redlines.md` — drop-in replacement text for each hard-rule violation, plus a clearly marked
  appendix of preferred-position fixes.
- `coo_onepager.md` — plain-English summary, five must-fixes, arithmetic shown.
- `QUESTIONS.md` — original questions logged as answered vs. flagged unknowns after the client
  response (2026-10-25). **Confirmed, no longer assumptions:** (i) both named affiliates will use
  the platform and Holdings signs; (ii) EU data in scope = driver names, locations, working hours,
  customer addresses. **Stated assumptions/defaults still in force:** EU go-live assumed at Service
  Start Date (date unknown); CPI-U unknown, so increase math is modeled at the contractual 8%
  floor. Remaining unknowns are flagged in QUESTIONS.md without re-asking, per client instruction.

## What was checked and deliberately NOT flagged (playbook accepts)
- §9.1 12-month mutual cap and §9.3 gross-negligence/willful-misconduct/fraud carve-outs (B1 —
  carve-outs are Cobalt's preferred position and should be kept); §12.2 30-day export (B2);
  Delaware law/venue/jury waiver (B3); §8.1's 15 days itself (B4 — only the missing cure language
  is noted); 99.5% target + credits themselves (B5); warranty §7 and the UCC excerpt, which we assess as
  inapplicable to a SaaS services agreement (our label, not library guidance — flagged unverified;
  the excerpt itself covers only sales of goods).
  Flagging these as violations would be a false positive.

## Method / verification
- Sources: only files in `documents/` (MSA .md and .pdf, playbook PDF, GC email) and
  `library/` (INDEX + 3 items). Library texts relied on: `gdpr_art28.md` (Art. 28(3) contract
  requirement and controller breach absent it) and
  `contract_interpretation_notwithstanding.md` ("notwithstanding" cap controls unless the cap
  clause itself carves the obligation out — hence the A1 fix is written into §9, not just §10.1).
- MSA `.md` vs `.pdf`: text extracted (`pdftotext`) and compared; substantive wording is identical
  (differences limited to headings/formatting artifacts).
- All arithmetic recomputed in Python (see one-pager footer; e.g., $18,500×12=$222,000;
  8% = +$1,480/mo; 24-mo lock ≈ $444,000–$479,520; SLA credit cap 25%×$18,500=$4,625).
- Nothing outside the library is cited as law. The "de-identified data" note (§5.4) flags the
  re-identifiability question as **unverified** because the library lacks anonymization guidance.
- No numbers failed to reconcile; the Order Form's $222,000/yr matches $18,500×12.

## Open items (do not block the review; flagged per client instruction)
1. Client answered on 2026-10-25 (both affiliates will use the Services — Europe: Rotterdam/Hamburg,
   Brokerage: carrier routing — Holdings signs; EU data = driver names, locations, working hours,
   customer addresses) and has **no further information** on the rest, so these are flagged, not
   re-asked: (a) controller entity (Holdings vs. the B.V.) — the DPA roles clause is drafted to work
   either way; (b) EU go-live date — default assumed at Service Start, and the DPA-at-signing redline
   is date-independent; (c) RouteWise's standard DPA — to be requested from the vendor in the redline
   exchange; (d) fleet size vs. the 350-vehicle cap — commercial check before signature. Details in
   QUESTIONS.md.
2. Exhibit C Annex 1 is populated with the confirmed data types/categories; audit and breach-notice
   mechanics still need to be squared with RouteWise's standard DPA if one exists.
3. If facts later change (e.g., an affiliate drops out), rank 5 (A5) can drop in priority, but the
   as-drafted break still requires the §2.2 + §1.2/§1.6 edits (or re-papering the signature so
   Holdings signs on the affiliates' behalf).
