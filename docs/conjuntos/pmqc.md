# Programa de Monitoramento da Qualidade dos Combustíveis (PMQC)

| Campo | Valor |
|-------|-------|
| **Slug** | `pmqc` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#28) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc-programa-de-monitoramento-da-qualidade-dos-combustiveis |
| **Unidade ANP (inventário)** | SBQ |
| **Periodicidade** | Mensal |
| **Formato** | CSV (`;` sep, UTF-8 c/ BOM) |
| **Fonte operacional** | PMQC / fiscalização analítica |
| **Pasta local** | `data/raw/pmqc/` |
| **Inventário ANP** | PMQC — Programa de Monitoramento da Qualidade dos Combustíveis |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Microdados de ensaios analíticos de combustíveis coletados em postos revendedores. O programa monitora gasolina, óleo diesel e etanol, com ~80–110 mil ensaios/mês.

## Relevância para anp-fuel-analytics

Qualidade regulatória; identifica postos com não-conformidade para análise cruzada com preços e fiscalização.

## Estrutura dos arquivos (portal `pmqc/`)

CSVs mensais organizados por ano. Nomes inconsistentes:

| Período | Padrão de nome | Exemplo |
|---------|---------------|---------|
| 2016–2018 | `pmqc_YYYY_MM.csv` | `pmqc_2016_01.csv` |
| 2019–2021 | `YYYY-MM-pmqc.csv` | `2019-01-pmqc.csv` |
| 2022 (misto) | ambos padrões | `2022-01-pmqc.csv`, `pmqc_2022_07.csv` |
| 2023–2024 | `pmqc-MM.csv` | `pmqc-01.csv` |
| 2025 (misto) | 3 variantes | `pmqc-01.csv`, `pmqc_2025_04.csv`, `pmqc-2025-07.csv` |
| 2026+ | `pmqc_YYYY_MM.csv` | `pmqc_2026_01.csv` |

## Schema (19 colunas, consistente 2024–2026)

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| DataColeta | DATE | Data da coleta no posto |
| IdNumeric | INT | ID interno do ensaio |
| GrupoProduto | VARCHAR | Gasolina / Óleo Diesel / Etanol |
| Produto | VARCHAR | Detalhe (GASOLINA C COMUM, ÓLEO DIESEL B S10 - COMUM, etc.) |
| RazaoSocialPosto | VARCHAR | Nome do posto |
| CnpjPosto | VARCHAR | CNPJ do posto (com pontuação) |
| Distribuidora | VARCHAR | Bandeira do posto |
| Endereço | VARCHAR | Logradouro |
| Município | VARCHAR | Cidade |
| Latitude / Longitude | DOUBLE | Coordenadas |
| Uf | VARCHAR | UF (2 letras) |
| RegiaoPolitica | VARCHAR | Região política |
| Ensaio | VARCHAR | Nome do teste analítico (27 tipos distintos) |
| Resultado | VARCHAR | Valor medido |
| UnidadeEnsaio | VARCHAR | Unidade de medida |
| Conforme | BOOL | Sim/Não |

## Inventário empírico dos brutos (2024–2026)

| Período | Arquivos | Linhas totais | Notas |
|---------|----------|---------------|-------|
| 2024-01 a 2024-10 | 10 | ~946.154 | schema consistente |
| 2025-01 a 2025-12 | 12 | ~946.136 | schema consistente |
| 2026-01 a 2026-04 | 4 | ~339.018 | schema consistente |
| **Total** | **26** | **~2.231.308** | |

## Qualidade e chaves

- **Encoding:** UTF-8 com BOM
- **Chave lógica:** `cnpj` + `data_coleta` + `ensaio`
- **Granularidade:** um ensaio por linha (vários ensaios por coleta/posto)
- **Taxa não-conformidade:** 0,01% (234/2.2M) — diesel concentra 96%
- **Cobertura geográfica:** 19 UFs (amostragem, não censo)

## Cruzamentos sugeridos

| Parceiro | Chave join | Sobreposição |
|----------|-----------|--------------|
| [serie-historica-precos](serie-historica-precos.md) | `cnpj` | 7.757 postos (29,3% do PMQC) |
| [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md) | `cnpj` | pendente |
| [fiscalizacao-abastecimento](fiscalizacao-abastecimento.md) | `cnpj` / `uf` + período | postos autuados vs não-conformes |

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #28 (SBQ, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional no fuel-analytics — trusted 2024–2026 concluído.

**Próximos passos (fuel-analytics):**

1. Download anos anteriores (2016–2023) para série longa
2. Notebook exploratório (distribuição geográfica, sazonalidade não-conformidade)
3. Refined: join com preços (postos não-conformes × preço praticado)
4. Série temporal taxa não-conformidade por UF/produto
