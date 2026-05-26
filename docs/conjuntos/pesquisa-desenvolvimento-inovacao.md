# Pesquisa, Desenvolvimento e Inovação

| Campo | Valor |
|-------|-------|
| **Slug** | `pesquisa-desenvolvimento-inovacao` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#26) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-pesquisa-e-desenvolvimento-e-inovacao-pd-i |
| **Unidade ANP (inventário)** | SFI |
| **Periodicidade** | Anual |
| **Formato** | CSV |
| **Fonte operacional** | Regulação / PD&I |
| **Pasta local** | `data/raw/pesquisa-desenvolvimento-inovacao/` |
| **Inventário ANP** | Pesquisa, Desenvolvimento e Inovação |
| **Prioridade fuel-analytics** | Baixa (regulação/inovação) |

## Contexto

Dados sobre investimentos obrigatórios em Pesquisa, Desenvolvimento e Inovação (PD&I) por concessionários — cláusula regulatória que destina percentual da receita bruta de campos de alta produção para P&D em universidades, institutos e empresas.

## Relevância para anp-fuel-analytics

Indicador de inovação setorial. Pode revelar áreas prioritárias de P&D (transição energética, eficiência de refino, biocombustíveis) mas sem uso direto em análises de abastecimento.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

## Cruzamentos sugeridos

- [producao-por-poco](producao-por-poco.md) — campos de alta produção que geram obrigação de PD&I
- [participacoes-governamentais](participacoes-governamentais.md) — receitas totais vs investimento em P&D
- [relacao-concessionarios](relacao-concessionarios.md) — concessionários obrigados

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SFI
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Investimentos em P&D

- **Volume total** — investimento anual em PD&I; evolução (correlação com produção/preço).
- **Por concessionário** — quem mais investe; concentração (Petrobras domina?).
- **Por área temática** — transição energética, refino, E&P, meio ambiente; tendências.

### Instituições beneficiadas

- **Top instituições** — universidades/institutos que mais recebem recursos.
- **Distribuição geográfica** — concentração no eixo RJ-SP vs interiorização.
- **Tipo** — universidades vs centros de pesquisa vs empresas; proporção.

### Cruzamentos

- **PD&I × produção** — campos que geram mais obrigação; proporção da receita.
- **PD&I × biocombustíveis** — investimento em etanol/biodiesel vs P&D geral.
- **PD&I × participações governamentais** — P&D como % das receitas totais do setor.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/pesquisa-desenvolvimento-inovacao/`
3. Documentar schema e volume
