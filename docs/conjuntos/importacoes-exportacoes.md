# Importações e exportações

| Campo | Valor |
|-------|-------|
| **Slug** | `importacoes-exportacoes` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#19) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/importacoes-e-exportacoes |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Estatística ANP / comércio exterior |
| **Pasta local** | `data/raw/importacoes-exportacoes/` |
| **Inventário ANP** | Importações e exportações de petróleo / derivados / etanol |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Importações e exportações de petróleo, derivados e etanol.

## Relevância para anp-fuel-analytics

Balanço oferta externa de combustíveis e derivados.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/importacoes-exportacoes/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — 4 CSVs (derivados, etanol, GN, petróleo) com sep `;`.

- **Separador:** `;`
- **Colunas:** `ANO`, `MÊS`, `PRODUTO`, `OPERAÇÃO COMERCIAL`, `IMPORTADO / EXPORTADO`, `DISPÊNDIO / RECEITA`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| importacoes-exportacoes-derivados.csv | 9.432 | Derivados imp/exp | 2000-2026 | 16 produtos |
| importacoes-exportacoes-etanol.csv | 684 | Etanol imp/exp | 2012-2026 | |
| importacao-gas-natural.csv | 630 | Gás natural imp | 2000-2026 | |
| importacoes-exportacoes-petroleo.csv | 630 | Petróleo imp/exp | 2000-2026 | |

## Qualidade e chaves

- Chave lógica: `ano` + `mes_abrev` + `produto` + `operacao`
- Volume importado derivados: 672M m³; exportado: 412M m³
- Sobreposição temporal com processamento: 2000-2026
- 16 produtos de derivados para cruzamento com vendas

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [processamento-petroleo-derivados](processamento-petroleo-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #19 (SDC, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + trusted + cruzamento). Trusted em `data/trusted/importacoes-exportacoes/`.

**Próximos passos (fuel-analytics):**

1. Notebook exploratório — balança comercial, dependência externa por produto
2. Refined layer — balanço produção + importação - exportação vs vendas (deficit/superávit por derivado)
