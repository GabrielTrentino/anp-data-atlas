# Distribuidores de combustíveis líquidos

| Campo | Valor |
|-------|-------|
| **Slug** | `distribuidores-combustiveis-liquidos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#15) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-distribuidores-de-combustiveis-liquidos |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Snapshot (atualização periódica) |
| **Formato** | CSV (`;` sep, Latin-1 / report-style) |
| **Fonte operacional** | Cadastro e autorizações ANP |
| **Pasta local** | `data/raw/distribuidores-combustiveis-liquidos/` |
| **Portal** | `.../arquivos/dcl/` |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Distribuidores autorizados pela ANP, contratos de cessão entre cedentes e cessionárias, e inutilizadores de botijões GLP.

## Relevância para anp-fuel-analytics

Atacado/distribuição — elos entre refinaria/terminal e varejo.

## Estrutura dos arquivos (portal `dcl/`)

| Arquivo | Tipo | Linhas | Descrição |
|---------|------|-------:|-----------|
| `planilha-aea-filiais.csv` | Report-style (latin-1) | 713 | Lista de distribuidores autorizados (AEA) |
| `ce-cr.csv` | CSV normal (latin-1) | 1.888 | Contratos de cessão/carregamento |
| `inutilizadores.csv` | Report-style (latin-1) | 36 | Inutilizadores de botijões |

## Schema — Distribuidores AEA (16 colunas)

| Coluna | Descrição |
|--------|-----------|
| Código Agente / i-SIMP | IDs internos |
| CNPJ | CNPJ da distribuidora |
| Nome Reduzido / Razão Social | Identificação |
| Endereço, Bairro, Município, UF, CEP | Localização |
| Situação | AUTORIZADA / CANCELADA / REVOGADA |
| Início da Situação / Data Publicação | Datas |
| Tipo de Ato / Autorização / Número | Detalhes regulatórios |

## Schema — Contratos CE/CR (29 colunas)

| Coluna chave | Descrição |
|--------------|-----------|
| TIPO DE CONTRATO | CARREGAMENTO / CESSÃO |
| CNPJ DA CEDENTE / CESSIONÁRIA | Partes do contrato |
| VOLUME (m³) | Volume contratado |
| Produtos (Gasolina A/C, Diesel, EAC, EHC, QAV...) | Flags por produto |

## Qualidade e chaves

- **Encoding:** Latin-1 (report-style com header nas primeiras linhas)
- **Chave lógica (AEA):** `cnpj` (713 distintos)
- **Chave lógica (CE/CR):** `cnpj_cedente` + `cnpj_cessionaria` + `inicio_contrato`
- **Cobertura:** 25 UFs, concentrado em SP (38%)

## Cruzamentos sugeridos

| Parceiro | Chave join | Observação |
|----------|-----------|------------|
| [movimentacao-derivados](movimentacao-derivados.md) | `cnpj` | Volume movimentado pela distribuidora |
| [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md) | distribuidora (nome) | Postos vinculados |
| [capacidade-armazenagem-terminais](capacidade-armazenagem-terminais.md) | `cnpj` | Terminais da distribuidora |

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #15 (SDL)
- [tancagem-abastecimento.md](tancagem-abastecimento.md)

## Sugestões de análises

### Estrutura do mercado de distribuição

- **Ranking de distribuidores** — por situação (ativo/inativo), tipo de autorização, UF.
- **Concentração geográfica** — HHI por UF baseado no número de autorizações.
- **Timeline de autorizações** — entrada e saída de distribuidores ao longo do tempo (data_publicacao).
- **Distribuidores por tipo de ato** — autorização vs. registro vs. comunicação.

### Contratos de cessão (CE/CR)

- **Rede de cessão** — grafo de relações cedente ↔ cessionária; clusters de empresas.
- **Volume contratado** — distribuição de volumes de cessão; contratos outliers.
- **Duração média** — tempo entre início e término dos contratos.

### Cruzamentos

- **Distribuidores × movimentação** — volume SIMP movimentado por distribuidor (match por CNPJ/razão social).
- **Distribuidores × cadastro-revendas** — quantos revendedores cada distribuidor abastece.
- **Distribuidores × vendas-derivados** — market share implícito por UF (se distribuidores ≈ oferta local).
- **Distribuidores × fiscalização** — autuações associadas a distribuidores vs. varejistas.

## Uso neste atlas

**Status da exploração:** pipeline operacional no fuel-analytics — trusted AEA completo.

**Próximos passos (fuel-analytics):**

1. Trusted contratos cessão (resolver encoding latin-1 no DuckDB)
2. Notebook exploratório (mapa, timeline autorizações)
3. Refined: join distribuidores × movimentação por CNPJ
