# anp-data-atlas

Atlas de exploração dos dados abertos da ANP: documentação em Markdown e pipelines raw/true/ref para reutilização em outros projetos.

## Objetivo

Este repositório é uma **referência exploratória** dos dados publicados pela [Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)](https://www.gov.br/anp/pt-br). Ele reúne:

- **Documentação** em Markdown com descobertas, dicionários de campos, qualidade dos dados e exemplos de uso;
- **Pipelines** reproduzíveis para ingestão e transformação;
- **Camadas de dados** organizadas localmente, fora do controle de versão.

A ideia é servir de base para outros projetos — quem for construir análises, dashboards ou modelos pode consultar este atlas antes de reimplementar explorações do zero.

## Estrutura prevista

```
anp-data-atlas/
├── docs/           # Explorações, notas e guias em Markdown
├── pipelines/      # Scripts de ingestão e transformação (raw → true → ref)
└── data/           # Dados locais — não versionados no Git
    ├── raw/        # Dados brutos como baixados da ANP
    ├── true/       # Dados limpos, tipados e padronizados
    └── ref/        # Tabelas de referência, dimensões e lookups
```

Os arquivos em `data/raw/`, `data/true/` e `data/ref/` ficam no `.gitignore`. O repositório versiona a **lógica** (pipelines) e o **conhecimento** (docs), não os datasets.

## Camadas de dados

| Camada | Conteúdo |
|--------|----------|
| **raw** | Arquivos originais da fonte, sem alteração estrutural |
| **true** | Dados tratados: tipos corretos, nomes padronizados, duplicatas e nulos tratados |
| **ref** | Tabelas auxiliares (códigos, mapeamentos, dimensões) usadas nos pipelines |

## Fonte dos dados

Os dados brutos são **dados abertos da ANP**. A reutilização segue os termos e políticas definidos pela agência e pelo governo federal — este repositório **não relicencia** o conteúdo original da ANP, apenas documenta e processa localmente.

Ao publicar análises ou derivados, cite a fonte oficial da ANP e consulte as condições vigentes no portal de dados abertos.

## Licenciamento

| Conteúdo | Licença |
|----------|---------|
| Código, pipelines e documentação deste repositório | [MIT](LICENSE) |
| Dados originais da ANP | Termos da ANP / dados abertos governamentais |
| Datasets derivados publicados no futuro | Recomendado: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt) (se houver redistribuição de dados processados) |

Sem um arquivo `LICENSE`, o padrão legal é “todos os direitos reservados”. Este projeto usa **MIT** para permitir cópia e reutilização do código e da documentação com atribuição.

## Como usar

1. Clone o repositório.
2. Execute os pipelines em `pipelines/` para baixar e transformar os dados nas pastas locais `data/`.
3. Leia as explorações em `docs/` antes de iniciar um novo projeto que consuma dados da ANP.

> Os pipelines e a documentação serão expandidos conforme cada conjunto de dados da ANP for explorado.

## Repositório

https://github.com/GabrielTrentino/anp-data-atlas
