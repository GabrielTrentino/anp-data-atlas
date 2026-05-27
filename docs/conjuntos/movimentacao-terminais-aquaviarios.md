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

## Sugestões de análises

### Fluxo logístico costeiro/fluvial

- **Volume por terminal** — ranking de terminais por volume total movimentado; concentração.
- **Série temporal** — evolução mensal do volume total (2013-2026); tendência e sazonalidade.
- **Sentido da operação** — recepção vs expedição; terminais importadores vs exportadores.
- **Modal de transporte** — peso de cabotagem, navegação interior, dutoviário na movimentação.

### Produtos e rotas

- **Mix de produtos** — quais derivados/biocombustíveis dominam a logística aquaviária?
- **Produtos por terminal** — especialização: terminais focados em gasolina vs. diesel vs. petróleo.
- **Volume por UF** — mapa de movimentação costeira; estados dependentes de cabotagem para abastecimento.

### Eficiência e utilização

- **Utilização vs capacidade** — (volume mensal × 12) / capacidade nominal = proxy de utilização anual (join com capacidade-armazenagem).
- **Terminais subutilizados** — volume < 30% da capacidade por >6 meses consecutivos.
- **Terminais congestionados** — volume > 80% da capacidade (potencial gargalo).

### Cruzamentos

- **Movimentação × vendas regionais** — volume recebido em terminal ≈ demanda local? (join com vendas-derivados por UF/mês).
- **Movimentação × importação** — volume de derivados importados vs recepção em terminais marítimos.
- **Movimentação × produção por estado** — fluxo: estados produtores (expedição) vs consumidores (recepção).

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + prepare + trusted + cruzamento). Trusted layer em `data/trusted/movimentacao-terminais-aquaviarios/movimentacao_terminais.parquet`.

**Próximos passos (fuel-analytics):**

1. Notebook `01_perfil_exploratorio.ipynb` — série temporal por terminal e produto
2. Refined layer — join com capacidade (taxa de utilização), correlação com vendas regionais

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-24 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
