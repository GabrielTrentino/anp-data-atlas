"""Download raw samples from ANP portal for all 22 pending datasets.

Probes each dataset page, extracts CSV/XLSX links, and downloads samples.
"""
from __future__ import annotations

import os
import re
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RAW = REPO / "data" / "raw"
USER_AGENT = "Mozilla/5.0 (anp-data-atlas; research)"
BASE = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos"

DATASETS: dict[str, str] = {
    # E&P
    "dados-ep": "dados-de-e-p",
    "fase-exploracao": "fase-de-exploracao",
    "fase-desenvolvimento-producao": "fase-de-desenvolvimento-e-producao",
    "blocos-fase-exploratoria-encerrada": "blocos-com-fase-exploratoria-encerrada",
    "incidentes-ep": "incidentes-de-exploracao-e-producao-de-petroleo-e-gas-natural",
    "resultado-poco": "resultado-de-poco",
    "previsao-atividades-investimentos": "previsao-de-atividades-e-investimentos-exploratorios",
    "relacao-concessionarios": "relacao-de-concessionarios",
    "rodadas-licitacoes": "rodadas-de-licitacoes-de-petroleo-e-gas-natural",
    # Gas natural
    "autorizacoes-gas-natural": "autorizacoes-de-gas-natural",
    "comercializacao-gas-natural": "comercializacao-de-gas-natural",
    "movimentacao-gas-gasodutos": "movimentacao-de-gas-natural-em-gasodutos-de-transporte",
    # Acervo
    "acervo-dados-tecnicos": "acervo-de-dados-tecnicos",
    "amostras-rochas-fluidos": "amostras-de-rochas-e-fluidos",
    "aquisicao-processamento-estudo-dados": "aquisicao-processamento-e-estudo-de-dados",
    "bacias-sedimentares": "dados-georreferenciados-das-bacias-sedimentares-brasileiras",
    # Regulacao
    "aditamento-conteudo-local": "aditamento-de-conteudo-local",
    "fiscalizacao-conteudo-local": "fiscalizacao-de-conteudo-local",
    "multas-2016": "multas-aplicadas-com-vencimento-a-partir-de-2016",
    "participacoes-governamentais": "participacoes-governamentais",
    "pesquisa-desenvolvimento-inovacao": "pesquisa-desenvolvimento-e-inovacao",
    "prestadores-apoio-administrativo": "prestadores-de-servico-de-apoio-administrativo",
}


def fetch_page(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
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
    seen = set()
    result = []
    for link in links:
        if link not in seen:
            seen.add(link)
            result.append(link)
    return result


def download_file(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            dest.write_bytes(resp.read())
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def process_dataset(slug: str, page_path: str) -> tuple[int, int]:
    url = f"{BASE}/{page_path}"
    print(f"\n{'='*60}")
    print(f"[{slug}] -> {url}")

    html = fetch_page(url)
    if not html:
        return 0, 1

    links = extract_links(html)
    if not links:
        print("  Nenhum link CSV/XLSX/ZIP encontrado na pagina")
        return 0, 0

    print(f"  {len(links)} links encontrados")
    dest_dir = RAW / slug
    ok, fail = 0, 0

    for link in links[:20]:  # limit to 20 files per dataset
        if link.startswith("/"):
            full_url = f"https://www.gov.br{link}"
        elif link.startswith("http"):
            full_url = link
        else:
            full_url = f"{url}/{link}"

        filename = link.split("/")[-1].split("?")[0]
        dest = dest_dir / filename

        print(f"  get {filename}")
        if download_file(full_url, dest):
            ok += 1
        else:
            fail += 1

    print(f"  -> {ok} ok, {fail} falhas")
    return ok, fail


def main() -> None:
    total_ok, total_fail = 0, 0
    results: dict[str, tuple[int, int]] = {}

    for slug, page_path in DATASETS.items():
        ok, fail = process_dataset(slug, page_path)
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
