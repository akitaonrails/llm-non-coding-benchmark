# Proposed Form 8594 allocation — Buyer A asset sale (counter to Exhibit A)

**Seller:** Brightline Cabinetry LLC (S corporation, election effective 1/1/2023) · **Buyer:** Lone Star
· **Total consideration:** $3,100,000 (all cash; no liabilities assumed as drafted — see notes)

The allocation below keeps Exhibit A's **class placement** (which matches the class list in
`library/irc_1060_form_8594.md`: III = mark-to-market & receivables, IV = inventory, V = all other assets,
VI = §197 intangibles including covenants not to compete, VII = goodwill) and corrects the **amounts** to
values the deal file itself supports. Both parties must file Form 8594 and report the allocation
**consistently** (`library/irc_1060_form_8594.md`); once signed, the written allocation binds the parties
absent strong contrary economic proof (*Danielson*, per `library/irc_197_and_noncompete.md`) — which is
exactly why Exhibit A must be fixed **before** signature, not on the 8594 afterwards.

## Proposed allocation

| Class | Asset | Adj. basis | **Allocated** | Exhibit A | Δ |
|---|---|---:|---:|---:|---:|
| III | Accounts receivable (no reserve, CPA file) | 0 **[cash-method fallback, Q1]** | 200,000 | 200,000 | — |
| IV | Inventory | 140,000 (carrying, CPA file) | 140,000 | 150,000 | −10,000 |
| V | Equipment & vehicles (itemized below) | 240,000 | **650,000** | 900,000 | **−250,000** |
| VI | Covenant not to compete (5 yr) | 0 | **100,000** (target 0) | 400,000 | −300,000 |
| VII | Goodwill & going-concern (residual) | 0 (self-created) | **2,010,000** | 1,450,000 | +560,000 |
| | **Total** | | **3,100,000** | 3,100,000 | |

Class VII is the **residual** by design: the §1060 regs described in the library file allocate Classes I–VI
to their supported values and let goodwill absorb the remainder.

### Class V itemization (from `documents/fixed_asset_register.csv`)

| Asset | Cost | Accum. dep. | Adj. basis | FMV | Gain at FMV | §1245 ordinary |
|---|---:|---:|---:|---:|---:|---:|
| CNC router | 420,000 | 420,000 | 0 | 230,000 | 230,000 | 230,000 |
| Edgebander | 180,000 | 156,000 | 24,000 | 95,000 | 71,000 | 71,000 |
| Spray booth | 140,000 | 98,000 | 42,000 | 90,000 | 48,000 | 48,000 |
| Dust collection | 95,000 | 95,000 | 0 | 30,000 | 30,000 | 30,000 |
| Trucks (3) | 165,000 | 61,000 | 104,000 | 135,000 | 31,000 | 31,000 |
| Shop miscellaneous | 100,000 | 30,000 | 70,000 | 70,000 | 0 | 0 |
| **Total** | **1,100,000** | **860,000** | **240,000** | **650,000** | **410,000** | **410,000** |

Every asset's gain is below its own accumulated depreciation, so under §1245
(`library/irc_1245.md`) **the entire Class V gain is ordinary recapture at any allocation in this range** —
there is no capital-gain relief hiding in the equipment class. This is why the Class V number matters:
each extra dollar allocated above $650,000 buys the buyer a deduction the IRS can unwind under the FMV /
consistent-reporting logic of `library/irc_1060_form_8594.md`, and costs the seller 37 cents while the same
dollar in Class VII costs 20.

## Why Exhibit A's numbers fail on the deal file's own evidence

1. **Class V $900,000 vs. register FMV $650,000.** The $250,000 excess lands entirely in §1245 ordinary
   recapture (headroom: $860,000 accumulated depreciation covers even the drafted $660,000 gain). Seller
   cost of the excess: $250,000 × (37% − 20%) = **$42,500**, with zero offsetting §1374 change (equipment
   recognized BIG is capped at the $230,000 conversion appraisal figure either way).
2. **Class VI $400,000 vs. economic reality $0.** Buyer B's LOI obtained a **3-year covenant for no
   separate consideration**; the covenant here is a deal ancillary, and the library file
   (`library/irc_197_and_noncompete.md`) makes seller covenant payments ordinary income (Rev. Rul. 69-643;
   *Muskat*) and warns that the IRS may challenge allocations that ignore economic reality. Seller cost of
   the label: up to $400,000 × 17% = **$68,000**. If Lone Star values the covenant, they should raise the
   price — not relabel goodwill.
3. **Class IV $150,000 vs. carrying value $140,000.** Inventory gain is ordinary either way; the unsupported
   $10,000 premium is just 37-cent money.

Total tax cost of signing Exhibit A as drafted, vs. this counter: **$95,200**
(= $660,000 reallocated × 17 points); **$112,200** if Class VI goes to zero.

## Notes to attach to the 8594 schedule

- **Liabilities:** as drafted, Buyer A assumes only trade payables listed on a closing schedule — none is
  quantified in the file (**$0 modeled, open item Q2**). Any payables that surface at PSA are additional
  consideration, added to the allocation under the residual method (`library/irc_1060_form_8594.md`) and
  reported on Form 8594 — expect them to land in Class V/VII mechanics above.
- **Retained items:** the Hardaway dispute ($9,800) and warranty contingencies (unquantified) are **not**
  scheduled payables; they stay with the seller. They do not enter the 8594 allocation, but the PSA should
  say so expressly and exclude them from any post-closing indemnity.
- **§1374:** recognized built-in gain is per-asset capped at the 1/1/2023 appraisal (goodwill/trade name
  $900,000; equipment & vehicles $230,000; other $0) — recognized BIG $1,130,000 in both drafted and
  counter versions, entity tax $237,300 (`library/irc_1374.md`); attaching the appraisal protects the caps.
- **Receivables:** $200,000 face, no reserve; basis 0 under the cash-method fallback (Q1). If the CPA
  confirms accrual, Class III gain drops to $0 — allocation amount unchanged.
- **Consistent reporting:** provide this schedule to Lone Star's accountants with the counter and require
  mutual Form 8594 conformity language in the PSA.
