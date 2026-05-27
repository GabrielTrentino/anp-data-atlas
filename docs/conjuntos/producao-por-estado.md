# Produção de petróleo e gás natural por estado e localização

| Campo | Valor |
|-------|-------|
| **Slug** | `producao-por-estado` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#34) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/producao-de-petroleo-e-gas-natural-por-estado-e-localizacao |
| **Unidade ANP (inventário)** | SDC / SDP |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P / estatística ANP |
| **Pasta local** | `data/raw/producao-por-estado/` |
| **Inventário ANP** | Produção de Petróleo e Gás Natural por Estado e Localização |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Produção de petróleo, LGN e gás por UF e tipo de localização (terra/mar).

## Relevância para anp-fuel-analytics

Contexto upstream; normalizações per capita ou por capacidade de abastecimento.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/producao-por-estado/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — 6 CSVs (petróleo, GN, LGN, queima, consumo próprio, GN disponível) com sep `;`.

- **Separador:** `;`
- **Colunas:** `ANO`, `MÊS`, `GRANDE REGIÃO`, `UNIDADE DA FEDERAÇÃO`, `PRODUTO`, `LOCALIZAÇÃO`, `PRODUÇÃO`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| producao-petroleo-m3.csv | 7.920 | Petróleo por UF | 1997-2026 | TERRA/MAR |
| producao-gas-natural-1000m3.csv | 7.643 | Gás natural por UF | 1997-2026 | 1000 m³ |
| producao-lgn-m3.csv | — | LGN por UF | — | |
| queima-e-perda-gn-1000m3.csv | — | Queima e perda | — | |
| consumo-proprio-gn1000m3.csv | — | Consumo próprio | — | |
| gn-disponivel-1000m3.csv | — | GN disponível | — | |

## Qualidade e chaves

- Chave lógica: `ano` + `mes_abrev` + `uf` + `produto` + `localizacao`
- 11 UFs produtoras (petróleo), localizações TERRA/MAR
- Volume total petróleo: 3.63 bilhões m³ (1997-2026)
- 7 UFs em comum com processamento (refinarias)

## Cruzamentos sugeridos

- [importacoes-exportacoes](importacoes-exportacoes.md)
- [anuario-estatistico](anuario-estatistico.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #34 (SDC / SDP, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Produção primária

- **Ranking de estados produtores** — RJ domina? Evolução do share de cada UF ao longo de 30 anos.
- **Terra vs Mar** — evolução da produção offshore vs onshore; pré-sal como inflexão.
- **Produção de gás natural** — crescimento do gás associado vs não-associado; UFs emergentes.
- **Declínio de campos maduros** — estados com produção em queda (ex.: BA, SE, RN onshore).

### Fluxo produção → refino

- **Petróleo produzido vs processado** — volume extraído na UF vs volume processado nas refinarias locais.
- **Dependência logística** — UFs que produzem mas não refinam (necessidade de escoamento).
- **Autossuficiência estadual** — produção local cobre demanda local? (join com vendas-derivados).

### Gás natural

- **Queima e perda** — proporção de GN queimado/perdido vs disponibilizado; evolução (melhoria ambiental?).
- **Consumo próprio** — quanto do GN fica na plataforma/campo vs vai para mercado.
- **GN disponível** — série temporal do GN efetivamente ofertado; base para planejamento energético.

### Cruzamentos

- **Produção × producao-por-poco** — validação: soma por estado (poco) ≈ total estado (esta série)?
- **Produção × processamento** — petróleo produzido alimenta quais refinarias? Fluxo implícito inter-UF.
- **Produção × importação** — estados que produzem e ainda assim importam (gargalo de refino).

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + trusted + cruzamento). Trusted em `data/trusted/producao-por-estado/`.

**Próximos passos (fuel-analytics):**

1. Notebook exploratório — concentração geográfica, evolução TERRA vs MAR
2. Refined layer — join com producao-por-poco (validação agregada) e processamento (fluxo produção→refino)

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-24 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
