# Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos

| Campo | Valor |
|-------|-------|
| **Slug** | `cadastro-revendas-combustiveis` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#12) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Diária |
| **Formato** | CSV |
| **Fonte operacional** | Cadastro ANP / i-SIMP |
| **Pasta local** | `data/raw/cadastro-revendas-combustiveis/` |
| **Inventário ANP** | Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Cadastro de postos revendedores de combustíveis automotivos (localização, bandeira, situação cadastral).

## Relevância para anp-fuel-analytics

Geografia do varejo e cruzamento com tancagem, preços e movimentação por município/UF.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/cadastro-revendas-combustiveis/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/cadastro-revendas-combustiveis/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [tancagem-abastecimento](tancagem-abastecimento.md)
- [pontos-abastecimento](pontos-abastecimento.md)
- [serie-historica-precos](serie-historica-precos.md)
- [movimentacao-derivados](movimentacao-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #12 (SDL, Diária)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (cadastro-revendas-combustiveis). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/cadastro-revendas-combustiveis/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
