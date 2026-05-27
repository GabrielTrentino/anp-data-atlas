# Multas Aplicadas com Vencimento a partir de 2016

| Campo | Valor |
|-------|-------|
| **Slug** | `multas-2016` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#24) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/multas-aplicadas-com-vencimento-a-partir-de-2016 |
| **Unidade ANP (inventário)** | SFI / SFO |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Fiscalização |
| **Pasta local** | `data/raw/multas-2016/` |
| **Inventário ANP** | Multas (vencimento a partir de 2016) |
| **Prioridade fuel-analytics** | Média (fiscalização downstream) |

## Contexto

Registro de multas aplicadas pela ANP — autuações em ações de fiscalização com vencimento a partir de 2016. Inclui o agente autuado, valor da multa, motivo, UF, status do pagamento/recurso.

## Relevância para anp-fuel-analytics

Relevante para cruzamento com fiscalização do abastecimento: postos autuados e valores de multas por tipo de infração. Pode complementar análise de qualidade (PMQC) e regularidade do mercado.

## Estrutura dos arquivos

> **Status:** validado — 9 arquivos de dados (CSV/XLSX) + 1 PDF metadados.

- **Formato:** CSV (sep `;`) e XLSX
- **CSVs:**
  - `multas-aplicadas-2016a2019.csv` (2,3 MB) — consolidado 2016–2019
  - `multas-aplicadas-2020.csv` a `multas-aplicadas-2025.csv` — anuais
- **XLSX:**
  - `multas-2021-junho22.xlsx` (721 KB) — versão Excel 2021
  - `multas-aplicadas-2024-excel.xlsx`, `multas-aplicadas-2025.xlsx`
- **Metadados:** `metadados-multas-aplicadas-2016a2019.pdf`

## Cruzamentos sugeridos

- [fiscalizacao-abastecimento](fiscalizacao-abastecimento.md) — ações que geraram as multas
- [pmqc](pmqc.md) — postos com não-conformidade que podem ter sido multados
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md) — postos autuados
- [fiscalizacao-conteudo-local](fiscalizacao-conteudo-local.md) — multas de CL

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SFI/SFO
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Panorama das multas

- **Volume anual** — total de multas aplicadas por ano; tendência.
- **Valor total** — soma dos valores; ticket médio; distribuição (muitas pequenas vs poucas grandes).
- **Por motivo** — classificação das infrações; tipos mais frequentes (adulteração, irregularidade cadastral, etc.).
- **Status** — pago vs recurso vs cancelado; taxa de arrecadação efetiva.

### Geográfico

- **Por UF** — estados com mais multas; normalizado por número de postos/agentes.
- **Concentração** — reincidentes (agentes multados múltiplas vezes).

### Cruzamentos

- **Multas × fiscalização-abastecimento** — ações que geraram multas; perfil.
- **Multas × PMQC** — postos não-conformes que foram multados; lag entre amostragem e sanção.
- **Multas × cadastro** — postos multados que perderam autorização.
- **Multas × preços** — postos que praticam preços outlier e são fiscalizados.

## Inventário empírico dos brutos

| Arquivo local | Formato | Notas |
|---------------|---------|-------|
| `multas-aplicadas-2016a2019.csv` | CSV | Consolidado 2016–2019 (2,3 MB) |
| `multas-aplicadas-2020.csv` | CSV | Multas 2020 |
| `multas-aplicadas-2021.csv` | CSV | Multas 2021 |
| `multas-aplicadas-2022.csv` | CSV | Multas 2022 |
| `multas-aplicadas-2023.csv` | CSV | Multas 2023 |
| `multas-aplicadas-2024.csv` | CSV | Multas 2024 |
| `multas-aplicadas-2025.csv` | CSV | Multas 2025 |
| `multas-2021-junho22.xlsx` | XLSX | Versão Excel 2021 (721 KB) |
| `multas-aplicadas-2024-excel.xlsx` | XLSX | Versão Excel 2024 |
| `multas-aplicadas-2025.xlsx` | XLSX | Versão Excel 2025 |
| `metadados-multas-aplicadas-2016a2019.pdf` | PDF | Dicionário de dados |

## Qualidade e chaves

- **Chave lógica:** Não estruturada — CSVs são report-style (header = cabeçalho institucional da ANP)
- **Granularidade:** 1 linha por auto de infração/multa
- **Encoding:** utf-8-sig, sep `;`, 10 colunas (nomeadas como Unnamed — header real está na linha 2+)
- **Arquivos:** 6 CSVs por período:
  - `multas-aplicadas-2016a2019.csv` — 16.444 linhas
  - `multas-aplicadas-2020.csv` — 2.032 linhas
  - (+ 2021, 2022, 2023, 2024)
- **Nulls:** `Unnamed:6` ~8–11% nulo (campo de observação)
- **Observações:** Formato report-style com cabeçalho institucional na primeira linha. Requer skip de linhas iniciais para extrair dados reais. Colunas prováveis: Nº processo, CNPJ, valor, data vencimento, situação.

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
