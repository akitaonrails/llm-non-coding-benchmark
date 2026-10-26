Client answers received. Two material updates: (1) refinance feasibility is now a planning question I must answer with arithmetic, and (2) the bonus is *recurring* (prior year ~$40k), which strengthens both the estate and support arguments. Let me run the new numbers — deferred-sale §121 mechanics, refinance arithmetic, and the recurring-bonus sensitivity:

Format-string glitch — rewriting with f-strings:

Now the remaining round-2 edits: `advice.md` (targeted sections), then `QUESTIONS.md` → answered/flagged log, then `STATUS.md`.

Now the two big rewrites — Section 5 and Section 8:

Now rewrite `QUESTIONS.md` as the round-2 Q&A log and update `STATUS.md`:

Final validation — parse both JSONs and cross-check the key figures that appear in multiple files:

All deliverables are now consistent with the client's round-2 answers. Round 2 complete.

## What changed

**1. Her refinance question — answered with arithmetic, not a question back.** P&I on the $400k loan is **$2,648/mo = 44.1% of her $6,000 gross** before taxes/insurance, and still **33.0%** even counting support income (which expires at month 36). She has no pre-approval. Verdict: treat refinance as infeasible — but that no longer forces a sale.

**2. New primary plan — Scenario A2, deferred joint sale (the answer to "stay 3–6 years without refinancing"):**
- Decree keeps both on title/mortgage, Wife occupies, fixed sale date, 50/50 net proceeds, principal-paydown credit to whoever pays (~$24,221 over 36 months).
- **§121(d)(3)(A) deemed-use** (`library/irc_1041_121_71.md`) keeps Husband's $250k exclusion alive while Wife occupies under the decree — so at a post-divorce joint sale **each claims their own $250k**, no joint return needed.
- At today's price: tax **39,546** (her 17,550 — MAGI 189k stays under the $200k NIIT threshold — vs his 21,996), *cheaper* than the immediate joint-return sale (43,992). Estate 1,360,654 → **$680,327 each** with a QDRO ~$134,211, vs $678,104 under sell-now (B, kept as fallback if Husband won't sign).
- Risks priced explicitly: appreciation past the $500k shelter (illustrative +3%/yr → tax 62,017, her NIIT triggers), Husband's creditors/lien exposure, cooperation risk — with enforcement terms (hard sale trigger, security, housing-cost-as-maintenance: his P&I $2,648 already exceeds his $2,000 cash maintenance offer).

**3. Recurring bonus:** her report ("always gets one; last year ≈$40k") is logged as client testimony — the documented 2026 letter/stubs carry the legal weight; discovery ask added for 2024–2026 W-2s. Support band now shown: **$2,004 / $2,023 / $2,042** (40k/45k/50.4k bonus).

**4. `QUESTIONS.md`** converted to a closed Q&A log — 2 topics answered, 10 remaining unknowns flagged as assumptions/discovery items per her instruction not to re-ask.

**Status: COMPLETE WITH OPEN ITEMS** — both JSONs re-parsed, every cross-file figure re-verified in Python (gap 48,992; A2 = 680,327/680,327; QDRO 134,210.53; support band reconciles). No open item blocks the advice; they are assumptions on the record.