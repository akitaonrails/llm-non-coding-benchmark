The PDFs couldn't be rendered natively; I'll extract their text with Python instead.

The advisor proposal and stock agreement are extracted. Now I have the full picture. Let me run the calculations.

All calculations are done. Now I'll write the deliverables, starting with the main opinion.

I noticed a stray character in the opinion; fixing it now.

Now the numbers file, agreements list, and client questions:

Final verification pass — JSON validity, file inventory, and citation audit:

All citations map to files in `library/INDEX.md`. One precision fix: the catch-up interest components round to $41,162.29 but the true sum is $41,162.30 — I'll note the rounding basis rather than leave a 1¢ mystery.

The engagement is complete. Summary of what was done and concluded:

## Engagement complete — Oakline Holdings restructuring review

**Files read:** `CONTRACT.md`, all four library authorities, and all five client documents (the two PDFs were extracted with `pdftotext` since direct rendering isn't supported).

**Deliverables written to `workspace/deliverable/`:**
- **`opinion.md`** — step-by-step analysis with authority and a do/don't verdict for each of the advisor's 4 steps, the revised plan, Helio Grid stock guidance, and loan remediation
- **`numbers.json`** — all key figures with arithmetic and assumptions
- **`agreements_required.md`** — 11 intercompany/governance documents mapped to the revised plan
- **`QUESTIONS.md`** — 6 non-blocking clarifying questions for the client
- **`STATUS.md`** — `COMPLETE WITH OPEN ITEMS` (6 listed)

**Key conclusions:**

1. **The one catastrophic error — don't contribute the Helio Grid stock.** Per §1202(h)(2) (`irc_1202_excerpt.md`), a contribution to a partnership is not a qualifying transfer; the stock ceases to qualify in the partnership's hands. Her $12,000-basis stake (409A ≈ $9.4M, held past the 5-year mark, $10M issuer cap) currently supports a fully excludable gain of **$9,388,000** — the whole exclusion would be forfeited. A contribute-then-distribute-then-sell workaround is also flagged as collapse bait under *Court Holding Co.*/*Gregory*.
2. **The "no tax event" claim is only partly true.** §721(a) covers Services/Digital, but contributing Properties triggers ≈ **$19,000** deemed gain (1% × $1.9M mortgage shifted to the 1% trust member, with no capital cushion from the −$380,000 tax capital). Per the contract's no-forcing rule, the net-asset view (which would show no gain) is flagged as an open reconciliation rather than papered over.
3. **"One bank account, one set of books" is rejected** — the library ties undocumented intercompany loans to commingling/veil-piercing, which would destroy the liability protection that is the proposal's own headline benefit. Remediation: dated AFR-interest notes (annual imputed interest $15,840 + $5,940 at the assumed 3.96% short-term AFR; catch-up deemed interest through 2026-10-25 of $41,162.30) and separate accounts/books.
4. **"One return" and "reinvest without tax" don't hold** — Colorado commercial-domicile filings survive the Wyoming wrapper (`state_nexus_summary.md`), and no library authority supports partnership-level tax deferral.