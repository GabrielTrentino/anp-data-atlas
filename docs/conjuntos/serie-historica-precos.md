# Série Histórica de Preços de Combustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `serie-historica-precos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#40) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Semanal (LPC) — agregações mensais/semestrais nos arquivos abertos |
| **Formato** | CSV (+ ZIP semestral; XLSX em alguns recortes 2026) |
| **Fonte operacional** | Levantamento de Preços de Combustíveis (LPC) |
| **Pasta local** | `data/raw/serie-historica-precos/` |
| **Inventário ANP** | Série Histórica Preços — Combustíveis automotivos / GLP |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |
| **Estudo ativo** | [anp-fuel-analytics — serie-historica-precos](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/serie-historica-precos/) |

## Estrutura do portal (`shpc/`)

**SHPC** = pasta raiz no servidor da ANP: *Série Histórica de Preços de Combustíveis*  
(`.../dados-abertos/arquivos/shpc/`). A LPC é **semanal** (microdados por posto); o portal republica o mesmo layout em três recortes:

| Pasta | Seção no portal ANP | Significado | Exemplos de arquivo |
|-------|---------------------|-------------|---------------------|
| **`qus/`** | *Quatro últimas semanas* | Janela móvel (~4 semanas), atualizada semanalmente | `ultimas-4-semanas-gasolina-etanol.csv` |
| **`dsan/YYYY/`** | *Dados semanais agrupados mensalmente* | Todas as coletas do mês, por família de produto | `precos-gasolina-etanol-12.csv`, `precos-diesel-gnv-01.csv` |
| **`dsas/ca/`** | *Dados semanais agrupados por semestre* — combustíveis automotivos | Histórico longo (semestre a semestre) | `ca-2024-02.csv`, ZIP `AUTOMOTIVOS_2025.02` |
| **`dsas/glp/`** | Idem — GLP P13 | Histórico semestral GLP | `glp-2024-02.csv` |

> **Nota:** DSAN, DSAS e QUS são **nomes de diretório** no portal (não constam como glossário no metadados PDF). “Agrupados” = reúne as **coletas semanais** do período, não necessariamente médias pré-calculadas por posto.

**Famílias de produto (dsan):** `precos-gasolina-etanol`, `precos-diesel-gnv`, `precos-glp` (12 arquivos por ano).

```
shpc/
├── metadados-serie-historica-precos-combustiveis-1.pdf
├── qus/                          ← últimas 4 semanas (3 CSVs)
├── dsan/2024|2025/               ← mensal por família
└── dsas/ca/ | dsas/glp/          ← semestral histórico
```

## Contexto

Preços de revenda por **posto** (`CNPJ da Revenda`), produto e data de coleta. Resumo das pastas:

| Pasta | Uso |
|-------|-----|
| `qus/` | Análise **recente** (rolling 4 semanas) |
| `dsan/YYYY/` | Série **mensal** recente (ex.: 2024–2025 no fuel-analytics) |
| `dsas/ca/`, `dsas/glp/` | Série **semestral** desde ~2004 |

Metadados: `metadados-serie-historica-precos-combustiveis-1.pdf`

## Schema (nível posto — confirmado)

Separador **`;`** · UTF-8.

| Coluna | Descrição |
|--------|-----------|
| `Regiao - Sigla` / `Estado - Sigla` / `Municipio` | Geo |
| `Revenda` | Nome do posto |
| **`CNPJ da Revenda`** | Chave de join com cadastro |
| `Produto` | GASOLINA, ETANOL, DIESEL S10, GLP, GNV, … |
| `Data da Coleta` | Data da pesquisa |
| `Valor de Venda` / `Valor de Compra` | Preços (vírgula decimal no CSV) |
| `Bandeira` | Marca na coleta |

## Inventário empírico (MVP fuel-analytics)

| Recorte | Linhas | CNPJ únicos | Período |
|---------|-------:|------------:|---------|
| `qus/ultimas-4-semanas-gasolina-etanol.csv` | 45.211 | 6.147 | abr–mai/2026 |
| `dsan/2024–2025` gasolina/etanol (24 CSVs) | 1.166.580 | 12.369 | 2024 – 2025 |
| **Trusted `lpc_posto.parquet`** | 1.244.835 | 15.832 | qus + dsan gasolina |

Download mensal:

```bash
py pipelines/python/download_serie_historica_precos.py --years 2024,2025
py pipelines/run.py serie-historica-precos trusted_lpc_posto
```

**Arquivos brutos:** 71 CSVs `dsan` (2024–2025 × gasolina, diesel, GLP) + 3 `qus` + metadados PDF.

## Qualidade e chaves

| Chave | Uso |
|-------|-----|
| `cnpj` + `produto` + `data_coleta` | Série por posto e combustível |
| `uf` + `municipio` | Agregação regional |

## Cruzamento cadastro revendas (empírico)

Script: [cruzamento_cadastro_revendas.py](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/serie-historica-precos/scripts/cruzamento_cadastro_revendas.py)

| Métrica | Valor |
|---------|------:|
| CNPJs precos (`lpc_posto`, 2024–2025 + qus) | 15.832 |
| Interseção com cadastro (46k postos) | **11.472 (~24,9% dos postos)** |
| Janela `qus` (4 sem recentes) | **~98%** dos CNPJs em preços batem cadastro |

**Join:** `precos.cnpj = cadastro.cnpj` — principal cruzamento útil do monorepo fuel.

## Conjuntos relacionados

- [cadastro-revendas-combustiveis.md](cadastro-revendas-combustiveis.md)
- [vendas-derivados.md](vendas-derivados.md)
- [tancagem-abastecimento.md](tancagem-abastecimento.md)

## Sugestões de análises

### Evolução temporal e sazonalidade

- **Série de preço médio semanal** por produto e UF — tendência, volatilidade e sazonalidade intra-anual.
- **Spread compra/venda** — margem bruta da revenda por produto; evolução ao longo do tempo.
- **Convergência regional** — dispersão de preços entre UFs diminuindo ou aumentando? Coeficiente de variação temporal.
- **Impacto de reajustes Petrobras** — defasagem média entre anúncio de reajuste e repasse ao consumidor.

### Geografia e competição

- **Mapa de preço médio por município** — heatmap para gasolina, diesel, etanol; identificar outliers.
- **Efeito bandeira** — preço médio por bandeira (Branca vs. marcas) controlando por município.
- **Dispersão intra-municipal** — range de preços no mesmo município; cidades com maior/menor spread.
- **Ranking de municípios** — mais caros e mais baratos por produto, por região.

### Postos e mercado

- **Comportamento individual do posto** (CNPJ) — frequência de alteração, amplitude de variação, tempo de repasse.
- **Postos "fora da curva"** — outliers persistentes (abaixo de P5 ou acima de P95 por >4 semanas).
- **Correlação preço × qualidade** — cruzar com PMQC: postos baratos têm mais não-conformidades?
- **Entrada/saída de postos** — CNPJs que surgem ou desaparecem da pesquisa LPC ao longo da série.

### Cruzamentos derivados

- **Preço × vendas regionais** — elasticidade implícita: quando preço sobe, vendas caem? (join com vendas-derivados por UF/mês)
- **Preço × custo de produção** — preço etanol vs produção safra (producao-biocombustiveis); diesel vs petróleo (processamento).
- **Preço × importação** — derivados com preço doméstico vs. paridade de importação.

## Uso neste atlas

**Status:** exploração com download dsan 2024–2025, trusted consolidado e join CNPJ cadastro. Diesel/GLP trusted e notebook pendentes.

**Próximos passos:** download mensal 2024–2025 · séries por produto · spread compra/venda × bandeira.

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-24 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
