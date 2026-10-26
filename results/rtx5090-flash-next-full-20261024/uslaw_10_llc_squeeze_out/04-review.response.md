Systematic audit: (1) re-read every source file, (2) re-read every deliverable, (3) check each citation against the closed library, (4) recompute all arithmetic, (5) cross-file consistency. Then fix.

OA text and Tooley file confirmed. Now reading CONTRACT.md (schemas) and all five deliverables in full:

Memo top section checks out arithmetically (verified: 189,100/1,764,000 = 10.7%; 189,100/597,800 = 31.6%; 9.8/7.2 = 1.36×; dilution formulas 14.9%/15.4%/12.1%; fee total 1,050,000). Now the JSON deliverables and remaining memo:

Full "why" string is intact on disk (json.load succeeded; ends "...not forced)."). Re-reading memo middle section for exact edit targets, re-checking CSV, and sweeping all citations:

Now the memo fixes:

Now update STATUS.md with the audit record, then run the full final verification:

The one "14.1M" hit is the quoted old wording inside STATUS.md's audit note describing the correction itself — intentional, not a residue. Everything else is clean: 6 schema-valid claims, all arithmetic reproduces exactly, zero unsupported citations.

**Audit complete. Here's what I reviewed, what I fixed, and what I deliberately left open.**

## What I checked
- **Every number** against `documents/`: offer ($189,100 = 6.1% × $3.1M), broker shares ($1,764,000 / $597,800), offer ratios (10.7% / 31.6%), manager-vs-broker (1.36×, $2.6M gap), dilution formulas (14.9% / 15.4% / 12.1%), back-solved inputs (~$14.05M new capital or ~$0.77M FV to reach 6.1%), fee totals ($1,050,000 = 180+195+210+225+240 from the CSV), fallback ($375,000 = 35.7%), notice timing (Aug 20 → Sep 20 = 31 days), limitations math for the ~Nov 2026 filing assumption.
- **Every citation** against `library/INDEX.md` (closed library): *Zimmerman*, *Dieckman*, *Nemec*, *Gerber*, *Tooley*, *Zuckerberg*, 6 Del. C. §18-1101(c),(e), §18-1001–1003, 10 Del. C. §8106 — all in the library. No authority outside the library is cited; fee-shifting and statutory inspection rights stay flagged **[unverified]**.
- **Every OA quotation** against the PDF text (§5.4, §6.3, §7.3, §9.2, §11.1, §11.2) — verbatim matches.

## What I changed
1. **claims.json claim 5** — `barred_portion: 375000` contradicted its own text ("expected barred portion is now 0") and claim 4. Now `0`, with the 2022–23 $375,000 fallback kept in the tolling text.
2. **claims.json claim 2** — "14.1M of new capital" → **~14.05M** (the actual back-solve is 14.046M; memo §3 already said ~$14.05M).
3. **claims.json claim 1 + memo §2.2** — Zimmerman paraphrase tightened to the library's exact formulation ("the issuer must comply strictly with the agreement's notice mechanics and purpose requirements; a call that fails the specified delivery method does not trigger dilution"); my "caller must strictly comply… non-compliant call" wording was a loose restatement.
4. **Memo §1** — "counter above $1.5M" harmonized with §4's actual recommendation: **counter at $1,764,000**.
5. **Memo header** — now records turn-2 answers, turn-3 pushback (§7), and this turn-4 audit, replacing "updated same day with client's answers."
6. **claims.json claim 4** — stray comma/formatting cleaned (JSON was valid but sloppy).
7. **STATUS.md** — added the audit record: what was re-verified, corrections applied, "no substantive theory changed."

## Left open deliberately (not forced to reconcile)
- **The 6.1% cannot be reproduced** from the Manager's own inputs under any standard formula — left open as evidence of arbitrariness; demand target in QUESTIONS.md item 1.
- **The "6% of gross rents" stream is unquantified** — the CSV shows the fee but no amounts; her 2026 bank statements should contain it (QUESTIONS.md item 2).
- **Fee escalation mismatch noted, not forced**: 2022 resolution says 8%/yr (→194,400/209,952/226,748/244,888) vs actual flat +$15,000/yr — already recorded in valuation_gap.json.
- The 6.1% figure, $3.1M book equity, and $7.2M/$14.5M/$9.8M valuations are taken **as stated in the file**, flagged unverified with workpaper demands.

All five deliverables re-validated (JSON parses, schema fields intact) under `workspace/deliverable/`. Status remains **COMPLETE WITH OPEN ITEMS**; the time-critical item is unchanged — the $189,100 offer expires **2026-10-31**.