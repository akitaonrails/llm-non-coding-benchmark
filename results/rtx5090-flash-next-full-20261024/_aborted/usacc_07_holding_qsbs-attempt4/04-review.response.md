Reviewing systematically. First, the full record and the citable authority set.

Now applying the fixes. Starting with the unsupported-authority items in §1–§4.

Numbers verify exactly. Now the STATUS.md entry.

Self-review is finished and every fix is applied and re-verified. Here is the change list.

## Pre-delivery self-review — what I checked and what changed

Checked three things: (1) arithmetic, (2) whether every citation actually maps to one of the five files in `library/INDEX.md`, (3) whether every figure reconciles. **The three required numbers are unchanged** — `qsbs_exclusion_at_risk` $9,388,000 (range $8,988,000–$9,988,000 on your $9–10M estimate), `imputed_interest_annual` $22,660, `properties_contribution_gain_estimate` $0 — and no recommendation changed. What changed is how much authority sits behind particular sentences, plus presentation fixes.

### 1. Unsupported authority — six propositions re-labelled [UNVERIFIED]
They read as if cited, but nothing in the library states them:

1. that a §1202 gain is included **in the year of sale** (`opinion.md` §1 table, §9.2) — the library has no inclusion-timing rule;
2. that **forming an LLC** is not itself a taxable event (Step 1);
3. that §1202(a) is triggered by a **"sale or exchange"** (§8.5 rule 3) — the excerpt grants an "exclusion of a percentage of gain" and contains no disposition rule; now also carried as §7 open item 5;
4. that **cash** is "property" for §721(a) purposes on the post-exit contribution (§9.4) — §721(a) says only "contribution of property for a partnership interest";
5. that outside **basis carries over** on a contribution (§6(b), §8.7) — a §722-type rule; §722 is now named *only inside* the [UNVERIFIED] label, since it is not in the library;
6. my paraphrase of §1202(g) as **"tacking"** — replaced by the library's own words: gain "held by a partnership flows to a partner only if the partner held its partnership interest when the partnership acquired the stock and at all times thereafter."

### 2. Citation hygiene
Every remaining statutory citation maps to a library file. Section references not in the library were removed even from the sentences that flag a gap (grantor-trust rules; the related-party interest rule), so nothing can be mistaken for support. §83(b) survives only as *your* document recited in the SPA. Step 4 now notes that §1202(g) is the library's **only** window into partnership mechanics and it is QSBS-specific.

### 3. Figures that did not reconcile
- **§6(b) / §8.7(1) — an over-stated claim.** I had implied the 2024 refinancing helped explain the $1,760,000 gap. It explains why stated tax capital is *negative* ($1.2M of mortgage proceeds to your personal brokerage account pushes a capital account down), but a distribution out of a disregarded entity moves neither inside asset basis nor assets-minus-liabilities, so it cannot close the gap at either end. A stale $560,000 residual that no longer tied to anything was deleted. The gap stays open and unforced.
- **Outside basis, tied out in one place.** Pre-shift **$3,280,000 (A) / $1,520,000 (B)** → less the $19,000 §752(b) shift → **$3,261,000 / $1,501,000** → plus the $1,900,000 cash contribution → **$5,161,000 / $3,401,000**. The A/B convention difference is stated (A = inside asset basis, excludes the mortgage; B = stated tax capital plus her share of debt, includes it), and that all four are Properties-level, excluding the $12,000 Helio basis.
- **Prior-year imputed interest now published with its convention.** 2024 Properties **$8,606.85** ($250,000 × 4.12% × 305/365); 2025 Properties **$13,669.37** ($10,300.00 + 199/365 of $6,180); 2025 Digital **$2,048.71** (121/365); 2024 Digital **$0**. Vague estimate keys in `numbers.json` were replaced with a `partial_year_arithmetic` key that reproduces each figure, and one earlier day-count figure ($8,635 on a 306-day count) was corrected because it did not reproduce. All still labelled **indicative**, pending the CPA (R2).
- **Re-computed and unchanged because they verify:** $16,480 / $6,180 / $22,660; $21,780 / $25,190 at the other AFRs; 1% × $1,900,000 = $19,000; 99% × $1,900,000 = $1,881,000 with $380,000 of §731(a) gain on Reading B; the ~79% gift breakpoint (0.79 × $1,900,000 = $1,501,000); cap headroom $612,000, and taxable gain starting at a stake value of $10,012,000.
- Every quoted sentence from the advisor's proposal and from the library re-checked verbatim against source; all tables well-formed; one grammar/typo fix.

### 4. Added follow-on work
`QUESTIONS.md` R2 now asks the CPA a new question that could collapse the two basis readings to one: which convention each Properties figure uses (is the building line net of the $1,120,000 depreciation; is the $(380,000) capital line net of depreciation and of the $1.2M distribution).

### Still open by design
The $1,760,000 Properties difference (you cannot resolve it, so both readings stay on the table), the prior-year §7872 accrual (pending the CPA), and every tax-rate figure (no rates exist in the library). Full change list is in `deliverable/STATUS.md`, "Pre-delivery self-review (2026-10-25)".