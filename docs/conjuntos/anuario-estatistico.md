# Anuário Estatístico Brasileiro do Petróleo, Gás Natural e Biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `anuario-estatistico` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#5) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-estatistico-brasileiro-do-petroleo-gas-natural-e-biocombustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Anual (tabelas históricas ~10 anos) |
| **Formato** | CSV |
| **Fonte operacional** | Consolidação estatística ANP |
| **Pasta local** | `data/raw/anuario-estatistico/` |
| **Inventário ANP** | Anuário Estatístico |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Consolida desempenho da indústria e do abastecimento em dezenas de tabelas CSV.

## Relevância para anp-fuel-analytics

Visão macro longa para validar séries mensais e benchmarks nacionais.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/anuario-estatistico/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/anuario-estatistico/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [producao-biocombustiveis](producao-biocombustiveis.md)
- [importacoes-exportacoes](importacoes-exportacoes.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #5 (SDC, Anual (tabelas históricas ~10 anos))
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (anuario-estatistico). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/anuario-estatistico/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
