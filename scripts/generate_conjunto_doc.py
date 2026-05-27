"""Gera docs/conjuntos/{slug}.md para todos os conjuntos configurados no datasets.yaml."""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "conjuntos"
CONFIG = ROOT / "config" / "datasets.yaml"


def load_datasets() -> dict:
    with open(CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def render(slug: str, meta: dict) -> str:
    cruz = "\n".join(f"- [{s}]({s}.md)" for s in meta.get("cruzamentos", []))
    schema = meta.get("schema", {})
    enc = schema.get("encoding") or "—"
    sep = schema.get("separator") or "—"
    keys = ", ".join(schema.get("key_columns", [])) or "—"

    return f"""# {meta["titulo"]}

| Campo | Valor |
|-------|-------|
| **Slug** | `{slug}` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) |
| **Página oficial** | {meta.get("page", "—")} |
| **Unidade ANP** | {meta.get("unidade_anp", "—")} |
| **Periodicidade** | {meta.get("periodicidade", "—")} |
| **Formato** | {meta.get("formato", "—")} |
| **Fonte** | {meta.get("fonte", "—")} |
| **Pasta local** | `data/raw/{slug}/` |
| **Encoding** | {enc} |
| **Separador** | `{sep}` |
| **Chaves** | `{keys}` |

## Contexto

> Consultar [docs/conjuntos/{slug}.md](conjuntos/{slug}.md) para detalhes completos.

## Cruzamentos sugeridos

{cruz}
"""


def main() -> None:
    cfg = load_datasets()
    OUT.mkdir(parents=True, exist_ok=True)

    generated = 0
    for slug, meta in cfg["datasets"].items():
        path = OUT / f"{slug}.md"
        if path.exists():
            continue
        path.write_text(render(slug, meta), encoding="utf-8")
        print(f"created {path.name}")
        generated += 1

    print(f"\n{generated} novos docs gerados ({len(cfg['datasets'])} totais no yaml)")


if __name__ == "__main__":
    main()
