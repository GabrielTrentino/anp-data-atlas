# Produção de Petróleo e Gás Natural por Poço

| Campo | Valor |
|-------|-------|
| **Slug** | `producao-por-poco` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#35) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-poco |
| **Unidade ANP (inventário)** | SDP |
| **Periodicidade** | Mensal / Anual (séries históricas) |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/producao-por-poco/` |
| **Inventário ANP** | Produção de Petróleo e Gás Natural por Poço |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produção detalhada por poço (séries recentes e históricas).

## Relevância para anp-fuel-analytics

Granularidade fina de upstream; uso indireto em estudos de abastecimento regional.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/producao-por-poco/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/producao-por-poco/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [producao-por-estado](producao-por-estado.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #35 (SDP, Mensal / Anual (séries históricas))
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (producao-por-poco). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/producao-por-poco/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
