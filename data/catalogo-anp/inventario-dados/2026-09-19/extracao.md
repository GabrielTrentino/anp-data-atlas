# Extração — Inventário de Dados ANP

Registro da cópia local da planilha oficial de inventário institucional da ANP.

| Campo | Valor |
|-------|-------|
| **Data da extração** | 2026-09-19 |
| **Arquivo local** | `inventario-dados.xlsx` |
| **Fonte (URL)** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/inventario-dados.xlsx |
| **Atualização informada no portal** | 16/7/2026 ([dados-abertos.md](../../../docs/dados-abertos.md)) |
| **Planilha** | `Dados ANP` |
| **Registros** | 236 bases de dados |
| **Tamanho** | ~38 KB |
| **PDA vigente** | [2026-2028](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/home/pda-2026-2028.pdf) |

## Mudanças de schema vs. 2026-05-24

| Extração | Colunas |
|----------|---------|
| 2026-05-24 | 8 colunas (sem agrupamento por conjunto) |
| **2026-09-19** | 10 colunas — inclui **Nome do conjunto de dados** e **Dados a serem publicados em 2026 a 2028** |

## Comparação rápida com 2026-05-24

| Métrica | 2026-05-24 | 2026-09-19 |
|---------|----------:|----------:|
| Bases | 240 | 236 |
| Nomes só na extração antiga | — | 32 (ver análise) |
| Nomes só nesta extração | — | 28 |

## Como reproduzir

1. Abrir a [página de Dados abertos da ANP](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos).
2. Baixar **Inventário de Dados** (`inventario-dados.xlsx`).
3. Criar pasta `data/catalogo-anp/inventario-dados/{AAAA-MM-DD}/`.
4. Salvar como `inventario-dados.xlsx` e registrar neste `extracao.md`.
5. Atualizar a análise em [docs/inventario-dados.md](../../../docs/inventario-dados.md) e o resumo no [README](../../../README.md).

## Documentação derivada

- Análise completa: [docs/inventario-dados.md](../../../docs/inventario-dados.md)
- Catálogo público (42 conjuntos): [docs/dados-abertos.md](../../../docs/dados-abertos.md)
- Extração anterior: [2026-05-24](../2026-05-24/)
