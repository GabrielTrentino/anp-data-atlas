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

**Status da exploração:** página oficial, metadados PDF, schema CSV e matriz de arquivos documentados abaixo.

**Exploração ativa:** notebooks em [anp-fuel-analytics — tancagem-abastecimento](https://github.com/GabrielTrentino/anp-fuel-analytics/tree/main/estudos/tancagem-abastecimento/notebooks) (perfil, qualidade, piloto temporal). Descobertas estáveis devem ser refletidas neste arquivo.

**Integração histórica (este atlas):** pipeline em `pipelines/` para consolidar jun/2022→hoje — harmonizar blocos, lacunas e série 2022. Pendente de implementação.

## Conjuntos relacionados

- [Capacidade de Armazenagem de Terminais](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/capacidade-de-armazenagem-de-terminais) — foco em terminais
- [Catálogo de dados abertos](../dados-abertos.md) — índice dos 42 conjuntos ANP
