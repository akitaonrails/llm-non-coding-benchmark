Vou auditar em três eixos: (1) cada autoridade citada confere com o texto da biblioteca; (2) toda aritmética fecha entre arquivos; (3) nada fica "solto" entre entregáveis. Primeiro, o texto integral das autoridades:

Autoridades conferidas. Agora as checagens sistemáticas — fontes primárias e citações nos entregáveis:

O único MISS é a redação exata da 5.7. Vou recuperar o texto real da cláusula 5.7 na minuta e verificar onde os entregáveis usam essa formulação:

Diagnóstico completo. Vou ler a seção da tabela da carta da rodada 3 e checar o "18" no STATUS antes de editar:

Revalidação completa — JSON, citações vs. INDEX, termos antigos e aritmética:

Tudo íntegro. Registro a auditoria no STATUS.md para fechar a trilha:

Corrigindo um erro de digitação que acabei de introduzir:

Revisão pré-entrega concluída. Auditoria: as 7 autoridades da biblioteca lidas por inteiro e conferidas 1× contra cada citação; 26 fatos verificados por regex direto nos PDFs/e-mail; aritmética refeita em Python; JSON revalidado. **Tudo fechou** — e encontrei 7 problemas reais, já corrigidos:

## O que mudou

1. **Citação de autoridade errada — `achados.json` (item Sorocaba)**: "CTN arts. 132–133" → agora atribuído à **nota de `ctn_133_sucessao.md`**. O corpo do arquivo só trata do art. 133; a proposição (certidão positiva impede novas certidões) vem da nota dele, não do art. 132.

2. **Autoridade fora da biblioteca — `resposta_representante_comprador_8-4c.md`**: removi "(e a boa-fé objetiva)" — princípio que nenhum arquivo da biblioteca sustenta. Substituído pela prática citada em `sandbagging_franquia_mercado.md`. (Os outros "boa-fé" restantes são descritivos, não citação de autoridade — mantidos.)

3. **Número sem lastro — carta da rodada 3**: "tetos específicos ≈ R$ 1,42 mi" aparecia sem origem. Agora com derivação explícita na nota: R$ 400 mil (IRPJ) + R$ 1.020.000 (parcela não provisionada das ações) — e o aviso de que **PJ e ISS ainda não entraram nesse total** (ele crescerá quando os dados vierem). A tabela de sensibilidade (2,92/3,67/4,42 mi) confere com essa premissa.

4. **Inconsistência conceitual — a "reclamação mínima de R$ 1.850.000"** (carta, `nota_socios.md`, `achados.json`, STATUS): a multa HZ (~R$ 520 mil) **não é reclamável pelas reps atuais** — é risco da empresa que o comprador tentaria cobrir via CP/holdback/desconto de preço. Reclassificado em todos os arquivos: **R$ 1.330.000 diretamente reclamáveis pelas reps 5.7/5.9** (1,02 mi + 310 mil) + R$ 520 mil de risco HZ estimado = R$ 1.850.000 de risco quantificado total. Isso inclusive reforça o argumento da nossa exigência de anuência HZ como condição no Anexo 3.2.

5. **Citações diretas da cl. 5.7 desalinhadas**: quatro arquivos traziam "inexiste risco"/"não existe risco" entre aspas; a minuta diz "**inexistindo** risco de reconhecimento de vínculo empregatício". Alinhado em `nota_socios.md`, `resposta_advogado_comprador.md`, `resposta_representante_comprador_8-4c.md` e `achados.json`. (Detalhe da auditoria: o MISS no meu check automático era do regex, não da cotação do redline — que já estava exata.)

6. **Teto IRPJ ~R$ 400 mil sem derivação — `redline.md`**: agora "[~R$ 400.000 = R$ 310.000 + ~R$ 90.000 de correção/multas (estimativa a confirmar com a planilha de cálculo)]" — coerente com o rotulado nos demais arquivos.

7. **Contagem desatualizada — `STATUS.md`**: "18 achados" → "19 achados" (o item novo da rodada 3 estava fora).

## O que a auditoria confirmou (sem mudança)

- CADE: limiares cumulativos 750/75 mi e os R$ 390 mi/R$ 4,2 mi constam do próprio `cade_limiares.md` → não notificável, condição suprimida;
- 10–20% de cap, franquia dedutível e 2–3 anos de sobrevivência: todos suportados por `sandbagging_franquia_mercado.md`;
- JUCESP não exige CND, CLT 10/448/448-A, CC 1.147 (com a contenção de excesso pelos tribunais), Lei 14.133 arts. 92 XVI/137 VI: todos conferem com o texto dos arquivos;
- 25/26 checagens de fonte primária OK na primeira tentativa (HZ 2024–2028, cl. 19 = 20% do saldo, 11 PJs, 3 ações de 1,4 mi com provisão de 380 mil, CND 310 mil, 044/2025 a 12%, preferência 30 dias, escrow 20%/5 anos, 8.4(a)–(d), earn-out 35% acima de 1,1 mi com cap 1,5 mi, 45 dias);
- Earn-out: limiar = 26,2% da receita; cap exige EBITDA ≥ R$ 5.385.714 > receita total — matematicamente inalcançável, como escrito.

`STATUS.md` ganhou um parágrafo registrando esta auditoria e permanece **COMPLETE WITH OPEN ITEMS** — os abertos continuam sendo os dados que só o cliente/comprador têm (preço, base dos PJs, ISS, saldo HZ), listados em `QUESTIONS.md`. Pronto para entrega.