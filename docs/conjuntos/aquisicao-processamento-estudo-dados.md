# Aquisição, Processamento e Estudo de Dados

| Campo | Valor |
|-------|-------|
| **Slug** | `aquisicao-processamento-estudo-dados` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#6) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/aquisicao-procedimento-e-estudo-de-dados |
| **Unidade ANP (inventário)** | SDT |
| **Periodicidade** | Eventual |
| **Formato** | CSV |
| **Fonte operacional** | Geociências / Acervo técnico |
| **Pasta local** | `data/raw/aquisicao-processamento-estudo-dados/` |
| **Inventário ANP** | Aquisição, Processamento e Estudo de Dados |
| **Prioridade fuel-analytics** | Baixa (geociências) |

## Contexto

Registros de programas de aquisição de dados geofísicos (sísmica 2D/3D, gravimetria, magnetometria), processamento e estudos (reprocessamento, interpretação). Dados sobre contratos ANP e operações realizadas.

## Relevância para anp-fuel-analytics

Sem uso direto em análises de abastecimento. Relevante para entender o esforço exploratório e a maturidade do conhecimento geológico por bacia.

## Estrutura dos arquivos

> **Status:** validado — 9 CSVs + 2 ZIPs + 4 PDFs metadados.

- **Formato:** CSV (sep `;`) e ZIP (arquivos históricos)
- **CSVs recentes:**
  - `202601-ead-resultado-sismicos.csv` a `202603-ead-resultado-sismicos.csv` — resultados sísmicos 2026
  - `202501-ead-resultado-sismicos.xlsx` a `202505-ead-resultado-sismicos.csv` — resultados 2025
  - `2020-autorizacoes-despachos.csv` — autorizações e despachos 2020
- **ZIPs históricos:**
  - `2016-2019-autorizacoes-despachos.zip`
  - `2004-2015-autorizacoes-despachos.zip`
- **Metadados:** 4 PDFs

## Cruzamentos sugeridos

- [acervo-dados-tecnicos](acervo-dados-tecnicos.md) — dados armazenados no acervo
- [fase-exploracao](fase-exploracao.md) — compromissos de aquisição de dados por bloco
- [previsao-atividades-investimentos](previsao-atividades-investimentos.md) — investimento previsto em dados

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SDT
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Programas de aquisição

- **Volume sísmica** — km 2D e km² 3D por ano; tendência de investimento exploratório.
- **Onshore vs offshore** — distribuição da aquisição; custo relativo.
- **Por bacia** — onde há mais esforço; fronteiras exploratórias emergentes.
- **Empresas de serviço** — prestadoras mais ativas (se identificáveis).

### Processamento e estudos

- **Reprocessamento** — dados antigos reprocessados com tecnologia moderna; volume.
- **Estudos multicliente** — programas não-exclusivos disponíveis para compra; cobertura.

### Cruzamentos

- **Dados × taxa de sucesso** — mais dados disponíveis = mais sucesso? Correlação por bacia.
- **Dados × rodadas** — disponibilidade de sísmica vs atratividade em licitações.
- **Dados × investimentos** — previsão de aquisição vs realizado.

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Notas |
|---------------|-------:|---------|----------|:---:|-------|
| `2020-autorizacoes-despachos.csv` | 17 | CSV | latin-1 | `;` | 5 colunas; autorizações e despachos 2020 |
| `202501-ead-resultado-sismicos.xlsx` | — | XLSX | — | — | 29 KB; resultados sísmicos jan/2025 |
| `202502-ead-resultado-sismicos.csv` | ~15 | CSV | utf-8-sig | `;` | Resultados sísmicos fev/2025 |
| `202503-ead-resultado-sismicos.csv` | ~15 | CSV | utf-8-sig | `;` | Resultados sísmicos mar/2025 |
| `202504-ead-resultado-sismicos.csv` | ~11 | CSV | utf-8-sig | `;` | Resultados sísmicos abr/2025 |
| `202505-ead-resultado-sismicos.csv` | ~19 | CSV | utf-8-sig | `;` | Resultados sísmicos mai/2025 |
| `202601-ead-resultado-sismicos.csv` | ~15 | CSV | utf-8-sig | `;` | Resultados sísmicos jan/2026 |
| `202602-ead-resultado-sismicos.csv` | ~15 | CSV | utf-8-sig | `;` | Resultados sísmicos fev/2026 |
| `202603-ead-resultado-sismicos.csv` | ~15 | CSV | utf-8-sig | `;` | Resultados sísmicos mar/2026 |
| `2016-2019-autorizacoes-despachos.zip` | — | ZIP | — | — | Dados históricos 2016–2019 |
| `2004-2015-autorizacoes-despachos.zip` | — | ZIP | — | — | Dados históricos 2004–2015 |
| `metadados-*.pdf` (4 arquivos) | — | PDF | — | — | Dicionários de dados |

## Qualidade e chaves

- **Chave lógica:** Não estruturada — CSVs são relatórios mensais de avaliação (formato report-style)
- **Granularidade:** 1 linha por item avaliado/autorizado no mês
- **Encoding:** misto (latin-1 em 2020, utf-8-sig nos demais), sep `;`
- **Schema:** 5 colunas (títulos tipo relatório — header = título do documento)
- **Registros:** 11–19 linhas por mês (baixo volume — dados administrativos)
- **Observações:** Formato não-padrão (header é título do relatório, não nomes de colunas). Requer pré-processamento para extrair dados tabulares. ZIPs contêm dados sísmicos complementares.
