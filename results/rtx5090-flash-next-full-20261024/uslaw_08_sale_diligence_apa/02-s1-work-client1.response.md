New facts from Ray change two things: the Hensley consent is now a relationship-management problem (friend not yet told), and the installers' 45–50 hour busy season puts real money into the FLSA overtime tail. Let me size the overtime first.

Now updating all deliverables with the new facts.

The §9.3 clause has a cross-reference error (7.5 instead of 7.4(b)) and needs the $200k fallback note. Fixing both:

Now the reply to buyer's counsel. Reading current version first:

One important issue: the redline now contains internal negotiation instructions. Let me check its header for an internal-use flag:

The redline is an internal working document — I'll make that explicit so the negotiation fallback never travels to the buyer:

Now updating the reply to buyer's counsel — Hensley sequencing, the customer-contact covenant, and indemnity sizing with the overtime math:

Now the note to Ray. Reading the current version:

Now rewriting QUESTIONS.md as an answered-log plus explicit open assumptions (no re-asking). First, the current file:

Now STATUS.md:

Final validation pass — JSON parse check and cross-reference consistency:

JSON is valid with correct schema and enum values. Two stale QUESTIONS.md references in the redline — fixing:

Correcting my cross-reference number — allocation is assumption 3 in QUESTIONS.md, not 5:

All deliverables are now updated for the client's round-2 answers. Round summary:

**What the new facts changed**

1. **Overtime is now money, not a maybe.** 45–50 hrs/week straight-hourly means the FLSA gap is the half-time premium: 0.5 × $37.50 avg rate = $18.75/OT-hour → $10,125–$33,750/yr across the nine installers → **$40,500–$135,000 over 4 open years** (busy season assumed 12–20 weeks, flagged). Combined with the ≈$74k tax math, the realistic classification band is **≈$115k–$210k**. The special indemnity strategy holds — **offer $150,000, $200,000 ceiling** — and the redline §9.3 escrow tranche now tracks whichever cap lands, with the cross-reference fixed (7.5 → 7.4(b)). "They like it" is treated as irrelevant, with the non-waivability point labeled UNVERIFIED since it's outside the library.

2. **Hensley is now a sequencing problem, and Ray owns the sequencing.** The owner is a friend who hasn't been told and "won't love a corporate buyer." Every deliverable now runs through that: Ray tells him personally **this week, before any buyer-side contact**; signed consent targeted pre-signing; new proposed **APA §3.4 no-customer-contact covenant** so the buyer's diligence team can't torch the friendship path; and the "what if he says no" branch (defined price cut vs. termination, outside date) negotiated now, not after the veto has leverage.

**File state** (`workspace/deliverable/`)
- `diligence_findings.json` — 13 findings, re-validated: parses clean, exact schema keys, enum-valued `deal_impact`
- `apa_redline.md` — §3.4 covenant added, §4.12 hours facts scheduled, §7.4(b) sized with OT arithmetic, §9.3 aligned; header now marks it an **internal working document** so the $150k-hold/$200k-fallback instruction never travels to Whitaker
- `reply_to_buyer_counsel.md` — sized $150k indemnity with visible arithmetic, successor-liability argument (buyer can't be covered twice for the same wage claims), contact-covenant demand
- `note_to_ray.md` — OT math in plain English; Hensley section rewritten as a 4-step "tell your friend first" plan
- `QUESTIONS.md` — closed round: answered log + 8 explicit assumptions, nothing re-asked per client instruction
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**, with the open items (price, busy-season weeks, lease guaranty, allocation, full APA, Hensley consent outcome) stated as flagged assumptions, and all non-library legal parameters (SOL, doubling, §3509 rates, waiver) listed as UNVERIFIED