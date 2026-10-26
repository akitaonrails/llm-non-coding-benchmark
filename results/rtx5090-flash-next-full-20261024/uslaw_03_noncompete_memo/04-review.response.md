I'll do a real review pass: full read of all four deliverables against the library and documents, then arithmetic and cross-reference checks.

One real citation error found: the memo and QUESTIONS.md quote §15.51(c) as "not recoverable for a breach that occurs before judicial reformation" — language that is **not** in the library excerpt (which says the court "may not award damages for breach before reformation"). Let me fix that everywhere.

Now a comprehensive check that every authority named in the memo prose has a `citations.json` entry:

Self-review is complete and all four deliverables are final. Here is the change list you asked for — it mirrors the itemized log in `workspace/deliverable/STATUS.md` (items 1–25).

## What the review found, and what changed

**Two arithmetic/labeling errors (both would have misled you):**
1. **Litigation cost range (§7).** An earlier draft gave $296,200–$428,500. That band was mislabeled: it held the fee-shift probability fixed at 70% and varied only the fee figure. Varying both variables, the true corners are **$289,600–$441,250**, midpoint **$362,350**. The memo now shows the arithmetic and replaces the four-entry break-even list with a full 15-cell table (cost × win probability).
2. **QUESTIONS.md Q10** repeated the same error, claiming break-even "exceeds $12M at our highest win probability." False: at our cheapest cost and highest win probability break-even is **$9.7M** ($289,600 ÷ 0.03).

**Five places the memo asserted more than the closed library supports:**
3. §3 timeline: our two sources described the same signing event differently ("2 hours" vs. 9:12→11:05 a.m. = **113 minutes**). Now reconciled and labeled; nothing turns on it.
4. §3 restraint period made precise: 24 months from the 2026-09-30 separation runs to **2028-09-30**, i.e. **718 days** from Kestrel's start (717-day alternative convention flagged, not silently resolved).
5. §15.51(b) is now quoted as the **conditional** it is — the burden falls on Meridian *if* the agreement's primary purpose is personal services; no library case applies that predicate.
6. The reformation point ("§15.51(c) cannot supply a missing ancillary basis") is now labeled **our reading of the text, not a library holding**, and added to the unverified-law list.
7. §5.4's injunction chain named only two of its three factors. The third (P(Texas court grants emergency relief on the merits) ≈ 0.25–0.50) is now stated, the chain is flagged as conditioning on §14 surviving, and the **contacts-gated variant** is added: **0.09%–1.5%**.
8. **This one makes Meridian's own exposure larger:** §16600.5(c) and (e) both reach a "**prospective employee**," which the memo had omitted. The claimant pool is not limited to people Meridian hired — it includes candidates required to sign the form.
9. §5.7(c) had blurred two different questions about pre-2024 hires: whether their contract is enforceable (answered by §16600.5(a)) vs. whether pre-2024 hiring conduct is itself a "civil violation" (an **unverified** reach-back, no longer asserted).
10–11. Two §9 recommendations hedged: "no law would let Meridian obtain an enforceable employee non-compete" (the library does not contain the §16600 exception provisions, so we can only say we find no route **on this library**), and "trade-secret claims are not an attempt to enforce" (the library never defines "attempt to enforce" — brief it before filing one).
12. *Edwards* is recorded as disapproving *Campbell* and *General Commercial Packaging* "**to the extent inconsistent**," the library's wording, not flatly "disapproving."
13. §10's memo-bank treatment corrected three ways: *Westbrook*'s en banc rehearing was **granted and argued January 2025** with no later disposition in the library (so we assume neither reversal nor affirmance); the 2025 update's premise that the FTC rule was "enjoined" conflicts with the verified record — *Ryan* **vacated it nationwide** and the FTC **acceded to vacatur** — and that error is now on the page; and the Rule's Federal Register date (**May 7, 2024**) post-dates Zhao's March 4, 2024 agreement.
14. The §6 spoliation warning is now labeled risk management, because that doctrine is not in the library. The advice is unchanged.
15. The unverified-law list grew by three entries (pre-2024 reach-back; whether §15.51(c) cures a missing ancillary basis; spoliation doctrine).
16. **`citations.json`: 8 of 20 propositions rewritten** to track library text exactly — §16600.5 (adding "prospective employee"; restoring (b)'s full "signed and the employment was maintained **outside of California**"), §16600.1 (restoring (b)(1)'s "does not satisfy an exception" qualifier; (b)(2) is "last known address," which we had rendered as "mailing address"), §§15.50–15.52 (conditional burden, full exclusivity language), *Light* ("overruled/modified" by *Sheshunoff*, not "no longer good law"), and three entries where we had mixed argument into the holding.
17–18. A duplicated sentence we introduced in §5.3 was deleted; the Brief Answer table, recommendations, Q3/Q10 and the STATUS bottom line were aligned to the corrected figures.

**Second pass — quote fidelity:**
19–21. Eight quoted phrases had been re-capitalized to start our own sentences; now bracketed to the library's case ("[p]rimarily resides…," "[a]s a condition of employment," "[a]djudicate outside of California," "[d]eprive…," "[a]ncillary to **or part of**," "[a]n employee, former employee, or prospective employee," "[t]he FTC's appeal…"). A truncated §925(b) quote was completed ("…California law shall govern **the dispute**"). And the Brief Answer had quoted §925(a)'s words as though Meridian's agreement said Zhao "primarily reside[d] and work[ed] in California" — it doesn't; the agreement says his work location was "Remote — Employee's residence (Oakland, California)." Both spots now quote the agreement as the fact and §925(a) as the trigger it satisfies.

**Third pass — validators and one more hedge:**
22–23, 25. Every quoted span (198) in the three prose files was checked against `library/**`, `documents/**`, and a text extraction of the agreement PDF; every non-matching span is the client's own words, our own superseded Rev. 1 wording being corrected, or our shorthand in scare quotes — none purports to be source text. Citation validator: 20 entries, all four keys uniform, every `library_file` in `library/INDEX.md`, every `status_checked` equal to the INDEX Status column, zero memo-bank entries, all 20 citable authorities used exactly once. Arithmetic: 32 recomputations plus the four chain products, no discrepancies. Every case name in the memo was matched to a citation entry — only *Calderon* and *Westbrook* are not, and they appear solely inside the §10 warning that they are not in the library and support nothing.
24. The Brief Answer row on Meridian's own violation now names the provisions (§16600.5(c), §16600.1(b)) and says the answer is subject to the chapter's exception provisions, which this library does not contain.

## What did not change

- **Recommendation: do not file in Travis County; send no §8 or §9 demand letter; cure the AB 1076 notice gap company-wide in the §16600.1(b)(2) form; scrub §8 from the engineer form; confidentiality/trade-secret channels only; litigation hold today.**
- Every probability: §925 voids §§14/venue 75–90%; Texas law reaches §8 5–15%; §8 void under California law 95%+; ancillarity 25–40%; end-to-end injunction **0.3%–3%** (contacts-gated 0.09%–1.5%); contacts-only jurisdiction 30–50%.
- The economics: **$362,350** expected filing cost, **$289,600–$441,250** true corners, labeled as our assumptions (Q10).
- The refusal to keep the notice failure out of writing, converted instead into a preservation and compliance instruction (§6).

Still open, and listed as such: 10 items, the largest being the unproduced full employment agreement (any employer-side promise in it reopens the ancillarity estimate) and the "Alvarez matter," which may be pre-existing §16600.5 exposure independent of Zhao.