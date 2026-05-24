# Programa de Monitoramento dos Lubrificantes (PML)

| Campo | Valor |
|-------|-------|
| **Slug** | `pml` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#29) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/o-programa-de-monitoramento-dos-lubrificantes-pml |
| **Unidade ANP (inventário)** | SBQ |
| **Periodicidade** | Conforme programa |
| **Formato** | CSV / relatórios |
| **Fonte operacional** | PML |
| **Pasta local** | `data/raw/pml/` |
| **Inventário ANP** | Programa de Monitoramento dos Lubrificantes |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Monitoramento da qualidade de lubrificantes no mercado.

## Relevância para anp-fuel-analytics

Segmento lubrificantes; complementa movimentação de lubrificantes e registro de produtos.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/pml/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/pml/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [movimentacao-derivados](movimentacao-derivados.md)
- [registro-lubrificantes](registro-lubrificantes.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #29 (SBQ, Conforme programa)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (pml). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/pml/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
