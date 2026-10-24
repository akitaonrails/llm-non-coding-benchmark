# STATUS — DAS maio/2026, Lumen Soluções Digitais ME

## COMPLETE WITH OPEN ITEMS

Entregáveis presentes: `apuracao.json`, `memoria.md`, `PERGUNTAS.md` (+`QUESTIONS.md`, exigido pela
regra de trabalho), `STATUS.md`. Esta é a **versão 2**, que incorpora o esclarecimento do cliente
(pró-labore de abril pago em 30/04/2026; glosa da 1184 = cancelamento de receita) e **substitui** a
versão 1 (que apontava Anexo V / DAS 15.188,84).

Resultado apurado com as premissas declaradas (detalhe e aritmética em `memoria.md`):

- RBT12 = R$ 1.020.000,00 → 4ª faixa (serviços e locação).
- Fator R em regime de **pagamento** (Res. CGSN 140, art. 26, §§1º–2º): folha 12m = R$ 287.800,00
  (193.000 salários + 38.400 pró-labore + 56.400 CPP/FGTS) → **28,22% ≥ 28% → serviços no Anexo III**
  (alíquota efetiva 12,5059%). Locação de notebooks segregada no **Anexo III sem ISS** (SV 31), e não
  “junto com os serviços”, como pedia o sócio.
- **DAS maio/2026 = R$ 10.261,08** (serviços 78.000,00 → 9.754,59; locação 6.000,00 → 506,49).
- Estorno parcial de R$ 4.000,00 (glosa confirmada pelo cliente) reduz a receita de serviços de maio
  (82.000 → 78.000).

**DEPENDÊNCIA CRÍTICA:** o resultado acima depende do pró-labore de abril (R$ 3.200,00) ter sido pago
em **30/04/2026** (palavra do cliente; o comprovante foi anunciado — “Te mando” — e **ainda não chegou**
a `documents/`). Se o pagamento foi em 06/05/2026 (versão do e-mail do sócio), a folha paga cai para
284.600 → Fator R 27,90% → **Anexo V** → DAS **15.188,84**. Diferença: **R$ 4.927,76** (memoria §5.2).

## Itens abertos

1. **Comprovante do pró-labore pago em 30/04/2026 (material, aguardando envio do cliente).** É o único
   fator que separa Anexo III (10.261,08) de Anexo V (15.188,84). Margem do Fator R sobre o limiar:
   apenas R$ 2.200,00 de folha.
2. **Premissa do encargo patronal (CPP/FGTS):** pagamentos com 1 mês de defasagem (evidência:
   DARF/GPS/FGTS ABR em 07/05); para fechar a janela de pagamentos adotou-se abr/2025 = R$ 4.700,00
   (mês não documentado; valor constante nas 12 linhas do resumo). Se abr/2025 foi diferente, o Fator R
   move-se junto. Robustez testada (memoria §5.2): por ser constante, o CPP é insensível ao recorte da
   janela; e mesmo que os salários tivessem a mesma defasagem de 1 mês (contra a evidência do extrato),
   o Anexo III se sustentaria até que a competência abr/2025 de salários fosse < R$ 14.500,00
   (vizinhas documentadas: 15.500–16.700).
3. **Segregação do faturamento dos 12 meses por atividade não fornecida.** Assumido que o
   `faturamento_12_meses.csv` é receita bruta total de todas as atividades (leitura literal de
   LC 123/2006 art. 18 §1º e §§5º-J/5º-M, que falam em “receita bruta”). Se houve locação nos 12
   meses, a RBT12 usada no Fator R é a total — adotada; não há regra na biblioteca exigindo receita de
   serviços segregada para o denominador do Fator R. Cliente informou não ter essa segregação.
4. **Escopo de “TI” no §5º-J para as NFS-e 1183 (consultoria de arquitetura) e 1186 (treinamento).**
   Biblioteca lista “desenvolvimento, licenciamento, suporte etc.”; tratei-as como TI do mesmo negócio.
   Se alguma não for TI, a biblioteca não tem Anexo I/II/IV para enquadrá-la — cliente informou não ter
   mais informação.
5. **DAS de abril/2026 (R$ 10.480,22) não reconcilia de forma fechada** com a biblioteca (RBT12 de
   abril não documentada). Observação: o valor é compatível com Anexo III (receita de abril ≈ 84 mil)
   e incompatível com Anexo V (exigiria ≈ 56 mil) — a prática recente aparenta ser Anexo III, apesar da
   fala do sócio sobre “ano passado”. Recomendação de revisão das guias de 2026 é **não verificada**
   (biblioteca não contém regras de retificação).
6. **Repartição da biblioteca soma 99,85%**, não 100%: a repartição consolidada (10.245,31) fica
   R$ 15,77 abaixo do DAS total (10.261,08). Deixado à vista, não balanceado.

Itens já respondidos pelo cliente (não re-perguntados): pró-labore de abril pago em 30/04 (Q1);
natureza do estorno da 1184/1188 como cancelamento de receita (Q3). Ver `QUESTIONS.md`.
