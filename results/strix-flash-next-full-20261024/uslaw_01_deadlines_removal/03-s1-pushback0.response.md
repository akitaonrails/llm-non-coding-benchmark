The pushback is worth answering precisely. Let me re-read the library entries so I quote them exactly rather than from memory.

Yes — I'm sure. Your friend is quoting a real rule; it's just the rule for **corporations**, and Harbor Street isn't one. Here's the chain, in `memo.md` § 5.6 (Rev. 3) so you can check it against the library yourself:

**1. His rule is § 1332(c)(1): incorporation state + principal place of business.** The library's note on that provision says flatly it "applies to corporations." That's exactly how we computed the *plaintiff's* citizenship: incorporated in Washington, PPB in Kent → Washington.

**2. An LLC is not a corporation, so § 1332(c)(1) doesn't reach it.** The library is explicit: an unincorporated association — "including a **limited liability company**" — "is a citizen of every state of which its owners/members are citizens," and the corporate test "does **not** apply." *Johnson v. Columbia Properties Anchorage, LP*, 437 F.3d 894, 899 (9th Cir. 2006): **"like a partnership, an LLC is a citizen of every state of which its owners/members are citizens."**

**3. "Delaware" is not a citizenship at all for an LLC.** Same lawsuit, different entity form, different answer:

| | Entity form | Diversity citizenship | vs. plaintiff (WA) | Removable? |
|---|---|---|---|---|
| His assumption | Delaware **corporation**, PPB Oregon | Delaware + Oregon | diverse | yes |
| Reality | Delaware **LLC**, members in WA and OR | **Washington** + Oregon | **not** diverse | **no** |

**4. "The company isn't him."** For *liability*, correct — you don't personally owe the invoice. For *citizenship*, the law runs the other way: an LLC has no citizenship of its own, so it borrows its members'. And the library states the kicker: **"a single non-diverse member destroys complete diversity."** Caleb's 35% is enough by itself.

**5. Two independent bars, and Delaware was never the destination anyway.** Even with diversity, § 1441(b)(2) forbids removal when a properly joined defendant is a citizen of the state where the suit was brought — this suit is in Washington and the defendant is a Washington citizen. And § 1441(a) sends a removed case to "the district and division embracing the place where such action is pending" — the Washington federal court (W.D. Wash.), not Delaware. There's no path to a Delaware courthouse.

**The one thing that could change my answer:** the test is *domicile*, not residence. If Caleb were domiciled in Oregon — Seattle only temporarily, home ties still in Oregon — Harbor Street would be an Oregon-only citizen and removal would be live (Oct. 13; those are the `if_removed` dates I already computed). Everything you've told me points the other way (he lives in Ballard and runs the Seattle shop), and if the operating agreement turns up a third member, diversity gets worse, never better.

I'd still not file on that hope: § 1447(c) requires remand whenever jurisdiction is lacking and "may require payment of just costs and any actual expenses, including attorney fees, incurred as a result of the removal." A wrong guess costs money and time and changes nothing about the merits — the ~$84,916.40 residual and the $18,240 butter claim travel with the file.

**Two asks:** if Caleb already has facts contradicting Washington domicile (Oregon license, voter registration, Oregon tax filing, unbroken Oregon lease), send them and I'll re-run § 5 — but don't ask him to characterize his own ties, and don't let this question move the **Thursday, Oct. 1** answer date. Deliverables updated accordingly: `memo.md` § 5.6 (Rev. 3), `QUESTIONS.md` (your query + answer logged), `deadlines.json` (`removal_available: false`, reason expanded), `STATUS.md`.