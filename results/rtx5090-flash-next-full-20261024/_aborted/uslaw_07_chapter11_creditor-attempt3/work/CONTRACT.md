# Engagement: Mesa Steel Supply — creditor of Redwood Fabrication (Chapter 11)

Today is March 19, 2026. Redwood filed nine days ago. Mesa's AR team has kept
collecting. The CEO wants "to file something and get paid first". Advise and prepare the filings.

## Deliverables (under `workspace/deliverable/`)
1. `claim_analysis.json` — `{"total_prepetition_claim": 0, "admin_503b9": {"amount": 0, "invoices": []}, "general_unsecured": 0, "reclamation": {"available": true/false, "why": ""}, "bar_date": "YYYY-MM-DD", "preference": {"transfers_in_90_days": 0, "ordinary_course_defense": {"protected": 0, "exposed": 0, "reasoning": ""}, "new_value_defense": 0, "net_exposure_estimate": 0}, "stay_violations": ["..."], "immediate_actions": ["..."]}`
2. `proof_of_claim_draft.md` — Official Form 410 content: creditor, basis, amount with the 503(b)(9) portion separately stated, supporting documents list.
3. `advice_to_ceo.md` — plain English: what to stop doing today and why; what Mesa may owe Redwood; the critical-vendor path.
4. `QUESTIONS.md` (optional), `STATUS.md`.

## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
