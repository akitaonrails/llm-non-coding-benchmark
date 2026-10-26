Good call — a full pre-delivery audit. Let me re-read every deliverable end to end and verify the legal propositions against the actual library text (not just filenames):

The FMLA library checks out (interference language, §825.220(c), "need not have begun it," remedies list — all verbatim support). Now let me read the full advice memo and the remaining deliverables, and pull the exact library text for the other propositions I rely on.

Three library propositions verified verbatim (Oubre "keep the severance and sue"; prompt/impartial + outside-accused's-chain + Faragher/Ellerth undermining... — confirming two suspected issues in the memo: the "failed retaliation defense" sentence and the conflated "prompt = days-to-weeks" gloss). Continuing the audit — now the JSON and the other three deliverables, plus the remaining library propositions:

JSON audited — several checks pass (Columbia and Title VII propositions are verbatim library language; Oubre support confirmed). But I found **two real errors in the JSON**:

1. **Claim 2, key fact 3**: the 10-02 email is described as "**6 days** before the termination request" — the math is email 10-02 → request 10-06 = **4 days** (the "6 days" belongs to the FMLA-request gap 9-30 → 10-06, and the advice memo already states 4 days correctly).
2. **`comparator_analysis`**: "Every employee in the PIP-eligible performance band (≤88%) is male... and untouched" contradicts Dana herself, who is female and in that band — needs "**Every *other* employee**."
3. Also a run-on sentence in claim 3 key fact 2 (two sentences fused at "[library/title_vii_704a.md]").

Let me fix those now, then finish reading the remaining three deliverables:

JSON fixed. Now the three memo fixes identified earlier, plus final reads of the remaining deliverables:

Cross-references check out: `QUESTIONS-1`/`QUESTIONS-2` in the terms memo and advice memo map correctly to the renumbered remaining questions (agreement text = 1, severance policy = 2); litigation-hold language matches the library verbatim. Now let me verify the performance-trend figures against the source documents (the memo asserts a five-point trend spanning "four years" — I want to confirm that against the personnel file) and read STATUS.md:

STATUS.md is consistent with the deliverables (claim 2 reference for the renewed directive ✓, arithmetic list ✓, open items ✓ — all verified against the source documents just read).

The source docs confirm the trend narrative is accurate: personnel file shows 118% (2022, Exceeds) → 101% → 96% → 92% → 88% (YTD Q1–Q3), so "−30-point slide over four years" and "rated 'Meets' every year **since 2023**" are both exactly right (2022 was "Exceeds," and both deliverables correctly say 2023-onward).

Now the final validation battery — schema asserts and the full citation audit:

Everything validates. Last step — record the QA pass in STATUS.md so the file history reflects what changed:

Review complete — 7 fixes made, everything revalidated clean.

## What I found and fixed

**Arithmetic/reconciling errors (in `risk_assessment.json`):**
1. **Claim 2 (FMLA interference):** the 10-02 Hale email was described as "6 days before the termination request." Actual math: email 10-02 → request 10-06 = **4 days** (the "6 days" belongs to the FMLA request gap, 9-30 → 10-06). The advice memo already had it right; now both agree.
2. **Comparator analysis:** "Every employee in the PIP-eligible performance band (≤88%) is male and untouched" literally excluded Dana herself — who is female and in that band. Changed to "Every **other** employee."
3. **Claim 3 (FMLA retaliation):** two sentences were fused into a run-on at a citation break; also softened "discriminatory motive" to "retaliatory motive" (the claim is §2615(a)(2) retaliation).

**Unsupported-authority phrasings (in `advice_to_hr.md`):**

4. "Silence reads as denial and hands her an interference claim" was a practical gloss stated like law. Replaced with library-grounded text: §2615(a)(1) reaches interference with "the exercise of or the **attempt to exercise**" FMLA rights — the request alone triggers protection.
5. "A failed retaliation defense also feeds the harassment case" was garbled logic. Rewritten to the library's exact two-part statement: failure to investigate *is itself evidence in a retaliation case* **and** *undermines the Faragher/Ellerth defense*.
6. Calendar table said investigations are "prompt = days-to-weeks, not months" — that borrows the Title VII *proximity* standard, which isn't the investigation duty's clock. Now states the library requires "prompt and impartial," with no fixed clock (and 24 days of nothing is already the problem on this record).
7. §1 heading trim: the email is "direct evidence of intent" (the *practice*, not "FMLA interference," is direct evidence).

## What was checked and found clean

- **Every legal proposition verified verbatim against library text:** *Oubre* "keep the severance and sue"; §825.220(c) negative-factor language; "need not have begun"; prompt/impartial/outside-the-accused's-chain; litigation-hold trigger (complaint + contemplated termination) and consequences; Columbia's "longer limitations period and uncapped compensatory damages"; the Title VII proximity/pretext/direct-evidence triad. All match.
- **Source facts vs. documents:** the five-point trend (118→101→96→92→88) and ratings (2022 **Exceeds**, "Meets" since 2023) are stated correctly in both files; 7.5-year tenure matches the 2019-04-15 hire date; all quoted client admissions verbatim.
- **Cross-references:** `QUESTIONS-1`/`QUESTIONS-2` map correctly to the renumbered remaining questions.
- **Revalidation:** `python3 -m json.tool` clean; schema asserts pass (`terminate_today: "no"`, `litigation_hold: true`, 6 claims / 7 defects / 8 steps, exact keys); citation audit across all five deliverables — no reference outside `library/INDEX.md`.

All changes are logged in a new "Final QA pass" section in `STATUS.md`. Status remains **COMPLETE WITH OPEN ITEMS**.