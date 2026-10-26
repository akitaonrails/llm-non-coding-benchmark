I have the contract, client file, and library. The two PDFs aren't readable by my model, but `pdftotext` is available locally, so I extracted them above. Now let me do the arithmetic.

Calculations reconcile with the client file. Now writing the Session 1 deliverables.

Session 1 deliverables are written and internally tied out. Note on method: my model can't ingest PDFs, so I extracted the two court orders with local `pdftotext` — both are in `documents/`, no outside sources used.

## Bottom line to the CFO (all three asks refused, with authority)

| Ask | Answer | Why |
|---|---|---|
| Pay Mesa's Feb invoice $62,400 from the DIP draw | **No** | Dkt. 48 Schedule 1 lists **only Apex** ("No other vendor is included"); Dkt. 61 ¶2 limits DIP proceeds to post-petition opex/admin/Carve-Out, "nothing herein authorizes payment of any pre-petition claim except as separately ordered"; paying it is an avoidable post-petition transfer, 11 U.S.C. §549(a). Its cap headroom is only **$3,800** ($35,000 − Apex's $31,200), so Mesa can't fit even on an amended order. |
| Net it against the returned-coil credit | **No** | Dkt. 61 ¶3: "No setoff, recoupment or netting of DIP proceeds against pre-petition obligations is permitted." |
| "We'll tell counsel after" | No cure | MOR Part 7 asks "were any payments made on pre-petition debt? (with docket reference)" and the form is signed under penalty of perjury — there would be no docket reference to give. |
| Holland & Pierce $140,000 | **Not in March** | §§330(a)/331: paid only on application and court award; payments outside those procedures are subject to disgorgement. Nothing was granted as of 3/31 — the interim comp order entered **4/14**, after the period. Same for Corbin's $45,000. |

What does keep the steel moving: pay Mesa's **post-petition** invoice ($18,900, unpaid at 3/31) under §§503(b)(1)/363(c)(1), and move to add Mesa to Dkt. 48 with notice and a hearing. Economics also cut against the CFO: plan treatment is 35% → **$21,840** vs. **$62,400** now, a $40,560 premium.

## Numbers (arithmetic in `march_mor_workpaper.md`)

- Receipts **$2,262,400** = collections 1,212,400 + DIP draws 1,050,000 (600k 3/12, 450k 3/26)
- Disbursements **$490,770** = payroll 412,000 + post-petition vendors 19,570 (2,120+9,800+7,650 ✓ ties to file) + Apex pre-petition 31,200 (Dkt. 48) + utilities deposit 28,000 (Dkt. 31)
- Part 2: post-petition payables **$207,826.16** (Mesa 18,900 + H&P 140,000 + Corbin 45,000 + UST accrual 3,926.16 = 0.8% × 490,770); pre-petition LSTC **$74,110** (105,310 pre-petition vendor invoices − Apex 31,200 paid)
- Part 5: **$0 / $0 / $0** for March; Part 7: **yes** on pre-petition debt (Apex 3/24 Dkt. 48; pre-petition wages Dkt. 9), **no** unapproved outside-ordinary-course payments

## Deliberately left open (not forced to balance)

1. **Ending cash $1,771,630 is activity-only** — the pre-petition balance swept to the DIP account on 3/10 is never quantified in the file, so true ending cash = that + beginning cash.
2. **Pre-petition wage split** of the 3/13 payroll isn't in the books; my 294,285.71 / 117,714.29 pro-rata figure is labeled an assumption, and the $17,150/employee cap test needs headcount.
3. **LSTC gap $8,325,890** between documented vendor claims ($74,110) and the plan term sheet's $8.4M allowed GUC — left open pending schedules/claims register.
4. **Apex's written "Customary Trade Terms"** (a Dkt. 48 ¶1 condition on the $31,200) is unconfirmed; if unsigned, that payment was outside the order.
5. Mesa's threat to withhold the Q2 order implicates §365 and the stay text, neither of which is in the library — flagged **[unverified]** rather than cited.

Files: `deliverable/session1/{response_to_cfo.md, march_mor.json, segregation.csv, march_mor_workpaper.md}`, plus `deliverable/QUESTIONS.md` (Q1–Q9, Q1–Q3 are filing-blocking, MOR due 4/21) and `deliverable/STATUS.md` → **COMPLETE WITH OPEN ITEMS**.