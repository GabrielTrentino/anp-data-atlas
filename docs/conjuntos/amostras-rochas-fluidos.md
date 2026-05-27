# Amostras de Rochas e Fluidos

| Campo | Valor |
|-------|-------|
| **Slug** | `amostras-rochas-fluidos` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#4) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/amostras-de-rochas-e-fluidos |
| **Unidade ANP (inventário)** | SDT |
| **Periodicidade** | Eventual |
| **Formato** | CSV |
| **Fonte operacional** | Geociências / Acervo técnico |
| **Pasta local** | `data/raw/amostras-rochas-fluidos/` |
| **Inventário ANP** | Amostras de Rochas e Fluidos |
| **Prioridade fuel-analytics** | Baixa (geociências) |

## Contexto

Catálogo de amostras físicas de rochas (testemunhos, calhas, amostras laterais) e fluidos (óleo, gás, água de formação) coletadas em poços exploratórios e de produção. Armazenadas no Litoteca da ANP (Rio de Janeiro e Belém).

## Relevância para anp-fuel-analytics

Sem uso direto em análises de abastecimento. Relevante para pesquisa geológica e caracterização de reservatórios.

## Estrutura dos arquivos

> **Status:** validado — 8 ZIPs anuais (2018–2025) + 7 PDFs metadados.

- **Formato:** ZIP contendo CSVs (consolidação anual de amostras)
- **Arquivos:** `consolidacao-<ano>.zip` (2020–2025), `<ano>-consolidacao.zip` (2018–2019)
- **Tipos de amostras (por metadados):** calha, células, fluidos, lâminas, laterais, plugues, testemunhos
- **Metadados:** 7 PDFs (um por tipo de consolidação)

## Cruzamentos sugeridos

- [acervo-dados-tecnicos](acervo-dados-tecnicos.md) — acervo geral que contém as amostras
- [resultado-poco](resultado-poco.md) — poços dos quais as amostras foram coletadas
- [bacias-sedimentares](bacias-sedimentares.md) — localização geológica

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SDT
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Catálogo de amostras

- **Volume total** — número de amostras por tipo (rocha vs fluido); litoteca.
- **Cobertura por bacia/poço** — bacias com mais amostras disponíveis.
- **Disponibilidade para pesquisa** — amostras públicas vs em período de confidencialidade.

### Caracterização

- **Tipo de fluido** — óleo leve vs pesado vs gás; distribuição por bacia (se disponível).
- **Profundidade** — distribuição de profundidade das amostras; correlação com tipo de formação.

### Cruzamentos

- **Amostras × produção** — campos com mais amostras têm melhor caracterização e produtividade?
- **Amostras × resultado-poco** — amostras de poços secos vs produtores.

## Inventário empírico dos brutos

| Arquivo local | Formato | Notas |
|---------------|---------|-------|
| `amostras-de-rocha-sedimentar.zip` | ZIP (shapefile) | Amostras de rocha sedimentar |
| `amostras-de-coquina.zip` | ZIP (shapefile) | Amostras de coquina |
| `amostras-de-fluido.zip` | ZIP (shapefile) | Amostras de fluido |
| `amostras-de-lamina.zip` | ZIP (shapefile) | Amostras de lâmina |
| `amostras-de-plugue.zip` | ZIP (shapefile) | Amostras de plugue |
| `amostras-de-testemunho.zip` | ZIP (shapefile) | Amostras de testemunho |
| `amostras-de-calha.zip` | ZIP (shapefile) | Amostras de calha |
| `amostras-laterais.zip` | ZIP (shapefile) | Amostras laterais |
| `metadados-*.pdf` (7 arquivos) | PDF | Dicionários de dados por tipo de amostra |

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
