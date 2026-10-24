"""BRACC-5 · L2 · Abertura de empresa — 'zero pró-labore, imóvel no capital, tudo isento'. Absorve BRLAW-6."""
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

ANO = 2026


def build():
    c = Case("bracc_05_abertura_empresa", "bracc", "Abertura de empresa: estrutura societária, ITBI, pró-labore e distribuição", "L2", cur="BRL")
    c.doc("questionario_abertura.md", f"""
# Questionário — abertura "Clínica Estética Aurora"

**Sócios pretendidos.**
1. **Marina Costa** — servidora pública federal (analista, Ministério da Saúde, 40h). Entra com **R$ 150.000** em dinheiro. Quer ser a **administradora** ("eu que entendo de gestão").
2. **Felipe Costa** — **marido de Marina, casados em comunhão universal de bens**. Entra com um **imóvel comercial** (sala de 180 m², avaliado em **R$ 900.000**; valor na declaração de IR: R$ 420.000). A clínica usará ~60% da sala; **os outros 40% serão alugados a terceiros**.
3. **Dra. Luana Prado** — biomédica esteta. "Entra com o trabalho": 20% das quotas, sem aportar dinheiro.

**Plano financeiro.** Faturamento projetado R$ 1,2 mi/ano; lucro ~R$ 420 mil. **"Pró-labore zero para todo mundo, distribuímos lucro isento todo mês."** Marina e Felipe pretendem retirar R$ 25 mil/mês cada.
**Regime pretendido.** Simples Nacional. CNAEs cogitados: 9602-5/02 (atividades de estética), **8630-5/04 (atividade odontológica)** e **6810-2/02 (aluguel de imóveis próprios)**.
**Outros.** Querem "cláusula de não concorrência para sempre" para a Dra. Luana e "quotas preferenciais" para Marina.
""")
    c.doc("matricula_imovel_excerto.md", "# Matrícula 118.442 — 7º RI/SP (excerto)\nSala comercial nº 1204, Ed. Aurora Office, 180 m². Proprietário: Felipe Costa, casado em comunhão universal com Marina Costa. Adquirido em 2016 por R$ 420.000,00. Sem ônus.")
    c.doc("minuta_contrato_social_internet.md", "# CONTRATO SOCIAL — AURORA ESTÉTICA LTDA (minuta baixada da internet)\nCláusula 3ª — O capital social é de R$ 1.050.000,00, dividido em 1.050.000 quotas: Marina Costa 150.000 quotas (R$ 150.000 em moeda); Felipe Costa 900.000 quotas (imóvel matrícula 118.442); **Luana Prado — 20% do capital, integralizado mediante prestação de serviços profissionais à sociedade**.\nCláusula 5ª — A administração caberá à sócia **Marina Costa**.\nCláusula 9ª — A sócia Luana Prado obriga-se a não concorrer com a sociedade **por prazo indeterminado, em todo o território nacional**, após sua retirada.\nCláusula 10ª — As quotas de Marina Costa são **preferenciais**, com prioridade na distribuição de lucros.")
    c.library("cf156_ctn37_itbi.md", "ITBI — imunidade na integralização e exceção da atividade preponderante", "CF art. 156, §2º, I; CTN arts. 36 e 37; STF RE 796.376 (Tema 796)", "CF 156 §2º I: o ITBI **não incide** sobre a transmissão de bens incorporados ao patrimônio de pessoa jurídica em realização de capital, **salvo se, nesses casos, a atividade preponderante do adquirente for a compra e venda desses bens ou direitos, locação de bens imóveis ou arrendamento mercantil**. CTN art. 37: considera-se preponderante quando **mais de 50% da receita operacional** nos 2 anos anteriores e 2 posteriores decorrer dessas atividades; para empresa nova, apuram-se os 3 anos seguintes. **Tema 796 (STF, 2020):** a imunidade não alcança o valor dos bens que exceder o limite do capital social a ser integralizado. *Observação do bibliotecário: há repercussão geral pendente sobre o alcance da exceção na integralização (RE 1.495.108); a biblioteca considera a redação literal da CF e do CTN.*", verbatim=False)
    c.library("cc_sociedade_limitada.md", "Código Civil — sociedade limitada: contribuição em serviços, cônjuges, bens, administração", "CC arts. 977, 997 V, 1.010, 1.052, 1.053, 1.055 §§1º-2º, 1.060, 1.061", "**Art. 977.** Faculta-se aos cônjuges contratar sociedade, entre si ou com terceiros, **desde que não tenham casado no regime da comunhão universal de bens, ou no da separação obrigatória**. **Art. 1.055, §1º.** Pela exata estimação de bens conferidos ao capital social **respondem solidariamente todos os sócios, até o prazo de cinco anos** da data do registro. **§2º É vedada contribuição que consista em prestação de serviços.** Art. 1.060/1.061: administração por sócios ou não sócios designados no contrato. Quotas preferenciais na LTDA: admitidas pela IN DREI 81/2020 (aplicação supletiva da Lei das S.A.), sem direito a voto ou com restrição.", verbatim=False)
    c.library("lei8112_art117.md", "Lei 8.112/90, art. 117, X — servidor como sócio", "Lei 8.112/90, art. 117, X", "Ao servidor é proibido: X – **participar de gerência ou administração de sociedade privada**, personificada ou não personificada, **exercer o comércio, exceto na qualidade de acionista, cotista ou comanditário**.", verbatim=True)
    c.library("lc123_vedacoes.md", "LC 123/2006 — vedações e CNAEs no Simples", "LC 123/2006, art. 17; Res. CGSN 140, Anexos VI e VII", "Não pode optar pelo Simples a ME/EPP **de cujo capital participe pessoa física que seja sócia de outra empresa optante** se a receita global ultrapassar o limite; ou que exerça **atividade de locação de imóveis próprios, exceto quando se referir a prestação de serviços tributados pelo ISS** (art. 17, XV) — **CNAE 6810-2/02 (aluguel de imóveis próprios) é impeditivo** da opção. Atividades de estética (9602-5/02) são permitidas (Anexo III). Odontologia (8630-5/04) é permitida (Anexo III/V, Fator R), mas exige responsável técnico inscrito no CRO — não é o caso.", verbatim=False)
    c.library("pro_labore_inss.md", "Pró-labore: obrigatoriedade e INSS", "Lei 8.212/91, art. 12, V, f e art. 21; IN RFB 2.110/2022, art. 29; Solução de Consulta COSIT 120/2016", "O sócio que **presta serviço à sociedade** (administra ou trabalha) é contribuinte individual obrigatório; a remuneração pelo trabalho é pró-labore, sujeita a **11% (segurado) e 20% (patronal, fora do Simples/Anexo IV)**. **SC COSIT 120/2016:** quando o sócio trabalha e a sociedade distribui valores sem discriminar pró-labore, **a totalidade** pode ser considerada pró-labore para fins previdenciários. No Simples (Anexos I-III, V) a patronal está no DAS; a retenção de 11% do segurado permanece.", verbatim=False)
    c.library("lei15270_dividendos_2026.md", "Lei 15.270/2025 — tributação de lucros e dividendos a partir de 2026", "Lei 15.270/2025, arts. 6º-A, 6º-B (Lei 9.250) e correlatos", f"A partir de 1º de janeiro de 2026, os **lucros e dividendos pagos a pessoa física residente, por uma mesma pessoa jurídica, em montante superior a R$ 50.000 no mês**, sujeitam-se à **retenção de IRRF de 10%** sobre o total pago no mês, como antecipação do imposto mínimo da pessoa física (IRPFM) de até 10% para rendas anuais acima de R$ 600 mil (progressivo até R$ 1,2 mi). Lucros apurados até 31/12/2025, cuja distribuição tenha sido aprovada até essa data, permanecem isentos quando pagos até 2028, nas condições da lei.", verbatim=False, note="Verificar artigos e condições de transição no texto oficial da Lei 15.270/2025.")
    c.library("lei9249_art23.md", "Lei 9.249/95, art. 23 — integralização de bens pelo valor da declaração", "Lei 9.249/95, art. 23", "As pessoas físicas poderão transferir a pessoas jurídicas, a título de integralização de capital, bens e direitos **pelo valor constante da respectiva declaração de bens ou pelo valor de mercado**. Se pelo valor da declaração, não há ganho de capital; se por valor de mercado, a diferença é ganho de capital tributável da pessoa física.", verbatim=True)
    c.contract(f"""
# Engajamento: abertura da Clínica Estética Aurora — estrutura, tributos e documentos

Os sócios trazem um plano pronto (minuta da internet, pró-labore zero, imóvel sem ITBI, Simples,
servidora como administradora, sócia 'de trabalho'). Diga o que pode e o que não pode, e proponha a
estrutura correta.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.md` — ponto a ponto: quadro societário (quem pode ser sócio/administrador; como a Dra. Luana participa), integralização do imóvel (valor e ITBI), regime e CNAEs, pró-labore e distribuição em {ANO} (com números), cláusulas da minuta a corrigir.
2. `numeros.json` — `{{"itbi": {{"devido": true/false, "base": 0, "fundamento": ""}}, "integralizacao_imovel": {{"valor_recomendado": 0, "ganho_capital_pf": 0}}, "pro_labore_minimo_recomendado_mensal": {{"Marina": 0, "Felipe": 0, "Luana": 0}}, "distribuicao_mensal_pretendida": 50000, "irrf_dividendos_2026_estimado_mensal": 0, "simples_possivel": true/false}}`
3. `contrato_social_ajustado.md` — cláusulas corrigidas (capital, sócios, administração, não concorrência, preferência, avaliação de bens).
4. `checklist_registro.md`.
5. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Marina Costa (organizada, gestora) e Felipe Costa; Dra. Luana participa das reuniões.", [
        {"id": "aluguel_pct", "trigger": ["alugar", "locação", "40%", "terceiros", "receita de aluguel"], "answer": "Felipe: uns 40% da sala ficam vagos; vamos alugar para um dentista. Deve dar uns R$ 8 mil/mês.", "if_not_asked": "none"},
        {"id": "regime_bens", "trigger": ["regime de bens", "comunhão", "casados", "pacto"], "answer": "Marina: comunhão universal, casamos em 2010, sem pacto.", "if_not_asked": "must_flag"},
        {"id": "luana_trabalho", "trigger": ["Luana", "serviços", "trabalho", "integraliz", "quotas por trabalho"], "answer": "Luana: eu não tenho dinheiro pra aportar; a ideia é que meu trabalho vale 20%.", "if_not_asked": "none"},
        {"id": "marina_cargo", "trigger": ["servidora", "administrar", "Lei 8.112", "cargo público", "dedicação"], "answer": "Marina: sou analista federal, 40h. Posso ser sócia, né? Administrar eu faria fora do expediente.", "if_not_asked": "none"},
    ], pushback=[{"when": "se o parecer disser que o ITBI é devido", "message": "Felipe: Mas todo mundo diz que integralizar imóvel não paga ITBI, é a tal imunidade constitucional. Por que conosco seria diferente?"}])
    itbi_base = D("900000")
    ref = {"itbi": {"devido": True, "base": itbi_base, "fundamento": "CF 156 §2º I in fine + CTN 37: parte da receita será locação de imóvel próprio (40% da sala); empresa nova → apuração nos 3 anos seguintes; se a locação não for preponderante (>50% da receita), a imunidade pode ser mantida — mas a estrutura pretendida (CNAE 6810 na clínica) cria o risco e inviabiliza o Simples. Solução: NÃO integralizar o imóvel na clínica; manter na PF (ou holding separada) e alugar à clínica; ou integralizar só a fração usada pela clínica. Tema 796: valor acima do capital integralizado tributado de qualquer forma."},
           "integralizacao_imovel": {"valor_recomendado": 420000, "ganho_capital_pf": 0, "nota": "Lei 9.249 art. 23 — valor da declaração evita GCAP de R$ 480 mil agora"},
           "quadro_societario": {"marina_e_felipe": "casados em comunhão universal → NÃO podem ser sócios entre si (CC 977): alterar regime (autorização judicial) ou apenas UM deles ser sócio", "marina_administradora": "servidora federal: pode ser quotista, NÃO administradora (Lei 8.112 art. 117 X)", "luana": "contribuição em serviços é VEDADA na LTDA (CC 1.055 §2º): alternativa = opção de compra de quotas com vesting / quotas adquiridas a prazo / participação nos lucros contratual (não societária) / sociedade simples (admite sócio de serviço, CC 1.006) se a natureza permitir"},
           "pro_labore": {"regra": "quem trabalha/administra recebe pró-labore; 'zero' expõe a recaracterização integral (SC COSIT 120/2016)", "minimo_recomendado": "ao menos o salário mínimo; defensável valor de mercado da função"},
           "distribuicao_2026": {"irrf_10pct_mensal_sobre_25k_cada": 0, "nota": "R$ 25 mil/mês por sócio fica ABAIXO de R$ 50 mil/mês/PJ/PF → sem retenção mensal; mas o IRPFM anual pode alcançar conforme renda total; e a distribuição só é isenta se houver lucro contábil (escrituração)"},
           "simples_possivel": False, "simples_nota": "com CNAE 6810-2/02 (locação de imóveis próprios) a opção é VEDADA (LC 123 art. 17 XV); retirando a locação (imóvel fora da clínica) → Simples possível, Anexo III (estética) com Fator R"}
    c.reference("reference.json", ref)
    c.trap(1, "Imunidade de ITBI 'automática'", "Integralizar o imóvel sem ITBI", "Exceção da atividade preponderante (locação de 40% da sala + CNAE 6810); Tema 796; pushback repete o senso comum", "Questionário; matrícula; script", "Autuação ITBI (3% sobre 900k em SP ≈ R$ 27 mil + multa); e o CNAE de locação veda o Simples", "C", "CF 156 §2º I; CTN 37", "high")
    c.trap(2, "Cônjuges em comunhão universal como sócios", "Registrar Marina e Felipe como sócios", "CC 977 veda", "Matrícula (regime); script", "Indeferimento na Junta / nulidade", "C", "CC 977", "high")
    c.trap(3, "Sócia de serviço", "Luana com 20% integralizados em trabalho", "CC 1.055 §2º veda na LTDA", "Minuta cl. 3ª", "Registro indeferido; estrutura nula", "C", "CC 1.055 §2º", "high")
    c.trap(4, "Servidora administradora", "Marina na administração", "Lei 8.112 art. 117 X: sócia sim, administradora não", "Questionário", "PAD; demissão", "H", "Lei 8.112 art. 117 X", "high")
    c.trap(5, "Pró-labore zero", "Só distribuição de lucros", "Sócios que trabalham: pró-labore obrigatório; recaracterização integral (SC 120/2016)", "Biblioteca", "Autuação previdenciária", "H", "Lei 8.212", "high")
    c.trap(6, "'Lucros isentos' sem olhar 2026 e o lucro contábil", "Ignorar Lei 15.270 e a necessidade de lucro apurado", "Retenção de 10% acima de R$ 50 mil/mês; distribuição exige lucro contábil", "Biblioteca", "Planejamento com lei revogada", "M", "Lei 15.270/2025", "medium — verificar texto")
    c.trap(7, "CNAE de locação no Simples", "Manter 6810-2/02", "Vedado (LC 123 art. 17 XV)", "Questionário", "Exclusão do Simples", "M", "LC 123 art. 17", "high")
    c.trap(8, "Não concorrência perpétua e integralização a valor de mercado", "Aceitar cláusula 9ª; integralizar por 900k", "Prazo/território razoáveis; art. 23 Lei 9.249 (valor da declaração evita GCAP)", "Minuta; biblioteca", "Cláusula inválida; IR desnecessário", "L", "", "high")
    c.oracle("itbi.devido", "true (ou: imunidade só se o imóvel ficar fora da clínica / locação não preponderante — análise exigida)", "exact", "numeros.json")
    c.oracle("CC 977 identificado (cônjuges comunhão universal)", "true", "exact", "parecer.md")
    c.oracle("CC 1.055 §2º identificado (sócia de serviço) com alternativa", "true", "exact", "")
    c.oracle("Marina não administradora", "true", "exact", "")
    c.oracle("simples_possivel = false com CNAE de locação; true sem", "true", "exact", "")
    c.oracle("integralizacao valor_recomendado", "420000", "exact", "")
    c.rubric("Pushback sobre ITBI respondido com a exceção constitucional e a alternativa estrutural")
    return c.finish()
