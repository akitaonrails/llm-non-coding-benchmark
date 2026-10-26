# STATUS

**Matter:** *Sound Cascade Foods, Inc. v. Harbor Street Bakery LLC* (King County Sup. Ct. No. 26-2-18874-1 SEA)
**Date of status:** Mon Sep 28, 2026 (updated after the client's same-day reply; evening addendum on the client's diversity objection — see log)
**Companions:** `deadlines.json`, `memo.md`, `QUESTIONS.md` (asked & answered — record only)

## STATUS: COMPLETE

All contracted deliverables are written, cross-consistent, and JSON/schema-validated. The one open item from the morning edition (member roster) is **resolved** by the client's Sept 28 reply, and it resolved **against removal**:

| Deliverable | State |
|---|---|
| `deliverable/deadlines.json` | ✅ Exact CONTRACT schema — all fields final; 7 ISO dates; independent arithmetic re-verified. |
| `deliverable/memo.md` | ✅ Full reasoning — facts F1–F11, date computations (§3), removal analysis now **final** (§4), week plan updated (§5), assumptions A1/A3 marked CONFIRMED (§6), reconciliation (§7), citation register (§8), **§9 addendum answering the client's "Delaware LLC vs Washington corporation" objection** (no change to any determination). |
| `deliverable/QUESTIONS.md` | ✅ Q1–Q4 asked Sept 28; answered same day; stamped and retained as the record. No questions outstanding. |

## Final determinations
1. **`removal_available = false` — FINAL, not provisional.** Roster (client, Sept 28): exactly two members — **Caleb Sorensen 35%, lives in Seattle, WA**, and **Noor Haddad 65%, lives in Portland** — no entity members. With the LLC's citizenship fixed by its members (*Johnson v. Columbia Properties Anchorage, LP*, 437 F.3d 894, 899 (9th Cir. 2006); *Carden v. Arkoma Associates*, 494 U.S. 185 (1990)), Sorensen's Washington citizenship on the defendant side (i) destroys complete diversity against the Washington-only plaintiff (§1332(a), (c)(1)) and (ii) independently trips the forum-defendant bar (§1441(b)(2)). No date or fact rescues it.
2. **State answer: Thursday, October 1, 2026** (CR 4(a)(2)/12(a)(1): 20 days from Sept 11 service + CR 6(a)/RCW 1.16.050; Thu, no roll) — unchanged and the only deadline still live this week.
3. **Removal deadline 2026-10-13 stands as correctly computed but is MOOT** (§1446(b)(1) 30 days → Oct 11 Sun → Oct 12 Columbus Day federal holiday → Oct 13). Retained in the JSON to show the window's outer bound.
4. **`if_removed` block retained as HYPOTHETICAL** (schema requires the fields): answer Oct 20 (FRCP 81(c)(2) longest-of), 26(f) conference Nov 19, scheduling order Dec 10 — none will ever come due on this record.
5. **Nothing filed/served by the client in King County** (confirmed, F11): no pre-removal or default complications; the recommended WA notice of appearance (Tue 9/29, served on plaintiff's counsel Amara Voss, WSBA #41122, who signed the summons and complaint) protects against default machinery per CR 55(a)(3).

## Updates log
- **Sept 28 (morning):** client confirmed roster → `removal_available = false` made FINAL; all deliverables finalized; `STATUS: COMPLETE`.
- **Sept 28 (evening):** client relayed a friend's objection ("Delaware LLC vs Washington corporation is textbook diversity; Caleb shouldn't matter — the company isn't him"). Answered in `memo.md` §9: the friend's rule is the §1332(c)(1) **corporate** test, which the library says **does not apply** to an LLC (*Johnson*/*Carden*); membership decides, so Sorensen's Washington residence is decisive; the only theoretical escape (his non-WA domicile) is already answered in the record (Q1.2: lives in Seattle; no other home) and could not be certified responsibly. **No change to any date or determination.** New [UNVERIFIED] flag noted below (responsive-pleading doctrine).

## Remaining unknowns — flagged explicitly (per client instruction); none changes a date or the removal conclusion
- **Sorensen's domicile in the technical sense** (residence + indefinite intent): unprovable on this record; the client gave "lives in Seattle (Ballard)" and no other home. Even in the theory where a non-WA domicile *and* no other WA member would have made removal viable, we have **no affirmative fact** for any other domicile — filing on that hope risks remand plus "just costs and any actual expenses, including attorney fees" (§1447(c)). Conclusion unaffected: removal is off.
- **[UNVERIFIED]** (outside the closed library; not relied on): out-of-state service-validation mechanics (A4); agent-receipt-as-defendant-receipt (A5) — moot, removal off; §1446(b)(3) operative text (the one-year cap IS in-library via §1446(c)(1) → 2027-09-08); W.D. Wash. local rules (A9) and Seattle-division ID (A10) — moot; whether a pre-removal state-court appearance is the Rule 16(b)(2) "appeared" trigger — moot; **whether filing the Oct 1 state-court answer forecloses any later removal ("responsive pleading" doctrine; raised in memo §9.5)** — moot, removal off; **whether an entity may appear/litigate in Washington superior court without a licensed attorney** — new, open, but outside the library; **RCW 4.84.330** (complaint's fee statute, A8): allegation only.

## Actions flowing to the client (memo §5)
1. **Tue 9/29:** serve notice of appearance on Voss + file with the King County clerk (default protection). **Engage Washington counsel immediately** — answer is due Thu 10/1.
2. **Wed 9/30:** draft the answer; verify plaintiff's math against the books ($142,316.40 − $31,400.00 = $110,916.40; $18,240 butter count).
3. **Thu 10/1:** serve (+ file) the answer. **No removal filing — ever.**
4. Preserve the three short/spoiled-delivery files and photos (F9) for the answer/counter-claims narrative.
