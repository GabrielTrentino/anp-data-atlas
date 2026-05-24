# Movimentação dos Terminais Aquaviários

| Campo | Valor |
|-------|-------|
| **Slug** | `movimentacao-terminais-aquaviarios` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#22) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/movimentacao-dos-terminais-aquaviarios |
| **Unidade ANP (inventário)** | SIM |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Terminais aquaviários |
| **Pasta local** | `data/raw/movimentacao-terminais-aquaviarios/` |
| **Inventário ANP** | Movimentação dos Terminais Aquaviários |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Movimentação em terminais aquaviários autorizados.

## Relevância para anp-fuel-analytics

Fluxo logístico costeiro/fluvial de derivados; complementa capacidade de terminais.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/movimentacao-terminais-aquaviarios/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/movimentacao-terminais-aquaviarios/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [capacidade-armazenagem-terminais](capacidade-armazenagem-terminais.md)
- [movimentacao-derivados](movimentacao-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #22 (SIM, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (movimentacao-terminais-aquaviarios). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/movimentacao-terminais-aquaviarios/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
