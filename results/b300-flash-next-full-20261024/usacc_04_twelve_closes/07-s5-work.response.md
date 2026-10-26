

New item this month: an order form for C-028. Reading all May sources:





Parser found 33 "rows" vs 31 actual transactions — probably picking up stray date-like lines. Debugging the parse:





33 transactions (not 31), and there's an anomalous block at lines 114–121 — extra lines around the 05/24 Birch Labs row. Inspecting:





The extra lines are just a repeated column caption (`1 / Credit / Balance` — page-break artifact), not a transaction. And the true transaction count is **33** (7 withdrawals + 26 deposits), not 31 — my earlier visual count was wrong. Fixing the assertion and rerunning:





Cleaning out leftover dead placeholder code:





The script has leftover messy sections (and a `prev`-not-updated bug in side detection). Rewriting it cleanly:





My date-conversion helper assumed the wrong format — receipts are ISO `YYYY-MM-DD`. Fixing:





April's script is gone from tmp; I'll rebuild from the April deliverables directly:





Schema confirmed. Writing and running the May posting script:





Checking prior months' differences so the "first zero-difference month" phrasing is accurate:





Writing the recon file via shell python instead:





Recon written. Now reading April's open_items.md to carry forward items 1–11, close item 12, and add item 13:





The recon is done. Before writing open_items.md, I need to fix a cross-reference inconsistency: the May JSONs I posted reference the Trestle overlap as "open item 4," but per the running numbering (month_01→04), the overlap is **item 3** (item 4 is Pinecone). Fixing so the May note matches:





Cross-references now consistent. Writing May's open_items.md:





Now updating STATUS.md:





All five deliverables written. Running a final cross-validation of the whole month_05 package:





Checking which tie failed:





The rollforward ties fine; the failing line is the release cross-check between rollforward and JEs. Debugging it directly:





The strict "no item 4 refs" check fired on open_items.md — but legitimate month-specific references like "month_01 item 4" exist. Confirming every remaining "item 4" mention is month-qualified:





Confirmed: the only "item 4" in open_items.md is the legitimate month-qualified "(month_01 item 4)" prepaid reference — the validation check was too strict. Re-running the tail checks with the correct rule (only bare "open item 4" refs are prohibited):





**May 2025 close is complete — COMPLETE WITH OPEN ITEMS.** All package validation checks passed.

## Deliverables (`deliverable/month_05/`)

| File | Result |
|---|---|
| `journal_entries.json` | 11 entries (JE-2025-05-01…11), each self-balancing; **no JE booked for the Gusto refund** (per April's stated treatment) |
| `trial_balance.json` | cumulative **1,053,341.90 = 1,053,341.90**; cash 260,300.00; 2200 115,000.00 cr; 4000 240,700.00 cr |
| `deferred_revenue_rollforward.json` | 99,200.00 + 30,000.00 billed − 14,200.00 released = **115,000.00**, ties TB 2200; every opening ties April's closing |
| `bank_reconciliation.md` | bank 260,300.00 = book 260,300.00 — **difference 0.00**; all 33 statement lines independently recomputed (33/33 printed balances tie); nothing forced |
| `open_items.md` | items 1–11 carried with five-month aging; **item 12 CLOSED**; new item 13 |
| `STATUS.md` | updated to May |

## May result
Revenue **44,650.00** (recurring 30,450 + Trestle prior FINAL 8,200 + renewal 2,000 + Marigold 1,500 + Quarry 2,500; Pinecone $0, unidentified $0) − expenses **84,007.78** = net loss **(39,357.78)**; five-month loss (210,588.90). Payroll agreed to register **and** bank on both legs (54,404.00 + 5,076.00 = 48,200.00 + 11,280.00 = 59,480.00 — single net-pay debit this month).

## Key events
- **New contract Quarry Analytics (C-028)** — 30,000.00 annual prepay wired 05/15; deferred in full, release 1 of 12 (2,500.00), 27,500.00 remains. The order form's referenced "MSA v3.2" is not in file — same documented gap as Marigold → **item 13** (treatment doesn't depend on it; stated assumption).
- **Trestle prior contract fully recognized and closed** — final 8,200.00 release, balance 0.00. Renewal exposure cap of **10,000.00 reached at end-May and frozen** pending evidence of the true term.
- **April's 48,200.00 bank duplicate refunded 05/09** (`ACH CREDIT GUSTO REFUND`, ticket GS-44812) — reconciling item extinguished with no entry; item 12 closed; reconciliation back to zero (Jan/Mar recons were also zero — April's was the year's only reconciling item).
- Statement artifacts documented, not trusted: header values print one caption below their labels, and a mid-page "1/Credit/Balance" caption repeat is a page artifact (true count 33). Read by content, the header cross-foots.

No prior-month corrections arose (no ASC 250 matter). One consistency fix was made during validation: May JSON cross-references to the Trestle overlap now read "item 3," matching the running numbering since March.

Ready for June when you are: releases then are 6,000.00 (renewal 2,000 + Marigold 1,500 + Quarry 2,500 — Trestle prior no longer releasing).