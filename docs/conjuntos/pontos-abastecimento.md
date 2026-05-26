# Pontos de Abastecimento Autorizados

| Campo | Valor |
|-------|-------|
| **Slug** | `pontos-abastecimento` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#27) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/pontos-de-abastecimento-autorizados |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Diário |
| **Formato** | CSV |
| **Fonte operacional** | Cadastro ANP |
| **Pasta local** | `data/raw/pontos-abastecimento/` |
| **Inventário ANP** | Dados Cadastrais de Pontos de Abastecimento Autorizados |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Instalações de pontos de abastecimento autorizados (estrutura cadastral distinta do revendedor varejista).

## Relevância para anp-fuel-analytics

Infraestrutura autorizada de abastecimento; cruzamento com cadastro de revendas e fiscalização.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/pontos-abastecimento/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/pontos-abastecimento/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md)
- [fiscalizacao-abastecimento](fiscalizacao-abastecimento.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #27 (SDL, Diário)
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

> Nota: este conjunto não possui CSV público. As análises abaixo seriam viáveis caso os dados se tornem disponíveis.

### Infraestrutura de abastecimento

- **Cobertura geográfica** — pontos autorizados por UF/município; identificar desertos de abastecimento.
- **Tipos de ponto** — distribuição entre postos terrestres, marítimos, aéreos, ferroviários.
- **Evolução temporal** — novos pontos autorizados vs desativados por ano.

### Cruzamentos potenciais

- **Pontos × cadastro-revendas** — validação cruzada de postos ativos (se dados existirem).
- **Pontos × tancagem** — capacidade autorizada nos pontos de abastecimento vs tancagem SIMP.
- **Pontos × vendas regionais** — cobertura vs demanda por combustível.

## Uso neste atlas

**Status da exploração:** documentação de referência criada (pontos-abastecimento). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/pontos-abastecimento/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
