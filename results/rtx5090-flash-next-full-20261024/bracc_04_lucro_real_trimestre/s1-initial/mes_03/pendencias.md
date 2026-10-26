# Pendências — março/2026 e fechamento do 1º trimestre/2026 (sessão 3/3)

**Status da sessão: BLOCKED** para apuração numérica; **entregues em estrutura** todos os arquivos
obrigatórios do contrato (`ajustes.json`, `pis_cofins.json`, `pendencias.md`, `lalur.json`,
`memoria.md`), com as chaves do `lalur.json` em `null` onde falta dado.

Duas causas independentes:

| # | Causa | Registros em `deliverable/UNKNOWN.md` |
|---|---|---|
| 1 | Razão/balancete de fevereiro e março não entregues (o cliente declarou em 26/10/2026 não ter informação adicional) | U-01, U-02, U-14, U-15 |
| 2 | Brindes e doação confirmados como existentes, sem valor e sem competência | U-03, U-04, U-05 |

Não há terceira causa pendente de decisão nossa: o memorial (`mes_03/memoria.md`) já fixa o fundamento de
cada linha do e-LALUR e a fórmula a executar.

---

## 1. O que é preciso para fechar (pedido único, não repetimos perguntas respondidas)

`documents/mes_02/razao.csv`, `documents/mes_02/balancete.csv`, `documents/mes_03/razao.csv`,
`documents/mes_03/balancete.csv` — mesmo layout dos de janeiro. Com isso:

1. rodam os testes T1–T7 (`mes_02/ajustes.json`) sobre os dois meses;
2. fecha o resultado contábil de fevereiro e março e o acumulado do 1T2026;
3. a compensação entra como MIN(30% × lucro antes da compensação; 900.000,00);
4. IRPJ 15% + adicional 10% sobre o que exceder R$ 60.000,00 no trimestre + CSLL 9%;
5. Parte B com os saldos remanescentes.

Nada disso depende de nova pergunta ao cliente — só dos arquivos.

## 2. Para as adições, falta um número (e uma data), não uma discussão jurídica

- **Brindes** (vinho + canivete gravado, 400 clientes): indedutibilidade firme — Lei 9.249/95, art. 13, VII
  (`library/lei9249_art13.md`). Falta o valor (U-03). Teto demonstrável em janeiro: R$ 85.000,00 (4.2.02).
- **Doação à Associação Luz**: sem título de utilidade pública federal nem qualificação de OSCIP, está fora
  do art. 13, § 2º, II → doação indedutível (art. 13, VI). Falta o valor (U-04). Teto demonstrável conjunto
  em janeiro: R$ 181.000,00 (4.2.02 + 4.2.03).
- **Competência** (U-05): se as duas despesas forem de 4T2025, a adição correta é de e-LALUR/ECF de 2025 e o
  1T2026 fica sem elas; a correção de 2025 não pode ser quantificada sem o valor. Enquanto isso, as linhas
  permanecem `null` no `lalur.json` — criadas, não omitidas.
- Qualquer uma destas três vias fecha o item: (a) detalhamento por documento de 4.2.02/4.2.03, (b) valor
  declarado pelo cliente com suporte, (c) instrução escrita de não apurar por insuficiência de registro.
  O custo de cada caminho está tabulado em `deliverable/QUESTIONS.md` § 4; o registro do desconhecido é
  U-03/U-04/U-05 em `deliverable/UNKNOWN.md`.

## 3. Efeito mensurável de não ter o número

Cada R$ 1.000,00 de adição não lançada custa R$ 238,00 de IRPJ/CSLL no trimestre (o teto de compensação
absorve 30%, então só 70% da adição viram base: 0,34 × 700 = 238). Com o teto demonstrável de janeiro, a
forquilla é de **R$ 20.230,00 a R$ 43.078,00** de tributo (85.000 → 181.000 de adição, alíquota efetiva de
23,8% sobre a adição nesse regime); abaixo de R$ 60.000,00 de lucro real trimestral cai para 16,8% e fica
entre R$ 14.280,00 e R$ 30.408,00. Memória completa, com os quatro cenários, em `mes_03/memoria.md` § 8.

## 4. Alertas de fechamento do trimestre (o que não vai mudar de posição)

1. **Compensação integral do prejuízo não será feita.** Teto de 30% do lucro líquido ajustado pelas adições
   e exclusões (Lei 9.065/95, arts. 15 e 16; Lei 8.981/95, arts. 42 e 58; RE 591.340/Tema 117 —
   `library/lei9065_art15_trava.md`). Compensar os R$ 900.000,00 exigiria lucro ajustado trimestral de
   **R$ 3.000.000,00** (23,35× janeiro). No ritmo demonstrado, o trimestre consome 12,85% do saldo e a
   absorção completa levaria ≈ 7,8 trimestres. A trava **difere**, não elimina o crédito.
2. **Abertura da Parte B sem comprovação.** R$ 900.000,00 de prejuízo fiscal e R$ 900.000,00 de base
   negativa (`documents/saldos_fiscais_abertura.md`) entram **como declarados**, com ressalva, até a ECF
   anterior (U-08). Sem a ECF, também não revisamos a higidez do saldo.
3. **Provisão do IRPJ/CSLL do trimestre** (AJ-03, modelo em `mes_03/ajustes.json`): recomendação de
   regime de competência, em contas novas (sugerido 4.3.02 despesa / 2.1.05 a recolher) porque o plano de
   contas do razão não tem conta para tributos da renda. **[NÃO VERIFICÁVEL]** pela biblioteca — não há
   norma CPC nela (U-13). Já o que a biblioteca sustenta vale em sentido contrário: as adições de brindes e
   doação **não** tocam a contabilidade societária, apenas a apuração fiscal
   (`library/irpj_csll_trimestral.md`).
4. **Retificações em cadeia:** EFD-Contribuições de 01/2026 (exclusão do crédito de R$ 11.100,00) já
   formalizada em janeiro; situação de transmissão/pagamento desconhecida (U-06) e acréscimos não
   calculados por falta de norma na biblioteca (U-07). Se T3 achar crédito sobre uso e consumo em
   fevereiro/março, estorna e retifica na competência respectiva.
5. **PIS/COFINS não tem apuração trimestral** — continua mês a mês; o "consolidado do trimestre" em
   `mes_03/pis_cofins.json` está `null` porque fevereiro e março não foram apurados.

## 5. Consequência para o status do engajamento

Janeiro: **COMPLETE WITH OPEN ITEMS**. Fevereiro e março: **BLOCKED** (falta dado de entrada), com os
entregáveis obrigatórios presentes e estruturados. Trimestre: **BLOCKED** — a apuração de IRPJ/CSLL é do
trimestre inteiro e não pode ser feita com 1 mês de 3; o `lalur.json` entregue **não deve ser transmitido**
enquanto as chaves obrigatórias estiverem `null`. Ver `deliverable/STATUS.md`.
