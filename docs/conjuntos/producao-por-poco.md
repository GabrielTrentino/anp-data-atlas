# Produção de Petróleo e Gás Natural por Poço

| Campo | Valor |
|-------|-------|
| **Slug** | `producao-por-poco` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#35) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-poco |
| **Unidade ANP (inventário)** | SDP |
| **Periodicidade** | Mensal / Anual (séries históricas) |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/producao-por-poco/` |
| **Inventário ANP** | Produção de Petróleo e Gás Natural por Poço |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produção detalhada por poço (séries recentes e históricas).

## Relevância para anp-fuel-analytics

Granularidade fina de upstream; uso indireto em estudos de abastecimento regional.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/producao-por-poco/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — ZIPs mensais contendo CSVs com 48+ colunas (report-style); prepare extrai 13 colunas-chave.

- **Formato original:** ZIP → CSV (sep `;`, encoding latin-1)
- **Colunas extraídas (13):** `estado`, `bacia`, `campo`, `operador`, `numero_do_contrato`, `periodo`, `oleo_bbl_dia`, `condensado_bbl_dia`, `petroleo_bbl_dia`, `agua_bbl_dia`, `instalacao_destino`, `tipo_instalacao`, `tempo_de_producao_hs_por_mes`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| zips/ (12 arquivos 2023) | — | ZIPs mensais | 2023 | Amostra MVP |
| _prepared/producao_poco.csv | 24.870 | Consolidado 2023 | 2023 | 13 colunas |

## Qualidade e chaves

- Chave lógica: `campo` + `operador` + `periodo` (+ `instalacao_destino`)
- 11 estados produtores, 14 bacias, 47 operadores, 305 campos
- Produção total petróleo (2023): 21.5M bbl/dia (soma diária dos meses)
- 100% estados match com producao-por-estado (11/11)

## Cruzamentos sugeridos

- [producao-por-estado](producao-por-estado.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #35 (SDP, Mensal / Anual (séries históricas))
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + prepare + trusted + cruzamento). Amostra 2023. Trusted em `data/trusted/producao-por-poco/`.

**Próximos passos (fuel-analytics):**

1. Expandir download para 2005-2022 (histórico completo ~50 ZIPs adicionais)
2. Notebook exploratório — concentração por operador/bacia, declínio de campos
3. Refined layer — agregação por bacia/UF vs producao-por-estado (validação cruzada)
