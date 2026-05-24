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

Síntese dos **42 conjuntos** da [página de dados abertos](docs/dados-abertos.md) — o tipo de informação que cada um publica (não substitui o dicionário de colunas em `docs/conjuntos/`). Conjuntos com doc local linkam para exploração detalhada.

### Abastecimento, distribuição e mercado downstream

| # | Slug | Dados que traz |
|---|------|----------------|
| 41 | [`tancagem-abastecimento`](docs/conjuntos/tancagem-abastecimento.md) | Capacidade de armazenagem autorizada (m³) por instalação, tanque (`Tag`) e grupo de produto |
| 21 | [`movimentacao-derivados`](docs/conjuntos/movimentacao-derivados.md) | Volumes movimentados no SIMP por produto (líquidos, GLP, lubrificantes, TRR, aviação, etc.) |
| 12 | [`cadastro-revendas-combustiveis`](docs/conjuntos/cadastro-revendas-combustiveis.md) | Cadastro diário de postos revendedores (localização, bandeira, situação) |
| 11 | [`cadastro-revendas-glp`](docs/conjuntos/cadastro-revendas-glp.md) | Cadastro diário de revendas de GLP (botijão e granel) |
| 27 | [`pontos-abastecimento`](docs/conjuntos/pontos-abastecimento.md) | Instalações de pontos de abastecimento autorizados |
| 15 | [`distribuidores-combustiveis-liquidos`](docs/conjuntos/distribuidores-combustiveis-liquidos.md) | Distribuidores autorizados, contratos de cessão e agentes GLP |
| 28 | [`pmqc`](docs/conjuntos/pmqc.md) | Indicadores de qualidade analítica dos combustíveis comercializados |
| 29 | [`pml`](docs/conjuntos/pml.md) | Monitoramento da qualidade de lubrificantes |
| 40 | [`serie-historica-precos`](docs/conjuntos/serie-historica-precos.md) | Preços semanais/mensais de revenda (gasolina, etanol, diesel, GNV, GLP) por localidade |
| 42 | [`vendas-derivados`](docs/conjuntos/vendas-derivados.md) | Volumes vendidos por distribuidoras, segmento, produto e geografia |
| 2 | [`fiscalizacao-abastecimento`](docs/conjuntos/fiscalizacao-abastecimento.md) | Ações de fiscalização, documentos lavrados e resultados por segmento |
| 9 | [`capacidade-armazenagem-terminais`](docs/conjuntos/capacidade-armazenagem-terminais.md) | Capacidade de terminais (tipo, empresa, UF, município) |
| 22 | [`movimentacao-terminais-aquaviarios`](docs/conjuntos/movimentacao-terminais-aquaviarios.md) | Movimentação em terminais aquaviários autorizados |
| 37 | [`registro-lubrificantes`](docs/conjuntos/registro-lubrificantes.md) | Catálogo de óleos e graxas lubrificantes registrados |

### Produção, refino, comércio exterior e estatística consolidada

| # | Slug | Dados que traz |
|---|------|----------------|
| 32 | [`processamento-petroleo-derivados`](docs/conjuntos/processamento-petroleo-derivados.md) | Processamento de petróleo e produção de derivados por refinaria |
| 33 | [`producao-biocombustiveis`](docs/conjuntos/producao-biocombustiveis.md) | Produção de biodiesel e etanol (séries temporais e regionais) |
| 34 | [`producao-por-estado`](docs/conjuntos/producao-por-estado.md) | Produção de petróleo, LGN e gás por UF e localização (terra/mar) |
| 35 | [`producao-por-poco`](docs/conjuntos/producao-por-poco.md) | Produção detalhada por poço (séries recentes e históricas) |
| 19 | [`importacoes-exportacoes`](docs/conjuntos/importacoes-exportacoes.md) | Comércio exterior de petróleo, derivados e etanol |
| 5 | [`anuario-estatistico`](docs/conjuntos/anuario-estatistico.md) | Dezenas de tabelas CSV consolidando ~10 anos da indústria e do abastecimento |

### Exploração e produção (E&P)

| # | Slug | Dados que traz |
|---|------|----------------|
| 13 | `dados-ep` | Informações agregadas sobre exploração e produção |
| 16 | `fase-exploracao` | Blocos e atividades na fase exploratória |
| 17 | `fase-desenvolvimento-producao` | Campos e ativos em desenvolvimento e produção |
| 8 | `blocos-fase-exploratoria-encerrada` | Blocos que encerraram a fase exploratória |
| 20 | `incidentes-ep` | Incidentes de segurança operacional em E&P (tipos, feridos, substâncias) |
| 38 | `resultado-poco` | Resultados e características de poços |
| 31 | `previsao-atividades-investimentos` | Previsão de investimentos e atividades exploratórias |
| 36 | `relacao-concessionarios` | Concessionários de blocos e contratos |
| 39 | `rodadas-licitacoes` | Blocos ofertados, vencedores e cessões de contrato |

### Gás natural

| # | Slug | Dados que traz |
|---|------|----------------|
| 7 | `autorizacoes-gas-natural` | Autorizações para atividades com gás natural |
| 10 | `comercializacao-gas-natural` | Vendas de gás natural a distribuidoras e consumidores livres |
| 23 | `movimentacao-gas-gasodutos` | Volumes transportados em gasodutos |

### Acervo técnico e geociências

| # | Slug | Dados que traz |
|---|------|----------------|
| 1 | `acervo-dados-tecnicos` | Poços, programas geofísicos e geoquímica do acervo ANP |
| 4 | `amostras-rochas-fluidos` | Declaração de amostras de rochas e fluidos |
| 6 | `aquisicao-processamento-estudo-dados` | Dados de aquisição sísmica e estudos geológicos |
| 14 | `bacias-sedimentares` | Limites e dados georreferenciados das bacias sedimentares |

### Regulação, fiscalização e participações

| # | Slug | Dados que traz |
|---|------|----------------|
| 3 | `aditamento-conteudo-local` | Aditamentos contratuais de conteúdo local |
| 18 | `fiscalizacao-conteudo-local` | Fiscalização de metas de conteúdo local por fase/rodada |
| 24 | `multas-2016` | Multas de fiscalização com vencimento a partir de 2016 |
| 25 | `participacoes-governamentais` | Participações governamentais e preços de referência do petróleo |
| 26 | `pesquisa-desenvolvimento-inovacao` | Projetos e investimentos em PD&I do setor |
| 30 | `prestadores-apoio-administrativo` | Cadastro de prestadores de apoio administrativo |

Catálogo completo com links do portal: [docs/dados-abertos.md](docs/dados-abertos.md) · progresso: [TODO.md](TODO.md) · inventário institucional (240 bases): [docs/inventario-dados.md](docs/inventario-dados.md).

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
