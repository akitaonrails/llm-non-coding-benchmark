# Nota à sócia — contrato NexaClin (Clínica Aurora)

**Resumo em uma linha:** o medo maior (foro) não existe; os riscos reais estão nos dados, no prontuário e em duas travas financeiras. Não assine a minuta como está — mas os ajustes são factíveis em 10 dias.

## 1. O foro de Florianópolis NÃO pode ser anulado pelo CDC — a colega está errada

- O Código de Defesa do Consumidor só protege a **relação de consumo**. A clínica contrata o software como **insumo da sua atividade** (prontuário, agenda, faturamento) — não é destinatária final. É a "teoria finalista" do STJ. A flexibilização ("finalista mitigada") exige vulnerabilidade técnica, jurídica ou econômica **demonstrada**, o que **não se presume** em sociedade com R$ 9,2 mi de faturamento assessorada por advogado. Consequência: **o art. 51 do CDC (nulidade de cláusulas abusivas, inclusive de foro) não se aplica a este contrato** (`library/cdc_art51_distrator.md`). Os pacientes da clínica não são partes deste contrato, o que também não abre a porta do CDC.
- Entre empresas, a cláusula de eleição de foro é **válida** se constar de instrumento escrito e citar o negócio — é o caso (CPC art. 63 e §1º; STJ, REsp 1.707.855/SP, citado em `library/cc_contratos_empresariais.md`). A checagem de ofício pelo juiz (CPC art. 63, §3º) existe para contratos de adesão com parte vulnerável — não é a nossa situação, e tentar o caminho da "vulnerabilidade" contradiria a cláusula 15.
- **Na prática:** se litigar em SC for inaceitável, isso se resolve **negociando agora** (foro da sua sede ou arbitragem), não com promessa de anulação futura. Juridicamente, porém, o foro não impede a assinatura — avaliação "aceitável".

## 2. Dados: aqui sim está o problema central (cláusula 5 → substituir pelo Anexo A)

A cláusula atual da NEXA tem três defeitos graves para quem vai colocar **prontuário e exames** no sistema (dados sensíveis de saúde — LGPD art. 5º, II):

1. **"Pesquisa e desenvolvimento de produtos" com os SEUS dados.** Vocês são a **controladora** (donas das decisões) e a NEXA é **operadora** (art. 5º, VI e VII): ela só pode tratar os dados **seguindo as instruções de vocês** (art. 39). Usar os dados para desenvolver produto próprio é finalidade dela, sem base legal — e a LGPD **veda** compartilhar dado sensível de saúde entre controladores para obter vantagem econômica (art. 11, §4º), exceto hipóteses de assistência e de faturamento, que não incluem "desenvolvimento de produto". "Anonimizado/agregado" não salva: se a reversão for possível com esforços razoáveis, o dado continua pessoal (art. 12) — e base agregada de ~22 mil pacientes raramente é irreversível (análise em `library/lgpd_excertos.md`). **Corte essa permissão do contrato.**
2. **Servidores "no Brasil ou no exterior" à escolha da NEXA.** Transferência internacional só é permitida nas condições do art. 33 (país adequado, cláusulas-padrão etc.). O Anexo A exige aviso prévio + enquadramento no art. 33; sem aviso, dados só no Brasil. Com a sua resposta, isso deixou de ser hipótese e virou fato — ver seção 2-A logo abaixo.
3. **Operadoras de saúde (Unimed, Bradesco): podem, sem medo — para faturar.** O compartilhamento para **faturamento/cobrança/auditoria TISS** é expressamente permitido pelo art. 11, §4º (transações administrativas em benefício do titular). O Anexo A limita a integração a essa finalidade. Base legal para o tratamento principal: **tutela da saúde por serviços de saúde** (art. 11, II, "f") — não precisamos de consentimento dos pacientes para operar o sistema, e é melhor assim (consentimento revogável travaria o serviço).

O texto completo do que inserir (papéis, bases legais, instruções, subcontratação, transferência internacional, incidentes, término/portabilidade, auditoria) está em `clausula_dados.md` — é para substituir a cláusula 5 inteira.

**Incidentes:** se a NEXA sofrer vazamento, a comunicação à ANPD e aos pacientes é **dever de vocês, controladoras, em 3 dias úteis** (Res. CD/ANPD 15/2024, via `library/lgpd_excertos.md`). Por isso o Anexo obriga a NEXA a avisar vocês em até 24 h.

## 2-A. Fatos novos da sua resposta (24/10) — e o que mudam

1. **Hospedagem AWS "provavelmente" nos EUA.** Deixou de ser hipótese de contrato e passou a ser transferência internacional potencial real. A LGPD só admite transferência nas hipóteses do art. 33 (país/organismo com nível adequado, cláusulas-padrão ou garantias equivalentes). A biblioteca de referência **não confirma que os EUA tenham nível adequado — não verificado**, e ninguém planeja dados de saúde em cima de "provavelmente". Regra prática já escrita no Anexo A (item 13-A): **até a NEXA demonstrar por escrito a região exata e a hipótese do art. 33 aplicável, os dados ficam só no Brasil e a migração não começa.** O ônus da demonstração é da NEXA — não estamos vedando a AWS, estamos exigindo AWS regularizada antes do primeiro prontuário migrado.
2. **Migrar 22 mil prontuários é projeto de meses e "sair no meio seria caótico".** Isso milita a favor de vocês nas duas pontas. *Entrada:* o contrato precisa de plano de migração com cronograma e critérios objetivos de aceite, com o sistema legado em paralelo até a aceitação escrita — por isso propusemos a nova **cláusula 1-A (Migração e Reversibilidade)** em `clausulas.json`, com rescisão sem multa da cláusula 10 se a migração fracassar por culpa da NEXA. *Saída:* justamente porque trocar de sistema é caro e lento, não dá para aceitar renovação automática de 36 em 36 meses, multa de 100% das vincendas e exportação só por 30 dias — é por isso que as cláusulas 3, 7 e 10 estão na lista de correção, e o Anexo A agora garante **exportação integral a qualquer tempo durante a vigência**, não só no fim.
3. **Faturamento com operadoras é essencial — confirmado.** Ótima notícia jurídica: é exatamente a hipótese expressamente permitida pelo art. 11, §4º, da LGPD (transações de faturamento/cobrança/auditoria em benefício do titular). O Anexo A (item 6) autoriza essa integração desde o primeiro dia — nada no contrato proposto trava o faturamento com Unimed/Bradesco; só se documenta a finalidade de cada integração.

## 3. Prontuário: "CSV por 30 dias" é incompatível com o dever de guarda (cláusula 7)

O prontuário **pertence ao paciente**, sob a **guarda** da clínica, pelo prazo mínimo de **20 anos** do último registro (Res. CFM 1.821/2007; Lei 13.787/2018; Res. CFM 2.299/2021 — `library/cfm_prontuario.md`, que aponta expressamente a incompatibilidade do prazo de 30 dias). Se um ex-paciente pedir o prontuário no ano 12, um CSV de 30 dias não nos salva. Proposta: exportação **completa** (inclusive anexos), em formato estruturado, **gratuita**, disponível por **180 dias** + assistência de migração.

## 4. Não concorrência (cláusula 13): cláusula sem causa — exigir a retirada

Proibir a clínica, por **5 anos**, em **todo o Brasil**, de "utilizar software concorrente", com multa de **R$ 500.000** (5,4% do faturamento), é o pior tipo de cláusula segundo o STJ: sem limite territorial, prazo desproporcional (o razoável em regra é até 2 anos) e, num contrato de licença, **inverte a lógica** — quem tem know-how a proteger é a NEXA, não vocês (REsp 1.203.109/MG; REsp 680.815/PR — `library/stj_nao_concorrencia.md`). Em juízo ela cairia, mas ninguém quer um processo com R$ 500 mil em jogo nem ficar 5 anos sem poder trocar de sistema. **Pedir supressão.**

## 5. Dinheiro: as duas travas e o teto de responsabilidade (cláusulas 2, 3, 8 e 10)

Cálculos (3 unidades × R$ 6.900 = **R$ 20.700/mês**; **R$ 248.400/ano** = 2,7% do faturamento):

| Item | Aritmética | Valor |
|---|---|---|
| Custo ano 1 | 48.000 + 12 × 20.700 | **R$ 296.400** |
| Custo 36 meses (sem reajuste) | 48.000 + 36 × 20.700 | **R$ 793.200** |
| Multa da cláusula 10 (24 meses vincendas) | 24 × 20.700 | **R$ 496.800** |
| Multa no pior caso (renova + denuncia logo) | 36 × 20.700 | **R$ 745.200** (8,1% do faturamento) |
| Teto de responsabilidade da NEXA | 3 × 6.900 = 20.700 **ou** 3 × 20.700 = 62.100 (texto ambíguo) | **0,23%–0,68% do faturamento** |
| Teto por paciente | 20.700 ÷ 22.000 = 0,94; 62.100 ÷ 22.000 = 2,82 | **R$ 0,94–R$ 2,82/paciente** |
| SLA 99% admite parada de | 8.760 h × 1% = 87,6 h | **≈ 3,6 dias/ano**, com crédito máximo de R$ 2.070/mês |

Pedidos proporcionais (não é "tudo ou nada"): reajuste só por índice fixo (hoje "IGP-M **ou outro índice a critério da NEXA**" — preço ao arbítrio dela contraria a boa-fé objetiva, CC art. 422); denúncia com aviso de 90 dias em vez de 180, sem renovação automática de 36 em 36 meses; multa da cláusula 10 **degressiva e limitada ao prejuízo comprovado** (o art. 413 do CC permite ao juiz reduzir multa manifestamente excessiva — mas depender de juiz não é plano); teto da cláusula 8 com excessões para **violação de dados, sigilo e PI** — num vazamento, os pacientes podem cobrar solidariamente de vocês e da NEXA (LGPD art. 42, §1º, I), e hoje o teto deixaria quase toda a conta com a Aurora.

## 6. Deveres nossos, independentemente do contrato

- **Encarregado (DPO):** a LGPD define o encarregado (art. 5º, VIII); ainda que os detalhes de dispensa de indicação não estejam verificáveis na biblioteca, recomendo indicar formalmente um nome — é condição para o Anexo A funcionar (canal de incidentes e pedidos de titulares).
- **Política de privacidade** específica (a atual é genérica) e **registro das operações** (art. 37), que o Anexo exige também da NEXA.
- Os contratos/integrações com Unimed e Bradesco para faturamento têm respaldo no art. 11, §4º — mas documente a finalidade de cada integração.

## 7. Plano para assinar em 10 dias

1. **Dias 1–2:** contraproposta com (a) Anexo A (`clausula_dados.md`) substituindo a cláusula 5; (b) supressão da cláusula 13; (c) cláusula 7 (exportação 180 dias/estruturada, + exportação sob solicitação na vigência); (d) cláusula 12 (subcontratação com comunicação, formalizando a Amazon/AWS); (e) nova cláusula 1-A (migração e reversibilidade). **Junto com a contraproposta, exigência por escrito:** região exata da hospedagem AWS, contrato da NEXA com a Amazon como subcontratada, demonstração da hipótese do art. 33 da LGPD aplicável e certificações de segurança — sem isso, nada de dados fora do Brasil e migração não começa.
2. **Dias 3–6:** negociar cláusulas 2, 3, 8 e 10 (índice, vigência, teto, multa degressiva).
3. **Dias 7–9:** indicar encarregado, conferir política de privacidade, validar tecnicamente o formato de exportação (prontuário + anexos) e revisar o plano de migração e o cronograma apresentados pela NEXA (cláusula 1-A).
4. **Dia 10:** assinatura — apenas se os quatro itens "altos" (5, 7, 12, 13 + Anexo A) estiverem resolvidos. Itens médios/baixos podem virar aditivo posterior, se necessário.

*Nada nesta nota depende do CDC — e é importante que a negociação não dependa: como explicitei no item 1, não podemos contar com ele.*
