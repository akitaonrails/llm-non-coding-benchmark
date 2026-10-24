# tasks/ — the 38 case packs

One directory per engagement. Model-visible: `CONTRACT.md` and `workspace/`. Runner-only:
`client_script.json`, `sessions.json`. Reviewer-only (shielded): `reviewer/`.

- Rebuild: `python scripts/build_cases.py [--only usacc_01 ...]` (deterministic).
- Validate + inventory: `python scripts/check_pack.py --table`.
- Every `reviewer/manifest.json` has: `traps[]` (wrong move / why wrong / authority / evidence / harm /
  severity / reviewer confidence), `oracle[]` (deterministic checks with tolerance), `rubric[]`,
  `library_verification[]` (which library excerpts are verbatim, which are paraphrased and must be
  verified against the official text before freezing, and which are planted distractors).
- Fictional jurisdictions: "State of Columbia" (USLAW-4, -5, -9) is invented so that state-law rules
  can be fixed by the library; all federal and Brazilian law is real.
