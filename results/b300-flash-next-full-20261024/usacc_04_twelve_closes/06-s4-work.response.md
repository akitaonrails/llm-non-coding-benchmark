

April has a new twist — an office-manager note about **two net-pay debits but only one payroll**. Let me parse the bank statement:





The prior TB uses a dict with different codes than my draft assumed — let me see the full account list:





No 2100 payroll-tax payable in the prior TB — I must match March's actual payroll posting pattern. Checking March JEs:





Now I understand the true conventions. Before rewriting, I need to nail down the April bank PDF parsing. Raw dump first:





March carryover list captured. Now writing the April builder in three compact scripts. First, sources + bank verification:





March had 25 invoices (24 recurring + Marigold C-027). Fixing the continuity assertion:





Date format mismatch in my multiset (bank `04/26/2025` vs receipt `2025-04-26`). Fixing:





That edit broke the loop header — rewriting it correctly:





Verification clean. Now generating the statement table rows and re-checking exact month_03 JSON shapes before posting:






Schema confirmed. Now the rollforward tail, TB totals, and full March open items for carryover:






All figures cross-checked. Writing the posting script:





One bug in the posting loop — it drops the prior credit balance before netting. Fixing:





That edit was a no-op — applying the real paren fix:





Already fixed. Running:





All JSON deliverables tie. Now the markdown files — checking month_03 reconciliation format for consistency:





March format clear. Checking April statement header wording before writing the reconciliation:





Bank header values misprinted under shifted labels (333,690 / 130,260 / 30,450) — ending 233,880 only on the last transaction row. Writing the reconciliation:





Table injected. Now reading March open_items items 1–2 in full for accurate carryover:





All March items captured. Writing April open_items.md with 4-month aging and the new duplicate-debit item:





Now updating STATUS.md to April, following the same per-month format:





STATUS.md updated. Final validation pass over all written April deliverables:





The withdrawal table also starts with `| 04/` — refining the check to ledger-table rows only (7 columns):





Checking actual withdrawal count in the verified ledger:





One precision check on the reconciliation's integrity sentence — counting actual printed/tie results in the verified ledger:





Refining that sentence to match the ledger exactly (31 printed balances, 30 tie, 1 mismatch, 1 unprinted):





April 2025 close is complete. All five deliverables are in `deliverable/month_04/` and `deliverable/STATUS.md` now reads **April 2025 — COMPLETE WITH OPEN ITEMS**.

## April 2025 close — summary

**Books** (9 journal entries, each self-balancing, independently re-derived from the March TB + April sources in final validation):
- Revenue **42,150.00** = recurring invoices INV-2276..2299 30,450.00 + Trestle prior release 8,200.00 (4th of 5) + renewal release 2,000.00 (4th of 12) + Marigold release 1,500.00 (2nd of 12). C-025 and UNIDENTIFIED: $0, unchanged.
- Expenses **83,837.78** = opex 22,580.00 + payroll 59,480.00 + depreciation 1,777.78 → **net loss (41,687.78)**; four-month YTD loss **(171,231.12)**.
- Trial balance ties: **991,114.12 = 991,114.12**. Deferred revenue roll-forward: 110,900.00 + 0 − 11,700.00 = **99,200.00**, agrees with TB account 2200 to the penny.

**Bank reconciliation — first non-zero difference, fully identified, nothing forced:**
- Bank **233,880.00** vs book **282,080.00** → difference **48,200.00** = the bank's duplicate `ACH GUSTO NET PAY` debit (04/25 + 04/26 for a single payroll run; Gusto ticket #GS-44812 open). The bank's own header totals include both debits, so it was actually processed — not a display artifact.
- Books carry exactly one payroll, agreed to the register AND the real 04/25 debits; no receivable booked (library silent — stated gap). When the reversal arrives, expect **no journal entry** — the reconciling item simply extinguishes.
- All 32 statement lines recomputed: 30 printed balances tie exactly, 1 mismatch and 1 unprinted balance are both documented PDF-extraction artifacts (header values print one caption off; Fjord's balance displaced onto the duplicate row); the recomputed roll lands exactly on the printed ending 233,880.00.

**Open items**: running list continues — new item 12 (bank duplicate, with escalation path), items 1–11 carried with 4-month aging (opening A/R 92,650.00 and A/P 17,420.00 now four months untouched; Trestle overlap exposure caps 10,000.00 by end-May). No ASC 250 corrections needed.

Ready for **May 2025** next — key events to expect: Trestle prior contract **final** 8,200.00 release, renewal 2,000.00, Marigold 1,500.00, and watching for the GS-44812 reversal (no JE if it arrives).