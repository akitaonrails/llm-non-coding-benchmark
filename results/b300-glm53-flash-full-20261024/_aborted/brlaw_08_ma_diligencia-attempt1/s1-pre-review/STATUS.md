# STATUS — Venda de 100% das quotas da Vértice Engenharia Consultiva Ltda. → Grupo Meridiano

**Estado: `COMPLETE WITH OPEN ITEMS`**

Em uma frase: **os entregáveis exigidos estão prontos, consistentes e já incorporam as
respostas do cliente de 25/10; os itens abertos abaixo são desconhecidos de fato/valor
registrados explicitamente — nenhum bloqueia substância, pois as entregas foram feitas com
premissas declaradas em vez de ficarem paradas.**

- Data: 25/10/2026 (respostas do cliente integradas no mesmo dia).
- Fontes dos fatos: data room (extraído dos PDFs da sala), minuta do comprador (extraída),
  e-mail dos sócios (prioridades: fechar em 45 dias, medo de CADE, engenheiros PJ) e
  **respostas dos sócios de 25/10** (Hélio e Beatriz).
- Autoridade citável: exclusivamente `workspace/library/` conforme `INDEX.md` (7 arquivos);
  toda citação de norma nos entregáveis aponta para um desses arquivos. Matérias fora da
  biblioteca (PJ-vínculo, Simples/ISS sublimite, certidão positiva com efeitos de negativa,
  destravamento Sorocaba) permanecem **rotuladas como não verificadas** — nunca como norma.

## 1. Entregáveis (contrato, itens 1–5)

| Arquivo | Estado | Conteúdo em uma linha |
|---|---|---|
| `achados.json` | ✅ pronto | **17 achados**; schema `achado / onde / por_que_importa / efeito / solucao` (efeito só entre: anuencia, preco, indenizacao, prazo, nenhum); campo `onde` admite prefixos `data room §…`, `minuta cl. …`, `cliente — … (25/10)` |
| `redline.md` | ✅ pronto | Posições cláusula a cláusula: 2.3 (EBITDA pela contabilidade histórica, sem rateio do grupo — `library/earnout_pratica.md`); 3.2 (Anexo 3.2 redesenhado e CADE: **não notificável**, excluir a condição — `library/cade_limiares.md`); 5.7 e 5.9 qualificadas para disclosure schedule; 8.4(a) franquia dedutível; 8.4(b) teto 15% mantido, carve-outs removidos, indenizações específicas calibradas com 25/10; 8.4(c) híbrido; 8.4(d) 3 anos para 5.7/5.9; 9.1 cinco anos no território efetivo (`library/cc_1147_nao_concorrencia.md`); 10.2 escrow dedicado com faixas fixadas |
| `resposta_advogado_comprador.md` | ✅ pronto | Anexo 3.2, CADE e 8.4(c) — tom técnico e urbano; **ajuste de integridade (25/10):** a anuência não atrasa, desde que o pedido formal saia por escrito de imediato |
| `nota_socios.md` | ✅ pronto | Exatamente as **três** coisas que custam dinheiro após o fechamento (IRPJ R$ 310 mil contestado; 11 PJ + 3 reclamatórias; earn-out) + bloco de urgência da anuência (25/10) |
| `PERGUNTAS.md` | ✅ pronto | **Registro de respostas (25/10) e desconhecidos** — seção 1: o que fechou (Q9, Q10, Q5-parcial); seção 2: desconhecidos registrados sem nova pergunta |
| `QUESTIONS.md` | ✅ pronto | Gêmeo **byte-idêntico** de `PERGUNTAS.md` (`cmp` OK) |
| `STATUS.md` | ✅ | este arquivo |

**Nenhum entregável exigido está ausente.**

## 2. Respostas do cliente (25/10) — como foram integradas

Citações exatas recebidas:

1. **Hélio (anuência):** "a Horizonte Azul é nosso maior cliente; o diretor deles é meu
   amigo, mas o jurídico deles é duro. Não contamos da venda ainda."
2. **Beatriz (11 PJ):** "os 11 engenheiros PJ trabalham 9h-18h aqui, exclusivos, com gestor.
   Sempre foi assim."
3. **Hélio (IRPJ):** "tem um débito de IRPJ de 2023 em cobrança, uns 310 mil; não parcelamos
   porque discordamos."
4. **Geral:** para as perguntas não respondidas acima, o cliente não tem informações
   adicionais → itens restantes registrados como **desconhecidos** (sem reabertura de
   perguntas).

Integração por arquivo:

- **`achados.json`** — (a) achado IRPJ: contestação registrada no `achado`, `onde` recebe
  `cliente — Hélio (25/10)`, `por_que_importa` ganha o desfecho binário da disputa, `solucao`
  substitui "parcelar/quitar" pela rota travada (contestação conduzida pela sociedade +
  escrow liberado conforme desfecho; destravamento Sorocaba com CND positiva não verificado
  em biblioteca); (b) achado 11-PJ: confirmação da Beatriz no `achado` e no `onde`,
  validação do regime como histórico (conversão → CLT endereça só o futuro), teto específico
  = âncora provisória nos pedidos conhecidos (parâmetro Solaris NÃO informado); (c) **novo
  achado #17 — anuência HA não solicitada** (efeito: prazo): caminho crítico = pedido formal
  por escrito de imediato, interlocutor jurídico da contratante, plano B preparado.
- **`redline.md`** — premissa atualizada (fatos 25/10 declarados); 3.2(B) ganha o estado do
  pedido; 5.7 motivo fecha o diapasão fático com a confirmação; 5.9 texto (a) menciona a
  contestação e o motivo troca parcelar/quitar pela rota escrow; 8.4(b) traz a **nota de
  calibragem** (aritmética abaixo); 10.2 fecha as faixas dedicadas.
- **`nota_socios.md`** — premissa remite aos desconhecidos; item 1 substitui "Melhor ainda:
  parcelar/quitar" pelo desenho escrow com contestação; item 2 registra a confirmação e a
  distinção futuro/passado; teto Solaris vira âncora provisória; "Para terminar" ganha o
  bloco de urgência da anuência.
- **`resposta_advogado_comprador.md`** — edição única de integridade: "não atrasa, desde que
  o pedido formal saia por escrito de imediato".
- **`PERGUNTAS.md`/`QUESTIONS.md`** — reescrita como registro (respondidas + desconhecidos).
- **`working/calc.py`** — estendido e rodando sem erros (aritmética da calibragem).

### Retransmissão de 25/10 (advogado do comprador + Hélio)

- O advogado do comprador (retransmitido): "8.4(c) é padrão de mercado; 5.7 e 5.9 são
  declarações de conformidade básicas — se está tudo certo, qual o problema?" — Rebatido na
  nova seção 4 de `resposta_advogado_comprador.md`: o pro-sandbagging como método não é
  disputado (o item 3 o preserva); questiona-se a leitura seletiva — a mesma prática da
  biblioteca (`sandbagging_franquia_mercado.md`) condiciona a indenização a disclosure
  schedule, indenização específica com teto e escrow dedicado, franquia dedutível, limite
  10–20% e prazo 2–3 anos, e caracteriza a combinação "declaração limpa + matéria revelada no
  data room + teto = preço + 5 anos" como transferência integral de um risco conhecido; e a
  premissa "tudo certo" desaba contra o próprio data room do comprador (11 PJs, CND positiva,
  ISS fora do recolhimento).
- Hélio: "podemos só assinar?" — Respondido na nova seção da `nota_socios.md`: podem assinar —
  a nota mostra a aritmética do que se assina (pagamento dobrado de 310k + encargos; gap PJ de
  1,02M; teto = preço integral; anuência segue pendente); recomendação: manter as condições;
  plano B (desconto de preço ou escrow da multa) apenas se a contraparte recusar.
- Sem mudança de posição nem nova exigência: os 17 achados, as 3 frentes e os gêmeos ficam
  como estavam; o cronograma de 45 dias segue.

## 3. Itens abertos = desconhecidos registrados (client-confirmed: sem mais informações)

| # | Desconhecido | Origem | O que calibra / estado hoje |
|---|---|---|---|
| 1 | **Preço Total ("P")** | Q1 | P é simbólico nos documentos: teto global 8.4(b) = 0,15 × P; escrow global (X)% = soma dos tetos específicos ÷ P; franquia de R$ 150 mil proporcional. |
| 2 | **Saldo contratual Horizonte Azul ("S")** | Q2 | Multa da cl. 19 = 0,20 × S. Receita anual em jogo: 0,31 × 4.200.000 = **R$ 1.302.000/ano**. |
| 3 | **Composição das quotas (terceiro sócio? 100%?)** | Q3 | Se só Hélio e Beatriz vendem 100%, a preferência de 30 dias não tem destinatário; do contrário, corre contra os 45 dias. |
| 4 | **Território e disciplinas efetivos** | Q4 | Redação final da 9.1 (5 anos, território efetivo). |
| 5 | **Valor do "caso Solaris"** | Q5 (parcial) | Perfil dos 11 PJ confirmado pela Beatriz; **valor não informado**. Teto específico PJ = aberto à negociação; âncora provisória R$ 1,4 mi. |
| 6 | **ISS "por fora": guias/municípios** | Q6 | Sem base na biblioteca (Simples/ISS — não verificado); qualifica a 5.9 no disclosure schedule. |
| 7 | **Base da provisão R$ 380 mil e estágio das 3 reclamatórias** | Q7 | Gap 1.400.000 − 380.000 = **R$ 1.020.000** (≈ 24,29% da receita) segue **aberto e não conciliado**. |
| 8 | **Substituto de Hélio como RT (quem, quando)** | Q8 | Pré-requisito da comunicação ao Município (Anexo 3.2; `library/lei14133_alteracao_societaria.md`). |
| 9 | **Encargos do IRPJ 2023** (atualização sobre R$ 310 mil) | novo (25/10) | Teto real da indenização específica fiscal = R$ 310 mil + encargos; parcela "encargos" em aberto. |
| 10 | **Prazo de processamento da anuência pela HA** | novo (25/10) | Calendário dos 45 dias; reforça pedido imediato + data externa. |
| 11 | **Destravamento da habilitação perante a Sorocaba com CND positiva** | novo (25/10) | **Não consta da biblioteca** (não verificado) — tributarista da sociedade. |
| 12 | **Escrow global (X)%** | Q1 + mix | Faixas dedicadas já fixadas (IRPJ: 310 mil + encargos; trabalhista/PJ: âncora R$ 1,4 mi — teto final a negociar); o % global depende de P e do teto final da matéria PJ. |

**Não há item aberto de CADE** (390.000.000 < 750.000.000 e 4.200.000 < 75.000.000 → não
notificável, `library/cade_limiares.md`) **nem de anuência dos demais contratos privados**
(data room §1.3: silentes quanto a mudança de controle).

## 4. Premissas declaradas (o que sustenta as entregas sem esperar resposta)

1. **Venda de 100% das quotas por Hélio e Beatriz** — se houver terceiro sócio, o item 3 recalibra o cronograma (preferência de 30 dias).
2. **P (e S) simbólicos** — todo valor dependente de preço/saldo ficou como fórmula (0,15 × P; 0,20 × P; 0,20 × S) ou como valor absoluto do data room (R$ 4,2 mi; R$ 1.302 mil; R$ 504 mil; R$ 310 mil; R$ 380 mil; R$ 1,4 mi).
3. **EBITDA do earn-out apurado pela contabilidade histórica da Sociedade**, sem rateio de despesas corporativas do grupo (posição do redline 2.3, lastro em `library/earnout_pratica.md`) — o rateio chega a custar 0,35 × rateio por ano (R$ 35 mil/R$ 70 mil nos exemplos calculados).
4. **Fatos de data room/cliente sem lastro em biblioteca** (PJ-vínculo; Simples/ISS sublimite; caso Solaris; destravamento Sorocaba) estão marcados como não verificados nessas palavras nos entregáveis — nunca como norma.
5. **Nada fora da `library/` foi citado como autoridade** — o que seria norma fora dela virou pergunta ou supuesto rotulado.

## 5. Aritmética (script `workspace/working/calc.py`, roda sem erros)

- Horizonte Azul: 31% × 4.200.000 = **R$ 1.302.000/ano**
- Sorocaba: 12% × 4.200.000 = **R$ 504.000/ano** (retenção por descumprimento de habilitação)
- Gap trabalhista: 1.400.000 − 380.000 = **R$ 1.020.000** = 24,29% da receita
- Earn-out: limiar do teto 1.500.000 ÷ 0,35 = R$ 4.285.714 de excesso ⇒ EBITDA de R$ 5.385.714 = **128,23% da receita** (teto inatingível na prática, conforme redline 2.3)
- Rateio do grupo: R$ 100 mil → perde **R$ 35.000**; R$ 200 mil → **R$ 70.000**
- **Calibragem PJ (25/10):** pedido médio conhecido = 1.400.000 ÷ 3 = **R$ 466.666,67/ação**;
  extrapolação mecânica = 11 × 466.666,67 = **R$ 5.133.333,33** ≈ **122,22%** da receita —
  explicitada pela nota de calibragem como **aritmética, não estimativa de perda nem base de
  teto** (é o teto superior que o comprador pode alegar); o teto específico PJ fica aberto à
  negociação.
- Fórmulas dependentes de preço: multa HA = 0,20 × S; teto 8.4(b) = 0,15 × P; escrow 10.2 = (X)% do Preço = soma dos tetos dedicados ÷ P.

**Nota de conciliação:** nada foi forçado a fechar. Os dois desencontros materiais — o gap
trabalhista de R$ 1.020.000 e o valor do teto específico PJ (âncora R$ 1,4 mi vs. extrapolação
mecânica R$ 5.133.333,33) — permanecem **explicitamente abertos** como riscos quantificados,
não "conciliados".

## 6. Verificações de conformidade executadas

- `achados.json`: parse OK (JSON válido), **17 achados**, chaves e valores de `efeito`
  dentro do enum do contrato; prefixos de `onde` verificados (`data room §`, `minuta cl.`,
  `cliente — … (25/10)`).
- Whitelist de citações: todo `library/*.md` citado nos entregáveis consta do `INDEX.md`
  (7 arquivos). Menções a nomes de entregáveis entre si (ex.: `redline.md`, `QUESTIONS.md`)
  são **cross-references internos** — não são citações de autoridade.
- `PERGUNTAS.md` ≡ `QUESTIONS.md` (byte-igual, `cmp`).
- Presença: os 7 arquivos do item 1, incluindo este `STATUS.md`.

**Próximo passo desta mesa:** o **pedido formal de anuência, por escrito, à Horizonte Azul é
o dia 0 do caminho crítico** — ainda não saiu e o relógio de 45 dias corre; enviar com dossiê
de habilitação e cronograma, com o jurídico da contratante como interlocutor. Em paralelo:
(a) decisão dos sócios sobre o plano B da anuência (desconto de preço ou escrow da multa de
0,20 × S) antes da assinatura; (b) nome/substituição do responsável técnico no CREA;
(c) negociação do teto específico PJ e do % global de escrow quando P for informado;
(d) ponto "só assinar" (pergunta de Hélio após a retransmissão) — respondido na seção
"Podemos só assinar?" da `nota_socios.md`; segue em acompanhamento até resposta da
contraparte à seção 4 de `resposta_advogado_comprador.md`.
