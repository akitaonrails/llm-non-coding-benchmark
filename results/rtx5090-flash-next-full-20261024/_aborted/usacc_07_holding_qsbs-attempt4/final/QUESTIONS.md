# Open items and information requests — Nadia Oakline

**Updated 2026-10-25 after the client's response.** Answered items are recorded below and are **not re-asked**. The
client states she has **no additional information** on anything else, so this file no longer poses questions to her.
It now does three things: (1) closes what she answered, (2) lists what can only come from **third parties** — Helio,
her CPA, the lender, counsel — where her only role is to authorize the request, and (3) records what cannot be
established at all and how `opinion.md` handles it. References in parentheses are the original question numbers.

---

## 1. Answered — closed

| Ref | Client's answer | Where it is used |
|---|---|---|
| (Q9, partly) | Helio is in discussions with acquirers; a sale in **12–18 months** is realistic; her stake would be about **$9–10M**. | `opinion.md` §8.3–§8.5; `numbers.json` → `client_response_2026_10_25`, `qsbs_detail.exit_scenarios` |
| (Q8, partly) | The $1.9M mortgage is **nonrecourse to her personally**; the 2024 refinancing proceeds went into her **personal brokerage account**. | `opinion.md` §8.7; §7.7 flag unchanged |
| (Q6, partly) | The 1% member is her **revocable living trust**; the advisor's reason was "we need two partners." | `opinion.md` §8.2 — the two-partner premise is rejected; the 99/1 design should be abandoned |
| (2026-10-25 challenge) | Challenged the §1202 conclusion: the advisor said "the holding is how I avoid tax when Helio sells — 'the gain lands in the LLC'" and asked who is right and whether the holding can own the stock **after** the sale. | `opinion.md` **§9** — answered on the existing record; **no information needed from the client** |

## 2. Still open, and gating

**G1 — Has anything already been executed? (from Q9).** `documents/org_chart.md` carries a "Step 1: Wyoming" note dated
**2025-11-04**, so Oakline Holdings may already exist even though the proposal is dated 2026-02-11. Needed: whether
Holdings has been formed, whether any assignment/contribution agreement or membership certificate has been signed,
whether **any Helio share** has been assigned or pledged, and whether bank accounts have been merged. *This is the
single most urgent item in the file: if the Helio shares were already moved, the §1202 analysis is no longer
prospective and the opinion must be redone.*

**G2 — Lender position on the $1.9M mortgage (remaining half of Q8).** Nonrecourse status is answered; the
**due-on-sale / change-of-control and consent** question is not. Only the loan documents and the lender can answer it.
See R3.

---

## 3. Requests to third parties (the client need only authorize these)

**R1 — From Helio Grid (company records, not personal knowledge) (was Q1, Q2, Q4):**
1. Balance sheet / gross-assets computation as of **18 Feb 2020** supporting SPA §2.3 ("aggregate gross assets do not
   exceed $1,000,000").
2. Written confirmation Helio has been a domestic **C** corporation continuously since formation (never an S corp).
3. Description of its business lines, for the "qualified trade or business" character.
4. The **complete** financing package: charter, bylaws, stockholders/investor agreement, and every ROFR, co-sale,
   drag-along or transfer-restriction provision.
5. Each annual **409A** report and its valuation date; confirmation whether $9.4M is still current.
6. The 2020 **§83(b) election** as filed, the FMV reported, whether the shares were subject to vesting or a repurchase
   right at grant, and whether any amount was included in her 2020 income; confirmation the paid-in amount is $12,000.
   *Effect on the numbers is small — the cap is $10,000,000 unless her basis exceeds $1,000,000 — but the record should
   be complete and the basis figure should not be guessed.*
7. **New, and now time-critical:** as soon as any term sheet, LOI, merger agreement or data room exists, send the
   **deal structure** (stock sale vs asset sale vs merger; consideration mix; any rollover equity, escrow, holdback or
   earnout; any requirement that holders contribute shares to an entity) **before signing**.

**R2 — From her CPA / the entity books (was Q3, Q5, Q10):**
1. Formation-to-date reconstruction of Oakline Properties' owner's capital account: contributions, **every**
   distribution, depreciation, losses, and unrecorded liabilities. The unexplained difference is **$1,760,000**
   (implied equity +$1,380,000 vs stated tax capital $(380,000)). Whether the $400,000 "Due from Services" is a real
   receivable or a distribution in substance. **Also ask which convention each book figure uses** — whether the
   building line is cost less accumulated depreciation, and whether the $(380,000) capital line is already net of
   depreciation and of the 2024 $1.2M distribution. That single answer decides which of the two outside-basis readings
   in `opinion.md` §6(b) ($3,280,000 vs $1,520,000 before the §752(b) shift) is the right one, and it may explain part
   of the gap.
2. How the three advances ($250,000 on 2024-03-01, $150,000 on 2025-06-15, $150,000 on 2025-09-01) were reported on
   the 2024 and 2025 returns, whether any were repaid or offset, and whether the Services→Digital $150,000 is on both
   sets of books or only in the email.
3. Digital's cumulative losses, her current basis/at-risk position, and the $1,120,000 of accumulated depreciation at
   Properties (needed if any building is ever sold).

**R3 — From the mortgage lender (was Q8):** the current loan agreement for the 2024 refinancing; whether it contains a
due-on-sale/change-of-control clause; whether transferring the Properties membership interest to a holding company
requires consent, and the lender's form of consent/estoppel.

**R4 — To a §1202 specialist (questions I cannot answer from the library):**
1. Does the per-issuer **$10,000,000 cap** apply per-issuer per-life, or per-sale/per-year? Do partial sales or
   tranches consume it separately?
2. Does a **donee** of gifted §1202 shares get a **separate** per-issuer cap (the §1202(h) tack is in the library; the
   separate-cap question is not)? Relevant only if the deal values her stake above **$10,012,000**, and only if a gift
   is made **well before** any LOI — a gift made during a negotiated sale is the classic step-transaction target.
3. Do the anticipated deal structures (stock sale, reverse merger, asset sale, rollover into an acquirer entity)
   preserve §1202 on the cashed-out and rolled portions?
4. Gain-recognition timing for escrow, holdback and earnout consideration.
5. Whether a transfer of her shares to her **own revocable trust** is a §1202 non-event (§1202(h) in the library does
   not address it).

**R5 — To estate/gift counsel:** the vehicle for the three Oakline LLC interests (her existing revocable trust vs a new
irrevocable vehicle), gift-tax and valuation consequences of any transfer of Holdings interests, and whether the estate
documents already pass the Helio shares at death without any pre-sale transfer.

**R6 — To her CPA for rates (was Q10):** her marginal federal rate and filing status and the Colorado rate, plus
**whether Colorado conforms to §1202**. Not quantifying Colorado state tax on a $9–10M gain is a real limitation of
this opinion; if Colorado does not conform, the state cost is six figures on any plausible rate.

---

## 4. Unknowns that cannot be established — handled as stated assumptions

| Unknown | How the opinion handles it |
|---|---|
| Whether Holdings will be a partnership for federal tax (trust as 1% member) | **[UNVERIFIED]** — both branches priced: §752(b) shift $19,000 vs $0; imputed interest $22,660 vs $0. Recommendation is to stop relying on the trust for partnership status (§8.2). |
| Which nonrecourse-liability allocation applies in a 99/1 partnership | **[UNVERIFIED]** — the library's 1% arithmetic is used; between 1% and 30% the current gain is $0 on both basis readings. |
| Oakline Properties outside basis | Stated as **two readings** (A $3,280,000 / B $1,520,000) because the sheet does not reconcile; nothing is forced to balance. The $19,000 contribution case is $0 gain on either reading; a 99% transfer would produce ~$380,000 of gain on reading B (§8.7). |
| Which AFR term and accrual method apply to undocumented demand loans; any §7872 exception | **[UNVERIFIED]** — mid-term 4.12% used; short-term and long-term totals ($21,780 / $25,190) shown for sensitivity. |
| Prior-year (2024–2025) §7872 reporting | Left **open**; remediation options in §5. Not fixed on assumed facts. |
| Tax rates (federal capital gain, NIIT, AMT, Colorado, Colorado conformity with §1202) | **[UNVERIFIED]** — every monetary tax figure is labelled illustrative. |
| "Qualified small business" / "qualified trade or business" definitions; the consequences of the 2020 §83(b) election recited in the SPA excerpt; at-risk and passive-loss limits; depreciation recapture; merger/asset-sale mechanics; installment-sale timing; gift and estate tax; Helio transfer restrictions | **[UNVERIFIED]** — outside the five library items; flagged where they bite and referred out in `agreements_required.md`. |
| Whether the businesses have nexus outside Colorado; whether Nadia is a Colorado resident | Nexus conclusion (Colorado filing regardless of Wyoming) is stated on the practice aid's stated assumption of a WY entity **managed from Colorado**; the assumption is prominent in §2, Step 1. |

**No further reply from the client is expected or required on the items in §3 and §4.** The client's only remaining
actions are to authorize R1–R3 (documents that exist at Helio, the CPA's office and the lender), answer **G1**, and route
R4–R6 to a §1202 specialist and estate counsel.
