# Movimentação de derivados de petróleo, gás natural e biocombustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `movimentacao-derivados` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#21) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo |
| **Unidade ANP (inventário)** | SDL |
| **Periodicidade** | Mensal |
| **Formato** | ZIP por produto → CSV dentro de cada ZIP |
| **Fonte operacional** | SIMP — Resolução ANP nº 729/2018 |
| **Pasta local** | `data/raw/movimentacao-derivados/` |
| **Inventário ANP** | Movimentação de Derivados… (várias sub-bases por produto) |
| **Prioridade fuel-analytics** | Sim — [TODO.md](../../TODO.md) |
| **Estudo ativo** | [anp-fuel-analytics — movimentacao-derivados](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/movimentacao-derivados/) |

## Contexto

Divulga **volumes movimentados** pelos agentes regulados no SIMP, segmentados por **família de produto** (combustíveis líquidos, GLP, lubrificantes, TRR, aviação, etc.), com proteção de informações sigilosas conforme a resolução. Complementa [tancagem-abastecimento](tancagem-abastecimento.md) (capacidade autorizada) com **fluxo real** de derivados.

## Metadados oficiais

| Documento | URL |
|-----------|-----|
| Metadado unificado (logística / SIMP) | [metadado-unificado-logistica.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/mdpg/metadado-unificado-logistica.pdf) |

Cópia local após download: `data/raw/movimentacao-derivados/metadado-unificado-logistica.pdf`

## Estrutura dos arquivos (portal)

Base dos links: `.../dados-abertos/arquivos/mdpg/{arquivo}`

| ZIP / PDF | Pasta local | Conteúdo |
|-----------|-------------|----------|
| `liquidos.zip` | `liquidos/` | Combustíveis líquidos — vendas, entregas, importação |
| `glp.zip` | `glp/` | GLP |
| `lubrificante.zip` | `lubrificante/` | Lubrificantes (Anexos A–J) |
| `trr.zip` | `trr/` | TRR |
| `aviacao.zip` | `aviacao/` | Combustíveis de aviação |
| `asfalto.zip` | `asfalto/` | Asfaltos |
| `solvente.zip` | `solvente/` | Solventes |
| `fornecedores-vendas-diretas.zip` | `fornecedores-vendas-diretas/` | Etanol — venda direta |
| `movimentacaologistica.zip` | `movimentacaologistica/` | Logística agregada (3 CSVs, desde 2022) |
| `metadado-unificado-logistica.pdf` | raiz | Metadados |

**Encoding:** `latin-1` (confirmado). **Separador:** `;` (ponto e vírgula) na maioria dos CSVs SIMP — incluindo `Liquidos_Vendas_Atual.csv`.

### Padrões de tabela SIMP (por produto)

Três famílias recorrentes dentro de cada ZIP:

| Tipo | Sufixo no nome | Granularidade típica |
|------|----------------|----------------------|
| **Vendas atual** | `*_Vendas_Atual.csv` | Agente × produto × origem/destino × mês |
| **Vendas histórico** | `*_Vendas_Historico.csv` | Idem, série até 2023-12 |
| **Vendas por UF** | `*_UF_Atual.csv` | Agregado por UF origem/destino |
| **Entregas** | `*_Entregas_*.csv` | Fluxo fornecedor ↔ distribuidor |
| **Anexos lubrificante** | `Lubrificante_Anexo_*.csv` | Layout específico por anexo |

### Amostra inspecionada — `liquidos/Liquidos_Vendas_Atual.csv`

- **Linhas:** ~1,0 M (1.001.125 na extração 2026-05-24)
- **Período:** 2017-01 – 2026-04
- **Granularidade:** agente regulado × produto × região/UF origem e destino × mercado destinatário × mês

| Coluna | Descrição |
|--------|-----------|
| `Ano` | Ano de referência |
| `Mês` | Mês de referência |
| `Agente Regulado` | Razão social do agente ( **não** é CNPJ) |
| `Código do Produto` | Código SIMP do produto |
| `Nome do Produto` | Descrição do produto |
| `Descrição do Produto` | Detalhe adicional |
| `Região Origem` / `UF Origem` | Origem geográfica |
| `Região Destinatário` / `UF Destino` | Destino geográfico |
| `Mercado Destinatário` | Segmento de mercado |
| `Quantidade de Produto (mil m³)` | Volume movimentado (**mil m³**) |

### Logística agregada — `movimentacaologistica/`

Três arquivos com recorte **mensal desde 2022/01** (visão macro, sem agente por linha em alguns casos):

| Arquivo | Colunas principais |
|---------|-------------------|
| LOGISTICA 01 — Abastecimento nacional | `Período`, `UF Origem`, `UF Destino`, `Produto`, `Classificação`, `Sub Classificação`, `Operação`, `Modal`, `Qtd Produto Líquido` |
| LOGISTICA 02 — Vendas mercado BR | `Período`, `UF Destino`, `Produto`, `Vendedor`, `Qtd Produto Líquido` |
| LOGISTICA 03 — Vendas congêneres | `Período`, `Produto`, `UF Origem`, `UF Destino`, `Vendedor`, `Comprador`, `Qtd Produto Líquido` |

> **Unidade logística:** validar no PDF — soma bruta de `Qtd Produto Líquido` sugere **litros**, não mil m³.

## Inventário empírico dos brutos

Extração **2026-05-24** — **47 CSVs** após download dos 9 ZIPs ([fuel-analytics](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/movimentacao-derivados/)).

| Arquivo local | Linhas | Col. volume | Período | Notas |
|---------------|-------:|-------------|---------|-------|
| `liquidos/Liquidos_Vendas_Atual.csv` | 1.001.125 | mil m³ | 2017-01 – 2026-04 | amostra principal downstream |
| `liquidos/Liquidos_Entregas_Historico.csv` | 564.014 | mil m³ | 2007-01 – 2023-12 | |
| `liquidos/Liquidos_Vendas_Historico_2007_a_2017.csv` | 710.831 | — | — | **sem cabeçalho** |
| `glp/GLP_Vendas_Historico.csv` | 342.522 | mil ton | 2007-01 – 2023-12 | |
| `lubrificante/Lubrificante_Anexo_B.csv` | 62.131 | Volume(L) | 2015-10 – 2026-04 | traz `Código do Regulado - ANP` |
| `movimentacaologistica/DADOS ABERTOS - LOGISTICA 01 - …` | 211.913 | Qtd Líquido | 2022/01 – 2026/04 | agregado nacional |
| _+ 41 arquivos_ | | | | tabela completa no estudo fuel |

Regenerar inventário:

```bash
py estudos/movimentacao-derivados/export_inventario_raw.py
```

### Histórico líquidos sem cabeçalho

`liquidos/Liquidos_Vendas_Historico_2007_a_2017.csv` — 11 campos separados por `;`, **sem linha de cabeçalho**. Versão normalizada no fuel-analytics:

`liquidos/Liquidos_Vendas_Historico_2007_a_2017_normalizado.csv` (UTF-8, vírgula) — gerada por `prepare_movimentacao_raw.py`.

## Cruzamento com tancagem (empírico)

Script: [cruzamento_tancagem.py](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/movimentacao-derivados/scripts/cruzamento_tancagem.py) — amostra `Liquidos_Vendas_Atual` × `tancagem.parquet`.

| Métrica | Valor |
|---------|------:|
| Agentes únicos movimentação (nome + UF origem) | 701 |
| Empresas únicas tancagem (nome + UF instalação) | 1.550 |
| **Match exato nome + UF** | 213 (**30,4%** dos agentes mov) |
| Match só por nome (ignora UF) | 122 / 214 nomes (**57%**) |

**Conclusão:** join direto por `CodInstalacao` **não existe** nesta base. Cruzamento operacional provável via **nome normalizado** (fuzzy) ou **cadastro revendas** (CNPJ). UF origem (movimentação) ≠ UF da instalação (tancagem) — explica match moderado.

## Camada trusted (MVP)

No fuel-analytics:

```bash
py pipelines/run.py movimentacao-derivados raw_prepare
py pipelines/run.py movimentacao-derivados trusted_liquidos
```

Saída: `data/trusted/movimentacao-derivados/liquidos_vendas_atual.parquet` (~1M linhas, 2017-01 – 2026-04).

Colunas: `ano`, `mes`, `agente_regulado`, `codigo_produto`, `nome_produto`, `uf_origem`, `uf_destino`, `volume_mil_m3`, `produto_familia`, `tipo_tabela`, `_source_file`.

## Qualidade e chaves

### Chaves observadas (≠ tancagem)

Os CSVs SIMP de movimentação **não expõem** `Cnpj` nem `CodInstalacao` (presentes na [tancagem](tancagem-abastecimento.md)). Ligação com outros conjuntos:

| Chave | Onde | Cruzamento |
|-------|------|------------|
| `Agente Regulado` | Vendas/entregas | Nome ↔ `NomeEmpresarial` (tancagem) — **match fuzzy** |
| `Código do Regulado - ANP` | Lubrificante Anexo B | Código interno ANP — mapear com cadastro |
| `Código Agente Regulado` | Venda direta etanol | Idem |
| `Ano` + `Mês` / `Período` | Todas | Série temporal |
| `Código do Produto` + `Nome do Produto` | Todas | Mix de produtos |
| `UF Origem` / `UF Destino` | Vendas, logística | Geo agregada ↔ vendas-derivados, preços LPC |

### Chave lógica candidata (vendas atual — líquidos)

Granularidade da fonte: **uma linha por** `Ano` × `Mês` × `Agente Regulado` × `Código do Produto` × origem/destino × `Mercado Destinatário`.

### Armadilhas conhecidas

| Item | Detalhe |
|------|---------|
| Separador `;` | Obrigatório `delim=';'` na leitura (DuckDB/pandas) |
| Histórico 2007–2017 líquidos | Sem header — usar arquivo `*_normalizado.csv` |
| Unidades mistas | mil m³ · mil ton · litros — **não somar** entre famílias |
| Tabelas `_Atual` vs `_Historico` | Overlap em 2023–2024 — evitar dupla contagem |
| Sigilo SIMP | Volumes agregados; agentes pequenos podem estar suprimidos |

## Cruzamentos sugeridos

- [tancagem-abastecimento](tancagem-abastecimento.md) — capacidade vs fluxo (via nome agente + UF, não `CodInstalacao` direto)
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md) — CNPJ ↔ razão social
- [vendas-derivados](vendas-derivados.md) — demanda agregada por UF/produto
- [serie-historica-precos](serie-historica-precos.md) — contexto de preço regional

## Sugestões de análises

Métrica base recomendada: **soma de `volume_mil_m3`** (líquidos) ou coluna de quantidade da família de produto — **nunca somar** mil m³ com litros ou mil ton sem conversão. Granularidade típica: **agente × produto × origem/destino × mês**.

### Visão nacional e evolução histórica

- **Volume total movimentado** por mês (líquidos, GLP, TRR…) — série desde 2007 (histórico) ou 2017+ (vendas atual).
- **Mix de produtos** — participação de gasolina C, diesel, etanol, GLP etc. no volume (`Código do Produto` / `Nome do Produto`).
- **Sazonalidade** — picos em colheita (etanol), inverno (GLP), mudanças regulatórias SIMP.
- **Ruptura 2017** — comparar `Liquidos_Vendas_Historico_2007_a_2017` normalizado vs `Liquidos_Vendas_Atual` no overlap.
- **Atual vs histórico** — evitar dupla contagem onde `_Atual` e `_Historico` coexistem (2023–2024).

### Agentes e mercado

- **Ranking de agentes** (`Agente Regulado`) por volume total e por produto.
- **Concentração** — share top 5 / top 10 distribuidores; índice HHI por produto.
- **Entrada e saída de players** — agentes que somem ou surgem entre anos.
- **Match com tancagem** — expandir [cruzamento tancagem](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/movimentacao-derivados/cruzamento_tancagem_resultado.md): fuzzy name, CNPJ após cadastro revendas.

### Geografia: fluxos e mercados

- **Matriz origem–destino** — `UF Origem` × `UF Destino` por produto (sankey ou heatmap).
- **Mercado destinatário** — peso de consumidor final, revenda, industrial etc. (`Mercado Destinatário`).
- **Região vs UF** — quando só houver `Região Origem`/`Destinatário`, mapear para UF.
- **Importação por distribuidor** — `Liquidos_Importacao_de_Distribuidores.csv` por UF e produto.

### Recortes por família de produto

- **Combustíveis líquidos** — vendas, entregas fornecedor/distribuidor, importação (6 CSVs).
- **GLP** — toneladas vs m³; comparar com cadastro revendas GLP.
- **TRR e bases** — volume por segmento TRR; cruzar com tancagem segmento TRR.
- **Lubrificantes** — Anexos A–J; usar `Código do Regulado - ANP` para join cadastral.
- **Logística agregada** — 3 CSVs desde 2022: abastecimento nacional, mercado BR, congêneres (validar unidade litros).

### Cruzamentos com outros conjuntos

- **Tancagem** — razão volume movimentado / capacidade autorizada (m³) por agente+UF após join por nome.
- **Cadastro revendas** — CNPJ como chave mestra; postos por município vs fluxo destino.
- **Vendas derivados (SDC)** — comparar demanda estatística vs movimentação SIMP por UF/produto/mês.
- **Série histórica de preços** — volume regional vs `PrecoMedio` (correlação exploratória).
- **Capacidade terminais** — fluxo costeiro vs movimentação terminais aquaviários (quando explorado).

### Qualidade e método (antes de publicar resultados)

- Forçar **`delim=';'`** em toda leitura; encoding `latin-1`.
- Harmonizar **unidades** por família (mil m³, mil ton, L) na camada trusted.
- Tratar **sigilo SIMP** — volumes zero ou ausência de agente pequeno.
- Documentar que movimentação é **fluxo reportado**, não estoque (complementa tancagem).
- Expandir trusted além de `liquidos_vendas_atual` antes de painéis multi-produto.

## Uso neste atlas

**Status da exploração:** download raw, inventário (47 CSVs), schema amostral, **cruzamento com tancagem**, histórico normalizado, trusted MVP (`liquidos_vendas_atual.parquet`). Demais produtos e refined **pendentes**.

**Próximos passos (fuel-analytics):**

1. Executar análises priorizadas em [TODO do estudo](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/movimentacao-derivados/TODO.md#próximas-análises)
2. `cadastro-revendas-combustiveis` — CNPJ para join confiável
3. Expandir trusted para GLP, TRR, logística
4. Validar overlap 2017 histórico vs vendas atual
