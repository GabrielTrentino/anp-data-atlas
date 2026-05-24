# Registro de Óleos e Graxas Lubrificantes

| Campo | Valor |
|-------|-------|
| **Slug** | `registro-lubrificantes` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#37) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/registro-de-oleos-e-graxas-lubrificantes |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Conforme demanda |
| **Formato** | CSV |
| **Fonte operacional** | Registro de produtos |
| **Pasta local** | `data/raw/registro-lubrificantes/` |
| **Inventário ANP** | Registro de Óleos e Graxas Lubrificantes |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produtos lubrificantes registrados na ANP.

## Relevância para anp-fuel-analytics

Catálogo de produtos; cruzamento com PML e movimentação de lubrificantes.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/registro-lubrificantes/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/registro-lubrificantes/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [pml](pml.md)
- [movimentacao-derivados](movimentacao-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #37 (SDL, Conforme demanda)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (registro-lubrificantes). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/registro-lubrificantes/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
