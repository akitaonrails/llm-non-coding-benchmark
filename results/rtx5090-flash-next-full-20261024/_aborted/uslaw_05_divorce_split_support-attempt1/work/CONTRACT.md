# Engagement: Marital dissolution — advise Wife on the proposed division and support

Husband's counsel proposes an "equal halves" division (see `asset_schedule.md`) and support based on
his salary. Advise the client, with numbers.

## Deliverables (under `workspace/deliverable/`)
1. `division.json` — `{"proposal_nominal": {"wife": 0, "husband": 0}, "proposal_after_tax": {"wife": 0, "husband": 0, "assumptions": "..."}, "undisclosed_income": {"found": true/false, "amount": 0, "source": "..."}, "alternatives": [{"name": "...", "wife_after_tax": 0, "husband_after_tax": 0, "instruments": ["QDRO", "..."]}], "maintenance_tax_treatment": "...", "dependents_and_filing_status": "..."}`
2. `child_support.json` — `{"husband_gross_used": 0, "wife_gross_used": 0, "combined_monthly_net": 0, "basic_obligation": 0, "husband_share_monthly": 0, "notes": "..."}`
3. `advice.md` — plain-English advice: is the proposal fair after tax; the house decision (affordability, refinance, §121); what instruments are needed; what to do about the undisclosed bonus.
4. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
