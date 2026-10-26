# STATUS

**COMPLETE WITH OPEN ITEMS** (atualizado na rodada 2, após resposta do cliente)

Entregáveis em `deliverable/`:
- `apuracao_teste.json` — OK, atualizado na rodada 2 com a mensagem de rejeição confirmada pelo cliente e o alerta sobre o rollback do emissor (totais inalterados: débitos CBS 4.320,00 / IBS 480,00; créditos CBS 1.458,00 / IBS 162,00; saldos CBS 2.862,00 / IBS 318,00; recolhimento R$ 0,00). Soma das saídas R$ 480.000,00 bate com a base PIS/COFINS da apuração normal de agosto.
- `orientacao.md` — OK, atualizado: seção nova sobre o "contorno" do TI (rollback do emissor **não** regulariza) e plano de ação revisado (prioridade 1: reverter o rollback e atualizar o emissor para a NT 2025.002).
- `QUESTIONS.md` — rodada de perguntas encerrada: o cliente respondeu só à pergunta 1 (parcialmente) e declarou não ter mais informação; o que resta está sinalizado como **desconhecidos explícitos**, sem repetir perguntas. (`PERGUNTAS.md` opcional dispensado; conteúdo em `QUESTIONS.md`.)
- `STATUS.md` — este arquivo.

Open items (não conciliáveis com os materiais disponíveis — desconhecidos sinalizados):
1. **Números/chaves das duas NF-e rejeitadas**: o cliente confirmou apenas a mensagem ("Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"), que é exatamente a rejeição prevista no comunicado do CGIBS. As arquivadas 2308/2310/2312 são candidatas de mesmo perfil, mas os arquivos estão em homologação (`tpAmb=2`) e a identidade das rejeitadas **não foi confirmada**. Assunção mantida: nenhuma reemissão substitui as 12 saídas arquivadas.
2. **Destino das reemissões do emissor rebaixado**: não se sabe se as notas geradas sem o grupo IBSCBS chegaram a ser **autorizadas em produção**. Se sim → contraria o comunicado do CGIBS (anomalia a esclarecer com o autorizador); se não → aquelas vendas podem estar sem DFe autorizado. A biblioteca não descreve a consequência/procedimento. Verificação na lista de produção é a ação nº 2 do plano.
3. **Instrumento de regularização** das notas irregulares (2308, 2309, 2310, 2312) não está descrito na biblioteca — tratado como não verificado, não citado; cliente não tem orientação do fisco.
4. **Escopo da perda da dispensa** (mês inteiro × só operações irregulares) não definido na biblioteca — sinalizado na condição de dispensa do JSON e na orientação; exposição máxima tratada como teto (saldo integral 2.862,00 + 318,00).
5. **Completude da carteira** de agosto (NFS-e nacional, CT-e, devoluções) não confirmada — assunção: exatamente as NF-e 2301–2317.
6. **Origem sistemática do erro de alíquotas da NF-e 2309** presumida (configuração do emissor) — não confirmada; possíveis outras notas afetadas fora do conjunto recebido não verificáveis.
