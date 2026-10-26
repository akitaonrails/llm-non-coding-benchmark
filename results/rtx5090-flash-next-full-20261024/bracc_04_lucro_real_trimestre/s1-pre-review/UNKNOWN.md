# UNKNOWN — registro explícito de desconhecidos (Atlas Distribuidora S.A., 1º trimestre/2026)

Atualizado em 26/10/2026 (rodada 3). O cliente informou que **não tem informação adicional** sobre os
pontos em aberto. Este arquivo é o registro fechado de tudo que **não sabemos**, com o impacto de cada
lacuna. Nada aqui foi preenchido por estimativa: onde há número, ele é **limiar/exposição**, nunca fato
apurado.

Legenda de efeito: **[BLOQUEIA]** impede produzir o entregável · **[VALOR]** impede medir o tributo ·
 **[RESSALVA]** não impede o número, mas impede afirmar conformidade.

| ID | Desconhecido | O que falta | Efeito | Como está tratado | Como se encerra |
|---|---|---|---|---|---|
| U-01 | Razão analítico e balancete de **fevereiro/2026** | arquivo | **[BLOQUEIA]** `mes_02/*` | arquivos de `mes_02/` entregues com valores `null` e checklist de testes, sem número inventado | enviar o razão/balancete (formato de janeiro) |
| U-02 | Razão analítico e balancete de **março/2026** | arquivo | **[BLOQUEIA]** `mes_03/*`, `lalur.json`, `memoria.md` | idem; apuração do trimestre não pode ser montada com 1 mês de 3 | idem |
| U-03 | **Valor das despesas com brindes** (vinho + canivete gravado, 400 clientes) | documento/valor | **[VALOR]** adição do art. 13, VII no e-LALUR | linha de adição `null` no `lalur.json`; exposição por teto em `mes_01/brindes_doacoes.md` | razão analítica de 4.2.02/4.2.03, NF-e de remessa de brinde, ou instrução escrita de não apurar por insuficiência de registro |
| U-04 | **Valor da doação à Associação Luz** | documento/valor | **[VALOR]** adição do art. 13, VI | idem; a entidade não tem título de utilidade pública federal/OSCIP, então é indedutível na totalidade | extrato/TED/recibo, ou instrução escrita |
| U-05 | **Competência** dos brindes e da doação (1T2026 × 4T2025) | data | **[VALOR] + [RESSALVA]** | alocado em 1T2026 por **assunção declarada**; se for de 2025, a correção é de e-LALUR/ECF de 2025 e o 1T2026 fica sem essa adição | data da despesa / documento fiscal |
| U-06 | Situação da **EFD-Contribuições e do DAS de 01/2026** (transmitido? pago?) | informação | **[VALOR]** apenas para acréscimos | apuração correta entregue (a recolher R$ 79.883,00); se já transmitida → EFD retificadora + diferença de R$ 11.100,00 | extrato da EFD/DAS ou recibo de transmissão |
| U-07 | **Acréscimos legais** sobre R$ 11.100,00 | norma (fora da biblioteca) | **[VALOR]** | **não calculado** — `library/INDEX.md` não contém norma de multa/juros; apontado para apuração na transmissão | informação da situação (U-06) + norma aplicável |
| U-08 | Comprovação dos **saldos de abertura**: prejuízo fiscal R$ 900.000,00 e base negativa R$ 900.000,00 | ECF do exercício anterior | **[RESSALVA]** | carregados na Parte B **como declarados pela empresa**; sem ECF, o direito de compensar não está demonstrado | ECF/DIRPJ anterior com a linha de saldos a compensar |
| U-09 | **Credor** dos Empréstimos (2.1.04, R$ 2.400.000,00) e natureza dos juros de R$ 28.000,00 | contrato/extrato | **[RESSALVA]** | nenhum ajuste; **não verificado** — a biblioteca não tem norma de dedutibilidade de juros/encargos nem de partes relacionadas | contrato e cadastro do credor |
| U-10 | Vida útil **fiscal** do imobilizado × depreciação contábil (R$ 51.667,00/mês sobre R$ 6.200.000,00) | norma (fora da biblioteca) | **[VALOR]** potencial (adição/exclusão no LALUR) | aceita como base contábil; divergência fiscal não verificada | tabela de depreciação fiscal |
| U-11 | Correção do **ICMS** sobre vendas (R$ 177.800,00, "7% líquido de créditos") e eventual crédito de ICMS/IPI na NF-e 8812 | norma (fora da biblioteca) | **[RESSALVA]** | **fora do escopo**: nenhuma norma de ICMS/IPI na biblioteca; nenhuma afirmação de conformidade | outro escopo, com a legislação estadual |
| U-12 | Desdobramentos de **PIS/COFINS/ICMS/IPI na remessa de brindes e na doação de bens** | norma (fora da biblioteca) | **[RESSALVA]** | não analisados; **não** devem ser lidos como conformidade | legislação específica (fora do arquivo) |
| U-13 | **Tributação diferida** / política contábil de provisão mensal de IRPJ/CSLL | norma (fora da biblioteca) + política | **[RESSALVA]** | nada provisionado em janeiro (regime trimestral — `library/irpj_csll_trimestral.md`); eventual efeito diferido não verificado | política contábil da companhia |
| U-14 | Se o **erro da NF-e 8812 se repete** em fev/mar (CFOP 1556 com crédito tomado) | dados (U-01/U-02) | **[VALOR]** | um único caso em janeiro (razão: refs `NF8812`, linhas 36-38 de `documents/mes_01/razao.csv`); teste prescrito no checklist de `mes_02/pendencias.md` | rodar o teste quando chegarem os razão |
| U-15 | Existência de **outras despesas indedutíveis** do art. 13 no trimestre (multas, despesas com veículos sem vínculo, representação etc.) | dados | **[VALOR]** | varredura prescrito no checklist; a biblioteca só permite afirmar o que está no razão de janeiro | razão analítico dos 3 meses |
| U-16 | Posição **formal** da administração sobre as duas instruções recusadas ("não mexer no crédito" / "compensar todo o prejuízo") | documento | **[RESSALVA]** | instruções **não atendidas**, com fundamento; divergência registrada em `mes_01/ajustes.json` (`correspondencia_cliente`) | deliberação/manifesto por escrito da diretoria |
| U-17 | **Prazo / decadência do prejuízo fiscal** e da base negativa a compensar (se prescrevem, se há ordem de uso por exercício) | norma (fora da biblioteca) | **[RESSALVA]** sobre a Parte B | saldos tratados como **compensáveis sem limite de prazo** porque a biblioteca não traz nenhuma regra de prazo; os R$ 784.365,30 (cenário A) pressupõem lucro futuro nos trimestres seguintes — se não houver, o crédito não vira tributo pago, deixa de ser usado | norma aplicável (fora do arquivo) + ECF anterior (U-08) |

## O que os desconhecidos não impediram

Janeiro está fechado e conferido: razão × balancete batem conta a conta (14 contas, R$ 19.880.584,00
nos dois lados), estorno AJ-01 (R$ 11.100,00) e compensação de crédito AJ-02 (R$ 155.067,00) lançados
em partida dobrada (R$ 166.167,00), balancete ajustado quadrado (R$ 20.046.751,00), PIS/COFINS a
recolher **R$ 79.883,00** e resultado do mês **R$ 128.483,00**.

## O que eles impedem

A apuração de IRPJ/CSLL do trimestre. Com um único mês conhecido, o máximo demonstrável é a **trava de
30%** sobre o resultado de janeiro: 128.483,00 × 30% = **R$ 38.544,90** de compensação, sobrando
R$ 861.455,10 de prejuízo fiscal na Parte B. Para compensar os R$ 900.000,00 por inteiro seria preciso lucro
líquido ajustado trimestral de **R$ 3.000.000,00** — 23,35× o resultado de janeiro. A instrução do
diretor ("compensar todo o prejuízo") é **aritmeticamente impossível** no ritmo atual do trimestre
(`library/lei9065_art15_trava.md`).
