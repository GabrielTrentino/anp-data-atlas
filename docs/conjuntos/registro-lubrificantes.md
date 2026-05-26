# Registro de Óleos e Graxas Lubrificantes

| Campo | Valor |
|-------|-------|
| **Slug** | `registro-lubrificantes` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#37) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/registro-de-oleos-e-graxas-lubrificantes |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Conforme demanda |
| **Formato** | CSV |
| **Fonte operacional** | Registro de produtos |
| **Pasta local** | `data/raw/registro-lubrificantes/` |
| **Inventário ANP** | Registro de Óleos e Graxas Lubrificantes |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produtos lubrificantes registrados na ANP.

## Relevância para anp-fuel-analytics

Catálogo de produtos; cruzamento com PML e movimentação de lubrificantes.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/registro-lubrificantes/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — CSV com separador `;`, encoding latin-1-like (DuckDB auto_detect).

- **Encoding:** latin-1 / cp1252
- **Separador:** `;`
- **Colunas (20):** `REG`, `SITUACAO`, `PROCESSO`, `ANO`, `MARCA_COMERCIAL`, `DETENTOR`, `CNPJ_DETENTOR`, `TIPO_EMPRESA`, `TIPO_PRODUTO`, `FINALIDADE`, `APLICACAO`, `PRODUTOR`, `ORIGEM`, `SAE`, `ISO`, `NLGI`, `ND`, `COMPOSICAO`, `ACONDICIONAMENTO`, `OBS.`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| dados-abertos-registro-produtos.csv | 14.910 | Registros de produtos | 2008-2026 | Todos ATIVO |

## Qualidade e chaves

- Chave lógica candidata: `registro` (REG) — campo único por produto
- 14.910 registros, todos com situação ATIVO
- 293 detentores únicos, 2 tipos de produto (óleo lubrificante, graxa)
- 79,1% dos CNPJs detentores no PML estão presentes neste registro
- 68,0% das marcas do PML encontradas no registro

## Cruzamentos sugeridos

- [pml](pml.md)
- [movimentacao-derivados](movimentacao-derivados.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #37 (SDL, Conforme demanda)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + trusted + cruzamento). Trusted layer em `data/trusted/registro-lubrificantes/registro_lubrificantes.parquet`.

**Próximos passos (fuel-analytics):**

1. Notebook `01_perfil_exploratorio.ipynb` — distribuição por tipo, detentor, composição
2. Refined layer — join com PML (conformidade por marca), análise temporal de registros
