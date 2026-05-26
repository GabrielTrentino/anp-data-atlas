# Ações de Fiscalização do Abastecimento

| Campo | Valor |
|-------|-------|
| **Slug** | `fiscalizacao-abastecimento` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#2) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/acoes-de-fiscalizacao |
| **Unidade ANP (inventário)** | SFI |
| **Periodicidade** | Mensal |
| **Formato** | CSV / painéis |
| **Fonte operacional** | Fiscalização ANP |
| **Pasta local** | `data/raw/fiscalizacao-abastecimento/` |
| **Inventário ANP** | Ações de Fiscalização do Abastecimento |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Ações de fiscalização nos segmentos do abastecimento (documentos, agentes, resultados).

## Relevância para anp-fuel-analytics

Contexto regulatório e qualidade de mercado; alguns recortes só em painel dinâmico.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/fiscalizacao-abastecimento/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** validado — XLSX do painel dinâmico SFI, convertido para CSV consolidado.

- **Formato real:** XLSX (dois arquivos: 1998-2018, a-partir-2019)
- **Encoding:** nativo Excel (unicode)
- **Separador após prepare:** `;`
- **Colunas (11):** `uf`, `municipio`, `bairro`, `endereco`, `cnpj_cpf`, `agente_economico`, `segmento_fiscalizado`, `data_do_df`, `numero_do_documento`, `procedimento_de_fiscalizacao`, `resultado`

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| dados-fisc-1998-2018.xlsx | ~350k | Documentos de fiscalização | 1998-2018 | Sheet Planilha1 |
| dados-fisc-a-partir-2019.xlsx | ~280k | Documentos de fiscalização | 2019-2026 | Sheet v_dados_abertos_dfs |
| _prepared/fiscalizacao.csv | 631.167 | Consolidado | 1998-01 a 2026-05 | Normalizado |

## Qualidade e chaves

- Chave lógica candidata: `cnpj_cpf` + `data_fiscalizacao` + `numero_documento`
- 27 UFs, 35 segmentos fiscalizados distintos
- 18,2% dos CNPJs fiscalizados estão presentes no PMQC
- Resultado mais frequente: "Sem Registro de Ocorrência" (57k registros)

## Cruzamentos sugeridos

- [pmqc](pmqc.md)
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #2 (SFI, Mensal)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Evolução das ações fiscalizatórias

- **Série temporal** — número de ações de fiscalização por mês/ano (1998-2026); tendência de longo prazo.
- **Resultado das ações** — proporção de "Sem Registro de Ocorrência" vs. notificações vs. autuações por período.
- **Procedimentos por tipo** — evolução dos tipos de procedimento (coleta, notificação, interdição) ao longo do tempo.
- **Sazonalidade** — períodos de pico de fiscalização (ex.: antes de feriados, operações especiais).

### Geografia da fiscalização

- **Cobertura por UF** — número de ações per capita por estado; UFs sub/super fiscalizadas.
- **Mapa municipal** — municípios mais fiscalizados; correlação com número de postos (cadastro-revendas).
- **Concentração urbana** — fiscalização concentrada em capitais/cidades grandes ou distribuída?

### Segmentos e agentes

- **Fiscalização por segmento** — distribuição entre postos, distribuidores, TRR, etc.
- **Agentes reincidentes** — CNPJs com múltiplas ações de fiscalização; evolução entre visitas.
- **Resultados por segmento** — taxas de irregularidade são maiores em quais segmentos?

### Cruzamentos

- **Fiscalização × PMQC** — postos com não-conformidade na qualidade são mais fiscalizados? Lag entre resultado PMQC e ação fiscal.
- **Fiscalização × cadastro-revendas** — proporção de postos ativos que nunca foram visitados.
- **Fiscalização × preços** — postos com preço outlier recebem mais visitas?
- **Cobertura temporal** — intervalo médio entre fiscalizações no mesmo CNPJ.

## Uso neste atlas

**Status da exploração:** pipeline operacional (download + prepare + trusted + cruzamento). Trusted layer em `data/trusted/fiscalizacao-abastecimento/fiscalizacao.parquet`.

**Próximos passos (fuel-analytics):**

1. Notebook `01_perfil_exploratorio.ipynb` — análise temporal, segmentos, distribuição geográfica
2. Refined layer — série de infrações por UF/mês, cruzamento com PMQC (não-conformidade vs fiscalização)
