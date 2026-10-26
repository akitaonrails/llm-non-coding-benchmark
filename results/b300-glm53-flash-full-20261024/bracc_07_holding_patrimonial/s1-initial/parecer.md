# Parecer — planejamento patrimonial e sucessório
**Cliente:** Dona Helena Furtado, 71 anos, viúva (comunhão parcial, viúva desde 2019). Três filhos: Ricardo (48), Paula (45), Marcos (41 — relação rompida há 6 anos; cliente informou: "não quero que receba nada; se a lei obriga, o mínimo possível e com cláusulas de proteção"). Patrimônio: 11 imóveis (mercado R$ 16.430.000; declaração IR R$ 4.720.000), aplicações R$ 2.100.000, aluguéis R$ 84.900/mês em carnê-leão, sem testamento. **Fatos pós-1ª rodada:** comissão da administradora 8%; ela paga IPTU/condomínio dos 2 imóveis vagos (Casa Campos do Jordão e Terreno Cotia), sem informar montantes.

**Escopo:** aferição das 5 afirmações da palestra (`documents/palestra_resumo.md`) com números, proposta de estrutura e limites. Fonte de autoridade: exclusivamente a biblioteca em `library/INDEX.md`. Números com aritmética explícita; premissas destacadas.

**Arredondamento:** valores em reais; no `numeros.json` arredondados ao inteiro mais próximo.

---

## 1. "Integralizar todos os imóveis numa holding sem ITBI (imunidade constitucional)"

**Veredicto: FALSA para o plano descrito (a regra é genuinamente "depende" no abstrato).**

Fundamento (`library/cf156_ctn37_tema796.md`):
- A imunidade do art. 156, §2º, I, da CF alcança a integralização de capital, **salvo** se a atividade preponderante do adquirente for compra e venda, **locação** de imóveis ou arrendamento mercantil — teste de >50% da receita operacional nos 2 anos anteriores e 2 posteriores; empresa nova: 3 anos seguintes (CTN art. 37, §§1º-2º).
- A holding da palestra é, por definição, uma **locadora**: 9 de 11 imóveis estão locados e 100% da receita projetada é aluguel. A exceção se aplica, e o ITBI é devido sobre a integralização.
- **Tema 796 (STF RE 796.376):** a imunidade não alcança o valor dos imóveis que exceder o capital social integralizado — ou seja, mesmo numa integralização imunizada, só a parcela efetivamente capitalizada está protegida.

**Números:** alíquota do ITBI-SP 3%. Base legal = valor venal municipal (**não informado pelo cliente**; premissa destacada: estimamos pelo valor de mercado — se o venal for menor, a estimativa cai na mesma proporção).

- 3% × 16.430.000 = **R$ 492.900** (integralização total)
- Decomposição Tema 796: 3% × 4.720.000 (desde que capitalizado e imune) = 141.600 evitável; 3% × 11.710.000 (excedente ao capital) = 351.300 devido.
- A conta do plano: integralizar agora (ITBI ~492.900 uma vez) **versus** manter os imóveis na PF e transferir por inventário no falecimento: ITCMD 4% × 16.430.000 = R$ 657.200 + custos/demora de inventário (não quantificáveis com a biblioteca). O ITBI é inferior ao ITCMD eventual; não é motivo para abandonar o plano, mas o "zero" da palestra não existe neste caso.

**Desenho alternativo (registrado, não recomendado aqui):** holding patrimonial sem receita de locação nos períodos-teste mantém a imunidade; mas aí a renda continua na PF a 27,5% e a economia de IR mensal se perde (ver item 2). Para uma titular de 71 anos que justamente quer reduzir a carga sobre a renda, a janela de 3 anos sem receita na PJ contraria o objetivo.

## 2. "Aluguel na PJ paga só 11,33% em vez de 27,5% na PF"

**Veredicto: DEPENDENTE — direção verdadeira, números errados no caso concreto.**

Fundamento (`library/locacao_pf_vs_pj.md`): no Presumido, locação tem presunção de 32%; IRPJ 15% + adicional 10% acima de R$ 20 mil/mês de presumido; CSLL 9%; PIS/COFINS 3,65%; sem ISS. Os 11,33% valem **só até o limite do adicional**; acima, a margem fica em ~14,53%. Com receita mensal de R$ 84.900, o adicional incide sempre.

**PF (premissa destacada):** a biblioteca só diz tabela progressiva até 27,5% — as faixas não estão na biblioteca. Adotamos o **teto** 27,5% sobre toda a renda tributável (sobrestima o IR da PF de leve; a diferença não muda a conclusão). A renda mensal está muito acima de qualquer faixa.
- Comissão da administradora informada pela cliente: **8%** → 84.900 × 8% = **6.792/mês**, dedutível no carnê-leão (`locacao_pf_vs_pj.md`: "comissão de administração").
- Base tributável: 84.900 − 6.792 = **78.108/mês** → 78.108 × 27,5% = 21.479,70/mês → × 12 = **R$ 257.756,40/ano** (25,3% da receita bruta).
- **IPTU/condomínio dos imóveis vagos** (Casa Campos do Jordão e Terreno Cotia) é pago pela cliente (**montante não informado**). Como não se vincula a aluguel recebido e o valor é desconhecido, **não deduzimos** (premissa: dedução zero por IPTU/condomínio). Se houver IPTU/condomínio de imóvel **locado** pago por ela e comprovado, o IR da PF cai um pouco mais — a vantagem relativa da PJ diminui na mesma medida.

**PJ no Presumido (aritmética mensal):**
- Presumido: 84.900 × 32% = 27.168,00
- IRPJ: 15% × 27.168 = 4.075,20; adicional: 10% × (27.168 − 20.000) = 716,80 → IRPJ total 4.792,00
- CSLL: 9% × 27.168 = 2.445,12
- PIS/COFINS: 3,65% × 84.900 = 3.098,85
- Total PJ (impostos da pessoa jurídica): 4.792,00 + 2.445,12 + 3.098,85 = 10.335,97/mês → ×12 = **R$ 124.031,64/ano = 12,17% da receita** (não 11,33%).

**Época 2026 (Lei 15.270/2025, conforme biblioteca):** distribuição de lucros a PF acima de R$ 50 mil/mês → IRRF 10%.
- Na PJ, a comissão de 8% não altera a base presumida (32% × receita bruta); ela só entra na conta do lucro a distribuir.
- Lucro mensal distribuível: 84.900 − 6.792 (comissão) − 10.335,97 (impostos PJ) = **67.772,03** → excede R$ 50 mil em 17.772,03.
- IRRF (premissa destacada: 10% sobre o **excedente** de R$ 50 mil; a biblioteca não explicita se a alíquota pega o excedente ou o total). 10% × 17.772,03 = 1.777,20/mês → **R$ 21.326,44/ano**.
- Carga total PJ 2026: 124.031,64 + 21.326,44 = **R$ 145.358,08/ano = 14,27% da receita**.

**Conclusão do item:** a comparação real é **25,3% (PF, já líquida da comissão dedutível) × 14,27% (PJ 2026, inclusive IRRF)** — e não 27,5% × 11,33%. Economia anual estimada: 257.756,40 − 145.358,08 = **R$ 112.398,32**. Se a leitura alternativa do IRRF (10% sobre o total distribuído) prevalecer: IRRF 6.777,20/mês = 81.326,44/ano, carga total 205.358,08/ano (20,16%) e economia de 52.398,32/ano — o ganho persiste, mas menor. Payback do ITBI: 492.900 ÷ 112.398,32 ≈ **4,39 anos** (na leitura alternativa: 492.900 ÷ 52.398,32 ≈ 9,41 anos).

## 3. "Doar as quotas aos filhos com reserva de usufruto, pagando ITCMD de 4% sobre o valor contábil (baixo)"

**Veredicto: FALSA no essencial (a alíquota está certa; a base "contábil" não).**

Fundamento (`library/itcmd_sp_lei10705.md`):
- ITCMD/SP incide sim na doação de quotas, **inclusive com reserva de usufruto** (fato gerador consumado). Alíquota 4% — corretíssima a alíquota citada na palestra.
- **Base:** a SEFAZ/SP exige **valor patrimonial atualizado / valor de mercado dos bens da PJ**, não o valor contábil histórico, quando este for menor (Decreto 46.655/2002, art. 14, §4º; jurisprudência TJSP). A ideia de pagar sobre o contábil de R$ 4.720.000 não sobrevive à fiscalização.
- Doação com reserva de usufruto: **2/3 do imposto na doação da nua-propriedade e 1/3 na extinção do usufruto** (a própria biblioteca marca "verificar" nesse dispositivo; o efetivo total em dinheiro é o mesmo — muda só o timing).

**Números (cenário recomendado: holding com os 11 imóveis; nua-propriedade de 50% das quotas doada — ver item 4; aplicações permanecem na PF):**
- Base da doação = valor de mercado das quotas doadas: 50% × 16.430.000 = 8.215.000 → 4% × 8.215.000 = **R$ 328.600**, sendo 2/3 = 219.066,67 no ato da doação e 1/3 = 109.533,33 na extinção do usufruto.
- Se 100% das quotas fossem doadas de uma vez (cenário da palestra): 4% × 16.430.000 = R$ 657.200 — mas isso excede o teto disponível (9.265.000) em 7.165.000 e seria inoficioso na parte excedente (ver item 4).
- Se as aplicações (R$ 2.100.000) também entrarem na PJ: base 18.530.000 → 4% × 18.530.000 = R$ 741.200.
- Comparação honesta: doando 328.600 agora **e** pagando no inventário 4% × 10.315.000 (herança remanescente: 8.215.000 de quotas + 2.100.000 de aplicações) = 412.600, a soma das duas transmissões é **R$ 741.200 = 4% × 18.530.000** — o mesmo ITCMD total que seria devido num único inventário sobre 18.530.000. **A estrutura não reduz o ITCMD total**; antecipa a transmissão com controle vitalício (usufruto), tira os imóveis do inventário e fixa a partilha em vida. A "vantagem" da palestra (4% × 4.720.000 = 188.800) não se sustenta perante a SEFAZ/SP: a base é o valor de mercado, não o contábil (4.720.000 × 4% = 188.800 é a promessa; o fiscal cobrará sobre 16.430.000).

## 4. "Quem você não quiser que herde, simplesmente não recebe quotas"

**Veredicto: FALSA.**

Fundamento (`library/cc_legitima_doacao.md`):
- Marcos é descendente e **herdeiro necessário** (CC arts. 1.845-1.846): pertence-lhe, de pleno direito, metade dos bens da herança (legítima, art. 1.789). **50% do patrimônio é indisponível** — `parcela_indisponivel_pct = 50`.
- Doar as quotas **só a Ricardo e Paula** é **doação inoficiosa** quanto à parte que invadir a legítima de Marcos — o art. 549 determina a **nulidade** do excesso, e o prejudicado pode exigir a **redução**.
- Doação de ascendente a descendente é **adiantamento de legítima** (art. 544) e sujeita-se a **colação** (art. 2.002) na apuração da herança.
- Marcos só sai da linha sucessória por **deserdação com causa legal** (arts. 1.961-1.965) ou indignidade — não por desenho societário.

**Números do teto disponível:** patrimônio atual ≈ 16.430.000 (imóveis) + 2.100.000 (aplicações) = 18.530.000 → disposição gratuita máxima (parte disponível) = 50% = **R$ 9.265.000**. A doação integral das quotas (16.430.000) excede o teto em 7.165.000 → essa parte é nula. Legítima individual de Marcos: 1/3 × 9.265.000 ≈ **R$ 3.088.333** (premissa destacada: patrimônio sem passivos — dívidas não informadas; Premissa D).

**O que é possível:** usufruto vitalício reservado (controle e renda enquanto viver); doação de nua-propriedade dentro do teto disponível; testamento disciplinando a metade disponível; eventual deserdação exige causa legal **provável em juízo** — a biblioteca lista os dispositivos (1.961-1.965) mas não reproduz suas causas legais, e o caso concreto (rompimento há 6 anos) precisa ser narrado por ela antes de qualquer decisão.

**Resposta ao pedido da cliente ("não quero que receba nada; se a lei obriga, o mínimo possível e com cláusulas de proteção"):** a lei garante a Marcos, no piso, 1/3 da legítima — colação incluída. Estrutura que entrega esse piso dentro da regra:

- **Doar nua-propriedade de 50% das quotas com reserva de usufruto vitalício**: base 8.215.000 a valor de mercado (teto disponível: 9.265.000 → folga de 1.050.000 para não pisar a fronteira da inoficiosidade), **em partes iguais a Ricardo e Paula** — 4.107.500 cada (premissa: divisão igualitária entre os dois; a cliente não especificou).
- **No falecimento**, com patrimônio constante: herança ≈ 8.215.000 (quotas restantes) + 2.100.000 (aplicações) = 10.315.000; somando as doações coladas, a base da legítima volta a 18.530.000 → legítima total 9.265.000 → **Marcos: R$ 3.088.333 ≈ 16,7% do patrimônio de hoje** (invariante: qualquer fração doada dentro do teto, a colação recomponhe a mesma legítima; doar mais ou menos não reduz o piso dele — abaixo disso só deserdação com causa legal). Ricardo e Paula, cada um, sob divisão testamentária igualitária (hipótese ilustrativa — a cliente não especificou): doação 4.107.500 + herança 3.088.333,33 + testamento 525.000 (½ × 1.050.000) ≈ **R$ 7.720.833 (41,7% cada)**; conferência: 3 × 3.088.333,33 + 8.215.000 + 1.050.000 = 18.530.000 ✓.
- **Cláusulas de proteção:** usufruto vitalício como escudo primário (renda e controle para ela, nada transacionável); nas doações, incomunicabilidade/impenhorabilidade/inalienabilidade **com justa causa documentada** (o CC 1.848 alcança a legítima, e a doação a descendente é adiantamento de legítima); sobre Marcos especificamente (na parte que recebe em herança), restrições só com justa causa declarada em testamento — a redação dessas cláusulas cabe ao advogado dela, fora do escopo aritmético deste parecer.
- **Identificação do limite:** o piso de Marcos (3.088.333) é igual à sua fração da legítima **incluindo** a colação — não é uma escolha do desenho, é o mínimo matemático do civil sob a biblioteca. A deserdação ou indignidade são as únicas saídas legais; as causas não estão reproduzidas na biblioteca (não verificáveis aqui), e exigirão fatos específicos e prova.

## 5. "Cláusulas de incomunicabilidade, impenhorabilidade e inalienabilidade protegem contra genros e credores"

**Veredicto: DEPENDENTE — parcialmente verdadeira, com limites materiais importantes.**

Fundamento (`library/cc_legitima_doacao.md`):
- **Art. 1.848:** o testador **não pode** impor impenhorabilidade/incomunicabilidade/inalienabilidade sobre o que pertence à **legítima**, salvo **justa causa declarada** no testamento. Como as quotas doadas a descendentes são adiantamento de legítima (art. 544), boa parte do patrimônio doado estará sujeita a essa limitação — as cláusulas não são automáticas nem absolutas sobre ela.
- Sobre cláusulas restritivas em **doações inter vivos fora da legítima**, a biblioteca não traz o dispositivo específico — **não verificável na biblioteca**; não afirmamos aqui regra alguma.
- Proteções confirmáveis com a biblioteca: incomunicabilidade afasta o cônjuge do donatário; impenhorabilidade resiste a penhora; inalienabilidade impede a alienação voluntária. A biblioteca **não** contém regras sobre (i) credores **do próprio donatário**, (ii) fraude contra credores do doador, (iii) efeitos conforme o regime de bens de cada filho — não temos os regimes de casamento/união estável dos três filhos (cliente sem informação adicional; Premissa D/E).
- A reserva de **usufruto** pela doadora dá controle e renda e fica, desde logo, fora do alcance dos genros enquanto durar — é a proteção mais robusta e imediata do plano.

**Síntese prática:** cláusulas úteis e em regra aceitas, mas (a) exigem justa causa quando tocam a legítima, (b) não são blindagem absoluta contra credores, e (c) nossa avaliação fica limitada ao que a biblioteca contém.

---

## Síntese — o que a palestra promete × o que os números mostram

| Afirmação | Veredicto | Número-chave |
|---|---|---|
| 1. Integralizar sem ITBI | Falsa no plano descrito | ITBI devido ≈ R$ 492.900 (3% × 16,43 mi) |
| 2. PJ paga só 11,33% vs 27,5% | Depende (números errados) | PJ 2026 ≈ 14,27% da receita vs 25,3% na PF (comissão 8% dedutível); economia ≈ R$ 112.398,32/ano |
| 3. ITCMD 4% sobre contábil | Falsa na base; alíquota certa | 4% × 8.215.000 (plano: 50% das quotas) = R$ 328.600; total da transmissão 741.200 — igual ao inventário |
| 4. Excluir quem quiser | Falsa | 50% indisponível; teto de doação R$ 9.265.000; piso de Marcos ≈ R$ 3.088.333 (invariante pela colação) |
| 5. Cláusulas protegem de todos | Depende | CC art. 1.848: na legítima, só com justa causa |

## Estrutura recomendada (nivelada aos números)

1. **Constituir holding (LTDA) patrimonial-locadora** com capital integralizado pelos 11 imóveis **ao valor declarado no IR** (R$ 4.720.000), nos termos de `library/lei9249_art23.md` — sem ganho de capital na integralização (GCAP evitado: 11.710.000 × 15% = R$ 1.756.500 na faixa mínima indicada pela biblioteca [15%-22,5%]; até 2.634.750 na superior — taxa de faixa não reproduzida na biblioteca, item em aberto).
2. **Reconhecer o ITBI** como custo do projeto (≈ 3% × valor venal; estimado R$ 492.900 pelo mercado) — a citação da "imunidade" da palestra não se aplica.
3. **Locação via PJ** no Lucro Presumido: carga 2026 estimada em 14,27% da receita vs 25,3% na PF (comissão 8% dedutível dos dois lados); economia ≈ R$ 112.398,32/ano; "payback" do ITBI ≈ 492.900 ÷ 112.398,32 = **4,39 anos**.
4. **Doar nua-propriedade de 50% das quotas com reserva de usufruto vitalício** a Ricardo e Paula em partes iguais — 4.107.500 cada, total 8.215.000 ≤ teto 9.265.000 (folga de 1.050.000) — resposta ao pedido de mínimo para Marcos: piso dele ≈ **R$ 3.088.333**, garantido pela colação e invariante às frações doadas dentro do teto; ITCMD da doação 4% × 8.215.000 = R$ 328.600 (2/3 = 219.066,67 no ato; 1/3 = 109.533,33 na extinção do usufruto); com o inventário sobre o remanescente (10.315.000 → 412.600), o ITCMD total do plano é 741.200 = 4% × 18.530.000, igual ao de um único inventário — a estrutura ganha em controle e timing, não em ITCMD.
5. **Testamento** disciplinando a parte disponível e, se for o caso dela, **deserdação** de Marcos somente com causa legal provável — decisão própria e assistida, nunca automática.
6. **Cláusulas restritivas** (inalienabilidade/impenhorabilidade/incomunicabilidade) onde couber, com justa causa documentada quando tocarem legítima; usufruto vitalício como proteção primária.
7. **Aplicações (R$ 2,1 mi) permanecem na PF** por ora: a biblioteca não trata da tributação da integralização de aplicações; Integralizá-las sem análise pode gerar ganho de capital — item em aberto (ver "Limites e premissas" abaixo).

## Limites e premissas (proeminentes)

- **Premissa A (PF):** IR carnê-leão pela alíquota de teto 27,5% sobre toda a renda tributável — a tabela progressiva (faixas) **não consta da biblioteca**; o IR real é algo menor. Dedução aplicada: **comissão da administradora 8%** (informada pela cliente; dedutível conforme `locacao_pf_vs_pj.md`). IPTU/condomínio dos **vagos**: pago pela cliente, mas **sem montante informado** e não vinculado a aluguel — não deduzido. IPTU/condomínio dos **locados**: sem informação de quem paga — não deduzido (se ela pagar algum com comprovante, a carga da PF cai e a vantagem da PJ diminui na mesma medida).
- **Premissa B (IRRF 2026):** 10% sobre o **excedente** de R$ 50 mil/mês (base de distribuição 67.772,03); a biblioteca não explicita a base (excedente ou total) — cenário alternativo (10% do total) quantificado no item 2. Item em aberto.
- **Premissa C (ITBI):** base estimada pelo **valor de mercado**; a base legal é o valor venal municipal, não informado.
- **Premissa D (patrimônio):** sem passivos/dívidas (não informados); legítima apurada sobre ativos.
- **Premissa E (sucessão):** patrimônio constante (18.530.000) até o falecimento; colação das doações a valor de mercado integral das quotas (a biblioteca não detalha como a colação apura nua-propriedade com usufruto); legítima dividida em partes iguais entre os 3 filhos; divisão da doação igualitária entre Ricardo e Paula (não especificada pela cliente).
- **Não verificável na biblioteca:** faixas da tabela progressiva do IRPF e do GCAP; base exata do IRRF da Lei 15.270/2025; art. 9º da Lei 10.705/2000 (o "2/3-1/3" vem com a ressalva "verificar" da própria biblioteca); **causas legais de deserdação** (arts. 1.961-1.965 listados, causas não reproduzidas — o rompimento de 6 anos, por si só, não foi confirmado como causa); regras sobre cláusulas restritivas em doação inter vivos fora da legítima; colação de nua-propriedade/usufruto; ISS no caso concreto; custas de inventário; LC 214/2025 (IBS/CBS sobre locação em 2026 é apenas apuração-teste; sem deltas monetários estimáveis com a biblioteca).
- **As decisões finais (deserdação, cláusulas, montante doado, estrutura societária detalhada)** exigem documentação e vontade da cliente; este parecer não substitui a documentação do projeto nem a constituição formal da holding, tampouco trata de direito registral/tabelional.

## Roteiro de cálculo (aritmética-show)

- Renda: 84.900 × 12 = 1.018.800 (confere com `documents/relacao_imoveis.csv`: soma dos aluguéis mensais linha a linha = 84.900).
- Mercado: soma dos `valor_mercado` = 16.430.000; declaração: soma = 4.720.000; diferença = 11.710.000.
- PF: comissão 8% × 84.900 = 6.792 → base 84.900 − 6.792 = 78.108 → 78.108 × 0,275 = 21.479,70/mês → × 12 = 257.756,40 (25,3% da receita).
- PJ: 84.900 × 0,32 = 27.168; 27.168 × 0,15 = 4.075,20 + (27.168 − 20.000) × 0,10 = 716,80 → 4.792,00; CSLL 27.168 × 0,09 = 2.445,12; PIS/COFINS 84.900 × 0,0365 = 3.098,85; total mensal 10.335,97 → × 12 = 124.031,64 (12,17%).
- IRRF 2026 (excedente): 84.900 − 6.792 − 10.335,97 = 67.772,03; excedente 67.772,03 − 50.000 = 17.772,03; × 10% = 1.777,20/mês → 21.326,44/ano.
- Carga PJ total: 124.031,64 + 21.326,44 = 145.358,08 (14,27% da receita). Economia vs PF: 257.756,40 − 145.358,08 = 112.398,32; payback ITBI: 492.900 ÷ 112.398,32 = 4,39 anos.
- ITBI: 16.430.000 × 0,03 = 492.900. Tema 796: 3% × 4.720.000 = 141.600 "dentro do capital" + 3% × 11.710.000 = 351.300.
- GCAP evitado: 11.710.000 × 0,15 = 1.756.500 (faixa mínima da biblioteca).
- ITCMD: 100% das quotas = 16.430.000 × 0,04 = 657.200 (inoficioso acima do teto); plano recomendado: doação 8.215.000 × 0,04 = 328.600 (2/3 = 219.066,67; 1/3 = 109.533,33) + inventário sobre 10.315.000 × 0,04 = 412.600 → total do plano 741.200 = 4% × 18.530.000 (inclui imóveis e aplicações).
- Legítima: 18.530.000 × 50% = 9.265.000; por filho: ÷ 3 = 3.088.333,33. Conferência do plano mínimo: herança 10.315.000 + colação 8.215.000 = 18.530.000 ✓; Marcos 3.088.333,33; Ricardo/Paula: 4.107.500 (doação) + 3.088.333,33 (herança) + 525.000 (testamento) = 7.720.833,33; soma: 3.088.333,33 + 2 × 7.720.833,33 = 18.530.000 ✓.
