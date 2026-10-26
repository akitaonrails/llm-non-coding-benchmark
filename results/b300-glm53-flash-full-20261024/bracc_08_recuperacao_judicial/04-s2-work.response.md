A Sessão 2 já foi concluída em turnos anteriores — antes de reportar, vou conferir que os dois artefatos estão íntegros e finais:

A Sessão 2 já foi executada e está íntegra — verifiquei os dois artefatos agora (`sessao2/analise_plano.md` e `sessao2/efeito_tributario_desagio.json`, JSON validado, aritmética conferida em Python). Segue o resultado consolidado:

## Sessão 2 — veredictos cláusula a cláusula

| # | Cláusula | Veredicto | Fundamento (biblioteca) |
|---|---|---|---|
| 1 | Classe I — trab. integral em **18 meses** | **CONDICIONAL** — ilegal como escrita | art. 54, caput = teto de **1 ano** (18 excede em 6); §2º (até 2 anos) exige **garantias + aprovação da classe** — não constam da minuta (NÃO VERIFICADO). Recomendação: **voltar a ≤ 12 meses** |
| 2 | Classes III/IV — deságio 60%, 120×, carência 24m | **Não impugnado pela biblioteca** | Sujeição correta (art. 49, caput); nenhum texto da biblioteca teta deságio/prazo de quiro/ME-EPP. Votação em classes: **NÃO VERIFICADO** — cláusula depende de aprovação regular |
| 3 | Fiduciários "sujeitos ao plano, deságio 40%" | **ILEGAL** | art. 49, §3º — **propriedade fiduciária prevalece**; o Beta não se submete ao plano. Máquinas são bens essenciais (confirmado) → art. 6º, §4º veda venda/retirada até 08/09/2026. Cláusula deve **sair** |
| 4 | União "no plano": deságio 50%, **180×** | **ILEGAL em dois planos independentes** | (i) CTN 187 + art. 68 — crédito tributário **não se sujeita** ao plano (nula); (ii) **180× não existe** na Lei 10.522 — regimes: 120× / 30%+84× / transação ≤ 70% em 120m. Deletar a cláusula inteira; solução é **extraplanar** (Sessão 3) |
| 5 | Fonte — galpão via UPI, R$ 4,5 mi | **Legal com ressalva operacional** | art. 6º-B (afastamento da trava de 30% no ganho de capital) cobre **só alienação judicial**. Recomendação: venda por via judicial. Folga do plano: **952.000** (cai para **142.000** se transação da União a 70%, custo 810.000) |

**Síntese:** a minuta **não deve ser protocolada como está** — quatro ajustes: (i) trabalhistas a 12m ou §2º formalizado; (ii) cláusula fiduciária removida; (iii) cláusula da União removida; (iv) UPI conduzida por alienação judicial. O núcleo do deságio III/IV é conforme, desde que aprovado em classes.

## Efeito tributário do deságio (momento: homologação — novação, teste dos 10% do CPC 48 superado com folga)

- **Ganho nominal: R$ 3.882.000** — 2.520.000 (Alfa) + 1.110.000 (Norte) + 252.000 (Sul); conferido em Python. É **piso**: com taxa de desconto positiva, o PV das 120 parcelas cai e o ganho contábil **cresce** (taxa não informada — item 13; base nominal rotulada).
- **PIS/COFINS = 0** — art. 50-A, I: a receita do devedor fica fora da base de cálculo.
- **Trava de 30% NÃO se aplica ao ganho** — art. 50-A, II (limite dos arts. 42/58 da Lei 8.981 e 15/16 da Lei 9.065). **Atenção:** isso é only sobre o limite de compensação — o ganho **segue tributável** em IRPJ/CSLL.
- **IRPJ/CSLL = NAO_CALCULAVEL** — alíquotas/adicional não constam da biblioteca; qualquer percentual seria invenção. Base mínima nominal: 3.882.000.
- **Compensação de prejuízo = null** — saldo não informado (item 3); fórmula condicional documentada: limite = 30% × (lucro − ganho), com o ganho **excluído** da base do limite (interpretação rotulada).
- **Dedutibilidade** — art. 50-A, III: despesas das obrigações assumidas no plano (3.548.000) são dedutíveis. **Parágrafo único:** se houver dívida com **pessoas ligadas** (NÃO VERIFICADO), nada disso alcança essa parte.

Nada mudou no estado do trabalho: `STATUS.md` segue **COMPLETE WITH OPEN ITEMS** — Sessão 1 COMPLETE, Sessão 2 COMPLETE WITH OPEN ITEMS, Sessão 3 bloqueada nos itens 11–14 do QUESTIONS.md (via fiscal da União; alienação judicial do galpão; taxa de desconto; data da homologação). Sem resposta do cliente a esses itens, a Sessão 3 sairá com as lacunas rotuladas como assunção/não verificado — nunca re-perguntadas.