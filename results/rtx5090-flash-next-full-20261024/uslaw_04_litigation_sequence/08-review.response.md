Good discipline. Let me re-verify every factual and legal assertion in the two session-5 files against the record.

The record now fully confirms the four fixes needed. Applying them:

Clean. Remaining term-sheet fixes:

Re-validating the JSON and the Oct. 20 offer terms cited in the recitals:

All cross-references check out. One last precision edit in §I (the $2,652.00/month rate applies only to the four deemed-accepted invoices, not J-4533), then a final read:

Review complete. Here is what I checked, what was wrong, and exactly what I changed.

## What I re-verified
Every factual, legal, and arithmetic assertion in `deliverable/session5/settlement.json` and `term_sheet.md` against `documents/open_invoices.csv`, the agreement (via `pdftotext`), the email/text records, the Sept. 29 Halvorsen letter, our session-1/2 letters, and `library/INDEX.md`.

## Errors found and fixed

**1. The J-4533 timeliness claim was wrong and self-contradictory (the big one).**
- The term sheet said Pinecrest's July 9 audit notice "postdates the §2 15-day dispute window." But `open_invoices.csv` shows J-4533 was due **July 31** (receipt ≈ July 1, window ≈ to July 16) — the notice was almost certainly **timely**. Their Sept. 29 letter affirmatively asserts it was "within 15 days," and **our own Oct. 25 demand letter already conceded the notice was timely**. Asserting untimeliness now would contradict our own correspondence — a Rule 3.3/consistency problem, not just a tactical error.
- Fix: removed from the term sheet §I basis and from the JSON reasoning (which said the notice "came months after" the window). Both now lean on what the record actually supports: four months of silence, no audit findings, no line-item itemization, no proposed adjusted figure — only the $3,100 defect our client found and credited.

**2. J-4533 interest waiver was miscalculated.**
- "≈$2,151.00 through Oct. 24" assumed a June 30 due date. From the true due date (July 31), at $717.00/month, full months through Oct. 24 = **≈$1,434.00**. (The $2,151 figure in the older session-1/4 files is a "up to… 3 mo" cap through Oct. 31 — defensible as of those dates, so I left the historical files untouched; the current correct figure is now in session 5.)
- Fix: term sheet §I waiver bullet now shows the full arithmetic: $71,700 × 1% = $717.00/mo, two full months (Aug, Sep) = $1,434.00 through Oct. 24, continuing to accrue.

**3. Unsupported characterization of the $64,000 figure.** Term sheet §II called it "Juniper's **documented** assumption" — it isn't documented in either direction. Relabeled "stated assumption — **unverified in both directions**" (matches how `settlement.json` already treats it).

**4. Agreement date.** "dated Jan. 15, 2024" → the PDF says "Effective January 15, 2024." Corrected to "effective."

**5. Signature block titles.** Lindqvist is Pinecrest's **Administrator** (she signed the agreement), not "counsel," and outside counsel is Halvorsen & Price; Okonkwo is Juniper's CEO. Block rewritten accordingly.

**6. Interest accrual line ambiguity.** "on the unpaid balance" at $2,652.00/month could read as including J-4533 (which accrues at $717/mo more, if at all). Clarified: rate applies to the **four deemed-accepted invoices** only.

## What checked out (no change)
- All invoice amounts/due dates vs. CSV; floor $377,747.50, ceiling $425,747.50, midpoint $401,747.50; interest $8,847.50 (through 10/24), $16,803.50 (12/31), $43,323.50 (10/31/27); PV of their Oct. 20 offer $256,160.04, gap $121,587.46; arbitration projection $421,883.50.
- Citations: *Zuniga v. Mercer* and FAA §§2–4 confirmed present in `library/INDEX.md`; the consent-award mechanism is already labeled "standard practice, not a library citation." No other authority appears in the session-5 files.
- Term dates (term to Jan. 14, 2027; §3 tail to Jan. 14, 2028, flagged as subject to §4 notice history), the seven hires and their roles, the Feb. 11 waiver quote, the "undisputed" concession, the abandoned-tort statement (matches reply letter ¶1.1 verbatim in substance), and the Oct. 20 offer terms.
- JSON re-parses cleanly; all four required keys intact.

`deliverable/STATUS.md` now carries a dated review paragraph recording these six corrections. The session-5 files are deliverable.