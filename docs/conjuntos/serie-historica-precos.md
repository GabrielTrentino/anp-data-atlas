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

## Contexto

Preços de revenda por **posto** (`CNPJ da Revenda`), produto e data de coleta. Três famílias no portal (`shpc/`):

| Pasta | Uso |
|-------|-----|
| `qus/` | Rolling — últimas 4 semanas |
| `dsan/YYYY/` | Mensal (gasolina/etanol, diesel/GNV, GLP) |
| `dsas/ca/`, `dsas/glp/` | Semestral histórico |

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

| Arquivo | Linhas (aprox.) | CNPJ únicos | Notas |
|---------|----------------:|------------:|-------|
| `qus/ultimas-4-semanas-gasolina-etanol.csv` | 45.211 | 6.147 | Abr–mai/2026 |
| `qus/ultimas-4-semanas-diesel-gnv.csv` | — | — | mesmo layout |
| `dsan/2025/precos-gasolina-etanol-12.csv` | — | — | dez/2025 |
| `dsas/ca/*.csv` (ZIP semestral) | — | — | ex.: AUTOMOTIVOS_2025.02 |

**Trusted MVP:** `data/trusted/serie-historica-precos/qus_gasolina_etanol.parquet`

```bash
py pipelines/run.py serie-historica-precos trusted_qus_gasolina
```

## Qualidade e chaves

| Chave | Uso |
|-------|-----|
| `cnpj` + `produto` + `data_coleta` | Série por posto e combustível |
| `uf` + `municipio` | Agregação regional |

## Cruzamento cadastro revendas (empírico)

Script: [cruzamento_cadastro_revendas.py](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/serie-historica-precos/scripts/cruzamento_cadastro_revendas.py)

| Métrica | Valor |
|---------|------:|
| CNPJs precos (qus gasolina/etanol) | 6.147 |
| Interseção com cadastro (46k postos) | **6.008 (97,7% dos CNPJs em preços)** |
| Cobertura cadastro com preço na janela | ~13% dos postos (esperado: LPC amostra semanal) |

**Join:** `precos.cnpj = cadastro.cnpj` — principal cruzamento útil do monorepo fuel.

## Conjuntos relacionados

- [cadastro-revendas-combustiveis.md](cadastro-revendas-combustiveis.md)
- [vendas-derivados.md](vendas-derivados.md)
- [tancagem-abastecimento.md](tancagem-abastecimento.md)

## Uso neste atlas

**Status:** exploração MVP no fuel (raw qus + trusted + join CNPJ). Expansão dsan/dsas histórico pendente.

**Próximos passos:** download mensal 2024–2025 · séries por produto · spread compra/venda × bandeira.
