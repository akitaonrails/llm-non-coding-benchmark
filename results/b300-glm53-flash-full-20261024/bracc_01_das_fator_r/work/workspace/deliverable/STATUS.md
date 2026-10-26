# STATUS — Apuração DAS maio/2026 · Lumen Soluções Digitais ME

**COMPLETE WITH OPEN ITEMS**

## Resultado
- `apuracao.json` ✔ — DAS total de maio/2026: **R$ 15.188,84**
  (serviços: R$ 78.000 × efetiva 18,8235% = R$ 14.682,35 · locação: R$ 6.000, Anexo III faixa 4,
  efetiva 12,5059% × 0,675 por dedução do ISS 32,50% = R$ 506,49).
- `memoria.md` ✔ — memória completa (§1–§10): RBT12 R$ 1.020.000; folha 12m R$ 284.600 com o
  pró-labore de abril pago em 30/04/2026 dentro da janela; Fator R 27,90% ⇒ Anexo V, faixa 4;
  estorno −4.000 (NFS-e 1188) e locação segregada (NF-e 000.512).
- `QUESTIONS.md` ✔ — registro: 1 pergunta respondida, 1 parcial, 2 sem resposta (o cliente
  informou não ter mais nada a acrescentar); incertos remanescentes listados.

## Respostas do cliente (2ª rodada) — efeito na apuração
- **Pró-labore de abril pago em 30/04/2026** (o "06/05" do e-mail inicial era apenas o
  lançamento do PIX no sistema contábil, não o pagamento). Pago dentro de mai/2025–abr/2026
  (Res. CGSN 140, art. 26, §2º) ⇒ **permanece na base** do Fator R de maio/2026: folha 12m =
  R$ 284.600,00, Fator R = 27,90% (< 28%) ⇒ Anexo V mantido; DAS inalterado.
- **Locação à Orla é corrente ("por uns meses")** — classificada como locação de bens móveis
  (NF-e, não NFS-e), coerente com **[LOCACAO]**; em maio só a NF-e 000.512 consta no acervo.

## Itens abertos
1. **Locações anteriores à NF-e 000.512 — composição do RBT12 (não confirmada).** O cliente
   disse que a locação à Orla vem ocorrendo "por uns meses", mas só apresentou a NF-e de maio e
   não confirmou se os valores anteriores estão somados em `faturamento_12_meses.csv`
   ("receita_bruta"). Se nenhuma locação anterior estiver no CSV (cenário ilustrativo, "uns
   meses" ⇒ teto de 6 meses × R$ 6.000):
   - +2 meses → RBT12 1.032.000: efetivas 18,8430% / 12,5465% ⇒ DAS = 14.697,56 + 508,13 = **R$ 15.205,69**;
   - +6 meses → RBT12 1.056.000: efetivas 18,8807% / 12,6250% ⇒ DAS = 14.726,93 + 511,31 = **R$ 15.238,24**.
   Impacto máximo +R$ 49,40 (≈ +0,3% do DAS). Em qualquer cenário: 4ª faixa (limite R$ 1.800.000)
   e Anexo V (o Fator R só diminui: 284.600 ÷ 1.056.000 = 26,95% < 28%). Fechar o valor exato
   exige as notas/extratos de locação dos meses anteriores.
2. **Repartição do Anexo V ausente da biblioteca.** Os percentuais por tributo (CPP, IRPJ, CSLL,
   COFINS, PIS) do Anexo V não constam em nenhum arquivo de `library/` (só a repartição do
   Anexo III, 4ª faixa, usada para deduzir o ISS da locação). O campo `reparticao` de
   `apuracao.json` está zerado e **não validado** — nenhuma fonte externa foi citada. Sem efeito
   no valor do DAS (divisão interna apenas).
3. **Comprovante de 30/04 do pró-labore de abril não anexado.** O cliente afirmou tê-lo
   enviado; não há arquivo correspondente em `documents/`. A entrada na base (Fator R 27,90%)
   repousa na declaração do cliente; anexar o comprovante ao dossiê.
4. **Remapeamento de pagamentos de folha anteriores a maio/2026 impossível.** Sem extratos de
   2025-05 a 2026-03 não é possível conferir mês a mês o critério do "pago" (ex.: encargos
   "DARF/GPS/FGTS ABR" −4.700 debitados só em 07/05). O cliente disse não ter mais nada a
   acrescentar. Resultado robusto: Fator R entre 25,49% e 27,90% em qualquer leitura — sempre
   < 28%, veredito e valor do DAS inalterados.
5. **Extrato `.pdf` ilegível** — apuração conferida com o `.csv` espelho; os valores cruzaram
   com as notas (premissa A4 em `memoria.md` §9).

## Correções ao pedido do sócio (não bloqueiam)
- "Repetir o Anexo V" ✔ anexo correto (Fator R 27,90% < 28%), mas o índice é a **alíquota
  efetiva** (§1º-A), 18,8235%, e não a nominal da faixa (20,50%): diferença evitada de
  R$ 1.307,65 nos serviços.
- Locação de notebooks **não** "vai junto com os serviços": Anexo III com dedução do ISS
  (Súmula Vinculante 31 / art. 18, §5º-A), receita segregada em livro próprio.
