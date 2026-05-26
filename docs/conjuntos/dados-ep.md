# Dados de E&P

| Campo | Valor |
|-------|-------|
| **Slug** | `dados-ep` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#13) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/gestao-contratos-exploracao-producao-dados-e-p |
| **Unidade ANP (inventário)** | SDP / SEP |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/dados-ep/` |
| **Inventário ANP** | Dados de Exploração e Produção (múltiplas sub-bases) |
| **Prioridade fuel-analytics** | Baixa (upstream genérico) |

## Contexto

Portal consolidado de dados de Exploração e Produção da ANP. Agrega informações sobre concessões, blocos, campos, poços e produção. Funciona como "hub" para sub-bases que também possuem páginas próprias (produção por poço, resultado de poço, etc.).

## Relevância para anp-fuel-analytics

Complementar ao foco downstream do monorepo. Utilidade principal em cruzamentos de supply (produção → processamento → abastecimento) e rastreamento de novos campos que alimentarão refinarias.

## Estrutura dos arquivos

> **Status:** parcial — apenas metadados (PDFs). Página não disponibiliza CSVs diretamente.

- 5 PDFs de metadados (consulta de área, poços exploratórios, indícios de HC, declaração de comercialidade)
- Dados de produção disponíveis via [fase-desenvolvimento-producao](fase-desenvolvimento-producao.md) e [producao-por-poco](producao-por-poco.md)

## Cruzamentos sugeridos

- [producao-por-poco](producao-por-poco.md) — dados detalhados por poço
- [producao-por-estado](producao-por-estado.md) — agregação por UF/localização
- [resultado-poco](resultado-poco.md) — classificação dos poços perfurados
- [fase-exploracao](fase-exploracao.md) — blocos em exploração ativa
- [fase-desenvolvimento-producao](fase-desenvolvimento-producao.md) — campos em desenvolvimento

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — sub-bases SDP/SEP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Panorama geral E&P

- **Evolução da produção nacional** — série histórica petróleo + gás; comparação com metas PDE.
- **Campos novos vs maduros** — proporção da produção de campos recentes (< 5 anos) vs antigos.
- **Pré-sal vs pós-sal** — split da produção; crescimento do pré-sal ao longo dos anos.

### Operadores e concessões

- **Market share por operador** — Petrobras vs independentes; tendência pós-cessão onerosa.
- **Atividade exploratória** — novos poços perfurados por ano; taxa de sucesso.
- **Rodadas e desinvestimentos** — novos entrantes por rodada; campos devolvidos.

### Cruzamentos

- **E&P × processamento** — produção dos campos vs capacidade de refino; gap logístico.
- **E&P × importação** — aumento de produção nacional reduz dependência de importação?
- **E&P × participações governamentais** — royalties vs produção por campo/bacia.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/dados-ep/`
3. Documentar schema e volume
