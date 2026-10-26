# STATUS do engajamento — atualização ao fim do fechamento de 03/2026 e da apuração do 1º trimestre

**COMPLETE WITH OPEN ITEMS** — todos os entregáveis do contrato foram produzidos (meses 01, 02 e 03 + e-LALUR trimestral Partes A e B). Itens em aberto listados ao final (não bloqueiam os números).

**Sessão final (sem novas informações):** o cliente declarou não ter mais informação sobre as perguntas remanescentes e nenhum documento novo chegou. Os itens 1–5 abaixo são portanto **desconhecidos encerrados com premissas documentadas** — únicos gatilhos de retrabalho futuro: (1) confirmação de que o sistema da ATLAS postou o estorno (testar 1.1.04 em todo balancete novo); (2) status real das EFD/DCTF de janeiro (retificação na competência janeiro; valores mensais inalterados); (3) eventual memória de ICMS (conferência fora do escopo); (4) convenção de arredondamento do ECF (Q6; impacto < R$ 0,01; só IRPJ e CSLL finais mudariam); (5) se surgirem documentos fiscais dos brindes/doação (ICMS/IPI — sem autoridade citável no acervo, nada afirmado).

## Entregáveis (todos escritos)
- `mes_01/`: ajustes.json · pis_cofins.json (a recolher **79.883,00**) · pendencias.md
- `mes_02/`: ajustes.json · pis_cofins.json (a recolher **81.141,00**) · pendencias.md
- `mes_03/`: ajustes.json · pis_cofins.json (a recolher **82.399,00**) · pendencias.md · **lalur.json** · **memoria.md**

## Fechamento de março
- Balancete de março confere com o razão jan+fev+mar **conta a conta** (Python) → prova que AJ-2026-01-001/AJ-2026-02-001 nunca foram espelhados (1.1.04 = 483.627,00 ainda contém os 11.100,00 indevidos). **AJ-2026-03-001** reitéra o estorno (D 4.2.04 / C 1.1.04); postar **um único** estorno; corrigido 1.1.04 = 472.527,00.
- PIS/COFINS mar: débito 242.350,00 (2.620.000,00 × 9,25%); créditos 159.951,00 (1.729.200,00 × 9,25%); estornos do mês 0,00; **a recolher 82.399,00**.
- Resultado líquido mar: 282.583,00. Trimestre corrigido: 128.483 + 193.083 + 282.583 = **604.149,00** (balancete sem estorno 615.249,00 − 11.100,00 ✔).

## e-LALUR 1º trimestre (Parte A — memoria.md com todos os fundamentos)
| Linha | Valor |
|---|---|
| Lucro líquido contábil (corrigido) | 604.149,00 |
| Adições: brindes NF-e 4410 (art. 13, VII) + doação Luz (art. 13, VI e §2º) | + 78.000,00 |
| Exclusões | 0,00 |
| Lucro antes da compensação | 682.149,00 |
| Compensação de prejuízo (trava 30% × 682.149,00 — Lei 9.065/95, arts. 15–16) | − 204.644,70 |
| **Lucro real** | **477.504,30** |
| IRPJ 15% | 71.625,65 (exato 71.625,645 — ver arredondamento) |
| Adicional 10% sobre o que excede 60.000,00/trimestre | 41.750,43 |
| CSLL 9% | 42.975,39 (exato 42.975,387) |
| **Total IRPJ + adicional + CSLL** | **156.351,47** |

## Parte B — saldos a compensar
| Saldo | 31/12/2025 | Compensado Q1 | Final |
|---|---|---|---|
| Prejuízo fiscal | 900.000,00 | 204.644,70 | **695.355,30** |
| Base negativa CSLL | 900.000,00 | 204.644,70 | **695.355,30** |

Pedido do diretor ("compensar todo o prejuízo") recusado por fundamento legal: a trava de 30% exige lucro ajustado ≥ 3.000.000,00 no trimestre para compensar 900.000,00; o STF (RE 591.340, Tema 117) confirmou a constitucionalidade da trava.

## Itens em aberto / desconhecidos (não alteram os números entregues)
1. **Estorno de 11.100,00 ainda não espelhado no sistema** (3ª reiteração; AJ-2026-03-001 é o formulário vigente). Todo balancete futuro deve ser testado pela conta 1.1.04.
2. **EFD-Contribuições/DCTF de janeiro**: status de entrega desconhecido; retificação (se houver) na competência janeiro — a recolher de todos os meses permanece.
3. **ICMS jan–mar**: sem memória de cálculo; valores mantidos como registrados (177.800 / 180.600 / 183.400).
4. **Q6 (nova) — arredondamento**: sem regra na biblioteca; aplicada a premissa "centavo mais próximo" (71.625,65 / 42.975,39); truncamento daria 71.625,64 / 42.975,38. Confirmar convenção do ECF.
5. **Não verificado (sem autoridade no acervo)**: ICMS/IPI na saída de brindes/doação — nada afirmado nem lançado.
