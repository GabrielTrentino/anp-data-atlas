# Processamento de petróleo e produção de derivados

| Campo | Valor |
|-------|-------|
| **Slug** | `processamento-petroleo-derivados` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#32) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/processamento-de-petroleo-e-producao-de-derivados |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Estatística de refino ANP |
| **Pasta local** | `data/raw/processamento-petroleo-derivados/` |
| **Inventário ANP** | Processamento de petróleo e produção de derivados (várias tabelas) |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Processamento de petróleo e produção de derivados por refinaria e tipo de produto.

## Relevância para anp-fuel-analytics

Oferta doméstica de derivados — contexto macro para abastecimento e vendas.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/processamento-petroleo-derivados/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — 6 CSVs com sep `;`.

- **Encoding:** UTF-8 / latin-1
- **Separador:** `;`
- **Colunas principais:** `ANO`, `MÊS`, `UNIDADE DA FEDERAÇÃO`, `REFINARIA`, `MATÉRIA PRIMA`/`PRODUTO`, `PROCESSADO`/`PRODUÇÃO`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| processamento-petroleo-m3-1990-2025.csv | 23.100 | Processamento por refinaria | 1990-2026 | Volume m³ |
| producao-derivados-petroleo-por-refinaria-m3-1990-2025.csv | 113.468 | Derivados por refinaria | 1990-2026 | 15 produtos |
| producao-derivados-centrais-petroquimicas-m3-2001-2025.csv | — | Centrais petroquímicas | 2001-2025 | |
| producao-derivados-xisto-m3-2001-2025.csv | — | Xisto | 2001-2025 | |
| producao-gas-combustivel-1000m3-2000-2025.csv | — | Gás combustível | 2000-2025 | |

## Qualidade e chaves

- Chave lógica: `ano` + `mes_abrev` + `refinaria` + `materia_prima`/`produto`
- 21 refinarias, 10 UFs
- 6 produtos em comum com vendas-derivados
- Período 1990-2026, volume total processado: 3.54 bilhões m³

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [importacoes-exportacoes](importacoes-exportacoes.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #32 (SDC, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + trusted + cruzamento). Trusted em `data/trusted/processamento-petroleo-derivados/`.

**Próximos passos (fuel-analytics):**

1. Notebook exploratório — série temporal por refinaria, mix de derivados
2. Refined layer — balanço oferta/demanda (processamento + importação - exportação vs vendas)
