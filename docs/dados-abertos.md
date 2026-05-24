# Dados abertos da ANP

Catálogo da página oficial de dados abertos da ANP. Serve como índice para explorações futuras em `docs/` e downloads locais em `data/raw/`.

**Fonte:** [Dados abertos — ANP](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos)  
**Última atualização no portal:** 20/05/2026 (página publicada em 26/10/2020)

A ANP disponibiliza dados em formato aberto para transparência — visualização, estudo e reutilização por cidadãos, academia, imprensa e agentes econômicos. Os conjuntos também podem ser consultados no [Portal Brasileiro de Dados Abertos](https://dados.gov.br/).

## Página e documentos relacionados

A [página de Dados abertos](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos) lista os conjuntos abaixo e aponta para os documentos de governança. Cada item tem URL própria (não confundir a página índice com o PDF do plano, por exemplo).

| Documento | Arquivo | Observação |
|-----------|---------|------------|
| Página de Dados abertos | [dados-abertos](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos) | Índice dos 42 conjuntos |
| Plano de Dados Abertos da ANP 2024-2026 | [pda-2024-2026.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/pda-2024-2026.pdf) | Política e metas de abertura |
| Inventário de Dados | [inventario-dados.xlsx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/inventario-dados.xlsx) | Atualizado em 5/12/2025 · [análise local](inventario-dados.md) · [extração 2026-05-24](../data/catalogo-anp/inventario-dados/2026-05-24/) |
| Execução Orçamentária e Contratos Administrativos | [nota-explicativa-exclusao-bases-dados-abertos-anp.docx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/nota-explicativa-exclusao-bases-dados-abertos-anp.docx) | Nota sobre exclusão de bases dos dados abertos |

### Relatórios Anuais de Dados Abertos

| Ano | PDF |
|-----|-----|
| 2020 | [relatorio_2020.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/relatorio_anual_de_atividades_dados_abertos_2020.pdf) |
| 2021 | [relatorio_2021.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/relatorio_anual_de_atividades_dados_abertos_2021.pdf) |
| 2022 | [relatorio_2022.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/relatorio_anual_de_atividades_dados_abertos_2022.pdf) |
| 2023 | [relatorio_2023.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/relatorio_anual_de_atividades_dados_abertos_2023.pdf) |
| 2024 | [relatorio_2024.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/relatorio_anual_de_atividades_dados_abertos_2024.pdf) |
| 2025 | [relatorio_2025.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/relatorio_anual_de_atividades_dados_abertos_2025.pdf) |

## Legislação (Saiba mais)

- [Decreto nº 8.777/2016](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/D8777.htm) — Política de Dados Abertos
- Portaria nº 8.542/2016
- Portaria nº 8.927/2017

## Conjuntos disponíveis em formato aberto

Cada linha corresponde a um conjunto listado na página oficial. O **slug** sugere pasta em `data/raw/{slug}/` e arquivo de exploração em `docs/conjuntos/{slug}.md` (a criar conforme for analisando).

| # | Conjunto | Slug | Explorado |
|---|----------|------|-----------|
| 1 | Acervo de Dados Técnicos | `acervo-dados-tecnicos` | |
| 2 | Ações de Fiscalização do Abastecimento | `fiscalizacao-abastecimento` | [doc](conjuntos/fiscalizacao-abastecimento.md) |
| 3 | Aditamento de conteúdo local | `aditamento-conteudo-local` | |
| 4 | Amostras de Rochas e Fluidos | `amostras-rochas-fluidos` | |
| 5 | Anuário Estatístico | `anuario-estatistico` | |
| 6 | Aquisição, Processamento e Estudo de Dados | `aquisicao-processamento-estudo-dados` | |
| 7 | Autorizações de gás natural | `autorizacoes-gas-natural` | |
| 8 | Blocos com Fase Exploratória Encerrada | `blocos-fase-exploratoria-encerrada` | |
| 9 | Capacidade de Armazenagem de Terminais | `capacidade-armazenagem-terminais` | [doc](conjuntos/capacidade-armazenagem-terminais.md) |
| 10 | Comercialização de Gás Natural | `comercializacao-gas-natural` | |
| 11 | Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo (GLP) | `cadastro-revendas-glp` | [doc](conjuntos/cadastro-revendas-glp.md) |
| 12 | Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos | `cadastro-revendas-combustiveis` | [doc](conjuntos/cadastro-revendas-combustiveis.md) |
| 13 | Dados de E&P | `dados-ep` | |
| 14 | Dados Georreferenciados das Bacias Sedimentares Brasileiras | `bacias-sedimentares` | |
| 15 | Distribuidores de combustíveis líquidos | `distribuidores-combustiveis-liquidos` | [doc](conjuntos/distribuidores-combustiveis-liquidos.md) |
| 16 | Fase de Exploração | `fase-exploracao` | |
| 17 | Fase de Desenvolvimento e Produção | `fase-desenvolvimento-producao` | |
| 18 | Fiscalização de Conteúdo Local | `fiscalizacao-conteudo-local` | |
| 19 | Importações e exportações | `importacoes-exportacoes` | |
| 20 | Incidentes de Exploração e Produção de Petróleo e Gás Natural | `incidentes-ep` | |
| 21 | Movimentação de derivados de petróleo e gás natural e biocombustíveis | `movimentacao-derivados` | [doc](conjuntos/movimentacao-derivados.md) |
| 22 | Movimentação dos Terminais Aquaviários | `movimentacao-terminais-aquaviarios` | [doc](conjuntos/movimentacao-terminais-aquaviarios.md) |
| 23 | Movimentação de Gás Natural em Gasodutos de Transporte | `movimentacao-gas-gasodutos` | |
| 24 | Multas aplicadas com vencimento a partir de 2016 | `multas-2016` | |
| 25 | Participações Governamentais | `participacoes-governamentais` | |
| 26 | Pesquisa, Desenvolvimento e Inovação | `pesquisa-desenvolvimento-inovacao` | |
| 27 | Pontos de Abastecimento Autorizados | `pontos-abastecimento` | [doc](conjuntos/pontos-abastecimento.md) |
| 28 | Programa de Monitoramento da Qualidade dos Combustíveis (PMQC) | `pmqc` | [doc](conjuntos/pmqc.md) |
| 29 | Programa de Monitoramento dos Lubrificantes (PML) | `pml` | [doc](conjuntos/pml.md) |
| 30 | Prestadores de serviço de apoio administrativo | `prestadores-apoio-administrativo` | |
| 31 | Previsão de Atividades e Investimentos Exploratórios | `previsao-atividades-investimentos` | |
| 32 | Processamento de petróleo e produção de derivados | `processamento-petroleo-derivados` | |
| 33 | Produção de biocombustíveis | `producao-biocombustiveis` | |
| 34 | Produção de petróleo e gás natural por estado e localização | `producao-por-estado` | |
| 35 | Produção de Petróleo e Gás Natural por Poço | `producao-por-poco` | |
| 36 | Relação de Concessionários | `relacao-concessionarios` | |
| 37 | Registro de Óleos e Graxas Lubrificantes | `registro-lubrificantes` | |
| 38 | Resultado de poço | `resultado-poco` | |
| 39 | Rodadas de Licitações de Petróleo e Gás Natural | `rodadas-licitacoes` | |
| 40 | Série Histórica de Preços de Combustíveis | `serie-historica-precos` | [doc](conjuntos/serie-historica-precos.md) |
| 41 | Tancagem do Abastecimento Nacional de Combustíveis | `tancagem-abastecimento` | [sim](conjuntos/tancagem-abastecimento.md) |
| 42 | Vendas de derivados de petróleo e biocombustíveis | `vendas-derivados` | [doc](conjuntos/vendas-derivados.md) |

### Notas do portal (resumo)

- **Anuário Estatístico** — consolida desempenho da indústria de petróleo, gás e biocombustíveis e do abastecimento nos últimos dez anos; tabelas em CSV.
- **Movimentação de derivados** — combustíveis líquidos, GLP e lubrificantes.
- **Série histórica de preços** — no menu do site também aparece como “Preços de Combustíveis e de GLP”.
- **Multas** — autuações em ações de fiscalização com vencimento a partir de 2016.

## Próximos passos neste atlas

1. Escolher um conjunto da tabela e abrir a subpágina no portal da ANP.
2. Baixar amostras para `data/raw/{slug}/`.
3. Registrar metadados, formatos, periodicidade e dicionário em `docs/conjuntos/{slug}.md`.
4. Marcar a coluna **Explorado** neste arquivo quando a exploração estiver documentada.
5. Acompanhar progresso detalhado em [TODO.md](../TODO.md) (42 conjuntos, etapas doc/raw/fuel).
