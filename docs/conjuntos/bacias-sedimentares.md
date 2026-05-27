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

> **Status:** validado — 6 ZIPs (shapefiles) + 6 PDFs metadados.

- **Formato:** Shapefile (.shp/.dbf/.shx/.prj) empacotados em ZIP
- **Shapefiles disponíveis:**
  - `blocos-exploratorios.zip` — polígonos dos blocos exploratórios
  - `campos-producao.zip` — polígonos dos campos de produção
  - `shapefiles-rodadas-concluidas.zip` — áreas de rodadas
  - `shapefile-de-pocos.zip` — pontos dos poços
  - `shapefile-programas-geofisicos.zip` — linhas sísmicas/geofísicas
  - `shapefile-levantamentos-geoquimicos.zip` — pontos de geoquímica
- **Metadados:** 6 PDFs correspondentes

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

## Inventário empírico dos brutos

| Arquivo local | Formato | Notas |
|---------------|---------|-------|
| `Bacias_Summit.zip` | ZIP (shapefile) | Polígonos das bacias (Summit) |
| `BaciasMaritimas.zip` | ZIP (shapefile) | Bacias marítimas |
| `BaciaTerrestres.zip` | ZIP (shapefile) | Bacias terrestres |
| `LimitePoliticoMaritimo.zip` | ZIP (shapefile) | Limite político marítimo |
| `Plataforma_Continental.zip` | ZIP (shapefile) | Plataforma continental |
| `Brasil.zip` | ZIP (shapefile) | Contorno do Brasil |
| `metadados-*.pdf` (6 arquivos) | PDF | Dicionários de dados por shapefile |

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
