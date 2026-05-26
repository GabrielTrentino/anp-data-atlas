# Capacidade de Armazenagem de Terminais

| Campo | Valor |
|-------|-------|
| **Slug** | `capacidade-armazenagem-terminais` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#9) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais |
| **Unidade ANP (inventário)** | SIM |
| **Periodicidade** | Semestral |
| **Formato** | CSV |
| **Fonte operacional** | Cadastro de terminais ANP |
| **Pasta local** | `data/raw/capacidade-armazenagem-terminais/` |
| **Inventário ANP** | Capacidade de armazenamento dos terminais… |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Capacidade de armazenagem de terminais (fluvial, lacustre, marítimo, terrestre) por empresa e local.

## Relevância para anp-fuel-analytics

Infra logística upstream do abastecimento; validação cruzada com tancagem (escopos diferentes).

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/capacidade-armazenagem-terminais/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — CSV direto do portal.

- **Encoding:** UTF-8
- **Separador:** `,`
- **Colunas (8):** `Tipo`, `Municipio`, `UF`, `Operador`, `Numero_de_tanques`, `Capacidade_nominal_petroleo`, `Capacidade_nominal_derivados_biocombustiveis`, `Capacidade_nominal_GLP`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| capacidade-armazenagem-terminais.csv | 134 | Terminais | Snapshot atual | Semestral |

## Qualidade e chaves

- Chave lógica candidata: `operador` + `municipio` + `uf` + `tipo`
- 134 terminais, 23 UFs
- Tipos: TERRESTRE (63), MARÍTIMO (58), FLUVIAL (9), LACUSTRE (4)
- Capacidade total derivados: 10.150.813 m³; GLP: 377.071 m³
- 63 operadores (capacidade) encontrados por nome em nome_instalacao (movimentação)

## Cruzamentos sugeridos

- [tancagem-abastecimento](tancagem-abastecimento.md)
- [movimentacao-terminais-aquaviarios](movimentacao-terminais-aquaviarios.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #9 (SIM, Semestral)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Infraestrutura de armazenagem

- **Capacidade por tipo** — ranking MARÍTIMO vs TERRESTRE vs FLUVIAL vs LACUSTRE; evolução se houver série.
- **Concentração por operador** — top operadores por capacidade total; HHI do segmento de terminais.
- **Distribuição geográfica** — mapa de capacidade por UF; litorais vs interior.
- **Dimensionamento** — capacidade média por tanque; terminais "gigantes" (outliers > P95).

### Produtos e mix

- **Capacidade por tipo de produto** — petróleo vs derivados/biocombustíveis vs GLP; proporção e evolução.
- **Especificidade regional** — UFs com capacidade majoritária em petróleo (produtoras) vs derivados (consumidoras).
- **GLP estratégico** — terminais com capacidade GLP significativa; cobertura regional para gás de cozinha.

### Cruzamentos

- **Capacidade × movimentação** — taxa de utilização (volume movimentado / capacidade nominal) por terminal/UF.
- **Capacidade × vendas regionais** — dias de estoque implícito (capacidade ÷ vendas mensais) por UF.
- **Capacidade × importação** — terminais marítimos próximos a portos de importação; gargalos de recepção.
- **Capacidade × tancagem-abastecimento** — comparar universo (terminais aquaviários vs. toda a cadeia SIMP).

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + trusted + cruzamento). Trusted layer em `data/trusted/capacidade-armazenagem-terminais/capacidade.parquet`.

**Próximos passos (fuel-analytics):**

1. Notebook `01_perfil_exploratorio.ipynb` — mapa de terminais, concentração por operador
2. Refined layer — join com movimentação (utilização vs capacidade), evolução semestral
