Client answers received. Let me recompute the residency math under the confirmed "about a third of the year" (~120 days) pattern, including the margin to residency tipping in later years and the CA-fee-tier sensitivity now that Tomás mostly works from Monterrey:

Answers incorporated — the NRA conclusion is now robust (161–163 weighted at 118–122 days), with 2027 residency needing 127 days (thin ~7-day margin). Updating all deliverables:

recommendation.md is done. Now the JSON assumptions strings:

Now the term sheet:

Now rewriting QUESTIONS.md and STATUS.md — reading current versions first:

All deliverables updated. Final validation pass — JSON integrity, arithmetic reconciliation, and citation-to-INDEX mapping:

The sum-check didn't find the expected key names — inspecting the JSON structure and re-running reconciliation:

All client answers are now incorporated across the six deliverables, and everything re-validates clean. Summary of this pass:

## What changed

**`recommendation.md`**
- §2.1 / §3.3 — residency conclusion upgraded from assumption-based to **client-confirmed-robust**: at 118–122 days the weighted SPT is 161.0–165.0 < 183. New forward-looking watch: **2027 residency tips at 127 days** (~7 days of margin over his ≈120-day pattern); the **2028 threshold falls to ≈123 days**.
- §3.1 — QBI paragraph now flags that Tomás performs services mostly from Monterrey; his US-source/ECI share and NRA QBI are library gaps for a specialist.
- §3.5 — updated: TN with **no green card application pending** (confirmed); married in Mexico with **no prenup** → spousal joinder mandatory; and a new bullet on **other-state nexus** from clients all over the US (library covers CA only).
- §4 — added CA fee-band sensitivity: if CA-allocable receipts drop to the $250k–$499,999 band, fee $900 → total **$103,211.90** (vs $104,183.10); allocation rule not in library, labeled unverified.
- §5 register — rows 2, 8, 9, 11 refreshed with confirmed facts; new row 13 for state nexus.

**`year1_comparison.json`** — assumption strings updated (confirmed day pattern → 163.0 variant, fee-band sensitivity with full arithmetic, sourcing and nexus flags). Base numbers unchanged and still flagged as labeled-rate assumptions.

**`compliance_calendar.md`** — Dec 2027 SPT row rewritten with the 127/123-day thresholds and "thin margin" warning; Section D adds annual CA fee-band re-check, NRA withholding setup before first K-1, and annual nexus check.

**`term_sheet.md`** — §3 and §5 now cite the confirmed marriage-in-Mexico/no-prenup fact; spousal joinder is a **mandatory closing condition**. §8 rewritten as specialist-routed open points (client contracts unknown, cross-border drafting, state exposure).

**`QUESTIONS.md`** — rewritten as a **"remaining unknowns — do not re-ask"** register: a table of answers already incorporated, plus 11 unresolved items each routed to the right resolver (immigration counsel, cross-border specialist, Mexican counsel, SALT, FTB, closing docket) instead of back to the client.

**`STATUS.md`** — **COMPLETE WITH OPEN ITEMS**, with the open list refreshed (formation-date assumption, TN clearance, NRA sourcing/QBI, 127-day residency watch, unsigned spousal joinder, contract review, labeled rates/DE costs/nexus).

## Validation results
- JSON parses; all four options reconcile component-sum = total ($97,680 / $104,183.10 / $102,180 / $104,183.10).
- Prose sensitivity figures re-derived independently: K-1 $129,150, SE $19,759.95, tax $30,996, total $103,211.90 ✓.
- Citation sweep: every `.md` reference in all deliverables maps to one of the 10 files in `library/INDEX.md` — zero out-of-library citations; everything else stays labeled "unverified/assumed."

The engagement is complete with open items. The two most consequential remaining flags: **immigration clearance of TN ownership/service before formation**, and the **127-day 2027 residency threshold** — the only fact that could reopen the S-corp question.