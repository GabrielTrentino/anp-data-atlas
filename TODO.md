# TODO — 42 conjuntos de dados abertos ANP

Rastreio de exploração e integração por conjunto. Catálogo oficial: [docs/dados-abertos.md](docs/dados-abertos.md).

**Legenda de etapas**

| Etapa | Descrição |
|-------|-----------|
| **Doc** | `docs/conjuntos/{slug}.md` — metadados, matriz de arquivos, lacunas |
| **Raw** | Amostra ou série em `data/raw/{slug}/` |
| **Emp.** | Inventário empírico (linhas, métricas por arquivo) no doc |
| **Fuel** | Estudo em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics) — notebooks + pipeline |
| **Int.** | Integração histórica documentada (pipeline atlas, quando aplicável) |

**Status:** `—` pendente · `◐` em andamento · `✓` concluído

---

## Resumo

| Status | Qtd |
|--------|----:|
| Concluído (doc + empírico) | 0 |
| Em andamento | 1 |
| Pendente | 41 |
| **Total** | **42** |

---

## Abastecimento, distribuição e mercado downstream

Prioridade alinhada ao foco de combustíveis do monorepo.

| # | Slug | Conjunto | Doc | Raw | Emp. | Fuel | Int. |
|---|------|----------|:---:|:---:|:----:|:----:|:----:|
| 41 | `tancagem-abastecimento` | Tancagem do Abastecimento Nacional | ◐ | ◐ | ◐ | ◐ | — |
| 21 | `movimentacao-derivados` | Movimentação de derivados, GLP e biocombustíveis | ✓ | — | — | — | — |
| 12 | `cadastro-revendas-combustiveis` | Cadastro revendedores varejistas (postos) | ✓ | — | — | — | — |
| 11 | `cadastro-revendas-glp` | Cadastro revendas GLP | ✓ | — | — | — | — |
| 27 | `pontos-abastecimento` | Pontos de Abastecimento Autorizados | ✓ | — | — | — | — |
| 15 | `distribuidores-combustiveis-liquidos` | Distribuidores de combustíveis líquidos | ✓ | — | — | — | — |
| 28 | `pmqc` | PMQC — Qualidade dos Combustíveis | ✓ | — | — | — | — |
| 29 | `pml` | PML — Monitoramento dos Lubrificantes | ✓ | — | — | — | — |
| 40 | `serie-historica-precos` | Série Histórica de Preços de Combustíveis | ✓ | — | — | — | — |
| 42 | `vendas-derivados` | Vendas de derivados e biocombustíveis | ✓ | — | — | — | — |
| 2 | `fiscalizacao-abastecimento` | Ações de Fiscalização do Abastecimento | ✓ | — | — | — | — |
| 9 | `capacidade-armazenagem-terminais` | Capacidade de Armazenagem de Terminais | ✓ | — | — | — | — |
| 22 | `movimentacao-terminais-aquaviarios` | Movimentação Terminais Aquaviários | ✓ | — | — | — | — |
| 37 | `registro-lubrificantes` | Registro de Óleos e Graxas Lubrificantes | ✓ | — | — | — | — |

---

## Produção, refino e biocombustíveis

| # | Slug | Conjunto | Doc | Raw | Emp. | Fuel | Int. |
|---|------|----------|:---:|:---:|:----:|:----:|:----:|
| 32 | `processamento-petroleo-derivados` | Processamento de petróleo e produção de derivados | ✓ | — | — | — | — |
| 33 | `producao-biocombustiveis` | Produção de biocombustíveis | ✓ | — | — | — | — |
| 34 | `producao-por-estado` | Produção por estado e localização | ✓ | — | — | — | — |
| 35 | `producao-por-poco` | Produção por Poço | ✓ | — | — | — | — |
| 19 | `importacoes-exportacoes` | Importações e exportações | ✓ | — | — | — | — |
| 5 | `anuario-estatistico` | Anuário Estatístico | ✓ | — | — | — | — |

---

## Exploração e produção (E&P)

| # | Slug | Conjunto | Doc | Raw | Emp. | Fuel | Int. |
|---|------|----------|:---:|:---:|:----:|:----:|:----:|
| 13 | `dados-ep` | Dados de E&P | — | — | — | — | — |
| 16 | `fase-exploracao` | Fase de Exploração | — | — | — | — | — |
| 17 | `fase-desenvolvimento-producao` | Fase de Desenvolvimento e Produção | — | — | — | — | — |
| 8 | `blocos-fase-exploratoria-encerrada` | Blocos com Fase Exploratória Encerrada | — | — | — | — | — |
| 20 | `incidentes-ep` | Incidentes de E&P | — | — | — | — | — |
| 38 | `resultado-poco` | Resultado de poço | — | — | — | — | — |
| 31 | `previsao-atividades-investimentos` | Previsão de Atividades e Investimentos Exploratórios | — | — | — | — | — |
| 36 | `relacao-concessionarios` | Relação de Concessionários | — | — | — | — | — |
| 39 | `rodadas-licitacoes` | Rodadas de Licitações | — | — | — | — | — |

---

## Gás natural

| # | Slug | Conjunto | Doc | Raw | Emp. | Fuel | Int. |
|---|------|----------|:---:|:---:|:----:|:----:|:----:|
| 7 | `autorizacoes-gas-natural` | Autorizações de gás natural | — | — | — | — | — |
| 10 | `comercializacao-gas-natural` | Comercialização de Gás Natural | — | — | — | — | — |
| 23 | `movimentacao-gas-gasodutos` | Movimentação em gasodutos de transporte | — | — | — | — | — |

---

## Acervo técnico e geociências

| # | Slug | Conjunto | Doc | Raw | Emp. | Fuel | Int. |
|---|------|----------|:---:|:---:|:----:|:----:|:----:|
| 1 | `acervo-dados-tecnicos` | Acervo de Dados Técnicos | — | — | — | — | — |
| 4 | `amostras-rochas-fluidos` | Amostras de Rochas e Fluidos | — | — | — | — | — |
| 6 | `aquisicao-processamento-estudo-dados` | Aquisição, Processamento e Estudo de Dados | — | — | — | — | — |
| 14 | `bacias-sedimentares` | Bacias Sedimentares Brasileiras | — | — | — | — | — |

---

## Regulação, fiscalização e participações

| # | Slug | Conjunto | Doc | Raw | Emp. | Fuel | Int. |
|---|------|----------|:---:|:---:|:----:|:----:|:----:|
| 3 | `aditamento-conteudo-local` | Aditamento de conteúdo local | — | — | — | — | — |
| 18 | `fiscalizacao-conteudo-local` | Fiscalização de Conteúdo Local | — | — | — | — | — |
| 24 | `multas-2016` | Multas (vencimento a partir de 2016) | — | — | — | — | — |
| 25 | `participacoes-governamentais` | Participações Governamentais | — | — | — | — | — |
| 26 | `pesquisa-desenvolvimento-inovacao` | Pesquisa, Desenvolvimento e Inovação | — | — | — | — | — |
| 30 | `prestadores-apoio-administrativo` | Prestadores de apoio administrativo | — | — | — | — | — |

---

## Em andamento — detalhe

### 41 · `tancagem-abastecimento`

- [x] Doc atlas — [docs/conjuntos/tancagem-abastecimento.md](docs/conjuntos/tancagem-abastecimento.md)
- [x] Matriz de URLs e metadados oficiais
- [x] Inventário empírico (36 CSVs, mai/2026)
- [x] Qualidade/chaves e anomalias (parcial)
- [x] Fuel-analytics — pipeline raw/trusted/refined + notebooks
- [ ] Fechar investigação nov/dez 2022
- [ ] Integração histórica no atlas (`pipelines/`)

---

## Como marcar progresso

1. Ao criar `docs/conjuntos/{slug}.md`, marcar **Doc** como `◐` e depois `✓`.
2. Após download local, marcar **Raw**; após tabela de arquivos medidos, **Emp.**
3. Ao abrir estudo no fuel-analytics, marcar **Fuel** (link no doc do conjunto).
4. Quando a série consolidada estiver documentada no atlas, marcar **Int.**
5. Atualizar coluna **Explorado** em [dados-abertos.md](docs/dados-abertos.md) quando **Doc** = `✓`.

**Ordem sugerida (combustíveis):** tancagem → movimentação derivados → cadastro revendas → PMQC → preços → vendas.
