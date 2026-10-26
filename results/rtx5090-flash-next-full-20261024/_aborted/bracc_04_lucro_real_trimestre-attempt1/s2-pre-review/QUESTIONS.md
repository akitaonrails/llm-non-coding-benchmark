# Perguntas ao cliente

**Estado atual: SEM PERGUNTAS PENDENTES.** As duas perguntas que estavam abertas (registros de março/2026; status de transmissão das EFD-Contribuições jan/fev) foram respondidas na sessão 6 com "**no additional information**" — o cliente declara não possuir a informação. Elas ficam **ENCERRADAS** e NÃO serão reabertas (instrução: "do not repeat already answered questions"). Nenhuma pergunta já respondida foi reaberta em nenhuma sessão.

## Perguntas encerradas sem resposta útil (sessão 6) — consequência definitiva

1. **Registros de março/2026.** Resposta: o cliente **não tem informação adicional** (2ª vez — a 1ª foi na sessão 3). Consequência: o fechamento de 03/2026 e a apuração **definitiva** do 1º trimestre são impossíveis nesta base documental; o contrato veda inventar fatos. Os entregáveis de `mes_03/` (mês) foram lavrados como **marcadores BLOQUEADO** (`ajustes.json`, `pis_cofins.json`, `pendencias.md` — campos `null` = "não apurável", nunca zero) e o e-LALUR do trimestre (`mes_03/lalur.json`) permanece **PRELIMINAR jan+fev**, não utilizável para recolhimento ou escrituração definitiva. Se os registros de março surgirem algum dia, o checklist de fechamento já está pronto em `mes_03/ajustes.json` e `mes_03/pendencias.md`.
2. **Status de transmissão das EFD-Contribuições de 01/2026 e 02/2026.** Resposta: o cliente **não tem informação adicional**. Consequência: o item permanece como **desconhecido sinalizado** (não como pergunta aberta). Orientação condicional mantida: (a) se a EFD de janeiro foi transmitida **com** o crédito da NF-e 8812 (11.100,00): EFD retificadora + DARF complementar da diferença com acréscimos (`library/pis_cofins_uso_consumo.md`); (b) se ainda não transmitidas: transmitir já com os créditos corretos (jan 155.067,00; fev 157.509,00). Cabe ao cliente verificar internamente nas transmissões da EFD.

## Registro consolidado das respostas do cliente

| # | Pergunta (sessão) | Resposta do cliente | Uso no trabalho |
|---|---|---|---|
| 1 | NF-e 8812 (CFOP 1556) é uso/consumo ou ativo imobilizado? | "É uso e consumo. Não mexe nesse crédito." | Crédito estornado (AJ-2601-01), fundamentado em [library/pis_cofins_uso_consumo.md]. Classificação "uso e consumo" aproveitada contra a própria defesa do crédito. |
| 2 | Brindes se beneficiário é pessoa jurídica? | "Sim." | Mantida a adição da parcela de brindes ([library/lei9249_art13.md] §A). |
| 3 | O que compõe a conta 4.2.02 (R$ 85.000,00)? | "Vinho e canivete gravado pros 400 melhores clientes. Marketing, ora." | Premissa: 100% brindes (decomposição não informada — premissa sinalizada em `mes_03/memoria.md` §2 e `RELATORIO_FINAL.md` §7). |
| 4 | Crédito de energia (220.000,00) e aluguel (55.000,00)? | "Creditamos energia e aluguel." | Não aproveitados (lista taxativa) — [library/pis_cofins_uso_consumo.md] §1. |
| 5 | Receitas financeiras em conta 4.x? | "Não tem. Só venda de mercadoria." | Débito de PIS/COFINS confirmado em 234.950,00. |
| 6 | Valores de 13º/férias em 5.03.01/5.03.02? | "Isso é ajuste do ano anterior, entra assim mesmo." | Sem efeito em PIS/COFINS; custo dedutível contábil. |
| 7 | Existe folha/razoabilidade para brindes? | "Vinho e canivete gravado pros 400 melhores clientes." | Considerado sufficientemente respondido; risco de glosa por unrelatedness registrado (`mes_03/memoria.md` §2.1). |
| 8 | (Sessão 3) Existem balancetes/razões de fev/mar? Onde estão? | "No additional information." | Na sessão 3 gerou encerramento BLOCKED para fev+mar. **Parcialmente superada na sessão 4**: os registros de **fevereiro** foram entregues e o mês foi fechado; a pendência de **março** foi re-perguntada (linha 10 abaixo). |
| 9 | (Sessão 4) Fornecimento dos registros de fevereiro e determinação de fechamento. | Cliente entregou `documents/mes_02/` (razão, balancete acumulado, NF-e 4410, recibo de doação, relatório de auditoria interna) e ordenou "Feche o mês 02/2026". | Fevereiro **fechado**: `mes_02/ajustes.json`, `mes_02/pis_cofins.json` (a recolher 81.141,00), `mes_02/pendencias.md`; e-LALUR preliminar do trimestre atualizado para jan+fev em `mes_03/`. |
| 10 | (Sessão 5, encerrada na 6) Registros de março/2026 existem em algum lugar? | "No additional information." (sessão 6) | **ENCERRADA sem resposta útil.** Março confirmado inexistente pelo cliente (2ª vez). Entregáveis de `mes_03/` (mês) lavrados como marcadores BLOQUEADO; trimestre permanece PRELIMINAR; STATUS = **BLOCKED definitivo nesta base**. |
| 11 | (Sessão 5, encerrada na 6) EFD-Contribuições de 01/2026 e 02/2026 já foram transmitidas? | "No additional information." (sessão 6) | **ENCERRADA sem resposta útil.** Item convertido em desconhecido sinalizado; orientação condicional mantida (EFD retificadora + DARF complementar 11.100,00 se a EFD de jan saiu com o crédito da NF 8812). |

## Consequência registrada

- Fev/2026 está **fechado** (entregáveis acima). **Março/2026 não existe** na base documental e o cliente **confirmou duas vezes** não ter informação — fechamento de `mes_03` (mês) e apuração definitiva seguem bloqueados **em caráter definitivo nesta base**.
- A apuração de IRPJ/CSLL do 1º trimestre permanece **preliminar** (piso jan+fev em `mes_03/lalur.json`); cenários de sensibilidade (só março variável) em `RELATORIO_FINAL.md` §5.
- Se os registros de março surgirem, o checklist é o mesmo usado em janeiro/fevereiro (tie-out abertura+razões ⇄ balancete, PIS/COFINS não cumulativo 9,25%, varredura de indedutíveis do art. 13 da Lei 9.249/95) — já lavrado em `mes_03/ajustes.json` e `mes_03/pendencias.md`.
