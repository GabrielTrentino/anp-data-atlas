# Inventário de Dados ANP

Análise da planilha oficial **Inventário de Dados** — catálogo institucional das bases mantidas pela ANP. **Contempla** o que a [página de 42 conjuntos](dados-abertos.md) publica para download, além de outros canais de acesso a dados que ainda serão explorados neste atlas.

| Item | Valor |
|------|-------|
| **Extração analisada** | [2026-05-24](../data/catalogo-anp/inventario-dados/2026-05-24/) |
| **Arquivo** | `inventario-dados.xlsx` |
| **URL oficial** | [inventario-dados.xlsx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/inventario-dados.xlsx) |
| **Atualização no portal** | 5/12/2025 |

## O que é este inventário

| Aspecto | Inventário ANP (esta planilha) | Catálogo dados abertos (`dados-abertos.md`) | Exploração `conjuntos/` |
|---------|-------------------------------|---------------------------------------------|-------------------------|
| Escopo | **240 bases** registradas internamente | **42 conjuntos** com página de download | Conjuntos explorados empiricamente |
| Conteúdo | Nome, descrição, unidade, periodicidade, sigilo | URL, formato, contexto de uso | Schema, arquivos medidos, ETL |
| Uso | Mapear quem mantém cada base e com que frequência | Saber o que baixar e onde | Integrar e documentar armadilhas |

## Relação com o portal de dados abertos

O inventário e a página dos **42 conjuntos** não são listas paralelas — são **níveis diferentes** do mesmo catálogo ANP:

```
Inventário (240 bases institucionais)
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
| **Nomenclatura** | Nome institucional fixo | Título da vitrine no gov.br |

Na extração **2026-05-24**, **41 dos 42** conjuntos do portal têm correspondência clara no inventário (várias linhas por conjunto). O restante (`dados-ep`) aparece como sub-bases **“Dados de Exploração e Produção — …”** no inventário.

**O inventário também cobre acessos fora da página dos 42**, indicados na coluna *Disponível no Portal Brasileiro de Dados Abertos?* — por exemplo bases **Sim/CGU**, painéis dinâmicos no site ANP (algumas fiscalizações), bases marcadas **Não** (sigilosas ou sem vitrine CSV). Esses canais **não têm slug próprio** no catálogo do portal; serão mapeados depois, quando forem explorados.

### Como usar os dois catálogos neste atlas

| Pergunta | Onde consultar |
|----------|----------------|
| Onde baixar e qual slug adotar? | [dados-abertos.md](dados-abertos.md) |
| Quantas sub-bases existem, quem mantém, periodicidade? | Este inventário |
| Schema, arquivos medidos, integração histórica | `docs/conjuntos/{slug}.md` |

> **Regra prática:** não criar slugs separados no monorepo para cada linha do inventário quando o portal já unifica o tema (ex.: movimentação SIMP = várias linhas, um conjunto `movimentacao-derivados`).

## Estrutura da planilha

**Planilha única:** `Dados ANP` — 240 linhas × 8 colunas

| # | Coluna | Conteúdo |
|---|--------|----------|
| 1 | *(índice)* | Numeração sequencial |
| 2 | **Nome da base de dados** | Título institucional da base |
| 3 | **Descrição da base** | Texto descritivo (escopo, origem, uso) |
| 4 | **Unidade/responsável pela base** | Sigla da superintendência/área ANP |
| 5 | **Disponível no Portal Brasileiro de Dados Abertos?** | Sim · Não · Sim/CGU · exceções anotadas |
| 6 | **Periodicidade de atualização** | Mensal, anual, diária, conforme demanda, etc. |
| 7 | **Nome da Política pública relacionada** | Ex.: PPA 3103 — Petróleo, Gás, Derivados e Biocombustíveis |
| 8 | **Possui conteúdo sigiloso?** | Sim / Não |

## Panorama (extração 2026-05-24)

| Métrica | Valor |
|---------|------:|
| Bases catalogadas | 240 |
| Disponíveis no dados.gov.br (`Sim`) | 182 |
| Disponíveis via CGU (`Sim/CGU`) | 17 |
| Não disponíveis no portal (`Não`) | 38 |
| Com conteúdo sigiloso | 38 |
| Sem conteúdo sigiloso | 202 |

### Por unidade responsável (top 12)

| Unidade | Bases | Área típica |
|---------|------:|-------------|
| SDC | 53 | Estatística, séries históricas, preços, vendas |
| SDT | 36 | Acervo técnico (poços, sísmica, geoquímica) |
| SEP | 20 | Exploração e produção |
| SDP | 19 | Desenvolvimento e produção |
| SPL | 17 | Licitações e rodadas |
| SDL | 15 | Distribuição, revenda, movimentação (SIMP) |
| SPG | 13 | Participações governamentais |
| SIM | 12 | Mercado, capacidade, tancagem |
| SCL | 11 | Conteúdo local |
| SFO | 10 | *(contato específico no inventário)* |
| STM | 8 | PD&I, recursos humanos |
| SFI | 3 | Fiscalização do abastecimento |

### Por periodicidade (top 10)

| Periodicidade | Bases |
|---------------|------:|
| Mensal | 87 |
| Anual | 65 |
| Diária | 28 |
| Semestral | 22 |
| Conforme demanda | 14 |
| Rodada | 8 |
| Semanal | 6 |
| Trimestral | 4 |
| Sem atualização | 2 |
| Carga única | 1 |

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
| **Qualidade** | PMQC | SBQ |
| **Fiscalização** | Ações de fiscalização do abastecimento; painéis dinâmicos | SFI |
| **Participações e regulação econômica** | Preço de referência do petróleo, corrente de petróleo | SPG |
| **Acervo técnico** | Poços, programas geofísicos, geoquímica | SDT |
| **PD&I e capacitação** | Projetos PD&I, PRH setor | STM |

## Bases ligadas a combustíveis e abastecimento

Filtro por palavras-chave (*combust*, *abastec*, *tancagem*, *derivados*, *GLP*, *etanol*, *revenda*, *SIMP*, *PMQC*, *fiscaliz*, *terminal*, *distribuidor*) — **98 entradas** na extração 2026-05-24.

### Cadastro e infraestrutura de mercado

| Base | Unidade | Periodicidade | Portal |
|------|---------|---------------|--------|
| Dados Cadastrais dos Revendedores Varejistas de Combustíveis Automotivos | SDL | Diária | Sim |
| Dados Cadastrais das Revendas de Gás Liquefeito de Petróleo | SDL | Diária | Sim |
| Dados Cadastrais de Pontos de Abastecimento Autorizados | SDL | Diário | Sim |
| Capacidade de armazenamento dos terminais… | SIM | Semestral | Sim |
| **Tancagem do Abastecimento Nacional de Combustíveis (2022 - 2023 - 2024)** | SIM | Mensal | Sim |
| Distribuidores de Combustíveis Líquidos (várias bases) | SDL | Mensal / Semanal / Semestral | Sim |

### Movimentação (SIMP / Res. ANP 729/2018)

| Base | Periodicidade |
|------|---------------|
| Movimentação… — Combustíveis líquidos | Mensal |
| Movimentação… — GLP | Mensal |
| Movimentação… — Combustíveis de aviação | Mensal |
| Movimentação… — TRR | Mensal |
| Movimentação… — Lubrificantes, solventes, asfaltos | Mensal |
| Movimentação… — Fornecedores de Etanol (Venda Direta) | Mensal |
| Movimentação… — Logística do Abastecimento Nacional | Mensal |

### Qualidade, fiscalização e preços

| Base | Unidade | Periodicidade | Portal |
|------|---------|---------------|--------|
| PMQC — Programa de Monitoramento da Qualidade dos Combustíveis | SBQ | Mensal | Sim |
| Ações de Fiscalização do Abastecimento | SFI | Mensal | Sim |
| Dados Brutos da Fiscalização — Painel Dinâmico… | SFI | Mensal | **Não** |
| Boletim Fiscalização do Abastecimento em Notícias | SFI | Semestral | **Não** |
| Série Histórica Preços — Combustíveis automotivos | SDC | Semestral | Sim |

### Exploração documentada neste atlas

| Base (inventário) | Slug / doc no atlas |
|-------------------|---------------------|
| Tancagem do Abastecimento Nacional… | [tancagem-abastecimento.md](conjuntos/tancagem-abastecimento.md) |

> O nome no inventário cita **2022–2024**; o portal já publica **2025–2026**. Usar a matriz e o inventário empírico no doc do conjunto.

## Bases não abertas no dados.gov.br (38)

Incluem bases **sigilosas** (38 marcadas com conteúdo sigiloso) e conjuntos disponíveis apenas em **painel dinâmico** no site ANP (ex.: algumas fiscalizações). Antes de integrar, verificar coluna 5 (*Disponível no Portal…*) e coluna 8 (*sigiloso*).

## Histórico de extrações

| Data | Pasta | Notas |
|------|-------|-------|
| 2026-05-24 | [data/catalogo-anp/inventario-dados/2026-05-24/](../data/catalogo-anp/inventario-dados/2026-05-24/) | Primeira extração versionada neste repositório |

## Como atualizar

1. Baixar nova versão do [portal ANP](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos).
2. Criar `data/catalogo-anp/inventario-dados/{AAAA-MM-DD}/` com `inventario-dados.xlsx` e `extracao.md`.
3. Reexecutar contagem (planilha `Dados ANP`) e atualizar as tabelas deste arquivo.
4. Registrar nova linha em **Histórico de extrações**.
