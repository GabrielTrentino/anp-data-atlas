"""Download raw samples from ANP portal for all configured datasets.

Reads dataset configuration from config/datasets.yaml.
Probes each dataset page, extracts CSV/XLSX links, and downloads samples.
"""
from __future__ import annotations

import re
import urllib.request
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
RAW = REPO / "data" / "raw"
CONFIG_PATH = REPO / "config" / "datasets.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def fetch_page(url: str, user_agent: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERRO pagina: {e}")
        return None


def extract_links(html: str) -> list[str]:
    """Extract CSV, XLSX, ZIP, PDF links from page HTML."""
    pattern = r'href="([^"]+\.(?:csv|xlsx|xls|zip|pdf|shp|json))"'
    links = re.findall(pattern, html, re.IGNORECASE)
    seen: set[str] = set()
    result: list[str] = []
    for link in links:
        if link not in seen:
            seen.add(link)
            result.append(link)
    return result


def download_file(url: str, dest: Path, user_agent: str) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            dest.write_bytes(resp.read())
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def process_dataset(
    slug: str, page_path: str, base_url: str, user_agent: str, max_files: int
) -> tuple[int, int]:
    url = f"{base_url}/{page_path}"
    print(f"\n{'='*60}")
    print(f"[{slug}] -> {url}")

    html = fetch_page(url, user_agent)
    if not html:
        return 0, 1

    links = extract_links(html)
    if not links:
        print("  Nenhum link CSV/XLSX/ZIP encontrado na pagina")
        return 0, 0

    print(f"  {len(links)} links encontrados")
    dest_dir = RAW / slug
    ok, fail = 0, 0

    for link in links[:max_files]:
        if link.startswith("/"):
            full_url = f"https://www.gov.br{link}"
        elif link.startswith("http"):
            full_url = link
        else:
            full_url = f"{url}/{link}"

        filename = link.split("/")[-1].split("?")[0]
        dest = dest_dir / filename

        print(f"  get {filename}")
        if download_file(full_url, dest, user_agent):
            ok += 1
        else:
            fail += 1

    print(f"  -> {ok} ok, {fail} falhas")
    return ok, fail


def main() -> None:
    cfg = load_config()
    base_url = cfg["base_url"]
    user_agent = cfg["user_agent"]
    max_files = cfg.get("max_files_per_dataset", 20)

    total_ok, total_fail = 0, 0
    results: dict[str, tuple[int, int]] = {}

    for slug, meta in cfg["datasets"].items():
        ok, fail = process_dataset(slug, meta["page"], base_url, user_agent, max_files)
        results[slug] = (ok, fail)
        total_ok += ok
        total_fail += fail

    print(f"\n{'='*60}")
    print(f"RESUMO: {total_ok} arquivos baixados, {total_fail} falhas")
    print(f"\nPor dataset:")
    for slug, (ok, fail) in results.items():
        status = "OK" if ok > 0 else ("VAZIO" if fail == 0 else "ERRO")
        print(f"  {slug:45s} {ok:3d} ok  {fail:2d} fail  [{status}]")


if __name__ == "__main__":
    main()
