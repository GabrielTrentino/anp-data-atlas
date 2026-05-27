# Incidentes de Exploração e Produção de Petróleo e Gás Natural

| Campo | Valor |
|-------|-------|
| **Slug** | `incidentes-ep` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#20) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/incidentes-seguranca-operacional |
| **Unidade ANP (inventário)** | SSO |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P / Segurança Operacional |
| **Pasta local** | `data/raw/incidentes-ep/` |
| **Inventário ANP** | Incidentes de Exploração e Produção |
| **Prioridade fuel-analytics** | Baixa (segurança operacional) |

## Contexto

Registro de incidentes operacionais em atividades de E&P — vazamentos, blowouts, falhas de equipamento, acidentes com pessoas. Classificação por tipo, severidade, instalação e consequências.

## Relevância para anp-fuel-analytics

Impacto indireto em abastecimento quando incidentes causam parada prolongada de plataformas ou campos produtores. Análise de risco operacional.

## Estrutura dos arquivos

> **Status:** validado — 5 CSVs complementares + 2 PDFs.

- **Formato:** CSV (encoding UTF-8)
- **Arquivos de dados:**
  - `incidentes.csv` (16,5 MB) — registro principal de incidentes
  - `incidentes-classificacao.csv` (1,9 MB) — classificação dos incidentes
  - `incidentes-tipo.csv` (2,7 MB) — tipologia
  - `incidentes-substancias.csv` (572 KB) — substâncias envolvidas
  - `incidentes-feridos.csv` (419 KB) — registro de feridos
- **Metadados:** `metadados-incidentes.pdf`, manual de comunicação

## Cruzamentos sugeridos

- [dados-ep](dados-ep.md) — instalações e campos afetados
- [producao-por-poco](producao-por-poco.md) — impacto em produção após incidente
- [fase-desenvolvimento-producao](fase-desenvolvimento-producao.md) — instalações em operação

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SSO
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Panorama de incidentes

- **Evolução temporal** — total de incidentes por ano; tendência (melhora ou piora).
- **Tipo de incidente** — distribuição: vazamento, falha, acidente pessoal, etc.
- **Severidade** — classificação por gravidade; incidentes graves vs menores.

### Geografia e infraestrutura

- **Por bacia/campo** — concentração de incidentes; campos com histórico pior.
- **Tipo de instalação** — FPSO vs plataforma fixa vs terrestre; risco relativo.
- **Operador** — taxa de incidentes normalizada por produção ou instalações.

### Impacto

- **Volume vazado** — série temporal de volumes totais derramados (se disponível).
- **Paradas de produção** — incidentes que causaram interrupção; duração estimada.
- **Penalidades** — cruzamento com multas aplicadas (se rastreável).

### Cruzamentos

- **Incidentes × produção** — queda de produção pós-incidente em campos afetados.
- **Incidentes × multas** — correlação temporal e geográfica.
- **Incidentes × idade da instalação** — instalações mais antigas têm mais incidentes?

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `incidentes.csv` | 30.745 | CSV | latin-1 | `;` | 13 | Registro principal: Numero, Empresa, CNPJ, Data_de_criacao, Autoridades_comunicadas, Instalacao, Data_primeira_observacao, Hora, UF, Municipio, Ambiente, Classificacao_origem, Observacao |
| `incidentes-classificacao.csv` | 45.241 | CSV | latin-1 | `;` | 2 | Numero, Classificacao_do_incidente |
| `incidentes-feridos.csv` | 30.822 | CSV | latin-1 | `;` | 2 | Numero, [dados de feridos] |
| `incidentes-substancias.csv` | 31.535 | CSV | latin-1 | `;` | 3 | Numero, Substancias, Volume |
| `incidentes-tipo.csv` | 35.598 | CSV | latin-1 | `;` | 4 | Numero, Tipo_de_incidente, DSC_GRAVIDADE_TIPO, DSC_QUASE_ACIDENTE_ACIDENTE |
| `metadados-incidentes.pdf` | — | PDF | — | — | — | Dicionário de dados |
| `manual-comunicacao-incidentes.pdf` | — | PDF | — | — | — | Manual de comunicação |

## Qualidade e chaves

- **Chave lógica:** `Numero` (ID do incidente — 30.741 distintos no arquivo principal)
- **Granularidade:** Tabela fato (`incidentes.csv`) + tabelas dimensão (classificação, feridos, substâncias, tipo)
- **Encoding:** latin-1, sep `;`
- **Schema principal:** 13 colunas: Numero, Empresa, CNPJ, Data_de_criacao, Autoridades_comunicadas, Instalacao, Data_primeira_observacao, Hora, UF, Municipio, Ambiente, Classificacao_origem, Observacao
- **Relação 1:N:** Um incidente pode ter múltiplas classificações (45.240 registros), substâncias (31.535) e tipos (35.598)
- **Nulls relevantes:** `Tipo_de_Ferimento` 98,1% nulo (maioria dos incidentes sem feridos)
- **Observações:** Modelo estrela — `Numero` liga as 5 tabelas

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
