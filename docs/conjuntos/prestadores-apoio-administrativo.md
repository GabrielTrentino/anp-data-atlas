# Prestadores de Serviço de Apoio Administrativo

| Campo | Valor |
|-------|-------|
| **Slug** | `prestadores-apoio-administrativo` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#30) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/prestadores-de-servicos-de-apoio-administrativo |
| **Unidade ANP (inventário)** | SFI |
| **Periodicidade** | Eventual (cadastral) |
| **Formato** | CSV |
| **Fonte operacional** | Regulação / Cadastro |
| **Pasta local** | `data/raw/prestadores-apoio-administrativo/` |
| **Inventário ANP** | Prestadores de apoio administrativo |
| **Prioridade fuel-analytics** | Baixa (cadastral) |

## Contexto

Cadastro de prestadores de serviço de apoio administrativo habilitados pela ANP — empresas contratadas por concessionários para atividades administrativas (jurídico, contábil, etc.) no âmbito dos contratos de E&P.

## Relevância para anp-fuel-analytics

Relevância mínima para análises de abastecimento. Base cadastral de caráter regulatório.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

## Cruzamentos sugeridos

- [relacao-concessionarios](relacao-concessionarios.md) — concessionários que contratam os prestadores
- [fiscalizacao-conteudo-local](fiscalizacao-conteudo-local.md) — serviços administrativos como item de CL

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SFI
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Cadastro

- **Total de prestadores** — empresas habilitadas; evolução ao longo dos anos.
- **Por tipo de serviço** — jurídico, contábil, logístico, etc. (se classificado).
- **Distribuição geográfica** — sede dos prestadores por UF; concentração.

### Cruzamentos

- **Prestadores × concessionários** — quais concessionários mais contratam; concentração.
- **Prestadores × conteúdo local** — serviços administrativos nacionais vs importados.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/prestadores-apoio-administrativo/`
3. Documentar schema e volume
