# Anuário Estatístico Brasileiro do Petróleo, Gás Natural e Biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `anuario-estatistico` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#5) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/anuario-estatistico-brasileiro-do-petroleo-gas-natural-e-biocombustiveis |
| **Unidade ANP (inventário)** | SDC |
| **Periodicidade** | Anual (tabelas históricas ~10 anos) |
| **Formato** | CSV |
| **Fonte operacional** | Consolidação estatística ANP |
| **Pasta local** | `data/raw/anuario-estatistico/` |
| **Inventário ANP** | Anuário Estatístico |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

Consolida desempenho da indústria e do abastecimento em dezenas de tabelas CSV.

## Relevância para anp-fuel-analytics

Visão macro longa para validar séries mensais e benchmarks nacionais.

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/anuario-estatistico/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** sem CSV público — página não oferece dados abertos em formato tabular, apenas publicação em PDF/painel.

Não há dataset CSV/XLSX disponível para download automatizado.

## Inventário empírico dos brutos

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| — | — | — | — | Sem CSV público disponível |

## Qualidade e chaves

- Dados consolidados do Anuário já estão presentes nas demais séries (vendas, produção, importação)
- Não há valor incremental em pipeline dedicado

## Cruzamentos sugeridos

- [vendas-derivados](vendas-derivados.md)
- [producao-biocombustiveis](producao-biocombustiveis.md)
- [importacoes-exportacoes](importacoes-exportacoes.md)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #5 (SDC, Anual (tabelas históricas ~10 anos))
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** cancelado — sem CSV público. Dados do anuário já cobertos pelas séries individuais (processamento, produção, vendas, importações).

**Próximos passos:** nenhum (dados redundantes com outros conjuntos já integrados).

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-24 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
