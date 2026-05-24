# Movimentação de derivados de petróleo, gás natural e biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `movimentacao-derivados` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#21) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Mensal |
| **Formato** | CSV / ZIP (por produto) |
| **Fonte operacional** | SIMP — Resolução ANP nº 729/2018 |
| **Pasta local** | `data/raw/movimentacao-derivados/` |
| **Inventário ANP** | Movimentação de Derivados… (várias sub-bases por produto) |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Divulga volumes movimentados pelos agentes regulados, segmentados por produto (combustíveis líquidos, GLP, lubrificantes, TRR, etc.), com proteção de informações sigilosas conforme a resolução.

## Relevância para anp-fuel-analytics

Núcleo analítico do abastecimento: volumes por agente, produto e fluxo logístico. Complementa tancagem (capacidade) com movimentação real.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/movimentacao-derivados/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/movimentacao-derivados/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [tancagem-abastecimento](tancagem-abastecimento.md)
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md)
- [vendas-derivados](vendas-derivados.md)
- [serie-historica-precos](serie-historica-precos.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #21 (SDL, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (movimentacao-derivados). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/movimentacao-derivados/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
