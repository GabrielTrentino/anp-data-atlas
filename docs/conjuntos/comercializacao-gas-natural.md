# Comercialização de Gás Natural

| Campo | Valor |
|-------|-------|
| **Slug** | `comercializacao-gas-natural` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#10) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/comercializacao-de-gas-natural |
| **Unidade ANP (inventário)** | SCM |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Gás Natural |
| **Pasta local** | `data/raw/comercializacao-gas-natural/` |
| **Inventário ANP** | Comercialização de Gás Natural |
| **Prioridade fuel-analytics** | Média (oferta energética) |

## Contexto

Volumes mensais de gás natural comercializados — por agente, origem (nacional/importado), destino (industrial, termelétrico, automotivo/GNV, distribuição canalizada). Dados sobre preços e contratos de fornecimento.

## Relevância para anp-fuel-analytics

Gás natural compete com GLP e diesel em alguns segmentos (industrial, geração). Entender o volume comercializado por segmento complementa análises de demanda energética.

## Estrutura dos arquivos

> **Status:** validado — 3 CSVs + 3 PDFs metadados.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- `distribuidoras-consumidores-livres.csv` — vendas a distribuidoras e consumidores livres
- `vendas-entre-produtores.csv` — transações entre produtores
- `vendas-aos-comercializadores.csv` — vendas a comercializadores
- PDFs de metadados correspondentes

## Cruzamentos sugeridos

- [autorizacoes-gas-natural](autorizacoes-gas-natural.md) — agentes autorizados
- [movimentacao-gas-gasodutos](movimentacao-gas-gasodutos.md) — transporte físico
- [importacoes-exportacoes](importacoes-exportacoes.md) — GN importado (Bolívia, GNL)
- [producao-por-estado](producao-por-estado.md) — produção nacional de gás

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SCM
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Volume e sazonalidade

- **Evolução mensal** — total comercializado (Mm³/dia); tendência e sazonalidade.
- **Mix de destinos** — industrial vs termelétrico vs automotivo vs distribuição; evolução.
- **Nacional vs importado** — dependência do gás boliviano e GNL spot; variação com câmbio.

### Preços

- **Preço médio por segmento** — industrial vs termelétrico vs GNV; spread.
- **Evolução de preços** — série temporal; indexação ao petróleo vs descolamento.
- **Competitividade** — GN vs GLP vs diesel no segmento industrial (R$/GJ).

### Agentes e mercado

- **Concentração** — market share por comercializador; Petrobras vs novos entrantes.
- **Impacto Nova Lei do Gás** — antes vs depois (2021); número de agentes, volumes.

### Cruzamentos

- **Comercialização × produção** — balanço nacional: produção + importação vs consumo.
- **Comercialização × geração elétrica** — despacho térmico vs volume de GN comercializado.
- **Comercialização × movimentação-derivados** — substituição: GN crescendo onde diesel industrial cai?

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `distribuidoras-consumidores-livres.csv` | 376 | CSV | UTF-16 | `;` | 6 | Ano, Mês, TipoMercado, RegiãoAgregada, Preço em Reais por MMBtu, Volume em mil m³/dia |
| `vendas-aos-comercializadores.csv` | 49 | CSV | UTF-16 | `;` | 4 | Vendas a comercializadores |
| `vendas-entre-produtores.csv` | 226 | CSV | UTF-16 | `;` | 5 | Inclui BaciaAgregada |
| `metadados-distribuidoras-consumidores-livres.pdf` | — | PDF | — | — | — | Dicionário de dados |
| `metadados-vendas-aos-comercializadores.pdf` | — | PDF | — | — | — | Dicionário de dados |
| `metadados-vendas-entre-produtores.pdf` | — | PDF | — | — | — | Dicionário de dados |

## Qualidade e chaves

- **Chave lógica:** `Ano` + `Mês` + `TipoMercado`/`BaciaAgregada` (série temporal por segmento)
- **Granularidade:** 1 linha por mês × segmento de mercado
- **Encoding:** UTF-16, sep `;` (atípico — atenção na ingestão)
- **Arquivos:**
  - `distribuidoras-consumidores-livres.csv` — 375 linhas, 6 cols (Ano, Mês, TipoMercado, Região, Preço MMBtu, Volume mil m³/dia)
  - `vendas-aos-comercializadores.csv` — 48 linhas, 4 cols
  - `vendas-entre-produtores.csv` — 226 linhas, 5 cols (inclui BaciaAgregada)
- **Cobertura temporal:** ~7 anos (Ano com 7 valores distintos)
- **Nulls:** `Preço em Reais por MMBtu` 19,2% nulo em distribuidoras (meses sem dado de preço)
- **Observações:** Encoding UTF-16 incomum no portal ANP — requer tratamento especial na ingestão

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
