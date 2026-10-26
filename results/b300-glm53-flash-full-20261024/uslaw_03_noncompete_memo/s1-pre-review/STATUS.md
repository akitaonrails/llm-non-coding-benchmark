# STATUS — Engagement: Meridian Robotics / Wei-Lin Zhao

**Date:** October 26, 2026 (updated after the client Q&A response and a follow-up client inquiry, both received same day)
**Deliverables directory:** `workspace/deliverable/`

---

## 1. Deliverables checklist

| Deliverable | Status | Location |
|---|---|---|
| Lawyer's memo (Question Presented, Brief Answer with probability bands, Facts, Analysis, Strongest Arguments, Recommendation) | **Complete — updated with Addendum Part VII (client Q&A record + remaining unknowns)** | `deliverable/memo.md` |
| Citations file — one entry per authority actually relied on | **Complete** (unchanged by the Q&A; no new authorities) | `deliverable/citations.json` |
| Questions to client on open facts | **Complete — converted to Q&A record**: answers logged; remaining unknowns flagged; no question repeated; nothing outstanding for the client | `deliverable/QUESTIONS.md` |
| Status tracker (this file) | **Complete** | `deliverable/STATUS.md` |

## 2. Citation integrity check (per engagement terms)

- `citations.json` contains **exactly 20 entries**; every entry maps to a row in `library/INDEX.md` (`library_file` verified programmatically against the index; zero mismatches).
- Every entry carries the authority's checked status, verbatim from `INDEX.md`: 16 **in force**; 2 **superseded** (*Campbell*, *General Commercial Packaging* — see *Edwards*, 2008); 1 **vacated** (FTC Rule 16 C.F.R. Pt 910 — see *Ryan LLC*); 1 **modified** (*Light v. Centel* — see *Sheshunoff*, 2006) — and the memo expressly instructs that *Light* **must not be cited** for the old timing rule.
- **No authority outside `INDEX.md` is cited in the memo.** Unverifiable propositions — Restatement §188 as the §187(2)(b) comparator, §17200 remedies via §16600.1(c), the "continuing duty" reading of §16600.1(b), trade-secret/confidentiality enforcement doctrine, litigation-duration/laches assumptions, and the firm memo bank's internal cases (*Calderon v. Pacific Dynamics*, *Westbrook Systems*) — are labeled **[unverified]** in the memo and are **not cited**. The memo-bank memos are used as background context only.
- All date and probability arithmetic was computed with Python and is copied into the memo with the arithmetic shown (Parts III.11 and IV.G).

## 3. Key conclusions (memo.md) — unchanged by the client's answers

1. **Do not file in Travis County.** Probability a Travis County action actually keeps Zhao off the Kestrel work: **0–10%** (strictly computed: 0.5–9.3%). The client's answers **strengthen** this conclusion: the Company's sole objection is "the competing itself," and there is no evidence of any Zhao misconduct that could add leverage.
2. **§14 (forum/choice of law) is voidable at Zhao's election under Cal. Lab. Code §925** (~80–90%) — now **company-wide confirmed**: standard form, same-day signature, nobody negotiates, so the §925(e) carve-out is unavailable for any California engineer.
3. **Even without §925, a Texas tribunal likely applies California law** under Restatement §187(2)(b) as adopted by both supreme courts (*DeSantis* on the Texas side; *Nedlloyd*/*Application Group* on the California side): ~55–70%. Net P(Texas law governs the merits): ~20–44% (no band change; Assumption A stands unconfirmed — see §5 below).
4. **Under California law, §8 is void**: §16600(a)/(b)(1) voids any employment noncompete "no matter how narrowly tailored"; *Edwards* forecloses narrow-restraint arguments; Ixchel's rule of reason is B2B only; §16600.5(a)–(b) reaches contracts signed outside California.
5. **Under Texas law** (the low-probability path, ~25–40% as written / ~50–70% as reformed under §15.51(c)): *Sheshunoff*/*Marsh* support ancillarity if confidential information/equity was actually supplied (**still undocumented** — see §5), **but** §15.51(c) gives no pre-reformation damages, §15.52 makes remedies exclusive, and any Texas injunction likely gets **non-recognition in California** (library's Texas jurisdictional practice note).
6. **Filing is itself the exposure**: §16600.5(b) bars attempting to enforce a void contract regardless of where signed; §16600.5(d) makes the attempt a civil violation; §16600.5(e) gives Zhao injunctive relief, actual damages, and prevailing-employee attorney's fees. Zhao's resignation email shows his side has already framed this theory with counsel.
7. **AB 1076 / §16600.1 as to Zhao:** the notice duty **never attached** (offer 2024-02-28 is 14 days after the 2024-02-14 deadline; signing 19 days after). The company-wide gap is now **client-confirmed**: no notices were ever sent; the LO-233 ticket was closed as "won't do" — a recorded decision, which heightens company-wide §16600.5(e) injunctive exposure and remediation urgency (not quantified).
8. **Recommended course (memo Part VI):** no lawsuit; no written demand invoking §8/§9; a narrowly drafted confidentiality reminder (his own email says he will honor §10, and the Company has no evidence to the contrary); preserve records as they stand (no edits/deletion of access records or LO-233); company-wide form remediation and §16600.1/.5 compliance inventory.

## 4. Client Q&A received (October 26, 2026) — log and effect

Per instruction, answered questions were not repeated; the effect of each answer is recorded in memo Addendum Part VII and in `QUESTIONS.md` §1:

1. **Standard form / nobody negotiates** (standing assumption): §925(e) carve-out unavailable company-wide; §15 acknowledgment conclusively boilerplate; §16600.5(c) class grows with every new California hire.
2. **No AB 1076 notices ever sent; LO-233 closed "won't do"**: gap confirmed as a recorded non-compliance decision; no change as to Zhao (duty never attached); exposure aggravator for the covered class; handling note recorded — analysis kept in privileged work product, records preserved as-is, remediation is the durable response.
3. **No evidence Zhao took anything; his stated objection is the competition itself**: no misuse predicate; trade-secret lane has no present facts; recommendation confirmed and strengthened; no band changes.
4. **Client inquiry — the 2024 outside-counsel memo (*Calderon*/*Westbrook*) and the vacated FTC rule (answered same day)**: no change to any conclusion. The memo-bank cases are outside the closed library, cannot be cited or verified, and *Westbrook*'s panel holding is unstable (en banc granted per the firm's 2025 memo, position held "pending further guidance"); the FTC rule is agreed vacated (*Ryan LLC* — status "vacated") but the memo never relied on it; the operative constraints are §§925 / 16600 / 16600.5, all in force. Full reply logged in `QUESTIONS.md` §1.

## 5. Remaining unknowns (client has no further information — flagged explicitly, not assumed away)

Full list with sources and materiality in memo Addendum Part VII.4 and `QUESTIONS.md` §2:

1. **Assumption A** — Meridian's state of incorporation / principal place of business (risk is one-directional: only downward on P(Texas law)).
2. Confidential information actually furnished to Zhao; access/export records (ancillarity and the confidentiality lane).
3. Zhao's equity compensation (*Marsh* consideration path).
4. Full agreement text — fee clause (Assumption B), §§1–7, 11–13, any arbitration mechanism, complete §8/§14.
5. Zhao's actual duties at Kestrel (§8 scope presumed from Kestrel's business line and his email, not verified).
6. Zhao's counsel identity / standing correspondence (known only from the resignation email; no demand letter received to date).
7. LO-233 covered-population count and ticket history (needed for Part V.5 remediation scoping).

## 6. Open items

- **Nothing is outstanding for the client.** All remaining unknowns depend on records the Company could not produce, Zhao-side information, or possible future compelled disclosure. Counsel updates the memo if any listed record surfaces, without re-asking answered questions.
- **Exposure quantification:** §16600.5(e) damages/fee exposure still cannot be computed from the file (no fee rates, no damages theory, no Zhao-side materials); deliberately not invented.
- **Analysis lanes outside the library** (would require an expanded authority list before any reliance): Restatement §188 defaults; California trade-secret/confidentiality enforcement; §17200 remedies; availability/wisdom of a §16600.1 "curative" notice for post-deadline hires ("continuing duty" reading).
- **Record-preservation advisory issued (memo Part VII.2):** the Company should not edit, re-characterize, or delete the LO-233 ticket or access records; remediation advice is separate and pending the client's remediation decision.
- **After Zhao's start date (2026-10-13):** §8's 24-month window would, if it ran, extend to 2028-09-30 (718 days remaining at his Kestrel start); §9's 12-month window to 2027-09-30. No action recommended within these windows consistent with the memo's recommendation.

## 7. Engagement status

Client instruction: continue the engagement; do not repeat answered questions. All four deliverables are complete and current as of this update. The engagement is at the posture the memo recommends — no filing, no demand, monitor for Zhao-side correspondence, remediation decision pending with the Company (which holds the records to scope it).
