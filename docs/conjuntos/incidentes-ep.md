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

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/incidentes-ep/`
3. Documentar schema e volume
