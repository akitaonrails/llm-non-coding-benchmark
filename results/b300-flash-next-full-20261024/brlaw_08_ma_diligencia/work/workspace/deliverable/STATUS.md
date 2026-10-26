# STATUS — Engajamento Vértice (sell-side)

**COMPLETE WITH OPEN ITEMS** (atualizado após a 3ª rodada — posicionamento do advogado do comprador + auditoria pré-entrega)

## Entregáveis (todos presentes em `deliverable/`)
1. `achados.json` — 12 achados, esquema validado (5 chaves fixas; efeitos ∈ {anuencia, preco, indenizacao, prazo}); nenhum uso de "nenhum"; fatos da 2ª rodada incorporados nos achados F1, F3 e F4.
2. `redline.md` — 2.3, 3.2 (Anexo 3.2 + CADE), 5.7, 5.9, 8.4(a)-(d), 9.1, 10.2: manter/alterar + redação + motivo; premissas e desconhecidos permanentes declarados no cabeçalho.
3. `resposta_advogado_comprador.md` — Anexo 3.2, CADE, 8.4(c) + **Adenda (seção 4)** respondendo à reformulação verbal da 3ª rodada ("padrão"/"conformidade básica") e reafirmando a proposta binária com prazo de 5 dias úteis. Fatos internos novos (anuência ainda não pedida; confessões dos sócios ao cliente) **não** se comunicam à contraparte — deliberadamente, inclusive na Adenda.
4. `nota_socios.md` — três itens que custam dinheiro pós-fechamento + seção "Depois das respostas de vocês" com agenda da semana + seção "Hélio perguntou 'podemos só assinar?'" (resposta: não, com a aritmética).
5. `QUESTIONS.md` / `PERGUNTAS.md` — registro de Q&A: 1 respondida (Q3), 2 parciais (Q5, Q7), 7 desconhecidos explícitos (Q1, Q2, Q4, Q6, Q8, Q9, Q10 — Q4 resolvida por premissa declarada) (cliente informou não ter mais dados; nada foi perguntado de novo).

## Conclusões centrais
- **CADE não notificável** (Meridiano R$ 390 mi < R$ 750 mi; Vértice R$ 4,2 mi < R$ 75 mi — limiar cumulativo, art. 88): suprimir a condição 3.2; os 45 dias dependem da preferência de 30 dias e da anuência da Horizonte Azul, não do CADE.
- **Anexo 3.2 "não aplicável" é inexato**: anuência Horizonte Azul (31% da receita; rescisão imediata + 20% do saldo), comunicação prévia a Sorocaba (Lei 14.133), RT/CREA.
- **Pacote indenizatório predatório**: declarações limpas (5.7/5.9) vs. fatos revelados (11 PJs; CND positiva R$ 310 mil; ações R$ 1,4 mi/provisão R$ 380 mil) + sandbagging 8.4(c) + limite = preço + 5 anos + escrow 20%/5 anos. Correção: anexos de exceção + indenizações específicas com tetos + franquia dedutível + sobrevida prescrição+6m.
- **Earn-out ilusório**: teto de R$ 1,5 mi exige EBITDA de R$ 5.385.714,29 (= 1.100.000 + 1.500.000/0,35) > faturamento total (R$ 4,2 mi), e a métrica é controlada pelo comprador com rateios.
- **9.1** (10 anos/Brasil) fora do padrão CC art. 1.147 (5 anos; razoabilidade/STJ).

## O que a 2ª rodada mudou
- **Horizonte Azul**: anuência **ainda não pedida**; jurídico da contratante "duro" → risco de alavanca renegotiatória se a notícia vazar ou o pedido atrasar; plano de abordagem (Hélio → diretor sob NDA, minuta pronta, consentimento não reabre preço) inserido em F1, redline 3.2 e nota aos sócios.
- **PJs**: 9h-18h, exclusivos, com gestor → subordinação e habitualidade confessadas; risco de equiparação **reclassificado de "possível" para alta probabilidade** (F4, redline 5.7).
- **IRPJ 2023**: não pago/não parcelado por discordância → CND positiva tende a persistir no fechamento; tratamento por indenização específica/retenção no preço, sem invocar mecanismos fora da library (ver limites de verificação) (F3, redline 5.9).

## O que a 3ª rodada (retrucas do comprador) mudou
- Advogado do comprador reafirmou 8.4(c) como "padrão" e 5.7/5.9 como "conformidade básica". Resposta por escrito na **Adenda (seção 4)** de `resposta_advogado_comprador.md`: o padrão existe, mas com a arquitetura completa (anexos + tetos + franquia + sobrevida menor); a premissa "se está tudo certo" cai sobre os fatos do próprio data room (CND positiva → 5.9 falsa na véspera; 11 PJs + R$ 1,02 mi acima da provisão → 5.7 inexata); a proposta binária (anexos → aceita-se 8.4(c); declarações limpas → suprime-se 8.4(c)) foi reafirmada e exige resposta escrita com escolha de (i) ou (ii).
- Hélio perguntou "podemos só assinar?" — resposta **não**, com a conta fechada na nota aos sócios (escrow 20% × 5 anos + regresso até 100% por fato conhecido + earn-out comprovadamente zero). Consequências de declaração sabidamente falsa além da indenização **não constam da library** → registradas como NÃO VERIFICADO, sem jurisprudência inventada.

## Auditoria pré-entrega
- Leitura integral de novo: 6 entregáveis + os 7 itens da `library/` + data room + minuta do comprador. Aritmética refeita (EBITDA p/ teto do earn-out R$ 5.385.714,29 > R$ 4,2 mi; 31% × 4,2 mi = R$ 1.302.000/ano; 12% × 4,2 mi = R$ 504.000/ano; gap 1,4 mi − 380 mil = R$ 1.020.000; exemplos 140 mil/315 mil) — tudo confere. JSON revalidado (12 achados, 5 chaves, enums).
- Corrigidos sem alterar conclusões: (i) título da seção CADE da nota, engolido por edição da 3ª rodada; (ii) asserção de regra padrão "conhecimento prévio afasta a indenização" e frase "é o padrão" sobre supressão de 8.4(c) — a disciplina sem a cláusula **não está na library** → reformulado como "remove o gancho contratual expresso" com rótulo NÃO VERIFICADO (achado F5, redline 8.4(c), carta §3(ii) e Adenda (c)); (iii) "cujos contratos descrevem" → fatos conforme data room §2.2 (contratos individuais não revisados); (iv) "Vértice é regional" → inferência rotulada (só a praça de Sorocaba é localizada); (v) "10%/2 anos" do escrow rotulado como posicionamento derivado, não regra da library; (vi) referência cruzada "(item 3 abaixo)" da carta → redline 3.2(e)/5.9; (vii) referências obsoletas a "ilustração do redline" (não existe mais) em PERGUNTAS/STATUS; (viii) "franquia de 15%" → teto global de 15% (a franquia é R$ 150 mil fixos); (ix) contagem do Q&A no STATUS (1 respondida, 2 parciais, 7 abertos) e descrições dos itens 3–5; (x) artefato "vídeo de confiança" → relação de confiança; (xi) achado preferência alinhado à premissa declarada da Q4.

## Itens em aberto — DESCONHECIDOS PERMANENTES (cliente não tem mais informação; não forçados)
1. **Preço de fechamento** → limites de 15%/20%/100% não conversíveis em R$; tetos "dimensionados" ficam em fórmula.
2. **Saldo contratual da Horizonte Azul** → multa de 20% não quantificada (mantida apenas como fórmula "20% × saldo", sem valor presumido).
3. **Folha dos 11 PJs** → teto da indenização por pejotização fica por calcular (a fórmula e a necessidade estão declaradas; nenhum valor presumido).
4. **Quadro societário/quem vende** → tratou-se por **assunção declarada** (Hélio + Beatriz vendem 100%; preferência exaurida na assinatura); sócio remanescente reativa a renúncia como condição.
5. **Estágio/provável perda das 3 reclamatórias** → exposição acima da provisão (R$ 1,4 mi vs. R$ 380 mil provisionados) tratada como intervalo, não como ponto.
6. **Simples/ISS "por fora"** → exposição não quantificada; **a library não contém norma sobre Simples/ISS — qualificação tratada como NÃO VERIFICADA** e o item fica excepcionado na 5.9.
7. **"Caso Solaris"** (citado no data room) → não está na library; conteúdo **não verificado**; usado apenas como o data room o descreve.
8. **Sucessor do RT no CREA** e **atividade da Meridiano no Brasil** (sobreposição p/ risco residual CADE §7º) → em aberto; nenhum entregável depende deles para concluir.

## Limites de verificação (regra do contrato)
- Só se citam arquivos indexados em `library/INDEX.md` (7 usados). Prazos prescricionais específicos, encargos de recálculo trabalhista/tributário, indexadores de atualização, parcelamento e suspensão da exigibilidade **não constam da library** → usados apenas como fórmulas ("prescrição + 6 meses", `library/sandbagging_franquia_mercado.md`) ou marcados **NÃO VERIFICADO**; nada calculado com taxa inventada.

Nada reconciliado à força: gaps de informação deixados abertos acima, com aritmética demonstrada nos entregáveis.
