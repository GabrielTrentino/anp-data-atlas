# Programa de Monitoramento dos Lubrificantes (PML)

| Campo | Valor |
|-------|-------|
| **Slug** | `pml` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#29) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/o-programa-de-monitoramento-dos-lubrificantes-pml |
| **Unidade ANP (inventário)** | SBQ |
| **Periodicidade** | Conforme programa (boletins anuais) |
| **Formato** | CSV (`;` sep, UTF-8 c/ BOM) |
| **Fonte operacional** | PML |
| **Pasta local** | `data/raw/pml/` |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Microdados de amostras de lubrificantes coletadas no mercado e analisadas quanto à conformidade com registro e qualidade.

## Schema (18 colunas)

| Coluna | Descrição |
|--------|-----------|
| AMOSTRA | ID da amostra |
| DETENTOR | Fabricante/detentor do registro |
| CNPJ_DETENTOR | CNPJ do detentor |
| MARCA_COMERCIAL | Nome comercial do produto |
| GRAU_SAE | Viscosidade (15W40, 5W30, etc.) |
| REGISTRO | Número do registro ANP |
| NÍVEL_DESEMPENHO | API (SL, CI-4, SN, etc.) |
| LOTE | Lote de fabricação |
| DATA_FABRICAÇÃO | Data de fabricação |
| RESULTADO_FINAL | Conforme / Não Conforme |
| RESULTADO_REGISTRO | Conforme / Não Conforme |
| RESULTADO_QUALIDADE | Conforme / Não Conforme |
| MUNICÍPIO | Localização da coleta |
| UF | Estado |
| BOLETIM | Número do boletim |
| ANO | Ano da coleta |

## Inventário empírico

| Arquivo | Linhas | Encoding | Sep |
|---------|-------:|----------|:---:|
| `dados-abertos-pml.csv` | 13.726 | UTF-8-sig | `;` |

## Qualidade e chaves

- **Chave lógica:** `amostra` (13.700 distintos)
- **Detentores:** 158 fabricantes, 180 CNPJs
- **Período:** 2016–2026 (11 boletins)
- **Cobertura:** 21 UFs

## Cruzamentos sugeridos

| Parceiro | Chave join | Observação |
|----------|-----------|------------|
| [registro-lubrificantes](registro-lubrificantes.md) | `registro` / `cnpj_detentor` | Produto registrado vs monitorado |
| [movimentacao-derivados](movimentacao-derivados.md) | limitado | PML = qualidade, não volume |

## Sugestões de análises

### Qualidade de lubrificantes

- **Taxa de não-conformidade** por tipo de resultado (final, registro, qualidade) — evolução anual.
- **Ranking de detentores** — empresas com maior número de amostras reprovadas.
- **Distribuição geográfica** — UFs/municípios com maior incidência de não-conformidade.
- **Marcas problemáticas** — marcas comerciais com reprovação recorrente.

### Mercado de lubrificantes

- **SAE e composição** — distribuição por grau SAE e tipo de composição (mineral, sintético, semissintético).
- **Nível de desempenho** — padrões API/ACEA mais frequentes nas amostras.
- **Evolução temporal** — mudança no perfil de produtos monitorados ao longo dos anos.

### Cruzamentos

- **PML × registro-lubrificantes** — marcas amostradas que não constam no registro (irregular).
- **PML × registro** — detentores com muitos produtos registrados mas nenhum monitorado.
- **Não-conformidade × origem** — produtos nacionais vs importados: qual tem mais reprovação?
- **PML × fiscalização** — ações de fiscalização em revendedores com lubrificantes reprovados.

## Uso neste atlas

**Status da exploração:** pipeline operacional no fuel-analytics — trusted completo.

**Próximos passos:**

1. Notebook exploratório (taxa conformidade por ano/detentor)
2. Join com registro-lubrificantes

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-24 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
