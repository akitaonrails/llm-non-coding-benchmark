# Pendências e ressalvas — fechamento 02/2026 (Atlas Distribuidora S.A.)

## 1. Estorno de janeiro não espelhado no sistema — refeita a baixa (AJ-2026-02-001)
- O balancete acumulado de fevereiro ainda trazia o crédito indevido: 1.1.04 = R$ 323.676,00 (= 166.167,00 de jan **sem estorno** + 157.509,00 de fev), e 4.2.04 = R$ 120.000,00 (deveria ser 131.100,00). O AJ-2026-01-001 proposto na sessão anterior não entrou no sistema contábil da empresa.
- Lançamento refeito em fevereiro (déb. 4.2.04 / créd. 1.1.04, R$ 11.100,00). Após o lançamento: 1.1.04 = R$ 312.576,00 ✓ (só créditos de mercadorias). O efeito fiscal (PIS/COFINS a recolher) continua sendo de **janeiro** (R$ 79.883,00), conforme `mes_01/pis_cofins.json`.
- **Ação para o cliente**: dar baixa do crédito na EFD-Contribuições e DCTF de **01/2026** (excluir o crédito, se ainda não transmitidas; retificar e recolher R$ 11.100,00 com acréscimos, se já transmitidas — status de entrega permanece desconhecido, sinalizado).

## 2. Brindes — localizados e quantificados: R$ 48.000,00 (NF-e 4410, Brindes Prime, 12/02/2026)
- "400 kits-presente (vinho + canivete gravado) para clientes — campanha 'Parceiros Atlas'" — é exatamente o fato que o cliente descreveu na sessão 1. Identificados em **fevereiro**, lançados em 4.2.02.
- **Premissa anterior substituida (retificação transparente)**: o teto de R$ 85.000,00 sobre a 4.2.02 de **janeiro** (premissa assumida por falta de documentos) está **superado**: os brindes são a NF 4410 de fevereiro; o relatório de auditoria interna de fevereiro ("brindes acima do padrão — R$ 48 mil em um único fornecedor... *sem outras observações*") não aponta brindes em janeiro. **Adição no e-LALUR do trimestre: R$ 48.000,00** (Lei 9.249/95, art. 13, VII — library/lei9249_art13.md).
- O rótulo "marketing" e a campanha de fidelização não afastam a vedação legal: é entrega de bens a clientes.

## 3. Doação Associação Beneficente Luz — R$ 30.000,00, indedutibilidade CONFIRMADA pelo cliente
- O próprio recibo informa que a entidade **não possui título de OSCIP nem certificação de utilidade pública federal** → não cabe a exceção do art. 13, §2º, II da Lei 9.249/95, que exige uma dessas qualificações (e teria limite de 2% do lucro operacional). O cliente confirmou na sessão 3: "não tem título nenhum". **Doação indedutível — adição no e-LALUR do trimestre: R$ 30.000,00** (Lei 9.249/95, art. 13, VI e §2º — library/lei9249_art13.md).
- O fato adicional trazido ("ONG do bairro", "o presidente conhece o dono") **não muda a conclusão**: a vedação decorre da ausência de título/certificação federal; vínculo pessoal não cria dedutibilidade que a lei não dá. (A biblioteca não traz regra específica sobre doações a entidades ligadas a administradores — nada além do art. 13 é afirmado aqui.)
- Item condicional anterior encerrado: não há certificação a trazer; a adição de R$ 30.000,00 está **fechada** para o e-LALUR.

## 4. Auditoria interna — recomendação atendida
- A auditoria pedia verificar "classificação contábil e eventuais reflexos" de brindes (R$ 48 mil) e doação (R$ 30 mil). Reflexo identificado: adições de R$ 78.000,00 no e-LALUR (nada muda na contabilidade societária — library/irpj_csll_trimestral.md). Recomendação de desdobrar a 4.2.02 em subcontas de controle — não forçada (não inventar plano de contas).

## 5. PIS/COFINS de fevereiro
- Débito 238.650,00 (2.580.000,00 × 9,25%) — confere com o razão; créditos permitidos 157.509,00 (mercadorias) — confere; **a recolher R$ 81.141,00**. Nenhum crédito indevido no mês; nada a estornar na apuração de fevereiro.

## 6. Trava de 30% — cenário projetado (para mes_03)
- Cumulado jan+fev: lucro líquido contábil corrigido R$ 321.566,00 + adições identificadas R$ 78.000,00 = R$ 399.566,00; compensação máxima pela trava (30%) = **R$ 119.869,80**, muito abaixo dos R$ 900.000,00. Mesmo com março, "compensar todo o prejuízo" exigiria lucro ajustado trimestral ≥ R$ 3.000.000,00 — a apuração final sairá em `mes_03/lalur.json` com a trava aplicada (Lei 9.065/95, arts. 15–16 — library/lei9065_art15_trava.md).

## 7. Conferências e desconhecidos sinalizados
- Razão de fevereiro em partida dobrada; balancete acumulado de fevereiro bate com o razão de janeiro + fevereiro **conta a conta** (verificado em Python; a única "divergência" era justamente o estorno de janeiro não espelhado, resolvida no item 1).
- ICMS fevereiro: 2.580.000,00 × 7% = 180.600,00 — confere com o registrado; memória de cálculo de créditos segue sem documentação (desconhecido remanescente, mantido como registrado).
- Tratamento de eventuais demais tributos sobre a saída de brindes para clientes (ex.: ICMS/IPI na remessa): **não abordado — a biblioteca não traz autoridade sobre o tema**; flag como não verificado, sem citação.
- 2.1.03 em 28/02: R$ 1.572.000,00 = 740.000,00 + 234.950,00 + 177.800,00 + 238.650,00 + 180.600,00 ✓.
