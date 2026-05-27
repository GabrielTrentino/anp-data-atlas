"""Valida coerência entre config/datasets.yaml e docs/conjuntos/*.md.

Verificações:
1. Todo slug em datasets.yaml tem um docs/conjuntos/{slug}.md correspondente
2. Todo doc tem seções obrigatórias (Inventário empírico, Qualidade e chaves)
3. Links internos entre docs não estão quebrados
4. Todo doc referenciado em conjuntos/ existe no yaml
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "datasets.yaml"
DOCS_DIR = ROOT / "docs" / "conjuntos"

REQUIRED_SECTIONS = [
    "Inventário empírico dos brutos",
    "Qualidade e chaves",
]


def load_config() -> dict:
    with open(CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_missing_docs(slugs: set[str]) -> list[str]:
    """Verifica se todo slug tem doc correspondente."""
    errors = []
    for slug in sorted(slugs):
        doc = DOCS_DIR / f"{slug}.md"
        if not doc.exists():
            errors.append(f"FALTA DOC: {slug} (esperado em docs/conjuntos/{slug}.md)")
    return errors


def check_orphan_docs(slugs: set[str], indisponiveis: set[str]) -> list[str]:
    """Verifica se todo doc corresponde a um slug no yaml."""
    errors = []
    all_known = slugs | indisponiveis
    for doc in sorted(DOCS_DIR.glob("*.md")):
        slug = doc.stem
        if slug not in all_known:
            errors.append(f"DOC ORFÃO: {doc.name} não tem entrada no datasets.yaml")
    return errors


def check_sections(slugs: set[str]) -> list[str]:
    """Verifica seções obrigatórias nos docs."""
    errors = []
    for slug in sorted(slugs):
        doc = DOCS_DIR / f"{slug}.md"
        if not doc.exists():
            continue
        content = doc.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in content:
                errors.append(f"SEÇÃO AUSENTE: '{section}' em {doc.name}")
    return errors


def check_internal_links(slugs: set[str], indisponiveis: set[str]) -> list[str]:
    """Verifica links internos (slug.md) que apontam para docs inexistentes."""
    errors = []
    all_known = slugs | indisponiveis
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")

    for doc in sorted(DOCS_DIR.glob("*.md")):
        content = doc.read_text(encoding="utf-8")
        for match in link_pattern.finditer(content):
            target = match.group(2)
            if target.startswith("http"):
                continue
            target_name = Path(target).name
            if target_name.endswith(".md"):
                target_slug = target_name[:-3]
                if target_slug in all_known:
                    target_path = DOCS_DIR / target_name
                elif target_name in ("dados-abertos.md", "inventario-dados.md",
                                     "variaveis-conjuntos.md", "anomalias-conhecidas.md",
                                     "README.md"):
                    target_path = ROOT / "docs" / target_name
                else:
                    target_path = DOCS_DIR / target_name

                if not target_path.exists():
                    # Check relative to doc's parent
                    alt = doc.parent / target
                    if not alt.exists():
                        errors.append(f"LINK QUEBRADO: {doc.name} -> {target}")
    return errors


def main() -> None:
    cfg = load_config()
    slugs = set(cfg["datasets"].keys())
    indisponiveis = set(cfg.get("indisponiveis", {}).keys())

    all_errors: list[str] = []
    all_errors.extend(check_missing_docs(slugs))
    all_errors.extend(check_orphan_docs(slugs, indisponiveis))
    all_errors.extend(check_sections(slugs))
    all_errors.extend(check_internal_links(slugs, indisponiveis))

    if all_errors:
        print(f"\n{'='*60}")
        print(f"VALIDAÇÃO: {len(all_errors)} problema(s) encontrado(s)\n")
        for err in all_errors:
            print(f"  ! {err}")
        print(f"\n{'='*60}")
        sys.exit(1)
    else:
        print(f"OK - Validacao OK: {len(slugs)} datasets, {len(list(DOCS_DIR.glob('*.md')))} docs, sem erros.")
        sys.exit(0)


if __name__ == "__main__":
    main()
