# Fase de Exploração

| Campo | Valor |
|-------|-------|
| **Slug** | `fase-exploracao` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#16) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-exploracao |
| **Unidade ANP (inventário)** | SEP |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/fase-exploracao/` |
| **Inventário ANP** | Fase de Exploração |
| **Prioridade fuel-analytics** | Baixa (upstream) |

## Contexto

Dados sobre blocos exploratórios ativos — contratos de concessão na fase de exploração, com informações sobre concessionários, bacias, áreas e compromissos exploratórios (poços, sísmica).

## Relevância para anp-fuel-analytics

Indicador antecedente de oferta futura: blocos em exploração hoje são campos produtores em 5-10 anos. Pouco uso direto no curto prazo para análise downstream.

## Estrutura dos arquivos

> **Status:** validado — CSVs mensais de blocos sob contrato.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- **Arquivos:** 11 CSVs mensais (jan–out 2025, abr 2026) + 1 PDF metadados
- **Tamanho típico:** ~80 KB/mês
- **Conteúdo:** blocos exploratórios sob contrato — concessionário, bacia, área, rodada, status

| Arquivo | Período | Tamanho |
|---------|---------|---------|
| blocos-sob-contrato-jan.csv a -out.csv | 2025 | ~80 KB cada |
| blocos-sob-contrato_abr_2026.csv | abr/2026 | 7,5 KB |

## Cruzamentos sugeridos

- [dados-ep](dados-ep.md) — visão geral E&P
- [rodadas-licitacoes](rodadas-licitacoes.md) — rodadas que originaram os blocos
- [blocos-fase-exploratoria-encerrada](blocos-fase-exploratoria-encerrada.md) — blocos que saíram da fase
- [resultado-poco](resultado-poco.md) — resultado dos poços perfurados nos blocos

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SEP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Atividade exploratória

- **Blocos ativos por bacia** — distribuição geográfica da exploração; concentração em Santos/Campos vs fronteiras.
- **Evolução temporal** — quantidade de blocos em exploração por ano; impacto das rodadas.
- **Compromisso mínimo** — poços obrigatórios vs efetivamente perfurados; taxa de cumprimento.

### Operadores

- **Diversificação** — operadores com mais blocos; concentração vs diversificação.
- **Novos entrantes** — empresas que entraram recentemente via rodadas; perfil (IOCs, NOCs, independentes).
- **Parcerias** — frequência de consórcios; combinações mais comuns de operadores.

### Cruzamentos

- **Exploração × rodadas** — blocos de quais rodadas; tempo médio entre licitação e perfuração.
- **Exploração × resultado-poco** — taxa de sucesso por bacia; economicidade.
- **Exploração → produção** — blocos que passaram para fase de desenvolvimento; lead time.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/fase-exploracao/`
3. Documentar schema e volume
