The library text confirms the prior treatment (locação → **Anexo III, deduzida a parcela de ISS 32,50%**, per SV 31). Now rewriting the deliverables with the client's answers applied:

Entrega finalizada. Os dois arquivos que ainda estavam na rodada 1 foram reescritos e o JSON foi validado.

## Resultado: DAS maio/2026 = **R$ 15.188,84** (mantido)

| Base | Valor |
|---|---|
| RBT12 (mai/25–abr/26) | 1.020.000,00 |
| Folha 12m | 284.600,00 (competência e pagamento convergem, após a resposta do pró-labore de 30/04) |
| Fator R | 27,90% < 28% → serviços no **Anexo V**, 4ª faixa: 20,50% − 17.100,00 → **18,8235%** |
| Serviços 78.000,00 | DAS **14.682,35** |
| Locação 6.000,00 | Anexo III com a parcela de ISS deduzida → **8,4415%** → DAS **506,49** |

Conferências em Python: 14.682,35 + 506,49 = 15.188,84; `apuracao.json` faz parse e todas as chaves do schema do contrato (inclusive `reparticao`) estão presentes.

## O que ficou aberto (sem repetir o que o cliente já respondeu)

**U1 — único item com efeito material.** A folha da janela é informada por resumo de **competência**, e a linha 2026‑03 está com `pro_labore = 0` sem explicação (a observação do cliente cobre abril). Limiar objetivo: folha paga ≥ **285.600,00** — margem atual de só **R$ 1.000,00**. Com a 12ª prestação na janela: folha 287.800,00 → fator R 28,22% → **Anexo III** → DAS **10.261,08** (−4.927,76). Fecha com extratos de mar/abr‑2026, folha de pagamento/DIRF, ou o comprovante de 30/04 (**não chegou** a `documents/`, hoje é alegação).

Sinal de alerta coerente com esse risco: o DAS de abr/2026 pago (10.480,22 = 12,05% dos 87.000,00 de abril) é compatível com Anexo III e incompatível com Anexo V.

**U2–U8 sinalizados como NÃO VERIFICADO NA BIBLIOTECA / não apurados:** composição do RBT12; classificação de consultoria e treinamento (as listas de anexos não existem na biblioteca — efeito do treinamento: −284,29); anexos de períodos anteriores; **repartição dos serviços (Anexo V) não apurada** — só existe a tabela do Anexo III, 4ª faixa, aplicada à locação; a tabela da biblioteca soma **99,85%** (componentes 505,36 vs. DAS locação 506,49, gap 1,13 — registrado, não corrigido); destaque de PIS/COFINS na NF‑e 512; CNAE/PGDAS‑D da locação e retenções de ISS.

Arquivos em `workspace/deliverable/`: `apuracao.json` (schema + cenários, premissas P1–P5, unknowns), `memoria.md`, `QUESTIONS.md` (U1–U8), `PERGUNTAS.md` (resumo PT), `STATUS.md` → **COMPLETE WITH OPEN ITEMS**.