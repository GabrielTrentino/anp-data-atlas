# Distribuidores de combustíveis líquidos

| Campo | Valor |
|-------|-------|
| **Slug** | `distribuidores-combustiveis-liquidos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#15) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-distribuidores-de-combustiveis-liquidos |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Mensal / Semanal / Semestral (subconjuntos) |
| **Formato** | CSV |
| **Fonte operacional** | Cadastro e autorizações ANP |
| **Pasta local** | `data/raw/distribuidores-combustiveis-liquidos/` |
| **Inventário ANP** | Distribuidores de Combustíveis Líquidos (várias bases) |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Distribuidores autorizados, contratos de cessão, inutilizadores de botijões GLP e início de atividade.

## Relevância para anp-fuel-analytics

Atacado/distribuição — elos entre refinaria/terminal e varejo.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/distribuidores-combustiveis-liquidos/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/distribuidores-combustiveis-liquidos/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [movimentacao-derivados](movimentacao-derivados.md)
- [capacidade-armazenagem-terminais](capacidade-armazenagem-terminais.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #15 (SDL, Mensal / Semanal / Semestral (subconjuntos))
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (distribuidores-combustiveis-liquidos). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/distribuidores-combustiveis-liquidos/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
