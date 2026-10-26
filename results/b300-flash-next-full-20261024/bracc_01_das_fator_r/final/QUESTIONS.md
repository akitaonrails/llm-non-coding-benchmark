# Perguntas ao cliente — DAS maio/2026 (Lumen Soluções Digitais ME) — FASE ENCERRADA

Duas rodadas foram conduzidas e **respondidas**. Na 2ª rodada o cliente declarou **não ter
informação adicional** sobre nenhum dos pontos restantes (inclusive o único capaz de mudar o
Anexo) e não trouxe o comprovante de 30/04 que havia prometido. Nenhuma pergunta é repetida
aqui. Este arquivo passa a ser o **registro do que foi perguntado, do que foi respondido e
dos desconhecimentos que permanecem, explicitamente sinalizados** (numerados U1–U6, refletidos
em `STATUS.md`).

## O que foi respondido (não re-perguntado)

| Rodada | Pergunta | Resposta do cliente | Efeito no cálculo |
|---|---|---|---|
| 1 | Data do pró-labore de abril/2026 | **Pago em 30/04/2026** (dentro da janela); comprovante prometido | Folha 281.400 → **284.600**; Fator R 27,59% → **27,90%**; **Anexo V e DAS inalterados** (mesmo a data do e-mail manteria V) |
| 1 | Natureza do débito de 4.000 em 29/05 | Glosa parcial da NFS-e 1184, devolvida via PIX | Receita de serviços de maio = **78.000** (82.000 − 4.000) ✓ |
| 1 | Regularidade da NF-e 000.512 (locação) | Confirmada | Segregação em Anexo III sem ISS mantida ✓ |
| 1–2 | Todas as demais | **Sem informação adicional** | Premissas adotadas em definitivo (U1–U6 abaixo) |

## Desconhecimentos que permanecem (sinalização explícita)

- **U1 — Pró-labore da competência março/2026 (único risco de mudança de Anexo).** A linha
  2026-03 do resumo traz **zero**; perguntado duas vezes, o cliente não confirmou nem negou
  pagamento além do registrado. **Premissa adotada:** não houve pró-labore em março/2026.
  **Risco residual:** se existir pagamento ≤ 30/04/2026 não registrado, folha = 287.800 →
  Fator R 28,22% ≥ 28% → **Anexo III** e DAS total cairia de 15.188,84 para **10.261,08**.
- **U2 — Comprovante do pró-labore de abril (30/04/2026) não entregue.** Divergência com o
  e-mail do sócio ("6 de maio", débito ausente do extrato) registrada na memória §4 sem
  forçar reconciliação. **Sem efeito no resultado:** 30/04 → 27,90%; 06/05 → 27,59%; ambas
  em Anexo V.
- **U3 — Repartição do DAS do Anexo V indisponível na biblioteca.** Solicitada ao cliente,
  que não a possui. O campo `reparticao` do `apuracao.json` contém **apenas** a cota da
  locação (R$ 506,49 decomposta — verificável pela tabela do Anexo III); a decomposição dos
  serviços (R$ 14.682,35) **não é calculável** com a biblioteca. Não inventamos números.
- **U4 — Mecânica da exclusão do ISS na locação não desambiguada pela biblioteca.**
  Adotada a proporcional à alíquota **efetiva** (8,4415% → 506,49). Alternativa sobre a
  **nominal** (7,3059%) daria locação = 438,35 e total = **15.120,70** (−68,14). Premissa
  definitiva; memória §5.3.
- **U5 — Premissas de caixa da folha não confirmáveis.** Salários/pró-labore pagos no mês
  da competência; encargos (4.700/mês) com defasagem de 1 mês (padrão do extrato de maio);
  encargos de competência 04/2025 = 4.700 (valor constante na série, não documentado). Faixa
  de sensibilidade das leituras documentadas: 27,44%–27,90% — **nenhuma** altera o Anexo.
- **U6 — Tabela de repartição da biblioteca soma 99,85%** (cotas não-ISS da locação: 505,36
  vs 506,49 pagos, diff 1,13). Divergência da própria fonte; não forçamos reconciliação
  (memória §6).

## Premissas remanescentes sem confirmação (cliente nada informou)

Nenhuma receita de locação em mai/2025–abr/2026 (o `faturamento_12_meses.csv` não registra);
pró-labore dividido 2 × 1.600 (Renato e Julia); as 7 NFS-e recebidas integralmente (saldo do
extrato confere em 86.100,33) sem cancelamentos além do estorno de 4.000.
