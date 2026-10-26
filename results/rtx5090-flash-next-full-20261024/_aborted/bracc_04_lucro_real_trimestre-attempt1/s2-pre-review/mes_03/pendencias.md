# Pendências — março/2026

## Status do mês: **BLOQUEADO — registros INEXISTENTES, confirmado pelo cliente**

Março/2026 **não possui registros na base documental**: não existe `documents/mes_03/` (não há razão, balancete, nota fiscal, recibo ou extrato do mês). A pergunta foi feita formalmente em `../QUESTIONS.md` e o cliente respondeu, **em duas rodadas distintas (sessões 3 e 6)**, que **não tem informação adicional**. Portanto:

- Os campos de `ajustes.json` e `pis_cofins.json` deste mês estão como `null` (**não apurável**) — preenchê-los com qualquer número, inclusive zero, seria **inventar fatos**, expressamente vedado pelo contrato.
- O fechamento mensal de 03/2026 e a apuração **definitiva** do IRPJ/CSLL do 1º trimestre são **impossíveis nesta base documental**. O e-LALUR em `../lalur.json` permanece **PRELIMINAR (jan+fev)** e não pode ser escriturado nem embasar recolhimento.
- Este arquivo e os dois JSON do mês existem para que a estrutura contratual de entregáveis (ajustes + pis_cofins + pendências por mês) esteja completa e documente exatamente o que falta e por quê.

## O que está FIRME apesar do bloqueio de março

| Item | Valor | Fonte |
|---|---|---|
| PIS/COFINS a recolher jan/2026 (DARF em aberto) | 79.883,00 | `../mes_01/pis_cofins.json` |
| PIS/COFINS a recolher fev/2026 (DARF em aberto) | 81.141,00 | `../mes_02/pis_cofins.json` |
| Total PIS/COFINS não recolhido jan+fev | **161.024,00** | soma acima; passivo 2.1.03 acumulado fev = 1.572.000,00 (amarração verificada) |
| e-LALUR preliminar (piso jan+fev): lucro real | 339.196,20 | `../lalur.json` |
| IRPJ preliminar (15% 50.879,43 + adicional 27.919,62) | 78.799,05 | idem — NÃO usar para recolhimento |
| CSLL preliminar (9%) | 30.527,66 | idem |
| Saldo de prejuízo a compensar após jan+fev (Parte B) | 754.630,20 | idem (trava de 30% — `library/lei9065_art15_trava.md`) |

## Itens abertos (carregados de janeiro/fevereiro — permanecem abertos)

1. **AJ-2601-01 ainda NÃO escriturada** (estorno do crédito indevido da NF-e 8812, 11.100,00, data 31/01/2026). Evidência no último balancete existente (fev, acumulado): 1.1.04 = 323.676,00, deveria ser 312.576,00. Reiterada três vezes (`../mes_01/ajustes.json`, `../mes_02/ajustes.json`, `./ajustes.json`). Orientação da diretoria ("não mexe nesse crédito") não afasta o crédito indevido — fundamento em `library/pis_cofins_uso_consumo.md`.
2. **Status de transmissão das EFD-Contribuições jan/fev: DESCONHECIDO — pergunta encerrada sem resposta útil** (cliente não tem a informação). Risco a verificar internamente pelo cliente: se a EFD de jan/2026 foi transmitida COM o crédito da NF-e 8812, é necessária EFD retificadora + DARF complementar de 11.100,00 com acréscimos; se ainda não transmitidas, transmitir já com os créditos corretos (jan 155.067,00; fev 157.509,00).
3. **DARFs de PIS/COFINS jan (79.883,00) e fev (81.141,00) não recolhidos** — nada foi pago (2.1.03 termina fev em 1.572.000,00). Acréscimos de mora **não calculáveis** com a biblioteca autorizada; calcular quando houver confirmação das datas de recolhimento.
4. **Decomposição dos 85.000,00 de 4.2.02 em janeiro**: premissa adotada de 100% brindes (resposta do cliente "vinho e canivete gravado pros 400 melhores clientes" + consistência com a NF-e 4410 de fev); decomposição formal não informada — premissa registrada proeminentemente em `../mes_03/memoria.md` §2 e `../RELATORIO_FINAL.md` §6.
5. **Notas fiscais de compras jan/fev** não entregues: créditos de 155.067,00 (jan, já líquido do estorno) e 157.509,00 (fev) aceitos com base no razão/balancete; documentos de suporte pendentes.
6. **Extratos de aplicação financeira** não entregues (receitas financeiras 27.800,00 jan + 27.800,00 fev reconhecidas pelo razão).
7. ICMS (jan 177.800,00; fev 180.600,00) permanece fora do escopo dos entregáveis; usado apenas na amarração do passivo 2.1.03.

## Checklist para fechar março SE os registros surgirem algum dia

(cópia navegável; mesma lavrada em `./ajustes.json`)

1. Tie-out: `balancete_abertura.csv` + razão de jan (sem linhas ABERT) + razões de fev e mar devem reproduzir o balancete acumulado de março; conferir equilíbrio débito=crédito.
2. Amarrações-padrão: 2.1.03 (PIS/COFINS + ICMS mês a mês) e 1.1.04 (créditos — deve já conter o estorno AJ-2601-01 se escriturado).
3. PIS/COFINS março: débito 9,25% × receita; varredura de créditos por item (somente insumo/revenda; rejeitar uso e consumo, energia, aluguel — `library/pis_cofins_uso_consumo.md`).
4. Varredura de indedutíveis do art. 13 da Lei 9.249/95 (`library/lei9249_art13.md`) nas contas 4.2.x de março: adições no e-LALUR sem alterar a contabilidade.
5. Atualizar `./lalur.json` e `./memoria.md` para a versão DEFINITIVA do trimestre e recalcular a Parte B (prejuízo a compensar) — ver sensibilidade já calculada em `../RELATORIO_FINAL.md` §5.

## Consequência para o engajamento

Enquanto os registros de março/2026 não existirem, o engajamento permanece **BLOCKED** (`../STATUS.md`): falta entregável obrigatório (fechamento de 03/2026) e a apuração trimestral é inexoravelmente parcial — o contrato veda reportar completo quando falta entregável. As duas perguntas que ainda estavam abertas foram **encerradas na sessão 6** com a resposta "no additional information" — ver `../QUESTIONS.md`.
