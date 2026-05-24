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

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/importacoes-exportacoes/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [processamento-petroleo-derivados](processamento-petroleo-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #19 (SDC, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (importacoes-exportacoes). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/importacoes-exportacoes/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
