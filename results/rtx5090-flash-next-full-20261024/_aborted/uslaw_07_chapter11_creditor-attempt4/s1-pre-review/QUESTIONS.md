# Remaining unknowns — flagged, not re-asked

The client answered what it could on 2026-03-19 (terms change and oldest-first shipping
condition; the Feb 27 wire demand; the "pay first" answer to debtor's counsel) and states it
has **no additional information** on the rest. This file therefore does not repeat answered
questions. It lists every material fact still unknown, the assumption we are proceeding under,
and where each item actually gets resolved (docket, claims agent, debtor's counsel, or Mesa's
own records).

**Resolved since the last round (no client input needed):**

- **$210,000 vs $125,000** — pure arithmetic: the Mar 12 letter quoted the **gross** of the six
  ledger invoices (48,200 + 62,400 + 41,300 + 6,900 + 36,800 + 14,400 = 210,000) with no credit
  for the **$85,000 already paid** in February (MS-7701 $48,200 in full on Feb 10; MS-7740
  $36,800 partial on Feb 27). 210,000 − 85,000 = **125,000**. Claim confirmed at $125,000; see
  `proof_of_claim_draft.md` §5.
- **Terms-change and wire-demand facts** — now client-admitted; folded into the preference
  analysis (`claim_analysis.json` preference; `advice_to_ceo.md` §2).

---

**U1 — §503(b)(9) procedure under the bar-date order.** The bar-date order itself is not in the
file, and the notice does not say whether a separate §503(b)(9) motion or pleading is required.
*Assumption:* asserting §503(b)(9) priority on the Form 410 filed by the bar date preserves the
priority (the library covers claim filing, not 503(b)(9) motion practice). *Resolution:* pull
the docket via the claims agent at filing; ask debtor's counsel before the Apr 2 hearing.

**U2 — DIP blanket lien scope.** The library note on reclamation assumes blanket liens defeat
reclamation; the actual DIP/cash-collateral order is not in the file. *Assumption:* reclamation
is preserved but economically hollow. *Resolution:* docket pull.

**U3 — Scheduling and service.** The §341/bar-date notice in the file suggests Mesa was a
noticed creditor, but the schedules are not in the file (amount scheduled, any objection).
*Assumption:* Mesa is scheduled; no amendment needed if we file by the bar date. *Resolution:*
claims agent / schedules on the docket.

**U4 — Notice date anomaly.** The notice recites "Notice dated: April 2, 2026," a date *after*
today (2026-03-19). Client cannot resolve it. *Assumption:* the recited bar date **June 11,
2026, 5:00 p.m. MT** is operative; we calendar it and file well before. *Resolution:* confirm
the operative order on the docket; if an earlier bar date surfaces, the early filing already
protects us.

**U5 — Reclamation facts (traceability, insolvency at receipt).** Whether the MS-7740/7788/7815
steel remains identifiable and unprocessed at Redwood's yard, and Redwood's insolvency at
receipt, are unknown. *Assumption/plan:* serve the written §546(c)(1) demand by **March 30,
2026** regardless — it is cheap and preserves leverage (see `advice_to_ceo.md` §3).
*Resolution:* debtor's inventory records / site inquiry post-service.

**U6 — Date of Frank's "pay first" call to Redwood's counsel.** The only undated incident; it
sits on the stay-violation timeline (first documented Mesa knowledge of the case: the Mar 15
call) and it frames the critical-vendor problem. *Assumption:* it occurred post-petition (the
supply-on-normal-terms offer concerns the Chapter 11 supply relationship) — date unknown,
flagged. *Resolution:* Mesa's own phone records/calendars — pull **now**, this is a records
task, not a court question.

**U7 — Whether the "hold all future shipments" threat was carried out.** Affects stay-violation
damages exposure and the critical-vendor narrative. *Assumption:* no post-petition shipment
hold has been executed; all shipping continues only on ordinary case terms. *Resolution:*
Mesa's shipping records for Mar 18 → present.

**U8 — Master supply agreement / late-payment interest terms.** The only terms document in the
file is the unilateral 2026-01-20 e-mail; no signed master agreement or interest clause is in
the file. *Assumption:* no enforceable contractual late interest; the claim asserts **no**
interest (Form 410 Item 5) and can be amended before the bar date if terms surface.
*Resolution:* Mesa's contract files (records task).

**U9 — Guaranties, UCC filings, judgments, other outside-the-estate avenues.** Nothing in the
file; client has no additional information. *Assumption:* none exist; we pursue nothing outside
the estate. *Resolution:* Mesa's contract/collection files (records task). Any such avenue
would need separate analysis — the library does not cover guaranty or co-debtor treatment, so
no position is taken here.

**U10 — Completeness of the payment ledger for the preference window.**
*Assumption:* `payment_history_12m.csv` is complete for Dec 10, 2025 – Mar 10, 2026 —
`transfers_in_90_days: 180,000` rests on it. *Resolution:* reconcile against Mesa's bank
statements before any preference negotiation (records task).
