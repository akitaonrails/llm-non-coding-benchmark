Library and source documents confirmed. Now recomputing every figure from the source data and checking the deliverables against them:

The extracted text files are gone, so I need to re-extract from the source PDFs to verify the quoted facts.

Source facts verified — proposal date is **2026-02-11**, the "not a law or CPA firm" disclaimer is verbatim, and the SPA details ($0.004 × 3,000,000 shares = $12,000, Feb 18 2020, §2.3 gross-assets rep, original issuance, 83(b) filed Mar 2 2020) all check out. Let me recompute the 5.98-year figure against the confirmed proposal date, and re-read the current deliverables:

All 8 edits applied. Now running the final verification pass — JSON validation, stale-string greps, and cross-file figure consistency:

JSON schema intact and no stale phrasing remains — the only "5.98" hits are the two newly dated statements. Final cross-file consistency sweep:

Everything reconciles: all five library citations match `INDEX.md` exactly, every recurring figure is identical across files, `numbers.json` validates with the four required keys untouched, and STATUS remains **COMPLETE WITH OPEN ITEMS**. Review pass complete.

## What I checked

1. **Re-extracted both source PDFs** (`advisor_proposal.pdf`, Helio SPA) and verified every quoted fact verbatim — proposal author/date (**Summit Peak Wealth Advisors, 2026-02-11**, "not a law or CPA firm"), the "gain lands in the holding so you can reinvest without tax" claim, and SPA facts (3,000,000 shares × $0.004 = $12,000, Feb 18 2020, §2.3 gross-assets/C-corp/QTOB reps, original issuance, 83(b) filed Mar 2 2020).
2. **Re-derived all arithmetic** independently (imputed interest $15,840 + $5,940 = $21,780/yr, cumulative $41,222 across the three loan tranches, $9,388,000 anchor, cap $10,000,000 vs 10× basis $120,000, break-even $10,012,000, deemed distribution $19,000, §731(a) gain $0, balance-sheet gap $1,760,000, holding-period day counts). All matched.
3. **Audited every citation** — all legal citations land on the five library files; nothing outside the library is cited, only labeled **[unverified]**.

## What I fixed (8 edits, all in `opinion.md`)

1. **Added a proposal-source line to "Facts relied on"** — author, date 2026-02-11, and the "not a law or CPA firm" disclaimer were load-bearing facts the opinion never actually stated.
2. **Holding-period figures (×2)** — the "~5.98 yrs at proposal date" claim was correct (2,185 days ÷ 365.25) but the proposal date was never stated, making it unverifiable. Now anchored: "5.98 years as of the proposal date 2026-02-11; ≈6.7 years as of this memo 2026-10-26 — 2,185 / 2,442 days since 2/18/2020."
3. **"ordinary capital gain" → "fully taxable gain"** — self-contradictory terminology in the Helio damages paragraph.
4. **"$2.88M of building equity" (Step 3)** — mislabeled on both counts: $2,880,000 is the *tax basis* of buildings + land, and net of the $1,900,000 mortgage the book equity is only ≈$980,000. Corrected with both figures.
5. **Same "building equity" phrasing in A4** → "the Properties real estate."
6. **Gift guidance tightened** — the old "transfers to her trust/beneficiaries by gift or at death" was misleading since the 1% Holdings partner is *her own revocable trust*: now specifies completed gifts (individuals/irrevocable trust) or death as the §1202(h)-safe routes, and flags that moving shares into her own revocable trust is probably a federal no-op **[unverified — not in library]**.
7. **Quote attribution expanded** at the "not a law or CPA firm" citation to name the advisor and proposal date.
8. Minor wording: "no rate in the library" → "no rate **authority** in the library" for precision.

## What I deliberately did **not** change

- `numbers.json` — keys and values verified correct against CONTRACT.md schema; untouched.
- The $1,760,000 balance-sheet gap, the dual $1,520,000/$3,280,000 basis readings, and the compounding/demand-loan conventions — already flagged as open items/assumptions rather than forced into false reconciliation.
- STATUS stays **COMPLETE WITH OPEN ITEMS** (the §1.1202-2 questions remain genuinely open — referenced but not reproduced in the library).

No errors of substance were found in the core analysis — the fixes were one terminology contradiction, one mislabeled financial figure, one potentially misleading estate-planning sentence, and three traceability/verifiability gaps.