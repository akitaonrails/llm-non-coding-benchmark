# Compliance calendar — Natarajan Herrera Advisory

**Master assumption:** formation and first day of business **Monday, November 2, 2026**, calendar tax years. If formation shifts, every "30 days" and "2 months 15 days" date moves with it (recompute — do not reuse this sheet).
**Legend:** ✔ = date/rule from `library/` (citation given). ⚠ = date commonly used but **not in the library — verify before relying** (marked ASSUMED).

## A. 2026 — formation year

| Date | Item | Authority / status |
|---|---|---|
| **Nov 2, 2026** | File CA LLC registration (single entity; Delaware skipped — see recommendation §2.4). Effective date = tax-year start. | ⚠ CA filing mechanics/dates not in library; the *substance* (CA tax + fee apply to any LLC doing business in CA, incl. foreign-registered) is ✔ `ca_llc_franchise.md` |
| **Nov 2, 2026** | Operating agreement executed; Priya's tool contribution effective (capital $120,000); Tomás's $20,000 cash + **50% profits interest grant** effective; Tomás treated as partner from grant (Rev. Proc. 2001-43 condition). | ✔ `irc_721_and_revproc_93-27.md` |
| **Nov 2, 2026** | EIN; CA-required registrations; begin withholding analysis for any non-partner workers. | ⚠ not in library — ASSUMED as standard; verify |
| **Dec 2, 2026** | **Protective §83(b) election for Tomás's profits interest — due 30 days after grant. NO EXTENSION.** (`26 U.S.C. §83(b)`; Treas. Reg. §1.83-2). Copy to the company — the regulation is cited in the library, but the copy requirement itself is **not in the excerpt text** (⚠ verify the copy/proof mechanics with the IRS instructions). Retain proof of timely filing. | ✔ 30-day deadline and "no extension" per `irc_83b.md`; ⚠ copy-to-company detail — *the single most unforgiving date on this calendar* |
| **Dec 2026** | **Do NOT file Form 2553.** Tomás is an NRA (SPT 2026 = 161.0–163.0 < 183 at 118 projected / ≈120 confirmed US days) → §1361(b)(1)(C) makes any S election void; the entity is a partnership. | ✔ `irc_1361_excerpt.md`, `irc_7701b_substantial_presence.md` |
| (for reference only) **Jan 17, 2027** | If the company were ever *eligible* to elect S status for tax year 2026 (it is not), Form 2553 would be due 2 months 15 days after the beginning of that year (Nov 2, 2026 + 2 mo = Jan 2 + 15 d). Late relief (Rev. Proc. 2013-30) needs all shareholders eligible the whole period — impossible here. | ✔ `form_2553_deadline.md` |

## B. 2027 — first full year

| Date | Item | Authority / status |
|---|---|---|
| **Jan 15, 2027** | 2026 Q4 federal estimated tax (stub period: Nov 2–Dec 31 allocations) — each founder. First-year filers: compute from actual allocation dates. | ⚠ estimated-tax calendar not in library — ASSUMED dates |
| **Jan–Feb 2027** | Recompute Tomás's 2026 substantial presence with **actual** days (client-confirmed pattern "maybe a third of the year" ≈120; calendar projects 118; either way 161.0–163.0 < 183; ≥140 would make him a 2026 resident and change every filing). | ✔ rule `irc_7701b_substantial_presence.md`; days from client |
| **Mar 15, 2027** | Form 1065 (TY2026 partnership return) + K-1s (15th day of 3rd month — not stated in library; ⚠ ASSUMED). | ⚠ |
| **Apr 15, 2027** | Priya: Form 1040 (TY2026). Tomás: NRA return (1040-NR class of filings) — NRA filing rules **not in library**, verify; also verify whether any withholding applies to his allocations. | ⚠ |
| **Apr 15, Jun 15, Sep 15, 2027 / Jan 15, 2028** | 2027 federal estimated taxes (each founder; Tomás's installment basis depends on his NRA/resident status — verify annually). | ⚠ ASSUMED dates |
| **CA annual $800 tax + $2,500 gross-receipts fee** (revenue $610k in the $500k–$999,999 band) — **due date not stated in the library**; calendar it with the FTB (first-year proration rules also not in library). | ✔ amount ✔ existence; ⚠ date — `ca_llc_franchise.md` |
| **Nov 2, 2027** | Tomás's 1-year cliff: 25% of profits interest vests (per term sheet). Keep grant/vesting records; no §83 income expected because a true profits interest has no capital claim (Rev. Proc. 93-27) — re-verify the waterfall actually delivers $0 on a day-one FMV liquidation. | ✔ `irc_721_and_revproc_93-27.md` |
| **Dec 2027** | Tomás 2027 SPT recheck — **thin margin, do not skip.** If 2026 actual ≈120 days, he is a 2027 resident if 2027 US days ≥ **127** (127 + 120/3 + 96/6 = exactly 183; the test is "equals or exceeds"); if 2026 actual was 118, the threshold is **128** (183.33 at 128). His confirmed ≈120-day pattern gives 2027 weighted ≈176.0 — still NRA, but only ~7 days of slack. The **2028 threshold drops to ≈123 days** as high-day years enter the weighted lookback. If he becomes a resident, S election *becomes legally possible* for 2028: Form 2553 anytime during 2027, or by **Mar 16, 2028** (2 months 15 days after the Jan 1, 2028 tax-year start). Decision framework in recommendation §3.3 — recommended posture is to stay a partnership until net > ~$400k. | ✔ `irc_7701b_substantial_presence.md`, `form_2553_deadline.md`, `irc_1361_excerpt.md` |

## C. If Delaware is chosen anyway (not recommended)

| Date | Item | Authority |
|---|---|---|
| At formation + every year | Register as **foreign LLC** in California before/while doing business; CA pays the same $800 + fee. Failure = penalty + cannot maintain actions in CA courts. Delaware's own filings/taxes are **not in the library** — unquantified. | ✔ `ca_llc_franchise.md` |

## D. Standing/recurring items

- Annual: re-run Tomás's substantial presence test (and check §7701(b)(4) first-year-election possibility — mechanics unverified) before year-end planning. **On his confirmed ≈120-day pattern the 2027 residency threshold is 127 days (~7 days of margin) and 2028 is ≈123 days — this must be tracked day-by-day during the year, not discovered in April.**
- Annual: CA $800 + fee; federal estimates quarterly; K-1s to both founders (Tomás's file may need NRA-form package — verify). **Confirm the CA gross-receipts fee band each year:** Tomás now works mostly from Monterrey, so if CA-allocable receipts fall below $500k the fee drops to $900 (allocation rules not in library — verify with the FTB; see recommendation §4 sensitivity).
- Annual: Tomás's services are performed **mostly outside the US** (client-confirmed). Any withholding on his distributive share and his NRA return mechanics are **not in the library** — a cross-border specialist must set this up before the first K-1. Likewise, other-state registrations from clients all over the US are outside the library — check annually.
- Event-driven: §83(b)-type protective election within **30 days, no extension**, for any *new* restricted equity grant; spousal consent before any transfer (community property); buy-sell appraisal process on trigger events (term sheet).
- The business plan should track: distributions vs. retained cash (QBI follows the pass-through allocation, not the cash moved — **inference** from the §199A library's wages-vs-distributions contrast, not library text), and wages-if-ever (S corp scenario only).
