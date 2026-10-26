# STATUS — Brightline Cabinetry asset sale (sell-side)

**Status: COMPLETE WITH OPEN ITEMS**

Date: 2026-10-25

## Deliverables delivered (all under `workspace/deliverable/`)

| File | Status | Notes |
|---|---|---|
| `diligence_findings.json` | Done | 12 findings; JSON validated (parses cleanly); every `deal_impact` drawn from the allowed enum (consent / price / indemnity / timing / none) |
| `apa_redline.md` | Done | All scoped sections: §§2.4, 3.3 (+ Schedule 3.3), 4.12 (+ §7.1A/schedule), 7.4(a) KEEP, 7.4(b) CHANGE, 7.4(c) CHANGE, 8.2, 9.3 KEEP; arithmetic block with all assumptions flagged |
| `reply_to_buyer_counsel.md` | Done | Answers Schedule 3.3 (disagree with "None"; counterschedule delivered), WARN (not a covered employer: 14 W-2, 23 even counting installers — under 100), §7.4(c) position (reject pro-sandbagging; anti-sandbagging counter), permit/closing-timeline note. **Rev-2 Addendum:** rebuts "§7.4(c) is market / every deal has it" (`library/sandbagging.md`: pro- and anti-sandbagging are both live market alternatives; buyer's "at any time, before or after" wording exceeds even the aggressive form described) and "§4.12 is plain vanilla" (data-room census fails the control test, `library/worker_classification_tx_irs.md`; full-price cap on an operational rep is off-market, `library/baskets_caps.md`); offers **Option A** (anti-sandbagging redline) or **Option B** (buyer keeps §7.4(c) verbatim for unscheduled matters; Schedule 4.12 + §7.1A $275,000 cap as exclusive scheduled remedy; §4.12 removed from §7.4(b) full-price carve-out); states the only un-signable combination: knowingly false rep + no schedule + full-price cap + post-signing knowledge |
| `note_to_ray.md` | Done | Plain-English three cost items (installers, earn-out, Hensley), with arithmetic shown. **Rev-2 Addendum:** answers Ray's "can we just sign?" — four-item sign-when checklist (Hensley call first; schedules in; $275k cap replacing the up-to-$3.1M checkback — $3.1M − $310k = up to $2,790,000 beyond escrow; earn-out decided consciously at ~$0 or held for the §2.4 redline), plain-English rebuttals of counsel's two claims, permit-set closing calendar |
| `QUESTIONS.md` | Done | 5 questions asked; client's scripted reply received and baked into all deliverables |

## Citation integrity

- Every authority cited points to a file in `library/INDEX.md`: `anti_assignment_change_of_control.md`, `worker_classification_tx_irs.md`, `sandbagging.md`, `baskets_caps.md`, `earnout_definitions.md`, `warn_act.md`, `tx_noncompete_sale_of_business.md`.
- Nothing outside the library was relied on as law. Items used but **not** in the library are labeled unverified in the deliverables where they appear (7.65% FICA figure; half-time OT-premium method; FLSA limitations period; §3509 reduced-rate percentages; Texas unemployment rate).

## Open items (explicitly flagged, none invented over)

1. **Purchase price is inferred, not stated.** No price appears anywhere in the client file; $3,100,000 is inferred from escrow of $310,000 stated as 10% (APA §9.3): 310,000 ÷ 0.10 = 3,100,000. Confirm against full APA §2.1 (never provided). All %-of-price figures depend on this.
2. **Schedule 3.1(c) (Assigned Contracts) never located** — not in the data room and missing from buyer's materials; requested from buyer's counsel. Which contracts buyer intends to "take" is unverified; cannot confirm whether the Hensley MSA sits on it.
3. **Prior-year installer 1099 totals (2023–2024) unverified.** Client provided 2025 only ($612,000) and no additional information beyond that; 2025 is used as the annual run-rate proxy for the exposure window (avg tenure 3.4 years from the census).
4. **Busy-season length unknown.** Ray answered "45–50 hours a week in busy season" without a week count; the lower exposure scenario assumes 12 weeks (flagged as assumption). Bracket $228,031–$302,619 spans both readings.
5. **Figures outside the library, labeled unverified:** the 7.65% employer FICA share (upper-bound assumption); the half-time overtime-premium method (standard payroll arithmetic, not library authority); FLSA limitations period (exposure quantified on 3.4-year census tenure instead of a limitations period); §3509 reduced-rate percentages and Texas unemployment contribution rates (regimes named in the library, numbers not — left as buffer inside the $275,000 cap rather than quantified).
6. **Hensley consent outcome unknown.** Not yet sought (client confirmed); owner unaware of the sale and "won't love a corporate buyer." Strategy assumes consent is unobtained and works around it: personal approach before signing + condition precedent + drop-dead date.
7. **Non-compete trade area is a placeholder.** Proposed 75-mile radius pending Ray's confirmation of his actual customer footprint (no geography in the data room).
8. **No purchase price allocation in the data room**, so any IRS-scrutiny concern about price-shifting to the overbroad non-compete is currently unsupported either way; also affects how much of the classification exposure is tax vs. wage recovery.
9. **Whether price was negotiated assuming the earn-out is unknown** (client's answer to Q3 was "no additional information"). Recommendation stands: value the earn-out at ~$0 as drafted (gate math in redline/diligence), price cash only until rewritten.
10. **Buyer-side negotiation is outside this engagement.** The redline and counsel letter are the sell-side ask; outcome of the Schedule 3.3/§4.12/§7.4(c) give-and-take is pending and not part of this status.
11. **Buyer has not chosen Option A or Option B.** The rev-2 addendum to `reply_to_buyer_counsel.md` offers two acceptable packages; as of this revision buyer's counsel has agreed to neither. Until one is accepted, the §7.4(c)/§4.12/§7.1A structure exists only as redline, not as agreed terms.
12. **Ray's conscious earn-out decision pending.** The note addendum frames the choice: sign with the earn-out valued at ~$0 as a deliberate economic choice (price treated as $3,100,000 cash only) or hold for the §2.4 rewrite. Recommendation stands (value ~$0, cash price only); client's answer not yet in.

## Not forced / left open on the arithmetic

- Scenario A escrow excess ($310,000 − $302,619 = $7,381) versus Scenario B headroom ($310,000 − $228,031 = $81,969): deliberately not reconciled — the bracket is the answer until the missing week-count and prior-year totals arrive.
- Earn-out value is shown as $0 across realistic buyer-measured scenarios, $16,000 in the single best case (calculation basis unchanged); expected value is treated as ~$0, not blended.

## Revision log

- **2026-10-25 (rev 2).** Buyer's counsel pushback relayed via client ("§7.4(c) is market, every deal has it"; "§4.12 is a plain-vanilla compliance rep — if the contractors are fine, what's the concern?") and Ray asked "can we just sign?". Actions: (a) Addendum appended to `reply_to_buyer_counsel.md` — market-practice rebuttal, control-test rebuttal with census facts, Option A/Option B package, and the un-signable combination; (b) Addendum appended to `note_to_ray.md` — four-item sign-when checklist, today-vs-after cost contrast (uncapped exposure up to $3,100,000, i.e., $3.1M − $310,000 = $2,790,000 beyond escrow, versus $275,000 cap on the ~$228,031–$302,619 bracket), earn-out conscious-decision framing; (c) `QUESTIONS.md` not reopened — neither client message supplied new facts (Hensley contact status unchanged per item 6). No changes to `diligence_findings.json` or `apa_redline.md`. Status unchanged: **COMPLETE WITH OPEN ITEMS** (now items 11–12 above).
