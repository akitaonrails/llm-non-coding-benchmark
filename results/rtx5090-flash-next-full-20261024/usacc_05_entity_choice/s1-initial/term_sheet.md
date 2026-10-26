# Term sheet — Operating Agreement, Natarajan Herrera Advisory LLC

California LLC (see recommendation.md for why). Terms keyed to the practitioner checklist at `library/llc_buy_sell_checklist.md` [citation: ABA Business Law Section, paraphrased] and the tax mechanics in `irc_721_and_revproc_93-27.md`, `irc_83b.md`, `irc_1361_excerpt.md`. Commercial terms are proposals for the founders to negotiate; nothing here is boilerplate they should sign without review.

## 1. Capital structure and contributions

| Member | Contribution | Capital account | Interest |
|---|---|---|---|
| Priya | PriceLab tool — appraised FMV **$120,000** (Coastline Valuation, Jan 15 2026), tax basis $31,000 | $120,000 | 50% capital + 50% profits, **fully vested** |
| Tomás | **$20,000** cash | $20,000 | $20,000 capital + **50% profits interest**, vested per §2 |

- **Distribution waterfall (mandatory drafting):** first, return positive capital accounts ($120,000 Priya / $20,000 Tomás); then split residual **50/50**. This implements the Rev. Proc. 93-27 §4.01 profits-interest safe harbor — on an immediate FMV liquidation at grant, Tomás receives only his $20,000, so his profits interest is worth $0 at grant and is not taxable compensation. A capital interest for services would be taxable at receipt or vesting; the agreement must not grant one.
- Year-1 profits allocated 50/50 (Tomás treated as a partner from grant per Rev. Proc. 2001-43); **protective §83(b) election filed by Dec 2, 2026** (30 days, no extension — Treas. Reg. §1.83-2).
- Capital accounts maintained on the books; additional contributions only by unanimous consent, non-dilutive absent agreement (drafting choice — state it expressly).
- Priya assigns PriceLab IP to the LLC at formation (warranty: sole owner; note $89,000 of costs she deducted → the LLC's basis in the tool is low; on a future asset sale, ~$89,000+ of gain is built in — no step-up from the contribution).

## 2. Vesting (Tomás)

- **3-year schedule, 1-year cliff:** 0% until Nov 2, 2027; **25%** at the cliff; then **1/36th per month** through Nov 1, 2030. (Calendar dates per the assumed Nov 2, 2026 formation.)
- **Unvested profits-interest units are repurchased at cost ($0 for the profits interest; his $20,000 cash capital is returned)** on any Departure (see §3) — per checklist: "vesting of founder units with repurchase at cost for unvested units."
- Acceleration: single-trigger on Death/Disability → 50% of unvested vests (or double-trigger on sale of the company → 100%) — negotiating point.
- Priya has no vesting (property contribution).

## 3. Buy-sell triggers (checklist: death, disability, divorce, bankruptcy, voluntary departure, for-cause removal)

Any of: **Death; Disability (12+ months unable to work); Divorce** (spouse claims or acquires any interest — critical: client-confirmed Tomás is **married in Mexico with no prenuptial agreement**, so the default community-property regime presumptively reaches his LLC interest); **Bankruptcy/insolvency; Voluntary departure (ceasing full-time work); Removal for Cause** (fraud, felony, material breach; member vote).

On a trigger:
- **Unvested units:** repurchased **at cost** (above).
- **Vested units:** company/other-member **option to purchase** at:
  - **Price:** formula — the checklist's "formula or appraisal": propose the **lower of (a) 1.0× trailing-12-month net income × the departing member's profit share, or (b) appraised FMV**, with a **25% discount** if Departure is voluntary-without-cause or Cause (checklist "discounts"); appraisal by a neutral valuation firm otherwise.
  - **Payment:** 20% down, balance over **36 monthly installments** with interest, secured by a pledge of the purchased interest — cash flow of a consulting firm cannot absorb a lump sum (checklist: "payment terms").
  - If not exercised within 90 days, the departing member may sell to the company at formula price; no outside sales without first offering (ROFR, §5).
- Death: insurance cross-purchase recommended if affordable (buy-sell funding; checklist-contemplated; not in library — flag only).

## 4. Deadlock (50/50 — mandatory)

Per checklist ("mediation → buy-sell shotgun"):
1. **Good-faith negotiation** (15 days) → **mediation** (30 days, single mediator, costs split).
2. Still deadlocked on a **Major Decision** (budget, hiring/firing key staff, distributions beyond tax withholding, sale >$50k, new members, loans, strategy): **shotgun buy-sell** — either member may serve a named price per 1% interest; the recipient must, within 30 days, either sell all its interest at that price or buy the server's at it. Drafting notes: minimum 60-day funding window; no shotgun during the first 18 months; shotgun suspended while a Death/Disability/Cause repurchase is pending.
3. Day-to-day management is **not** a Major Decision; each member runs their own function.

## 5. Transfer restrictions and spousal consent (checklist)

- **No transfers** without consent of the other member (consent not unreasonably withheld for estate-planning vehicles the member wholly controls, provided the transferee signs a joinder).
- **Spousal consent:** each spouse (or community-property claimant) signs consenting to the agreement's transfer and buy-sell terms and waiving member rights. Client has confirmed Tomás married **in Mexico with no prenuptial agreement**, so his spouse's joinder is a **mandatory condition of his admission**, not a negotiable extra. The consent itself has not yet been obtained — it is an open item (§8). Foreign-law effect is **outside the library** — have Mexican local counsel paper both the joinder and any marital-property arrangement the couple chooses.
- Any transfer that would make an **ineligible holder for a future S election** (e.g., another nonresident alien, per §1361(b)(1)(C)) can be refused outright — protects optionality if Tomás later becomes a US resident and the owners elect S status.
- **No one other than Priya and Tomás may be a member without unanimous consent**; economic-only interests otherwise (no voting).

## 6. Drag-along / tag-along (checklist)

- **Tag-along:** if one member sells >50% to a third party, the other may join pro rata at the same terms.
- **Drag-along:** with unanimous consent to the sale itself first (protects a 50/50 owner from being dragged at a price they reject — conservative for two founders), all members must convey; permitted only if the buyer takes the firm as a whole (no asset-stripping of one founder's book of business).
- Non-compete/non-solicit tied to *sale* of the member's interest and to Cause departures (24 months, the clients/market actually served) — enforceability not addressed by the library; flag for review.

## 7. Governance and money mechanics

- Two-member manager-managed LLC: each member is a manager; Major Decisions unanimous; annual budget adopted by Dec 31 each year.
- **Mandatory tax distributions** of at least the estimated tax on each member's allocation (QBI is driven by *allocations*, not distributions — `irc_199a_sstb.md`); discretionary distributions only after the CA $800 + gross-receipts fee and reserves are funded (`ca_llc_franchise.md`).
- Books, fiscal year = calendar; members' right to inspect; annual valuation update memo feeding the §3 formula.
- No W-2 wages to members (partnership); if the S-election scenario ever activates (Tomás US resident + net > ~$400k), this term sheet is amended with reasonable-compensation policy per `reasonable_compensation.md` (*Watson*), and §5's ineligible-holder clause becomes a hard covenant.

## 8. Open points (client has said it has **no additional information** — do not re-ask; resolve with specialists, see QUESTIONS.md)

- **Spousal joinder not yet signed**; its form and enforceability under Mexican law need Mexican counsel (marriage in Mexico, no prenup — confirmed).
- **Client-contract assignment restrictions: unknown.** The founders have no information on whether their existing client agreements bar assigning relationships to the LLC. Until obtained, §1's IP-assignment warranty and any client novations are conditional; a contract review is a pre-closing condition.
- **Cross-border drafting points:** Tomás performs services mostly from Monterrey — non-compete/non-solicit scope, place-of-performance covenants, and any withholding on his allocations need a cross-border specialist (not in library).
- **Other-state exposure:** clients are all over the US; whether other states require registration/tax is outside the library — SALT check before first out-of-state engagement letters.
- Insurance availability/affordability for the §3 death cross-purchase (checklist-contemplated; not in library).
