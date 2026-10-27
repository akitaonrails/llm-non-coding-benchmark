Good discipline. I'll re-verify from the source up: documents → library authority → arithmetic → cross-file consistency → contract compliance. Starting with the contract requirements and the library index:

The contract's schema uses exact JSON key names — I need to check my `return.json` against those. Also, the INDEX lists **6** library files, not the 7 that STATUS.md claims. Let me audit both directories in full:

INDEX confirms 6 files. Key finding: the 1040 instructions excerpt contains **no §55/28% comparison rule** — the "28% × TI" check in my deliverables may be unsupported authority. Reading the remaining four library files:

All W-2/K-1/1095-A/1098/1099-INT figures match my computations. Reading the two remaining text documents and the current deliverables:

`return.json` audited — found two real errors: (1) the `section55_minimum_tax_comparison` field cites a rule **not in the library**; (2) the `basis_rollforward` string **omits the 2023 +9,800 income** (and mislabels years) — its sequence multiplies out to 1,700, not the stated 11,500. Now reading the prose deliverables:

judgment_calls.md audited — found: **judgment 8b quotes the 1040 library excerpt for a "26%/28% §55 tentative minimum with 50% limitation" rule — that language does not exist in the library file at all** (fabricated citation); judgment #8's rate-schedule figure (6,708) is arithmetically 6,705; #7's variant AGI "85,600" doesn't compute; #11 repeats 5,217.49; #2's variant TI 43,350 embeds an inconsistency. Reading the last two files:

I have the full judgment_calls.md and STATUS.md context. Now re-reading the exact current text of return.md and return.json sections I need to edit:

Now the full return.json:

All current text in hand. Before editing, I need three exact references: the contract's JSON schema, the judgment_calls.md opening entries (#2 text), and the library's rate-schedule lines:

Schema keys confirmed. Now I need the exact text of judgment_calls.md entries 2, 8b, 10, and 11 to edit:

All exact strings for judgment_calls.md are captured. Now I need the remaining exact chunks — return.md §6–§8, STATUS.md header, return.json middle block, and the library repayment-cap table:

Library caps confirmed ($1,900 for 200–<300%; $3,150 for 300–<400%). Now the tail of return.json and the STATUS judgment-count wording:

All exact text is in hand. Applying the fix list now — judgment_calls.md first (all seven corrections, disjoint anchors):

Line 49's exact text captured. Applying the remaining four judgment_calls.md corrections:

judgment_calls.md complete. Now the five return.md fixes:

return.md complete. Now STATUS.md — the count fix, the judgment-log description, and a review-corrections record:

STATUS.md updated. Now the full `return.json` rewrite to the contract's exact nested schema, with all corrected values:

JSON written. Validating parse + sweeping every deliverable for leftover review artifacts:

Final consistency check before reporting — confirming every remaining grep match is an intentional correction record, not stale content:

Review complete. All checks pass: five deliverables in place, `return.json` parses with the contract's exact schema, and the only surviving traces of the old figures are the deliberate correction records. Here is the full report.

## Pre-delivery review — what I found and changed

I re-audited every citation against the six files in `workspace/library/`, re-extracted all ten source documents, and re-did the arithmetic. **No federal bottom-line figure changed** — AGI $91,350, taxable income $59,850, total tax $6,408, refund **$2,322** all stand. What changed was one fabricated authority, several arithmetic slips, a few unsupported assertions, and the JSON structure.

### 1. Fabricated citation removed (headline finding)
- The draft contained a **"§55 minimum-tax comparison"** (28% × $59,850 = $55,250, "50%-of-taxable-income limitation") attributed to `1040_instructions_tax_computation.md`, complete with a quotation about an "11.2% effective rate" and a "26%/28% §55 tentative minimum." **No such rule, quotation, or figure exists in that file — or in any of the six library files.** The 1040 excerpt's only computation rule is that TI under $100,000 must use the Tax Table.
- Removed from `return.md` §6 (replaced with a visible correction paragraph), `return.json` (`section55_minimum_tax_comparison` key deleted, `fed_status` reworded), and rewritten `judgment_calls.md` 8b as a correction record so the audit trail stays visible. Tax remains **$6,708 from the Tax Table alone**.

### 2. Arithmetic corrections
- **Rate-schedule cross-check** (`return.md` L130, `judgment_calls.md` #8): the draft claimed the schedule gives "6,708.00" at TI 59,850 and matches the table. It actually gives **$6,705** (2,385 + 4,320) — $3 less. The table's $6,708 is the schedule at the bracket **midpoint** 59,875 (2,385 + 4,323). Method conclusion unchanged: table controls under $100,000.
- **Form 8962 annual contribution**: 5,217.49 → **$5,217.46** (91,350 × 5.7115% = 5,217.45525), fixed in `return.md`, `return.json`, and judgment #11; the rejected 12-month-netting variant figures follow to **$4,922.54 / $4,977.46**. Repayment stays **$1,900 either way** (capped), so no tax effect.
- **Form 7203 basis-rollforward string** in `return.json`: had mislabeled years and omitted the 2023 +9,800 income year. Now correct: 2021: 10,000 − 2,100 = 7,900 → 2022: +6,400 → 2023: +9,800 − 12,000 = 12,100 → 2024: +4,600 − 5,200 = **11,500 opening 2025**.
- **Two variant figures in `judgment_calls.md`** (hypotheticals, not the filed figures): #2's full-loss variant TI $43,350 was internally inconsistent (it let the rental allowance stay at 19,550 while allowing the full S-corp loss) — corrected to **$41,882** with the full cascade (MAGI 94,400 → allowance restores to 25,000 → full rental allowed); #7's rejected-MAGI variant AGI "$85,600" was simply wrong — corrected to **$97,100**. Both marked as corrections; both variants remain outside the library's table excerpt, as before.

### 3. Unsupported assertions softened to open points
- **Chase interest NY sourcing** (`return.md` §9): the claim that nonresident-period interest "follows domicile (FL)" cites nothing in the library — now stated as **left unallocated, library silent**.
- **Family-of-3 8962 variant** (judgment #10): "(320%+ territory)" and the $3,150 cap were premised on an unverifiable family-of-3 FPL — now conditional: the cap is $3,150 **if** the variant lands in the 300–<400% band, but band placement itself can't be verified from the library.

### 4. Structural / wording fixes
- **`return.json` restructured** to the contract's exact nested keys (`form1040` with `1a_wages`…`34_refund_or_37_owed`, `form7203`, `form8582`, `form8962`, `dependents`, `ny`), with all detail blocks preserved as extra keys. Validated — parses cleanly.
- **`STATUS.md`**: "seven library documents" → **six** (INDEX lists exactly six); judgment log described as "19 numbered entries (18 judgment calls plus 8b, a correction record)"; a new "Pre-delivery review (corrections applied)" paragraph records the above.
- `QUESTIONS.md` — audited, no changes needed.

### Status
**COMPLETE WITH OPEN ITEMS** — unchanged, and unchanged in substance by this review. The open items are the ones the library genuinely cannot close: NY IT-203 tax/refund amounts (no NY rates in the library), the family-of-3 FPL, the missing 2019 lease (documentary risk only — facts client-confirmed), and the stated assumptions on residency end date (6/30) and household size (4).