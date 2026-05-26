# Participações Governamentais

| Campo | Valor |
|-------|-------|
| **Slug** | `participacoes-governamentais` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#25) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/participacoes-governamentais |
| **Unidade ANP (inventário)** | SPG |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Participações governamentais |
| **Pasta local** | `data/raw/participacoes-governamentais/` |
| **Inventário ANP** | Participações Governamentais |
| **Prioridade fuel-analytics** | Média (receitas do setor) |

## Contexto

Dados sobre receitas governamentais oriundas da exploração de petróleo e gás natural — royalties, participação especial, bônus de assinatura, pagamento pela ocupação/retenção de área. Detalhamento por campo, beneficiário (União, estados, municípios) e período.

## Relevância para anp-fuel-analytics

Indicador econômico do setor. Correlação direta com produção e preço do petróleo. Relevante para análise de impacto fiscal em estados produtores (RJ, ES, BA).

## Estrutura dos arquivos

> **Status:** validado — 15 CSVs anuais (royalties União 2011–2025).

- **Formato:** CSV (sep `;`, encoding UTF-8)
- **Naming:** `royalties-uniao-<ano>.csv` (2019+) ou `royalties_uniao_<ano>.csv` (2011–2018)
- **Tamanho típico:** ~1,3 KB/ano (tabela resumida União)
- **Cobertura:** 2011–2025 (15 anos)
- **Nota:** página contém 92 links totais (royalties estados, municípios, participação especial) — amostra limitada a União

## Cruzamentos sugeridos

- [producao-por-estado](producao-por-estado.md) — produção que gera os royalties
- [producao-por-poco](producao-por-poco.md) — produção por campo (base do cálculo)
- [rodadas-licitacoes](rodadas-licitacoes.md) — bônus de assinatura por rodada

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SPG
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Receitas

- **Evolução temporal** — total de royalties + participação especial por ano; correlação com Brent.
- **Por tipo** — royalties vs participação especial vs ocupação; proporção.
- **Por beneficiário** — União vs estados vs municípios; top beneficiários.

### Campos e concentração

- **Top campos** — campos que mais geram participações (Tupi/Lula, Búzios, etc.).
- **Pré-sal vs pós-sal** — proporção das receitas; crescimento do pré-sal.
- **Concentração estadual** — RJ domina? Tendência com novos campos em Santos.

### Impacto fiscal

- **Dependência municipal** — municípios onde royalties > 30% da receita total.
- **Volatilidade** — variação ano-a-ano; risco para planejamento orçamentário.
- **Per capita** — royalties/habitante por município; desigualdades.

### Cruzamentos

- **Participações × produção** — correlação direta; verificar alíquotas implícitas.
- **Participações × preço petróleo** — elasticidade da receita ao preço.
- **Participações × investimento** — reinvestimento das receitas em infraestrutura/social?

## Inventário empírico dos brutos

| Arquivo local | Formato | Encoding | Sep | Notas |
|---------------|---------|----------|:---:|-------|
| `royalties-uniao-*.csv` / `royalties_uniao_*.csv` (15 CSVs) | CSV | utf-8-sig | `,` | Royalties União 2011–2025; naming inconsistente entre anos |

> Página contém 92 links no total (royalties estados, municípios, participação especial, etc.). Amostra baixada limitada a royalties União. Sem PDFs neste diretório.
