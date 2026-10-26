

Client confirmed the root cause — the SEFAZ rejection was the correct NT 2025.002 enforcement, and TI deliberately bypassed it by reverting the emitter version. This strengthens the irregularity narrative (intentional workaround, not a glitch). I'll fold this into the deliverables and convert the remaining questions into explicitly flagged unknowns. Numbers are unaffected.






Agora vou reescrever o `PERGUNTAS.md` registrando a resposta e declarando os ignorados remanescentes:





Corrigindo um typo que escapou no texto:





Validação final — rodar o cálculo de novo, validar o JSON e conferir referências cruzadas nos entregáveis:





A asserção do schema falhou — vou inspecionar as chaves reais do JSON:





O JSON está truncado/incompleto — faltam 6 chaves obrigatórias do escopo do contrato. Vou ler o arquivo inteiro para avaliar o dano:





Sem lastro nos documentos para a frase sobre "480,00" — vou removê-la. Reescrevendo o gerador com o parser correto:





Simplificando o parser do grupo IBSCBS (a versão com lambdas está frágil):





O CNPJ 23.456.789/0001-50 não existe em nenhuma fonte — o verificado nos 17 XMLs é 27.119.804/0001-30 (o `emit` de todas as notas). Corrigindo o gerador e o STATUS:






Tudo consistente. Trabalho concluído — resumo desta rodada:

**Resposta do cliente incorporada**
- `orientacao.md` §§3–4: causa-raiz registrada — a rejeição era o bloqueio correto do Comunicado CGIBS e o "contorno" do TI (reverter a versão do emissor) foi **workaround deliberado**, não falha; orientação de correção nº 1 agora é *desfazer o rollback* e migrar para o leiaute da NT 2025.002.
- `PERGUNTAS.md` reescrito: resposta da pergunta 2 registrada (não será re-perguntada) e os pontos sem informação viraram **4 ignorados declarados** com seus efeitos (integralidade dos tpAmb=2; circulação das 2308/2310/2312; regime das fornecedoras; procedimento de regularização e extensão da perda da dispensa — exposição R$ 3.180,00).
- `STATUS.md` atualizado: **COMPLETE WITH OPEN ITEMS**, números inalterados.

**Problemas que encontrei e corrigi ao validar**
1. `apuracao_teste.json` tinha sido sobrescrito por uma versão de rascunho com schema errado (faltavam `empresa`, `cnpj`, `chave`, `status_destaque` etc.). Reconstruí o gerador em `workspace/tools/gerar_apuracao_teste.py` (persistente e re-executável — o script anterior estava em /tmp e se perdeu) e regenerei o JSON no schema completo do contrato, com a confirmação do cliente embutida nas observações das notas irregulares. Validação integral passou: 12 saídas + 5 entradas, débitos linha a linha = 0,9%/0,1% da base, totais e saldo amarrados, base R$ 480.000,00 conferindo com a apuração PIS/COFINS.
2. **CNPJ divergente**: o valor 23.456.789/0001-50 usado antes não consta de nenhuma fonte. Corrigi JSON e STATUS para **27.119.804/0001-30**, o `emit` verificado em todas as NF-e emitidas (como já constava na orientação).
3. Removi das observações uma frase sobre "IBS de creditamento de 480,00" que não tem lastro nos documentos.

**Números finais (inalterados):** CBS débito 4.320,00 / crédito 1.458,00 / saldo 2.862,00; IBS 480,00 / 162,00 / 318,00; recolhimento devido R$ 0,00 (dispensa condicional); irregulares 2308, 2309, 2310, 2312.