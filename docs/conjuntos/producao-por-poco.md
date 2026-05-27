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

## Sugestões de análises

### Produção por poço e campo

- **Ranking de campos** — top campos por produção de petróleo e gás; concentração.
- **Curva de declínio** — produção por poço ao longo dos meses; modelagem de declínio exponencial/hiperbólico.
- **Poços novos vs maduros** — proporção da produção de poços recentes (< 2 anos) vs antigos.
- **Razão gás/óleo (RGO)** — evolução por bacia; indicador de maturidade do reservatório.

### Operadores e bacias

- **Concentração por operador** — Petrobras vs operadores independentes; evolução do share.
- **Produção por bacia** — ranking de bacias (Santos, Campos, Solimões, etc.); tendência.
- **Novos entrantes** — operadores que aparecem pela primeira vez em poços; leilões recentes.
- **Produtividade** — produção média por poço por operador (proxy de eficiência ou qualidade de ativos).

### Água e sustentabilidade

- **Razão água/óleo (RAO)** — indicador de maturidade; campos com RAO muito alta (injeção extensiva).
- **Horas de produção** — poços com baixa utilização (< 50% do mês); intermitentes por limitação?

### Cruzamentos

- **Poco × estado** — validar soma (producao-por-poco ≈ producao-por-estado em 2023).
- **Poco × processamento** — produção dos campos alimenta quais refinarias? (se contrato identificar).
- **Poco × importação** — produção nacional crescente reduz dependência de importação? Série longa.

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + prepare + trusted + cruzamento). Amostra 2023. Trusted em `data/trusted/producao-por-poco/`.

**Próximos passos (fuel-analytics):**

1. Expandir download para 2005-2022 (histórico completo ~50 ZIPs adicionais)
2. Notebook exploratório — concentração por operador/bacia, declínio de campos
3. Refined layer — agregação por bacia/UF vs producao-por-estado (validação cruzada)

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-24 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
