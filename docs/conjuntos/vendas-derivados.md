# Vendas de derivados de petróleo e biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `vendas-derivados` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#42) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Mensal / Anual (subconjuntos) |
| **Formato** | CSV |
| **Fonte operacional** | Estatística ANP / distribuidoras |
| **Pasta local** | `data/raw/vendas-derivados/` |
| **Inventário ANP** | Vendas de combustíveis por segmento / por tipo / vendas anuais por município |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Volumes vendidos por distribuidoras, segmento, tipo de produto e recorte geográfico (estado/município).

## Relevância para anp-fuel-analytics

Demanda aparente por produto e região; complementa movimentação e produção.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/vendas-derivados/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/vendas-derivados/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [movimentacao-derivados](movimentacao-derivados.md)
- [producao-biocombustiveis](producao-biocombustiveis.md)
- [importacoes-exportacoes](importacoes-exportacoes.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #42 (SDC, Mensal / Anual (subconjuntos))
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (vendas-derivados). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/vendas-derivados/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
