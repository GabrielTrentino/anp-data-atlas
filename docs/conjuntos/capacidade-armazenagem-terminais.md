# Capacidade de Armazenagem de Terminais

| Campo | Valor |
|-------|-------|
| **Slug** | `capacidade-armazenagem-terminais` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#9) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais |
| **Unidade ANP (inventário)** | SIM |
| **Periodicidade** | Semestral |
| **Formato** | CSV |
| **Fonte operacional** | Cadastro de terminais ANP |
| **Pasta local** | `data/raw/capacidade-armazenagem-terminais/` |
| **Inventário ANP** | Capacidade de armazenamento dos terminais… |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Capacidade de armazenagem de terminais (fluvial, lacustre, marítimo, terrestre) por empresa e local.

## Relevância para anp-fuel-analytics

Infra logística upstream do abastecimento; validação cruzada com tancagem (escopos diferentes).

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/capacidade-armazenagem-terminais/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/capacidade-armazenagem-terminais/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [tancagem-abastecimento](tancagem-abastecimento.md)
- [movimentacao-terminais-aquaviarios](movimentacao-terminais-aquaviarios.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #9 (SIM, Semestral)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (capacidade-armazenagem-terminais). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/capacidade-armazenagem-terminais/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
