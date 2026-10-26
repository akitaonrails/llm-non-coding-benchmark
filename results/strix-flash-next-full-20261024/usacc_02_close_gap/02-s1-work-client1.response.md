Client answers received. Applying them: two new entries (the *4420 transfer and the Uchi dinner), keeping the 4,312.00 in 2100 suspense (the policy-compliant place to "park" it), and no Hardaway entry.

Now updating the open items and questions files with the client's answers.

All deliverables are updated for the client's answers and validated. Final state of the engagement:

**Applied this round**
- **AJE-6** — *4420 transfer 1,500.00: owner confirmed it's his personal money, "not a sale" → Dr 4000 Sales / Cr 3100 Owner's contributions. Sales drop to 138,720.00; cash unaffected. Closed.
- **AJE-7** — Uchi dinner 212.00: personal anniversary dinner ("Put it on me") → Dr 3200 Owner's draws / Cr 6500 Meals. Closed.
- **Cascade CH-7731** — owner confirmed the mailed copy duplicates the emailed invoice and it was paid once, which validates the AJE-3 duplicate reversal (A/P and COGS each −4,860.00). Closed with a housekeeping watch-note on duplicate-invoice remittance details.
- **Hardaway 9,800.00** — "Don't write it off yet" → **no entry**; full amount stays in A/R, dispute disclosed. Stays open by instruction.
- **4,312.00 unidentified deposit** — owner asked to "park it somewhere." It stays in **2100 Unidentified receipts / suspense**, which is the policy-compliant parking spot and what the AJE already does. It was **not** moved to revenue — the payer is still unknown (Carla checked too), and revenue shown to the lender must be identifiable.

**Final numbers**
- Bank rec: still ties at **zero difference** (adjusted bank = adjusted book = 10,318.30); Summit card ties at 2,306.12.
- `adjusting_entries.json`: 7 balanced AJEs (verified programmatically).
- `trial_balance_2026-03-31.json`: 30 accounts, **Dr = Cr = 424,932.07**; YTD NI 29,944.23 (revenue 154,920.00, expenses 124,975.77), draws 212.00, contributions 1,500.00.

**Flagged unknowns (client had no information — reported, not plugged)**
1. **Material:** A/R GL 115,288.00 vs aging 49,850.00 → unexplained **65,438.00** rooted in the 2/28 opening balance. No entry without the 2/28 invoice detail.
2. 4,312.00 deposit in 2100, payer unidentified.
3. Hardaway 9,800.00 dispute (open per owner).
4. Prepaid 2,400.00 — coverage unknown.
5. Allied "Q2" dates assumed Apr–Jun 2026, unconfirmed.
6. No March depreciation — no fixed-asset schedule exists.
7. A/P carryover 22,755.40 — no supporting bills in the file.
8. Check gaps #2037/#2039/#2042/#2043 unaccounted for.

**STATUS: COMPLETE WITH OPEN ITEMS** — everything the documents support is booked; the eight items above are explicitly flagged in `open_items.md`, with the A/R gap marked as must-not-be-presented-to-the-lender-as-supported.