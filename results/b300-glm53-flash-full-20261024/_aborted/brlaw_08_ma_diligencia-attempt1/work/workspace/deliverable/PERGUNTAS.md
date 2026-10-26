# Perguntas ao cliente (Vértice) — registro de respostas (25/10) e desconhecidos

> **Status:** o ciclo de perguntas foi respondido em 25/10 (Hélio e Beatriz). Este arquivo é o
> **registro** do que foi respondido e do que ficou **sem informação** (desconhecidos). Não há
> reabertura de perguntas: o cliente informou que **não há dados adicionais** para os itens
> abertos — por isso eles aparecem abaixo como desconhecidos registrados, não como questionário.
> O gêmeo `QUESTIONS.md` é byte-idêntico a este arquivo. As respostas já foram integradas aos
> entregáveis (`achados.json`, `redline.md`, `nota_socios.md`,
> `resposta_advogado_comprador.md`) — ver `STATUS.md`.

---

## 1. Respondido em 25/10 — o que fechou

| # | Pergunta (do ciclo original) | Resposta do cliente (25/10) | O que fechou / o que mudou |
|---|---|---|---|
| 9 | O pedido de anuência à Horizonte Azul já foi feito? | **Não.** A venda não foi comunicada à contratante; o diretor é amigo de Hélio, mas o jurídico deles é quem decide ("é duro"). | Trava prática confirmada: **pedido formal por escrito de imediato** — dia 0 do caminho crítico dos 45 dias; interlocutor = jurídico da contratante; plano B (desconto de preço ou escrow da multa de 0,20 × saldo) preparado. Achado novo em `achados.json` (efeito: prazo). |
| 10 | Há intenção de parcelar/quitar o IRPJ 2023 de R$ 310 mil? | **Não parcelamos — discordamos.** A cobrança é contestada pelos sócios. | Rota travada: sem declaração limpa; proteção = qualificação com menção expressa da contestação + indenização específica (teto R$ 310 mil + encargos) + escrow dedicado liberado conforme o desfecho. A recomendação anterior de "parcelar/quitar" foi substituída em `redline.md` (5.9) e `nota_socios.md` (item 1). |
| 5 (parcial) | O que aconteceu no "caso Solaris" — configuração do perfil dos 11 PJ | **Confirmada por Beatriz:** os 11 engenheiros PJ trabalham 9h–18h, exclusivos, com gestor — "sempre foi assim". | Base fática da qualificação da 5.7 fechada (reconhecida pelos próprios declarantes); conversão para CLT trata só o **futuro** — o regime histórico segue como exposição retroativa. **O valor do caso Solaris não foi informado** — segue como desconhecido (item 2.5 abaixo). |

---

## 2. Desconhecidos registrados (sem resposta em 25/10 — sem nova pergunta)

O cliente informou que **não tem informações adicionais** para os demais itens. Cada um fica
registrado abaixo como desconhecido, com o peso que carrega. Nenhum impede a entrega; seguem
abertos para negociação/verificação direta.

| # | Desconhecido | Onde pesa | Estado |
|---|---|---|---|
| 1 | **Preço Total ("P")** | Teto global (0,15 × P); escrow global (X)% do Preço; proporcionalidade da franquia de R$ 150 mil | `redline.md`/`achados.json` trabalham com P simbólico; percentuais relativos só fecham com P |
| 2 | **Saldo contratual Horizonte Azul** (data room §1.1) | Multa de anuência = 0,20 × saldo; dimensionamento do plano B | Só conhecemos a receita anual: 0,31 × 4.200.000 = **R$ 1.302.000/ano**; saldo desconhecido |
| 3 | **Composição societária — só vende 100% com Hélio e Beatriz?** (data room §4.1 fala em preferência de 30 dias) | Cronograma: preferência corre contra os 45 dias se houver terceiro sócio | Premissa de venda de 100% mantida (declarada); ponto segue em vigilância |
| 4 | **Território e disciplinas efetivamente atendidos** | Redação final da 9.1 (nossa proposta: 5 anos, território efetivo vs. minuta: 10 anos / Brasil) | Redline mantido; alternativa da minuta segue recusada |
| 5 | **Valor do caso Solaris** | Único parâmetro que dimensionaria o teto específico do risco de vínculo dos 11 PJs | Âncora provisória: pedidos conhecidos de R$ 1,4 mi. Extrapolação mecânica explicitada e **não adotada** como teto: 1.400.000 ÷ 3 = R$ 466.666,67/ação; 11 × 466.666,67 = R$ 5.133.333,33 (≈ 122,22% da receita) — ver `redline.md` 8.4(b) e `working/calc.py` |
| 6 | **Guias ISS municipais e municípios** (data room §3.2 — "por fora" desde o sublimite 2025) | Qualificação completa da 5.9 (disclosure schedule) | Matéria sem base na biblioteca (Simples/ISS — fora do acervo de `library/INDEX.md`); tratada como fato do data room, sem conclusão jurídica |
| 7 | **Base de cálculo da provisão R$ 380 mil e estágio das 3 reclamatórias** (data room §2.3) | Gap trabalhista: 1.400.000 − 380.000 = **R$ 1.020.000** (1.020.000 ÷ 4.200.000 ≈ 24,29% da receita) sem cobertura contábil | Gap segue **aberto e não reconciliado** em `STATUS.md` |
| 8 | **Substituto de Hélio como responsável técnico — quem e quando** (data room §3.3) | Habilitação no contrato público de Sorocaba (Lei 14.133/2021 — art. 92, XVI e 124, II, conforme `library/lei14133_alteracao_societaria.md`); item (iii) do Anexo 3.2 | O nome e a data são pré-requisitos da comunicação ao Município |
| 9 | **Encargos do IRPJ 2023** (juros/multa correntes sobre R$ 310 mil) | Teto real da indenização específica fiscal = R$ 310 mil + encargos | Teto aberto na parcela "encargos"; escrow dedicado fecha a matemática quando houver valor |
| 10 | **Prazo de processamento da anuência pela Horizonte Azul** | Calendário do fechamento (45 dias) e viabilidade da condição (i) | Desconhecido; reforça pedido por escrito de imediato + data externa |
| 11 | **Meio de destravamento da habilitação perante a Sorocaba com CND positiva** | Execução do contrato público (Lei 14.133/2021, art. 92, XVI — retenção/sanções) | **Não consta da biblioteca** (não verificado) — tratar com o tributarista da sociedade |

---

## 3. O que não precisou de pergunta (fechado pelo acervo)

- **CADE:** limiares do art. 88 fechados pelo data room §4.2 (390.000.000 < 750.000.000;
  4.200.000 < 75.000.000): **não notificável** (`library/cade_limiares.md`).
- **Anuências dos demais contratos privados:** data room §1.3 ("silentes quanto a mudança de
  controle") — nada a fazer pelo acervo.

*Biblioteca citada neste registro (somente arquivos de `library/INDEX.md`):
`cade_limiares`; `lei14133_alteracao_societaria`.*
