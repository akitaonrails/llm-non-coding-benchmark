Starting the pre-delivery review. First, I'll load all deliverables and the authority sources in parallel.

The §4(a) verbatim quote matches the library file in substance (only bold `**` markers stripped). Now loading the remaining deliverables and sources.

Now loading the remaining files: PERGUNTAS.md, calc.py, INDEX.md, and CONTRACT.md.

Let me check CONTRACT.md requirements and the library files cited, then run the verification script.

CONTRACT requirements confirmed. Now let me verify the in-text library claims against the actual library files, and load the verify script.

All library files loaded. The "CND positiva → retenção" and "JUCESP não exige CND" claims check out against `ctn_133/lei14133`. Let me read the verify script, then run the mechanical checks.

Mechanical checks confirmed green (twins identical; 17 findings; enum counts valid). Now I'll locate the exact strings for each fix target (F1–F6 plus the redline list-label slip I flagged) before editing.

All targets located. Reading the surrounding context of each fix so the edits anchor precisely.

Now reading the nota "Para terminar" region and the STATUS §1/§6 regions to prepare F4–F6.

All fix targets have unique anchors. Applying the fixes now — F1 (three files), F2 (quote punctuation), F3 (typo + trigger attribution), F4 (unsupported market claim), F5/F6 (STATUS reconciliation).

Deliverable edits applied. Now the STATUS reconciliation edits (F5: §1 table rows; F6: §6 verification record).

All fixes are in. Now regenerate the verification script fresh and run the full green sweep. First, capture `calc.py`'s exact output so the script can assert the real numbers, and re-confirm the twins.

`calc.py` clean and twins identical. Writing the fresh verification script with the 8 checks plus fix-specific assertions.

The script I just wrote has the known bug in check 2e (`onde = a["onde"]` sitting at the wrong indent level) plus a fragile token-resolution step. Before rewriting it cleanly, let me confirm the exact contract-token strings it will assert.

All tokens confirmed. Rewriting the verification script cleanly (fixing the check-2e indentation, robust token resolution via basename/path map, clean detail output), then running it.

ALL GREEN — 31/31 checks pass. One final spot-check of the newest text (the §6 record I added to `STATUS.md` and the reworked §1 passage) to confirm it reads cleanly, then I'll report.

Review complete — all fixes applied and the full verification sweep is **ALL GREEN** (31/31 checks, including twins byte-identical, `calc.py` running clean, and the re-run confirming every edit).

## What I changed (7 fixes, 10 edits)

1. **`a contrario` scope narrowed — 3 files** (`resposta_advogado_comprador.md` §1, `redline.md` Anexo 3.2(ii), `achados.json` achado #2): the library applies the *a contrario* reading only to **art. 137, VI**. Communication (art. 92, XVI) and habilitation (art. 124, II) are now cited as direct duties, not "interpretados a contrario".
2. **Quote fidelity** (`resposta` §2): the CADE citation now reads `"Fora dos limiares, não há notificação obrigatória"` with the period moved outside the quotes, so the quoted fragment is exactly a contiguous excerpt of `library/cade_limiares.md`.
3. **Typo + attribution** (`achados.json` achado #8): "aceleração/**doação** anualizada" → "**aceleração do earn-out por base anualizada**"; the acceleration mechanics are cited to `library/earnout_pratica.md` **for revenda**, and the additional triggers (cisão, alteração relevante) are now explicitly labeled "extensão nossa".
4. **Removed an unsupported claim** (`nota_socios.md`, "Para terminar"): deleted "e o comprador costuma descontar isso do preço de hoje" — a market-practice assertion with no basis in the library.
5. **List label** (`redline.md`, motivo 3.2): "A lista (A)-(iii)" → "A lista (i)-(iii)" (straggler mislabel of the proposed (i)/(ii)/(iii) items).
6. **STATUS §1 reconciled**: the `resposta` row now records the §4 Aditamento (25/10) and the `nota` row now records the "Podemos só assinar?" section — previously the table understated both files.
7. **STATUS §6**: added the "Revisão de pré-entrega" record (fix list i–vi) and the "Checagem final pré-entrega" verification bullet.

## Checked and deliberately left intact

- The resposta's opening "premissa de 'minuta padrão' se sustenta" — rhetorical concession, consistent with §4(a) ("Não disputamos o método"); no change.
- The §4 verbatim quote of `library/sandbagging_franquia_mercado.md` — verified letter-for-letter (only `**` dropped).
- All arithmetic re-verified via `calc.py` (1.302M / 504k / 1.806M / gap 1.02M = 24,29% / teto 4.285.714,29 → 5.385.714,29 = 128,23% / 35k–70k rateio / PJ 466.666,67 → 5.133.333,33 = 122,22%).
- The labored items stay open as required: the R$ 1,02M labor gap (unreconciled) and the PJ teto-específico (arithmetic only, no base); the 12 unknowns were not re-asked; the 4 non-library topics remain flagged "não verificado"; all 12 unknowns and the 17-findings schema/twin files untouched.

Deliverable set in `/work/workspace/deliverable/` is ready to go out.