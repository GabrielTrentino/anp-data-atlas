# Vendas de derivados de petróleo e biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `vendas-derivados` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#42) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Mensal / Anual (subconjuntos) |
| **Formato** | CSV (`;` sep, UTF-8 c/ BOM) |
| **Fonte operacional** | Estatística ANP / distribuidoras |
| **Pasta local** | `data/raw/vendas-derivados/` |
| **Inventário ANP** | Vendas de combustíveis por segmento / por tipo / vendas anuais por município |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Volumes vendidos por distribuidoras, segmento, tipo de produto e recorte geográfico (estado/município). Série histórica longa (1990–presente).

## Relevância para anp-fuel-analytics

Demanda aparente por produto e região; complementa movimentação e produção.

## Estrutura dos arquivos (portal `vdpb/`)

O portal organiza os CSVs em subpastas:

| Subpasta | Descrição | Arquivo(s) |
|----------|-----------|------------|
| `vendas-derivados-petroleo-e-etanol/` | Série principal mensal (m³) | `vendas-combustiveis-m3-1990-2025.csv` |
| `vcs/` | Vendas por segmento | `vendas-combustiveis-segmento-m3-2012-2025.csv` |
| `vct/` | Vendas por tipo (diesel, GLP-vasilhame) | `vendas-oleo-diesel-tipo-m3-2013-2025.csv`, `vendas-glp-tipo-vasilhame-m3-2007-2025.csv` |
| `vendas-de-biodiesel/` | Biodiesel B100 | `vendas-biodiesel-b100-m3.csv` |
| `vaehdpm/` | Vendas anuais por município (gasolina, diesel, etanol, GLP, etc.) | 9 CSVs |

## Inventário empírico dos brutos

| Arquivo local | Linhas | Sep | Período | Cols chave |
|---------------|-------:|:---:|---------|------------|
| `vendas-combustiveis-m3-1990-2025.csv` | 93.960 | `;` | 1990–2026 | ANO, MÊS, GRANDE REGIÃO, UF, PRODUTO, VENDAS |
| `segmento/vendas-combustiveis-segmento-m3-2012-2025.csv` | 41.553 | `;` | 2012–2026 | ANO, MÊS, UF, PRODUTO, SEGMENTO, VENDAS |
| `tipo/vendas-oleo-diesel-tipo-m3-2013-2025.csv` | ~5k+ | `;` | 2013–2025 | ANO, MÊS, GRANDE REGIÃO, UF, PRODUTO, VENDAS |
| `tipo/vendas-glp-tipo-vasilhame-m3-2007-2025.csv` | ~5k+ | `;` | 2007–2025 | ANO, MÊS, GRANDE REGIÃO, UF, VASILHAME, VENDAS |
| `biodiesel/vendas-biodiesel-b100-m3.csv` | 1.852 | `,` | mensal | Mês/Ano, Região Origem, Região Destino, Vendas de Biodiesel |
| `municipio/vendas-anuais-de-gasolina-c-por-municipio.csv` | 180.839 | `;` | 1990–2024 | ANO, GRANDE REGIÃO, UF, PRODUTO, CÓDIGO IBGE, MUNICÍPIO, VENDAS |

## Qualidade e chaves

- **Encoding:** UTF-8 com BOM (byte order mark) — requer `utf-8-sig` ou strip BOM
- **Mês:** abreviado em português (JAN, FEV, ..., DEZ) na série principal/segmento
- **Vendas:** formatação numérica com `,` como separador decimal
- **Chave lógica (mensal):** `ano` + `mes` + `uf` + `produto`
- **Chave lógica (segmento):** `ano` + `mes` + `uf` + `produto` + `segmento`
- **Chave lógica (município):** `ano` + `codigo_ibge` + `produto`

## Cruzamentos sugeridos

| Parceiro | Chave join | Observação |
|----------|-----------|------------|
| [movimentacao-derivados](movimentacao-derivados.md) | `uf` + mês | 111 meses sobrepostos (2017–2026); vendas SDC vs movimentação SIMP |
| [serie-historica-precos](serie-historica-precos.md) | `produto` + `uf` + mês | Precisa mapear nomes (Gasolina C ↔ GASOLINA) |
| [producao-biocombustiveis](producao-biocombustiveis.md) | região + mês | Oferta vs demanda etanol/biodiesel |
| [importacoes-exportacoes](importacoes-exportacoes.md) | produto + mês | Balança (produção + importação – exportação ≈ vendas) |

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #42 (SDC, Mensal / Anual)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional no fuel-analytics — trusted mensal + segmento concluídos.

**Próximos passos (fuel-analytics):**

1. Trusted diesel/tipo, GLP/vasilhame, biodiesel, municipal
2. Notebook exploratório (evolução temporal, sazonalidade por produto)
3. Refined: join vendas × movimentação (volume SDC vs SIMP por UF/mês)
4. Refined: join vendas × preços médios (receita estimada)
