# Where the fixtures come from

All client data in the suite is synthetic. Realism comes from modeling each document on public
exemplars — real structure, language, length and clutter — with every party, amount, date and
case number invented. Famous or recent real cases are never used as the *facts* of a trap: models
may remember the outcome, and that would test memory rather than judgment. Each pack's reviewer
manifest records which exemplar a fixture was modeled on.

## United States (mostly public domain)

| Need | Source |
|---|---|
| Pleadings, motions, orders, dockets | CourtListener / RECAP Archive (Free Law Project); PACER for gaps |
| Opinions | CourtListener; Caselaw Access Project (case.law); Google Scholar; Justia |
| Executed contracts (MSA, APA, employment, LLC operating agreements, non-competes) | SEC EDGAR exhibits 10.x; LawInsider / onecle as indexes into EDGAR |
| Chapter 11 packs (first-day motions, DIP orders, critical-vendor motions, MORs, plans, bar-date notices) | Claims-agent dockets: Kroll, Epiq, Stretto, Verita; US Trustee MOR forms (justice.gov) |
| Restatements, revenue-recognition pressure, fraud patterns | SEC 8-K Item 4.02 non-reliance filings; SEC comment letters; SEC/PCAOB enforcement orders; AICPA sample engagement letters |
| Tax | IRS forms and instructions (verbatim); Tax Court opinions (ustaxcourt.gov); TaxCalcBench repository; state child-support worksheets; state court self-help form sets (CA Judicial Council, NY UCS) |
| Employment | EEOC appellate decisions; NLRB decisions; DOL opinion letters |
| Statutes / regulations | uscode.house.gov; eCFR; state legislature sites |

## Brasil

| Necessidade | Fonte |
|---|---|
| Peças completas | Consulta pública e-SAJ (TJSP); PJe (TRTs, TRFs); processos de RJ de grande porte (sites dos administradores judiciais: editais, relação de credores, relatórios mensais, planos) |
| Jurisprudência | Pesquisa dos tribunais (STF, STJ, TST, TJSP); DataJud/CNJ; JusBrasil e Escavador como índices |
| Tributário com fatos reais | Acórdãos do CARF; Soluções de Consulta COSIT (RFB); PGFN (execução fiscal, transação) |
| Societário e contratos | IN DREI (modelos de contrato social); Juntas Comerciais; CVM; ANPD (LGPD) |
| Textos legais e normas contábeis | planalto.gov.br; normas RFB; CPC (cpc.org.br); CFC/NBC |

## Rules

1. Model on real, re-factualize everything. Public records carry real names (and LGPD applies
   in Brazil); strip them.
2. Statute and regulation excerpts in the libraries are meant to be verbatim; each library file in
   a pack is flagged `verbatim: true/false` in the manifest, and non-verbatim excerpts are a
   verification item for the professional review before the pack is frozen.
3. Planted distractors (superseded authorities, the fictitious "memo bank") are listed in the
   manifest and never mixed into the real-law index without that marker.
