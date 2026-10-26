Client answers received. Let me first check the TB file structure before applying the one new entry this triggers.

The file stores non-ASCII as `\u2014` escapes — I'll modify AJE-3 via Python instead:

Trial balance updated and re-verified. Now updating the three markdown deliverables:

All deliverables updated for the client's responses and re-verified (JSON parses, 7 AJEs balanced, TB Dr = Cr = $424,932.07, every account code validated against the client's own chart of accounts in the earlier pass — `3100 Owner's contributions` is a valid code).

## What changed based on the client's answers

**1 new accounting move — the only one the answers required:**
- **$1,500 transfer from *4420** → AJE-3 now credits **3100 Owner's contributions** instead of suspense: *Dr 4000 Sales 1,500 / Cr 3100 1,500*, memo quoting his exact words ("my money, not a sale"). Effect: suspense 2100 drops $5,812 → **$4,312**; contributions 3100 appears at $1,500; TB total unchanged (same $1,500 just moves from liability to equity). Full roll-forward re-verified: **zero mismatches** per account.

**Confirmed as correct, no change needed:**
- **Cascade CH-7731** — client confirms one invoice, paid once; AJE-2 reversal stands. Only the "is the 2/26 booking inside the Feb close?" assumption remains (unprovable without the February GL — flagged).
- **Uchi $212** — personal; AJE-7 draws treatment confirmed.
- **Hardaway $9,800** — client says don't write off; nothing was booked and nothing will be without a credit memo/settlement; stays in A/R aged 90+.

**On "just park it somewhere" (the $4,312 mobile deposit):** it's parked exactly where the close policy says — **suspense liability 2100**, visible on the balance sheet, **not revenue, not buried** in some plausible-looking account. Neither Ray nor Carla knows the payer, so I've proposed the one concrete path forward: ask the bank for the **mobile-deposit image/deposit slip for 03/21** (needs only his authorization). The bank rec's lender note explains this directly.

**Flagged unknowns** (client had no info): the $59,188 A/R control-vs-aging gap (still the biggest issue — lender told A/R is "in the process of being confirmed"), the $2,400 unsupported prepaid carryover, the Allied Apr–Jun assumption, and unverified payroll gross/deductions. All written into `open_items.md` and `STATUS.md`; `QUESTIONS.md` now logs the answers received and asks only for documents/authorizations that could close the rest.

**Status: COMPLETE WITH OPEN ITEMS** — books tie ($0.00 bank difference, balanced TB), with four disclosed unknowns awaiting documents, not plugs.