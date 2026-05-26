# Relação de Concessionários

| Campo | Valor |
|-------|-------|
| **Slug** | `relacao-concessionarios` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#36) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/relacao-de-concessionarios |
| **Unidade ANP (inventário)** | SEP / SDP |
| **Periodicidade** | Eventual (atualização cadastral) |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/relacao-concessionarios/` |
| **Inventário ANP** | Relação de Concessionários |
| **Prioridade fuel-analytics** | Baixa (cadastral E&P) |

## Contexto

Cadastro de empresas concessionárias de blocos exploratórios e campos produtores — dados cadastrais (razão social, CNPJ, sede) e contratos associados.

## Relevância para anp-fuel-analytics

Tabela de dimensão para cruzamento. Permite enriquecer análises de produção/exploração com dados do concessionário (grupo econômico, nacionalidade, porte).

## Estrutura dos arquivos

> **Status:** validado — 2 CSVs + 2 PDFs metadados.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- `relacao-concessionarios.csv` — cadastro dos concessionários (CNPJ, razão social, contratos)
- `relacao-pais-origem-concessionarios.csv` — país de origem de cada concessionário
- PDFs de metadados correspondentes

## Cruzamentos sugeridos

- [fase-exploracao](fase-exploracao.md) — blocos por concessionário
- [fase-desenvolvimento-producao](fase-desenvolvimento-producao.md) — campos por concessionário
- [producao-por-poco](producao-por-poco.md) — produção por operador
- [rodadas-licitacoes](rodadas-licitacoes.md) — vencedores por rodada

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SEP/SDP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Perfil dos concessionários

- **Distribuição por tipo** — IOCs vs NOCs vs independentes nacionais vs estrangeiras.
- **Concentração** — top 10 concessionários por número de contratos e por produção.
- **Evolução** — novos concessionários por ano; saídas (devoluções/cessões).

### Geográfico

- **Sede vs atuação** — concessionários com sede em SP/RJ vs operações em todo o país.
- **Internacionalização** — presença de empresas estrangeiras por bacia.

### Cruzamentos

- **Concessionários × produção** — ranking por produção efetiva; eficiência por contrato.
- **Concessionários × rodadas** — perfil dos vencedores; mudança ao longo das rodadas.
- **Concessionários × incidentes** — taxa de incidentes por operador (normalizada).

## Inventário empírico dos brutos

| Arquivo local | Formato | Notas |
|---------------|---------|-------|
| `relacao-concessionarios-cessao-onerosa.csv` | CSV | Concessionários do regime de cessão onerosa |
| `relacao-concessionarios-concessao.csv` | CSV | Concessionários do regime de concessão |
| `metadados-relacao-concessionarios-cessao-onerosa.pdf` | PDF | Dicionário de dados (cessão onerosa) |
| `metadados-relacao-concessionarios-concessao.pdf` | PDF | Dicionário de dados (concessão) |
