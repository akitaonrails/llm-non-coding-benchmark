# Memo — Buyer A ($3,100,000 asset sale) vs. Buyer B ($2,850,000 stock sale)

**To:** Ray Brightline, Brightline Cabinetry LLC
**Date:** October 25, 2026
**Re:** Comparing the Lone Star (A) asset-sale LOI and the Hensley (B) stock-sale LOI

All citations below are to files in `workspace/library/` (the closed library for this engagement). Anything
outside the library is labeled **[unverified — outside library]**. All source numbers trace to the two LOIs,
the fixed-asset register, and the CPA tax-history/conversion file in `workspace/documents/`.

---

## 1. Bottom line

**Do not sign Buyer A's LOI on Friday as drafted.** Your rule of thumb — "$3.1M > $2.85M and business sales
are capital gains" — is the right instinct applied to the wrong deal. Buyer B's deal actually *is* mostly
capital gain; Buyer A's is not.

At an assumed **2026 closing** (both fallback assumptions stated in §8):

| Scenario | Total tax | Net after tax | vs. B (PV basis) |
|---|---:|---:|---:|
| A, as drafted | $909,399 | $2,190,601 | **B wins by $157,688** |
| A, counter-allocation (VI = $100k) | $814,199 | $2,285,801 | **B wins by $62,488** |
| A, best allocation (VI = $0) | $797,199 | $2,302,801 | **B wins by $45,488** |
| B, stock sale (PV @ 6%) | $519,300 | $2,348,289 PV ($2,420,700 nominal) | — |

Even the *best possible* re-cut of Buyer A's allocation does not close the gap at a 2026 close. Two levers do:

1. **Timing.** If the asset-sale closing slips past **December 31, 2027**, the entity-level built-in gains
   tax disappears entirely (§1374 recognition period ends). That is worth **$149,499** after tax to you on
   the A side and flips the ranking: counter-allocation A nets **$2,435,300** vs. B's $2,348,289.
2. **Price with corrected classes.** To match B's value at a 2026 close, A's price must rise to
   **≈ $3,178,110** on the corrected allocation (≈ $3,156,860 if the noncompete goes to $0) — or
   **≈ $3,350,298** if Lone Star keeps its drafted class pattern.

**Negotiating position:** counter A on the allocation (worth $95,200–$112,200) and on the closing date
(target a post-12/31/2027 close, or a price bump to ~$3.16–3.18M to compensate); keep B warm as your walk-
away. If A won't move on allocation, timing, or price, **take B at $2.85M** — it beats A as drafted by
roughly $158k of present value, and it delivers the clean capital-gain result you were pricing in.

Your naive estimate of $2,480,000 from deal A ($3.1M × 0.80) **overstates the real number by $289,399**.
Deal B is the one that lands near your estimate.

---

## 2. Buyer A as drafted — character of every dollar

Exhibit A of the A LOI allocates the $3,100,000 exactly as: Class III receivables **$200,000**; Class IV
inventory **$150,000**; Class V equipment & vehicles **$900,000**; Class VI five-year noncompete
**$400,000**; Class VII goodwill **$1,450,000** (sums to $3,100,000). The *class placement* is correct under
the library's class list — `irc_1060_form_8594.md`: Class III = mark-to-market assets and **accounts
receivable**, Class IV = **inventory**, Class V = all other assets (equipment, vehicles), Class VI = §197
intangibles **including noncompete covenants**, Class VII = **goodwill** — the library
controls here, and the defects in Exhibit A are not classification errors: they are in the **amounts**, §3.

Because the S election is effective 1/1/2023 (tax-history file), a 2026 asset-sale closing sits inside the
five-year §1374 recognition period (`irc_1374.md` (d)(7): 1/1/2023 – 12/31/2027).

### Class III — receivables, $200,000 → **ordinary**

**[Assumed — Q1 unanswered; your CPA can resolve in one call.]** The CPA file lists AR of $200,000, no
reserve, but not the accounting method. Cash-method fallback: zero basis in the receivables, so selling them
for $200,000 produces **$200,000 of ordinary income** — taxed at 37%, not 20%. (If Brightline is accrual
with basis = face, this $200,000 of sale-year ordinary income disappears — see §8 sensitivity; it is now
outcome-relevant.)

### Class IV — inventory, $150,000 → **ordinary**

Carrying value per the CPA file is **$140,000**, so Exhibit A's $150,000 generates $10,000 ordinary.
Inventory gain is ordinary regardless (stock in trade). The $10,000 premium over carrying value has no
support in the file.

### Class V — equipment & vehicles, $900,000 → **all §1245 ordinary**

The fixed-asset register shows cost $1,100,000, accumulated depreciation **$860,000**, adjusted basis
**$240,000**, total FMV **$650,000** — of which the three trucks are $135,000 FMV / $104,000 basis. At the
drafted $900,000: gain = $900,000 − $240,000 = **$660,000**. Under §1245 (`irc_1245.md`), ordinary recapture
is the lesser of (recomputed basis − adjusted basis) and amount realized − basis — here the whole gain,
because depreciation of $860,000 exceeds the $660,000 gain. **Not one dollar of Class V gain is capital.**
Even at the register's true FMV of $650,000, the $410,000 gain is fully recaptured: every per-asset gain is
below that asset's own accumulated depreciation (checked asset by asset — CNC $230k gain/$420k dep;
edgebander $71k/$156k; spray booth $48k/$98k; dust collection $30k/$95k; trucks $31k/$61k; shop misc
$0/$30k).

### Class VI — 5-year noncompete, $400,000 → **ordinary**

`irc_197_and_noncompete.md`: payments to a selling shareholder for a covenant not to compete are
**ordinary income** to the seller (Rev. Rul. 69-643; *Muskat*). Exhibit A even labels it as consideration
for the covenant, so the label is binding on the parties — the library file confirms the parties' written
allocation binds them (*Danielson*; §1060(a)) "absent strong proof of contrary economic reality," and the
IRS may challenge allocations that don't reflect economic reality. Note what that same file implies for
this number: **Hensley offered you a 3-year covenant for $0.** A written $400,000 price tag on a longer
covenant in the A deal is worth exactly nothing to you in tax terms — 37 cents of every dollar to the IRS
vs. 20 in Class VII — and its removal is the cheapest concession to demand.

### Class VII — goodwill, $1,450,000 → **long-term capital gain**

Self-created goodwill sold with the business: the library's overview (`stock_vs_asset_overview.md`) treats
asset-sale recapture and covenant payments as ordinary and stock-sale gain as capital; goodwill is neither
recapture property nor a covenant payment, and zero basis means the full $1,450,000 is gain taxed at 20%.
**[Character per library overview; the file does not spell out "self-created goodwill = LTCG" verbatim.]**

### Entity level — §1374 built-in gains tax: **$237,300**

At conversion (1/1/2023) the CPA's appraisal fixed built-in gain at **goodwill/trade name $900,000;
equipment & vehicles $230,000; other assets $0**. Recognized BIG per asset is capped at that conversion
built-in gain (`irc_1374.md`): equipment min($660,000 gain, $230,000) = **$230,000**; goodwill
min($1,450,000, $900,000) = **$900,000**; receivables/inventory/covenant $0. Net recognized BIG
**$1,130,000 × 21% = $237,300** entity-level tax, a real cost to you — but not a deadweight one:
`irc_1374.md` (citing §1366(f)(2)) treats the tax paid as **a loss sustained by the S corporation**, which
passes through and offsets your sale-year income. Modeled against ordinary income first **[ordering
convention — outside library; harmless here since ordinary income exceeds the entity tax by at least
$372,700 in every scenario]**, the shareholder-level math is:

```
Ordinary:  200,000 + 10,000 + 660,000 + 400,000            = 1,270,000
Capital:   1,450,000                                        = 1,450,000   (total gain 2,720,000
                                                                        = 3,100,000 − 380,000 basis ✓)
Entity:    1,130,000 × 21%                                  =   237,300
Individual: 37% × (1,270,000 − 237,300) = 382,099
            20% ×  1,450,000            = 290,000          =   672,099
Total tax: 237,300 + 672,099                               =   909,399
Net:       3,100,000 − 909,399                             = 2,190,601   ← effective rate 29.3%
```

---

## 3. The counter-allocation — what to sign instead

Same classes (they're correct), honest amounts: **III $200,000 / IV $140,000 / V $650,000 / VI $100,000
(target $0) / VII $2,010,000 (residual).**

Justification, class by class:

- **Class V = $650,000, the register's own FMV.** Exhibit A's $900,000 is $250,000 above the appraised-in-
  the-register value of everything in the class. Both parties must report the allocation **consistently**
  on Forms 8594 (`irc_1060_form_8594.md`), and *Danielson* binds *you* to your own written number
  (`irc_197_and_noncompete.md`) — if you sign $900,000 for a $650,000 class, you are locked into reporting
  $250,000 of phantom ordinary recapture income the IRS will happily let you keep. This is the single
  most indefensible number in the LOI and Lone Star knows it: their own deal file's asset list is the
  register.
- **Class IV = $140,000 carrying value** (CPA file). No support for the $150,000.
- **Class VI ≤ $100,000, target $0.** Hensley got a *shorter* covenant for nothing. Any real consideration
  you take for the covenant is ordinary anyway; the $400,000 is a 17-point tax leak ($68,000) dressed as a
  deal term. If Lone Star wants to pay for a covenant, it should *increase the price*, not re-label goodwill.
- **Class VII takes the residual** — the §1060 residual method is exactly how the library file describes
  allocation (`irc_1060_form_8594.md`): Classes I–VI first, goodwill absorbs the rest. For Lone Star the
  trade is roughly neutral: they lose §1245 step-up they were over-claiming (Class V above FMV is not
  defensible to the IRS either — the same file's consistent-reporting and FMV logic), and gain §197
  15-year amortization on a bigger goodwill number.

```
Ordinary:  200,000 + 0 + 410,000 + 100,000                =   710,000
Capital:   2,010,000                                       = 2,010,000
Entity:    min(410,000,230,000) + min(2,010,000,900,000)  = 1,130,000 × 21% = 237,300 (unchanged!)
Individual: 37% × (710,000 − 237,300) = 174,899; 20% × 2,010,000 = 402,000 = 576,899
Total tax: 814,199      Net: 2,285,801     (+$95,200 vs. drafted)
Best case, VI = 0:  ordinary 610,000 / tax 797,199 / net 2,302,801  (+$112,200)
```

Note the entity tax is **identical** ($237,300) in drafted and counter scenarios: both §1374 caps are
already binding (equipment gain ≥ $230,000 BIG; goodwill gain ≥ $900,000 BIG) whether or not you move
dollars around. So every reallocated dollar saves exactly **37% − 20% = 17 cents** and not a cent more —
$660,000 moved drafted→optimal × 0.17 = $112,200. ✓

---

## 4. Buyer B — the stock sale that actually behaves like a capital gain

Structure: $2,350,000 cash at closing + $500,000 seller note (5 years, 6%, annual interest, $100,000
principal/yr); buyer assumes **all liabilities, known and unknown**; 12-month indemnity capped at 10% of
price ($285,000); $100,000 escrow; 3-year noncompete with no separate consideration.

- Gain: $2,850,000 − $420,000 stock basis = **$2,430,000, all long-term capital gain**
  (`stock_vs_asset_overview.md`). No §1245, no §1374 — the corporation sells nothing.
- Installment method (`irc_453_installment.md`): gross-profit ratio 2,430,000 / 2,850,000 = **85.2632%**.
  Closing payment recognizes 2,350,000 × 85.2632% = $2,003,684 of gain (tax $400,737); each $100,000
  principal installment recognizes $85,263 (tax $17,053/yr). The §453(i) rule that forces recapture income
  into year 1 doesn't bite — a stock sale has no asset recapture.
- Note interest 30/24/18/12/6 = **$90,000 ordinary**, tax $33,300 at 37%.

```
Total tax:  2,430,000 × 20% + 90,000 × 37% = 486,000 + 33,300 = 519,300
Nominal net: 2,850,000 + 90,000 − 519,300                       = 2,420,700
After-tax flows: 1,949,263 | 101,847 | 98,067 | 94,287 | 90,507 | 86,727
PV @ 6%:                                                  = 2,348,289
  less escrow timing (100k of closing cash held 12 mo):   −    5,660  → 2,342,628
```

The PV comparison is the honest one: A pays in one day; B drips for five years and carries $500,000 of
your buyer's credit risk as an unsecured seller note **[credit-risk treatment is a stated assumption, not
library law]**. At 6% the note stream costs you ~$72,411 of value versus face; at 8–15%: $2,328,042 /
$2,309,407 / $2,292,219 / $2,268,841.

Two loose ends on B's paper: (i) the **$0 covenant** — `irc_197_and_noncompete.md` says allocations must
reflect economic reality and the IRS may challenge them, so there is a low-probability argument the IRS
re-labels part of B's price as ordinary covenant income; the same economic-reality language supports
honoring $0 when the covenant is ancillary to a stock sale **[unverified beyond the file's language]**;
(ii) selling S-corporation *stock* to your LP buyer will terminate the S election post-closing — a buyer-
side issue that can surface as a PSA price argument **[S-corp eligibility rules are outside the library —
flagged, not analyzed]**.

---

## 5. Liabilities: the Hardaway dispute, warranty, and the escrow squeeze

You told us: the Hardaway dispute ($9,800) and "the usual warranty stuff — nothing big that I know of."
Warranty exposure is therefore **unquantified** and stays flagged, not modeled.

- **Deal A:** Lone Star assumes *only* trade payables listed on a closing schedule; disputed items are not
  scheduled payables — **you keep Hardaway**. The LLC pays it pre-closing (or in its final year) and the
  deduction passes through at 37%: after-tax cost ≈ $9,800 × 0.63 = **$6,174**. Every $1 of retained
  warranty claims costs you $0.63.
- **Deal B:** Hensley takes **all liabilities, known and unknown**. Disclose Hardaway on the schedules and
  it belongs to the buyer at closing: **$0 to you**. If it surfaces undisclosed, it comes back through the
  escrow/indemnity (well inside the $100,000 escrow and $285,000 cap). If instead they reprice it at PSA,
  worst case is a $9,800 price cut: after-tax $9,800 × (1 − 85.2632% × 20%) = **$8,129**.
  Either way it cannot move the ranking — it is ~1% of the gap.
- **Escrow squeeze (both deals):** your *known* contingency pool is ≈ $10,000. B's drafted $100,000 escrow
  is ~10× that, but its PV cost is only ~$5,660 — concede it, and instead negotiate that the disclosed
  Hardaway matter is excluded from the indemnity. A's LOI has **no escrow at all** — expect Lone Star to
  ask for one in the PSA; cap it at ≤ 2.5% of price, 12 months, Hardaway carved out.

---

## 6. Head-to-head

| | A drafted | A counter | A best | B (PV@6%) |
|---|---:|---:|---:|---:|
| Price / proceeds | 3,100,000 | 3,100,000 | 3,100,000 | 2,850,000 + 90,000 interest |
| Ordinary income | 1,270,000 | 710,000 | 610,000 | 90,000 |
| Capital gain | 1,450,000 | 2,010,000 | 2,110,000 | 2,430,000 |
| Entity (§1374) tax | 237,300 | 237,300 | 237,300 | 0 |
| Total tax | 909,399 | 814,199 | 797,199 | 519,300 |
| Net (nominal) | 2,190,601 | 2,285,801 | 2,302,801 | 2,420,700 |
| **Net (PV@6%)** | **2,190,601** | **2,285,801** | **2,302,801** | **2,348,289** |
| Liabilities | retained (Hardaway ~6,174) | same | same | assumed (≈ $0 if disclosed) |
| Cash at closing | 3,100,000 | 3,100,000 | 3,100,000 | 2,250,000 + 100k escrow |
| Credit/claim risk | none (cash out) | none | none | $500k unsecured note |

**Post-2027 close (recognition period over — `irc_1374.md` (d)(7)):** entity tax $0 → drafted $2,340,100 /
counter **$2,435,300** / best **$2,452,300** nominal. B's PV advantage evaporates: A-counter beats B by
~$87,000; even drafted A is within ~$8,200. If *both* closings defer a year, both sides discount ~5.7% at
6% and the ranking holds. Deferring A's close out of the window is worth **$149,499** — the single largest
number in this file. And if Lone Star insists on a 2026 close, the price fix is ≈ **$3,178,110** (counter
allocation; $3,156,860 at VI=0; $3,350,298 if they keep their drafted class pattern where marginal dollars
land in all-ordinary Class V equipment at a 63-cent net marginal rate).

---

## 7. Recommendation & negotiating points

1. **Counter A on allocation now** (Form 8594 schedule in `form_8594_counter.md`): III $200k / IV $140k /
   V $650k / VI ≤ $100k / VII residual. Worth **+$95,200–$112,200**. This costs Lone Star nothing real —
   their register supports your numbers, and consistent 8594 reporting protects them too.
2. **Move the closing date.** Ask for a closing after **12/31/2027** (or structure: sign now, close
   January 2028 — the 45-day exclusivity works in your favor for keeping B warm). Worth **+$149,499**.
   If they refuse, price it: ~$150k added consideration restores A's lead (≈ $3.18M on corrected classes).
3. **Fix the liabilities paper:** Hardaway disclosed and specifically carved out of any indemnity/escrow
   in either deal; A escrow (when it appears in the PSA) ≤ 2.5% / 12 months; B escrow conceded as-is
   (~$5,660 PV) in exchange for the Hardaway exclusion.
4. **Hedge B's credit risk** if you end up there: secure the $500k note (security interest in the assets),
   acceleration on default, keep the 10%-cap indemnity as drafted.
5. **If A refuses allocation, timing, and price** — sign B. It nets ~$158k more (PV) than A as drafted,
   ~$45k more than A's best case, all-cash-equivalent character at 20%, and it walks your ~$10k of known
   liabilities across the closing table with the company.

## 8. Assumptions & open items (client could not answer — resolve via CPA/PSA)

- **Q1 AR accounting method** — cash/zero-basis fallback used (+$200k ordinary, $74,000 tax, in every A
  scenario). Accrual would *cut each A scenario's sale-year tax by $74,000* and flip counter-allocation A
  past B's PV by ~$11,512 at a 2026 close. **This is now outcome-relevant — call the CPA before Friday.**
  Related: the appraisal's "other assets BIG $0" fits accrual; if cash-method AR really carries $200k of
  conversion BIG, entity tax rises to $279,300 and each A net falls $26,460.
- **Q2 liabilities** — no payables schedule for A's assumption → $0 modeled (each assumed payable is extra
  A consideration under the residual method, `irc_1060_form_8594.md`). Hardaway $9,800 + unquantified
  warranty handled per §5; warranty not modeled.
- **Q3 closing date** — 2026 assumed; the post-2027 alternative is fully priced above.
- **Q4 NIIT** — material participation assumed, so no NIIT (library rate sheet disapplies it for active
  businesses). If wrong: +$103,360 per A scenario vs +$95,760 on B; the **3.8% rate itself is not in the
  library [unverified]**.
- **Conventions:** BIG loss offsets ordinary first (never binds — margin ≥ $372,700); taxes paid in the
  year income is received; PV discount 6% (8/10/12/15% shown). Texas franchise-tax effects of either
  structure: outside the library, not analyzed **[unverified]**.

*Every figure above is reconciled: A scenarios all produce total gain $2,720,000 = $3,100,000 − $380,000
of asset basis (inventory $140,000 + equipment $240,000) regardless of allocation — the allocation only
moves character; B's flows sum exactly to $2,420,700 nominal. Nothing was forced to balance.*
