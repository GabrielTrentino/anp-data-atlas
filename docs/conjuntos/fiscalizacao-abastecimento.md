# Ações de Fiscalização do Abastecimento

| Campo | Valor |
|-------|-------|
| **Slug** | `fiscalizacao-abastecimento` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#2) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acoes-de-fiscalizacao |
| **Unidade ANP (inventário)** | SFI |
| **Periodicidade** | Mensal |
| **Formato** | CSV / painéis |
| **Fonte operacional** | Fiscalização ANP |
| **Pasta local** | `data/raw/fiscalizacao-abastecimento/` |
| **Inventário ANP** | Ações de Fiscalização do Abastecimento |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Ações de fiscalização nos segmentos do abastecimento (documentos, agentes, resultados).

## Relevância para anp-fuel-analytics

Contexto regulatório e qualidade de mercado; alguns recortes só em painel dinâmico.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/fiscalizacao-abastecimento/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/fiscalizacao-abastecimento/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [pmqc](pmqc.md)
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #2 (SFI, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada (fiscalizacao-abastecimento). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/fiscalizacao-abastecimento/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
