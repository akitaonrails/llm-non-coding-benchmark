# Note to Ray — the plain-English version

Ray —

You said "just tell me what bites me later." Here are the three things that cost you money **after** closing, worst first. Nothing below is a lawyer trick; it's arithmetic and contract text in the buyer's own draft.

## 1. Your installers — this is the one that bites (and buyer will make you pay for it twice)

You told me "everyone in the industry does it" and "they like it." Both are true and both are irrelevant. The legal test looks at who controls the work, not the 1099 form. Nine people working only for Brightline, in your trucks, with your tools, scheduled every day by your foreman, paid hourly for 3–4 years: **the law calls them employees no matter what the 1099s say** (that's the IRS finding structure with the control factors — see `library/worker_classification_tx_irs.md`, IRS Rev. Rul. 87-41).

What it costs (shown arithmetic; the flagged assumptions are in the redline):

- Employer payroll taxes on their pay: $612,000 (2025) × 7.65% = **$46,818/yr**; over their ~3.4-year average tenure ≈ **$159,181**. (The 7.65% employer-share figure is a common payroll number but is not stated in the reference library, so treat it as an unverified upper-bound assumption. The library does note that the reduced-rate regime under IRC §3509 applies only where the failure is *not* willful — see `library/worker_classification_tx_irs.md`.)
- Overtime on straight-hourly pay when they're at 45–50 hours: at a $37.50/hr midpoint wage, add ~$18.75 for every hour over 40. Your busy season alone: 9 installers × 10 OT hrs/wk × ~$18.75 × 12 weeks = **$20,250/yr** (busy-season length not in your records — my assumption). Buyer's diligence model will assume more, up to ~**$149,175** total if it assumes 45 hours all year.
- **Bracket: $228,000–$308,000** — which is 7–10% of your price and nearly your whole $310,000 escrow.

And here's the part that actually costs extra: **you signed a "clean" rep** (§4.12) saying everyone is properly classified and all taxes were paid. That isn't true. Buyer's §7.4(c) says they can collect even on things they knew about — before or after signing. Put together, you have promised to insure Lone Star for a problem they knew was in the room. My fix (in the redline): disclose the installers up front and replace the blank check with a **capped special indemnity of $275,000**. That's what it costs to stop the bleeding; uncapped, the clause as written reaches the entire price.

## 2. The earn-out — as written, it's worth about zero. Don't price it into your "sell number"

Buyer agreed to pay you 40% of EBITDA above $700,000, capped at $400,000. Sounds good. Watch the math:

| | Amount |
|---|---|
| Earn full earn-out requires EBITDA of | 700,000 + 400,000 ÷ 0.40 = **$1,700,000** (2.3× your 2025 figure) |
| Your 2025 EBITDA per your own numbers | $740,000 — but that counts your $180k salary and $42k "one-time" legal **as add-backs** |
| Same business without those add-backs | 740 − 180 − 42 = **$518,000** |
| If buyer pays a manager ~$180k to run it | 518 − 180 = **$338,000** |
| Either way vs. the $700,000 gate | **below the gate → you get $0** |
| Even in best case (your numbers unchanged) | 0.40 × (740 − 700k) = **$16,000** |

The killer isn't the gate — it's the words: EBITDA "**determined by Buyer** in good faith under **Buyer's accounting policies**, consistently applied." Buyer writes both the score and the rules; provisions like that are the textbook mechanism buyers use to pay effectively nothing post-closing (`library/earnout_definitions.md`). My redline fixes the definition, adds audit rights and acceleration if they flip the business. **Until it's fixed, treat the earn-out as worth $0 when you're deciding whether the $3.1M cash offer is enough.**

## 3. Hensley Homes — your biggest customer can say "no," and you haven't asked yet

Hensley is 38% of your revenue — about $1.75M/year. Their contract says you **cannot transfer it without their written consent**, they can refuse **for any reason or no reason** ("sole discretion" — that's in the data room, §1.1), and a transfer made anyway is void. You told me he's a friend, he doesn't know yet, and he "won't love a corporate buyer." Right now the plan per buyer's schedule is "no consents needed" — which is false.

Two things to do: (1) **tell him yourself, before you sign anything** — this is the classic moment where a friend finds out from a letterhead instead of from you; and (2) tell him the shop keeps running as it always has, which is the pitch for the consent letter. If he says no or wants something for it, better to know **before** you're bound to close. My redline makes his consent a closing condition so you're not trapped.

Two smaller ones while I have you: the **spray-booth permit** doesn't transfer — the city makes the buyer reapply, 30–60 days — so the real closing date is 30–60 days after signing, not two weeks. And the **non-compete** as drafted is 7 years within 500 miles — you'd sign it, you're retiring, but I've cut it to 3 years / 75 miles because courts dislike overbroad ones and a bloated one invites tax scrutiny if they shove purchase price into it (see `library/tx_noncompete_sale_of_business.md`).

## The three, in one line each

1. **Installers:** disclosed + capped at $275k — otherwise you've promised buyer up to $3.1M back on a ~$228k–$308k problem.
2. **Earn-out:** worth ~$0 as written; fix it or delete it from your side of the negotiation.
3. **Hensley:** get his consent **before signing** — with a condition in the contract so you can walk away if he says no.

I've sent Whitaker the corrections, the WARN answer (your 23-person headcount including installers is far under the 100 threshold — no notices needed, `library/warn_act.md`), and the redline.

## You asked: "can we just sign?"

Short answer: **not as drafted — yes, within days, once four cheap things are done.** Two are already finished and on my desk. One is a phone call only you can make. One is a decision only you can make.

1. **The Hensley call (yours — before you sign anything).** You haven't told him yet. He's 38% of revenue — about $1.75M/yr — and his contract dies if the deal happens without his written consent: a transfer made anyway is void, so the single biggest thing you're selling can be treated as never delivered. Make the call first. My redline makes his consent a closing condition, so a "no" costs you nothing but the deal.
2. **The schedules (mine — done).** Whitaker's draft says the wrong things are true: Schedule 3.3 "None," nothing discloses the installers. The Schedule 3.3 counter and the new Schedule 4.12 (nine installers) are written and go in as-is. Half a day of paper.
3. **The $275,000 cap (one page).** This is the whole difference:
   - **Sign as drafted** → the known installer problem (~$228k–$308k on the assumptions flagged in §1 above) is **uncapped up to the whole price: $3,100,000**. The escrow covers the first $310,000; as much as the rest comes back out of your pocket ($3.1M − $310k = up to **$2,790,000**).
   - **Sign with the cap** → worst case **$275,000**, inside your escrow, and Buyer keeps every one of its "market" rights on everything else.
   One warning: if Whitaker says "fine, disclose them and we're done," **that's not enough**. His no-claims-barred clause covers knowledge "at any time, whether before or after" execution — disclosure alone doesn't stop a claim under it. The fine print has to route scheduled matters to the capped indemnity instead. Disclosure only protects you if the fine print says so (`library/sandbagging.md`).
4. **The earn-out decision (yours — make it consciously).** As written it's worth about $0; even the single best case is 0.40 × ($740,000 − $700,000) = **$16,000** (math in §2 above). You can sign with it unrevised **only if you're treating it as zero** when you check whether the $3.1M cash is enough. If it isn't, hold for my §2.4 fix — already drafted.

Whitaker's two lines, in plain English:

- **"That clause is market, every deal has it."** There are two kinds of that clause, and both sides pick between them deal by deal — the reference material treats it as a live choice, not a universal rule (`library/sandbagging.md`, citing the ABA Deal Points Study). His version even reaches further than the aggressive form: it covers things Buyer learns **after signing**, at any time. Either way, I've offered him the easy exit — keep his clause for everything else; only the one known problem gets capped.
- **"§4.12 is a plain-vanilla rep — if your contractors are fine, what's the concern?"** They aren't fine, and his own data room says so: Brightline trucks, Brightline tools, your foreman's daily schedule, hourly pay, 3–4 years. The legal test calls that employees no matter what the 1099s say (`library/worker_classification_tx_irs.md`). Vanilla practice for a known issue is exactly what I'm asking for: put it on the schedule and price it.

And the calendar: the permit sets the real closing date — 30–60 days after signing — no matter how fast anyone signs.

**Bottom line: sign when (1) Hensley has heard it from you, (2) the schedules are in, (3) the installer problem is capped at $275k, and (4) you've decided the earn-out with your eyes open.** That's the version I'll tell you is safe. Sign without 1 or 3 and you're back in the blank-check version above.
