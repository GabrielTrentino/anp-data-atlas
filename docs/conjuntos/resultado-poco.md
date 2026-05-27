# Resultado de Poço

| Campo | Valor |
|-------|-------|
| **Slug** | `resultado-poco` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#38) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/resultados-de-poco |
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

> **Status:** parcial — apenas metadados (PDF). CSV não localizado na página.

- 1 PDF de metadados (`metadados-resultado-poco.pdf`)
- CSV com resultados de poço não encontrado (possível acesso via BDEP ou canal diferente)

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

## Inventário empírico dos brutos

| Arquivo local | Tipo | Notas |
|---------------|------|-------|
| `metadados-resultado-poco.pdf` | PDF | Metadados e dicionário de dados |

> CSV não disponível publicamente. Dados possivelmente acessíveis via BDEP ou canal restrito.

## Qualidade e chaves

- **Status:** Não validável empiricamente — apenas metadados (PDF) disponíveis no portal.
- **Schema esperado (conforme metadados):** Código do poço, campo, bacia, resultado (seco/subcomercial/comercial), profundidade
- **Chave lógica esperada:** `CodigoPoco`
- **Acesso alternativo:** Possivelmente disponível via BDEP (Banco de Dados de Exploração e Produção)

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
