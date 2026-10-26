Now the library files:

Code Mode is JS, not Python — I'll run the calculations through the shell instead:

Audit is clean — the only "BAD" hits are the audit regex catching my cross-references to the other deliverable files (`memo.md`, `form_8594_counter.md`), not legal citations. Every legal authority cited is in `library/INDEX.md`.

## Engagement complete

**Deliverables** (in `deliverable/`): `comparison.json`, `memo.md`, `form_8594_counter.md`, `QUESTIONS.md`, `STATUS.md` (status: **COMPLETE WITH OPEN ITEMS**).

**Headline result — Ray is wrong, and the "smaller" offer wins:**

| | Buyer A as drafted | Buyer A w/ counter allocation | Buyer B (Hensley) | Ray's guess |
|---|---:|---:|---:|---:|
| Ordinary income | $1,070,000 | $420,000 | $0 | — |
| Capital gain | $1,450,000 | $2,100,000 | $2,430,000 | — |
| Entity §1374 tax | $237,300 | $237,300 | $0 | — |
| **Net after tax** | **$2,176,800** | **$2,287,300** | **$2,364,000** | ~$2,480,000 |

Key findings:
- **Asset sales are not "all capital gains."** Lone Star's "standard" Exhibit A allocates $900,000 to equipment whose basis is $240,000 with $860,000 depreciation — all $660,000 of gain is ordinary §1245 recapture, and the $400,000 non-compete allocation is ordinary too (Rev. Rul. 69-643, *Muskat*). Ray's estimate overstates Deal A by ~$303,200.
- **§1374 built-in gains bite**: the S election became effective 1/1/2023, so the 5-year recognition period runs through 12/31/2027 — any 2026 asset sale triggers 21% × $1,130,000 recognized BIG = **$237,300 entity-level tax**. A stock sale triggers none.
- **The drafted allocation violates §1060's FMV cap** ($900k vs the register's $650k equipment FMV) and, once signed, binds Ray via Form 8594 consistency and *Danielson*. My counter (Class V $650,000 / Class VI $0 / Class VII $2,100,000) saves **$110,500** and costs Lone Star nothing (VI and VII are both 15-year §197 intangibles to them).
- **Buyer B's $2.85M nets ~$187,200 more than Buyer A as drafted** — all capital gain, full §453 installment deferral (~$13,400 PV benefit), plus $90,000 of note interest (+$56,700 after tax), plus a clean liability break (A leaves all unknown liabilities in Ray's shell; B caps exposure at a $285,000 indemnity / $100,000 escrow).
- **Negotiating levers**: don't sign Friday; reprice equipment above FMV at ~$17 per $100 shifted; refuse any §338(h)(10)/§336(e) election without ~$237,300+ compensation; the only version of Deal A that beats B is counter-allocated **with closing deferred past 12/31/2027** (≈ $2,524,600); secure Hensley's unsecured note.

`QUESTIONS.md` lists six non-blocking confirmations (equipment FMV support, stock-basis adjustments, consulting arrangement, undisclosed liabilities, 2028 closing feasibility, election requests). Unverified-in-library points (ordinary character of inventory gain, zero goodwill basis, S-corp character flow-through) are explicitly flagged as such per the working rules.