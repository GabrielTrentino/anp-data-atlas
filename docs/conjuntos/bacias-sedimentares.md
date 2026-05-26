# Dados Georreferenciados das Bacias Sedimentares Brasileiras

| Campo | Valor |
|-------|-------|
| **Slug** | `bacias-sedimentares` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#14) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-georreferenciados-das-bacias-sedimentares-brasileiras |
| **Unidade ANP (inventário)** | SDT |
| **Periodicidade** | Eventual (atualização cartográfica) |
| **Formato** | SHP / CSV |
| **Fonte operacional** | Geociências |
| **Pasta local** | `data/raw/bacias-sedimentares/` |
| **Inventário ANP** | Bacias Sedimentares Brasileiras |
| **Prioridade fuel-analytics** | Baixa (referência geográfica) |

## Contexto

Polígonos georreferenciados das bacias sedimentares brasileiras — limites oficiais utilizados pela ANP para demarcação de blocos, concessões e atividades exploratórias. Serve como base cartográfica para todo o setor de E&P.

## Relevância para anp-fuel-analytics

Tabela de dimensão geográfica. Pode ser usada para mapas temáticos (produção por bacia, instalações por bacia) em visualizações do atlas.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

Provável formato shapefile (.shp + .dbf + .shx + .prj) com polígonos das bacias.

## Cruzamentos sugeridos

- [producao-por-estado](producao-por-estado.md) — produção agregada por bacia
- [producao-por-poco](producao-por-poco.md) — localização dos poços nas bacias
- [fase-exploracao](fase-exploracao.md) — blocos dentro de cada bacia
- [rodadas-licitacoes](rodadas-licitacoes.md) — áreas licitadas por bacia

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SDT
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Cartografia

- **Mapa de referência** — visualização das bacias com área (km²) e classificação (marginal, interior, offshore).
- **Bacias produtoras** — destacar bacias com produção ativa (Santos, Campos, Solimões, Potiguar, etc.).
- **Fronteiras exploratórias** — bacias com blocos ofertados mas sem produção significativa.

### Métricas por bacia

- **Produção por km²** — densidade produtiva por bacia.
- **Investimento acumulado** — sísmica + poços por bacia (se cruzado com outros datasets).
- **Maturidade** — classificação qualitativa (madura, em exploração, fronteira).

### Cruzamentos

- **Bacias × produção** — ranking de bacias por volume produzido; concentração.
- **Bacias × rodadas** — áreas ofertadas dentro de cada bacia; atratividade relativa.
- **Bacias × incidentes** — taxa de incidentes normalizada por bacia.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear arquivos disponíveis (SHP / CSV)
2. Download para `data/raw/bacias-sedimentares/`
3. Documentar schema, projeção (CRS) e volume
