# Compliance Calendar — Natarajan Herrera Advisory

**Prepared:** October 25, 2026. "T" = target formation date. Proposed T = **Monday, November 2, 2026** (first business day after today), so tasks are also expressible relative to T. If formation already occurred (see `QUESTIONS.md`), every date keyed to T moves backward to that date. **Note:** the client did not answer on this (Q1 unanswered, October 25, 2026) — the premise that no 2026 activity preceded formation is an unconfirmed assumption; see `STATUS.md` open item 1.

Citations in brackets. Entries marked **[mechanics not in library]** use conventional dates that the closed library does not state; they are provisional and must be confirmed before reliance.

---

## 1. What we will NOT be doing (negative instructions)

| Item | Why not | Authority |
|---|---|---|
| Form 2553 S election for 2026 | Impossible: Tomás is a nonresident alien shareholder (161 < 183 substantial-presence days), and §1361(b)(1)(C) forbids an NRA shareholder; the election would be void (`irc_1361_excerpt.md`, `irc_7701b_substantial_presence.md`) | library |
| Any 83(b) on Priya's tool | She contributes property for her interest — §83 concerns transfers for services, not property purchases (`irc_83b.md`) | library |
| Delaware-only formation without California registration | Requirement to register as a foreign LLC + same $800/fee (`ca_llc_franchise.md`) | library |

## 2. Absolute deadlines (library-stated)

| Deadline | Date | Action | Authority |
|---|---|---|---|
| **Profits-interest grant date** | **T = 2026-11-02** | Admit Tomás; the 30-day §83(b) clock starts on **the date of the transfer of the interest**, not on formation | `irc_83b.md`; `irc_721_and_revproc_93-27.md` |
| **Protective §83(b) election** | **≤ T + 30 days = 2026-12-02 (hard, no extension)** | File the protective election for Tomás's unvested profits interest per Rev. Proc. 2001-43 (`irc_83b.md`: "not later than 30 days", no extension) | `irc_83b.md`; `irc_721_and_revproc_93-27.md` |
| Form 2553 window (if ever used) | n/a 2026 | If the practice grows Tomás's US days so he later meets substantial presence and the firm elects S: file any time during the year preceding the effective tax year, or no more than 2 months + 15 days after the tax year begins; late relief requires reasonable cause and shareholder eligibility all along | `form_2553_deadline.md` |
| Reasonable-compensation discipline | n/a (partnership — rule doesn't bite) | If/when an S corp ever exists, market-level salaries are a precondition to any distribution policy | `reasonable_compensation.md` |

## 3. Formation and first 90 days

| Date | Action | Authority / note |
|---|---|---|
| 2026-11-02 (T) | File formation with the **California Secretary of State** (recommended; see `recommendation.md` §3). If the founders insist on Delaware, form there and **register as a foreign LLC in California before transacting business**; same $800 + fee; failure bars maintaining an action in CA courts and incurs penalties | `ca_llc_franchise.md` |
| 2026-11-02 (T) | Execute **operating agreement** (see `term_sheet.md`): capital accounts, 50/50 profit allocation, 3-yr/1-yr-cliff vesting of Tomás's profits interest, repurchase at $0 for unvested units, buy-sell triggers, deadlock protocol, drag/tag, spousal consents | `llc_buy_sell_checklist.md` |
| 2026-11-02 (T) | Tomás: purchases $20,000 capital interest with cash **and** receives 50% profits interest (services); Priya: contributes PriceLab tool (appraised **$120,000**; basis **$31,000**, client-confirmed per her CPA on 2026-10-25: ~$89,000 expensed on Schedule C 2023–2025) under §721 | `irc_721_and_revproc_93-27.md`; `tool_appraisal.pdf` |
| 2026-11-02 through 2026-12-02 | **Tomás spousal consent** (married; community-property Mexico; **no prenup**, client-confirmed): written consent + election for treatment of his units — required BEFORE/AAT grant | `llc_buy_sell_checklist.md` |
| By 2026-12-02 | **83(b) protective election filed and proof of timely filed delivery retained** | `irc_83b.md` |
| Within 90 days of T (≈ 2027-01-31) | EIN, bank account, books that track capital accounts and vesting; engagement letters for client relationships moved into the firm [mechanics not in library — administrative] | — |
| Before 2026-12-31 | Determine whether the partnership owes **partner-level withholding on Tomás's effectively-connected income for 2026** (short period); quantify and **fund by the 2026 due date**. **[Not in library: §1446 amounts/dates unverified — open item; no withholding vendor identified (Q4 unanswered)]** | — |
| 2026-12-31 | **Priya taxable-income watch**: year-1 taxable ≈ $93,612 → SSTB limit doesn't apply (under ~$200,300 single). Model says her 20% QBI deduction survives year 2 (~$133,727). Restart planning if her taxable income approaches ~$275,300 | `irc_199a_sstb.md` |

## 4. Tax-year 2026 (ending during formation year) and 2027 payments

| Date | Action | Authority / note |
|---|---|---|
| 2027-02-15 | CA **$800 annual LLC tax** — treated here as first-year payment for a 2026-forming LLC. **[Due-date mechanics not in library]** | `ca_llc_franchise.md` |
| 2027-04-15 | CA **gross-receipts fee** for the 2026 short tax year: revenue $610,000 → **$2,500** (fee paid with the California partnership return; CA return due-date mechanics not in library) | `ca_llc_franchise.md` |
| 2027-04-15 | Federal **Form 1065** + Schedule K-1s for the 2026 short tax year **[due-date mechanics not in library]**; show Priya's carryover basis ($31,000 + contribution events) explicitly | — |
| 2027-04-15 | 2026 **estimated-tax catch-up** for both founders (model: Priya ≈ $48,091 total incl. SE tax; Tomás flagged — NRA mechanics differ) **[estimated-payment dates not in library]** | `year1_comparison.json` |
| 2027-06-15, 2027-09-15, 2028-01-15 | 2027 quarterly estimates, sizes computed off year-2 projections (each ≈ $183,350 share + $25,907 SE tax; see model) **[dates not in library]** | `projections.csv` |
| 2027 and annually | CA $800 + gross-receipts fee; year-2 revenue $820,000 stays in the $500k–$999,999 bracket → $2,500 | `ca_llc_franchise.md`; `projections.csv` |

## 5. Recurring / standing obligations

- **Vesting administration:** monthly; record each 12/24/36-month vesting increment (0/33/66/100%) in the minutes; lapse-forfeiture mechanics per `llc_buy_sell_checklist.md`.
- **Every capital event, transfer or distribution:** reconfirm Priya's tool basis ($31,000) and the $89,000 built-in gain sits properly with her allocation — the split she took is embedded in her capital account; do not let later 50/50 profit allocations silently absorb it (allocation rules for contributed built-in gain not in library — open item 3 in `STATUS.md`).
- **Spousal status of Tomás:** re-confirm community-property treatment any time his units move (death, divorce, transfer) per `llc_buy_sell_checklist.md`.
- **Each Jan 1:** re-run the substantial-presence tally from Tomás's travel log: 2027 count = 2027 days + ⅓ × 118 + ⅙ × 96; he remains disqualified from S shares until the formula clears 183 (`irc_7701b_substantial_presence.md`). If it ever clears, an S conversion (not a same-entity election of a partnership) is a different plan — evaluate before assuming.
- **Each tax-year end:** if the firm considers an S election "any time during the preceding year" window remains available only with all-shareholder eligibility for the whole period (`form_2553_deadline.md`).
