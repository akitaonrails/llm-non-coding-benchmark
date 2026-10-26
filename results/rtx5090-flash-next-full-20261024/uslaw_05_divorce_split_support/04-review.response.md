Running a full pre-delivery audit: re-reading everything, verifying each citation against the library, and recomputing every number.

Now verifying every cited authority against the actual library text, and the facts against the client documents:

All six library files are now verified. The remaining deliverables and the client documents need a final fact pass:

Schemas match CONTRACT.md. Now the fact pass against the client documents:

All facts reconcile with the documents. Now a full arithmetic re-verification of every figure in the deliverables:

Excellent — the script caught my own error before it reached the file: `2,311.58/yr` in `child_support.json` is actually **correct** (it's the unrounded difference $2,022.6316 − $1,830.00 = $192.6316 × 12); only the rounded-monthly product gives 2,311.56, so no change there. The two genuine numeric errors stand. Final consistency greps, then fixes:

All artifacts reviewed. Applying the fixes now — two hard numeric errors and five authority/phrasing precision fixes:

Exact text in hand. Applying the five remaining edits in parallel:

Now the two `division.json` fixes — reading the full file first to get exact text:

Now the STATUS.md touch-up — audit note plus the citation-traceability nuance:

Final validation pass — JSON parse + schema keys + arithmetic re-run:

Audit complete — everything re-verified, two real errors fixed, five precision fixes applied, and one "fix" I nearly made was reversed because the original was right. All changes are logged in `deliverable/STATUS.md` under "Pre-delivery audit."

## What I checked

- **Authority:** re-read all six files in `workspace/library/` against every citation in the deliverables; anything the library doesn't support is now labeled as an assumption or flagged `[unverified]`.
- **Facts:** re-checked every figure against `workspace/documents/` (asset schedule, affidavit, HR letter, pay stub, client goals).
- **Arithmetic:** re-ran a 69-check script covering every number in the deliverables (after-tax values, mortgage amortization, §121 shelter, all four division options, the full child-support worksheet and bonus sensitivities).
- **Schemas:** both JSONs re-parsed and matched key-for-key to the CONTRACT.md required shapes.

## What I fixed

1. **`advice.md` §3 — numeric error.** Said "≈ $762,700 interest remains." That's actually the total of the remaining 288 payments (principal *and* interest); interest alone is ≈ **$362,700**. Corrected.
2. **`division.json` alternative B — garbled figure.** Said the $734,000 gain was "sheltered to 468,000." The shelter is the **two $250,000 §121 exclusions ($500,000)** → $234,000 taxable. The downstream taxes ($21,996 / $17,550 / $39,546) were already correct and unchanged.
3. **NIIT on Husband's brokerage gain — labeled.** The library's stated NIIT convention covers only *Wife's* house gain; applying 3.8% to his brokerage gain is a conservative extension of IRC §1411. Now explicitly labeled as an assumption in both `advice.md` §2 and `division.json`.
4. **QDRO language — matched to source.** §5 now mirrors `library/qdro_72t.md`: absent a QDRO, a distribution to the participant to pay the former spouse is taxable to the participant and, if under 59½, subject to the 10% additional tax. (My earlier "you get nothing taxed-to-you basis" phrasing was muddled — deleted.)
5. **§408(d)(6) — sourcing nuance disclosed.** That section appears in the *body* of `library/qdro_72t.md` but not in that file's INDEX citation line; flagged at the citation point.
6. **Head-of-household test — completed.** The library requires both a qualifying child living with you >half the year *and* paying >half the home's cost; §9 (and `division.json`) now state both, noting your ~70% overnights satisfy the first.
7. **§1 caveat.** "His slice doesn't shrink under Option C" holds at the 24% and 32% conventions but **not** at the 12% sensitivity (there his own proposal leaves him ahead) — noted, with the standing advice to pin his real bracket.

## What I checked and deliberately did *not* change

- **`child_support.json` "$2,311.58/yr"** — I had flagged this as a rounding error, but re-derivation showed it's **correct**: it's the unrounded difference ($2,022.6316 − $1,830.00) × 12 = 2,311.58. The 2,311.56 figure would come from multiplying the already-rounded monthly number. Fix withdrawn.
- The "≈ $14k–$21k" support stream and "≈ $63k–$70k" total stack: exact values are $13,870–$20,804 and $62,568–$69,503 — the "≈" phrasing is accurate.
- The $18,525 combined net, $3,050 bracket, $2,022.63 share, $661,707 build-up, $51,446 tax saving, and the YTD $27,212 / $4,712-residual discovery trail all re-verified exactly.

Bottom line: the substance of the advice is unchanged — after-tax the proposal is $613,008/$658,960 (gap $45,952), Option C remains the recommendation, and support is ≈ $2,023/month — but the audit removed two numerical misstatements and closed three authority-precision gaps before delivery.