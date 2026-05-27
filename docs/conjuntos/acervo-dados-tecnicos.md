# Acervo de Dados Técnicos

| Campo | Valor |
|-------|-------|
| **Slug** | `acervo-dados-tecnicos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#1) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acervo-de-dados-tecnicos |
| **Unidade ANP (inventário)** | SDT |
| **Periodicidade** | Eventual |
| **Formato** | CSV |
| **Fonte operacional** | Geociências / Acervo técnico |
| **Pasta local** | `data/raw/acervo-dados-tecnicos/` |
| **Inventário ANP** | Acervo de Dados Técnicos |
| **Prioridade fuel-analytics** | Baixa (geociências) |

## Contexto

Catálogo do acervo técnico mantido pela ANP — dados de poços (perfis, testemunhos), levantamentos sísmicos, estudos geológicos e geoquímicos. Gerenciado pelo Banco de Dados de Exploração e Produção (BDEP).

## Relevância para anp-fuel-analytics

Relevância indireta. O acervo é insumo para decisões exploratórias que, no longo prazo, definem oferta de petróleo e gás. Sem uso direto em análises de abastecimento/preços.

## Estrutura dos arquivos

> **Status:** validado — 8 CSVs + 7 PDFs metadados.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- **CSVs disponíveis:**
  - `tabela-programas-geofisicos.csv` — programas sísmicos/geofísicos
  - `tabela-dados-geoquimicos.csv` — dados geoquímicos
  - `tabela-levantamentos-geoquimicos.csv` — levantamentos
  - `tabela-de-estudos.csv` — estudos técnicos
  - `pocos-publicos-2020.csv` a `pocos-publicos-2023.csv` — poços públicos por ano
- **Metadados:** 7 PDFs (um por tipo de tabela)

## Cruzamentos sugeridos

- [resultado-poco](resultado-poco.md) — poços cujos dados estão no acervo
- [fase-exploracao](fase-exploracao.md) — dados sísmicos associados a blocos ativos
- [amostras-rochas-fluidos](amostras-rochas-fluidos.md) — sub-acervo de amostras
- [aquisicao-processamento-estudo-dados](aquisicao-processamento-estudo-dados.md) — processamento de dados do acervo

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SDT (36 sub-bases)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Cobertura do acervo

- **Volume por tipo** — perfis de poço vs sísmica vs geoquímica; total de registros.
- **Cobertura por bacia** — bacias com mais dados disponíveis; vazios de informação.
- **Evolução temporal** — novos dados incorporados por ano; digitalização vs novos levantamentos.

### Acesso e utilização

- **Solicitações** — se disponível: número de acessos ao acervo por tipo de usuário.
- **Dados públicos vs confidenciais** — proporção; prazo de confidencialidade de dados de poço.

### Cruzamentos

- **Acervo × taxa de sucesso** — bacias com mais dados disponíveis têm melhor taxa de sucesso exploratório?
- **Acervo × rodadas** — disponibilidade de dados técnicos e atratividade de blocos.

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `pocos-publicos-2020.csv` | ~107 | CSV | utf-8-sig | `;` | 21 | POCO, CADASTRO, OPERADOR, POCO_OPERADOR, ESTADO, BACIA, BLOCO, SIG_CAMPO, CAMPO, TERRA_MAR, etc. |
| `pocos-publicos-2021.csv` | ~140 | CSV | utf-8-sig | `;` | 21 | Idem |
| `pocos-publicos-2022.csv` | ~180 | CSV | utf-8-sig | `;` | 21 | Idem |
| `pocos-publicos-2023.csv` | ~219 | CSV | utf-8-sig | `;` | 21 | Idem |
| `tabela-dados-geoquimicos.csv` | 4.667 | CSV | utf-8-sig | `;` | 38 | Dados geoquímicos |
| `tabela-de-estudos.csv` | 45 | CSV | utf-8-sig | `;` | 7 | Estudos técnicos |
| `tabela-levantamentos-geoquimicos.csv` | 70 | CSV | utf-8-sig | `;` | 8 | Levantamentos geoquímicos |
| `tabela-programas-geofisicos.csv` | 3.811 | CSV | utf-8-sig | `;` | 11 | Programas sísmicos/geofísicos |
| `metadados-*.pdf` (7 arquivos) | — | PDF | — | — | — | Dicionários de dados por tipo de tabela |

## Qualidade e chaves

- **Chave lógica:** `POCO` + `CADASTRO` (ambos 100% únicos nos poços públicos)
- **Granularidade:** 1 linha por poço tornado público no ano
- **Encoding:** utf-8-sig, sep `;`, 58 colunas (schema amplo com muitos campos técnicos)
- **Arquivos principais:**
  - `pocos-publicos-20XX.csv` (4 anos) — 107–218 linhas por ano, 58 cols
  - `tabela-dados-geoquimicos.csv` — 4.667 linhas, 38 cols
  - `tabela-programas-geofisicos.csv` — 3.811 linhas, 11 cols
  - `tabela-de-estudos.csv` — 45 linhas, 7 cols
  - `tabela-levantamentos-geoquimicos.csv` — 70 linhas, 8 cols
- **Nulls relevantes:** Muitas colunas técnicas 100% nulas (UNIDADE_ESTRATIGRAFICA, AGP, PERFIS_DIGITAIS) — campos opcionais do cadastro
- **Cobertura:** Poços de 10+ operadores, múltiplas bacias
