# Perguntas ao cliente

**Estado atual: sem perguntas pendentes.**

Conforme instrução recebida ("do not repeat already answered questions"), nenhuma pergunta será reaberta. A última pergunta feita — se os balancetes/razões de fev/2026 e mar/2026 existem em algum lugar e onde estão — foi respondida pelo cliente com "no additional information", em três rodadas sucessivas. A pendência deixa de ser tratada como "aguardando resposta" e passa a **condição definitiva do encerramento**.

## Registro consolidado das respostas do cliente

| # | Pergunta (sessão) | Resposta do cliente | Uso no trabalho |
|---|---|---|---|
| 1 | NF-e 8812 (CFOP 1556) é uso/consumo ou ativo imobilizado? | "É uso e consumo. Não mexe nesse crédito." | Crédito estornado (AJ-2601-01), fundamentado em [library/pis_cofins_uso_consumo.md]. Classificação "uso e consumo" aproveitada contra a própria defesa do crédito. |
| 2 | Brindes se beneficiário é pessoa jurídica? | "Sim." | Mantida a adição da parcela de brindes ([library/lei9249_art13.md] §A). |
| 3 | O que compõe a conta 4.2.02 (R$ 85.000,00)? | "Vinho e canivete gravado pros 400 melhores clientes. Marketing, ora." | Premissa: 100% brindes (decomposição não informada — premissa sinalizada em `mes_03/memoria.md` §2 e `RELATORIO_FINAL.md` §7). |
| 4 | Crédito de energia (220.000,00) e aluguel (55.000,00)? | "Creditamos energia e aluguel." | Não aproveitados (lista taxativa) — [library/pis_cofins_uso_consumo.md] §1. |
| 5 | Receitas financeiras em conta 4.x? | "Não tem. Só venda de mercadoria." | Débito de PIS/COFINS confirmado em 234.950,00. |
| 6 | Valores de 13º/férias em 5.03.01/5.03.02? | "Isso é ajuste do ano anterior, entra assim mesmo." | Sem efeito em PIS/COFINS; custo dedutível contábil. |
| 7 | Existe folha/razoabilidade para brindes? | "Vinho e canivete gravado pros 400 melhores clientes." | Considerado sufficientemente respondido; risco de glosa por unrelatedness registrado (`mes_03/memoria.md` §2.3). |
| 8 | (Sessão 3) Existem balancetes/razões de fev/mar? Onde estão? | "No additional information." | Encerramento definitivo como **BLOCKED**; ver `RELATORIO_FINAL.md`. |

## Consequência registrada

- Fev/2026 e mar/2026 **não serão fechados** nesta base documental.
- A apuração de IRPJ/CSLL do 1º trimestre de 2026 permanece **preliminar** (piso em `mes_03/lalur.json`) e os cenários de sensibilidade estão em `RELATORIO_FINAL.md` §5.
- Se algum dia os registros surgirem, o checklist de fechamento de fev/2026 está pronto em `mes_02/pendencias.md` §2, e o mesmo se aplica a mar/2026.
