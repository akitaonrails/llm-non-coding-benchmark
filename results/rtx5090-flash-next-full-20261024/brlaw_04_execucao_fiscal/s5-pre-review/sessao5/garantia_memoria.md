# Memória de cálculo — Sessão 5 (garantia × transação)

Registro auxiliar de `sessao5/garantia.json` (entregável do contrato). Valores com SELIC cotada nos autos até **30/11/2026**. Toda cotação percentual usada vem dos autos (`documents/sessao5/proposta_garantia.md`); toda regra, da biblioteca (fontes no fim).

## 1. Decomposição da CDA por período (extração da Sessão 1)

| Período | Total na CDA | Multa 75% (texto da CDA) | Principal | Encargo embutido (resíduo) |
|---|---:|---:|---:|---:|
| 3T/2020 | 268.000 | 104.520 | 139.360 * | 24.120 |
| 4T/2020 | 241.000 | 93.990 | 125.320 (texto) | 21.690 |
| 1T/2021 | 302.000 | 117.780 | 157.040 (texto) | 27.180 |
| 2T/2021 | 289.000 | 112.710 | 150.280 * | 26.010 |
| **Total** | **1.100.000** | **429.000** | **572.000** | **99.000** |

\* principal retrocalculado pela régua **multa = 75% × principal** (Lei 9.430/96, art. 44, I), padrão **verificado nos dois períodos em que a CDA traz principal e multa**: 93.990 = 0,75 × 125.320 ✓ e 117.780 = 0,75 × 157.040 ✓.
O resíduo de 99.000 (encargos/correção já embutidos na CDA) tem **natureza não discriminada** — memória de cálculo do AIF ainda não junta nos autos (**U6**).

## 2. Débitos vivos × decaídos

- Decaídos (crédito inteiro extinto, inclusive a multa do período): 3T/2020 + 4T/2020 = **509.000** (multas extintas junto: 104.520 + 93.990 = 198.510).
- Vivos: 1T/2021 + 2T/2021 = **591.000** = principal **307.320** + multa **230.490** + encargos CDA **53.190**.

## 3. Atualização do remanescente (intimação: "sobre o valor remanescente atualizado")

- SELIC acumulada 10/07/2026 (inscrição da CDA — data dos autos) → 30/11/2026: **3,9%** (cotação dos autos).
- **591.000 × 1,039 = 614.049,00** (acréscimo SELIC = 23.049,00).

## 4. Cobertura da garantia e custos

- Cobertura exigida: débito atualizado **+30%** (Portaria PGFN 164/2014, art. 3º):
  **614.049,00 × 1,30 = 798.263,70** (almofada = 184.214,70 — absorve discussões de cálculo, p. ex. a disputa dos DARFs 84.000 < almofada, sem risco de alegação de insuficiência).
- **Seguro-garantia** 1,2% a.a. (cotação dos autos; biblioteca: faixa típica 0,8–1,5% ✓):
  798.263,70 × 0,012 = **9.579,16/ano**.
- **Fiança bancária** 2,5% a.a. (cotação; biblioteca: faixa 2–3% ✓):
  798.263,70 × 0,025 = **19.956,59/ano**.
- Alternativas: depósito em dinheiro = travar 798.263,70; **penhora de faturamento (5%)** não calculável — faturamento não informado (**U4**) — e é medida excepcional (biblioteca).

## 5. Transação por adesão (edital nos autos)

Base admissível: **apenas os créditos vivos** atualizados — a biblioteca é expressa: "não se transaciona débito decaído: excluem-se primeiro os períodos nulos".

Desconto "até 65%" incide sobre multa/juros/encargos, com teto no principal (biblioteca):

| Cenário de desconto | Conta | Valor |
|---|---|---:|
| Piso (só multa) | 0,65 × 230.490 | 149.818,50 |
| **Estimado (multa + SELIC nova)** | 0,65 × (230.490 + 23.049) | **164.800,35** |
| Máximo (multa + encargos CDA + SELIC) | 0,65 × (230.490 + 53.190 + 23.049) | 199.373,85 |

Teto legal respeitado em todos: desconto ≤ principal 307.320 ✓.
Líquido resultante: **414.675,15 a 464.230,50** em até 120 meses ≈ 3.455,63–3.868,59/mês (acréscimos por parcela **não verificados** na biblioteca — não estimados).

**Condições não confirmadas** (não assumo como fato): classificação do crédito como de difícil recuperação + CAPAG (o desconto é "até 65%" — pode ser menor ou zero); 70% exige PF/ME/EPP (enquadramento não informado); se os DARFs não foram abatidos no lançamento (**U1**), a base cai para **526.773** (item 7) e ainda cabe reduzir a multa calculada sobre valor pago — transacionar sem esse abatimento confessaria débito já pago.

## 6. Comparação de rotas

| Rota | Pagamento esperado | Custo de garantia | Riscos/obs |
|---|---:|---:|---|
| **Defesa (embargos) vencedora** | ~**526.773** (507.000 × 1,039; sem desconto) | seguro ~9.579/ano | mantém tudo; decadência já arguida de ofício (Súmula 393) |
| Defesa + transação futura no resíduo | < 526.773 com desconto sobre a multa remanescente | idem | janela preservada; exige reclassificação do resíduo |
| **Transação hoje (estimado)** | 614.049 − 164.800,35 = **449.248,65** | zero | **confissão irrevogável + desistência de defesas** nos débitos incluídos; perde DARFs (84.000) e vícios formais de 1T/21 e 2T/21; condições do edital não confirmadas |
| Transação hoje (máximo teórico) | 614.049 − 199.373,85 = **414.675,15** | zero | idem, e otimista |

Leitura econômica: a transação máxima barateia ~100–112 mil sobre a defesa vencedora, **mas** (i) esse ganho depende de condições não confirmadas; (ii) queima defesas certas (DARF 84.000 é comprovante de pagamento); (iii) o custo de **manter as duas janelas abertas** é só o prêmio (~9,6 mil/ano ≈ <10% do ganho potencial). Decisão: **seguro-garantia + embargos; transação como plano B condicional**.

## 7. Refinamento transparente de estimativa anterior

A carta da Sessão 4 dizia "591.000 − 145.000 de DARFs → ~R$ 446.000". Correção: o DARF de **61.000** pertence ao **4T/2020, período inteiro morto** pela decadência (241.000 extintos, inclusive a multa) — deduzi-lo dos créditos vivos seria **contar duas vezes**. A dedução economicamente relevante no remanescente vivo é só o DARF de **84.000 (1T/2021)**:

- máx. vivo: **591.000 − 84.000 = 507.000** → atualizado **507.000 × 1,039 = 526.773,00**;
- cobertura nesse cenário: 526.773 × 1,30 = **684.804,90** (seguro ~8.217,66/ano; fiança ~17.120,12/ano);
- e, se o DARF não foi abatido, a **multa** calculada sobre os 84.000 pagos (≈ 54.780 = 0,75 × 84.000) também é excesso de execução — a base cairia ainda mais (não refinado aqui: alocação dos encargos embutidos depende da memória de cálculo ausente — U6);
- o DARF de 61.000 continua importante como **prova** do pagamento antecipado parcial (Tema 163 → art. 150 §4º), não como dedução autônoma.

## 8. Cenário-extremo de vigilância (aditamento por fraude)

Se a Fazenda provasse fraude a ponto de reabrir o 4T/2020 pela exceção do art. 150 §4º: base 591.000 + 241.000 = 832.000 × 1,039 = **864.448**; cobertura **1.123.782,40**; seguro ~13.485,39/ano. O **3T/2020 (268.000) não reabre** em nenhuma hipótese (regra aplicável: art. 173, I, sem cláusula de fraude). Hoje o cenário não tem suporte: AIF e CDA substitutiva reafirmam multa de **75%** (art. 44, I), não 150% (§1º).

## 9. Passos práticos

1. Contratar o **seguro-garantia de 798.263,70** imediatamente — **o prazo da intimação não consta dos autos**; cumprir sem demora para evitar penhora.
2. Garantido o juízo, **embargos em 30 dias** (LEF art. 16): decadência (509.000, de ofício), excesso de execução (até 84.000 + multa sobre valor pago), vícios formais.
3. **Não assinar transação** antes de confirmar por documento: classificação/CAPAG, percentual real, abatimento prévio dos DARFs e exclusão formal dos períodos decaídos.
4. A garantia **não encerra** a defesa de Ana Paula no redirecionamento; e eventual transação da empresa não a libera automaticamente (efeito **não verificado** na biblioteca).

## Fontes (biblioteca fechada) e não verificados

- `library/selic_e_garantia.md`: SELIC (Lei 9.430, art. 61 §3º); cobertura +30% (Portaria PGFN 164/2014, art. 3º); faixas de custo seguro 0,8–1,5% / fiança 2–3%; penhora de faturamento excepcional; LEF art. 9º §3º.
- `library/transacao_pgfn.md`: Lei 13.988/2020; Portaria PGFN 6.757/2022; até 65% (70% PF/ME/EPP) sobre multa/juros/encargos, teto no principal; 120 meses; confissão irrevogável + desistência de defesas; **não se transaciona débito decaído**.
- Cotações 1,2% / 2,5% / 5% / SELIC 3,9% / edital 65%-120m: **autos** (`documents/sessao5/proposta_garantia.md`) — cotação, não fato garantido.
- **Não verificados** (citados apenas como alerta, jamais como autoridade): efeito da transação sobre a execução e sobre o redirecionamento; mecânica de transação parcial (exclusão de períodos antes da adesão); acréscimos por parcela do parcelamento; natureza dos 99.000 de encargos embutidos na CDA.
