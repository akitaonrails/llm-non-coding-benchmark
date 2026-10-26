# Engagement: Brightline Cabinetry asset sale — sell-side diligence and APA redline

Ray wants to sign in two weeks and says "just tell me what bites me later". Review the data room and
the buyer's draft, and answer buyer's counsel's two questions (Schedule 3.3; WARN).

## Deliverables (under `workspace/deliverable/`)
1. `diligence_findings.json` — `[{"issue": "...", "where": "data room §", "why_it_matters": "...", "deal_impact": "consent|price|indemnity|timing|none", "fix": "..."}]`
2. `apa_redline.md` — for §§2.4, 3.3, 4.12, 7.4(a)-(c), 8.2, 9.3: keep / change, replacement language, and why.
3. `reply_to_buyer_counsel.md` — answers on Schedule 3.3 and WARN, and your position on 7.4(c).
4. `note_to_ray.md` — plain English: the three things that could cost him money after closing.
5. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
