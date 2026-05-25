# Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos

| Campo | Valor |
|-------|-------|
| **Slug** | `cadastro-revendas-combustiveis` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#12) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automoveis |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Diária |
| **Formato** | CSV + PDF metadados |
| **Fonte operacional** | Cadastro ANP / i-SIMP |
| **Pasta local** | `data/raw/cadastro-revendas-combustiveis/` |
| **Inventário ANP** | Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |
| **Estudo ativo** | [anp-fuel-analytics — cadastro-revendas-combustiveis](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/cadastro-revendas-combustiveis/) |

## Contexto

Cadastro de **postos revendedores** de combustíveis automotivos: razão social, CNPJ, endereço, UF/município, bandeira e datas cadastrais. É a fonte canônica de **CNPJ no varejo** para cruzar com preços, fiscalização e mapas — distinto da [tancagem-abastecimento](tancagem-abastecimento.md) (capacidade de armazenagem em instalações SIMP) e da [movimentacao-derivados](movimentacao-derivados.md) (volumes por **agente regulado** distribuidor).

## Estrutura dos arquivos

| Arquivo | Descrição |
|---------|-----------|
| `dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv` | Snapshot cadastral |
| `metadados-revendedores-varejistas-combustiveis-automoveis.pdf` | Metadados ANP |

**Separador:** `;` · **Encoding:** UTF-8 no arquivo atual (DuckDB auto-detect); pandas em scripts auxiliares usa `latin-1` se necessário.

### Amostra inspecionada (extração 2026-05)

| Campo | Valor |
|-------|-------|
| Linhas | **46.095** |
| Granularidade | 1 linha por posto (CODIGOISIMP / CNPJ únicos) |
| UFs | 27 |

| Coluna raw | Coluna trusted | Descrição |
|------------|----------------|-----------|
| `CODIGOISIMP` | `codigo_isimp` | Código instalação i-SIMP (7 dígitos) |
| `AUTORIZACAO` | `autorizacao` | Número de autorização |
| `DATAPUBLICACAO` | `data_publicacao` | Data publicação cadastro |
| `RAZAOSOCIAL` | `razao_social` | Razão social |
| `CNPJ` | `cnpj` | CNPJ sem máscara (14 dígitos) |
| `ENDERECO` … `CEP` | `endereco` … `cep` | Localização |
| `UF` / `MUNICIPIO` | `uf` / `municipio` | Geo |
| `BANDEIRA` | `bandeira` | Marca ou Bandeira Branca |
| `DATAVINCULACAO` | `data_vinculacao` | Vínculo com bandeira |

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Notas |
|---------------|-------:|---------|-------|
| `dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv` | 46.095 | 46.095 CNPJ únicos | Bandeira Branca ~49% |

Regenerar:

```bash
py estudos/cadastro-revendas-combustiveis/export_inventario_raw.py
```

**Trusted (fuel-analytics):** `data/trusted/cadastro-revendas-combustiveis/revendas.parquet`

```bash
py pipelines/run.py cadastro-revendas-combustiveis trusted
```

## Qualidade e chaves

| Chave | Uso |
|-------|-----|
| `cnpj` | Join primário com preços LPC, fiscalização, pontos |
| `codigo_isimp` | Ligação conceitual com `CodInstalacao` SIMP (quando o posto possui instalação cadastrada) |
| `uf` + `municipio` | Agregações territoriais |
| `bandeira` | Market share varejo |

**Validado:** zero duplicatas em `cnpj` e `codigo_isimp` na extração atual.

## Cruzamentos (empírico)

Script: [cruzamento_tancagem_movimentacao.py](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/cadastro-revendas-combustiveis/scripts/cruzamento_tancagem_movimentacao.py)

| Conjunto | Chave tentada | Resultado | Nota |
|----------|---------------|------------:|------|
| [tancagem-abastecimento](tancagem-abastecimento.md) | `cnpj` × `Cnpj` | **0%** | Tancagem ≈ 2,5k CNPJs (bases, TRR, terminais); não lista postos de rua |
| [tancagem-abastecimento](tancagem-abastecimento.md) | `codigo_isimp` × `CodInstalacao` | **0%** | Mesma população distinta na amostra |
| [movimentacao-derivados](movimentacao-derivados.md) | `razao_social` → agente | **~0,5%** | Movimentação = distribuidores; cadastro = varejo |

**Join recomendado:** cadastro ↔ **serie-historica-precos** / **pontos-abastecimento** por CNPJ; movimentação ↔ cadastro apenas quando o agente for de fato um revendedor (caso raro).

## Conjuntos relacionados

- [tancagem-abastecimento.md](tancagem-abastecimento.md) — capacidade armazenagem (outro universo de CNPJ)
- [movimentacao-derivados.md](movimentacao-derivados.md) — volumes SIMP por agente
- [serie-historica-precos.md](serie-historica-precos.md) — preços por posto (CNPJ esperado)
- [pontos-abastecimento.md](pontos-abastecimento.md) — infraestrutura de abastecimento
- [cadastro-revendas-glp.md](cadastro-revendas-glp.md) — cadastro GLP (paralelo)

## Uso neste atlas

**Status da exploração:** pipeline MVP no fuel-analytics (raw + trusted) · cruzamentos documentados · notebook/refined pendentes.

**Próximos passos (fuel-analytics):**

1. Notebook `01_perfil_exploratorio.ipynb` (geo, bandeira, entradas cadastrais)
2. Join **serie-historica-precos** por CNPJ
3. Refined agregado UF × bandeira
