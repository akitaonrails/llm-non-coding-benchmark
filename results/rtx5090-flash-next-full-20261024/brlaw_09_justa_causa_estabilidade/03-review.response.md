Good check to run before delivery. Let me re-audit every number, citation and claim against the library and documents.

The audit confirmed one real arithmetic error and several labeling issues. Let me read the current files and fix them.

The files still contain the wrong figures. Applying all corrections now.

Now validating the JSON and sweeping for any leftover stale figures:

Two consistent but stale-worded date references; let me align them, and verify the CONTRACT's STATUS wording requirement:

Contract says "with one of" — the file already includes it; I'll also end the file with the marker to satisfy the stricter reading, then re-validate everything:

Final consistency sweep across all three deliverables:

Review complete — it caught one real arithmetic error and a few labeling gaps. All fixed and re-validated. Here's what changed:

## 1. Real arithmetic error (the headline fix)
My month-count helper double-subtracted a month when the end date's day-of-month is smaller than the start's. The CIPA stability window (11/10/2026 → 02/06/2028) was computed as **18.70 months** — wrong. Correct derivation, now shown in §5.2: **19 full months** (→ 11/05/2028) **+ 22 days** = 19 + 22/30 = **19.733 months** (600 calendar days). Gestante (11.40) was unaffected.

| Figure | Was | Now |
|---|---|---|
| Indenização estabilidade (CIPA base) | 174,221.67 | **183,848.89** |
| Total cenário-base | 230,684.74 | **240,311.96** |
| Cenário sem justa causa (§8.3) | ≈215,684.74 | **≈225,311.96** |
| "Economia" da troca justa→sem justa causa | ~7% sobre ~215 mil | **6.7% sobre ~225 mil** |
| Faixa de exposição | 163–231 mil | **163–240 mil** |

Updated consistently in `parecer.md` (conclusão, §5.2, §5.4, §6, §7.3, §8.3 table), `parecer.json` (`exposicao_se_reverter`, alternativas, recomendação) and `STATUS.md`. Note: figures quoted in the turn-2 chat replies to Renata used the understated number — the corrected files are the authoritative record. JSON re-validated: components sum to total exactly (Decimal check), schema keys intact.

## 2. Unsupported authority — relabeled "não verificado"
- **§8.1**: "Difamação exige imputação falsa" was asserted as law; the general defamation concept isn't in the library. Now labeled as an untranscribed general concept, with the argument anchored on the library's own 482-"k" language.
- **§5.1**: the ≥15-days fractional rule for 13º (9/12) and férias (7/12) is an assumed methodology — the library only names the line items. Now footnoted as such and added to §7.1.
- **§8.3 table**: seguro-desemprego in the *direct* sem-justa-causa scenario — the library mentions it only as an effect of reversion. Now labeled accordingly (§7.1 too).
- Added a line in §7.1 and STATUS open item 3 covering these labels.

## 3. Reconciliation/wording fixes
- §2 table: "51 dias depois" of the fact → clarified as **51 days after knowledge** (21/08), 52 after the fact.
- §4.1: "fim do mandato ≈ 01/06/2027 → estabilidade 02/06/2028" was internally off by a day; now "término ≈ 01/06–02/06/2027; referência adotada 02/06/2028 (= posse + 2 anos, estimativa)" — same wording aligned in `parecer.json`.
- §5.2: displayed multiplication now reproducible — the 22/30 fraction (19.733, not 19.73) and note that products use the exact monthly 9,316.667; the month-counting convention itself labeled as assumed.
- `STATUS.md` now also ends with the `COMPLETE WITH OPEN ITEMS` marker.

No stale figures remain (grep sweep: 0 hits for all old values). Conclusion is unchanged — justa causa still not viable; the correction actually *strengthens* the "don't apply" recommendation since exposure is ~R$ 9.6k higher than previously stated.