Handling this in three steps: (1) finish the remaining deliverables, (2) full self-review sweep against the source extracts, (3) answer Ray. First, re-verifying the exact source language I quoted, since the review must check every quote:

The `/tmp` extracts were cleaned up — regenerating from the source PDFs before the quote check:

All seven library memos are now verified verbatim. Now reading the current deliverables to run the review and finish the rewrites:

JSON verified — 20 findings, all enum values valid; found the "change of of" typo. Now the redline:

`note_to_ray.md` is riddled with fabrications ("Ray Delgado", "Hensley Property Group", the $16,000 non-compete payment, "2017 consent", "45-day Lessor notice", "Hardaway lien", wrong §7.4(c) cite, deprecated $42,188/$268,150/$824,600 figures). A full rewrite is the right fix. Reading the other three stale files:

Now re-reading the engagement spec to lock deliverable requirements before the rewrites:

I have everything verified. Now executing the fix plan — first the targeted fixes to the two current files, then the four rewrites. Let me get the exact gross-up text in the JSON:

Exact strings in hand. Applying the three targeted fixes now — first the redline context around line 179 and 251:

Applying the gross-up consistency fixes and typo fix to both current files:

All four targeted fixes are in. Now re-reading the two stale files in full (they were truncated earlier) so Q-numbering stays stable through the rewrite, and validating the JSON still parses:

JSON is valid (20 findings). Before rewriting Q9, I must verify the DR §5.2 warranty-claims quote I plan to keep — checking the rest of `/tmp/dr.txt`:

All source quotes now verified. Executing the four rewrites — starting with `note_to_ray.md`:

Now the remaining rewrites. First, confirming the exact tail of the old QUESTIONS.md and STATUS.md so the Q-numbering stays stable:

Both old files fully captured. Fixing one integrity issue in the reply I just wrote (it implied Hensley outreach had already begun — the client says the owner hasn't been told, so that must not be said to buyer's counsel):

Now the full rewrite of `QUESTIONS.md` (Q1–Q10 numbering preserved, client answers recorded, stale citations corrected):

Now the `STATUS.md` rewrite with the review-correction log:

The §7.4(a)–(c) zero counts are a regex artifact (unescaped parens in ERE). Re-checking with literal strings:

All required sections confirmed present (the earlier zeros were a regex artifact — unescaped parens in ERE). The full sweep is now complete and clean:

- **Stale/fabricated string scan:** zero real hits across all six files (every `lien` hit was the substring inside "client"; every `$16,000` is earn-out context).
- **Authority check:** the only `library/…md` citations used anywhere are exactly the seven memos in `INDEX.md` — no outside authority cited.
- **Cross-refs:** every Q1–Q10 cited in the other five files resolves to a defined heading in `QUESTIONS.md`.
- **Redline coverage:** §§2.4, 3.3, 4.12, 7.4(a), 7.4(b), 7.4(c), 8.2, 9.3 each have their own section (plus a §7.4(d) survival tune).
- **JSON:** re-parses; 20 findings; schema and `deal_impact` enums valid.
- **Files:** all six deliverables on disk in `workspace/deliverable/`.

---

## Corrections made in the self-review

Logged in full in `STATUS.md` ("Corrections made in the pre-delivery self-review"). Summary:

1. **`note_to_ray.md` — full rewrite.** Wrong client name; a separate non-compete payment figure that doesn't exist in the draft; a non-compete description (2-year term, family-entity sweep) that doesn't match §8.2's actual text ("Seller and Ray Brightline," 500 miles, 7 years); MSA consent/notice mechanics quoted from nowhere in the data room; the Hardaway item mis-described (data room says "dispute ($9,800, warped door)"); cap cites to §7.4(c) instead of §7.4(b); a stale single-point OT estimate and a stale Hensley value anchor computed on mixed bases; and assertions about draft content we never received (a closing-conditions article; a defined-term qualifier on Schedule 3.3).
2. **`reply_to_buyer_counsel.md`.** Exposure table updated to the canonical scenario bands; the consent-status line fixed so it **never implies Hensley has been contacted** (he hasn't — we cannot say otherwise to buyer's counsel); buyer-first outreach steps and lease-notice mechanics removed in favor of the seller-led sequence.
3. **`QUESTIONS.md`.** Q3 had the caps **backwards** — the draft caps Fundamental Reps *and §4.12* at the **full Purchase Price in §7.4(b)**, not at $310,000 in §7.4(c); Q4's covenant description didn't match §8.2; Q5 and Q7 cited the wrong data-room sections; Q8 said ~200 contracts (data room says **22**); Q9's §2.3/§5.1 quotes were paraphrases, now verbatim; Q10's retired single-point number replaced with the current bands; Q2 marked **ANSWERED** with the reconciliation.
4. **`apa_redline.md` + `diligence_findings.json`.** A gross-up sentence that **didn't foot** ("roughly doubling" → a number that wasn't double) replaced with an explicit 1.5× block: $157,578 × 1.5 = **$236,367**; multiples restated to 13.1×–21.4×; a duplicated word inside a quoted clause fixed so the quote matches the library verbatim.
5. **`STATUS.md`.** Finding count (20), memo count (7), and stale open-item text corrected.
6. **Verification pass (no change needed):** every "as drafted" APA quote re-checked verbatim against the extract (including the "[deductible]" bracket in §7.4(a)); §9.3 confirmed to contain **no** sole-recourse language, so nothing quotes it as if it did.

**Reconciliation, not forced:** the one flagged non-reconciliation — installer pay (~$68,000 avg) vs. claimed 45–50 hr weeks — **now ties out** with the client's answer: $68,000 ÷ $37.50/hr ≈ 1,813 hrs/yr = 33–50 hrs/wk across a 40–50-week year, i.e., heavy seasonality, exactly what the client described. Nothing was adjusted to force it; the §2.3-vs-§5.1/5.2 contradiction and the earn-out add-back ambiguity remain **reported as inconsistencies**.

---

## Answer to buyer's counsel ("7.4(c) is market… 4.12 is plain-vanilla")

Full text in `reply_to_buyer_counsel.md` §3. The core:

- **§7.4(c):** We're not disputing the label — pro-sandbagging clauses are common. But a sandbagging clause **plus** a disclosed issue **plus** a clean rep is, per the library memo, the combination where the buyer has "effectively agreed to indemnify for the disclosed issue." Your own file (DR §2.2) discloses 1099 installers while §4.12 reps full compliance. If 7.4(c) is market, then the market companion — a schedule exception, an anti-sandbagging flip, or a sized special indemnity — is equally market. A clean rep is not one of the seller protections.
- **§4.12:** It isn't plain-vanilla **on your own data room**. §2.2's facts map onto the control test in the worker-classification memo; "1099 forever" and "they like it" are not defenses (the label doesn't control; consent/industry-practice defenses aren't in our library — flagged unverified). The rep is untrue as drafted.
- **The math:** 3-yr exposure **$144,648–$157,578** (×1.5 gross-up ≈ **$236,400**) against a §7.4(b) carve-out cap of the **full $3,100,000** price — $2,790,000 collectible beyond your escrow, roughly **13×–21×** the actual exposure. The off-market clause isn't 7.4(c); it's §7.4(b) carving an operational rep out to a full-price cap.
- **The trade:** we'll live with 7.4(c) if §4.12 gets a schedule exception; failing that, a §7.5 special indemnity of **$[250,000], escrow-only** closes it.

## Answer to Ray ("can we just sign?")

**No — not as drafted.** Full plain-English version in `note_to_ray.md`. Three sentences: as written, the clean §4.12 rep + §7.4(b)'s full-price carve-out + pro-sandbagging §7.4(c) means your own disclosure doesn't protect you — you'd back the entire $3.1M for a known worker-classification problem the buyer already knows about. Separately, Hensley's consent has never been requested and is now the critical path (you call the owner first, before any buyer outreach), and the spray-booth permit reapplication (30–60 days, non-transferable) gates the closing date. Signing in two weeks is feasible **if** the §3.3 / §4.12 / §7.4 fixes are agreed first. The earn-out is worth $0–$16,000, not $400,000, so don't trade real indemnity terms for it.

**STATUS: COMPLETE WITH OPEN ITEMS** — drafting is done; the open items are confirmations (Q1 price, permit interim operations, lease guarantee, CPA figures, buyer's responses), each already routed in `QUESTIONS.md`.