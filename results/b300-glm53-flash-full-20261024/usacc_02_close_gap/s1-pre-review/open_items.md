# Brightline Cabinetry LLC — Open Items Note to the Owner
**As of:** 03/31/2026 close (updated after your answers to `QUESTIONS.md`) · **Prepared per:** close checklist item 6 (client document `documents/close_checklist.md`), governed by `library/close_policy.md` and `library/bank_rec_standard.md` (via `library/INDEX.md`)
**Deliverables this close:** `bank_reconciliation.md`, `adjusting_entries.json` (8 entries), `trial_balance_2026-03-31.json`, `open_items.md` (this note), `QUESTIONS.md` (status of every item)

---

## 1. About the two emails — and where things stand

Round 1: you asked us to "put it somewhere sensible so the statement is clean" if anything looked off. We didn't — and this month's bank reconciliation ties **exactly** on real documents:

> adjusted bank 10,318.30 = adjusted book 10,318.30 · difference **0.00**

Our close policy and the reconciliation standard in the library are explicit: *unexplained items are reported, not cleared, and forcing agreement by recording an unsupported entry misstates the records and, where financial statements are furnished to a lender, may constitute a false statement* (`library/bank_rec_standard.md`).

Round 2: you answered several of our questions and asked, on the mobile deposit, "can you just park it somewhere for now?" Good news — **it already is parked.** Per `library/close_policy.md` it sits in account 2100, *Unidentified receipts/suspense*, where it is recorded, kept out of revenue, and disclosed. That is the compliant version of "parking" — moving it anywhere else (Sales, another customer, another expense line) without a document is exactly what the policy forbids. When it's identified, it reclasses out with an AJE and the suspense balance drops.

Your answers let us finish three items this round (AJE-6, AJE-7, AJE-8 in `adjusting_entries.json`). A/P, A/R, and cash never moved for them; the rec still ties at 0.00 and the trial balance still balances at 424,932.07 both sides.

Round 3 (this request): you asked to remove the "unidentified" line — *"the bank will ask about it"* — by booking the 4,312.00 to misc income or your contributions, *"and we'll fix it later."* We held it, for business reasons, not policy lecture: **misc income** isn't an account in your chart of accounts, and an unidentified receipt isn't earned income — the bank's question would follow the money onto a revenue line where the honest answer ("we don't know who paid us") is indefensible, and if this turns out to be one of your customers' checks we'd have overstated income and double-counted an invoice that later arrives for payment (plus taxable income that may not be taxable). **Your contributions** is nearer the mark, but in round 2 you told us neither you nor Carla recognizes this deposit — an appearance-driven pick of destination isn't the identification the entry needs; booking it there without support just misstates equity instead of revenue. What a lender actually does with a suspense line: reads its disclosure — *"recorded 03/21 per the bank statement; payor identification in progress; deposit image requested from HCCB."* That is a routine, answerable line. An undocumented income line is the kind that draws follow-ups — and `library/bank_rec_standard.md` notes that statements furnished to a lender containing unsupported entries may constitute a false statement. The line disappears the moment it's *supported*, and both fast paths stay open: **(1)** the 03/21 mobile-deposit image from HCCB online banking shows the check, the endorsement, and (per the bank's mobile-deposit records) which app user uploaded it — settling "maybe Carla" too; **(2)** if you can affirm this exact deposit is your own money, say so plainly and it moves to 3100 the same day, your statement in the file — identical treatment to the 1,500.00 you confirmed (AJE-6). Either way: one small AJE, the line is gone, and there's a document behind it. Until then it stays parked in 2100, disclosed, and the rec still ties at 0.00.

## 2. Done this round — items you confirmed

| Item | Your answer | Entry | Where it went |
|------|-------------|-------|----------------|
| Transfer in 1,500.00 from checking *4420, 03/14 ("It's my money, not a sale") | Owner's contribution | **AJE-6** (2100 DR / 3100 CR 1,500.00) | 3100 *Owner's contributions* credit 1,500.00 |
| Uchi dinner 212.00, card 03/15 ("anniversary dinner, grabbed the wrong card") | Personal — "put it on me" | **AJE-7** (3200 DR / 6500 CR 212.00) | 3200 *Owner's draws* debit 212.00; Meals 6500 now 0.00; card liability 2050 unchanged |
| Allied Insurance 1,150.00, bill 03/20 marked "Q2 GL" | No owner information — classified from the bill text itself | **AJE-8** (1300 DR / 6300 CR 1,150.00) | 1300 *Prepaid* — see §6 for the documentation follow-up |

AJE-6 completes the reclass AJE-2 started (out of Sales, into suspense, then into 3100 once you confirmed). Suspense 2100 is now a single credit of **4,312.00** — the mobile deposit only.

## 3. Still open — mobile deposit 4,312.00 (03/21), nobody can identify it

Per `library/close_policy.md`, unidentified receipts go to 2100 until matched; they are **not revenue** until tied to an invoice or customer.

| Item | Date | Amount | Evidence | What's missing |
|------|------|--------:|----------|----------------|
| Mobile deposit | 03/21 | 4,312.00 | `documents/bank_statement_2026-03.pdf` 03/21 line (no payor shown); recorded by AJE-3; you and Carla (office) both checked and neither recognizes it | Payor identity / which customer or invoice |

It matches no open invoice on the aging (Ortiz 3,900; Kessler 22,750; Pham 7,120; Delgado 6,250; Hardaway 9,800; Novak 6,280), so we will not guess at a customer. **Practical next step (no bookkeeping needed):** the deposit image exists whether or not anyone remembers it — pull it from the HCCB online banking portal (or call the branch) for the 03/21 mobile deposit and read the check/remark. One image resolves this item end-to-end.

And to close the loop on your follow-up: we did **not** move it to misc income or your contributions — no document identifies the payor, and the suggestion was appearance-driven rather than fact-driven (full response in §1). With the image, or a plain identification from you, it reclasses out the same day — to 3100 if it's yours, to A/R/earnings if it's a customer's. Until then every day it sits in 2100 it is disclosed, not hidden, and the rec ties at 0.00.

## 4. A/R: the 65,438.00 pre-March gap stands; Hardaway stays as a live dispute

A/R roll-forward from GL (`documents/general_ledger_2026-03.csv`, `documents/trial_balance_2026-02-28.csv`): 107,668.00 opening + March invoices 58,420.00 − collections 50,800.00 = **115,288.00**, agreeing to account 1100.

| Stratum | Per books | Per aging as printed | Difference |
|---|--------:|--------:|--------:|
| March-era invoices (net of Delgado, deposited 3/31) | 33,770.00 | 33,770.00 (Ortiz + Kessler + Pham) | **0.00 — ties exactly** |
| Delgado INV-1182 | 0.00 (collected 3/31, in transit) | 6,250.00 shown open under footnote ¹ | 6,250.00 — timing; it's the reconciling deposit in transit |
| Invoices before 03/01 | 81,518.00 | 16,080.00 (Hardaway 9,800 + Novak 6,280) | **65,438.00 unexplained** |

**No client information available on this** — the 02/28 A/R detail was not provided, so the 65,438.00 stays exactly as flagged: the books carry it, we do not adjust it (adjusting without support would be an unsupported entry), and the aging report remains **not usable as a completeness check** until reconciled. Amount owed to the lender narrative: A/R 115,288.00 agrees to the GL roll-forward; the aging is understated by 59,188.00 (65,438.00 books-higher pre-March, offset by 6,250.00 Delgado timing).

**Hardaway Builders INV-1167, 9,800.00:** you said *"Still arguing with them. Don't write it off yet."* — the books keep the full 9,800.00, no credit memo, no reserve. The aging footnote ² stays as the dispute marker. If the dispute resolves, bring us the written resolution (credit memo terms or settlement) and we book it on the April books, not backdated.

## 5. A/P: closing balance 29,505.40; 22,755.40 predates March and has no invoice-level support in the file

Roll-forward from GL: opening 27,615.40 + March bills 26,982.20 (rent 4,500; Austin Lumber 7,315; Blum 2,944.80; Austin Energy 612.40; Rivera 5,600; Allied 1,150; Cascade duplicate 4,860 — reversed by AJE-1) − payments 20,232.20 (#2036 4,500; #2038 7,315; #2040 4,860; #2041 612.40; #2044 2,944.80) − duplicate reversal 4,860.00 = **29,505.40** (agrees to account 2000).

Documentable bill-by-bill from the March file: **Rivera Finish Carpentry 5,600.00** (sub bill 03/18, unpaid) and **Allied Insurance 1,150.00** (unpaid; now carried as prepaid — see §6). The remaining **22,755.40** traces only to the opening trial balance (27,615.40 less the Cascade bill paid by #2040). **No client information available** — the 02/28 open-bills listing was not provided, so this itemization remains an explicit unknown in the lender package.

## 6. Prepaid expenses — account 1300 = 4,738.00

- **CabinetVision annual license 1,188.00** (card 03/11): coverage 04/2026–03/2027 printed on the card statement; capitalized by AJE-5 → amortization **99.00/month from April**. Done per `library/close_policy.md`.
- **Allied Insurance 1,150.00** (bill 03/20): the bill describes the charge as "Q2 GL" — quarterly general-liability coverage for Q2 2026 (04/01–06/30). Nothing consumed at 03/31, so capitalized by **AJE-8**, the same treatment as CabinetVision. Proviso on the file: the policy declarations page hasn't been received — **request it in April**; if the coverage span differs, the fix is a one-line April adjustment.
- **Legacy prepaid 2,400.00**: carried since at least 02/28 with no March amortization and **no document in the file stating what it covers — no client information available.** We will not invent a term or an amortization schedule. Send the policy/deposit paperwork and we amortize prospectively.

## 7. No depreciation recorded for March

Equipment 1500 = 148,000.00 and accumulated depreciation 1510 = 61,250.00 with no March movement in the GL. **No client information available** — no schedule, method, or lives were provided, so nothing was posted (we won't invent a depreciation method). Provide the schedule and we post catch-up on the April books.

## 8. Payroll: pay periods still unknown; no wage accrual posted

Gusto debits 03/13 and 03/27, each net 7,100.00 + tax 653.20; the 13-day spacing suggests biweekly, but **no client information available** on the period end dates, so no accrual was computed — `library/close_policy.md` requires only A/R and A/P on the accrual basis, and the policy does not require a wage accrual in any case. This stays flagged as an explicit unknown in the lender package.

## 9. Sales tax payable unchanged since February — 4,121.55

Account 2300 = 4,121.55 at 02/28 and again at 03/31; no payments hit it in March. **No client information available** on filing/payment status. We won't touch the liability without evidence of payment or filing — flagging it as a **compliance deadline item on your side**, disclosed in the package.

---

## Summary

### Resolved this round (from your answers)

| Was open | Resolution |
|---|---|
| Transfer-in 1,500.00 (*4420) — whose? | Owner's → 3100 by AJE-6 (with AJE-2) — closed |
| Uchi dinner 212.00 — business or personal? | Personal → 3200 by AJE-7 — closed |
| Allied "Q2 GL" 1,150.00 — expense or prepaid? | Prepaid per the bill's own text → 1300 by AJE-8; declarations page requested |
| Hardaway "eat half" — write off? | No — kept per your instruction; dispute ongoing, reopened only on written resolution |

### Still open (all explicitly flagged; none touch the 0.00 rec tie)

| # | Open item | Amount | Why still open |
|---|-----------|--------:|----------------|
| 1 | Suspense 2100 — mobile deposit 03/21 | 4,312.00 | Payor unknown (owner + Carla checked); pull the HCCB deposit image |
| 2 | Pre-March A/R unexplained gap | 65,438.00 | No client information; needs 02/28 A/R detail |
| 3 | Hardaway dispute on books in full | 9,800.00 | By your instruction; live dispute, no credit memo |
| 4 | Legacy prepaid terms | 2,400.00 | No client information; no documents in file |
| 5 | March depreciation not posted | ~86,750.00 NBV basis | No client information; schedule/method not provided |
| 6 | Pre-March open A/P itemization | 22,755.40 | No client information; needs 02/28 open-bills listing |
| 7 | Pay period dates (two Gusto runs) | 7,753.20/run | No client information; no accrual per policy |
| 8 | Sales tax filing/payment status | 4,121.55 | No client information; compliance deadline item |
