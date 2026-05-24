# Programa de Monitoramento da Qualidade dos Combustíveis (PMQC)

| Campo | Valor |
|-------|-------|
| **Slug** | `pmqc` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#28) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pmqc-programa-de-monitoramento-da-qualidade-dos-combustiveis |
| **Unidade ANP (inventário)** | SBQ |
| **Periodicidade** | Mensal |
| **Formato** | CSV / relatórios |
| **Fonte operacional** | PMQC / fiscalização analítica |
| **Pasta local** | `data/raw/pmqc/` |
| **Inventário ANP** | PMQC — Programa de Monitoramento da Qualidade dos Combustíveis |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Indicadores de qualidade dos combustíveis comercializados e focos de não conformidade.

## Relevância para anp-fuel-analytics

Qualidade regulatória; contexto para anomalias em séries de preço ou movimentação.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/pmqc/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/pmqc/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [fiscalizacao-abastecimento](fiscalizacao-abastecimento.md)
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #28 (SBQ, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (pmqc). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/pmqc/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
