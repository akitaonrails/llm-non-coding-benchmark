Lena's relay is important in two ways — it's a legal question to answer, and it's itself a recordable fact (Hale is renewing the same directive through HR on the same day). Let me update the JSON with the renewed-push fact, then add the rebuttal section to the advice memo:

My oldString had a typo. Retrying with the exact text:

Now adding Lena's three questions with answers to the advice memo, right before the "later action" section:

Now updating `STATUS.md` to reflect the addendum, then re-validating everything:

That's a false positive — the advice memo's header references `INDEX.md` itself (the allowed set). Re-running with the index excluded, as in the earlier audit:

All validated. Here's the direct answer to Lena:

## Straight answers to Tom's arguments

**1. "She's at-will and we have a PIP, so we're covered." — Neither works.**
- **At-will** answers "do we need cause to fire someone generally?" — yes, and nobody disputes that. It does *not* mean the reason can be an unlawful one. The library is explicit: at-will status does not permit termination for discrimination, retaliation, or exercise of statutory rights `[library/columbia_at_will_exceptions.md]`. At-will is not a shield against a retaliation claim; it's irrelevant to one.
- **The PIP doesn't cover you — it incriminates.** It's her *first discipline of any kind in 7.5 years*, authored by the accused **4 days after her complaint**, only 20 of 60 days old (it wasn't and can't yet be "failed" — it ends 2026-11-15), and its "100% of quarterly quota" standard can't even be measured against a completed quarter inside its window. Peers at 79–86% have no PIP. The PIP is Exhibit A for pretext, not protection.

**2. "He wants it done before she goes on leave." — That schedule *is* the violation.** Terminating to prevent a requested leave is interference; her request alone triggered the protection — she never needs to have started the leave `[library/fmla_2615.md]`. Hale's 10-02 email says this in writing, and this conversation shows the intent renewed *after* being advised to pause. Complying with that schedule hands her a case with the company's own words attached, plus **double damages** on lost wages.

**3. "If we wait, aren't we stuck with her forever?" — No. Here's the calendar:**

| Step | When |
|---|---|
| FMLA answered in writing, on the merits, without Hale's sign-off | Now (it's already overdue) |
| Investigation of the 9/12 complaint, run independently | Starts this week; prompt = days-to-weeks |
| PIP runs its full 60 days | Ends **2026-11-15** (40 days remain) |
| Q4 completes, giving the PIP standard a completed quarter | 12-31 (flagged assumption) |
| If the merits still support discipline, with an independent decision-maker, comparator-consistent standard | After 11-15 |

That's weeks, not "forever" — and it's the **shortest lawful path**, not stalling. If she's genuinely underperforming, the clean process proves it. The rushed one converts even a real performance problem into retaliation with direct evidence.

**4. "Can we at least do it right after her leave?" — No. Same claim, dates moved.** Using "the taking of FMLA leave as a negative factor" is prohibited `[library/fmla_2615.md]`, and proximity in either direction carries causation `[library/title_vii_704a.md]`. A termination landing right after her return — to the accused's PIP, with untouched peers and no investigation on file — is retaliation on its face. What makes a *future* termination defensible isn't the timing; it's everything around it: independent decision-maker, completed investigation, FMLA resolved, PIP genuinely run, the same standard applied to the 79–86% peers, and a gap from the protected activity.

**One caution for HR directly:** Hale is the accused in the pending complaint — his "we're covered" assessment can't be the company's risk posture. Don't adopt or repeat it. And note the date, participants, and content of this exchange: it's within the preservation scope too `[library/litigation_hold.md]`.

**Files updated:** the renewed "before she's out on leave" push is now recorded in `risk_assessment.json` (claim 2); `advice_to_hr.md` gained a "Tom's three arguments, answered" section with the calendar table; `STATUS.md` reflects the follow-up Q&A. JSON re-validated, schema intact, citations checked — all within `library/INDEX.md`.