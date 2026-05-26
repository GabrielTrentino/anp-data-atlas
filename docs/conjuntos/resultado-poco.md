# Resultado de Poço

| Campo | Valor |
|-------|-------|
| **Slug** | `resultado-poco` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#38) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/resultado-de-poco |
| **Unidade ANP (inventário)** | SDP |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/resultado-poco/` |
| **Inventário ANP** | Resultado de poço |
| **Prioridade fuel-analytics** | Baixa (upstream) |

## Contexto

Classificação final de poços perfurados — descoberta comercial, sub-comercial, seco, produtor, injetor, etc. Cada registro associa um poço a seu resultado (tipo de fluido encontrado, classificação ANP).

## Relevância para anp-fuel-analytics

Indicador da qualidade exploratória. Poços produtores de óleo/gás eventualmente alimentam o sistema de abastecimento. Taxa de sucesso como métrica de saúde do setor upstream.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

## Cruzamentos sugeridos

- [producao-por-poco](producao-por-poco.md) — produção efetiva dos poços classificados como produtores
- [fase-exploracao](fase-exploracao.md) — poços perfurados durante a exploração
- [blocos-fase-exploratoria-encerrada](blocos-fase-exploratoria-encerrada.md) — resultado antes da devolução

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SDP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Taxa de sucesso

- **Sucesso exploratório** — % poços com descoberta comercial por ano; tendência.
- **Por bacia** — bacias com maior/menor taxa de sucesso; maturidade.
- **Por operador** — eficiência exploratória relativa; normalizada por investimento.
- **Poços secos** — distribuição geográfica; custo afundado estimado.

### Tipo de resultado

- **Fluido encontrado** — óleo vs gás vs condensado; evolução do mix ao longo dos anos.
- **Classificação** — produtor vs injetor vs especial; proporção.
- **Profundidade** — correlação entre profundidade e tipo de resultado; pré-sal vs pós-sal.

### Cruzamentos

- **Resultado × produção** — poços classificados como produtores que efetivamente produzem; lag.
- **Resultado × rodadas** — sucesso por rodada; qualidade dos blocos ofertados.
- **Resultado × acervo técnico** — dados sísmicos disponíveis vs taxa de sucesso.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/resultado-poco/`
3. Documentar schema e volume
