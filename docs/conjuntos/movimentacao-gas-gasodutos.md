# Movimentação de Gás Natural em Gasodutos de Transporte

| Campo | Valor |
|-------|-------|
| **Slug** | `movimentacao-gas-gasodutos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#23) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-consolidados-movimentacao-de-gas-natural-em-gasodutos-de-transporte |
| **Unidade ANP (inventário)** | SCM |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Gás Natural |
| **Pasta local** | `data/raw/movimentacao-gas-gasodutos/` |
| **Inventário ANP** | Movimentação em gasodutos de transporte |
| **Prioridade fuel-analytics** | Média (infraestrutura energética) |

## Contexto

Volumes transportados em gasodutos de transporte — por gasoduto, trecho, transportador, mês. Inclui capacidade contratada, volume efetivo e fator de utilização.

## Relevância para anp-fuel-analytics

Infraestrutura de transporte de gás é gargalo relevante para abastecimento energético. Análise de ociosidade/congestionamento complementa visão de oferta.

## Estrutura dos arquivos

> **Status:** validado — 14 CSVs mensais + 1 PDF metadados.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- **Arquivos:** movimentação mensal em gasodutos (jan 2024 – dez 2025)
- **Naming:** `gn_<mes>_<ano>.csv` ou `gn-<mes>.csv`
- **Metadados:** `metadados-gn-sim.pdf`

| Exemplo | Conteúdo |
|---------|----------|
| gn_dezembro_2025.csv | Volumes transportados dez/2025 |
| gn-janeiro.csv | Volumes transportados jan/2025 |

## Cruzamentos sugeridos

- [comercializacao-gas-natural](comercializacao-gas-natural.md) — volumes comercializados que passam pelos gasodutos
- [autorizacoes-gas-natural](autorizacoes-gas-natural.md) — transportadores autorizados
- [importacoes-exportacoes](importacoes-exportacoes.md) — volumes importados que entram via gasodutos (GASBOL)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SCM
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Infraestrutura

- **Mapa de gasodutos** — extensão, capacidade, transportador; malha nacional.
- **Fator de utilização** — volume/capacidade por trecho; gargalos vs ociosidade.
- **Expansões** — novos trechos ao longo dos anos; investimento em malha.

### Volumes

- **Evolução mensal** — total transportado (Mm³/dia); sazonalidade (despacho térmico no seco).
- **Por transportador** — concentração; TBG vs TAG vs NTS vs outros.
- **Origem-destino** — fluxo do gás: produção offshore → UPGN → city-gate.

### Cruzamentos

- **Gasodutos × comercialização** — coerência entre transportado e vendido.
- **Gasodutos × geração térmica** — pico de transporte coincide com despacho?
- **Gasodutos × importação** — volume via GASBOL vs produção nacional escoada.
- **Gasodutos × tancagem** — GLP/derivados vs gás: modais complementares.

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `gn_*.csv` / `gn-*.csv` (14 CSVs) | 5.400–11.100 cada | CSV | latin-1 | `;` | 6 | Dez/2024 a fev/2025 + abr–dez/2025 + jan–fev/2026. Cols: Código Instalação Transporte, Nome Instalação Transporte, Nome Instalação Gasoduto, Código Instalação Gasoduto, Competência, Volume (m³) |
| `metadados-gn-sim.pdf` | — | PDF | — | — | — | Dicionário de dados |
