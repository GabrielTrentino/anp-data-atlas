# Série Histórica de Preços de Combustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `serie-historica-precos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#40) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Semanal (LPC) — agregações mensais/semestrais nos arquivos abertos |
| **Formato** | CSV |
| **Fonte operacional** | Levantamento de Preços de Combustíveis (LPC) |
| **Pasta local** | `data/raw/serie-historica-precos/` |
| **Inventário ANP** | Série Histórica Preços — Combustíveis automotivos / GLP |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Preços medios de revenda/distribuição por localidade (gasolina C, etanol, diesel, GNV, GLP P13).

## Relevância para anp-fuel-analytics

Série temporal de preços para cruzar com tancagem regional, movimentação e eventos de mercado.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/serie-historica-precos/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/serie-historica-precos/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md)
- [tancagem-abastecimento](tancagem-abastecimento.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #40 (SDC, Semanal (LPC) — agregações mensais/semestrais nos arquivos abertos)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (serie-historica-precos). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/serie-historica-precos/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
