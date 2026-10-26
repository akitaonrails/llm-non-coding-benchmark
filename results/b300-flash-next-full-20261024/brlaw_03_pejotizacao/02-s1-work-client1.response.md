

Client reply received. The director's assertion is exactly the defense argument registered in `verbas_e_calculo.md` ("salvo prova de que embutia tributos/custos"). Let me quantify the 12k scenario properly before updating the deliverables.





Numbers verified. The key legal point: the library treats "base = valor pago à PJ" as the presumption, rebuttable only by **prova** of embedded taxes/costs — an unsupported assertion doesn't rebut it. I'll keep the main case at R$ 18k, quantify the 12k scenario, and update all deliverables.





Now inserting §6.1 and updating §7/§8. First let me check §0 (resumo executivo) for consistency:





Now rewrite `QUESTIONS.md` for round 2 (don't re-ask answered/no-info items):





All checks pass. One last consistency touch — add the 12k scenario as a row in the §6 sensitivity table pointing to §6.1:





Rodada 2 concluída. Resumo do tratamento da resposta do diretor:

## Análise da alegação "CLT equivalente = 12 mil"

**Não altera o caso central.** A biblioteca (`verbas_e_calculo.md`) trata "base = valor pago à PJ" como **presunção, salvo prova** de tributos/custos embutidos — e a frase do diretor é asserção de parte interessada sem nenhum lastro documental. Motivos adicionais registrados no parecer (§6.1):

- A cláusula 2ª pagava quantia fixa *"independentemente de entregas"*, sem prestação de contas ou reembolso — estrutura que contradiz a tese de repasse de custos;
- O overhead alegado seria 33,3% do faturamento (6k/18k) — ordem de grandeza implausível, mas sinalizado **[não verificado]** (conhecimento geral, fora da biblioteca);
- **Espada de dois gumes**: dizer que o mesmo posto vale ~12 mil como CLT admite função permanente no negócio — piora a responsabilidade e dá benchmark salarial ao reclamante.

## Números (aritmética verificada em Python)

| | 18k (central) | 12k (alegação) | Δ |
|---|---|---|---|
| Verbas 2–7 | 665.584 | **443.722,67** | −221.861,33 |
| HE comprovadas (135 h) | 16.568,18 | 11.045,45 | −5.522,73 |
| Provisão pontual | **682.152 (mantida)** | ≈ 454.768 | — |

Ponderações ilustrativas: 85/15 → ≈ 648 mil; 75/25 → ≈ 625 mil — defensáveis **só se** a empresa produzir contabilidade/declarações fiscais da PJ.

## Arquivos atualizados (`workspace/deliverable/`)
- **parecer.md** — novo §6.1 com a análise completa; §0, quadro de sensibilidades, §7 (provisão), §8 (defesa/acordo) atualizados. Provisão 682.152 e faixa 500–700 mil **mantidas** (a alegação ancoraria no máximo o *piso* da faixa).
- **parecer.json** — números inalterados; 8º fundamento registra a presunção mantida e remete o cenário-12k ao §6.1. Parse/soma re-validados.
- **QUESTIONS.md** — reescrito: nada re-perguntado; **uma única pergunta nova** (Q-A: documentos que provem a alegação — com recomendação de *não* explorar a tese em negociação se não existirem, dado o efeito confissional); tabela dos 7 **desconhecidos confirmados** + deliberação de acordo pendente.
- **STATUS.md** — **COMPLETE WITH OPEN ITEMS**, com o que mudou e o que permaneceu.

Ponto de atenção para o cliente: sem os documentos da Q-A, a alegação dos 12 mil só existe como argumento vazio — e o gatilho do protocolo (16/11/2026) continua sendo o relojoeiro da decisão de acordo.