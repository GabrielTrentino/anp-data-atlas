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

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/processamento-petroleo-derivados/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [importacoes-exportacoes](importacoes-exportacoes.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #32 (SDC, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (processamento-petroleo-derivados). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/processamento-petroleo-derivados/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
