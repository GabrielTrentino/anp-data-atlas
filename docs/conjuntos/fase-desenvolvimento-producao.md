# Fase de Desenvolvimento e Produção

| Campo | Valor |
|-------|-------|
| **Slug** | `fase-desenvolvimento-producao` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#17) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/fase-de-desenvolvimento-e-producao |
| **Unidade ANP (inventário)** | SDP |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/fase-desenvolvimento-producao/` |
| **Inventário ANP** | Fase de Desenvolvimento e Produção |
| **Prioridade fuel-analytics** | Baixa (upstream) |

## Contexto

Informações sobre campos em fase de desenvolvimento ou produção — status dos Planos de Desenvolvimento (PD), reservas declaradas, instalações de produção e dados operacionais.

## Relevância para anp-fuel-analytics

Campos em produção alimentam refinarias e terminais. Útil para entender oferta doméstica por bacia e projetar impacto em abastecimento regional quando campos entram/saem de operação.

## Estrutura dos arquivos

> **Status:** validado — produção marítima mensal 1994–2026 (15 CSVs).

- **Formato:** CSV
- **Arquivos:** 15 CSVs de produção marítima (séries históricas segmentadas por período)
- **Cobertura:** 1994–2026

| Arquivo | Período |
|---------|---------|
| producao-mar-2026.csv | 2026 |
| producao-mar-2025.csv | 2025 |
| producao-mar-2023.csv | 2023 |
| producao-mar-2022.csv | 2022 |
| producao-mar-2021.csv | 2021 |
| producao-mar-2020.csv | 2020 |
| producao-mar-2019.csv | 2019 |
| producao-mar-2016-2018.csv | 2016–2018 |
| producao-mar-2013-2015.csv | 2013–2015 |
| producao-mar-2010-2012.csv | 2010–2012 |
| producao-mar-2005-2009.csv | 2005–2009 |
| producao-mar-2001-2004.csv | 2001–2004 |
| producao-mar-1998-2000.csv | 1998–2000 |
| producao-mar-1994-1997.csv | 1994–1997 |
| producao_por_poco_2024.csv | 2024 |

## Cruzamentos sugeridos

- [dados-ep](dados-ep.md) — visão geral E&P
- [producao-por-poco](producao-por-poco.md) — produção granular dos poços do campo
- [producao-por-estado](producao-por-estado.md) — agregação estadual
- [fase-exploracao](fase-exploracao.md) — blocos que evoluíram para desenvolvimento

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SDP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Campos e reservas

- **Campos ativos por bacia** — distribuição e concentração da produção.
- **Status dos PDs** — planos aprovados vs em revisão; atrasos.
- **Reservas vs produção** — taxa de depleção; campos próximos do esgotamento.
- **Novas declarações de comercialidade** — campos recém-descobertos em desenvolvimento.

### Instalações e infraestrutura

- **FPSOs e plataformas** — distribuição por bacia; capacidade instalada.
- **Gargalos** — campos com produção limitada por escoamento (dutos, FPSOs).
- **Desinvestimentos** — campos devolvidos ou com baixa produção; perfil.

### Cruzamentos

- **Desenvolvimento × produção** — campos em PD vs produção efetiva; lag de startup.
- **Desenvolvimento × processamento** — campos → refinarias; rotas de escoamento.
- **Desenvolvimento × participações** — royalties projetados por campo novo.

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `producao-mar-*.csv` (15 CSVs) | ~438.000 total | CSV | misto (utf-8-sig / latin-1) | `,` | 13–14 | Períodos: 1994-1997, 1998-2000, 2001-2004, 2005-2009, 2010-2012, 2013-2015, 2016-2018, 2019–2023 (anuais), 2025, 2026. Cols: Ano, Mês/Ano, Estado, Bacia, Campo, Poço, Ambiente, Instalação, Produção de Óleo, Produção de Condensado, Produção de Gás, Produção de Água, Injeção de Água |
| `producao_por_poco_2024.csv` | 15.230 | CSV | utf-8-sig | `,` | 14 | Formato atualizado com colchetes nos headers |

> Cobertura temporal: 1994–2026. Encoding inconsistente entre arquivos antigos (latin-1) e recentes (utf-8-sig).

## Qualidade e chaves

- **Chave lógica:** `Poço` + `Mês/Ano` (produção mensal por poço)
- **Granularidade:** 1 linha por poço × mês
- **Encoding:** misto (utf-8-sig nos mais antigos, latin-1 em 2016–2021), sep `,`
- **Schema:** 13–14 colunas (mudança de schema a partir de 2022 — headers com colchetes `[Ano]`)
- **Cobertura temporal:** 1994–2026 (15 CSVs segmentados por período)
- **Total estimado:** ~438k linhas, ~1.047 poços distintos no período mais antigo
- **Nulls relevantes:** `Injeção de Gás` (100%), `Injeção de Água para Recuperação Secundária` (100%), `Injeção de Água para Descarte` (100%) — colunas presentes mas vazias nos arquivos antigos
- **Observações:** Quebra de formato em 2022 (headers passam a usar colchetes); encoding inconsistente entre períodos

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
