# Produção de biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `producao-biocombustiveis` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#33) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-biocombustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Estatística ANP |
| **Pasta local** | `data/raw/producao-biocombustiveis/` |
| **Inventário ANP** | Produção de Biocombustíveis — biodiesel / etanol |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produção de biodiesel e etanol (séries por período e região).

## Relevância para anp-fuel-analytics

Oferta de etanol/biodiesel no mix de abastecimento.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/producao-biocombustiveis/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — CSVs com sep `;`, volumes com decimal vírgula.

- **Separador:** `;`
- **Colunas biodiesel:** `ANO`, `MÊS`, `GRANDE REGIÃO`, `PRODUÇÃO`
- **Colunas etanol:** `ANO`, `MÊS`, `GRANDE REGIÃO`, `UNIDADE DA FEDERAÇÃO`, `PRODUTO`, `PRODUÇÃO`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| producao-biodiesel-m3-2005-2023.csv + 2024-2026.csv | 24.004 | Biodiesel por região | 2005-2026 | 5 regiões |
| producao-etanol-anidro-hidratado-m3-2012-2026.csv | 9.288 | Etanol por UF/produto | 2012-2026 | ANIDRO + HIDRATADO |

## Qualidade e chaves

- Chave lógica: `ano` + `mes_abrev` + `grande_regiao` (+ `uf` + `produto` para etanol)
- Produção total biodiesel: 89.8M m³; etanol: 443.8M m³
- 27 UFs para etanol, 5 grandes regiões para biodiesel
- Vendas-derivados tem 11.745 registros de etanol para cruzamento

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [movimentacao-derivados](movimentacao-derivados.md)
- [serie-historica-precos](serie-historica-precos.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #33 (SDC, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + trusted + cruzamento). Trusted em `data/trusted/producao-biocombustiveis/`.

**Próximos passos (fuel-analytics):**

1. Notebook exploratório — tendência produção por região, sazonalidade
2. Refined layer — producao vs vendas etanol/biodiesel (autossuficiência regional)
