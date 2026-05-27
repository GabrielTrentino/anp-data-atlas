# Anomalias Conhecidas — Dados Abertos ANP

Registro de problemas técnicos e armadilhas encontrados durante a exploração empírica dos 42 conjuntos. Referência para pipelines e análises futuras.

---

## Encoding e separadores

| Conjunto | Problema | Impacto |
|----------|----------|---------|
| `comercializacao-gas-natural` | Encoding **UTF-16** (atípico no portal) | Requer parâmetro explícito na ingestão; pandas/DuckDB não detectam automaticamente |
| `fase-desenvolvimento-producao` | Encoding misto: utf-8-sig (1994–2015, 2020, 2022+) e latin-1 (2016–2019, 2021) | Pipeline precisa testar ambos por arquivo |
| `movimentacao-gas-gasodutos` | Encoding latin-1 com acentos corrompidos nos nomes de instalações | Normalizar nomes antes de joins |
| `distribuidores-combustiveis-liquidos` | Encoding latin-1, formato report-style (header institucional na linha 1) | Skip de linhas ou pré-processamento |

---

## Schema e headers

| Conjunto | Problema | Impacto |
|----------|----------|---------|
| `fase-desenvolvimento-producao` | A partir de 2022, headers usam colchetes: `[Ano]`, `[Mês/Ano]` | Schema muda de 14 para 13 colunas; require normalização de headers |
| `multas-2016` | CSVs em formato report-style — primeira linha é cabeçalho institucional da ANP, colunas nomeadas `Unnamed:0` a `Unnamed:9` | Requer identificação da linha real de header (geralmente linha 2 ou 3) |
| `pesquisa-desenvolvimento-inovacao` | Apenas `obrigacaopdi.csv` é tabular padrão; os demais (`investimentos-prh.csv`, etc.) são report-style | Ingestão automática falha nos report-style |
| `aquisicao-processamento-estudo-dados` | Headers são títulos do relatório mensal (ex: "Avaliação de Dados Sísmicos Fevereiro/2025") | Não é uma tabela convencional — cada CSV é um mini-relatório |
| `movimentacao-gas-gasodutos` | Formato **wide/pivotado** — 1 coluna por dia do mês (ex: `01/02/2025`, `02/02/2025`...) | Requer unpivot (melt) para gerar série temporal por gasoduto |

---

## Dados ausentes e nulls estruturais

| Conjunto | Problema | Impacto |
|----------|----------|---------|
| `fase-desenvolvimento-producao` | Colunas `Injeção de Gás`, `Injeção de Água (Recuperação)`, `Injeção de Água (Descarte)` — 100% nulas nos arquivos 1994–2000 | Campos existem no schema mas não eram coletados na época |
| `incidentes-ep` | `Tipo_de_Ferimento_barra_Fatalidade` — 98,1% nulo | Normal: maioria dos incidentes não envolve feridos |
| `fase-exploracao` | `3ª PE VENCIMENTO` (99% nulo), `DATA INÍCIO SUSPENSÃO` (90%) | Campos de fases contratuais avançadas — poucos blocos chegam lá |
| `fiscalizacao-conteudo-local` | `fiscalizacao-desenvolvimento-mar.csv` tem **0 linhas de dados** (apenas header) | Arquivo publicado vazio — desconsiderar ou reportar |
| `comercializacao-gas-natural` | `Preço em Reais por MMBtu` — 19% nulo em distribuidoras | Meses sem dado de preço disponível |

---

## Formato e valores

| Conjunto | Problema | Impacto |
|----------|----------|---------|
| `vendas-derivados` (municipal diesel) | Valores com vírgula decimal brasileira (`49796537,7`) em CSV separado por `;` | parse_vendas precisa trocar `,` por `.` antes de converter |
| `participacoes-governamentais` | 3 linhas de subtotal/total por arquivo (20% das linhas) resultam em nulls na coluna `competencia` | Filtrar linhas onde `competencia IS NULL` |
| `cadastro-revendas-glp` (municipal GLP) | Coluna `VENDAS` substituída por `P13` + `OUTROS` (schema diferente dos demais municipais) | Somar P13+OUTROS para obter vendas totais |

---

## Dados indisponíveis

| Conjunto | Situação | Alternativa |
|----------|----------|-------------|
| `anuario-estatistico` | Sem CSV público — apenas PDF e painel dinâmico | Dados cobertos pelas séries individuais (vendas, produção, importações) |
| `autorizacoes-gas-natural` | Página removida do portal (404) | Possível reestruturação; monitorar |
| `resultado-poco` | Apenas metadados (PDF) — CSV não localizado | Possivelmente acessível via BDEP |
| `pontos-abastecimento` | Apenas metadados (PDF) — dados via painel dinâmico | Verificar API interna do painel |
| `blocos-fase-exploratoria-encerrada` | Apenas metadados (PDF) | Dados possivelmente integrados em `fase-exploracao` |

---

## Tancagem — anomalia temporal

| Período | Problema | Detalhes |
|---------|----------|----------|
| Nov–Dez/2022 | Queda de **44%** no volume e **23%** nas linhas vs meses adjacentes | Publicação possivelmente incompleta — investigação aberta em `fuel-analytics/estudos/tancagem-abastecimento/TODO.md` |

---

## Como atualizar

Ao encontrar nova anomalia durante exploração ou pipeline:
1. Adicionar linha na tabela relevante acima
2. Referenciar o conjunto e o impacto prático
3. Se resolvido (ex: fix no pipeline), mover para seção "Resolvidas" (criar quando necessário)
