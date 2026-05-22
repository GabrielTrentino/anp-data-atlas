# anp-data-atlas

Atlas de exploração dos dados abertos da ANP: documentação em Markdown e pipelines de ingestão para reutilização em outros projetos.

## Objetivo

Este repositório é uma **referência exploratória** dos dados publicados pela [Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)](https://www.gov.br/anp/pt-br). Ele reúne:

- **Documentação** em Markdown com metadados, contexto, dicionários de campos, qualidade dos dados e exemplos de uso;
- **Pipelines** reproduzíveis para baixar e organizar os dados brutos localmente;
- **Dados brutos** (`raw`) mantidos fora do Git, apenas para análise local de metadados e contexto.

A ideia é servir de base para outros projetos — quem for construir análises, dashboards ou modelos pode consultar este atlas antes de reimplementar explorações do zero.

## Estrutura prevista

```
anp-data-atlas/
├── docs/
│   ├── dados-abertos.md   # Catálogo oficial (índice dos 42 conjuntos)
│   └── conjuntos/         # Exploração por conjunto (metadados, contexto)
├── pipelines/             # Scripts de ingestão (download e organização dos brutos)
└── data/
    └── raw/{slug}/        # Dados brutos por conjunto (não versionados)
```

Os arquivos em `data/raw/` ficam no `.gitignore`. O repositório versiona a **lógica** (pipelines) e o **conhecimento** (docs), não os datasets.

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

O catálogo completo dos conjuntos publicados pela ANP está em **[docs/dados-abertos.md](docs/dados-abertos.md)** (42 conjuntos, documentos relacionados e índice de exploração).

## Como usar

1. Clone o repositório.
2. Consulte [docs/dados-abertos.md](docs/dados-abertos.md) e escolha um conjunto.
3. Execute os pipelines em `pipelines/` para baixar os dados brutos em `data/raw/{slug}/`.
4. Leia ou escreva a exploração em `docs/conjuntos/` — metadados, contexto e notas — antes de iniciar um novo projeto que consuma dados da ANP.

> Os pipelines e a documentação serão expandidos conforme cada conjunto de dados da ANP for explorado.

## Repositório

https://github.com/GabrielTrentino/anp-data-atlas
