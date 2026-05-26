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

> **Status:** validado — 5 CSVs + 6 PDFs metadados.

- **Formato:** CSV (sep `;`) e XLSX
- **CSVs:**
  - `obrigacaopdi.csv` — obrigações de PD&I por concessionário
  - `investimentos-prh.csv` — investimentos em formação de RH (PRH)
  - `projetos-rt-3-2015.csv` — projetos RT (regulamento técnico 3/2015)
  - `projetos-rt-5-2005.csv` — projetos RT (regulamento técnico 5/2005)
- **XLSX:**
  - `dados-abertos-unidades-pesquisa-area-tema-subtema.xlsx` — unidades de pesquisa por área
- **Metadados:** 6 PDFs

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

## Inventário empírico dos brutos

| Arquivo local | Formato | Notas |
|---------------|---------|-------|
| `obrigacaopdi.csv` | CSV | Obrigações de PD&I por concessionário |
| `investimentos-prh.csv` | CSV | Investimentos em formação de RH (PRH) |
| `projetos-rt-3-2015.csv` | CSV | Projetos RT (regulamento técnico 3/2015) |
| `projetos-rt-5-2005.csv` | CSV | Projetos RT (regulamento técnico 5/2005) |
| `dados-abertos-unidades-pesquisa-area-tema-subtema.xlsx` | XLSX | Unidades de pesquisa por área/tema |
| `metadados-*.pdf` (6 arquivos) | PDF | Dicionários de dados |
