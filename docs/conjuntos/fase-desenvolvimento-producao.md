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

> **Status:** pendente — página ainda não explorada empiricamente.

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

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/fase-desenvolvimento-producao/`
3. Documentar schema e volume
