

Client answered two items and confirmed there's no further information on the rest. This resolves the "divergence" root cause (SEFAZ *was* rejecting; the TI rollback is why group-less notes started passing) and confirms Ponto Fixo's Simples status. Updating the deliverables accordingly — numbers don't change (rejected notas are not authorized documents; the saidas base already ties to the ledger).





Now updating `QUESTIONS.md`, `PERGUNTAS.md` and `STATUS.md` to reflect answered items and flag the remaining unknowns.





Respostas do cliente absorvidas. Resumo do que mudou e o que fica sinalizado:

**O que as respostas confirmaram (sem mudar os números):**
- A rejeição *"Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"* prova que a regra de rejeição do Comunicado CGIBS **está valendo** na SEFAZ — e o "contorno" do TI (retorno de versão do emissor) é a **causa raiz** das 2308/2310/2312 terem saído sem grupo e sido autorizadas. `orientacao.md` §3.2, §5 e plano de ação §6.2 agora dizem isso explicitamente: desfazer o rollback (a versão que emitia certo já existiu — 2306/2307/2311), cancelar/reemitir as 4 irregulares; autorização obtida por contorno não sana o documento (art. 346).
- Rejeição **não gera documento fiscal**: as duas tentativas rejeitadas não entram na apuração — e as operações subjacentes parecem cobertas pelas 12 autorizadas (480.000,00 amarra exatamente com PIS 3.120,00 + COFINS 14.400,00 do livro). Parágrafo novo no §3.2 com a contingência: se surgir documento *autorizado* não enviado, refazer.
- Ponto Fixo (Simples) confirmado — o tratamento da NF-e 2315 (sem destaque → **sem crédito**, art. 347) já estava correto e segue inalterado; nota de confirmação no §4.

**Desconhecidos explicitamente sinalizados** (cliente não dispõe de mais informação — listados em `QUESTIONS.md`/`PERGUNTAS.md` e `STATUS.md`):
1. Números/chaves das duas tentativas rejeitadas — sem XML, sem registro no cliente; sem efeito nos totais pela razão acima.
2. Premissa mantida: regime regular da Logística Atlas (NF 2316), por `CRT=3` + destaque no XML; se cair, saldos viram CBS 3.222,00 / IBS 358,00.
3. Premissa de completude do conjunto de agosto, sustentada apenas pela conciliação com o livro.

**Arquivos:** `apuracao_teste.json` inalterado e ainda validado (schema + parse); `orientacao.md` atualizado em 4 pontos; `QUESTIONS.md`, `PERGUNTAS.md` e `STATUS.md` reescritos. Status final: **COMPLETE WITH OPEN ITEMS** — os itens abertos são os três desconhecidos acima, nenhum dos quais altera os totais entregues: débitos 4.320,00/480,00, créditos 1.458,00/162,00, saldos 2.862,00/318,00, recolhimento 0,00 sob a condição do ADCT art. 125 §4º.