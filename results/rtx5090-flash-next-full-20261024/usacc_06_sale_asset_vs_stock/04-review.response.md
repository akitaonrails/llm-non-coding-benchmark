Good discipline — I'll audit against the closed library line by line, re-run every number, and check cross-file consistency. First, the library's actual text (citations must be supported by the file contents, not just the INDEX line):

The library actually covers the Danielson rule, §1366(f)(2), §338(h)(10)/§336(e), 21%, the 5-year period, and the FMV cap — good. Next, the remaining two library files and the source documents:

Library fully verified. Now the source documents — checking every LOI/email fact quoted in the deliverables:

All five files reviewed; JSON math exactly verified. Now applying the fixes found in the audit:

Now the §1b ladder precision, the "only version" claims, and the assumption notes:

Final validation pass — JSON re-check, dollar-figure sweep of the memo against the python-verified set, and render check of edited sections:

The convoluted identity assertion in my check script itself had a bug — re-running with a clean one:

Audit complete. Everything is now verified and delivered. Here's what I reviewed and what I changed.

## What I verified (no changes needed)

**Authority check — every citation traced to actual library file text, not just INDEX lines:**
- *Danielson* rule, *Muskat*, Rev. Rul. 69-643, economic-reality → all actually in `irc_197_and_noncompete.md` ✓
- 21% rate, 5-year recognition period (§1374(d)(7)), per-asset BIG cap, §1366(f)(2) pass-through loss → all actually in `irc_1374.md` ✓
- "Each class up to FMV before the next class" + consistent Form 8594 filing → actually in `irc_1060_form_8594.md` ✓
- §338(h)(10)/§336(e) deemed-asset-sale language → actually in `stock_vs_asset_overview.md` ✓
- §453(i) recapture-in-year-of-sale, inventory exception; 37/20/21 rates; no-NIIT material-participation rule → ✓
- Every [unverified] flag from before (inventory character, zero goodwill basis, S character flow-through) still correctly flagged.

**Document facts — every LOI/email fact re-read from the PDFs and files:** $3.1M all-cash, Exhibit A classes, $400k covenant/5-yr, 45-day exclusivity; $2,850,000 = $2,350,000 cash + $500,000 note 6%/5-yr annual principal; 12-month indemnity capped at 10% (= $285,000) + $100,000 escrow; unpriced 3-year covenant; register FMV $650,000; conversion BIGs $230k/$900k; stock basis $420,000. All quoted correctly.

**Full arithmetic re-run in python from raw facts:** both Deal A models, Deal B, GPR 0.85263158, interest $90,000 → $56,700, deferral PV $13,431, the $437,200 bridge and its decomposition, all three §1b match prices, and the 2028 figures — all reconcile exactly. `comparison.json` re-validated: schema keys, gain+basis=price, net identity, and rate build-up.

## What I changed (7 fixes)

1. **memo §1 bullet 3 — factual error fixed.** It said Deal A wins only if the allocation is rewritten *and* (price up or 2028). Wrong: as-drafted A closing in 2028 nets ≈ $2,414,100 and beats B's $2,364,000 without any allocation fix. Rewrote to the accurate rule with §1b cross-references.
2. **memo §3 §1374 table — mislabeled row.** "Non-compete / other: $410,000" now reads "Non-compete + inventory ('Other'): $410,000.00 (covenant $400,000 + inventory $10,000)" so the column demonstrably foots to the $2,520,000 total gain.
3. **memo §5 — arithmetic typo.** Deferral figure "$85,211" → correct **$85,263** ($426,315.79 × 20%), with the derivation shown.
4. **memo §7.3 and QUESTIONS.md item 3 — contradiction resolved.** The "only version of Deal A that beats Deal B" claim conflicted with the §1b match ladder; both now say "at the current $3,100,000 price" and point to §1b for the higher prices that would also win.
5. **memo §1b ladder — precision.** Header "(tax-only table)" was wrong since rows 3–4 are all-in; each row now states its explicit target ($2,364,000 closing-date net vs $2,428,131 all-in), and the 2028 row is labeled "(counter allocation)". Also fixed "both goodwill caps" → "the equipment and goodwill conversion-BIG caps" (§1374 caps are per-asset).
6. **memo §4 — new [unverified] flag.** "5-year MACRS" for the buyer's equipment benefit is not supported anywhere in the closed library; now flagged **[unverified]** with the point restated as "a short MACRS recovery period."
7. **memo §8.7 + §3 — assumption transparency.** The 6% rate used for both the deferral PV (≈$13,431) and the escrow carry (−$6,000) is now stated as an assumption, and the §1366(f)(2) offset note now points to the §8.5 flow-through flag.

STATUS.md's file description was updated to mention the §1b Q&A section. **`comparison.json` and `form_8594_counter.md` needed no changes** — their numbers verified exact. Deliverables are final and internally consistent.