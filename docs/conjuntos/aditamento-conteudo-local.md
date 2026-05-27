# Aditamento de Conteúdo Local

| Campo | Valor |
|-------|-------|
| **Slug** | `aditamento-conteudo-local` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#3) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/aditamento-de-conteudo-local |
| **Unidade ANP (inventário)** | SFI |
| **Periodicidade** | Eventual |
| **Formato** | CSV |
| **Fonte operacional** | Regulação / Conteúdo Local |
| **Pasta local** | `data/raw/aditamento-conteudo-local/` |
| **Inventário ANP** | Aditamento de conteúdo local |
| **Prioridade fuel-analytics** | Baixa (regulação) |

## Contexto

Registros de aditamentos (alterações contratuais) nos compromissos de conteúdo local de contratos de E&P. Conteúdo local é o percentual de bens e serviços nacionais utilizados em atividades de exploração e produção.

## Relevância para anp-fuel-analytics

Relevância indireta. Aditamentos podem indicar dificuldades da cadeia produtiva nacional e afetar cronogramas de desenvolvimento de campos.

## Estrutura dos arquivos

> **Status:** validado — 1 CSV + 1 PDF metadados.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- `planilha-aditamento-conteudo-local.csv` — registro de aditamentos de conteúdo local
- `metadados-aditamento.pdf` — dicionário de dados

## Cruzamentos sugeridos

- [fiscalizacao-conteudo-local](fiscalizacao-conteudo-local.md) — fiscalização do cumprimento
- [rodadas-licitacoes](rodadas-licitacoes.md) — compromissos originais nas rodadas
- [fase-desenvolvimento-producao](fase-desenvolvimento-producao.md) — campos afetados

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SFI
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Panorama regulatório

- **Volume de aditamentos** — total por ano; tendência (flexibilização crescente?).
- **Motivo** — tipos de alteração: redução de meta, extensão de prazo, mudança de escopo.
- **Impacto nos compromissos** — meta original vs meta aditada; redução média.

### Por contrato/rodada

- **Rodadas mais afetadas** — quais rodadas geraram mais aditamentos.
- **Operadores** — concessionários com mais pedidos de aditamento.
- **Fase afetada** — exploração vs desenvolvimento; onde conteúdo local é mais difícil.

### Cruzamentos

- **Aditamento × fiscalização** — contratos aditados têm menos autuações?
- **Aditamento × investimento** — impacto na cadeia de fornecedores local.
- **Aditamento × rodadas** — evolução das regras de CL ao longo das rodadas.

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `planilha-aditamento-conteudo-local.csv` | 1.046 | CSV | latin-1 | `;` | 11 | Ordem, Solicitação, Data do Protocolo, Contrato, Operador do Contrato, Nome do Bloco/Campo, Bacia, Localização, Rodada, Status, [outro] |
| `metadados-aditamento.pdf` | — | PDF | — | — | — | Dicionário de dados |

## Qualidade e chaves

- **Chave lógica:** `Ordem` (518 distintos — 1:1 com linhas)
- **Granularidade:** 1 linha por solicitação de aditamento
- **Encoding:** latin-1, sep `;`, 11 colunas
- **Colunas:** Ordem, Solicitação, Data do Protocolo, Contrato, Operador do Contrato, Nome do Bloco/Campo, Bacia, Localização, Rodada, Status, [observação]
- **Cobertura:** 287 contratos distintos, múltiplas rodadas e bacias
- **Nulls:** Sem nulls significativos
