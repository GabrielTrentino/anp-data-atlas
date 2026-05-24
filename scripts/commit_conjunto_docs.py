"""Commits incrementais: doc atlas + TODO + dados-abertos por slug."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from _conjuntos_fuel_metadata import CONJUNTOS_FUEL

ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "TODO.md"
DADOS = ROOT / "docs" / "dados-abertos.md"


def update_todo(slug: str) -> None:
    text = TODO.read_text(encoding="utf-8")
    pattern = rf"(\| \d+ \| `{re.escape(slug)}` \|[^|]+\|) — (\|)"
    new_text, n = re.subn(pattern, r"\1 ✓ \2", text, count=1)
    if n != 1:
        raise RuntimeError(f"TODO not updated for {slug}")
    TODO.write_text(new_text, encoding="utf-8")


def update_dados(num: int, slug: str) -> None:
    text = DADOS.read_text(encoding="utf-8")
    pattern = rf"(\| {num} \| [^|]+ \| `{re.escape(slug)}` \|) \s*(\|)"
    link = f"[doc](conjuntos/{slug}.md)"
    new_text, n = re.subn(pattern, rf"\1 {link} \2", text, count=1)
    if n != 1:
        raise RuntimeError(f"dados-abertos not updated for #{num} {slug}")
    DADOS.write_text(new_text, encoding="utf-8")


def git_commit(slug: str, title: str, num: int) -> None:
    subprocess.run(
        [
            "git",
            "add",
            f"docs/conjuntos/{slug}.md",
            "TODO.md",
            "docs/dados-abertos.md",
        ],
        cwd=ROOT,
        check=True,
    )
    msg = f"Doc atlas: {slug} (#{num}) — referencia para fuel-analytics.\n\nDocumentacao de referencia do conjunto {title}."
    subprocess.run(["git", "commit", "-m", msg], cwd=ROOT, check=True)


def main() -> None:
    for c in CONJUNTOS_FUEL:
        slug = c["slug"]
        if not (ROOT / "docs" / "conjuntos" / f"{slug}.md").exists():
            raise FileNotFoundError(slug)
        update_todo(slug)
        update_dados(c["num"], slug)
        git_commit(slug, c["title"], c["num"])
        print("committed", slug)


if __name__ == "__main__":
    main()
