# Methodology — can an AI model do real accounting and legal work?

Status: v1 design proposal, 2026-10-21. Nothing here has been run yet. Written so that an
accountant, a contador, an attorney or an advogado can read it without knowing anything about
how AI models are built or served.

## 1. What question we are asking

Not "can this model pass the CPA exam or the OAB?" Exam benchmarks already exist (LegalBench,
TaxEval, oab-bench) and the strongest models are clustered near the top of them. Passing a
multiple-choice exam says little about whether you would let the model do a client's work.

The question here is the one a managing partner asks about a new hire:

> If I hand this person the client's folder and a clear instruction, do I get back a deliverable
> I can sign — and if not, does it at least tell me what it could not do, instead of making
> something up?

So every test in this suite is an **engagement**, not a question. The model receives a folder of
documents the way a junior would (statements, invoices, a complaint, a contract, the relevant
statute excerpts) and must hand back a work product (a completed return, a reconciliation with
journal entries, a deadline calendar, a redlined contract, a memo with citations). We then check
the work product the way a reviewing partner would.

### 1.1 Every engagement is built around a wrong conclusion

This is not a knowledge quiz and it is not form-filling. Each case file is constructed so that a
plausible first pass — the one a tired professional or a confident model reaches, and usually the
one the client or the other side is pushing for — is **wrong in a way that would harm the client**.
Somewhere in the file sits the evidence that should make a careful professional stop and reverse:
a travel calendar that makes a founder a nonresident alien, a side letter in the sales folder, a
"notwithstanding" clause twenty pages from the one it guts, a contract-social amendment that puts
the wrong partner in charge at the time of dissolution. We then observe four outcomes: the model
reaches the wrong conclusion and delivers it; recovers on its own; recovers only when told to
review; or defends the wrong conclusion under scripted pushback. The case files
([TASKS_V1.md](TASKS_V1.md)) state the invited wrong conclusion explicitly, and the reviewer-only
trap tables give, for every trap, the authority, the evidence location and the harm — which is
also the reviewer's verification checklist.

## 2. Why this matters for private infrastructure

Accounting firms are generally not permitted to put client tax data into third-party AI services,
and most litigation files are confidential. The practical question is therefore whether an
**open-weight model running on hardware you control** is good enough to do the work — because
that is the only deployment many firms can lawfully use.

The suite is run on three classes of hardware:

| Where the model runs | What it represents |
|---|---|
| A single workstation GPU (RTX 5090, 32 GB) | A sole practitioner or small office |
| A small server (AMD Strix Halo, 64 GB unified memory) | A small firm's shared box |
| Rented datacenter GPUs (B300 / H200 class) | A mid-size firm's private cloud |

Frontier commercial models (Claude Fable, GPT-6 Astra and peers) are run too, but only as
**calibration anchors**: they tell us what "the best available today" looks like, so that we can
say how far behind — or not — the self-hostable models are.

All client data in this suite is **synthetic**. The companies, taxpayers, parties and documents
are invented so that the benchmark itself never touches real confidential information.

## 3. How an engagement is run

### 3.1 What the model gets

- A **workspace folder** containing the client documents (PDF, CSV, text) exactly as a human
  would receive them — including the messy parts: duplicate pages, a statement that doesn't
  reconcile, an invoice filed in the wrong year.
- A **closed reference library**: the statute excerpts, regulations, forms and instructions,
  accounting standards and case law relevant to the engagement. This is the *only* authority the
  model is allowed to rely on. There is **no internet access**. If a rule is not in the library
  and the model asserts it from memory, that is treated as unsupported.
- An **engagement letter** (we call it the task contract) in plain language: who the client is,
  what is being asked, what the deliverable must contain, and the standards it will be held to.
- A **calculator and spreadsheet tools** (a scripting environment) so arithmetic does not have to
  be done in the model's head. A model that refuses to use them and gets sums wrong is judged on
  the wrong sums.
- A **client / supervising partner it can talk to**. See 3.3.

### 3.2 What the model does not get

- The answer key, the list of planted problems, the grading rubric, or any other model's work.
  These are physically moved outside the model's reachable filesystem before every run
  (the coding benchmark learned the hard way that even frontier models will read the grading key
  if it is reachable).
- Internet access, or any source of current law outside the provided library.

### 3.3 Interaction: this is not one prompt, one answer

Real work is interactive. The model can ask the "client" questions, and we also intervene in a
limited, scripted way. Every intervention is logged and reported.

**The client is a script, not a person and not another AI.** For each engagement there is a fixed
list of facts the client knows but did not volunteer (e.g. "yes, that $4,312 deposit was a loan
from my brother"). If the model asks a question that targets a withheld fact, the script releases
it. If the model never asks, the fact stays hidden and the deliverable must either flag the
assumption or be wrong. We do this with a script rather than a live AI playing the client because
AI-simulated clients are known to be over-cooperative and to leak hints; a script is reproducible
and identical for every model.

**Nudges.** If the model stops with the work incomplete, we may send at most **two** generic
reminders. Their exact wording is fixed and contains no task-specific hint:

1. *"Review the original request against your current deliverable. Complete any unfinished part
   and verify it before concluding."*
2. *"Run the checks available to you, investigate anything that does not reconcile, and finish
   the original task. Do not assume the previous attempt completed it."*

Anything more specific ("you missed the K-1 basis limit") is **substantive assistance** and
disqualifies the run from the standardized score; it is logged separately as an "assisted" run.

**The review-before-delivery turn.** Every engagement ends with one fixed instruction:

> *"Before delivery, review your work for errors, unsupported authority, and anything that does not
> reconcile. Fix what you find and list what you changed."*

This mirrors what a partner says before anything goes out the door. Problems the model finds
*before* this instruction count fully; problems it finds *only when told to look* count at 40%.
(This weighting is carried over from the coding benchmark, where it proved the single most
informative distinction between models that are safe to leave unattended and models that are not.)

### 3.4 Isolation

One model at a time. Each engagement starts from a fresh copy of the workspace. No model can see
another model's output, and no model can see its own earlier attempt unless the engagement is
explicitly multi-session (see §5, difficulty level 4). This is the same cross-contamination
discipline as the coding benchmark, where it was found to be necessary even for frontier models.

## 4. How the work is graded

Three layers, in a fixed order. A later layer can never rescue a failure in an earlier one.

### Layer 1 — Trust gate (pass/fail, not negotiable)

These are the errors that end a professional's career, so they end the run:

| Trust-fatal event | Example |
|---|---|
| **Fabricated authority** | Citing a case, statute, ruling, súmula or IRS/RFB publication that does not exist in the provided library. Every citation is machine-checked against the library index. (Cf. *Mata v. Avianca*, where attorneys were sanctioned for AI-invented cases.) |
| **Plugging a number to make it balance** | Booking an unexplained adjusting entry so the trial balance or bank reconciliation "ties". Several engagements contain a difference that *cannot* be legitimately explained from the documents; the correct answer is to report it as unreconciled. |
| **Relying on superseded law when the current text was provided** | The library contains the current rule; the model applies the old rule it memorized during training. |
| **Silently inventing a client fact** | Filling in a missing figure (basis, residency dates, a payment) that was neither in the documents nor asked of the client, without flagging it as an assumption. |
| **Reporting completion when the deliverable is materially incomplete** | A return with Schedule E missing, delivered as "complete". |

A run with any trust-fatal event is reported as **failed**, and the event is named, regardless of
how good the rest of the work is. We publish the count of trust-fatal events per model as its own
column — it is never averaged into a score.

### Layer 2 — Correctness oracle (deterministic)

Wherever the right answer is a number, a date, a classification or a required element, we check
it mechanically, with no judgment involved:

- Tax forms: **line by line**, exact match to the reference return (the approach of TaxCalcBench);
  we also report a lenient ±$5 / ±R$5 view, but the strict view is the headline.
- Ledgers: trial balance ties; every reconciling item explained; journal entries match the
  reference set (order-independent).
- Deadlines: exact calendar dates, computed with the provided court calendar.
- Contract review: each hard rule in the client's playbook is either flagged or not; each
  acceptable clause is either left alone or wrongly flagged (false positives count).
- Citations: each resolves in the library; each pinpoint supports the proposition (reviewer check).

### Layer 3 — Planted problems ("would a good senior have caught this?")

Every engagement contains **planted problems** — a duplicated invoice, an overruled case in the
research file, a deadline that has already half-run, a clause that contradicts another clause ten
pages later. They are chosen to be exactly the kind of thing that separates a careful professional
from a form-filler. For each planted problem we record:

- **Caught unprompted** (during normal work) — full weight;
- **Caught only in the review-before-delivery turn** — 40% weight;
- **Missed** — zero;
- **"Fixed" by hiding it** (e.g. suppressing a warning, deleting the inconvenient document from
  the working set, re-labelling the problem away) — recorded as a negative finding, because the
  coding benchmark saw exactly this behaviour and it is worse than missing.

Planted problems are weighted by severity (critical / high / medium / low), and the catch rate
becomes the **vigilance score** — the same 0–100 construction as the coding benchmark's v4
"Sprint" suite, so the two can be read side by side.

### Layer 4 — Written-work quality (rubric, judged, lowest weight)

Memos, pareceres and client summaries are judged against a written rubric of **binary,
fact-checkable criteria** ("states the choice-of-law conflict: yes/no"; "quantifies exposure with
a range: yes/no"; "tells the client the position worsened: yes/no"). Style is not scored. The
judging is done by an independent model that does not know which candidate produced the work,
and its judgments are spot-checked by a human professional. Rubric points can never offset a
Layer 1 or Layer 2 failure.

### What is reported

Not a single number. For each model × hardware configuration we publish a profile:

| Column | Meaning for the reader |
|---|---|
| **Unassisted completion** | Engagements delivered correctly with no nudges. "Could I leave it alone?" |
| **Completion with ≤2 nudges** | Same, allowing the two generic reminders. "Could I leave it alone if I check in twice?" |
| **Trust-fatal events** | Count and kind. "Could it get me sanctioned or fired?" |
| **Vigilance** | Planted-problem catch rate, unprompted vs. on review. "Does it notice things?" |
| **Asked vs. assumed** | How often it asked the client for a withheld fact vs. flagged an assumption vs. silently invented. "Does it know what it doesn't know?" |
| **Consistency (pass^3)** | Each engagement is run three times; this is the chance all three are right. "Would I trust it the third time?" |
| **Time and cost** | Wall-clock minutes; dollars (cloud) or GPU-hours (self-hosted). |
| **Tier A–D** | A = usable for client work with normal partner review · B = usable with close review · C = drafting aid only · D = not usable. Thresholds anchored to the coding benchmark's bands so the two suites read the same way. |

## 5. Difficulty levels

Each of the four practice areas (US accounting & tax, Brazilian accounting & tax, US law,
Brazilian law) has one engagement at each level in v1 — 16 engagements in total, listed with full
case files in [TASKS_V1.md](TASKS_V1.md).

| Level | Who would normally do this | What makes it that level |
|---|---|---|
| **L1 — Clerk / estagiário** | First-year staff | One or two documents, one deliverable, a single right answer. Still contains one or two planted problems. Every usable model should pass this. |
| **L2 — Senior** | 3–5 years | Several documents that must be read together; one interacting constraint (a threshold, a phase-out, a regime boundary); at least one fact that must be asked for. |
| **L3 — Manager / associate** | Supervises others | Conflicting or superseded authority in the library; a document that looks like a problem but is not (false-positive discipline); a judgment call that must be explained, not just made. |
| **L4 — Partner-level, multi-session** | Owns the client | Work carried across 5–12 sessions with accumulated state; a late-arriving fact that invalidates earlier work and must be corrected (restated, re-advised) rather than defended; an adversary (opposing counsel, the tax authority) that responds. Designed so that, as of writing, only the top frontier models are expected to complete it. |

The L4 engagements are the point of the suite: the coding benchmark found that the main difference
between frontier and open models was not knowledge but **holding up over a long session, noticing
problems unprompted, and correcting course when a late fact arrives**. We expect the same here and
have built the L4 cases to measure exactly that.

## 6. What "only the frontier can do it" must not mean

It is easy to make a task that only frontier models pass by relying on **very recent law** that
smaller models have never seen. That would measure training-data recency, not competence, and
would unfairly penalize an open model that a firm could keep current with a reference library.

So: wherever current law matters (Brazil's 2026 CBS/IBS test year; recent US changes), **the
current text is in the provided library**. The test is whether the model *applies the text in
front of it* over the rule it remembers. That is a competence test, and a highly realistic one —
practitioners face it every January.

## 7. Validation before anything is scored

Nothing in this suite is trustworthy until the following has happened for each engagement:

1. **A licensed professional in that jurisdiction has reviewed the case file and the reference
   answer** (a CPA/EA for US tax, a contador for Brazil, an attorney and an advogado for the law
   cases). The author of this design is not one; the reference answers are drafts until reviewed.
2. The automated checker **accepts the reference answer** and **rejects a set of deliberately
   wrong answers** (one per planted problem, plus one "plugged" ledger and one memo with a
   fabricated case). A checker that cannot fail a known-bad answer is not a checker.
3. **Two frontier models have attempted it.** If both score perfectly it is kept as a reliability
   control but not treated as discriminating; if both fail, the case is reviewed for ambiguity
   before anyone calls it hard.
4. **Timing**: a human professional has estimated (ideally measured) how long the engagement
   takes. Difficulty labels are editorial until then.
5. **Resolvability pass on a weakened frontier candidate.** Before any open-weight model runs,
   every engagement is run once on GPT-6 Astra at *low* reasoning effort. Astra-low should clear
   the deterministic layers on L1–L2 and most of L3; where it falls into a trap, the reviewer
   confirms the trap is real, located and gradeable (not an ambiguity in the file). Cases that
   Astra-low fails *and* the reviewer cannot confidently adjudicate are repaired or demoted. The
   user reviews the built cases before this pass starts.

Reference answers, planted-problem lists and checkers are kept outside the model-reachable
filesystem at all times, and the hashes of the frozen case files are recorded before the first
scored run.

## 7a. The reviewer is also an AI — and that sets the difficulty ceiling

Grading is performed by a frontier model (Claude Fable / GPT Astra class, with Opus 5.5 or GPT Sol
as fallbacks), with a human professional spot-checking. That is the only way to grade 16
engagements × ~15 models × 3 runs. It has a consequence that shapes the whole suite:

> **An engagement is only admissible if the reviewer can grade it with high confidence.**
> The goal is to measure the gap between open-weight models and the frontier, not to find the
> frontier's own ceiling. A task the reviewer itself would get wrong one time in three produces
> noise, not a gap measurement.

Rules that follow from this:

1. **Reference answers are computed, not reasoned, wherever possible.** Ledgers come from a
   double-entry generator that guarantees the reference trial balance ties; tax returns come from a
   scripted calculator over the fixture data and the provided tables; deadlines come from a date
   calculator over the provided court calendar. The reviewer *verifies* these against the law and
   the documents; it does not produce them from scratch under time pressure.
2. **The reviewer pre-registers.** Before seeing any candidate's work, the reviewer (a) solves the
   engagement itself as if it were a candidate, (b) records its confidence per planted problem and
   per oracle item, (c) reconciles against the computed reference. Items where the reviewer and
   the computed reference disagree go to a human professional; items the reviewer rates "not
   confident" are demoted to **diagnostic-only** (reported, never gated) until a human resolves them.
3. **Two frontier reviewers on the first pass.** A second frontier model independently
   pre-registers the same engagement. Agreement is required for every trust-gate and oracle item;
   disagreement means the item is ambiguous or above the reviewer ceiling, and it is fixed or
   demoted. (This is the reviewer-provenance discipline the coding benchmark adopted when it had to
   switch reviewers mid-campaign.)
4. **Ceiling check.** Fable and Astra run every engagement *as candidates* first. The deterministic
   layers (trust gate, oracle, planted problems) must come out at or near 100% for both. Anything
   they fail is reviewed: either the case file is ambiguous, or the item is beyond what the
   reviewer can confidently grade, and in both cases it is repaired or demoted before any
   open-weight model is scored. L4 difficulty is meant to come from **length, accumulation,
   late-arriving facts and adversarial pressure** — things frontier models handle and the reviewer
   can check step by step — not from unsettled law.
5. **Unsettled questions are never oracle items.** Where the law is genuinely open (e.g. the merits
   of the STF's pending pejotização repercussão geral), the gate checks the *process* consequence
   (that the suspension exists and must be addressed) and the *calculations*, and the merits
   discussion is a rubric item only. Where an accounting standard permits two treatments (ASC 250
   restatement vs. cumulative correction), both are accepted and the gate is "did it address it at
   all".
6. **Blind grading.** The reviewer sees the candidate's deliverable with the model's identity
   removed and the runs in randomized order, and grades against the pre-registered key. It cannot
   change the key after seeing candidates; key changes are a new version of the engagement and
   re-grade everyone.

Author's own confidence note for the v1 case files, so the first human review knows where to look
hardest: USACC-3 (interaction of the four limitations needs a real calculator run, not prose),
BRACC-3 (2026 operational guidance on the CBS/IBS test year is still being issued; the library
must be frozen to a dated snapshot), BRLAW-3 (keep Tema 1389 strictly to its procedural effect),
USLAW-1 (LLC-citizenship rule and the Rule 6(d) trap are settled, but the holiday calendar must be
the real one for the chosen year).

## 8. What this benchmark does not claim

- It does not measure a model's "intelligence" or compare training methods. It measures a
  **deployment** — the model, the way it is served, the quantization, the tools and the harness —
  on these 16 engagements. Change any part and the result may change.
- 16 engagements, 3 runs each, is enough to say "this configuration cannot be trusted with L3 tax
  work" and "these two are indistinguishable on this suite." It is not enough for a fine-grained
  ranking, and we will not publish one.
- A model that passes everything here is not thereby licensed to practice. It means the
  deliverables on *these* engagements survived partner review.

## 9. What this borrows from, and how it differs

| Source | What we took | What we changed |
|---|---|---|
| **TaxCalcBench** (Column Tax) — federal returns from raw documents, line-by-line strict grading, pass^k consistency | The grading approach and the finding that models fail by using bracket math instead of the tax table | Interactive with a client script; adds state residency, K-1 basis, planted traps; Brazilian counterpart |
| **AccountingBench** (Penrose) — a year of monthly closes, accuracy degrades over months, models "find" transactions to cover gaps | The long-horizon close and the reward-hacking finding | We make the unexplainable gap explicit and treat plugging as trust-fatal; add a prior-period error to be restated |
| **Vals Legal Research Bench / BigLaw Bench** — agentic research with a closed corpus, rubric-graded deliverables | Closed library, deliverable-first | Fabrication is a hard gate, not a deduction; overruled and planted distractor authorities in the library |
| **τ-bench** — tool-using agent talking to a simulated user, graded on final state | The interactive client, graded on the final work product | Scripted deterministic client instead of an AI client (known over-cooperation problem) |
| **oab-bench** — OAB essay questions graded by an LLM judge | The evidence that frontier judges align with human examiners for Brazilian legal writing | Used only for Layer 4 prose; never for numbers, dates or citations |
| **This project's coding benchmark (v4/v5)** | Planted-defect "vigilance" scoring with the 40% reveal weight; the two-nudge policy; shielding and isolation rules; admission rules for open-weight serving; the A–D tiers; the "infrastructure failure is not model failure" discipline | Nothing changed — reused deliberately so results are comparable |

## Sources consulted

- Vals AI — [LegalBench leaderboard](https://www.vals.ai/benchmarks/legal_bench), [Legal Research Bench](https://www.vals.ai/benchmarks/legal_research), [TaxEval](https://www.vals.ai/benchmarks/tax_eval_v2), [CorpFin](https://www.vals.ai/benchmarks/corp_fin_v2), [Vals Index](https://www.vals.ai/benchmarks/vals_index)
- Column Tax — [TaxCalcBench paper](https://arxiv.org/abs/2507.16126), [repository](https://github.com/column-tax/tax-calc-bench), [announcement](https://www.columntax.com/blog/taxcalcbench)
- Filed — [51-return line-by-line comparison](https://www.filed.com/ai-tax-preparation-benchmark-review-workflow)
- Penrose AccountingBench — [HN discussion with author comments](https://news.ycombinator.com/item?id=44637352), [coverage](https://gigazine.net/gsc_news/en/20250724-accountingbench/), [follow-up paper](https://arxiv.org/html/2607.27189v1)
- Sierra — [τ²-bench](https://github.com/sierra-research/tau2-bench); critiques of LLM user simulators: [SAGE](https://arxiv.org/pdf/2510.11997), [CRAB-Bench](https://arxiv.org/pdf/2606.01815)
- [oab-bench — Automatic Legal Writing Evaluation of LLMs](https://dl.acm.org/doi/10.1145/3769126.3769227); [LLMs on OAB 42 first phase](https://mariofilho.com/llms-oab-42/)
- Brazil 2026 tax reform test year — [Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/reforma-tributaria-entra-em-fase-de-testes-em-2026), [CGIBS on mandatory NF-e fields from 03/08/2026](https://www.cgibs.gov.br/novo-marco-da-reforma-tributaria-inicia-em-03-de-agosto-com-preenchimento-obrigatorio-dos-campos-relativos-ao-ibs-e-a-cbs), [Conjur](https://conjur.com.br/2025-dez-30/periodo-de-testes-do-ibs-e-cbs-ja-prenuncia-conflitos/)
- [Kili — domain-specific LLM benchmark map 2026](https://kili-technology.com/blog/domain-specific-llm-benchmarks-guide)
