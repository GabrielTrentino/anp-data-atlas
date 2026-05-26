# Movimentação dos Terminais Aquaviários

| Campo | Valor |
|-------|-------|
| **Slug** | `movimentacao-terminais-aquaviarios` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#22) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/movimentacao-dos-terminais-aquaviarios |
| **Unidade ANP (inventário)** | SIM |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Terminais aquaviários |
| **Pasta local** | `data/raw/movimentacao-terminais-aquaviarios/` |
| **Inventário ANP** | Movimentação dos Terminais Aquaviários |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Movimentação em terminais aquaviários autorizados.

## Relevância para anp-fuel-analytics

Fluxo logístico costeiro/fluvial de derivados; complementa capacidade de terminais.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/movimentacao-terminais-aquaviarios/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — arquivo com extensão .csv mas formato XLSX interno; convertido via Python prepare.

- **Formato real:** XLSX disfarçado de CSV
- **Encoding:** unicode (Excel)
- **Colunas (13):** `mes_de_referencia`, `codigo_anp_do_terminal`, `nome_do_terminal`, `municipio_do_terminal`, `uf`, `sentido_da_operacao`, `tipo_da_operacao`, `modo_de_transporte`, `codigo_anp_do_produto`, `descricao_do_produto`, `sentido_modal`, `volume_m3`, `nome_da_instalacao`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| dados-abertos-movimentacao-terminais-aquaviarios.csv | 177.314 | Operações mensais | 2013-01 a 2026-02 | Formato XLSX |
| _prepared/movimentacao_terminais.csv | 177.314 | Normalizado | 2013-01 a 2026-02 | CSV real |

## Qualidade e chaves

- Chave lógica candidata: `codigo_terminal` + `mes_referencia` + `codigo_produto` + `sentido_modal`
- 78 terminais únicos, 457 produtos, 19 UFs
- Volume total acumulado: 5.67 bilhões m³
- 6 produtos em comum com vendas-derivados (gasolina, diesel, etanol, QAV, QI, gasolina aviação)

## Cruzamentos sugeridos

- [capacidade-armazenagem-terminais](capacidade-armazenagem-terminais.md)
- [movimentacao-derivados](movimentacao-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #22 (SIM, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + prepare + trusted + cruzamento). Trusted layer em `data/trusted/movimentacao-terminais-aquaviarios/movimentacao_terminais.parquet`.

**Próximos passos (fuel-analytics):**

1. Notebook `01_perfil_exploratorio.ipynb` — série temporal por terminal e produto
2. Refined layer — join com capacidade (taxa de utilização), correlação com vendas regionais
