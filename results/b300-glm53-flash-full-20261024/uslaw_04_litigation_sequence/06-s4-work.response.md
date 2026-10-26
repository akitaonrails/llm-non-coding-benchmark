Session 4 — the strategy memo. First, re-reading the engagement spec and the Session 1 baseline I'm asked to compare against, plus the current record state and sources, all in parallel:

Continuing Session 4. The first read batch was truncated in places — pulling the remaining source files in parallel: the rest of the engagement spec and Session 1 assessment, the full question log, the demand letter baseline, current status, prior advice files, and the verified contract text:

Good — I have the Session 1 baseline, the demand letter, current status, and the Session 3 memo. Now the Session 2 record and the opposing-counsel documents, in parallel:

The full record is in hand. Verifying there are no new documents delivered with this turn, and running the arithmetic verification for every figure the memo will state:

The script surfaced two issues: two of my own loop bugs (the J-4571 day-count shift and a mis-keyed first interest term), and — more importantly — a **real arithmetic error in the Session 1 assessment's $862,000 reconciliation**: the four-term check (`−410,000 − 32,000 + 13,361.74 + 16,000`) sums to −412,638.26, not the −428,638.26 claimed. The correct decomposition is three terms (the −$16,000 "residual" double-counts Rosa & Tay, whose 25%×$64,000×2 is exactly the $32,000 term). Before writing the memo, let me locate every instance of that flawed check, re-read the exact lines, and re-run the ledger with corrected code:

All figures now re-verified (Oct 25 standing basis reproduces exactly: $430,172.87 total, $276,417.47 conceded block, $73,755.40 J-4533R, $13,272.87 interest; the Session 1 reconciliation error is confirmed — the printed four-term check sums to −$412,638.26, while the correct three-term decomposition −410,000 − 32,000 + 13,361.74 = −$428,638.26 checks out; the top-line delta in Session 1 was always right, only the intermediate decomposition was wrong).

Fixing the Session 1 file first, and pulling the full current QUESTIONS.md and STATUS.md in parallel since they're next to be edited:

Session 1 record corrected. Two quick precision checks before drafting the memo — the exact text of Points 3–4 of Halvorsen's letter (quote bank) and the tail of Session 2's advice for the decoupling language:

Points 3–4 confirmed: the audit is *not* in their letter — Point 3 disputes J-4533 on "padded hours; notice given within 15 days" grounds (our audit-output unknown arose from our own reply requests). Point 4 is the Superior Court jab. Now writing the Session 4 strategy memo:

The Session 4 memo is on disk. Now finishing the two remaining housekeeping files — first reading `QUESTIONS.md` in full so the edits land precisely:

The file is exactly 40 lines as expected. Applying the three planned edits — header update first, with the full `STATUS.md` read in parallel since it's independent:

Header done. Now the Q10 closing note:

And the standing-unknowns list, extended to #7–#10:

Both files updated. Now the `STATUS.md` rewrite in the same pattern used when Session 3 closed — new top header, condensed history, full Session 4 entry, consolidated open items:

All three files are done. A quick check that the `QUESTIONS.md` edits landed cleanly:

Everything is on disk and consistent. Session 4 is closed out — `QUESTIONS.md` now closes Q9 (as #7) and the three Q10 items (as #8–#10) as standing unknowns per protocol, and `STATUS.md` carries the **Session 4 — COMPLETE WITH OPEN ITEMS** entry. Here is your summary:

---

## Session 4 — where you stand (memo: `deliverable/session4/strategy_memo.md`, Nov 6)

**The straight answer: your position is better where the money is real, and worse where the money was never collectible.**

### What got better
- **Their lawyer admits the four clean invoices in writing.** His letter says Pinecrest "will pay the undisputed balance of the remaining invoices" — he calls them "undisputed." That block is **$277,920.27 at our November 11 filing date — 64.3% of everything collectible at filing** (277,920.27 ÷ 432,081.97). On October 25 that money depended on our proof; now it rests on their own admission.
- **Our numbers are honest to the penny.** We found and credited our own $3,100 invoice double-entry before they could find it and use it against us.
- **The forum is settled.** Our contract requires arbitration — a private hearing, not a lawsuit in court. Both sides now say so. Going to court is off the table for good documented reasons, and nobody needs to win a fight about it.

### What got worse — told plainly
- **The claim is smaller: $430,172.87 vs. $433,361.74 at Session 1.** That's $3,188.87 of our own correction — the $3,100 credit plus $88.87 of interest on the piece we credited (2,144.27 − 2,055.40 = 88.87).
- **$862,000 is not happening.** Our best supportable number at filing is $432,081.97 — **$429,918.03 short** of that original target (862,000 − 432,081.97), and nothing that happened since October 25 narrows it. The lawsuit and the $410,000 line are gone as claims, permanently.
- **Filing now has real to-do items:** the signed original agreement hasn't been located (we would file from our typed copy, saying plainly that we assume it matches); the filing fee isn't priced yet; Mr. Bell's signed statement and the timesheet proof for the two double-entered shifts are still outstanding.
- **Their waiver argument on three of the five hires ($48,000) is now their written position** — no longer a risk we merely flagged from our own records. We must plan for that fight.
- We also found and fixed an arithmetic slip in our own Session 1 memo this week (a bookkeeping middle step; the bottom-line figure was always right). Nothing about your demand changed.

### The clock
- **November 9** — your call on the conversion-fee count. My recommendation: **keep it, with the $80,000 honestly labeled as an estimate.** The payroll data that could prove or kill that number only becomes available if the claim is actually on the table. If you'd rather carry zero risk on that piece, we can hold it in reserve for talks — your decision.
- **November 10** — the day we gave them to answer our five requests and pay.
- **November 11** — if they haven't paid the conceded block unconditionally, we file. Waiting costs them $112.30/day in our favor, but it gives them time to build their defense.

### Where the money can land at filing
| If | Then |
|---|---|
| Everything holds | $432,081.97 |
| They win the waiver argument on 3 hires | $384,081.97 (−$48,000) |
| They win on the whole June invoice | $357,920.27 (−$74,161.70) |
| Both go against us | $309,920.27 |
| **Floor — the conceded four, whatever else** | **$277,920.27** |

Fee awards are left out of every number — that clause cuts both ways and can't be priced from what's verified.

### What's still unknown (flagged in the memo, not re-asked)
The payroll behind the $64,000 average; what Mr. Bell said in that six-minute May call; what their records review of the June invoice produces; **the mystery of the "demand" they answered — still nothing in our file matches it, and if some paper matching it exists on your side, it contradicts our record and would surface in evidence — treat that as a live risk**; and the signed original agreement, which we'll work around with a plainly stated assumption.

**My path:** finish the filing to-do list this week; hold November 11 unless they pay, or a deal in the $277,920.27–$432,081.97 range appears; everything through me, one voice.

Housekeeping done this session: `deliverable/QUESTIONS.md` and `deliverable/STATUS.md` updated (Session 4 marked COMPLETE WITH OPEN ITEMS), and the Session 1 memo's reconciliation corrected in place with a dated note. When you're ready, the next session turns this into your settlement numbers and a one-page term sheet.