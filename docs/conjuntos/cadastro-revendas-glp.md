# Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo (GLP)

| Campo | Valor |
|-------|-------|
| **Slug** | `cadastro-revendas-glp` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#11) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Diária |
| **Formato** | CSV |
| **Fonte operacional** | Cadastro ANP |
| **Pasta local** | `data/raw/cadastro-revendas-glp/` |
| **Inventário ANP** | Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Cadastro de revendas de GLP (botijão e granel), com localização e situação.

## Relevância para anp-fuel-analytics

Mercado de gás engarrafado; complementa movimentação GLP e tancagem por grupo de produtos.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/cadastro-revendas-glp/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/cadastro-revendas-glp/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [movimentacao-derivados](movimentacao-derivados.md)
- [tancagem-abastecimento](tancagem-abastecimento.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #11 (SDL, Diária)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (cadastro-revendas-glp). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/cadastro-revendas-glp/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
