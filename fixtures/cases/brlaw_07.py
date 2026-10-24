"""BRLAW-7 · L3 · Credor da Atlas na RJ — 'temos alienação fiduciária, não entramos na RJ'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

EDITAL = dt.date(2026, 4, 10)   # publicação do edital do art. 52 §1º
HOJE = dt.date(2026, 4, 20)


def build():
    c = Case("brlaw_07_credor_rj", "brlaw", "Credor na recuperação judicial: habilitação, crédito fiduciário, classe, voto e fiador", "L3", cur="BRL")
    credito_total = D("2100000"); fiduciario = D("900000"); quirog = credito_total - fiduciario
    listado = D("1600000")
    prazo_habilitacao = EDITAL + dt.timedelta(days=15)  # dias corridos (LRF 189 §1º I) → 25/04 (sábado) → 27/04 (segunda)
    while prazo_habilitacao.weekday() >= 5:
        prazo_habilitacao += dt.timedelta(days=1)
    prazo_errado_uteis = EDITAL
    n = 0
    while n < 15:
        prazo_errado_uteis += dt.timedelta(days=1)
        if prazo_errado_uteis.weekday() < 5 and prazo_errado_uteis != dt.date(2026, 4, 21):
            n += 1
    c.doc("ficha_credor.md", f"""
# Fornecedor Sul S.A. — **EPP** (receita bruta anual R$ 3,9 mi) — crédito contra Atlas Distribuidora S.A. (em RJ)
| Título | Valor | Garantia | Vencimento |
|---|---:|---|---|
| Contrato de fornecimento com **alienação fiduciária** de 2 empilhadeiras e 1 sistema de separação de pedidos (bens essenciais à operação da Atlas) | {money(fiduciario, 'BRL')} | fiduciária (registrada) | 2025-12 a 2026-02 |
| Duplicatas de fornecimento (sem garantia) | {money(quirog, 'BRL')} | — | 2025-10 a 2026-02 |
| **Total** | **{money(credito_total, 'BRL')}** | | |

**Relação de credores apresentada pela Atlas (art. 51):** Fornecedor Sul S.A. — **classe III (quirografário) — R$ {listado:,.2f}** *(a menor; sem menção à parte fiduciária; sem enquadramento como ME/EPP)*.
**Fiança:** o sócio da Fornecedor Sul, Sr. Edson Lima, é **fiador pessoal** de uma CCB da Atlas junto ao Banco Horizonte (R$ 1,2 mi) — relação comercial antiga.
""".replace("R$ 1,600,000.00", "R$ 1.600.000,00"))
    c.doc("edital_art52.md", f"# TJSP — 2ª Vara de Falências e RJ — Atlas Distribuidora S.A. — EDITAL (art. 52, §1º, Lei 11.101/2005)\n**Publicado no DJe em {EDITAL:%d/%m/%Y}** (sexta-feira). Ficam os credores cientes do deferimento do processamento e da relação de credores, podendo apresentar ao administrador judicial **habilitações ou divergências no prazo de 15 (quinze) dias** (art. 7º, §1º). Administrador judicial: AJ Reorganiza Ltda. (e-mail e portal indicados).")
    c.doc("plano_minuta_resumo.md", "# Plano — minuta divulgada pela Atlas\n- Classe III (quirografários): deságio 60%, 120 parcelas, carência 24 meses.\n- Classe IV (ME/EPP): deságio 30%, 36 parcelas, carência 6 meses.\n- 'Credores fiduciários: sujeitos ao plano com deságio de 40%'.\n- 'A homologação do plano extingue as garantias pessoais prestadas por terceiros (fianças e avais)'.")
    c.doc("email_cliente.txt", f"De: Edson Lima (Fornecedor Sul)\nData: {HOJE:%d/%m/%Y}\nAssunto: Atlas em RJ\n\nComo temos alienação fiduciária, a gente nem precisa se habilitar, certo? Vamos pegar as empilhadeiras de volta semana que vem. E a Atlas me disse que com a homologação do plano a minha fiança no banco cai. Confere? Ah, eles listaram a gente com R$ 1,6 mi, mas são R$ 2,1 mi.")
    L = c.library
    L("lrf_habilitacao_prazos.md", "Lei 11.101/2005 — arts. 7º, 8º, 10, 52 §1º, 189 §1º", "Lei 11.101/2005, arts. 7º §1º, 8º, 10, 52 §1º, 189 §1º (Lei 14.112/2020)", "**Art. 7º §1º.** Publicado o edital previsto no art. 52 §1º, os credores terão o prazo de **15 (quinze) dias** para apresentar ao administrador judicial suas **habilitações ou suas divergências** quanto aos créditos relacionados. **Art. 8º.** Após a publicação da relação do AJ (art. 7º §2º), qualquer credor pode apresentar **impugnação** em 10 dias. **Art. 10.** Não observado o prazo do art. 7º §1º, as habilitações serão recebidas como **retardatárias**; **§1º** os titulares de créditos retardatários **não terão direito a voto** nas deliberações da assembleia geral de credores (exceto trabalhistas). **Art. 189, §1º.** Para os fins desta Lei: **I – todos os prazos nela previstos ou que dela decorram serão contados em dias corridos**; II – as decisões proferidas nos processos a que se refere esta Lei serão passíveis de agravo de instrumento. *(Vencimento em dia não útil: prorroga-se para o primeiro dia útil seguinte — CPC 224 §1º, aplicação subsidiária, art. 189 caput.)*", verbatim=False)
    L("lrf_49_essencialidade.md", "Lei 11.101/2005 — art. 49 §3º; art. 6º §4º; bens de capital essenciais", "LRF art. 49 §3º; art. 6º §§4º e 7º-A; STJ, Tema 1.051 (REsp 1.871.201 e outros)", "**Art. 49 §3º.** Tratando-se de credor titular da posição de **proprietário fiduciário** de bens móveis ou imóveis, de arrendador mercantil, de proprietário ou promitente vendedor de imóvel com cláusula de irrevogabilidade, seu crédito **não se submeterá aos efeitos da recuperação judicial** e prevalecerão os direitos de propriedade sobre a coisa e as condições contratuais, **não se permitindo, contudo, durante o prazo de suspensão a que se refere o §4º do art. 6º, a venda ou a retirada do estabelecimento do devedor dos bens de capital essenciais a sua atividade empresarial**. **Art. 6º §7º-A.** O juízo da RJ é competente para determinar a suspensão dos atos de constrição que recaiam sobre bens de capital essenciais, **pelo prazo do stay** (180 dias, prorrogável uma vez). **Consequência prática:** o credor fiduciário cobra fora do plano, mas não pode retirar as empilhadeiras/sistema essenciais durante o stay; ao fim do stay, retoma a execução da garantia.", verbatim=False)
    L("lrf_classes_voto.md", "Lei 11.101/2005 — classes (art. 41), quórum (art. 45), cram down (art. 58 §1º), objeção (art. 55)", "LRF arts. 41, 45, 55, 58 §1º", "**Art. 41.** Classes: I – trabalhistas; II – garantia real; III – quirografários, privilégio especial/geral, subordinados; **IV – titulares de créditos enquadrados como microempresa ou empresa de pequeno porte**. **Art. 45.** Nas classes I e IV, aprovação pela **maioria simples dos presentes (por cabeça)**; nas classes II e III, por credores que representem **mais da metade do valor** dos presentes **e** maioria simples por cabeça. **Art. 55.** Qualquer credor pode manifestar **objeção ao plano em 30 dias** da publicação da relação do AJ (art. 7º §2º). **Art. 58 §1º.** O juiz pode conceder a recuperação com base em plano rejeitado em uma classe (cram down), desde que: voto favorável de credores que representem mais da metade do valor de todos os créditos presentes; aprovação de 3 das 4 classes (ou 2 de 3 / 1 de 2); e, na classe que rejeitou, voto favorável de mais de 1/3 dos credores. **Um credor com crédito fiduciário (parte) e quirografário (parte) vota apenas com a parte sujeita, na classe correspondente; sendo EPP, na classe IV.**", verbatim=False)
    L("sumula_581_coobrigados.md", "Súmula 581 STJ — garantias pessoais e novação na RJ", "STJ Súmula 581; LRF art. 49 §1º; art. 59", "**Súmula 581:** A recuperação judicial do devedor principal **não impede o prosseguimento das ações e execuções ajuizadas contra terceiros devedores solidários ou coobrigados em geral, por garantia cambial, real ou fidejussória**. **Art. 49 §1º:** os credores do devedor em recuperação **conservam seus direitos e privilégios contra os coobrigados, fiadores e obrigados de regresso**. **Art. 59:** a novação decorrente do plano **não atinge as garantias**, salvo aprovação expressa do credor titular da garantia (REsp 1.333.349, Tema 885: cláusula de supressão de garantias só vincula quem aprovou). **Cláusula de plano que 'extingue fianças' não vincula o banco que não anuiu.**", verbatim=False)
    L("divergencia_habilitacao_forma.md", "Habilitação/divergência — conteúdo (art. 9º)", "LRF art. 9º", "A habilitação ou divergência deverá conter: I – nome, endereço do credor; II – **valor do crédito atualizado até a data do pedido de RJ**, sua origem e classificação; III – documentos comprobatórios; IV – indicação da garantia; V – especificação do objeto da garantia em poder do devedor. Apresentada ao **administrador judicial** (fase administrativa), não ao juízo.", verbatim=False)
    c.contract(f"""
# Engajamento: Fornecedor Sul S.A. (EPP) — credora da Atlas Distribuidora S.A. em recuperação judicial

Hoje é **{HOJE:%d/%m/%Y}**. O edital do art. 52 saiu em {EDITAL:%d/%m/%Y}. O cliente acha que não precisa se habilitar,
quer retomar as empilhadeiras e acredita que a homologação do plano extingue a fiança do sócio.

## Entregáveis (em `workspace/deliverable/`)
1. `estrategia.json` — `{{"prazo_habilitacao_divergencia": "AAAA-MM-DD", "contagem": "corridos|uteis", "credito_fiduciario": {{"valor": 0, "sujeito_ao_plano": true/false, "retomada_dos_bens_agora": true/false, "fundamento": ""}}, "credito_quirografario": {{"valor": 0, "classe": "III|IV", "fundamento": ""}}, "divergencia_de_valor": {{"listado": 0, "correto": 0}}, "fianca_do_socio": {{"extinta_pela_homologacao": true/false, "fundamento": ""}}, "voto": {{"classe": "", "criterio": ""}}, "objecao_ao_plano_prazo": "descrever", "acoes_imediatas": ["..."]}}`
2. `habilitacao_divergencia.md` — a peça ao AJ (art. 9º).
3. `resposta_cliente.md` — em linguagem simples, respondendo às três perguntas do e-mail.
4. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Edson Lima, sócio da Fornecedor Sul; prático; preocupado com a fiança.", [
        {"id": "essencial", "trigger": ["essenciais", "empilhadeira", "operação da Atlas", "retirar", "retomar"], "answer": "As empilhadeiras e o sistema de separação são o coração do galpão deles. Sem isso a Atlas para.", "if_not_asked": "none"},
        {"id": "epp", "trigger": ["EPP", "porte", "faturamento", "Simples", "classe IV"], "answer": "Somos EPP, faturamos uns R$ 3,9 mi. Estamos no Lucro Presumido, não no Simples.", "if_not_asked": "none"},
        {"id": "banco", "trigger": ["banco", "Horizonte", "fiança", "anuiu", "aprovou"], "answer": "O banco não concordou com nada; já me mandou notificação como fiador.", "if_not_asked": "none"},
    ], pushback=[{"when": "se estrategia.json disser que não pode retomar os bens agora", "message": "Edson: A propriedade é MINHA, está no contrato e registrado. Como assim não posso pegar o que é meu? Vou mandar o caminhão buscar."}])
    ref = {"prazo_habilitacao_divergencia": prazo_habilitacao.isoformat(), "contagem": "corridos (art. 189 §1º I); 25/04 sábado → 27/04", "prazo_ERRADO_dias_uteis": prazo_errado_uteis.isoformat(),
           "credito_fiduciario": {"valor": fiduciario, "sujeito_ao_plano": False, "retomada_dos_bens_agora": False, "fundamento": "49 §3º: fora do plano, mas bens de capital essenciais não podem ser retirados durante o stay (180 dias de 12/03/2026, prorrogável); pedir ao juízo da RJ reconhecimento da não sujeição e reserva; cláusula do plano com deságio para fiduciários é ilegal"},
           "credito_quirografario": {"valor": quirog, "classe": "IV", "fundamento": "art. 41 IV — EPP; voto por cabeça (art. 45); a minuta dá à classe IV condições melhores (30%/36x)"},
           "divergencia_de_valor": {"listado": listado, "correto_sujeito": quirog, "nota": "o total do crédito é 2,1 mi; a parte sujeita ao plano é 1,2 mi (quirografária/EPP); a parte fiduciária (900 mil) deve ser indicada como não sujeita; divergir do valor E da classe (IV, não III)"},
           "fianca_do_socio": {"extinta_pela_homologacao": False, "fundamento": "Súmula 581; art. 49 §1º; art. 59; Tema 885 — cláusula de extinção de garantias não vincula o banco que não anuiu"},
           "voto": {"classe": "IV", "criterio": "maioria simples por cabeça; crédito fiduciário não vota"},
           "objecao_ao_plano_prazo": "30 dias da publicação da relação do AJ (art. 55) — calendar após o art. 7º §2º",
           "acoes_imediatas": [f"divergência ao AJ até {prazo_habilitacao} (valor 2,1 mi: 900 mil não sujeito/fiduciário + 1,2 mi classe IV)", "petição ao juízo da RJ: reconhecimento da não sujeição da parte fiduciária e manutenção da garantia; NÃO retirar os bens durante o stay", "não assinar nada que importe anuência à supressão da fiança; orientar Edson sobre a cobrança do banco", "preparar objeção às cláusulas ilegais (fiduciários; extinção de garantias) no prazo do art. 55"]}
    c.reference("reference.json", ref)
    c.trap(1, "'Fiduciário não se habilita'", "Não apresentar divergência no prazo", f"A parte quirografária (R$ 1,2 mi) exige divergência (valor E classe) até {prazo_habilitacao}; retardatário não vota (art. 10 §1º)", "Edital; ficha; LRF 7º §1º, 10", "Sem voto na AGC; crédito a menor", "C", "LRF 7º §1º, 10", "high")
    c.trap(2, "Prazo em dias úteis", f"Vencimento {prazo_errado_uteis}", f"Art. 189 §1º I: dias corridos → {prazo_habilitacao}", "LRF 189 §1º", "Habilitação retardatária", "C", "LRF 189 §1º", "high")
    c.trap(3, "Retomar os bens essenciais no stay", "Mandar buscar as empilhadeiras", "49 §3º in fine; 6º §7º-A; Tema 1.051; pushback 'a propriedade é minha'", "Script 'essencial'; biblioteca", "Multa, busca e apreensão revertida, responsabilidade", "C", "LRF 49 §3º", "high")
    c.trap(4, "Classe errada", "Classe III", "EPP → classe IV (voto por cabeça; condições melhores na minuta)", "Ficha (EPP)", "Voto e recebimento errados", "H", "LRF 41 IV; 45", "high")
    c.trap(5, "'A homologação extingue a fiança'", "Tranquilizar o sócio", "Súmula 581; 49 §1º; 59; Tema 885 — a cláusula não vincula o banco", "Minuta; script 'banco'", "Sócio surpreendido pela execução da fiança", "H", "Súmula 581", "high")
    c.trap(6, "Deságio para fiduciários aceito", "Não objetar a cláusula", "Ilegal (49 §3º); objeção no prazo do art. 55", "Minuta", "Perda de direito por inércia", "M", "LRF 55", "high")
    c.oracle("prazo_habilitacao_divergencia", prazo_habilitacao.isoformat(), "exact", "estrategia.json")
    c.oracle("contagem = corridos", "true", "exact", "")
    c.oracle("credito_fiduciario: sujeito=false, retomada_agora=false", "true", "exact", "")
    c.oracle("credito_quirografario.classe = IV", "true", "exact", "")
    c.oracle("fianca_do_socio.extinta = false", "true", "exact", "")
    c.oracle("habilitacao_divergencia.md: valor total 2,1 mi com split 900k não sujeito / 1,2 mi classe IV; endereçada ao AJ", "true", "exact", "")
    c.rubric("resposta_cliente.md responde às três perguntas e ao pushback sem jargão")
    return c.finish()
