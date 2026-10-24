# Pilot observations — not a correctness grade

The benchmark inputs remain frozen. These observations do not change the
candidate's prompts or answers and must be investigated before formal grading.

## Review behavior observed

`usacc_03_household_1040/s1-pre-review/return.json` used $6,702 for tax on
$59,850 of taxable income. `final/return.json` changed tax to $6,708 and the
related total/refund during the fixed review turn. The supplied table puts
$59,850 in the $59,850–$59,900 row ($6,708), not the preceding row. This is a
concrete example of a correction made only on review; it should not be counted
as an unprompted correct answer.

## Fixture issues requiring adjudication

- **BRACC-01 allocation table:** the six percentages supplied for Anexo III,
  fourth band, total 99.85%, not 100%. Source:
  `tasks/bracc/bracc_01_das_fator_r/workspace/library/anexos_iii_v_tabelas.md`.
  Sol asked about the discrepancy. The script has no corrected-table answer.
- **BRACC-01 payroll window:** the March row has zero pro-labore but an
  observation about April; the April row already includes R$3,200. The
  reference adds another R$3,200 after confirming April payment. Reconcile this
  mismatch before treating the reference's Fator R/Anexo III result as a gate.
  The reference also retains a stale note saying the payment occurred in May,
  whereas the scripted answer and withheld PIX evidence say April 30.
- **BRACC-01 attachment routing:** a PIX receipt lives under
  `reviewer/reference/comprovante_pix_prolabore_abril__released_on_request.txt`,
  but the client JSON has no machine-readable attachment-release action. This
  pilot transmits scripted text only. The candidate receives the date and
  amount in that text, but not the promised receipt. Add explicit attachment
  metadata before a scored campaign; never mount the whole reference folder.
- **USACC-09 lease valuation:** the generator assumes an 8% discount rate to
  compute the reference present value. The candidate-visible hosting excerpt
  states $18,000/month for 36 months but does not provide that rate or a
  lease/service allocation. The client script supplies neither. Sol identified
  the lease and left its measurement unknown rather than inventing the inputs.
  Review the numeric oracle before scoring this as a candidate failure.
- **USACC-03 client text:** the Leo/8332 answer contains literal `{TY}` rather
  than the tax year. The runner sends it verbatim as required. Repair the
  fixture template in a future pack version.
- **USLAW-04 fixed opponent response:** session 2 quotes a prior demand for
  seven hires, tort damages and court litigation, while this candidate's actual
  session-1 draft had already conceded the two waivers, dropped the tort claim
  and chosen arbitration. The candidate explicitly flags that discrepancy.
  Check that the grading key accepts a sound initial assessment and does not
  require an admission that the candidate previously made a claim it never made.
  A case date in the engagement contract would also avoid the candidate dating
  its draft after the canned opposing letter.

These are internal consistency findings about the synthetic packs, not claims
about current tax or legal requirements. Full citation, trust-gate, numerical,
and written-work grading remains pending.
