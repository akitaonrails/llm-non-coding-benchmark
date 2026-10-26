# Engagement: review the RouteWise MSA for Cobalt Logistics against the playbook

The GC wants what matters, ranked, with redlines for hard-rule breaks and a one-pager for the COO.

## Deliverables (under `workspace/deliverable/`)
1. `issues.json` — `[{"rank": 1, "clause": "§9.1/§10.1", "playbook_rule": "A1", "severity": "hard|preferred|note", "issue": "...", "why": "...", "redline": "replacement text or 'none'"}]` — include **only** real issues; flagging a clause the playbook accepts counts against you.
2. `redlines.md` — replacement clause text for each hard-rule violation.
3. `coo_onepager.md` — plain English: what the deal does, the 3–5 things that must change before signature, and business impact.
4. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
