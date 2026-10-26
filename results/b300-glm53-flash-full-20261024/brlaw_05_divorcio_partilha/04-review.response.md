Starting the pre-delivery review. First step: full re-read of all deliverables and the source documents for cross-checking.

Path typo on the third read — retrieving alimentos.json plus the remaining files:

All deliverables read. Now verifying every citation against the library whitelist and checking the remaining library bodies + source documents:

A retomar a revisão em partes menores. Primeiro, uma releitura completa dos dois arquivos que foram truncados:

Full pocket documents in hand. I've already found candidates to verify (FGTS "meação" wording inconsistency; the carro sensitivity direction; CC 1.664/1.027 whitelist edges). Now the remaining deliverables and source docs in full:

I need the exact current text of each fix site to build precise edits. Re-reading in bounded slices to avoid truncation:

Now the JSON files in bounded slices, plus QUESTIONS.md and STATUS.md in full:

Now alimentos.json rest, QUESTIONS.md and STATUS.md in full:

All fix sites confirmed — including two extra spots (STATUS.md line 7 + line 18) carrying the wrong carro sensitivity. Now the remaining source documents for the fact cross-check:

All documents cross-checked. Now the INDEX (to quote its exact listing wording) plus a full arithmetic verification with receipts:

Verification receipts are all green (partilha 95.000 closes both ways; sensitivity flows 125.000/155.000 close; 54.730/ano exact). Now extracting the exact current text of every fix site so each edit lands on the first try:

Exact texts locked in. Now the remaining fix sites (STATUS.md full, alimentos l.26, proposta §1.3/§6.4 CC 1.027 lines, and the DÍVIDAS table row):

Everything needed is in hand. Applying the correction pass now — Batch A: first half of `proposta_acordo.md` (CC 1.664 provenance, PGBL pointer, FGTS attribution + meações list):

Batch A landed. Batch B — second half of `proposta_acordo.md` (CC 1.027 removal ×2, §5 FGTS row, 54.730 ×2, leitura econômica, sensitivity):

`proposta_acordo.md` complete. Batch C — `partilha.json` (FGTS controversy, quotas CC 1.027, carro sensitivity, DÍVIDAS provenance):

Batch C landed. Batch D — `alimentos.json` (54.730), `QUESTIONS.md` (carro item), and `STATUS.md` (both sensitivity spots + new review section):

All figure-fixing edits are in. Now appending the review section to `STATUS.md`:

Now three micro-fixes for full citation rigor (one pt-PT slip "facto", and trimming bare `1.664` mentions in spots where it could read as an unsourced citation):

All edits landed. Final re-verification: JSON validity, banned-string sweep, presence of the corrected figures, and CC 1.664 provenance coverage:

Validation results: both JSONs parse cleanly; the banned phrases survive **only inside the STATUS.md changelog** (which quotes them as removed — intended); all corrected figures are present in every deliverable spot. One residual catch: `QUESTIONS.md` line 13 still cites CC 1.664 bare ("entram como comuns (CC 1.664)") with no provenance in that file — same defect I fixed in item 3. Fixing it plus one awkward changelog phrasing:

Everything closes. Final sweep is clean — the only remaining hits for removed wording are inside the STATUS.md changelog itself, which quotes them as *the things that were fixed*.

## ✅ Correção pré-entrega aplicada — changelog

**Nenhuma cifra do quadro mudou:** partilhável 2.650.000 · dívidas 360.000 · líquido 2.290.000 · meação 1.145.000 · **equalização única: Marcelo paga Fernanda R$ 95.000** (conferência fecha nos dois lados: 1.050.000+95.000 ✓; 1.240.000−95.000 ✓). Valores de alimentos intactos (8.812,50 / teto 9.750 / piso 7.050; oposta 14.540).

### 1. FGTS — linguagem corrigida em 5 pontos (`proposta_acordo.md` ×4, `partilha.json` ×1)
- Eliminado todo "concede a meação" e "paga a meação em dinheiro". Posição única e consistente: **FGTS 100% com Marcelo; Fernanda NÃO cobra a meação de 70.000** — abdicada pela própria contraparte ("fica com ele"), nada entra no fluxo a esse título.
- §5 redesenhado: de "conceder (R$ 70.000)" para "**ACEITAR como está**" com fundamentação econômica (aceitar é dinheiro ganho; reabrir devolve os 70.000 à mesa).

### 2. Sensibilidade do carro — RECALCULADA em 4 pontos (proposta §6.4, `partilha.json`, `QUESTIONS.md`, `STATUS.md` ×2)
- A versão anterior ("equalização se inverte; Fernanda pagaria entre ≈5.000 e ≈65.000") estava **errada em direção e magnitude**. Correto: se provada compra pré-casamento, o carro sai do quadro comum → meação líquida cai de 1.145.000 para **1.085.000** (dívida comum, ex-CC 1.664) ou **1.115.000** (dívida dela); a equalização **Sobe** de 95.000 para **125.000–155.000** — sempre a favor de Fernanda, o fluxo nunca se inverte. Aritmética re-verificada (ambas as variantes fecham).

### 3. CC 1.027 removido das citações (3 pontos)
- Dispositivo fora da whitelist do INDEX → regra mantida como nota descritiva ("anotada na biblioteca") em proposta §1.2, §1.3(i) e `partilha.json` (quotas).

### 4. CC 1.664 — proveniência declarada (4 pontos + 1 bônus achado nesta checagem)
- Nota de proveniência na linha do apto; pointer na linha DÍVIDAS (proposta) e nota completa no row DÍVIDAS (`partilha.json`); pointer no carro do `partilha.json`. **Na re-checagem final achei ainda uma citação nua em QUESTIONS.md l.13 (outras dívidas)** → corrigida com pointer para a nota da partilha.

### 5. Aritmética de alimentos — "54.700" → **"54.730" exato** (3 pontos)
- Proposta §5 tabela, leitura econômica e `alimentos.json`; com o acréscimo "(exato: 174.480 − 119.750)" e "4.560/mês" → "**4.560,83/mês**".

### 6. Pointer errado corrigido (`proposta_acordo.md` §1.1)
- Linha do PGBL apontava "(ver §1.2)" — que trata de quotas — trocado pela referência correta à conferência de equalização do próprio §1.1.

### 7. Higiene
- Typo pt-PT "facto" → "fato"; phrasing redundante no changelog do STATUS ajustado.
- **Validação técnica**: `partilha.json` e `alimentos.json` parseiam limpo (JSON OK); grep confirma zero menções a "1.027", "54.700", "≈5.000/65.000", "se inverte" e "concede/paga a meação" fora das citações do próprio changelog.

**STATUS: COMPLETE WITH OPEN ITEMS** (7 pendências + seção "Revisão pré-entrega (26/10/2026)" documentando a pass). Pacote pronto em `/work/workspace/deliverable/`: `proposta_acordo.md`, `partilha.json`, `alimentos.json`, `QUESTIONS.md`, `STATUS.md`.