# Tancagem do Abastecimento Nacional de Combustíveis

| Campo | Valor |
|-------|-------|
| **Slug** | `tancagem-abastecimento` |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/tancagem-do-abastecimento-nacional-de-combustiveis |
| **Publicado** | 03/06/2022 |
| **Atualizado no portal** | 04/05/2026 |
| **Título oficial** | Tancagem Autorizada a Operar |
| **Formato** | CSV (dados abertos) · PDF (metadados) |
| **Fonte operacional** | [SIMP](https://www.gov.br/anp/pt-br/assuntos/distribuicao-revenda/simp-sistema-de-informacoes-de-movimentacoes-de-produtos) |
| **Frequência** | Mensal |
| **Idioma** | Português |
| **Contato** | faleconosco@anp.gov.br |
| **Pasta local** | `data/raw/tancagem-abastecimento/` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#41) |

## Contexto

**Tancagem** é a **capacidade de armazenagem** (em m³) das unidades — tanques, vasos de pressão ou esferas — cadastradas nas instalações autorizadas pela ANP. O dado informa quanto volume a instalação está autorizada a operar, não o estoque físico nem o nível de ocupação no momento.

Dados públicos sobre essas **instalações com tancagem autorizadas a operar** (definição do [metadados-tancagem.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/metadados-tancagem.pdf)). O painel dinâmico **Tancagem Autorizada a Operar** (Power BI) apresenta essa capacidade por tipo de instalação, empresa, grupo de produto e localidade.

**Painel dinâmico (catálogo origem):** https://www.gov.br/anp/pt-br/centrais-de-conteudo/paineis-dinamicos-da-anp/painel-dinamico-da-tancagem-do-abastecimento-nacional-de-combustiveis

**Palavras-chave (ANP):** tancagem, tanque, instalação, segmento, grupo de produtos, localização, combustíveis, armazenamento, derivados de petróleo, GLP, petróleo.

No menu da ANP, o tema aparece ligado a **Dados de estoques de combustíveis** e **Distribuição e Revenda**.

## Metadados oficiais

Documento consultado: [metadados-tancagem.pdf](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/metadados-tancagem.pdf) (cópia local em `data/raw/tancagem-abastecimento/metadados-tancagem.pdf`).

| Campo | Valor |
|-------|-------|
| Título | Tancagem Autorizada a Operar |
| Descrição | Dados sobre instalações com tancagem autorizadas a operar; visualização interativa no painel dinâmico homônimo |
| Órgão responsável | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) |
| Fonte do dado | Sistema de Informações de Movimentação de Produtos — SIMP |
| Formato do arquivo | CSV |
| Frequência de atualização | Mensal |
| Idioma | Português |
| Contato | faleconosco@anp.gov.br |

## Estrutura dos arquivos (CSV)

**Padrão de URL** (a partir de 2023):

```
.../arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/{ano}/{arquivo}.csv
```

Cada arquivo cobre um **recorte temporal** (mês ou intervalo de meses). A coluna `Data` é a **data de disponibilização** do dado aberto na página da ANP (`AAAA-MM-DD`), não necessariamente o “mês de estoque” — usar o nome do arquivo e valores distintos de `Data` ao montar séries temporais.

### Amostra inspecionada (`2026/janeiro.csv`)

- **Linhas de dados:** ~14,5 mil (1 cabeçalho + registros por tanque/unidade)
- **Encoding:** UTF-8
- **Separador:** vírgula
- **Granularidade:** uma linha por combinação de instalação × tanque (`Tag`) × grupo de produto, com capacidade em m³

| Coluna | Tipo (ANP) | Descrição oficial | Exemplo |
|--------|------------|-------------------|---------|
| `Data` | Data | Data de disponibilização dos dados abertos na página da ANP (`AAAA-MM-DD`) | `2026-01-31` |
| `NomeEmpresarial` | Texto | Nome registrado da PJ autorizada a operar as instalações com tancagem | `2 IRMAOS PRODUTOS DE PETROLEO LTDA` |
| `Uf` | Texto | Sigla da UF onde a instalação está estabelecida | `SP` |
| `Municipio` | Texto | Município da instalação | `CAMPINAS` |
| `Cnpj` | Texto | CNPJ da empresa autorizada (no CSV aparece sem máscara) | `43544287000123` |
| `CodInstalacao` | Número | Código de instalação i-SIMP — sequência de sete algarismos | `1066748` |
| `Segmento` | Texto | Atividade econômica integrante da indústria de petróleo, gás e biocombustíveis | `BASES DO RAMO DE TRR` |
| `DetalheInstalacao` | Texto | Detalhe relevante do segmento em que a instalação atua | `EXCLUSIVA` |
| `Tag` | Texto | Rótulo (numérico ou alfanumérico) da unidade cadastrada no SIMP | `TQ 01` |
| `TipoDaUnidade` | Texto | Recipiente de armazenagem > 230 L, instalação fixa, não industrial: `TANQUE`, `VASO DE PRESSÃO` ou `ESFERA` | `TANQUE` |
| `GrupoDeProdutos` | Texto | `DERIVADOS E BIOCOMBUSTÍVEIS`, `GLP`, `PETRÓLEO`, `OUTROS` | `DERIVADOS E BIOCOMBUSTÍVEIS` |
| `TancagemM3` | Número | Capacidade operacional total das unidades (m³), arredondada para inteiro; sem vírgula nem separador de milhares | `20` |

## Arquivos disponíveis no portal

Base dos links: `.../arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/{ano}/`

| Mês | 2022 | 2023 | 2024 | 2025 | 2026 |
|-----|------|------|------|------|------|
| Janeiro | — | [janeiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/janeiro.csv) | [janeiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/janeiro.csv) | [janeiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/janeiro.csv) | [janeiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2026/janeiro.csv) |
| Fevereiro | — | [fevereiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/fevereiro.csv) | [fevereiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/fevereiro.csv) | [fevereiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/fevereiro.csv) | [fevereiro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2026/fevereiro.csv) |
| Março | — | [marco.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/marco.csv) | [marco-julho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/marco-julho.csv) † | [marco.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/marco.csv) | [marco.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2026/marco.csv) |
| Abril | — | [abril.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/abril.csv) | [marco-julho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/marco-julho.csv) † | — ‡ | [abril.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2026/abril.csv) |
| Maio | — | [maio.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/maio.csv) | [marco-julho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/marco-julho.csv) † | [maio-junho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/maio-junho.csv) † | — |
| Junho | [junho_2022.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_junho_2022.csv) § | [junho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/junho.csv) | [marco-julho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/marco-julho.csv) † | [maio-junho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/maio-junho.csv) † | — |
| Julho | [julho_2022.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_julho_2022.csv) § | sem link ¶ | [marco-julho.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/marco-julho.csv) † | [julho-agosto.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/julho-agosto.csv) † | — |
| Agosto | [v1.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_v1.csv) § | [agosto.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/agosto.csv) | [agosto.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/agosto.csv) | [julho-agosto.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/julho-agosto.csv) † | — |
| Setembro | [2022_09_01.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_2022_09_01.csv) § | [setembro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/setembro.csv) | [setembro-outubro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/setembro-outubro.csv) † | [set.-nov.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/setembro-a-novembro.csv) † | — |
| Outubro | [out_2022.xlsx](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_outubro_2022-csv.xlsx) § | [outubro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/outubro.csv) | [setembro-outubro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/setembro-outubro.csv) † | [set.-nov.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/setembro-a-novembro.csv) † | — |
| Novembro | [nov_2022.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_novembro_2022.csv) § | [novembro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/novembro.csv) | [novembro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/novembro.csv) | [set.-nov.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/setembro-a-novembro.csv) † | — |
| Dezembro | [dez_2022.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2022/tancagem_terminais_dados_abertos_dezembro_2022.csv) § | [dezembro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2023/dezembro.csv) | [dezembro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2024/dezembro.csv) | [dezembro.csv](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2025/dezembro.csv) | — |

**Legenda:** `—` = sem publicação naquele mês/ano · † = mesmo arquivo cobre vários meses (bloco) · ‡ = abril/2025 ausente no portal · ¶ = julho/2023 citado na página, sem hyperlink · § = 2022: série inicia em junho; nomes de arquivo originais abreviados no rótulo do link (ver URLs completas)

## Periodicidade e lacunas

- **Desde jun/2022:** publicação mensal ou em **blocos** (células repetidas com o mesmo link na tabela acima).
- **2026:** publicação até abril; demais meses ainda sem arquivo no portal.
- Validar schema dos arquivos de 2022 (especialmente outubro em `.xlsx`) antes de concatenar séries históricas.

## Inventário empírico dos brutos

> **Status:** preenchido — medição local em **22/05/2026** (CSVs em `anp-fuel-analytics/data/raw/tancagem-abastecimento/`).

Complementa a [matriz do portal](#arquivos-disponíveis-no-portal) com o que foi **medido** após download. **36 arquivos CSV** · **492.412 linhas** no total empilhado · soma bruta ~**1.972 M m³** (soma por snapshot — **não** é série mensal deduplicada).

| Arquivo local | Linhas | Soma m³ | `Data` (min – max) | Notas |
|---------------|-------:|--------:|--------------------|-------|
| `2022/tancagem_terminais_dados_abertos_2022_09_01.csv` | 13.468 | 57.99 M | 2022-09-01 – 2022-09-01 | encoding latin-1; nome set/2022 |
| `2022/tancagem_terminais_dados_abertos_dezembro_2022.csv` | 10.302 | 32.15 M | 2022-12-01 – 2022-12-01 | anomalia ~−44% m³ vs jun–out/2022 |
| `2022/tancagem_terminais_dados_abertos_julho_2022.csv` | 13.442 | 57.95 M | 2022-07-01 – 2022-07-01 | |
| `2022/tancagem_terminais_dados_abertos_junho_2022.csv` | 13.362 | 57.78 M | 2022-06-01 – 2022-06-01 | |
| `2022/tancagem_terminais_dados_abertos_novembro_2022.csv` | 10.352 | 32.27 M | 2022-11-01 – 2022-11-01 | anomalia ~−44% m³ vs jun–out/2022 |
| `2022/tancagem_terminais_dados_abertos_outubro_2022-csv.csv` | 13.468 | 58.07 M | 2022-10-03 – 2022-10-03 | derivado de XLSX (`raw_prepare`) |
| `2022/tancagem_terminais_dados_abertos_v1.csv` | 13.473 | 58.07 M | 2022-08-01 – 2022-08-01 | |
| `2023/abril.csv` | 13.474 | 55.91 M | 2023-04-01 – 2023-04-01 | |
| `2023/agosto.csv` | 13.558 | 56.22 M | 2023-08-01 – 2023-08-01 | |
| `2023/dezembro.csv` | 13.705 | 56.66 M | 2023-12-04 – 2023-12-04 | |
| `2023/fevereiro.csv` | 13.434 | 56.11 M | 2023-02-01 – 2023-02-01 | |
| `2023/janeiro.csv` | 13.571 | 55.97 M | 2023-01-02 – 2023-01-02 | |
| `2023/junho.csv` | 13.478 | 55.89 M | 2023-06-01 – 2023-06-01 | |
| `2023/maio.csv` | 13.500 | 55.97 M | 2023-05-01 – 2023-05-01 | |
| `2023/marco.csv` | 13.419 | 55.86 M | 2023-03-01 – 2023-03-01 | |
| `2023/novembro.csv` | 13.705 | 56.66 M | 2023-12-04 – 2023-12-04 | idêntico a dez/2023 |
| `2023/outubro.csv` | 13.705 | 56.66 M | 2023-12-04 – 2023-12-04 | idêntico a dez/2023 |
| `2023/setembro.csv` | 13.600 | 56.38 M | 2023-09-01 – 2023-09-01 | |
| `2024/agosto.csv` | 13.809 | 57.75 M | 2024-09-04 – 2024-09-04 | |
| `2024/dezembro.csv` | 14.060 | 58.52 M | 2025-01-06 – 2025-01-06 | |
| `2024/fevereiro.csv` | 13.769 | 57.09 M | 2024-03-27 – 2024-03-27 | |
| `2024/janeiro.csv` | 13.748 | 56.69 M | 2024-01-02 – 2024-01-02 | |
| `2024/marco-julho.csv` | 13.825 | 57.56 M | 2024-07-10 – 2024-07-10 | bloco multi-mês |
| `2024/novembro.csv` | 13.979 | 58.26 M | 2024-11-04 – 2024-11-04 | |
| `2024/setembro-outubro.csv` | 13.979 | 58.26 M | 2024-11-04 – 2024-11-04 | bloco multi-mês; idêntico a nov/2024 |
| `2025/dezembro.csv` | 14.448 | 59.59 M | 2025-12-31 – 2025-12-31 | |
| `2025/fevereiro.csv` | 14.192 | 58.81 M | 2025-03-24 – 2025-03-24 | |
| `2025/janeiro.csv` | 14.114 | 58.59 M | 2025-01-27 – 2025-01-27 | |
| `2025/julho-agosto.csv` | 14.393 | 59.38 M | 2025-08-26 – 2025-08-26 | bloco multi-mês |
| `2025/maio-junho.csv` | 14.251 | 59.07 M | 2025-06-06 – 2025-06-06 | bloco multi-mês |
| `2025/marco.csv` | 14.210 | 58.98 M | 2025-05-09 – 2025-05-09 | |
| `2025/setembro-a-novembro.csv` | 14.448 | 59.66 M | 2025-11-07 – 2025-11-07 | bloco multi-mês |
| `2026/abril.csv` | 14.556 | 59.96 M | 2026-04-30 – 2026-04-30 | snapshot mais recente |
| `2026/fevereiro.csv` | 14.545 | 59.98 M | 2026-02-27 – 2026-02-27 | |
| `2026/janeiro.csv` | 14.517 | 59.86 M | 2026-01-31 – 2026-01-31 | |
| `2026/marco.csv` | 14.553 | 59.96 M | 2026-03-31 – 2026-03-31 | |

**Leituras rápidas:**

- **Jun–out/2022:** ~13,4 mil linhas e ~58 M m³ por mês; **nov/dez/2022** caem para ~10,3 mil linhas e ~32 M m³.
- **2023→2026:** patamar ~56–60 M m³ por snapshot; crescimento gradual de linhas (~13,7k → ~14,5k).
- **`Data` única por arquivo** na maioria dos casos — confirma que é data de publicação do snapshot, não série intra-arquivo.
- **Arquivos duplicados:** `2023/outubro` e `2023/novembro` iguais a `dez/2023`; `2024/setembro-outubro` igual a `nov/2024`.

**Como atualizar:** reexecutar `py estudos/tancagem-abastecimento/export_inventario_raw.py --md inventario.md` no fuel-analytics e promover a tabela para este arquivo.

_Última atualização do inventário: 22/05/2026._

## Qualidade e chaves

> **Status:** parcialmente documentado — validado em snapshot `2026/janeiro.csv` (exploração fuel-analytics).

### Chave lógica candidata

Granularidade da fonte: **uma linha por** `Data` × `CodInstalacao` × `Tag` × `GrupoDeProdutos`.

| Campo | Papel |
|-------|--------|
| `Data` | Data de disponibilização do snapshot na página ANP (não “mês de estoque”) |
| `CodInstalacao` | Instalação i-SIMP (7 dígitos) |
| `Tag` | Unidade de armazenagem na instalação |
| `GrupoDeProdutos` | DERIVADOS E BIOCOMBUSTÍVEIS, GLP, PETRÓLEO, OUTROS |

**Validação (jan/2026):** 14.517 linhas; **0 duplicatas** na chave acima.

### Tipos e identificadores

| Coluna | Tratamento recomendado no ETL |
|--------|-------------------------------|
| `Cnpj` | Ler como **texto** (evitar float / notação científica) |
| `CodInstalacao` | Texto ou inteiro consistente; normalizar `.0` se vier de Excel |
| `TancagemM3` | Numérico; soma apenas após agregar na granularidade da chave |

### Domínios observados (snapshot jan/2026)

| Coluna | Cardinalidade | Valores principais |
|--------|---------------|-------------------|
| `GrupoDeProdutos` | 4 | DERIVADOS E BIOCOMBUSTÍVEIS (~77%), GLP, PETRÓLEO, OUTROS |
| `Segmento` | 11 | ex.: BASES DO RAMO DE TRR, DISTRIBUIDORES, etc. |
| `TipoDaUnidade` | 3 | TANQUE, VASO DE PRESSÃO, ESFERA |

Confirmar domínios em outros meses antes de assumir série histórica fechada.

### Regras de agregação

- Métrica base: **soma de `TancagemM3`** no recorte desejado.
- Não somar a mesma `Tag` duas vezes no mesmo snapshot.
- Para totais por empresa, UF ou município: agregar **explicitamente** a partir da chave, não usar média de `TancagemM3` entre tanques.

### Trusted (fuel-analytics)

Regras implementadas em SQL no repositório fuel-analytics; promover aqui quando validadas:

- [ ] Linhas 100% nulas nas 12 colunas de negócio — política de descarte na trusted
- [ ] Colunas de rastreio: `_source_file`, `_source_year`, `_source_period`

## Anomalias conhecidas

> **Status:** em investigação no [TODO do estudo](https://github.com/GabrielTrentino/anp-fuel-analytics/blob/main/estudos/tancagem-abastecimento/TODO.md).

| Período | Observação | Impacto na integração |
|---------|------------|------------------------|
| **nov/dez 2022** | ~44% menos m³ e ~23% menos linhas que jun–out/2022 | Não tratar como queda real de capacidade até confirmar escopo dos arquivos `tancagem_terminais_*` |
| **out/2022** | Publicado como `.xlsx` no portal | Converter para CSV antes do ETL (`raw_prepare`) |
| **abr/2025** | Sem arquivo no portal | Lacuna na série mensal |
| **jul/2023** | Citado na página, sem hyperlink | Lacuna / validar download manual |
| **Blocos multi-mês** | ex. `marco-julho.csv`, `setembro-a-novembro.csv` | Um arquivo → vários meses; não duplicar ao harmonizar |
| **out/nov 2023** | Mesmas linhas, m³ e `Data` que dez/2023 | Possível republicação do mesmo snapshot; validar download |
| **set/out 2024** | `setembro-outubro.csv` idêntico a `novembro.csv` | Idem |

**Hipóteses em aberto (não promovidas):** série 2022 com prefixo `tancagem_terminais_*` pode representar universo parcial (terminais) até a padronização `janeiro.csv` em 2023.

## Sugestões de análises

Métrica base recomendada: **soma de `TancagemM3`** no recorte desejado. A granularidade da fonte é **unidade (`Tag`) × instalação × grupo de produto** — evitar somar a mesma `Tag` duas vezes no mesmo snapshot; para totais por instalação, empresa ou município, agregar explicitamente nesse nível.

### Visão nacional e evolução histórica

- **Tancagem total do Brasil** por mês (jun/2022 → hoje), em m³ e, se útil, em milhões de m³ ou barris equivalentes (conversão documentada).
- **Evolução por `GrupoDeProdutos`** — participação de derivados/biocombustíveis, GLP, petróleo e outros no estoque autorizado.
- **Evolução por `Segmento`** — peso de distribuidores, TRR, produtores, terminais etc. na capacidade nacional.
- **Sazonalidade e rupturas** — picos após mudanças regulatórias, crises de abastecimento ou inclusão de novos agentes no SIMP.
- **Crescimento acumulado** — variação % em 12 meses, 24 meses e desde o início da série (2022).

### Empresas e mercado

- **Ranking de empresas** (`Cnpj` / `NomeEmpresarial`) por tancagem total e por grupo de produto.
- **Desenvolvimento da tancagem por empresa** — série temporal por CNPJ; empresas que mais expandiram ou reduziram capacidade.
- **Entrada e saída de players** — CNPJs ou `CodInstalacao` que aparecem ou deixam de aparecer entre meses.
- **Concentração do setor** — índice HHI ou share dos top 5 / top 10 por segmento.
- **Expansão por instalação** — novas `Tag`, aumento de `TancagemM3` na mesma instalação, mudança de `DetalheInstalacao`.

### Geografia: município, UF e região

- **Tancagem por UF** — mapa coroplético e ranking; evolução temporal por estado.
- **Tancagem por município** — top cidades; capacidade per capita se cruzar com população (IBGE).
- **Tancagem por região** — agregar UF → Norte, Nordeste, Centro-Oeste, Sudeste, Sul.
- **Dependência local** — municípios com pouca tancagem própria vs. vizinhos com alta capacidade (proxy logístico).
- **Hotspots industriais** — municípios com muitas instalações de terminal ou base de TRR.

### Instalações e infraestrutura

- **Capacidade média por tanque** — `TancagemM3` médio/mediano por `Tag` ou por instalação.
- **Número de unidades** — contagem de `Tag` por instalação, segmento ou UF.
- **Mix de `TipoDaUnidade`** — proporção tanque vs. vaso de pressão vs. esfera (relevante para GLP).
- **Instalações “gigantes”** — top `CodInstalacao` por soma de m³; outliers acima de um limiar (ex. > 100 mil m³).

### Recortes temáticos

- **GLP vs. derivados** — comparar dinâmica de capacidade autorizada para gás de cozinha e combustíveis líquidos.
- **TRR e bases de distribuição** — foco em `Segmento` relacionado a TRR e `DetalheInstalacao` (exclusiva/compartilhada).
- **Terminais vs. revenda** — contrastar com o conjunto [Capacidade de Armazenagem de Terminais](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais) (escopo diferente, possível validação cruzada).

### Cruzamentos com outros dados (projetos derivados)

- **Revendas e postos** — cruzar com cadastro de revendas / pontos de abastecimento: tancagem autorizada próxima ao consumo.
- **Movimentação de derivados** — relação capacidade instalada vs. volume movimentado (SIMP / movimentação ANP).
- **Preços** — série histórica de preços vs. expansão de tancagem regional (oferta local de armazenagem).
- **População e frota** — indicadores por UF (IBGE, DENATRAN) para normalizar “m³ de tancagem por habitante” ou por km².

### Qualidade e método (antes de publicar resultados)

- Harmonizar **lacunas** (abr/2025, jul/2023, blocos multi-mês) ao construir painéis mensais.
- Tratar **arquivos de 2022** (nomes e outubro em XLSX) numa etapa de ETL dedicada.
- Documentar que `TancagemM3` é **capacidade autorizada/operacional cadastrada**, não estoque físico nem ocupação.
- Padronizar `Municipio` (maiúsculas, acentos, homônimos) antes de agregações geográficas.

## Uso neste atlas

```text
data/raw/tancagem-abastecimento/
├── metadados-tancagem.pdf      # metadados oficiais ANP (consultado)
├── 2026-janeiro.csv            # exemplo de nomenclatura local
└── {ano}/{periodo}.csv         # espelhar estrutura do portal ao baixar
```

**Status da exploração:** página oficial, metadados PDF, schema CSV, matriz de arquivos, [inventário empírico](#inventário-empírico-dos-brutos) (36 CSVs medidos), [qualidade](#qualidade-e-chaves) e [anomalias](#anomalias-conhecidas).

**Exploração ativa:** notebooks em [anp-fuel-analytics — tancagem-abastecimento](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/tancagem-abastecimento/notebooks) (perfil, qualidade, piloto temporal). Descobertas estáveis devem ser refletidas nas seções acima — ver critérios nos [READMEs](https://github.com/GabrielTrentino/anp-data-atlas#o-que-promover-para-o-atlas-e-o-que-não) de cada repositório.

**Integração histórica (este atlas):** pipeline em `pipelines/` para consolidar jun/2022→hoje — harmonizar blocos, lacunas e série 2022. Pendente de implementação.

## Conjuntos relacionados

- [Capacidade de Armazenagem de Terminais](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais) — foco em terminais
- [Catálogo de dados abertos](../dados-abertos.md) — índice dos 42 conjuntos ANP

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-22 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
