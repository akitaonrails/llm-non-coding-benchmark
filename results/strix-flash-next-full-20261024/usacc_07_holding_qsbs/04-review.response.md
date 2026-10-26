Good discipline. I'll re-verify every deliverable against the source documents and the library line by line, then fix what's wrong.

Facts all tie to the file. Now verifying the two PDF extractions' quoted language and re-reading the remaining deliverables + contract:

All quoted language from both PDFs verified authentic — including the SPA's own representation that Helio "is a domestic C corporation," which supports the §8 check wording. Now let me pull the exact current text of the passages needing correction:

Five fixes applied. Now finishing the review pass on the rest of the opinion (§4–§8):

`agreements_required.md` checks out — item 6 already collects the 83(b) election copy, and §8's "A.3" reference is correct. One completeness gap remains: the re-extracted SPA mentions an **83(b) election (filed 3/2/2020)** which the opinion never addresses — it hints the founder stock may have been restricted, which could touch the acquisition analysis. The library has no §83 authority, so it gets a flagged note, not analysis:

Final verification pass — re-reading the edited passages and checking every citation tag maps to a library file:

Review complete — all citation tags map to the five `INDEX.md` files, arithmetic re-verified, JSON valid. Everything else (AFR figures, case cites, balance-sheet/CSV/org-chart facts, the $1.76M gap treatment, exit-window math) reconciled as written. Here's what I changed:

## Errors found and fixed in `opinion.md`

1. **Legal error (§3 DON'T #1, §1202(g))** — I had written that a partner who contributes her own QSBS to her own partnership "fits neither leg" of §1202(g)'s continuity condition. That was wrong: the contributor *does* literally satisfy (g) — she held the partnership interest when the partnership acquired the stock and thereafter. Corrected to the accurate failure mode: (g) only operates on stock that is QSBS **in the partnership's hands**, and contributed stock never becomes such under (c)(1)+(h) — there's simply no qualified stock for (g to reach).

2. **Overstated gloss on (g)** — "tested on the partner's own holding period and cap" goes beyond the library text; softened to what (g) actually conditions the exclusion on (partner's continuity of interest in the partnership).

3. **Unsupported attribution of the $1M gross-assets test (§3 checklist)** — I had tied "aggregate gross assets ≤ $1,000,000" to "the QSB-at-issuance test of §1202(c)(1)," but the library excerpt never defines the QSB asset threshold. Reattributed: it's the **SPA's own representation**; the library requires QSB status at issuance but defines nothing — now labeled UNVERIFIED.

4. **Under-labeled classification/filing rules (§1)** — "entity classification requires two distinct tax owners" and "no partnership return is required" are outside the closed library. The UNVERIFIED label now expressly covers the two-owner classification requirement and return-filing rules, and flags that consequences (i)–(iii) rest on it.

5. **Loose liability-allocation claim (§2)** — "nonrecourse liabilities allocate per the library's 99/1 example" implied the library addresses recourse vs. nonrecourse allocation; it doesn't — its example just shifts 1% of this same mortgage. Reworded, and noted the **balance sheet itself states the mortgage is nonrecourse** (so it's file-sourced, not just client-confirmed), with a UNVERIFIED flag on whether any recourse distinction could move the $19,000.

6. **Over-specific pin cite** — "[1202(h)(1)]" → "[1202(h)]"; the library excerpt isn't subdivided to (h)(1).

7. **Missed fact from the SPA (new §8 note)** — re-extraction of the SPA PDF confirmed it records an **§83(b) election filed 3/2/2020**, which the opinion hadn't addressed. Added a flagged note: §83 rules aren't in the library (no analysis offered), an 83(b) hints at restricted/compensation stock, but under the library's (c)(1) text acquisition at original issue for money **or services** both qualify — so it's a confirm-the-full-SPA item, not an exclusion risk.

8. **Disregarding premise consistency (§8)** — §6.1 and §7.1 assume transfers among the three LLCs are "within one owner." The org chart labels them "disregarded," but that's a legal rule outside the library; the §8 bullet now covers single-member-LLC disregarding alongside grantor-trust disregarding and cross-points §6.1/§7.1.

## Supporting files

- **`STATUS.md`** — bumped to rev. 3, UNVERIFIED inventory expanded to match (classification/filing rules, SMLLC disregarding, QSB threshold, §83).
- **`QUESTIONS.md`** — closed-library limitations list expanded identically.
- **`numbers.json`** — re-validated; no changes needed (all figures reconfirmed: $9,388,000; $16,480 + $6,180 = $22,660; $0 contribution gain; break-even $10,012,000).

## What I verified and did **not** change

- The step-transaction case cites (*Court Holding*, *Gregory*) are genuinely in `library/step_transaction.md` — safe to cite.
- Both PDFs' quoted language is authentic, including the SPA's own "domestic C corporation" representation, so §3 item 4's wording stands.
- The $1,760,000 balance-sheet gap remains deliberately open (per the no-forced-reconciliation rule), still the only execution-gating item.

No conclusion changed: Helio stock stays out of Holdings, steps 1–2 with the carve-out, step 3 refused, sell personally then optionally move cash in.