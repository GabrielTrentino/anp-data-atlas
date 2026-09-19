# Inventário de Dados ANP

Análise da planilha oficial **Inventário de Dados** — catálogo institucional das bases mantidas pela ANP. **Contempla** o que a [página de 42 conjuntos](dados-abertos.md) publica para download, além de outros canais de acesso a dados que ainda serão explorados neste atlas.

| Item | Valor |
|------|-------|
| **Extração analisada** | [2026-09-19](../data/catalogo-anp/inventario-dados/2026-09-19/) |
| **Arquivo** | `inventario-dados.xlsx` |
| **URL oficial** | [inventario-dados.xlsx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/inventario-dados.xlsx) |
| **Atualização no portal** | 16/7/2026 |
| **PDA vigente** | [2026-2028](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/pda-2026-2028.pdf) |

## O que é este inventário

| Aspecto | Inventário ANP (esta planilha) | Catálogo dados abertos (`dados-abertos.md`) | Exploração `conjuntos/` |
|---------|-------------------------------|---------------------------------------------|-------------------------|
| Escopo | **236 bases** registradas internamente (extração 2026-09-19) | **42 conjuntos** com página de download | Conjuntos explorados empiricamente |
| Conteúdo | Nome do conjunto, nome da base, descrição, unidade, periodicidade, sigilo, flag PDA 2026–2028 | URL, formato, contexto de uso | Schema, arquivos medidos, ETL |
| Uso | Mapear quem mantém cada base e com que frequência | Saber o que baixar e onde | Integrar e documentar armadilhas |

## Relação com o portal de dados abertos

O inventário e a página dos **42 conjuntos** não são listas paralelas — são **níveis diferentes** do mesmo catálogo ANP:

```
Inventário (236 bases institucionais)
        ↓ agrupamento / vitrine pública
Portal — 42 conjuntos (página de download)
        ↓ outros canais (painéis, dados.gov.br, CGU…)
Acesso empírico — docs/conjuntos/{slug}.md
```

| Aspecto | Inventário | Portal (42 conjuntos) |
|---------|------------|------------------------|
| **Papel** | Registro interno de cada base | Página de download por tema |
| **Granularidade** | Fina — sub-tabelas, séries por ano/produto | Grossa — um conjunto agrega várias linhas |
| **Relação típica** | **N linhas → 1 conjunto** | **1 conjunto → N linhas** |
| **Nomenclatura** | Nome institucional + coluna de conjunto | Título da vitrine no gov.br |

Na extração **2026-09-19**, a planilha passa a trazer explicitamente o **Nome do conjunto de dados**, alinhando sub-bases aos conjuntos da vitrine. Continuam existindo blocos fora dos 42 (ex.: execução orçamentária, “Não abertos”, bases do PDA a publicar).

**O inventário também cobre acessos fora da página dos 42**, indicados na coluna *Disponível no Portal Brasileiro de Dados Abertos?* — por exemplo painéis dinâmicos no site ANP e bases marcadas **Não** (sigilosas ou sem vitrine CSV). Esses canais **não têm slug próprio** no catálogo do portal; serão mapeados depois, quando forem explorados.

### Como usar os dois catálogos neste atlas

| Pergunta | Onde consultar |
|----------|----------------|
| Onde baixar e qual slug adotar? | [dados-abertos.md](dados-abertos.md) |
| Quantas sub-bases existem, quem mantém, periodicidade? | Este inventário |
| Schema, arquivos medidos, integração histórica | `docs/conjuntos/{slug}.md` |

> **Regra prática:** não criar slugs separados no monorepo para cada linha do inventário quando o portal já unifica o tema (ex.: movimentação SIMP = várias linhas, um conjunto `movimentacao-derivados`).

## Estrutura da planilha (2026-09-19)

**Planilha única:** `Dados ANP` — 236 linhas de base × **10 colunas**

| # | Coluna | Conteúdo |
|---|--------|----------|
| 1 | *(índice / seção)* | Numeração ou marcadores de seção |
| 2 | **Nome do conjunto de dados** | Agrupa várias bases sob o tema da vitrine (preenchido na 1ª linha do grupo) |
| 3 | **Nome da base de dados** | Título institucional da base |
| 4 | **Descrição da base** | Texto descritivo (escopo, origem, uso) |
| 5 | **Unidade/responsável pela base** | Sigla da superintendência/área ANP |
| 6 | **Disponível no Portal Brasileiro de Dados Abertos?** | Sim · Não |
| 7 | **Periodicidade de atualização** | Mensal, anual, diária, conforme demanda, etc. |
| 8 | **Nome da Política pública relacionada** | Ex.: PPA 3103 — Petróleo, Gás, Derivados e Biocombustíveis |
| 9 | **Possui conteúdo sigiloso?** | Sim / Não |
| 10 | **Dados a serem publicados em 2026 a 2028** | Flag do [PDA 2026-2028](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/pda-2026-2028.pdf) |

> Schema anterior (extração [2026-05-24](../data/catalogo-anp/inventario-dados/2026-05-24/)): 8 colunas, sem colunas 2 e 10.

## Panorama (extração 2026-09-19)

| Métrica | Valor |
|---------|------:|
| Bases catalogadas | 236 |
| Disponíveis no dados.gov.br (`Sim`) | 198 |
| Não disponíveis no portal (`Não`) | 38 |
| Com conteúdo sigiloso | 28 |
| Sem conteúdo sigiloso | 208 |
| Marcadas para publicação no PDA 2026–2028 | 10 |

### Por unidade responsável (top 12)

| Unidade | Bases | Área típica |
|---------|------:|-------------|
| SDC | 55 | Estatística, séries históricas, preços, vendas |
| SDT | 37 | Acervo técnico (poços, sísmica, geoquímica) |
| SEP | 20 | Exploração |
| SIM | 18 | Mercado, capacidade, tancagem |
| SDP | 17 | Desenvolvimento e produção |
| SPL | 16 | Licitações e rodadas |
| SDL | 15 | Distribuição, revenda, movimentação (SIMP) |
| SPG | 13 | Participações governamentais |
| SFO | 10 | *(contato específico no inventário)* |
| SCL | 8 | Conteúdo local |
| STM | 8 | PD&I, recursos humanos |
| SSO | 5 | Segurança operacional |

### Por periodicidade (top 10)

| Periodicidade | Bases |
|---------------|------:|
| Mensal | 92 |
| Anual | 69 |
| Diária | 24 |
| Semestral | 20 |
| Conforme demanda | 12 |
| Rodada | 8 |
| Semanal | 4 |
| Trimestral | 4 |
| Carga única | 1 |
| Sem atualização | 1 |

## Bases a publicar no PDA 2026–2028

Linhas com a coluna **Dados a serem publicados em 2026 a 2028** preenchida (`Sim`):

| Base | Conjunto (inventário) |
|------|------------------------|
| Registro de autoprodutor e autoimportador | Registro de autoprodutor e autoimportador |
| Autorização da atividade de distribuição de Gás Natural Comprimido (GNC) | Autorização da atividade de distribuição de Gás Natural |
| Autorização da atividade de distribuição de Gás Natural Liquefeito (GNL) | Autorização da atividade de distribuição de Gás Natural |
| Autorização para as operações de transbordo entre embarcações (ship-to-ship) | Autorização para as operações de transbordo… |
| Autorização para atividade de importação de gás natural e GNL | Autorização para atividade de importação… |
| Autorização para atividade de exportação de cargas ociosas de GNL | Autorização para atividade de exportação… |
| Autorização para transporte a granel aquaviário (petróleo, derivados, GN, biocombustíveis) | Autorização para a atividade de transporte a granel… |
| Autorização para atividade de carregamento de gás natural | Autorização para atividade de carregamento… |
| Autorização para atividade de comercialização de gás natural | Autorização para atividade de comercialização… |
| Listagem dos Dados Técnicos Marítimos Disponibilizados no âmbito do PROMAR | Acervo de Dados Técnicos |

Ainda **não** há páginas próprias na vitrine dos 42 conjuntos para a maioria desses itens — acompanhar o portal e o inventário.

## Temas presentes no inventário

A planilha cobre todo o escopo regulatório da ANP. Agrupamento temático (uma base pode aparecer em um grupo):

| Tema | Exemplos no inventário | Unidades frequentes |
|------|------------------------|---------------------|
| **Exploração e produção (E&P)** | Poços, produção por estado/poço, incidentes, rodadas | SDP, SEP, SDT, SSO |
| **Processamento e derivados** | Refino, produção de derivados, import/export | SDC |
| **Biocombustíveis** | Biodiesel, etanol (séries por período) | SDC |
| **Distribuição e abastecimento** | Movimentação SIMP, cadastro revendas/postos, TRR, GLP | SDL, SIM |
| **Tancagem e armazenagem** | Tancagem autorizada a operar; capacidade de terminais | SIM |
| **Preços e vendas** | LPC, vendas por segmento/município/estado | SDC |
| **Qualidade** | PMQC, PML | SBQ |
| **Fiscalização** | Ações de fiscalização do abastecimento; multas | SFI |
| **Participações e regulação econômica** | Participações especiais, preço de referência | SPG |
| **Acervo técnico** | Poços, programas geofísicos, geoquímica | SDT |
| **PD&I e capacitação** | Projetos PD&I, credenciamento de universidades | STM |
| **Gás natural (autorizações futuras)** | GNC/GNL, ship-to-ship, carregamento, comercialização | SCM / PDA |

## Bases ligadas a combustíveis e abastecimento

Filtro por palavras-chave (*combust*, *abastec*, *tancagem*, *derivados*, *GLP*, *etanol*, *revenda*, *SIMP*, *PMQC*, *fiscaliz*, *terminal*, *distribuidor*) — **~68 entradas** na extração 2026-09-19 (contagem menor que em 2026-05-24 por consolidação de nomes e remoções/renomes).

### Cadastro e infraestrutura de mercado

| Base | Unidade | Portal |
|------|---------|--------|
| Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos | SDL | Sim |
| Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo (GLP) | SDL | Sim |
| Pontos de Abastecimento Autorizados | SDL | Sim |
| Capacidade de Armazenagem de Terminais | SIM | Sim |
| Tancagem do Abastecimento Nacional de Combustíveis | SIM | Sim |
| Distribuidores de Combustíveis Líquidos (várias bases) | SDL | Sim |

### Exploração documentada neste atlas

| Base (inventário) | Slug / doc no atlas |
|-------------------|---------------------|
| Tancagem do Abastecimento Nacional… | [tancagem-abastecimento.md](conjuntos/tancagem-abastecimento.md) |

## Bases não abertas no dados.gov.br (38)

Incluem bases **sigilosas** e conjuntos disponíveis apenas em **painel dinâmico** no site ANP (ex.: alguns painéis de produção/vendas marcados como descontinuados no inventário). Antes de integrar, verificar colunas de disponibilidade e sigilo.

## Diff vs. extração 2026-05-24 — nomes ausentes nesta planilha

> **Política do atlas:** nomes que sumiram da planilha **não são apagados da documentação** — ficam registrados abaixo. Muitos parecem **renomeio ou consolidação** (ex.: séries por ano fundidas; “Multas … 2017” → “Multas … 2016”; “Capacidade de armazenamento dos terminais…” → “Capacidade de Armazenagem de Terminais”), não necessariamente descontinuidade do dado no portal.

**32 nomes** presentes em [2026-05-24](../data/catalogo-anp/inventario-dados/2026-05-24/) e **ausentes** em 2026-09-19 (texto exato da coluna *Nome da base*):

| Nome na extração 2026-05-24 | Observação |
|-----------------------------|------------|
| Acervo Físico de Dados | Ausente na planilha atual |
| Amostras de de Rochas e Fluidos - Fluidos | Tipografia antiga; ver “Amostras de Rochas e Fluidos - Fluidos” na extração nova |
| Ações de Desenvolvimento de Pessoas | Ausente na planilha atual |
| Cadastro Básico de Universidades | Parece renomeado para “… (Unidades de Pesquisa Credenciadas)” |
| Capacidade de armazenamento dos terminais de petróleo e combustíveis líquidos autorizados pela ANP | Parece renomeado para **Capacidade de Armazenagem de Terminais** |
| Certificação Conteúdo Local | Ausente na planilha atual |
| Concurso ANP | Ausente na planilha atual |
| Dados Brutos da Fiscalização  Painel Dinâmico da Fiscalização do Abastecimento | Ausente na planilha atual |
| Documentos Físicos Recebidos e Gerados | Ausente na planilha atual |
| Fase de Desenvolvimento e Produção - Previsão de Atividade e Investimento | Possível desmembramento em linhas de atividade/investimento realizados e previsão por atividade |
| Isenção e Ajuste de Conteúdo Local | Ausente na planilha atual |
| Multas aplicadas com vencimento a partir de 2017 | Parece alinhado/renomeado para **… a partir de 2016** |
| Organograma/ Quem é quem | Ausente na planilha atual |
| Participações Governamentais - Participações Especiais distribuídas aos Campos Produtores | Parece substituído por “… apuradas em cada Campo Produtor” |
| Processamento de petróleo e produção de derivados - Processamento de petróleo *(variação tipográfica)* | Ver linha consolidada na extração nova |
| Processo de planejamento de aquisições… Tecnologia da Informação | Ausente na planilha atual |
| Processos Administrativos Eletrônicos Públicos | Ausente na planilha atual |
| Processos Administrativos Eletrônicos Restritos por Outras Hipóteses Legais de Sigilo | Ausente na planilha atual |
| Processos Administrativos Físicos | Ausente na planilha atual |
| Produção de Biocombustíveis - Produção de biodiesel (metros cúbicos) 2005-2021 | Séries reagrupadas (2005-2023 / 2024-2026) |
| Produção de Biocombustíveis - Produção de biodiesel (metros cúbicos) 2022-2024 | Séries reagrupadas |
| Produção de Biocombustíveis - Produção de etanol anidro e hidratado (metros cúbicos) 2012-2024 | Estendida/renomeada para 2012-2026 |
| Produção de Petróleo e Gás Natural por Poço (2005 - 2017) | Consolidada em “Produção de Petróleo e Gás Natural por Poço” |
| Produção de Petróleo e Gás Natural por Poço 2021 | Idem |
| Produção de Petróleo e Gás Natural por Poço 2022 | Idem |
| Produção de Petróleo e Gás Natural por Poço 2023 | Idem |
| Produção de Petróleo e Gás Natural por Poço 2024 | Idem |
| Registro de contratos de compra e venda de gás natural | Ausente na planilha atual (comercialização permanece em outras linhas) |
| Relatório mensal de exportação de cargas ociosas de gás natural liquefeito (GNL) | Relacionado a autorizações GNL no PDA 2026–2028 |
| Relatório mensal de importação de gás natural liquefeito (GNL) | Relacionado a autorizações GNL no PDA 2026–2028 |
| Relatórios de Dispêndios de Conteúdo Local | Ausente na planilha atual |
| Usuários Associados | Ausente na planilha atual |

### Nomes novos nesta extração (28)

Incluem, entre outros: **Anuário Estatístico 2025**; autorizações GNC/GNL, ship-to-ship, carregamento/comercialização/importação/exportação; **Registro de autoprodutor e autoimportador**; painéis de processamento/vendas/etanol-biodiesel (alguns marcados descontinuados); consolidação de produção por poço; séries de biocombustíveis atualizadas.

## Histórico de extrações

| Data | Pasta | Notas |
|------|-------|-------|
| 2026-09-19 | [data/catalogo-anp/inventario-dados/2026-09-19/](../data/catalogo-anp/inventario-dados/2026-09-19/) | Schema com conjunto + flag PDA 2026–2028; 236 bases; portal 16/7/2026 |
| 2026-05-24 | [data/catalogo-anp/inventario-dados/2026-05-24/](../data/catalogo-anp/inventario-dados/2026-05-24/) | Primeira extração versionada — 240 bases; portal 5/12/2025; schema de 8 colunas |

## Como atualizar

1. Baixar nova versão do [portal ANP](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos).
2. Criar `data/catalogo-anp/inventario-dados/{AAAA-MM-DD}/` com `inventario-dados.xlsx` e `extracao.md`.
3. Comparar nomes com a extração anterior: **registrar ausências** nesta seção (não apagar histórico).
4. Reexecutar contagens e atualizar as tabelas deste arquivo.
5. Registrar nova linha em **Histórico de extrações**.
