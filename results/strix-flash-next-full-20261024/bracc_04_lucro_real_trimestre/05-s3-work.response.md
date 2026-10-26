Documentos de março chegaram. Vou amarrar razão ⇄ balancete dos três meses e calcular tudo em Python antes de redigir.

Contas fecham. Vou reler os dois textos-base para as citações exatas da memória e conferir o formato dos ajustes de fevereiro.

Base normativa confirmada. Escrevendo os cinco entregáveis de março agora.

Tudo validado. Engajamento do 1º trimestre/2026 encerrado.

## Fechamento de março (`deliverable/mes_03/`)

**Conferências (Python):** razão de março equilibrado; balancete de março == razão jan+fev+mar **conta a conta** — o que prova que os ajustes anteriores nunca foram espelhados (1.1.04 = 483.627,00 ainda contém os 11.100,00 indevidos).

- **ajustes.json** — **AJ-2026-03-001** (D 4.2.04 / C 1.1.04, 11.100,00): terceira reiteração do estorno, com aviso explícito para postar **um único** estorno (os AJs de jan/fev jamais entraram). Corrigido: 1.1.04 = 472.527,00 (= 155.067 + 157.509 + 159.951).
- **pis_cofins.json** — débito 242.350,00 (2.620.000 × 9,25%); créditos 159.951,00 (1.729.200 × 9,25%, todos de revenda — mês limpo); estornos 0; **a recolher 82.399,00**.

## e-LALUR do trimestre (`lalur.json` + `memoria.md`)

| Parte A | Valor |
|---|---|
| Lucro líquido contábil (corrigido; balancete sem estorno 615.249 − 11.100 ✔) | 604.149,00 |
| Adições: brindes NF-e 4410 (Lei 9.249/95, art. 13, VII) + doação Luz (art. 13, VI e §2º — "não tem título nenhum") | + 78.000,00 |
| Lucro antes da compensação | 682.149,00 |
| Compensação — **trava de 30%** (Lei 9.065/95, arts. 15–16; STF RE 591.340) | − 204.644,70 |
| **Lucro real** | **477.504,30** |
| IRPJ 15% / adicional 10% s/ excedente de 60.000/trimestre | 71.625,65 / 41.750,43 |
| CSLL 9% | 42.975,39 |
| **Total** | **156.351,47** |

**Parte B:** prejuízo fiscal e base negativa CSLL terminam em **695.355,30** cada. O pedido do diretor ("compensar tudo") é inviável: exigiria lucro ajustado ≥ 3.000.000,00 no trimestre.

## Status

`STATUS.md` atualizado: **COMPLETE WITH OPEN ITEMS** — todos os 11 entregáveis do contrato produzidos. Em aberto (não alteram os números): estorno ainda não espelhado no sistema (3ª vez); status da EFD/DCTF de janeiro desconhecido; memória de ICMS ausente; e o novo **Q6** em `QUESTIONS.md` — a biblioteca não traz regra de arredondamento, então apliquei "centavo mais próximo" (71.625,65 / 42.975,39) com a alternativa de truncamento declarada (diferença < R$ 0,01).