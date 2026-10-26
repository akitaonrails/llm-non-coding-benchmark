Reviewing everything before delivery — first, pulling the source documents and cross-checking the Session 5 numbers against them:

Quotations and party names check out. Two details to pin down — the full Sept. 29 letter text (does it actually reference $112,000? is the payment promise conditional?) and the hire names:

The Sept. 29 letter reveals two things I mis-cited, and the email export reveals a worse error — I have the wrong initials for the hires in the term sheet. Verifying my remaining assumption labels and checking whether the letters repeat the bad initials:

Re-reading the term sheet in full to apply the fixes precisely:

Both files confirmed. Applying the six fixes — first the four term-sheet corrections:

The Structure B edit didn't match — checking exact indentation:

Now the drafting notes (interest breakdown fix + de-linking note + Structure A implied-fee note):

Updating `STATUS.md` to match the corrected Structure B, then re-validating the JSON:

All arithmetic reconciles. Final sweep of the edited file for any remaining stale references:

Audit complete — everything now reconciles. Here is the review result and the change list.

## Errors found and fixed

**In `session5/term_sheet.md` (5 errors, all introduced in the final draft):**

1. **Wrong hire initials (§2).** I had "Priya N., Luis B., Keisha D., Anne K., Victor O." The roster in `documents/email_export_juniper.txt` reads **Priya S. (RN), Luis F. (RN), Keisha B. (LPN), Anne O. (RN), Victor H. (CNA)**. Corrected, with roles now stated — which also supports the fee-upside argument. (Earlier deliverables already had these right; only the term sheet was wrong.)

2. **Unsupported attribution of the $112,000 ceiling (§2).** I had written that the ceiling "equals the per-hire rate implicit in the $112,000.00 figure **Pinecrest's own correspondence references**." That's doubly wrong: the $112,000 actually originates in *our client's* `damages_summary.md` (7 × 25% × $64,000), and Pinecrest's Sept. 29 letter merely characterizes it as a demand we never made. Importing it into the hand-off instrument would breach the A8 discipline and hand them a phantom-demand talking point. The parenthetical was also incoherent ("ceiling equals … 5 × $16,000 = $80,000 floor"). Replaced with an independent derivation: floor $80,000 = 5 × 25% × $64,000 (roster average); ceiling $112,000 as certainty of total exposure against higher RN pay.

3. **Structure B omitted J-4533 entirely — a $74,568 giveaway.** As drafted, Structure B paid only the conceded four + fees, so a signed release would gift away J-4533 (EV ≈ $62,773 at p = 0.85). Restructured into three tranches: (i) undisputed **$279,351.50** in 10 days, (ii) J-4533 net **$74,568.00** in 30 days, (iii) fee tranche in 60 days. Verified: 279,351.50 + 74,568.00 = 353,919.50 = $336,900 claimed + $17,019.50 interest through Nov. 30.

4. **Date mislabel inside Structure B.** "$276,699.50 … interest through Nov. 30" was wrong — $276,699.50 is the through-Oct.-31 figure. All Part II payment figures are now true Nov. 30 figures, and the drafting note gives the correct accrual split ($2,652.00/mo undisputed four; $717.00/mo J-4533; $3,369.00/mo total) instead of the vague "+ one month" line.

5. **Truncated quote changed a concession's meaning (Recitals).** The Sept. 29 letter says Pinecrest will pay the undisputed balance "**upon resolution of the conversion-fee issue**" — my quote dropped the condition, making it look unconditional. Full quote restored, and Structure B (i) is now expressly drafted to pay *without* that condition, with a drafting note on how far to concede if they push back.

**Minor clarity fixes (no numbers changed):**

6. `term_sheet.md` Part I table + `settlement.json`: J-4533 amounts now show **billed $74,800.00 less our $3,100.00 credit = $71,700.00 claimed**, so the EV table reconciles to `open_invoices.csv` (CSV shows 74,800; our claim runs on 71,700). Recitals likewise note the credit ($340,000 billed → $336,900 net claimed), and the Part I conceded-invoice row now flags that their written promise is fee-conditioned (the 0.95 already priced that risk).
7. Added a Structure A drafting note: a $385,000 lump against $353,919.50 of invoice value embeds only ~$31,000 of fee value vs. the $80,000 floor — the client should see that trade before fixing the number.
8. `STATUS.md` session-5 bullet updated to the corrected Structure B figures; JSON re-validated (schema keys exact, values unchanged: [330000, 410000] / 300000 / 150000).

## Verified correct (no changes needed)

- **Authority check:** every citation in all five sessions traces to `library/INDEX.md` — FAA §§2–4, Rule 12(b)(6)/*Iqbal*, *Ashby*/Restatement §§766–773, CJI 14.02/16.10, RPC 3.1/3.3/1.4, *Zuniga v. Mercer*. All cost/timeline/probability figures are labeled UNVERIFIED or counsel judgment.
- **Core arithmetic:** $340,000 billed total (CSV), $336,900 net claimed, interest $13,650.50 (Oct. 31) / $17,019.50 (Nov. 30), demand $430,550.50 / $433,919.50, EV $380,837.88, BATNA $328,337.88, their ceiling ≈ $478,338–$598,338, and the $862,000 reconciliation all re-derived in Python.
- **Party names, Exhibit/Schedule references, and quotes** (Bell email verbatim, Sept. 29 letter passages) match the source documents.
- **A8/A9 discipline:** no outbound-facing text asserts an earlier demand was transmitted or repeats "never consented" — the ceiling fix actually removed the one remaining leak.

The one thing I could not verify is anything outside the file (AAA fee schedules, arbitration timeline), and those items are flagged as estimates wherever they appear. The deliverable set is now internally consistent end-to-end and ready for client review — still gated on the client's reply-letter approval, written tort-abandonment confirmation, and the final Structure A number.