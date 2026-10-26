I'll audit every deliverable line by line before delivery.

Several real problems. Let me fix them, starting with the JSON.

Both audit passes are now on disk and re-verified. Here is the change list.

## Verification state after the edits

`/work/deliverable/risk_assessment.json` — valid JSON, exactly the six required keys, schema intact: **9 claims, 11 separation-agreement defects, 12 recommended steps**, `terminate_today: "no"`, `litigation_hold: true`.
Zero citations to any file outside `library/INDEX.md`. Every quoted term/case we rely on (`2615(a)`, `825.220(c)`, `2000e-3(a)`, `626(f)(1)`, `24-34-402`, `37(e)`, *Oubre*, *Zubulake*, *Faragher*, *Ellerth*, *Burlington Northern*, *Breeden*) exists in the library text. Quote-pairing and quote-fidelity sweeps are clean; what remains inside quotation marks is only (a) labels for standards the library does not contain, explicitly flagged as gaps, (b) contract language we are proposing, which we label as ours, and (c) self-quotations inside the §14 correction log.

## Round one — 7 corrections (logged in `advice_to_hr.md` §14)

1. **§1, the one place we had been stronger than the record.** We had said you "currently have all three" routes to Title VII causation. Wrong. The library's direct-evidence limb requires statements linking the action to the *protected activity*; Hale's 10/02 email links it to *leave*, which is FMLA evidence, not Title VII direct evidence. Causation is now scored route by route: proximity present, pretext present, direct evidence **not available** for Title VII.
2. **§1** — the 24-day complaint-to-termination interval is no longer called "very close" (library says "days to a few weeks" without characterizing it; 24 days ≈ 3.4 weeks). The 4-day complaint-to-PIP interval carries proximity.
3. **§2/§8** — PIP elapsed time restated as of today: 20 ÷ 60 = 33.3% at your 10/06 request, 40 of 60 = 66.7% today, plan closes 11/15. Both figures kept, each labeled with its date.
4. **§5** — "anyone over 40" → "any employee the ADEA protects." The library's ADEA file contains only the waiver provision; the age-40 threshold is an assumption, now flagged (`QUESTIONS.md` item 16).
5. **§5 + terms §1** — new flag: the library states the 21-day and 7-day periods but never says **what starts the 21-day clock**. We run it from delivery of a complete writing expressly referring to ADEA rights, labeled UNVERIFIED.
6. **§8** — investigation-by-outsider wording now quoted as the library actually writes it ("should be conducted," not "requires").
7. **Comparators are now sourced, not inferred** — see below.

## The one finding that strengthens the case against terminating

`documents/comparator_data.csv` has a **`complaint_filed` column**: `"no"` for Brennan, Osei, Lind and Park; `"yes (9/12)"` for Dana alone. The library's pretext limb is literally "disparate treatment of comparators who did not complain." That limb was previously an inference we flagged; it is now documented in your own file. Three men with worse attainment (79/84/86 against her 88), no PIP, no complaint.

## Round two — 14 verbatim-quote corrections

The defect class: quotations that were close to the source but not word-for-word, including our own shorthand sitting inside quotation marks. Fixed in all four documents:

- **§12 and `QUESTIONS.md` §E headings** joined non-adjacent sentences of HR's 10/26 message into one quotation, silently deleting the middle sentence. Now each quotes her sentences separately.
- **Four places** quoted a singular "shifting justification." The library says **"shifting or thin justifications."** Corrected in memo §2/§8/§13 and JSON steps 5 and 7 — point unchanged, wording now the library's.
- **`risk_assessment.json` claims 4/8 and comparator analysis:** a quoted `"Exceeds / Presidents Club (2022)"` rating does not exist — `personnel_file_summary.md` puts **Exceeds** in the rating column and **Presidents Club** in the notes column of the 2022 row, **Meets** in 2023–2025. Now: 2022 rated 'Exceeds' with the note 'Presidents Club', 2023–2025 rated 'Meets'.
- A quoted **'unwelcoming'** standard removed — the library never uses that word; the gap it pointed at stays flagged as unverified (item 15).
- **§0 table** — the argument about the undecided leave request was in quotes though no one wrote it. Unquoted.
- **§6** — our paraphrase of Hale's email replaced with the email's words: "nightmare to move on her."
- **§12 subheadings** — compressed HR wording; only the verbatim ones keep quotation marks, and an intro note now says which headings are quotes.
- **§9** — restored to the document's sentence: "The VP wants this done this week."
- **§11** — ratings restated as separate rows (see above).
- **Terms §§4–5 and JSON defects 8–9** — the (B)/(E) OWBPA requirements had been paraphrased inside quotation marks; now the library's wording, with the unverified "or class of employees" scope flagged (the library stops at "offered to a group").
- Our own shorthand unquoted: `PIP at 88%, nothing at 79%`, `sign it this week`, `fire her now or keep her forever`.
- `STATUS.md` self-descriptions brought back in line with the files (spoliation trigger wording, the causation sentence it quotes).

## What did **not** move

No claim rating changed — FMLA interference (pre-leave) high, FMLA inaction medium, FMLA retaliation high, Title VII §704(a) high, harassment medium, *Columbia* analog high, ADEA medium, PIP-as-adverse-action high, spoliation medium. `terminate_today` stays **no**. The OWBPA runway stays 21 days ("Just her. No RIF"), earliest compliant effective date **11/17** with revocation to **11/24** — 9 days after the PIP closes on 11/15, which is why the PIP has to be closed or rebuilt in writing by someone outside Hale's chain before 11/15.

## Still needing your decision (unchanged)

1. Whether to authorize sources outside `library/INDEX.md`. You've twice confirmed there is no further information, so the legal-standard gaps (severity/pattern, "serious health condition," FMLA designation deadlines, whether a PIP is per se materially adverse, the ADEA age threshold, what starts the OWBPA clock) stay flagged as assumptions by design rather than being silently filled in.
2. Whether to **stop the termination in writing today** and have us draft the four operational documents — litigation hold, written stop instruction, Hale's written removal from Dana decisions, written FMLA determination plus outside-chain investigation. Offered repeatedly, never drafted. Say the word and they're an hour of work.