# Produção de petróleo e gás natural por estado e localização

| Campo | Valor |
|-------|-------|
| **Slug** | `producao-por-estado` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#34) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-estado-e-localizacao |
| **Unidade ANP (inventário)** | SDC / SDP |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P / estatística ANP |
| **Pasta local** | `data/raw/producao-por-estado/` |
| **Inventário ANP** | Produção de Petróleo e Gás Natural por Estado e Localização |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produção de petróleo, LGN e gás por UF e tipo de localização (terra/mar).

## Relevância para anp-fuel-analytics

Contexto upstream; normalizações per capita ou por capacidade de abastecimento.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/producao-por-estado/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/producao-por-estado/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [importacoes-exportacoes](importacoes-exportacoes.md)
- [anuario-estatistico](anuario-estatistico.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #34 (SDC / SDP, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (producao-por-estado). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/producao-por-estado/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
