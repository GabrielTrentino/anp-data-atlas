# anp-data-atlas

Atlas de referência dos dados abertos da ANP: documentação em Markdown e **integração histórica** dos conjuntos (série consolidada no tempo).

## Objetivo

Este repositório é uma **referência exploratória** dos dados publicados pela [Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)](https://www.gov.br/anp/pt-br). Ele reúne:

- **Documentação** em Markdown — metadados, contexto, dicionário de colunas, matriz de arquivos e lacunas;
- **Pipelines de integração** — baixar brutos, harmonizar meses/blocos e produzir série histórica utilizável (`data/raw/` → processamento documentado);
- **Descobertas** incorporadas a partir de explorações no [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics) (notebooks exploratórios).

| Repositório | Papel |
|-------------|--------|
| **anp-data-atlas** | Referência + **integração histórica** por assunto |
| [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics) | **Análises exploratórias** (perfil, qualidade, pilotos) que validam o que entra no atlas |

A ideia é servir de base para outros projetos — quem for construir análises, dashboards ou modelos pode consultar este atlas antes de reimplementar explorações do zero.

## O que cada conjunto traz

Síntese dos **42 conjuntos** da [página de dados abertos](docs/dados-abertos.md). Cada linha traz uma descrição do que o dataset representa e as variáveis-chave para cruzamento. Índice completo: **[docs/variaveis-conjuntos.md](docs/variaveis-conjuntos.md)** (✓ = confirmado empiricamente · ~ = inferido do portal).

### Abastecimento, distribuição e mercado downstream

| # | Slug | Descrição | Variáveis-chave | Liga com |
|---|------|-----------|-----------------|----------|
| 41 | [`tancagem-abastecimento`](docs/conjuntos/tancagem-abastecimento.md) | **Capacidade de armazenamento autorizada** (m³) por instalação registrada no SIMP. Uma linha por instalação × unidade (`Tag`) × grupo de produto, publicada mensalmente. Não é estoque físico. | `Data`, `Cnpj`, `CodInstalacao`, `Uf`, `Municipio`, `GrupoDeProdutos`, `TancagemM3` ✓ | movimentação, cadastros, preços |
| 21 | [`movimentacao-derivados`](docs/conjuntos/movimentacao-derivados.md) | **Fluxo de derivados e biocombustíveis entre agentes** (distribuidores, TRR, terminais), em mil m³, com UF de origem e destino. Permite traçar rotas de distribuição e volumes por produto. | `Ano`, `Mês`, `Agente Regulado`, `Código do Produto`, UF origem/destino ✓ | tancagem, vendas, cadastros |
| 12 | [`cadastro-revendas-combustiveis`](docs/conjuntos/cadastro-revendas-combustiveis.md) | **Registro de postos e revendedores varejistas** de combustíveis autorizados pela ANP — CNPJ, endereço, bandeira, segmento e situação cadastral. Base de referência para cruzar fiscalização e preços. | `Cnpj`, `Uf`, `Municipio`, `Bandeira`, `Situacao` ~ | tancagem, preços, movimentação |
| 11 | [`cadastro-revendas-glp`](docs/conjuntos/cadastro-revendas-glp.md) | **Cadastro de revendas de GLP** (botijão/granel), com CNPJ, endereço, modalidade de revenda e situação. Versão específica para o mercado de gás liquefeito. | `Cnpj`, `Uf`, `Municipio`, modalidade ~ | movimentação GLP, tancagem |
| 27 | [`pontos-abastecimento`](docs/conjuntos/pontos-abastecimento.md) | **Instalações autorizadas** a abastecer aeronaves, embarcações e veículos especiais — aeroportos, portos, frotas. Diferente do cadastro de postos varejistas comuns. | `CodInstalacao`, `Cnpj`, `Uf`, `Municipio` ~ | cadastros, fiscalização |
| 15 | [`distribuidores-combustiveis-liquidos`](docs/conjuntos/distribuidores-combustiveis-liquidos.md) | **Lista de distribuidores atacadistas** autorizados (combustíveis líquidos), com CNPJ, UF de atuação e status do contrato. Nível atacado — acima dos postos. | `Cnpj`, `Uf`, contratos ~ | movimentação, terminais |
| 28 | [`pmqc`](docs/conjuntos/pmqc.md) | **Resultados do Programa de Monitoramento da Qualidade dos Combustíveis** — amostras colhidas nos postos, parâmetros analisados e conformidade (aprovado/reprovado). | `Periodo`, `Produto`, `Uf`, conformidade ~ | fiscalização, cadastros |
| 29 | [`pml`](docs/conjuntos/pml.md) | **Resultados do Programa de Monitoramento de Lubrificantes** — análises laboratoriais de óleos e graxas no mercado, por produto, parâmetro e região. | produto, parâmetros, região ~ | registro lubrificantes, movimentação |
| 40 | [`serie-historica-precos`](docs/conjuntos/serie-historica-precos.md) | **Preços médios de venda ao consumidor** (R$/litro ou R$/kg) de combustíveis nos postos, levantados semanalmente pela ANP desde 2001. Inclui preço de compra do revendedor e margem. | `Produto`, `Uf`, `Municipio`, semana, `PrecoMedio` ✓ | vendas, cadastros, tancagem |
| 42 | [`vendas-derivados`](docs/conjuntos/vendas-derivados.md) | **Volume de combustíveis vendidos** por distribuidores ao mercado final (m³), por produto, UF, município e segmento de consumidor (automotivo, industrial, etc.). | `Periodo`, `Produto`, `Uf`, `Municipio`, `Segmento` ~ | movimentação, importações |
| 2 | [`fiscalizacao-abastecimento`](docs/conjuntos/fiscalizacao-abastecimento.md) | **Registro de ações de fiscalização** do setor de abastecimento (postos, distribuidores) — data, agente fiscalizado, UF, resultado e tipo de infração detectada. | `DataAcao`, `Cnpj`, `Uf`, `Segmento`, resultado ~ | PMQC, cadastros |
| 9 | [`capacidade-armazenagem-terminais`](docs/conjuntos/capacidade-armazenagem-terminais.md) | **Capacidade de armazenamento dos terminais primários** (portuários e dutoviários), em m³, por produto e tipo de tanque. Complementa a tancagem do SIMP (inclui terminais de petróleo). | `Terminal`, `Cnpj`, `Uf`, m³ ~ | tancagem, mov. aquaviária |
| 22 | [`movimentacao-terminais-aquaviarios`](docs/conjuntos/movimentacao-terminais-aquaviarios.md) | **Volumes movimentados nos terminais aquaviários** (embarque/desembarque de petróleo e derivados), por terminal, produto e período. Foco no modal marítimo/fluvial. | `Terminal`, `Periodo`, `Produto` ~ | capacidade terminais |
| 37 | [`registro-lubrificantes`](docs/conjuntos/registro-lubrificantes.md) | **Catálogo dos lubrificantes registrados** na ANP — nome comercial, fabricante/importador, classe SAE, tipo e registro ANP. Base de referência para o PML. | registro ANP, classe, fabricante ~ | PML, movimentação |

### Produção, refino, comércio exterior e estatística consolidada

| # | Slug | Descrição | Variáveis-chave | Liga com |
|---|------|-----------|-----------------|----------|
| 32 | [`processamento-petroleo-derivados`](docs/conjuntos/processamento-petroleo-derivados.md) | **Volumes processados e produzidos nas refinarias** (petróleo → derivados), por refinaria, produto e período. Permite ver eficiência de refino e mix de derivados por planta. | refinaria, `Produto`, `Periodo` ~ | vendas, importações |
| 33 | [`producao-biocombustiveis`](docs/conjuntos/producao-biocombustiveis.md) | **Produção mensal de biocombustíveis** (etanol, biodiesel, biogás, etc.) por usina, UF e produto. Essencial para análise de mandatos de mistura e sazonalidade do etanol. | `Produto`, `Uf`, volume, mês ~ | vendas, preços etanol |
| 34 | [`producao-por-estado`](docs/conjuntos/producao-por-estado.md) | **Produção mensal de petróleo e gás natural agregada por UF**, com abertura por localização (terra/mar) e tipo de fluido. Série desde 2000. | `Uf`, terra/mar, petróleo/gás, mês ~ | anuário, importações |
| 35 | [`producao-por-poco`](docs/conjuntos/producao-por-poco.md) | **Produção mensal de petróleo, gás e água por poço individual** — o menor nível de granularidade disponível. Permite rastrear declínio de poços e campos. | `CodigoPoco`, `Campo`, volumes, mês ~ | produção por estado |
| 19 | [`importacoes-exportacoes`](docs/conjuntos/importacoes-exportacoes.md) | **Fluxo de comércio exterior** de petróleo, derivados e gás — volumes importados e exportados por produto, país de origem/destino e mês. | `Produto`, `Pais`, mês ~ | vendas, refino |
| 5 | [`anuario-estatistico`](docs/conjuntos/anuario-estatistico.md) | **Anuário Estatístico da ANP** — coletânea anual com dezenas de tabelas sobre toda a cadeia (E&P, refino, distribuição, preços). Referência para benchmark de séries mensais. | `Ano`, `Produto`, `Volume`, `Uf` (varia) ~ | benchmark de séries mensais |

### Exploração e produção (E&P)

| # | Slug | Descrição | Variáveis-chave | Liga com |
|---|------|-----------|-----------------|----------|
| 13 | [`dados-ep`](docs/conjuntos/dados-ep.md) | **Painel consolidado de E&P** — agregados por bloco, campo e operador (fase exploratória, produção, devolução). Porta de entrada para o universo de contratos de E&P. | `Bloco`, operador, fase ~ | fases, produção |
| 16 | [`fase-exploracao`](docs/conjuntos/fase-exploracao.md) | **Status dos blocos em fase exploratória** — quem é o concessionário, qual a bacia, prazo de exploração e cumprimento do programa mínimo de trabalho. | `Bloco`, `Bacia`, concessionário ~ | rodadas, produção |
| 17 | [`fase-desenvolvimento-producao`](docs/conjuntos/fase-desenvolvimento-producao.md) | **Campos em fase de desenvolvimento e produção** — campos declarados comerciais, operadores, campos unitizados e status de aprovação dos planos de desenvolvimento. | `Campo`, `Bloco`, operador ~ | produção por poço |
| 8 | [`blocos-fase-exploratoria-encerrada`](docs/conjuntos/blocos-fase-exploratoria-encerrada.md) | **Histórico de blocos que tiveram a fase exploratória encerrada** (devolvidos ou convertidos) — data de encerramento, bacia e motivo. Útil para análise de portfólio histórico. | `Bloco`, data encerramento ~ | rodadas |
| 20 | [`incidentes-ep`](docs/conjuntos/incidentes-ep.md) | **Registro de incidentes de segurança operacional em E&P** (vazamentos, fogo, lesões) — data, campo, tipo de incidente, severidade e consequências. | `Data`, campo, tipo, feridos ~ | produção |
| 38 | [`resultado-poco`](docs/conjuntos/resultado-poco.md) | **Resultado técnico de cada poço perfurado** — se encontrou petróleo/gás, se foi produtor, seco ou abandonado. Complementa a produção por poço com o histórico de perfuração. | `CodigoPoco`, `Campo`, `Bacia` ~ | produção por poço, acervo |
| 31 | [`previsao-atividades-investimentos`](docs/conjuntos/previsao-atividades-investimentos.md) | **Previsão declarada de atividades exploratórias e investimentos** pelos concessionários — perfurações previstas, levantamentos sísmicos e valores por bloco e ano. | `Bloco`, investimento, ano ~ | rodadas |
| 36 | [`relacao-concessionarios`](docs/conjuntos/relacao-concessionarios.md) | **Cadastro dos concessionários** de E&P registrados na ANP — CNPJ, razão social, participações em blocos e campos e status dos contratos. | `Bloco`, `Cnpj`, contrato ~ | rodadas, produção |
| 39 | [`rodadas-licitacoes`](docs/conjuntos/rodadas-licitacoes.md) | **Resultados das rodadas de licitação de blocos** exploratórios — bloco ofertado, empresa vencedora, bônus de assinatura, conteúdo local proposto e data de assinatura. | `Rodada`, `Bloco`, vencedor ~ | concessionários |

### Gás natural

| # | Slug | Descrição | Variáveis-chave | Liga com |
|---|------|-----------|-----------------|----------|
| 7 | [`autorizacoes-gas-natural`](docs/conjuntos/autorizacoes-gas-natural.md) | **Autorizações concedidas pela ANP** para atividades com gás natural (importação, exportação, produção independente, comercialização) — CNPJ, atividade e UF. | `Cnpj`, atividade, `Uf` ~ | comercialização, gasodutos |
| 10 | [`comercializacao-gas-natural`](docs/conjuntos/comercializacao-gas-natural.md) | **Contratos e volumes de compra e venda de gás natural** entre agentes — vendedor, comprador, volume contratado e realizado, por mês. Retrata o mercado atacadista de gás. | vendedor/comprador, volume, mês ~ | gasodutos |
| 23 | [`movimentacao-gas-gasodutos`](docs/conjuntos/movimentacao-gas-gasodutos.md) | **Volumes transportados nos gasodutos de transporte**, por ponto de entrada/saída e mês. Permite mapear fluxos físicos na malha de gás canalizado. | `Gasoduto`, pontos, mês ~ | comercialização |

### Acervo técnico e geociências

| # | Slug | Descrição | Variáveis-chave | Liga com |
|---|------|-----------|-----------------|----------|
| 1 | [`acervo-dados-tecnicos`](docs/conjuntos/acervo-dados-tecnicos.md) | **Catálogo do acervo técnico da ANP** — inventário de poços perfurados, levantamentos sísmicos e outros dados geológicos custodiados. Base para solicitar acesso a dados de subsuperfície. | `CodigoPoco`, tipo, coords ~ | resultado poço, bacias |
| 4 | [`amostras-rochas-fluidos`](docs/conjuntos/amostras-rochas-fluidos.md) | **Registro de amostras de rochas e fluidos** coletadas em poços — tipo de amostra, profundidade, status de custódia e localização no acervo físico da ANP. | `CodigoPoco`, código amostra ~ | acervo |
| 6 | [`aquisicao-processamento-estudo-dados`](docs/conjuntos/aquisicao-processamento-estudo-dados.md) | **Levantamentos sísmicos e estudos geológicos** autorizados — bacia, operador, área, tipo de aquisição (2D/3D/PSTM) e status. | `Bacia`, survey, área ~ | bacias, acervo |
| 14 | [`bacias-sedimentares`](docs/conjuntos/bacias-sedimentares.md) | **Geometria georreferenciada das bacias sedimentares brasileiras** (polígonos SHP/CSV) — base cartográfica para qualquer análise espacial de E&P. | `Bacia`, polígonos ~ | blocos, E&P |

### Regulação, fiscalização e participações

| # | Slug | Descrição | Variáveis-chave | Liga com |
|---|------|-----------|-----------------|----------|
| 3 | [`aditamento-conteudo-local`](docs/conjuntos/aditamento-conteudo-local.md) | **Aditamentos aos contratos de conteúdo local** em E&P — alterações nos compromissos de conteúdo local negociados entre concessionários e ANP (dispensa, repactuação, etc.). | contrato, `Bloco`, % local ~ | fiscalização conteúdo local |
| 18 | [`fiscalizacao-conteudo-local`](docs/conjuntos/fiscalizacao-conteudo-local.md) | **Resultado da fiscalização de conteúdo local** nos contratos de E&P — meta comprometida vs. realizado por fase (exploração, desenvolvimento, produção) e bloco. | `Bloco`, meta/realizado ~ | aditamentos, rodadas |
| 24 | [`multas-2016`](docs/conjuntos/multas-2016.md) | **Multas aplicadas pela ANP** com vencimento a partir de 2016 — processo, CNPJ autuado, valor original, status de pagamento e segmento infrator. | processo, `Cnpj`, valor ~ | fiscalização |
| 25 | [`participacoes-governamentais`](docs/conjuntos/participacoes-governamentais.md) | **Participações governamentais** pagas pelos concessionários (royalties, participação especial, bônus de retenção) — por campo, competência e preço de referência utilizado. | `Campo`, preço referência ~ | produção E&P |
| 26 | [`pesquisa-desenvolvimento-inovacao`](docs/conjuntos/pesquisa-desenvolvimento-inovacao.md) | **Investimentos em P&D e inovação** realizados pelos concessionários como obrigação contratual — CNPJ, projeto, instituição receptora e valor por ano. | `Cnpj`, projeto, investimento ~ | — |
| 30 | [`prestadores-apoio-administrativo`](docs/conjuntos/prestadores-apoio-administrativo.md) | **Empresas prestadoras de serviços de apoio administrativo** autorizadas pela ANP para atuar em E&P — CNPJ, tipo de serviço e status da autorização. | `Cnpj`, tipo serviço ~ | — |

Catálogo completo: [docs/dados-abertos.md](docs/dados-abertos.md) · variáveis e chaves: [docs/variaveis-conjuntos.md](docs/variaveis-conjuntos.md) · progresso: [TODO.md](TODO.md) · inventário (240 bases): [docs/inventario-dados.md](docs/inventario-dados.md).

## O que cada repositório guarda

Divisão de responsabilidades entre este atlas e o [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics):

| Conteúdo | **anp-data-atlas** (este repo) | **anp-fuel-analytics** |
|----------|-------------------------------|-------------------------|
| Metadados oficiais ANP | Sim — `docs/conjuntos/` | Link para o atlas |
| Matriz de URLs e lacunas do portal | Sim | Usa o atlas como referência |
| Inventário empírico dos brutos (linhas, m³, `Data` por arquivo) | Sim — quando estabilizado | Notebooks geram e validam |
| Schema confirmado na prática | Sim — resumo em Markdown | Código + tabelas completas |
| Chave candidata, regras de agregação | Sim | Prova nos notebooks |
| Anomalias documentadas (ex.: nov/dez 2022) | Sim — seção de qualidade | Investigação ativa (`TODO.md`) |
| Gráficos, `describe()`, experimentos | Não | Sim — notebooks |
| Camadas trusted / refined | Não | Sim — pipelines na raiz |
| Pipelines de integração histórica | Sim — `pipelines/` (planejado) | Protótipos por estudo |

**Promover para o atlas** quando a informação for reproduzível, útil para integração (ETL, chaves, lacunas) e relativamente estável. **Manter no fuel-analytics** gráficos exploratórios, comparações analíticas e hipóteses ainda em aberto.

No atlas, cada conjunto tem um `.md` em `docs/conjuntos/` com seções como: estrutura oficial, inventário empírico, qualidade/chaves e link para a exploração ativa nos notebooks — sem duplicar o notebook inteiro.

## Fluxo de processamento

Visão geral de como os dados circulam entre portal, repositórios e documentação:

```mermaid
flowchart TB
  ANP[Portal ANP — CSV/PDF]
  Raw[data/raw no atlas ou fuel]
  Docs[docs/conjuntos — referência]
  FuelExplore[anp-fuel-analytics — notebooks]
  FuelETL[anp-fuel-analytics — trusted/refined]
  AtlasETL[anp-data-atlas — integração histórica]
  Promote[Promover findings estáveis]

  ANP --> Raw
  Raw --> Docs
  Raw --> FuelExplore
  FuelExplore --> Promote
  Promote --> Docs
  Raw --> FuelETL
  FuelETL -.->|regras documentadas| Docs
  Raw --> AtlasETL
  AtlasETL --> Docs
```

| Etapa | Onde | O que acontece |
|-------|------|----------------|
| 1. Fonte | Portal ANP | Publicação mensal ou em blocos; metadados em PDF |
| 2. Raw local | `data/raw/{slug}/` | Cópia fiel dos arquivos (não versionada no Git) |
| 3. Exploração | [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics) | Perfil, qualidade, inventário por arquivo nos notebooks |
| 4. Documentação | `docs/conjuntos/{slug}.md` | Metadados oficiais + inventário empírico + regras de integração |
| 5. Integração histórica | `pipelines/` (atlas, planejado) | Harmonizar lacunas/blocos e série consolidada documentada |
| 6. Camadas analíticas | fuel-analytics (`trusted` / `refined`) | Protótipos ETL; regras estáveis voltam para o atlas |

Neste repositório, o foco do processamento é **documentar** o caminho raw → série utilizável. A implementação pesada de trusted/refined fica no fuel-analytics até a integração histórica do atlas estar madura.

## O que promover para o atlas (e o que não)

### Promover (sim)

| Tipo | Exemplo | Onde no atlas |
|------|---------|---------------|
| Schema confirmado em amostras reais | `Cnpj` como texto; 12 colunas de negócio | Estrutura dos arquivos |
| Domínios categóricos estáveis | 4 valores de `GrupoDeProdutos` | Estrutura / qualidade |
| Chave lógica validada | `Data` + `CodInstalacao` + `Tag` + `GrupoDeProdutos` sem duplicatas | Qualidade e chaves |
| Inventário por arquivo baixado | linhas, soma m³, faixa de `Data` | Inventário empírico |
| Lacunas e blocos do portal | abr/2025 ausente; `marco-julho.csv` | Matriz / periodicidade |
| Anomalia confirmada | queda nov/dez 2022 com evidência | Anomalias conhecidas |
| Regra de agregação | somar `TancagemM3` no nível da chave; não duplicar `Tag` | Qualidade e chaves |
| Decisão de ETL | descartar linhas 100% nulas na trusted | Qualidade (quando validado) |

### Não promover (ficar no fuel-analytics)

| Tipo | Exemplo | Onde ficar |
|------|---------|------------|
| Outputs de célula | `df.describe()`, tabelas gigantes | Notebook |
| Gráficos exploratórios | ranking UF, GO vs SP | Notebook |
| Hipótese em aberto | “será corte parcial em 2022?” | `TODO.md` do estudo |
| Código de pipeline | SQL DuckDB, `run.py` | `pipelines/` |
| Análise de negócio | HHI, participação de mercado | Notebook ou projeto derivado |
| Números de uma execução só | contagem exata sem data de referência | Reexecutar e documentar com snapshot |

### Critérios (checklist)

Promova quando **todas** forem verdadeiras:

1. **Reproduzível** — outra pessoa com os mesmos CSVs deve chegar à mesma conclusão.
2. **Útil para integração** — ajuda ETL, chaves, harmonização temporal ou leitura do dicionário.
3. **Estável** — não depende de um notebook em edição; vale após revisão.
4. **Referenciável** — indique fonte (arquivo, notebook, data da medição).

Se falhar em (3) ou (4), mantenha no fuel-analytics até fechar a investigação.

## Estrutura prevista

```
anp-data-atlas/
├── docs/
│   ├── dados-abertos.md        # Catálogo oficial (42 conjuntos)
│   ├── inventario-dados.md     # Análise do inventário institucional (240 bases)
│   └── conjuntos/              # Exploração por conjunto
├── data/
│   ├── catalogo-anp/           # Documentos ANP versionados por data de extração
│   │   └── inventario-dados/{AAAA-MM-DD}/
│   └── raw/{slug}/             # Dados brutos por conjunto (não versionados)
└── pipelines/                  # Integração histórica (planejado)
```

Os arquivos em `data/raw/` ficam no `.gitignore`. O **inventário institucional** (`data/catalogo-anp/`) e a documentação em `docs/` são versionados.

## Dados brutos

Mantemos somente a camada **raw** — arquivos originais da fonte, sem alteração estrutural — para inspecionar metadados, entender o contexto de cada conjunto e registrar as descobertas em `docs/`. Tratamentos e camadas derivadas ficam fora deste repositório, em projetos que consumirem este atlas.

## Fonte dos dados

Os dados brutos são **dados abertos da ANP**. A reutilização segue os termos e políticas definidos pela agência e pelo governo federal — este repositório **não relicencia** o conteúdo original da ANP, apenas documenta e armazena localmente para exploração.

Ao publicar análises ou derivados, cite a fonte oficial da ANP e consulte as condições vigentes no portal de dados abertos.

## Licenciamento

| Conteúdo | Licença |
|----------|---------|
| Código, pipelines e documentação deste repositório | [MIT](LICENSE) |
| Dados originais da ANP | Termos da ANP / dados abertos governamentais |
| Datasets derivados publicados no futuro | Recomendado: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt) (se houver redistribuição de dados processados) |

Sem um arquivo `LICENSE`, o padrão legal é “todos os direitos reservados”. Este projeto usa **MIT** para permitir cópia e reutilização do código e da documentação com atribuição.

## Documentação

O catálogo dos **42 conjuntos** publicados na página da ANP está em **[docs/dados-abertos.md](docs/dados-abertos.md)**. A análise do **Inventário de Dados** (240 bases institucionais) está em **[docs/inventario-dados.md](docs/inventario-dados.md)**.

## Como usar

1. Clone o repositório.
2. Consulte [docs/dados-abertos.md](docs/dados-abertos.md) (42 conjuntos) ou [docs/inventario-dados.md](docs/inventario-dados.md) (240 bases).
3. Execute os pipelines em `pipelines/` para baixar dados brutos em `data/raw/{slug}/`.
4. Leia ou escreva a exploração em `docs/conjuntos/`.

> Os pipelines e a documentação serão expandidos conforme cada conjunto de dados da ANP for explorado.

## Inventário de Dados ANP

Planilha oficial que cataloga **240 bases** mantidas pela ANP. **Contempla** o que a [página de 42 conjuntos](docs/dados-abertos.md) publica (agregando várias linhas por conjunto) e **outros canais de acesso** ainda não mapeados neste atlas — ver [Relação com o portal](docs/inventario-dados.md#relação-com-o-portal-de-dados-abertos).

| Item | Valor |
|------|-------|
| **Documentação** | [docs/inventario-dados.md](docs/inventario-dados.md) — análise completa |
| **Extração atual** | [data/catalogo-anp/inventario-dados/2026-05-24/](data/catalogo-anp/inventario-dados/2026-05-24/) |
| **Arquivo** | `inventario-dados.xlsx` + `extracao.md` (manifesto) |
| **URL oficial** | [inventario-dados.xlsx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/inventario-dados.xlsx) |
| **Atualização no portal** | 5/12/2025 |

### O que há neste inventário

A planilha `Dados ANP` registra, para cada base:

1. **Nome e descrição** — título institucional e escopo da base.
2. **Unidade responsável** — sigla da área ANP (SDC, SDT, SDL, SIM, SDP, etc.).
3. **Disponibilidade no dados.gov.br** — Sim (182) · Sim/CGU (17) · Não (38).
4. **Periodicidade** — mensal (87), anual (65), diária (28), semestral, conforme demanda, etc.
5. **Política pública** — vínculo ao PPA quando aplicável.
6. **Sigilo** — 38 bases com conteúdo sigiloso; 202 sem.

**Temas cobertos:** exploração e produção · acervo técnico · refino e derivados · biocombustíveis · movimentação SIMP · cadastro de revendas/postos · tancagem e terminais · preços (LPC) · vendas · qualidade (PMQC) · fiscalização · licitações · PD&I.

**Relacionadas a combustíveis/abastecimento:** ~98 entradas (filtro por palavras-chave na análise) — detalhes e tabelas em [docs/inventario-dados.md](docs/inventario-dados.md).

**Nova extração:** criar `data/catalogo-anp/inventario-dados/{AAAA-MM-DD}/`, registrar em `extracao.md` e atualizar a documentação (passo a passo no manifesto).

## Repositório

https://github.com/GabrielTrentino/anp-data-atlas
