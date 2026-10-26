All documents are in hand. Now let me verify the arithmetic and the decadência dates with Python.

Sessão 1 concluída. Entregáveis em `deliverable/sessao1/` + `QUESTIONS.md` e `STATUS.md`.

## Decadência por período (regra do acervo: CTN 150 §4º / 173 I; Súmula 555; Tema 163)

| Período | Situação no PAF | Regra | Termo final | AI 03/02/2026 | Valor CDA |
|---|---|---|---|---|---|
| 3T/2020 | sem pagamento, DCTF zerada | **173 I** (marco 01/01/2021) | 31/12/2025 | **DECAÍDO** | R$ 268.000 |
| 4T/2020 | pagto parcial (DARF 29/01/2021) | **150 §4º** (FG 31/12/2020) | 31/12/2025 | **DECAÍDO** | R$ 241.000 |
| 1T/2021 | pagto parcial (DARF 30/04/2021) | 150 §4º (FG 31/03/2021) | 31/03/2026 | hígido | R$ 302.000 |
| 2T/2021 | sem pagamento, DCTF zerada | 173 I (marco 01/01/2022) | 31/12/2026 | hígido | R$ 289.000 |

**Decaido: R$ 509.000 (46,3%) | Remanescente: R$ 591.000.** Aritmética da CDA conferida em Python (multas = exatos 75% do art. 44 I da Lei 9.430; somas fecham em R$ 1.100.000). Ponto de reforço: a multa de 75% (e não 150% do §1º, que exigiria fraude/sonegação fundamentada) afasta a cláusula de exceção do 150 §4º; e para o 4T/2020 a decadência se verifica sob qualquer premissa de termo inicial (FG ou vencimento do DARF).

## Vícios formais
- Campo "fundamento da multa" em branco → LEF art. 2º §5º III (sanável por emenda — §8º/Súmula 392, por isso não é o veículo principal);
- Endereço da CDA desatualizado (sede alterada na JUCESP 12/03/2026 e RFB 20/03/2026, antes da inscrição) → mandado negativo de 28/09/2026;
- Base de cálculo não individualizada + imputação dos DARFs de R$ 61k/84k → matérias de embargos (rotuladas como não expressamente suportadas pela biblioteca quando foi o caso).

## Veículo escolhido: **exceção de pré-executividade**
Decadência é conhecível de ofício e prova-se com datas do próprio título + DARFs/DCTFs (Súmula 393) — sem garantia do juízo, ao passo que embargos exigiriam garantia (LEF arts. 9º, 16 §1º). Peça protocolar em `peca.md`; embargos ficam reservados para as matérias dependentes de prova, e a Súmula 392 (vedada modificação do sujeito passivo) já fica arada contra a emenda/redirecionamento da Sessão 2.

**Aberto** (questões escritas em `deliverable/QUESTIONS.md`): (1) inconsistência citação 14/09 × mandado negativo 28/09; (2) auto de infração integral (imputação dos DARFs e memória de cálculo); (3) comprovantes originais para instruir a exceção. `STATUS.md`: COMPLETE WITH OPEN ITEMS.