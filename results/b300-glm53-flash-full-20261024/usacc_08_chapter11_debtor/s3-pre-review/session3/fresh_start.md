# Fresh-start reporting determination — Redwood Fabrication, Inc.

**Case:** No. 26-11842 (Bankr. D. Colo.) — plan confirmed **9/2/2026** (Dkt. 214), effective
date **9/30/2026**.

**Rule (library: `asc852_fresh_start.md`, in force):** fresh-start reporting is applied upon
emergence **only if both** conditions are met:

- (a) the reorganization value of the assets of the emerging entity **immediately before the
  date of confirmation** is **less than** the total of all post-petition liabilities and allowed
  claims; and
- (b) holders of existing voting shares immediately before confirmation receive **less than
  50 percent** of the voting shares of the emerging entity.

If either condition fails, the entity does not adopt fresh-start reporting.

## The test, with numbers

| Prong | Requirement | Facts from the record | Result |
|---|---|---|---|
| (a) | reorg value < post-petition liabilities + allowed claims | $14,000,000 (reorganization value per Corbin — Dkt. 214 excerpt, term sheet) vs. $16,200,000 (post-petition liabilities + allowed claims — same sources) | **Met** — 14,000,000 < 16,200,000 (shortfall $2,200,000) |
| (b) | existing equity receives < 50% of new voting shares | old equity **retains 60%** of reorganized equity (term sheet; repeated in the Dkt. 214 excerpt) | **Not met** — 60% ≥ 50% |

Two record caveats, neither outcome-relevant:
- *Prong (b) assumption:* the 60% is treated as voting shares — the record describes it as an
  interest in "reorganized equity" and says nothing that would make it non-voting.
- *Prong (a) valuation date:* the record supplies a single reorganization value (Corbin,
  "effective-date basis"); it is used here as the test value. Prong (a) is not
  outcome-determinative because prong (b) fails.

Both prongs are required. Prong (b) fails.

## Conclusion

**Redwood Fabrication, Inc. does NOT adopt fresh-start reporting** upon the 9/30/2026 emergence.

This was foreseeable from the term sheet read in Session 2: the 60% retention by old equity is a
business term of the plan fixed before confirmation; no presentation choice can change it. Prong
(a) passing does not matter — the test requires both conditions.

## Consequences (same library rule), applied to this emergence

1. **Liabilities compromised by the plan are stated at the present value of amounts to be paid.**
   For the GUC pool: $2,940,000 payable over 24 months, stated at PV. The installment calendar and
   the discount rate are not in the record — **QUESTIONS.md Q13**. Until answered, the plan
   payables are presented at the undiscounted $2,940,000 and flagged as pending (PV will be lower).
2. **The gain on discharge is reported as a reorganization item in the income statement** — not in
   paid-in capital or equity. Interim measurement: carrying amount of the liabilities subject to
   compromise $8,400,000 − plan payables $2,940,000 = **$5,460,000** (undiscounted placeholder,
   same Q13 dependency; final = $8,400,000 − PV, so the gain rises as the payables fall).
3. **No reorganization-value restatement of assets and no goodwill.** The library's fresh-start
   mechanics go with adopting fresh start; since it is not adopted, the Corbin $14,000,000 stays a
   disclosure datum and assets remain at carrying amounts. The library prescribes no asset
   write-up on the no-fresh-start path.
4. **During-the-case presentation carried through the effective date** (ASC 852-10-45-4 to 45-6,
   library): liabilities subject to compromise presented separately from post-petition
   liabilities; pre-petition liabilities not netted against post-petition assets. The MOR Part 2
   presentations followed exactly that split ($74,110 documented pre-petition trades;
   post-petition payables on separate lines).

## Tax overlay (library: `irc_108.md`)

The $5,460,000 book gain has no current taxable-income counterpart: the corresponding COD income
is excluded under 26 U.S.C. §108(a)(1)(A) (discharge in a title 11 case) and applied to attributes
under §108(b)(1) — NOL $6,100,000 → $640,000. See `cod_schedule.json`. Deferred-tax effects of
the gain and of the attribute reduction cannot be quantified without tax rates (**Q14**) — the
library is silent on rates, and none were assumed.

## Open items

- **Q13** — GUC installment calendar (incl. the effective-date first installment) and discount
  rate → PV of the plan payables and the final gain figure.
- **Q14** — 2026 (year-of-discharge) NOL, completeness of the §108(b) attribute list, tax rates.
- **Q15** — effective-date data (exit financing, final DIP payoff, 9/30 carrying values) if a
  fuller pro-forma balance sheet is wanted beyond the discharge/gain presentation CONTRACT.md
  requires.
