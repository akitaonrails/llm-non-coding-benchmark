# Vértice Engenharia Consultiva Ltda. — comparação tributária de 2026

**Conclusão provisória.** Pelos dados recebidos e pelas premissas abaixo, permanecer no Simples custa cerca de **R$ 975.600**, contra **R$ 1.111.120** no Lucro Presumido e **R$ 1.112.290** no Lucro Real. Não recomendo a mudança pedida para o Lucro Real. A estimativa do Simples **não é um cálculo legal fechado**: a biblioteca autorizada não contém a tabela do Anexo IV necessária para os 15% de obras. A base de remuneração previdenciária também não foi informada. Esses dois pontos exigem validação antes de qualquer opção efetiva. Os valores do `comparativo.json` são estimativas condicionais, em reais, para o ano inteiro.

## Dados e premissas

| Item | Base usada | Situação |
|---|---:|---|
| Receita anual e RBT12 | R$ 4.200.000 | Projeção estável para 2026; RBT12 mensal constante é premissa. |
| Obras com materiais | R$ 630.000 = 15% | Confirmado pelo cliente; tratadas como empreitada com emprego de materiais. |
| Consultoria | R$ 3.570.000 = 85% | Diferença da receita total; Anexo III conforme regime informado. |
| Lucro antes de IRPJ/CSLL | R$ 756.000 = 18% × R$ 4.200.000 | Usado como lucro tributável no Real, sem ajustes fiscais conhecidos. |
| Folha sujeita à contribuição patronal | R$ 1.300.000 | **Proxy superior e incerta:** o número do balancete inclui encargos e FGTS, que não integram integralmente a base. |
| RAT/FAP/terceiros | 28% ao todo | Taxa típica estimada, sem dados específicos da empresa [inss_patronal.md](../library/inss_patronal.md). |
| ISS | 5% × receita integral = R$ 210.000 | Alíquota informada pelo cliente; pressupõe base integral também nas obras, sem deduções ou retenções. |

O enquadramento como EPP continua possível com receita anual de R$ 4,2 milhões, abaixo do teto de R$ 4,8 milhões. A empresa ultrapassa o sublimite de R$ 3,6 milhões para ISS; na projeção, o imposto é calculado fora do DAS. O momento exato em que isso ocorreu não foi informado; a comparação anual pressupõe que o tratamento fora do DAS vale durante todo 2026. A lei distingue o início dos efeitos conforme o percentual do excesso [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md). O Anexo III da 6ª faixa atribui ISS de 0% no DAS [anexo_iii_faixa6.md](../library/anexo_iii_faixa6.md).

## Memória de cálculo

### Simples Nacional

As receitas precisam ser segregadas: consultoria no Anexo III e obras com emprego de materiais no Anexo IV [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md). A receita de obras não pode ser integralmente tributada no Anexo III.

- **Consultoria, Anexo III:** alíquota efetiva = (R$ 4.200.000 × 33% − R$ 648.000) ÷ R$ 4.200.000 = **17,57142857%**. DAS = R$ 3.570.000 × 17,57142857% = **R$ 627.300** [anexo_iii_faixa6.md](../library/anexo_iii_faixa6.md).
- **Obras, Anexo IV — premissa legal não verificada:** para permitir uma estimativa numérica, foi *suposta* alíquota nominal de 33% e parcela a deduzir de R$ 828.000 na 6ª faixa. Essa tabela **não está na biblioteca e não é citada como direito vigente**. Sob essa hipótese, alíquota efetiva = (R$ 4.200.000 × 33% − R$ 828.000) ÷ R$ 4.200.000 = **13,28571429%**; DAS = R$ 630.000 × 13,28571429% = **R$ 83.700**. O DAS combinado estimado é R$ 627.300 + R$ 83.700 = **R$ 711.000**. O valor de Anexo IV é o principal item pendente de fonte autorizada.
- **ISS fora:** R$ 4.200.000 × 5% = **R$ 210.000**.
- **Contribuição patronal fora do DAS sobre obras:** proxy de folha das obras = R$ 1.300.000 × 15% = R$ 195.000; contribuição estimada = R$ 195.000 × 28% = **R$ 54.600**. O rateio por receita é uma premissa, não foi informado pelo cliente. A CPP de consultoria no Anexo III integra o DAS; no Anexo IV, é paga à parte [inss_patronal.md](../library/inss_patronal.md).
- **Total estimado:** R$ 711.000 + R$ 210.000 + R$ 54.600 = **R$ 975.600**.

### Lucro Presumido

As bases de presunção para empreitada com materiais são 8% para IRPJ e 12% para CSLL; para consultoria, 32% para ambos. As alíquotas e o adicional estão em [lei9249_9430_presumido.md](../library/lei9249_9430_presumido.md). A receita foi distribuída uniformemente entre trimestres para aplicar o limite anual equivalente de R$ 240.000 ao adicional.

- Base IRPJ = R$ 630.000 × 8% + R$ 3.570.000 × 32% = **R$ 1.192.800**. IRPJ = R$ 1.192.800 × 15% + (R$ 1.192.800 − R$ 240.000) × 10% = R$ 178.920 + R$ 95.280 = **R$ 274.200**.
- Base CSLL = R$ 630.000 × 12% + R$ 3.570.000 × 32% = **R$ 1.218.000**. CSLL = 9% × R$ 1.218.000 = **R$ 109.620**.
- PIS/COFINS cumulativos = R$ 4.200.000 × (0,65% + 3%) = **R$ 153.300**, sem créditos [lei9249_9430_presumido.md](../library/lei9249_9430_presumido.md).
- ISS = **R$ 210.000**. Contribuição patronal estimada = R$ 1.300.000 × 28% = **R$ 364.000** [inss_patronal.md](../library/inss_patronal.md).
- **Total:** R$ 274.200 + R$ 109.620 + R$ 153.300 + R$ 210.000 + R$ 364.000 = **R$ 1.111.120**.

### Lucro Real

Adotou-se o lucro contábil de R$ 756.000 como base tributável, sem adições, exclusões ou compensações. **A biblioteca não contém regra geral de apuração do IRPJ/CSLL no Lucro Real**; o uso de alíquotas de 15% de IRPJ, adicional de 10% acima de R$ 240.000 anuais e 9% de CSLL nesta simulação é **premissa jurídica não verificada para esse regime**, tomada dos percentuais apresentados apenas no material do Presumido [lei9249_9430_presumido.md](../library/lei9249_9430_presumido.md). A base e a apuração trimestral dependem de conferência antes de optar.

- IRPJ estimado = R$ 756.000 × 15% + (R$ 756.000 − R$ 240.000) × 10% = R$ 113.400 + R$ 51.600 = **R$ 165.000**.
- CSLL estimada = R$ 756.000 × 9% = **R$ 68.040**.
- Débito PIS/COFINS = R$ 4.200.000 × (1,65% + 7,6%) = **R$ 388.500** [pis_cofins_nao_cumulativo.md](../library/pis_cofins_nao_cumulativo.md).
- Créditos estimados = R$ 900.000 × 9,25% = **R$ 83.250**; PIS/COFINS líquido = **R$ 305.250**. O CSV detalha R$ 420.000 de perfis metálicos, R$ 280.000 de cabos e quadros e R$ 200.000 de licenças CAD/BIM. O crédito sobre software pressupõe uso essencial ou relevante na consultoria e documentação hábil, ainda não confirmados. Os R$ 500.000 restantes (móveis, veículos e papelaria) ficam fora por uso administrativo; folha e pró-labore pagos a pessoas físicas tampouco geram esses créditos [pis_cofins_nao_cumulativo.md](../library/pis_cofins_nao_cumulativo.md). A indicação de ICMS-ST nos R$ 700.000 de materiais não demonstra, por si, direito a crédito de PIS/COFINS; a premissa é o uso como insumo.
- ISS = **R$ 210.000**. Contribuição patronal estimada = **R$ 364.000**.
- **Total:** R$ 165.000 + R$ 68.040 + R$ 388.500 − R$ 83.250 + R$ 210.000 + R$ 364.000 = **R$ 1.112.290**.

O crédito sugerido pelo sócio, 9,25% sobre todas as compras de R$ 1,4 milhão, seria R$ 129.500. Ele supera a estimativa justificada de R$ 83.250 em **R$ 46.250**. Se o software de R$ 200.000 não atender ao critério de insumo, os créditos caem a R$ 64.750 e o total do Real sobe a R$ 1.130.790.

## Sensibilidade e itens abertos

Com o DAS do Anexo IV **hipotético** de R$ 83.700, o Simples antes da contribuição patronal seria R$ 921.000, contra R$ 747.120 no Presumido e R$ 748.290 no Real. Se a base de remuneração efetivamente sujeita à contribuição for `F`, e 15% dela estiver ligada às obras, os totais seriam respectivamente `921.000 + 0,042 × F`, `747.120 + 0,28 × F` e `748.290 + 0,28 × F`. Nessas hipóteses, o Simples fica abaixo do Presumido quando `F` excede **R$ 730.588,24** e abaixo do Real quando excede **R$ 725.672,27**. A folha informada, de R$ 1,3 milhão **incluindo encargos e FGTS**, não comprova essa base. Logo, a recomendação é condicional, embora a diferença estimada seja favorável ao Simples.

Permanecem sem resposta: a fonte autorizada da tabela do Anexo IV; a folha tributável e sua alocação às obras; RAT/FAP e terceiros específicos; eventuais ajustes do lucro tributável; elegibilidade e documentação do crédito de software; possíveis deduções/retenções de ISS; e a trajetória mensal da RBT12. Não há informação suficiente para resolver esses itens. Não se deve tratar os números apresentados como valor devido em guia.

## Pedido de mudança e procedimento

**Não é possível trocar de regime somente para dezembro e evitar a alíquota daquele mês.** A opção pelo Simples vale pelo ano-calendário; a exclusão voluntária comunicada após o último dia útil de janeiro só produz efeitos em 1º de janeiro do ano seguinte [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md). O último dia útil de janeiro de **2026 foi 30/01/2026**, prazo pertinente à exclusão com efeitos desde 1º/01/2026 (`prazo_opcao` no JSON). Esse prazo já passou na data deste memorando, 24/10/2026. Uma comunicação em dezembro de 2026 teria efeitos em **1º/01/2027**, não em dezembro. O último dia útil de janeiro de 2027 será **29/01/2027** (contagem de calendário, sujeita à conferência de feriados aplicáveis).

Se a empresa decidir sair do Simples para 2027 depois de validar os itens abertos: (1) fechar a escrituração e a projeção de 2027, inclusive a separação das obras; (2) comunicar a exclusão voluntária nos canais fiscais competentes até o prazo aplicável e guardar o protocolo; (3) apurar ISS e contribuição previdenciária fora do DAS a partir da data efetiva; (4) escolher o regime de IRPJ para 2027. No Presumido, a opção se manifesta pelo pagamento da primeira quota do primeiro período de apuração e é definitiva para o ano [lei9249_9430_presumido.md](../library/lei9249_9430_presumido.md). **A biblioteca não fornece o procedimento nem o prazo de opção pelo Lucro Real**; esses detalhes precisam ser verificados antes de qualquer escolha desse regime. Dadas as estimativas, a orientação presente é manter o Simples e validar os itens abertos antes de eventual decisão para 2027.

### Dúvida posterior do sócio: pedido no portal e outra empresa

**Pedir a exclusão em dezembro de 2026 é possível como comunicação para o ano seguinte, mas não muda a tributação de dezembro de 2026.** A data de protocolo e a data de início dos efeitos são diferentes: pelo art. 16, §2º-A, reproduzido na biblioteca, a exclusão voluntária comunicada depois do último dia útil de janeiro só produz efeitos em 1º de janeiro do ano seguinte [lc123_sublimite_opcao.md](../library/lc123_sublimite_opcao.md). Assim, a fala do amigo pode estar correta quanto a *protocolar* em dezembro, mas não quanto a deixar o Simples ainda naquele mês. A operação concreta do portal não é detalhada na biblioteca; convém guardar o protocolo e conferir a data de efeitos nele.

**Abrir outro CNPJ não altera o regime da Vértice nem transfere, por si só, a receita dos serviços que ela já prestou.** O comparativo recebido trata da empresa e dos contratos atuais. Uma sociedade nova que efetivamente contrate e execute atividades próprias exigiria outra análise, com contratos, equipe, custos, sócios, faturamento e regime de apuração próprios; esses fatos não constam dos arquivos. Simplesmente emitir por ela as notas de serviços executados pela Vértice não é uma premissa de planejamento que possamos validar. A biblioteca não contém regras suficientes sobre empresas com sócios comuns, reorganização, atribuição de receitas ou opção inicial pelo Lucro Real; qualquer conclusão jurídica específica a respeito seria **não verificada**. Portanto, não há base para recomendar essa abertura como meio de tributar dezembro pelo Real ou para projetar uma economia fiscal. Antes de qualquer operação nova, a documentação da prestação efetiva e essas regras teriam de ser examinadas com fontes autorizadas.
