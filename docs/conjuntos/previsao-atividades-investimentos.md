# Previsão de Atividades e Investimentos Exploratórios

| Campo | Valor |
|-------|-------|
| **Slug** | `previsao-atividades-investimentos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#31) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/previsao-de-exploracao |
| **Unidade ANP (inventário)** | SEP |
| **Periodicidade** | Anual |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/previsao-atividades-investimentos/` |
| **Inventário ANP** | Previsão de Atividades e Investimentos Exploratórios |
| **Prioridade fuel-analytics** | Baixa (planejamento upstream) |

## Contexto

Programas exploratórios futuros declarados pelos concessionários — previsão de perfuração de poços, aquisição sísmica e investimentos planejados por contrato/bloco.

## Relevância para anp-fuel-analytics

Indicador forward-looking de oferta futura de petróleo e gás. Permite antever incrementos de produção em 5-10 anos.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

## Cruzamentos sugeridos

- [fase-exploracao](fase-exploracao.md) — blocos ativos correspondentes
- [rodadas-licitacoes](rodadas-licitacoes.md) — compromissos mínimos por rodada
- [resultado-poco](resultado-poco.md) — previsão vs resultado efetivo

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SEP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Investimentos

- **Volume total previsto** — investimento exploratório agregado por ano; tendência.
- **Por operador** — quem planeja investir mais; concentração.
- **Previsão vs realização** — investimentos previstos em anos anteriores vs efetivamente realizados.

### Atividades

- **Poços previstos** — quantidade por bacia; foco exploratório do setor.
- **Sísmica planejada** — km planejados de aquisição; onshore vs offshore.
- **Taxa de cumprimento** — atividades previstas vs realizadas no período.

### Cruzamentos

- **Previsão × resultado** — investimentos em bacias com alto vs baixo sucesso histórico.
- **Previsão × produção futura** — lag entre investimento e início de produção.
- **Previsão × preço do petróleo** — correlação com ciclo de commodities.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/previsao-atividades-investimentos/`
3. Documentar schema e volume
