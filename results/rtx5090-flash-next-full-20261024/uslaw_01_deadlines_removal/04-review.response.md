Good discipline — let me re-verify everything against the library and documents before anything goes out.

Now let me verify every quoted/paraphrased authority against the actual library file texts, and confirm the complaint really recites RCW 4.84.330.

The library matches well. Now the FRCP excerpts file and the complaint's fee statute recital:

Rule citations verified. One detail to check — my memo says the summons' "demand that plaintiff file" option is a **14-day** period. Let me confirm that number is actually in the summons:

All quotes verified; the "14 days" is in the summons ✓. Let me see the JSON in full before making the fix list:

All verified. I found several issues to fix. Applying them now:

Now let me pull the exact texts I need for the remaining fixes — the §1446(c)(1) line from the library, the full summons "demand to file" paragraph, and the current JSON/STATUS files:

Everything is confirmed. The library's §1446(c)(1) reads: "A case may not be removed under (b)(3) on the basis of diversity more than 1 year after commencement" — my memo's phrasing needs to align with that. The 14 days in the summons is the period for the **plaintiff to file** after the defendant's request — my summary needs to be stated more precisely. Applying the remaining memo fixes now:

One edit missed the exact text — let me pull the exact jury bullet line:

All edits applied. Final validation pass — JSON parse + key check, and a sweep for any leftover stale or unsupported phrasing:

The JSON edit introduced unescaped double quotes (`"lives in Seattle"`) inside the string. Fixing:

JSON validates with all required keys. Final visual check of the edited memo sections:

One cosmetic line-wrap to tidy in §8, then I'm done:

Review complete. I re-verified every date computation in Python, checked every quotation against the actual library file texts, and cross-checked all citations against `library/INDEX.md`. **Here is everything I changed:**

## Errors and unsupported authority fixed

**`memo.md`**
1. **Removed a fabricated citation (§2).** The caveat about service validity cited "CR 4.21" — that rule appears nowhere in the library (I had stated it from memory). The caveat now accurately says the library's only touchpoint is the parenthetical "under RCW 4.28.185" inside the CR 4(a)(2) excerpt, whose text is *not* in the library, so service validity is flagged unverifiable — no rule is asserted from memory.
2. **Removed an unsupported legal assertion (§5.2).** "Single plaintiff vs. single defendant, so there is no aggregation problem" stated a doctrine the library never addresses. Replaced with the arithmetic reality: the contract count alone ("not less than $110,916.40") clears the §1332(a) $75,000 threshold by itself, so aggregation never needs answering.
3. **Labeled the jury-demand advice unverified (§7).** "Join the demand to preserve it" implied a procedural rule that is not in the library. Now: plaintiff's jury demand is a documented fact (summons caption "(Jury Demand)"), joining it is prudent, but jury-demand procedure (deadline/waiver) is expressly flagged as having no library authority — confirm locally before filing.
4. **Replaced a vague figure with exact arithmetic (§7.3).** "Roughly $85,000" → **$84,916.40** ($110,916.40 − $26,000.00), still flagged as the client's unverified account.
5. **Aligned the §1446(c)(1) reference (§4) to the library text**, which frames the one-year bar as applying to removal "under (b)(3) on the basis of diversity" — now quoted as excerpted, plus a note it's moot.
6. **Corrected a stale section heading (§4).** "(even though removal is not recommended)" → removal is *barred*, cross-referenced to §5.
7. **Made the §6 table counting notation unambiguous.** "Sep 12 + 21" style entries (which invite off-by-one challenges) became "day 21 counting Sep 12 as day 1" with the segment sums shown. Also added a robustness note on Rule 16(b)'s 60-day-appearance prong: whether the appearance is the removal (Oct 13 → Dec 12 Sat → Dec 14) or the answer (Oct 20 → Dec 19 Sat → Dec 21), the 90-day prong (Dec 10) controls either way. Completed the 26(f)(1) rule wording ("before a scheduling conference is held or a scheduling order is due").
8. **Sharpened the summons description (§3).** The 14-day "demand that plaintiff file" mechanism is now described precisely (plaintiff must file within 14 days of the demand or service is void — verified against the summons text), with mootness explained.
9. **§8 unverified list updated** to include jury-demand procedure and claim aggregation; **footer note added** that the INDEX "Citation" column is shorthand for each excerpt file and every cited provision (including §1332(c)(1) and §1446(c)(1)) appears in the named file.

**`deadlines.json`**
10. `removal_reason`: "Caleb Sorensen's Seattle citizenship" → softened to client-reported residence with domicile-assumption flagged (consistent with memo §8); fixed dangling grammar "against removing" → "against the removing party." (One edit briefly broke JSON quoting; fixed and re-validated — all required keys present, all dates unchanged.)

## Verified with no change needed
- All dates re-computed in Python: answer **Oct 1**, removal **Oct 13** (Columbus Day roll), federal answer **Oct 20**, scheduling order **Dec 10**, 26(f) conference **Nov 19** — all confirmed, including the Dec 19→21 and Dec 12→14 rollovers.
- Every quoted rule/case text matches its library file verbatim (CR 12(a)/6(a)/6(e)/4(a)(2), §1446(b)(1), §1441(b)(2), §1447(c), §1332(c)(1), Rule 6(a)(6)(A), 6(d), 4(h), 81(c)(2), 16(b)(2), 26(f)(1), CR 55(a)(3), *Johnson*).
- The "Agreement §14 and RCW 4.84.330" reference is a verbatim recital of the complaint (¶ prayer), used only to identify what's excluded from the amount computation — accurate as description, not cited as authority.
- `QUESTIONS.md` — clean, unchanged.

**Status remains COMPLETE WITH OPEN ITEMS** — the open items (domicile confirmation, spoilage documentation, butter-handler identity, service-validity assumption) are unchanged and flagged in memo §8. The one live deadline is untouched: **answer due Thursday, October 1, 2026.**