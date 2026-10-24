# Sol 6 medium — core timing baseline

Model: `gpt-6-sol`; reasoning: `medium`; concurrency: 4; started: 2026-10-22T18:48:18Z.

Finished executions: 16/16. Infrastructure failures: 0. Correctness is not yet graded.

Suite elapsed wall time: **22.26 minutes** (includes controller waits).

Summed active candidate time: 67.33 minutes. Median per engagement: 3.78 minutes.
Summed controller waiting: 14.09 minutes; these waits can overlap across workers.

Input: 8,857,980, including 8,327,552 cached and 0 cache-write tokens. Output: 259,753, including 78,071 reasoning tokens.

Estimated API-equivalent cost: **$5.3239**. Authentication used ChatGPT subscription; this is not an observed API invoice.

| Engagement | Active min | Elapsed min | Turns | Input | Cached | Output | API equiv. USD | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| bracc_01_das_fator_r | 4.54 | 5.52 | 3 | 532,931 | 500,224 | 18,479 | 0.3502 | completed_ungraded |
| bracc_03_cbs_ibs_ano_teste | 2.91 | 3.28 | 3 | 428,857 | 384,256 | 11,404 | 0.2801 | completed_ungraded |
| bracc_06_venda_quotas_vs_ativos | 3.74 | 4.27 | 3 | 366,809 | 343,040 | 14,438 | 0.2605 | completed_ungraded |
| bracc_10_provisoes_covenant | 4.49 | 5.26 | 4 | 475,507 | 444,928 | 19,157 | 0.3417 | completed_ungraded |
| brlaw_01_prazos_processuais | 2.47 | 3.24 | 3 | 372,285 | 350,208 | 8,445 | 0.1986 | completed_ungraded |
| brlaw_03_pejotizacao | 3.54 | 3.91 | 3 | 339,704 | 316,160 | 13,240 | 0.2427 | completed_ungraded |
| brlaw_07_credor_rj | 3.42 | 4.49 | 4 | 408,795 | 370,304 | 12,366 | 0.2747 | completed_ungraded |
| brlaw_10_cobranca_prescrita | 4.41 | 5.39 | 4 | 529,638 | 498,176 | 19,316 | 0.3557 | completed_ungraded |
| usacc_02_close_gap | 4.65 | 5.32 | 4 | 582,806 | 549,248 | 16,610 | 0.3431 | completed_ungraded |
| usacc_03_household_1040 | 3.67 | 4.29 | 4 | 525,483 | 497,280 | 13,662 | 0.2925 | completed_ungraded |
| usacc_06_sale_asset_vs_stock | 5.70 | 6.82 | 4 | 596,220 | 559,616 | 20,537 | 0.3905 | completed_ungraded |
| usacc_09_revenue_going_concern | 4.10 | 5.90 | 5 | 472,349 | 436,352 | 15,466 | 0.3139 | completed_ungraded |
| uslaw_01_deadlines_removal | 2.98 | 3.95 | 4 | 356,914 | 332,160 | 11,433 | 0.2303 | completed_ungraded |
| uslaw_03_noncompete_memo | 3.81 | 4.25 | 3 | 447,121 | 416,384 | 14,918 | 0.2939 | completed_ungraded |
| uslaw_04_litigation_sequence | 9.58 | 12.09 | 9 | 2,101,257 | 2,031,232 | 36,730 | 0.9136 | completed_ungraded |
| uslaw_09_retaliation_termination | 3.31 | 3.46 | 3 | 321,304 | 297,984 | 13,552 | 0.2418 | completed_ungraded |

| Phase | Turns | Summed active min | API equiv. USD |
|---|---:|---:|---:|
| Initial/session work | 20 | 22.33 | 1.7313 |
| Client follow-up | 9 | 14.51 | 1.0062 |
| Pushback | 17 | 5.37 | 0.4057 |
| Final review | 17 | 25.12 | 2.1807 |

Standard API-equivalent rates per million tokens: uncached input $2; cache reads $0.20; cache writes $2.50; output $10. Reasoning is included in output, not added twice. Rates checked 2026-10-22: [official model pricing](https://developers.openai.com/api/docs/models/gpt-6-sol).

Setup, preflight, the invalidated first attempt, and Astra controller usage are excluded from these candidate measurements. Normal provider caching was enabled; this is not a cold-cache measurement. Four workers were scheduled, but controller pauses and uneven case lengths affect effective concurrency. This single timing pilot does not establish reliability or professional fitness. Controller decisions about question paraphrases and scripted pushback are documented in docs/BASELINE_RUN.md; all client answers are verbatim from the frozen script.
