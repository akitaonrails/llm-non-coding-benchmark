Good discipline. I'll audit systematically: (1) rebuild the authority whitelist from the library, (2) re-read every deliverable against source docs, (3) re-run every arithmetic chain in Python, (4) fix what fails.

Library whitelist captured (7 files). The /tmp extracts were cleaned again — regenerating:

Library captured. Now reading every deliverable in full for the audit:

Redline read. I've already spotted a problem in the §3509 arithmetic (line 67). Reading the remaining deliverables and JSON:

The JSON read truncated at line 100. Let me get the rest, STATUS.md, and grep every occurrence of the §3509-derived figures:

All §3509-derived figures located. Now I need exact current text for edits — re-reading the files in full (earlier reads truncated):

Now re-running the corrected arithmetic in Python and pulling the full JSON + remaining unread sections:

Citation whitelist verification: all reporter cites match library strings, including *Lazard* `114 A.3d 193 (Del. 2015)`, *Marsh USA* `354 S.W.3d 764 (Tex. 2011)`, *SQL Solutions* `1991 WL 626458 (N.D. Cal.)`, and *Akorn* cited as `(Del. Ch. 2018) (dicta)` without an invented reporter number. One last check on the `§15.51(c)` subsection cite:

§15.51(c) is in the library — good. Now re-reading the exact edit target lines to ensure precise replacements:

Applying the corrected figures now — first pulling exact text of remaining edit targets:

All target strings located. Applying the corrections across all six files:

Redline and reply corrected. Now the client note, JSON findings, and QUESTIONS:

Now STATUS.md — stale figures plus a pre-delivery audit log entry:

All edits applied. Final verification pass — JSON validity/schema, stale-figure sweep, and new-figure consistency:

The two STATUS hits are the audit log itself (deliberately quoting the corrected error). Consistency check on the new figures:

QUESTIONS.md showing 0 combined-band hits — checking whether its band reference updated (it intentionally carries only component bands, but the indemnity band should read $150k–$250k):

Pre-delivery review is complete. Verdict: the package is internally consistent and deliverable, but the audit found **one substantive arithmetic error and one drafting inversion**, both now fixed across all six files.

## What changed

**1. The §3509 employment-tax math was wrong (the significant one).**
The old figure — "$18,544/yr = 1.5% × wages + 20% × employer FICA → ≈$56,800 over 3 years" — used a rate factor (20% of employer FICA) that matches no reading of §3509, and silently ignored whether the employer's own FICA share is even reduced. Replaced everywhere with a dual-reading band (Python-recomputed; all rates still labeled unverified working assumptions, since the library cites §3509 but no percentages):

- **Low reading** (§3509(a) as all-in reduced substitution): $9,180 income tax + $23,409 half-FICA + $378 FUTA = $32,967/yr → **≈$99,000 over 3 years**
- **Standard practitioner reading** (full employer FICA + half employee-side): $79,785/yr → **≈$239,000 over 3 years**
- Combined with the FLSA band: **$126,400–$383,300** (was $84,300–$200,700)
- Buyer's full-price cap restated as **~8–25x** the band (was "15–35x")
- Special-indemnity discussion band restated **$150k–$250k**; the drafted number stays **$150,000** — the cap's job is to fix exposure at a negotiated number, not to match the band's top

Updated in `apa_redline.md`, `reply_to_buyer_counsel.md`, `note_to_ray.md`, `diligence_findings.json` (findings 2 and 5), and `STATUS.md`.

**2. Redline §2.4 drafting inversion fixed.** Our own earn-out replacement read "(ii) **include** all costs of the spray-booth permit transition" — the opposite of the seller protection clause (i) was designed for. Now "**exclude** all costs of the spray-booth permit transition and any interim-operating costs attributable to the permit not transferring."

**3. `QUESTIONS.md` rate list corrected.** The old parenthetical "(1.5% / 20% vs 28% / 35%)" misstated the statute; rewritten as 1.5%/2% of wages + 50%/100% of the §3111 FICA amount, with an explicit note that the employer-FICA ambiguity drives the ~2.4x spread. Two new assumption flags added: the 3-year federal assessment period, and that 2025 payment levels are assumed for each lookback year (avg tenure 3.4 yrs makes it reasonable, but earlier-year payments aren't in the data room).

**4. `STATUS.md`** now carries a "Pre-delivery audit" log documenting the error, the correction, and what was re-verified.

## What was checked and came back clean

- **All other arithmetic re-verified unchanged**: implied price $3.1M (escrow $310,000 = 10% per §9.3); earn-out (max payout needs $1.7M EBITDA; $16,000 at $740k; $518k unadjusted = $182k below hurdle); basket $75k ≈ 2.4%; known claims $32,800 under basket; Hensley 0.38 × $4.6M = $1,748,000; escrow = general cap; FLSA $765–$1,845/week × 12–26 wks × 3 yrs; the 1,813 hrs/yr/installer sanity check; WARN counts (14 W-2 / 23 total vs. 100 threshold).
- **Citation whitelist passed**: every authority in the deliverables appears verbatim in `library/INDEX.md` files — *SQL Solutions* 1991 WL 626458, *Marsh USA* 354 S.W.3d 764, *Lazard* 114 A.3d 193, §§15.50/15.51(c), 29 U.S.C. §2101(a)(1), 29 C.F.R. §639.3, Rev. Rul. 87-41, Treas. Reg. §31.3121(d)-1 — and *Akorn* is cited as "(Del. Ch. 2018) (dicta)" exactly as the library has it, with no invented reporter number.
- **JSON schema valid**: 14 findings, all five required fields, all `deal_impact` values in the CONTRACT enum.
- **Stale-figure sweep clean**: no old numbers survive anywhere except the audit log itself, which deliberately quotes the corrected error.

All five deliverables under `/work/deliverable/` are now reconciled to the corrected figures and ready to send.