# Pendências — março/2026 e fecho do 1º trimestre

## Conferências efetuadas (Python)
- Razão de março equilibrado (débitos = créditos).
- **Balancete de março == razão jan+fev+mar, conta a conta** (nenhuma divergência), o que prova que **nenhum dos ajustes propostos (AJ-2026-01-001 / AJ-2026-02-001) jamais foi espelhado no sistema da ATLAS**: 1.1.04 = 483.627,00 = 166.167 + 157.509 + 159.951 (ainda contém os 11.100,00 indevidos de janeiro).
- PIS/COFINS de março conferem: débito 242.350,00 = 2.620.000,00 × 9,25%; crédito 159.951,00 = 1.729.200,00 × 9,25%. ICMS 183.400,00 = 2.620.000,00 × 7% (valor registrado, ver item 3).
- Lucro líquido: mar 282.583,00; trimestre corrigido 604.149,00 (balancete sem estorno 615.249,00 − 11.100,00 ✔).

## Pendências e desconhecidos remanescentes

> **Sessão final:** o cliente declarou não ter mais informação sobre esses itens e nenhum documento novo chegou. Eles permanecem como **desconhecidos explícitos**, com as premissas documentadas abaixo — os números entregues não mudam em nenhum dos cenários.

1. **Estorno do crédito indevido (R$ 11.100,00) continua não espelhado — 3ª reiteração.**
   AJ-2026-03-001 é o formulário vigente; **postar um único estorno** (não acumular os três AJs). Até que o sistema registre, todo balancete novo deve ser testado (1.1.04 deveria ficar em R$ 472.527,00 no trimestre). Efeito fiscal permanece na competência **janeiro/2026** (a recolher 79.883,00). O pedido do diretor ("não mexe") está superado pelo fundamento legal (library/pis_cofins_uso_consumo.md) e pela confirmação do cliente ("papel e toner da sede").

2. **EFD-Contribuições/DCTF de 01/2026**: status de entrega segue **desconhecido** (cliente não tem a informação). Rotas em `mes_01/pis_cofins.json`; em qualquer cenário a retificação é na competência janeiro, nunca em março, e os valores mensais apurados não mudam.

3. **ICMS de março (183.400,00)**: mesma situação de jan/fev — sem memória de cálculo de créditos; mantido como registrado (7% líquido). Fora do escopo de ajuste do contrato.

4. **Arredondamento na apuração de IRPJ/CSLL (novo)**: os valores exatos IRPJ = 71.625,645 e CSLL = 42.975.387 têm fração de centavo e **a biblioteca fechada não traz regra de arredondamento**. Assunção declarada na memória e no lalur.json: arredondar ao centavo mais próximo (71.625,65 / 42.975,39); truncamento daria 71.625,64 / 42.975,38. Pergunta registrada em QUESTIONS.md (Q6). Impacto < R$ 0,01.

5. **Trava de 30% versus expectativa da diretoria (reiterado em memorando)**: o desejo de "compensar todo o prejuízo" (R$ 900.000,00) é legalmente inviável — compensado 204.644,70 (30% × 682.149,00), sobram 695.355,30 em cada saldo da Parte B (Lei 9.065/95, arts. 15–16; STF RE 591.340, Tema 117 — constitucional). Para compensar tudo num só trimestre seria preciso lucro ajustado ≥ R$ 3.000.000,00 (4,4× o trimestre atual). Pedido diretório registrado com a posição técnica em `deliverable/memorando_diretor_trava.md`: saldo não prescreve (biblioteca não fixa termo), trava renova por trimestre, recuperação total em ~4,4 trimestres no ritmo atual; valores de lalur.json inalterados. Penalidades de eventual compensação acima da trava: **não verificáveis no acervo fechado** — nada afirmado.

6. **Eventos não cobertos pela biblioteca (mantido como não verificado)**: eventual ICMS/IPI/ISS na entrega de brindes a clientes e IPI/ICMS na doação — sem autoridade citável no acervo; nada foi afirmado nem lançado.

7. **Reclassificação contábil (recomendação, não lançada)**: desdobrar 4.2.02 em subcontas "brindes" (48.000,00) e "doações" (30.000,00) para facilitar a extração do e-LALUR nos próximos trimestres.
