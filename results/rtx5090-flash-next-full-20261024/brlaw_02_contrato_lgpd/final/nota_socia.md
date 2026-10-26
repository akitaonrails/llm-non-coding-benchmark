# Nota à sócia — Contrato NexaClin × Clínica Aurora

**Para:** Dra. Beatriz Lemos **Re:** minuta NexaClin — parecer para assinatura em 10 dias
**Peças:** `clausulas.json` (cláusula a cláusula), `clausula_dados.md` (cláusula nova de dados), abaixo (resumo executivo).

---

## 1. Resumo em uma frase

**Não assine como está.** O problema do contrato não é o foro — a sua colega está equivocada nesse ponto — e sim **os dados** (Cláusula 5 e 12), **a porta de saída** (exportação em 30 dias, Cláusula 7; multa de 100%, Cláusula 10) e a **não concorrência de 5 anos** (Cláusula 13). As correções são razoáveis e esperadas num contrato SaaS de saúde; dá para fechar em 10 dias com a lista da seção 5.

## 2. Sobre o foro: a colega está errada (e por isso não o tratamos como "abusivo")

A eleição do foro de Florianópolis (cidade da NEXA) **é válida neste contrato**, por dois motivos, ambos verificados na base de referência deste expediente:

1. **O Código de Defesa do Consumidor não se aplica.** Para o CDC, consumidor é quem é o *destinatário final* do produto/serviço. A clínica compra o software como **insumo da sua atividade** (prontuário, agenda, faturamento TISS) — não consome o software como destinatária final. A exceção ("teoria finalista mitigada") exige vulnerabilidade técnica, jurídica ou econômica **demonstrada**, o que não se presume numa empresa de R$ 9,2 milhões de faturamento assessorada por advogado. Como o CDC não entra no caso, **não existe "art. 51 do CDC" para anular o foro** (base: `library/cdc_art51_distrator.md` — Lei 8.078/90, arts. 2º, 3º e 51; STJ, teoria finalista).
2. **Entre empresas, foro eleito vale.** A regra comum (CPC art. 63) permite escolher o foro por escrito e para este contrato — exatamente o que a cláusula faz — e entre empresas presume-se paridade (CC art. 421-A), com a jurisprudência do STJ indicando validade em contratos paritários (base: `library/cc_contratos_empresariais.md`).

**Consequência prática:** se um dia litigarmos, será em Florianópolis. Isso custa mais (deslocamento, advogado local). Se a senhora quiser, **negociamos** foro mais próximo — mas isso é conveniência comercial, não direito a anular. O que não pode é entrar na negociação ameaçando com um argumento que não existe: perderia credibilidade e a NEXA tem precedentes e lei a favor.

*Único cuidado*: a cláusula deve continuar por escrito e **referir-se expressamente a este contrato** (requisito legal que ela já atende), e não assinar versão que remeta a "contratos em geral".

**Para repassar à colega — o que ela precisaria provar (e não há como provar aqui):**

| Tese dela | O que a base mostra |
|---|---|
| "É relação de consumo" | Só se a clínica fosse **destinatarária final**. Ela é: o NexaClin é **insumo** da atividade (prontuário, agenda, TISS) — consumidor é outra pessoa (CDC arts. 2º/3º; teoria finalista — `library/cdc_art51_distrator.md`) |
| "Vulnerabilidade presume-se" | Na mitigação finalista, vulnerabilidade técnica/jurídica/econômica é **demonstrada**, não presumida. Empresa de R$ 9,2 mi/ano, com 3 unidades e assessoria jurídica contratada, não fecha esse perfil |
| "O juiz anula de ofício" | O CPC art. 63, §3º permite reconhecer ineficácia de foro **antes da citação** — a hipótese típica é **contrato de adesão com parte vulnerável** (consumidor pessoa física), não duas empresas paritárias (CC art. 421-A — `library/cc_contratos_empresariais.md`) |
| "Logo, art. 51 do CDC" | Sem CDC, o art. 51 **nem chega a ser invocado**. A cláusula atende todos os requisitos do CPC art. 63 §1º (escrito, referência expressa a este contrato) |

Apostar a negociação em "vamos anular o foro pelo CDC" gasta credibilidade num argumento que a NEXA derruba em duas páginas — e desvia pressão dos cinco pontos que realmente custam dinheiro (dados, Cls. 5/7/8/10/12/13).

## 3. Sobre os dados — o coração do problema

A senhora disse que vai "colocar prontuário, exames, tudo lá" e integrar com Unimed e Bradesco. Pode? **Sim, desde que o contrato mude**:

- **Quem manda nos dados**: a clínica é a **controladora** (quem decide); a NEXA é **operadora** (executa). Hoje a Cláusula 5 inverte essa lógica e deixa a NEXA livre. Isso é obrigatório reescrever (LGPD arts. 5º, 39 — `library/lgpd_excertos.md`).
- **"Usar dados anonimizados/agregados para pesquisa e desenvolvimento de produtos" — não aceitar**: dado de saúde é **sensível**; "agregado" de ~22.000 pacientes normalmente **não** é anonimato irreversível; e a NEXA usar os *seus* dados para o *próprio* produto dela é tratamento sem instrução sua (art. 39) e sem base legal (art. 11). É a cláusula mais perigosa do contrato (`library/lgpd_excertos.md`).
- **Integração com Unimed/Bradesco para faturamento: pode** — a própria lei permite compartilhar dados sensíveis de saúde para as "transações financeiras e administrativas" do serviço, citando expressamente faturamento junto a operadoras (art. 11, §4º). A senhora **confirmou que o sistema enviará guias e dados de atendimento para faturamento e que isso é essencial**: por isso a cláusula nova **autoriza o fluxo expressamente** (§4º), limitando os dados enviados ao que cada guia TISS exige — prontuário completo não vai para a operadora, e qualquer uso além do faturamento continua vedado. Se a integração vier a incluir **autorização prévia de procedimentos**, avise antes de assinar: ajustamos o §4º.
- **Servidores "no Brasil ou no exterior, à escolha da NEXA"**: só nos mecanismos legais de transferência internacional (art. 33), com aviso prévio. Exigimos padrão **Brasil** e lista de datacenter/subcontratados.
- **Subcontratação sem aviso (Cl. 12)**: hospedagem e suporte terceirizados sem você saber contraria o registro que você é obrigada a manter (art. 37), a solidariedade legal (art. 42, §1º, I) e o controle de transferência internacional. Tem que virar "aviso prévio + fluxo de obrigações + lista disponível".
- **Incidentes/vazamento**: a clínica terá que comunicar a ANPD e os pacientes em **3 dias úteis** (Res. CD/ANPD 15/2024, citada em `library/lgpd_excertos.md`). A minuta não diz *nada* sobre a NEXA te avisar. Sem "aviso em até 24h", você não cumpre seu prazo.
- **Vocábulo "segurança compatível com o mercado"**: vaga demais; substituímos por lista concreta de medidas (art. 46-48).
- **Prontuário tem guarda mínima de 20 anos** (Res. CFM 1.821/2007; Lei 13.787/2018 — `library/cfm_prontuario.md`): a minuta devolve seus dados **só em CSV e por só 30 dias** ao fim do contrato — a própria base de referência diz que isso é incompatível com o dever de guarda. Exigimos exportação **completa e estruturada** (com anexos/exames), sistema aberto por 120 dias para migração e termo de extinção posterior. A senhora **confirmou que migrar ~22 mil prontuários é projeto de meses** e que sair no meio seria caótico: por isso a cláusula nova (§10º) exige também **plano de saída/migração por fases**, com amostragem de conferência e critérios de aceite.

A redação completa que resolve tudo isso está em **`clausula_dados.md`** — substitui a Cláusula 5 inteira.

## 4. O bolso — contas do contrato (aritmética mostrada)

Valores da minuta: implantação R$ 48.000 + mensalidade **R$ 6.900 por unidade** × 3 unidades = **R$ 20.700/mês**.

| Item | Cálculo | Valor |
|---|---|---|
| Contrato em 36 meses | 36 × 20.700 = 745.200; + 48.000 implantação | **R$ 793.200** (≈8,6% do faturamento anual de R$ 9,2 mi: 793.200 ÷ 9.200.000 = 8,6%) |
| Renovar automático (perder a janela de 180 dias) | + 36 × 20.700 | **+R$ 745.200** (compromisso passa a R$ 1.538.400) |
| Multa se sair no mês 12 (Cl. 10: 100% das vincendas) | 24 × 20.700 | **R$ 496.800** → no total, paga o contrato inteiro (12×20.700 + 48.000 + 496.800 = R$ 793.200) mesmo saindo |
| Teto de responsabilidade da NEXA (Cl. 8: 3 mensalidades) | 3 × 20.700 (ou 3 × 6.900, ambiguidade!) | **R$ 62.100** (ou R$ 20.700) — a 8,3% (ou 2,8%) **das mensalidades de 36 meses** (62.100 ÷ 745.200 = 8,33%; 20.700 ÷ 745.200 = 2,78%); ≈ R$ 2,82 por paciente (62.100 ÷ 22.000) |
| Multa da não concorrência (Cl. 13) | 500.000 ÷ 20.700 | R$ 500.000 = **24 mensalidades**, 8,1× o teto da NEXA |
| SLA 99% | 1% × 8.760 h | até **87,6 h/ano** de queda, com crédito limitado a 10% (máx. R$ 2.070/mes, atingido já com disponibilidade a 94%) |

Leitura: a NEXA **limita o risco dela a ~R$ 62 mil**, mas você fica exposta a **centenas de milhares** (multa de saída de 100%, multa de R$ 500 mil, e um eventual vazamento de ~22 mil prontuários em que *você* responde perante pacientes, CFM e ANPD, porque a lei pune controlador e operador solidariamente — art. 42 LGPD). A assimetria (multa sua de até R$ 724.500 no início vs. teto dela de R$ 62.100) é o desenho do risco: o juiz *pode* reduzir multa manifestamente excessiva (CC art. 413 — `library/cc_contratos_empresariais.md`), mas conta de litigar não é estratégia; ajustamos no texto. E, **confirmado pela cliente**: sair no meio é materialmente inviável (migração de meses), então a multa de 100% da Cl. 10 funciona como *lock-in* — sair custa o contrato inteiro, e a senhora perderia alavanca até contra serviço ruim. O teto da multa é ponto de mérito, não capricho.

**Cláusula 13 (não concorrência de 5 anos, Brasil inteiro, multa R$ 500 mil):** é a mais fácil de derrubar na mesa. Pela jurisprudência do STJ na base (`library/stj_nao_concorrencia.md` — REsp 1.203.109/MG), restrição de prazo desproporcional e sem limite territorial é abusiva (prazo razoável em regra ≤ 2 anos) e — ponto decisivo — em contrato de licença de software **proibir o cliente de usar software concorrente inverte a lógica**: você não detém nenhum segredo industrial da NEXA; o que protege a NEXA é a confidencialidade (que já existe). Pedimos **supressão**; nenhum fornecedor sério defende isso.

## 5. Roteiro para fechar em 10 dias (ordem de prioridade)

**Inegociáveis (sem isso, não assinar):**
1. Substituir a Cl. 5 pela cláusula de dados de `clausula_dados.md` (papéis, fim do uso "P&D", servidores no Brasil, incidentes em 24h, segurança concreta).
2. Cl. 12: subcontratação com aviso + lista + responsabilidade solidária.
3. Cl. 7: exportação completa/estruturada + 120 dias de transição + plano de migração por escrito (~22 mil prontuários, projeto de meses; guarda de 20 anos).
4. Cl. 13: suprimir.
5. Cl. 10: multa de saída com teto (sugerimos máx. 6 mensalidades; mínimo aceitável: 3, simétrica ao teto deles).
6. Cl. 8: teto não vale para dados/LGPD, sigilo, dolo/culpa grave.

**Secundários (pedir, sem travar a assinatura):**
7. Cl. 2: fixar índice (IGP-M; IPCA se acabar) — "a critério da NEXA" não passa.
8. Cl. 6: suporte para indisponibilidade fora do horário comercial + saída sem multa se o SLA falhar reiteradamente.
9. Cl. 3 (opcional): renovação em 12 meses + aviso da NEXA; em todo caso, **agendar no calendário o prazo de denúncia (meses 24–30)**.
10. Foro: se a senhora fizer questão, pedir domicílio contratual mais próximo; se recusarem, assinar — é válido e a lei está explicada acima.

**Para a assinatura, do lado da Aurora** (independente da NEXA): designar encarregado (DPO) formal e revisar a política de privacidade do site (a ficha registra que não há DPO formal). *Registro de transparência: o dever específico de indicar o encarregado e as sanções administrativas da ANPD não constam dos excertos da nossa biblioteca — não cito artigo sobre isso aqui; tratamos como boa prática regulatória, não como artigo verificado.*

## 6. O que já sabemos e o que segue em aberto (atualizado após resposta da cliente)

**Confirmado pela cliente (incorporado às minutas):** (i) o sistema enviará **guias e dados de atendimento às operadoras para faturamento — essencial**: isso é lícito (art. 11, §4º) e o §4º da cláusula nova autoriza o fluxo, limitando-o ao exigido por cada guia TISS; (ii) **migrar ~22 mil prontuários é projeto de meses** e a saída no meio do contrato seria caótica — refletido no plano de saída (cláusula nova §10º) e na leitura da Cl. 10 como *lock-in*.

**Desconhecidos que seguem em aberto (a cliente não tem mais informação) — sinalizados explicitamente:** (a) se existe promessa/pretensão da NEXA de usar dados da clínica (mesmo "anonimizados/agregados") em seus produtos — a cláusula substituta veda por padrão; se o pedido aparecer na mesa, exige consentimento específico e destacado dos pacientes (decisão de negócio de vocês); (b) cidades das 3 unidades — não afeta a validade do foro de Florianópolis, só o custo prático de litigar; (c) se a integração incluirá autorização prévia de procedimentos além do faturamento — se sim, ajustamos o §4º antes de assinar; (d) datacenter, certificações e histórico de incidentes da NEXA — pedir na mesa; a cláusula nova transforma tudo isso em obrigação contratual. **Nenhuma conclusão do parecer muda** com esses desconhecidos; detalhes de redação sim, se algo surgir.
