"""Gera docs/conjuntos/{slug}.md para conjuntos prioritários do fuel-analytics."""
from __future__ import annotations

from pathlib import Path

from _conjuntos_fuel_metadata import CONJUNTOS_FUEL

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "conjuntos"


def render(c: dict) -> str:
    cruz = "\n".join(f"- [{s}]({s}.md)" for s in c["cruzamentos"])
    return f"""# {c["title"]}

| Campo | Valor |
|-------|-------|
| **Slug** | `{c["slug"]}` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#{c["num"]}) |
| **Página oficial** | {c["url"]} |
| **Unidade ANP (inventário)** | {c["unidade"]} |
| **Periodicidade** | {c["periodicidade"]} |
| **Formato** | {c["formato"]} |
| **Fonte operacional** | {c["fonte"]} |
| **Pasta local** | `data/raw/{c["slug"]}/` |
| **Inventário ANP** | {c["inventario"]} |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |

## Contexto

{c["contexto"]}

## Relevância para anp-fuel-analytics

{c["relevancia"]}

Estudo planejado em [anp-fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/{c["slug"]}/) (documentação de referência; pipeline pendente).

## Estrutura dos arquivos

> **Status:** pendente — confirmar schema, encoding e periodicidade real após download de amostra.

Consultar a página oficial e metadados publicados no portal antes de integrar.

## Inventário empírico dos brutos

> **Status:** pendente — preencher após download em `data/raw/{c["slug"]}/`.

| Arquivo local | Linhas | Métrica | Período | Notas |
|---------------|-------:|---------|---------|-------|
| _a preencher_ | | | | |

## Qualidade e chaves

> **Status:** pendente — validar na exploração fuel-analytics.

- Chave lógica candidata: _a definir_
- Regras de agregação: _a definir_

## Cruzamentos sugeridos

{cruz}

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base institucional #{c["num"]} ({c["unidade"]}, {c["periodicidade"]})
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Uso neste atlas

**Status da exploração:** documentação de referência criada ({c["slug"]}). Inventário empírico, qualidade e pipeline fuel-analytics **pendentes**.

**Próximos passos (fuel-analytics):**

1. Download amostra → `data/raw/{c["slug"]}/`
2. Notebook `01_perfil_exploratorio.ipynb`
3. Promover findings estáveis para este arquivo
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for c in CONJUNTOS_FUEL:
        path = OUT / f"{c['slug']}.md"
        path.write_text(render(c), encoding="utf-8")
        print("wrote", path.name)


if __name__ == "__main__":
    main()
