# Juniper Health Staffing, LLC v. Pinecrest Senior Living, Inc. — Session 1 assessment

**Prepared:** October 26, 2026 · **Privileged & confidential — attorney work product**

Scope: assessment of claims, strengths/weaknesses, contract requirements, and forum, based solely on the
client file (`documents/`) and the closed reference library (`library/`). Assumptions are flagged; open
questions are in `deliverable/QUESTIONS.md`.

---

## 1. The contract — what it requires

Staffing Services Agreement, effective January 15, 2024 (`documents/staffing_services_agreement.pdf`):

| Provision | What it requires / gives us |
|---|---|
| §2 Fees; Payment | Pay Schedule 1 bill rates within 30 days of invoice; **1%/month interest** on late amounts; disputes must be noticed **within 15 days of invoice receipt** — invoices not timely disputed are **deemed accepted**. |
| §3 Conversion; Non-Solicitation | Pinecrest may not hire Personnel introduced by Juniper during the term + 12 months **except on payment of 25% of first-year annualized compensation**. Waiver only **"in writing in [Juniper's] discretion."** |
| §6 Limitation of Liability | **No consequential damages between the parties**; carve-out: liability for **unpaid fees and conversion fees is not limited**. |
| §7 Entire Agreement | Integration clause — informal statements outside the writing are vulnerable; but §3 expressly contemplates written waivers, so the Feb. 11 email operates inside the contract. |
| Exhibit C.1 | **AAA arbitration, single arbitrator, Capital City, Columbia** — all disputes "including… the arbitrability of any claim" (delegation clause). C.2 class waiver. C.3 **prevailing-party fees** in any arbitration *or any action to compel arbitration*. C.4 provisional injunctions in court. C.5 survives termination. C.6 small-claims carve-out **only** for "claims solely for collection of undisputed invoices of less than $25,000." |
| §8 Governing law | State of Columbia. |

## 2. Claim-by-claim assessment

### A. Unpaid invoices — $340,000 · **STRONG (with one invoice contested)**

Per `documents/open_invoices.csv`:

| Invoice | Period | Amount | Due | Dispute notice | Status under §2 |
|---|---|---|---|---|---|
| J-4411 | Mar | $68,400 | 2026-04-30 | none | **Deemed accepted** |
| J-4452 | Apr | $71,250 | 2026-05-31 | none | **Deemed accepted** |
| J-4490 | May | $66,100 | 2026-06-30 | none | **Deemed accepted** |
| J-4533 | Jun | $74,800 | 2026-07-31 | yes — 2026-07-09 | timely disputed (see below) |
| J-4571 | Jul | $59,450 | 2026-08-31 | none | **Deemed accepted** |
| **Total** | | **$340,000** | | | |

- **Undisputed: $265,200.** Four invoices draw no dispute notice, so under §2 they are deemed accepted.
  Under the account-stated doctrine, an invoice retained without objection within the contractually fixed
  period is **prima facie evidence of the debt** (CJI 14.02; `library/columbia_account_stated_waiver.md`).
  This is the strongest claim in the case.
- **J-4533 ($74,800) was disputed in time, and the dispute is partly justified.** Lindqvist's audit email
  (7/9) is inside 15 days of the implied ≈7/1 invoice date (exact receipt date unknown; client has no
  further data — carried as assumption). **Client admission (CEO, this session): two shifts were
  double-entered in June, about $3,100; the rest is legitimate.** We therefore credit $3,100 and claim
  **$71,700** on J-4533. Demand the full invoice, or repeat that padding exists after our own CEO has
  conceded it, would assert facts our own file contradicts (CONTRACT.md standards) — the corrected number
  is now in the demand letter. Pinecrest's audit objection, once substantiated at $3,100 out of $74,800
  (≈4%), also cuts against any broader "padded" characterization of the June bill.
- **Interest: +$11,499.50 on undisputed invoices through Oct. 31, 2026** (1%/month; see §4 arithmetic).
- §6 carve-out: unpaid fees are expressly **not limited** by the liability cap.

### B. Conversion fees — demanded $112,000 · **GOOD for 5 hires, DEAD for 2, contested data on amounts**

Contract rate: 25% × each hire's **first-year annualized compensation**. The CEO's spreadsheet uses an
**average of $64,000 → $16,000 per hire × 7 = $112,000**. Per-hire compensation figures are missing
(*QUESTIONS.md Q1*); the $64,000 average is a client-supplied assumption, not a verified fact.

The seven hires (`documents/email_export_juniper.txt`, Bell→CEO 7/20): Rosa M. (CNA, Mar), Tay W. (CNA, Mar),
Priya S. (RN, Apr), Luis F. (RN, May), Keisha B. (LPN, May), Anne O. (RN, Jun), Victor H. (CNA, Jun).
All occurred during the term; §3 applies. None paid fees.

| Hires | Fee at $16k avg | Assessment |
|---|---|---|
| Rosa M., Tay W. | $32,000 | **Waived — do not demand.** Bell's Feb. 11 email ("consider the fee waived for Rosa and Tay as a one-off") satisfies §3's writing requirement. Asserting these fees would contradict our own file; Pinecrest holds the email. |
| Priya S., Luis F., Keisha B. | $48,000 | **Demand — now stronger.** Lindqvist's texts ("same deal as before?", "two more coming over") drew only equivocal replies ("ha, we'll talk"; "😬 call me"). §3 requires waivers **in writing**; these are not. A course-of-dealing implied-waiver/estoppel argument remains available to Pinecrest ("a fact question" per `library/columbia_account_stated_waiver.md`), but **Bell — the only Juniper person involved — now states on the record: he waived "just those two" and "never agreed to the other five."** His testimony contradicts the acquiescence story, and the content of the May 14 call remains unknown to us (client has no further information; carried as assumption that nothing contrary was agreed). |
| Anne O., Victor H. | $32,000 | **Clean.** No prior contact or waiver in the file; hired June 2026, after Bell's 5/20-style protest. Demand in full. |

Note the waiver email helps us beyond Rosa/Tay: its express "as a one-off" limitation is precisely the kind
of term that "does not extend to later hires" under `library/columbia_account_stated_waiver.md`.

### C. Tortious interference — demanded $410,000 · **DO NOT ASSERT — weak to frivolous**

The CEO's $410,000 is lost profits on the whole account. Every element is compromised by our own file:

1. **Party defense.** "*A party to the contract cannot tortiously interfere with it* (the remedy is breach
   of contract)" — *Ashby v. Caldera Partners*, 212 Col. App. 3d 440 (2019) (`library/columbia_tortious_interference.md`).
   Pinecrest is a party.
2. **At-will employees.** Interference with Juniper's relationships with its at-will staff requires **improper
   means**; nothing in the file shows fraud, threats, or the like — the hires were announced openly by email/text.
3. **Consent.** The Feb. 11 waiver email and Lindqvist's texts ("same deal as before?") evidence consent at
   least in part — a **complete defense** (Restatement §773, via *Ashby*).
4. **Legitimate business justification.** Lindqvist twice put corporate cost-cutting on the record (5/2 email,
   5/14 text) — §773 justification, also a complete defense.
5. **Contract bar.** §6 excludes consequential damages between the parties; only unpaid fees and conversion
   fees escape the cap. Lost account profits are quintessential consequential damages.
6. **Pleading risk.** "A tortious-interference claim fails where the complaint and incorporated documents
   show consent or justification" (`library/frcp_12b6.md`, *Iqbal*). Attaching the contract and quoting the
   emails would doom the claim at the 12(b)(6) stage. Rule 3.1 caution applies (`library/fee_shifting_and_candor.md`):
   we should not build the demand — or later a pleading — on this theory.

### D. Interest — **STRONG (contractual)** — see arithmetic below.

## 3. Forum — the CEO's "lawsuit" plan is the wrong first move

- Exhibit C.1 sends **everything** — including arbitrability — to AAA arbitration before a single arbitrator
  in Columbia. FAA §§2–4 make that "valid, irrevocable, and enforceable" (`library/faa_2_4.md`); the delegation
  clause ("including… the arbitrability of any claim") is "clear and unmistakable" and would be enforced
  (*Rent-A-Center v. Jackson*, 561 U.S. 63 (2010), as summarized in the library).
- **Filing in court as the opener is a fee trap.** If we sue, Pinecrest moves to compel; we would be sent to
  arbitration and, under Exhibit C.3 plus *Zuniga v. Mercer*, 198 Col. 2d 77 (2017), "a party that files suit
  on arbitrable claims may be compelled to arbitrate and, under a fee clause, may owe the fees of the motion
  to compel" (`library/faa_2_4.md`, `library/fee_shifting_and_candor.md`).
- **No usable court carve-out.** C.6 allows small claims only for "claims solely for collection of undisputed
  invoices of less than $25,000." Every invoice exceeds $25,000 individually, and our claim includes
  conversion fees — so C.6 is unavailable. C.4 (provisional injunction in aid of arbitration) has no obvious
  application here; there is no imminent-irreparable-harm fact pattern.
- **Bottom line:** demand letter now → AAA demand if no resolution. We hold a strong invoice claim they
  cannot move out of arbitration either; fees provisions cut both ways, so pick claims we can win.
  Fee exposure quantification is deferred to Session 5 (no AAA fee data in the library — do not invent one).

## 4. Numbers — showing the arithmetic

**Interest** (contract §2: 1%/month, simple, whole months past due through Oct. 31, 2026 — assumption:
months counted from due date; exact day-count would change figures slightly; J-4533 shown net of the
client-acknowledged $3,100 double-entry credit):

| Invoice | Amount | Due | Months past due | Interest |
|---|---|---|---|---|
| J-4411 | $68,400 | 4/30 | 6 | $4,104.00 |
| J-4452 | $71,250 | 5/31 | 5 | $3,562.50 |
| J-4490 | $66,100 | 6/30 | 4 | $2,644.00 |
| J-4533 | $71,700 (= $74,800 − $3,100 credit) | 7/31 | 3 | $2,151.00 |
| J-4571 | $59,450 | 8/31 | 2 | $1,189.00 |
| | **$336,900** | | | **$13,650.50** |

Undisputed-four interest: $13,650.50 − $2,151.00 = **$11,499.50**.

**Conversion fees (CEO average $64,000):** 0.25 × $64,000 = $16,000/hire.
Clean (2 hires) = $32,000 · contested (3 hires) = $48,000 · waived (2 hires) = $32,000.

**Defensible demand:** $336,900 + $13,650.50 + $80,000 (5 non-waived hires) = **$430,550.50**.

**Reconciliation with the CEO's $862,000** (it does not survive intact, and here is exactly where the gap is):

```
$862,000 (CEO) = $430,550.50 (defensible demand)
               + $410,000   tortious interference — do not assert (§2C above)
               + $32,000    Rosa & Tay conversion fees — waived in writing by our own account manager
               + $3,100     J-4533 double-entered June shifts — conceded by our CEO; credited
               − $13,650.50 contractual interest we now add
Check: 430,550.50 + 410,000 + 32,000 + 3,100 − 13,650.50 = 862,000.00 ✓
```

Scenario floors (invoiced amounts and the $3,100 credit are firm on this record; only the conversion-fee
tranche is at real risk):
- All five conversion fees denied (implied waiver/estoppel wins): $336,900 + $13,650.50 = **$350,550.50**
- Clean two only (Anne, Victor): +$32,000 = **$382,550.50**
- All five (Bell's statement defeats the defense): **$430,550.50**
These are ranges, not promises; settlement banding is a Session 5 exercise.

## 5. Strengths / weaknesses summary

**Strengths:** deemed-accepted invoices under §2 + account stated (CJI 14.02) on $265,200; contractual
1%/month interest; §3 fee clause with a waiver written "as a one-off" that by its terms does not extend
further, and Bell's now-documented position that he "never agreed to the other five"; §6 carve-out
expressly preserves fees and conversion fees; Pinecrest's audit produced only a ~$3,100 (~4%) error that
*we* substantiated, not the padded-books narrative; corporate cost-cutting was Pinecrest's stated reason,
which frames the hires as business as usual rather than our management.

**Weaknesses:** the Feb. 11 waiver email kills $32,000 of the fee claim and colors the next three hires;
Bell's equivocal texts ("ha, we'll talk", "call me") still create a fact-finder waiver/estoppel risk worth
up to $48,000, and the June double-entry (≈$3,100) is a genuine defect in our own invoicing that opposing
counsel will use to attack bill reliability generally; the tortious-interference claim is the CEO's favorite
number ($410,000) and the least defensible piece of the case; the arbitration clause forces us into a forum
where C.3 fee-shifting can penalize a wrong first move; conversion-fee amounts rest on an unverified $64,000
average, and per-hire compensation (RN vs. CNA mix) could move the number materially in either direction.

**Candor note (per CONTRACT.md standards):** the file we hold contradicts a large share of the CEO's
$862,000. The demand letter asserts $430,550.50 (net of the client-conceded $3,100 credit) and stays off
the tort theory entirely. Per
`library/fee_shifting_and_candor.md`, a misstatement in a demand letter that is repeated in a pleading
becomes a statement to a tribunal — so the letter is built only on what the file can prove.
