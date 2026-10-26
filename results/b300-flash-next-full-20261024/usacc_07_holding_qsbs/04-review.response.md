

Good instruction — a self-review pass is warranted. Let me re-read everything with fresh eyes and reconcile the numbers against the source documents.






Continuing the self-review: I need to verify every citation against the actual library text and re-check the remaining files and source documents. Let me pull all of it.








Library texts check out against the citations so far, but I found a mangled sentence at line 90–92 and a sloppy cap sentence at 182–184. Reading the rest:






Now verifying the source documents and remaining library files against the claims made:








All facts reconcile with the source docs except the balance-sheet capital gap I just found. Now let me get exact text for the edits:





Now applying the fixes. First the opinion.md text repairs (sequentially, same file):





Continuing the self-review fixes. I need exact text for the remaining edit targets:






I have the exact text for most edits. I need the Step 2(a) and Step 3 areas plus numbers.json's assumptions field for precise insertion points:






All anchors confirmed. Applying fixes — first batch touches four different files (independent):








Four fixes in. Next: the cap sentence in opinion.md and the full STATUS.md rewrite (independent files):






Now the three remaining opinion.md insertions (same file — applying sequentially):





All eight fixes are in. Final validation pass:





Self-review complete. I re-verified every citation verbatim against the five library files, every fact against the source documents, and every number by recomputation. The good news: all §1202/§721/§752/§731/§7872/AFR citations, the *Court Holding*/*Gregory* and nexus references, the org-chart/CSV/balance-sheet/advisor-PDF facts, and all core arithmetic ($9,388,000 gain; $10,012,000 cap breakpoint; $22,660/yr imputed interest; $19,000 vs $1,520,000; $2,720,000 2024 basis check) check out. What I found and fixed:

**Errors fixed**
1. **opinion.md Step 3 — garbled sentence.** A mangled clause about Helio's liability shield ("already pierced-nothing — it's a C corp, fine") was rewritten; the commingling/veil point now rests solely on the library's stated rule, with a cross-reference that Helio never enters the holding anyway.
2. **opinion.md §3 — imprecise §1202(g) cite.** The library's (g) conditions the exclusion on the **partner** holding the interest when the partnership acquired the QSBS — I had paraphrased it as a partnership-level requirement. Rewrote: the contributed-stock disqualification now cites §1202(h) (which the library squarely supports), and the general "gain flows out in the year of sale" timing rule — which the library does not state — is now tagged **UNVERIFIED** instead of asserted flatly.
3. **opinion.md §3 — vague cap sentence.** "Above ≈ $9.4M+ headroom the excess is taxable" replaced with the precise breakpoint: fully excluded through a stake value of **$10,012,000**, every dollar above taxable (consistent with §5.1 and numbers.json).
4. **agreements_required.md item 14 — unsupported authority.** I had attributed a "Colorado franchise/annual report" to the nexus library; the library only supports the WY annual report and Colorado filing via commercial-domicile nexus. Fixed, with Colorado entity annual-report filing now flagged UNVERIFIED (check SoS/CPA).

**Things that don't reconcile — flagged, not forced**
5. **Balance sheet doesn't internally add up.** Assets (3,400,000 − 1,120,000 + 600,000 + 400,000 = 3,280,000) less the $1,900,000 mortgage imply capital **+$1,380,000**, yet stated tax capital is **−$380,000** — a **$1,760,000 unexplained gap**. Per the contract I did not force a reconciliation: added flags in opinion.md (Step 2(a) + §7), numbers.json, and a new **QUESTIONS.md R7** asking the preparer for Properties' tax-basis rollforward. The $0 §731(gain) conclusion survives either reading (basis $1,520,000 or $3,280,000 vs a $19,000 deemed distribution), and I softened an earlier line that claimed other basis items "could only make it more secure."
6. **§7872 classification nuance added.** Whether transfers between wholly **disregarded** SMLLCs are "loans" between two parties at all isn't addressed by the library — now caveated as UNVERIFIED in Step 3, noting the library's directive governs the file's facts and the veil-piercing point stands regardless.

All changes are itemized in the new "Self-review corrections" section of `deliverable/STATUS.md`; final validation passed (numbers.json parses, all arithmetic re-asserted, defective text fully removed). Status remains **COMPLETE WITH OPEN ITEMS** (R1–R7 outstanding).