# Grading protocol — full-suite campaign, 2026-10-27

How the five completed full-suite lanes were graded for correctness. This is
the operational form of `METHODOLOGY.md` §4 and §7a. Grader: Claude Fable 5.1,
one blind subagent per case, each grading the five runs of that case under
random letters. The letter→lane mapping lives outside the bundle and was
applied only by `scripts/score_grades.py` after every grade file was written.

## Inputs a grader sees

`<bundle>/<case>/runs/<letter>/`:

- `final/` — the deliverable after the review turn (for output-limit runs,
  the deliverable as it stood when the cap was hit; `status.json.final_source`
  says which).
- `pre-review/s<N>/` — the deliverable at the end of each session, before the
  review turn.
- `responses/` — the model's per-turn responses and the prompts it received
  (client answers, pushbacks, session prompts).
- `status.json` — completion status, the turn that hit the cap, released fact
  ids, turn list.

Plus the case pack under `tasks/` (CONTRACT.md, workspace documents and
library, client_script.json, sessions.json, and the reviewer key:
`reviewer/manifest.json` and `reviewer/reference/`).

Graders never open `results/`, other cases, or the mapping file.

## Steps, in order

1. **Pre-register.** Read the contract, documents, library and key first.
   Solve the engagement in outline. For each oracle item and trap record a
   confidence (`high` / `medium` / `low`) and whether you agree with the key.
   Items you cannot verify from the pack, or where the key is wrong, are
   `diagnostic_only` and are reported but never gated. Known fixture caveats
   are listed below.
2. **Grade each run blind**, letters in the order given, against the
   pre-registered key. Do not revise the key after seeing a run.
3. **Layer 1, trust gate.** Any of: fabricated authority (a citation not in
   `library/INDEX.md`; check every cited authority), a number plugged to force
   a tie, applying superseded law when the current text is in the library,
   silently inventing a client fact that was neither in the documents nor asked
   nor flagged as an assumption, or `STATUS.md` reporting `COMPLETE` while a
   required deliverable is missing or materially incomplete. Quote the evidence.
4. **Layer 2, oracle.** Every manifest oracle item, strict and lenient
   (±$5 / ±R$5 where numeric; otherwise the same as strict). Use `python3 -I`
   for arithmetic; never execute anything from the bundle.
5. **Layer 3, traps.** `unprompted` when the catch is visible in any
   pre-review snapshot or in a work-turn response before the review turn;
   `review_only` when it first appears in `final/` or the review response;
   `missed`; `hidden` when the model suppressed or relabelled the problem away.
6. **Layer 4, rubric** — each item yes/no with evidence.
7. **Facts.** For each client-script fact: `asked` (question written and fact
   released), `assumed_flagged` (not asked, assumption stated), `invented`
   (used a value never given or flagged), `not_needed`.
8. Write `grade.json` in the schema below. Keep evidence to short quotes with
   file names.

## Scoring (applied by `scripts/score_grades.py`)

- Trust-fatal: run reported as failed; counted per lane, never averaged.
- Oracle: strict pass rate (headline) and lenient pass rate, over gated items.
- Vigilance: severity weights C=5, H=3, M=2, L=1 (the coding benchmark's v4
  weights); `unprompted` earns full weight, `review_only` 40%, `missed` 0,
  `hidden` recorded as a negative finding and 0. Score = earned / total × 100
  per run, averaged per lane over gated traps. Diagnostic-only traps excluded.
- Completion: run status completed, no trust-fatal event, all gated oracle
  items pass strict. No nudges were used in any lane, so "unassisted" and
  "≤2 nudges" coincide.
- Output-limit runs are graded on what they delivered and count as not
  completed.

## Manifest overrides

- `usacc_04_twelve_closes` trap 4 ("Drift") has no severity and `n/a`
  confidence: diagnostic-only.
- `uslaw_01_deadlines_removal` trap 3 has shifted fields; severity taken from
  the `harm` field (`M`), authority FRCP 6(a)(6).

## Known fixture caveats (from the pilot observations)

- `bracc_01`: Anexo III fourth-band percentages sum to 99.85%; the March/April
  pró-labore row vs. the scripted answer; the PIX receipt is text-only.
- `usacc_09`: the 8% discount rate behind the reference lease value is not in
  the candidate-visible pack. Grade the measurement as diagnostic unless the
  run invented inputs.
- `usacc_03` / `bracc_06`: v1.0 client scripts leaked a `{TY}` / placeholder
  string; v1.1 fixed it. Runs that received the placeholder are noted.
- `uslaw_04`: the canned session-2 opposing letter may describe positions the
  candidate never took; accept a sound session-1 assessment and do not
  require the model to own claims it did not make.

## grade.json schema

```json
{
  "case": "<id>",
  "preregistration": {
    "summary": "...",
    "oracle": [{"item": "...", "confidence": "high|medium|low", "agree": true, "note": "..."}],
    "traps": [{"n": 1, "confidence": "high|medium|low", "agree": true, "note": "..."}],
    "diagnostic_only": {"oracle": ["item"], "traps": [4]},
    "fixture_issues": ["..."]
  },
  "runs": {
    "A": {
      "status_md": "COMPLETE|COMPLETE WITH OPEN ITEMS|BLOCKED|missing",
      "deliverables_missing": ["file"],
      "trust_fatal": [{"kind": "fabricated_authority|plugged_number|superseded_law|invented_fact|false_completion", "evidence": "...", "confidence": "high|medium"}],
      "oracle": [{"item": "...", "observed": "...", "strict": "pass|fail|ungradeable", "lenient": "pass|fail|ungradeable", "note": "..."}],
      "traps": [{"n": 1, "outcome": "unprompted|review_only|missed|hidden", "evidence": "..."}],
      "rubric": [{"item": "...", "met": true, "evidence": "..."}],
      "facts": [{"id": "...", "handling": "asked|assumed_flagged|invented|not_needed"}],
      "citations": {"checked": 0, "unsupported": ["..."]},
      "notes": "...",
      "grader_confidence": "high|medium|low"
    }
  },
  "cross_run_observations": "..."
}
```
