# Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo (GLP)

| Campo | Valor |
|-------|-------|
| **Slug** | `cadastro-revendas-glp` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#11) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-das-revendas-de-gas-liquefeito-de-petroleo |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Diária (snapshot) |
| **Formato** | CSV (`;` sep, UTF-8 c/ BOM) |
| **Fonte operacional** | Cadastro ANP |
| **Pasta local** | `data/raw/cadastro-revendas-glp/` |
| **Inventário ANP** | Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Cadastro de revendas de GLP (botijão e granel), com localização, distribuidora vinculada e classificação de segurança NBR.

## Relevância para anp-fuel-analytics

Mercado de gás engarrafado; complementa movimentação GLP e tancagem por grupo de produtos.

## Schema (14 colunas)

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| CODIGOISIMP | INT | Código interno SIMP |
| AUTORIZACAO | VARCHAR | Número da autorização ANP |
| CNPJ | VARCHAR | CNPJ da revenda (14 dígitos) |
| RAZAOSOCIAL | VARCHAR | Razão social |
| ENDERECO | VARCHAR | Logradouro |
| COMPLEMENTO | VARCHAR | Complemento |
| BAIRRO | VARCHAR | Bairro |
| CEP | VARCHAR | CEP |
| UF | VARCHAR | UF (2 letras) |
| MUNICIPIO | VARCHAR | Município |
| DISTRIBUIDORA | VARCHAR | Distribuidora vinculada |
| CLASSE | VARCHAR | Classificação NBR (segurança) |
| DATAPUBLICACAO | DATE | Data de publicação no DOU |
| DATAVINCULACAO | DATE | Data de vinculação à distribuidora |

## Inventário empírico

| Arquivo | Linhas | Encoding | Sep |
|---------|-------:|----------|:---:|
| `cadastro-revendas-glp.csv` | 59.349 | UTF-8-sig | `;` |

## Qualidade e chaves

- **Chave lógica:** `cnpj` (59.346 distintos — quase 1:1)
- **Distribuidoras:** 19 (27,3% são "INDEPENDENTE")
- **Cobertura:** 27 UFs, 5.163 municípios
- **Classe NBR:** 113 variantes (padrão: "1 AREA - Classe X - NBR 15514")

## Cruzamentos sugeridos

| Parceiro | Chave join | Observação |
|----------|-----------|------------|
| [vendas-derivados](vendas-derivados.md) (GLP) | `uf` | Densidade revendas × volume vendido |
| [tancagem-abastecimento](tancagem-abastecimento.md) | `uf` / distribuidora | Capacidade GLP vs distribuição |
| [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md) | `cnpj` | Postos que também vendem GLP |
| [movimentacao-derivados](movimentacao-derivados.md) | `uf` | Volume movimentado GLP |

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #11 (SDL, Diária)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** pipeline operacional no fuel-analytics — trusted completo.

**Próximos passos (fuel-analytics):**

1. Notebook exploratório (mapa, concentração distribuidora/UF)
2. Refined: densidade revendas × volume vendas por município
3. Cross-match com cadastro-revendas-combustiveis (sobreposição CNPJ)
