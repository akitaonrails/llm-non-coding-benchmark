Sessão 5. Lendo as duas fontes de biblioteca relevantes na íntegra antes de fechar os números:

Fontes confirmadas: cobertura de **130%** (Portaria PGFN 164/2014: débito atualizado "acrescido de 30%"), custos típicos seguro 0,8–1,5% a.a. / fiança 2–3% a.a., transação de até 65% sobre multa/juros/encargos limitada ao principal, com confissão e desistência de defesas — e "não se transaciona débito decaído". A biblioteca **não traz tabela SELIC mensal**, então a atualização fica rotulada. Fechando os números:

Agora as atualizações de acompanhamento:

Conferência final da estrutura entregue:

**Sessão 5 entregue** — `deliverable/sessao5/garantia.json` (JSON válido, chaves exatamente conforme o schema do contrato; aritmética conferida por script).

## Números fechados

| Grandeza | Valor | Origem |
|---|---|---|
| Débito remanescente | **R$ 591.000** (302k + 289k) | decadência já afastou os 509k |
| Cobertura exigida (seguro/fiança) | **R$ 768.300** = 591.000 × 1,30 | Portaria PGFN 164/2014: "acrescido de 30%" |
| Custo anual seguro-garantia | R$ 6.146–11.525 (ponto médio **8.835**) | 0,8–1,5% a.a. sobre a apólice |
| Custo anual fiança | R$ 15.366–23.049 (ponto médio **19.208**) | 2–3% a.a. |
| Base de transação | **R$ 591.000** (os 509k decaídos ficam fora — a fonte veda transacionar débito decaído) | transacao_pgfn.md |
| Desconto estimado (piso) | **R$ 164.636** = 65% × multa 253.285,71 (multa = 591.000 − 591.000÷1,75) | abaixo do teto legal (desconto ≤ principal 337.714) |

**Recomendação** (registrada no JSON): **seguro-garantia** em vez de fiança (~R$ 10 mil/ano de economia + não consome limite bancário); **não aderir à transação agora** — adesão implica confissão irrevogável e desistência das defesas sobre o débito incluído, o que mataria a exceção de decadência e os embargos. Sequência: garantia reescalada → embargos (30 dias da garantia) + sustentar a extinção dos 509k → transação só do resíduo, após a decisão.

## Ressalvas rotuladas (não verificáveis na biblioteca)
- **SELIC**: a biblioteca não traz tabela mensal → 591.000/768.300/164.636 são **pisos sem atualização**; a planilha PGFN/CDAP deve ser obtida e tudo reescalado antes de contratar ou aderir (nova pendência 8 em `QUESTIONS.md`/`STATUS.md` — obtenção pelo escritório, não pergunta ao cliente).
- Decomposição principal/multa (÷1,75) parte da premissa multa 75% = art. 44 I, a confirmar no inteiro teor do AI (pendência 3 já existente).

## Livro-razão atualizado
- `STATUS.md`: cabeçalho agora **Sessões 1 a 5**, bloco da Sessão 5 detalhado, e seção final substituída por "Próximo passo (pós-entrega das 5 sessões)" — as cinco sessões do contrato estão concluídas; status global permanece **COMPLETE WITH OPEN ITEMS** (pendências documentais 1–3 e 6–8 seguem rotuladas como premissas nas peças).
- `QUESTIONS.md`: nova pendência 8 (planilha SELIC), marcada como item de obtenção documental, sem re-perguntar ao cliente.