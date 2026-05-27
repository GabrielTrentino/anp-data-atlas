# Fiscalização de Conteúdo Local

| Campo | Valor |
|-------|-------|
| **Slug** | `fiscalizacao-conteudo-local` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#18) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-fiscalizacao-de-conteudo-local |
| **Unidade ANP (inventário)** | SFI |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Regulação / Conteúdo Local |
| **Pasta local** | `data/raw/fiscalizacao-conteudo-local/` |
| **Inventário ANP** | Fiscalização de Conteúdo Local |
| **Prioridade fuel-analytics** | Baixa (regulação) |

## Contexto

Resultados da fiscalização do cumprimento de compromissos de conteúdo local em contratos de E&P. A ANP verifica se os concessionários atingiram os percentuais comprometidos de bens e serviços nacionais.

## Relevância para anp-fuel-analytics

Regulação industrial. Pode indicar gargalos na cadeia de fornecedores nacionais para E&P e impacto em cronogramas de projetos.

## Estrutura dos arquivos

> **Status:** validado — 7 CSVs + 7 PDFs metadados.

- **Formato:** CSV (sep `;`, encoding UTF-8)
- **Segmentação por fase e rodada:**
  - `fiscalizacao-exploracao-r1-r6-1.csv` — exploração, rodadas 1–6
  - `fiscalizacao-exploracao-r7-aditados-1.csv` — exploração, rodada 7+
  - `fiscalizacao-desenvolvimento-mar.csv` — desenvolvimento marítimo
  - `fiscalizacao-desenvolvimento-terra.csv` — desenvolvimento terrestre
  - `fiscalizacao-desenvolvimento-r1-r4.csv` — desenvolvimento, rodadas 1–4
  - `fiscalizacao-desenvolvimento-r5-r6.csv` — desenvolvimento, rodadas 5–6
  - `fiscalizacao-desenvolvimento-r7.csv` — desenvolvimento, rodada 7
- **Metadados:** 7 PDFs correspondentes

## Cruzamentos sugeridos

- [aditamento-conteudo-local](aditamento-conteudo-local.md) — contratos que pediram flexibilização
- [rodadas-licitacoes](rodadas-licitacoes.md) — compromissos originais
- [multas-2016](multas-2016.md) — penalidades por descumprimento (se aplicável)

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SFI
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Cumprimento

- **Taxa de cumprimento** — % de contratos que atingiram a meta; evolução anual.
- **Gap médio** — diferença entre meta e realizado; distribuição.
- **Por fase** — exploração vs desenvolvimento; onde há mais descumprimento.

### Penalidades e consequências

- **Multas aplicadas** — valor total; frequência; tendência.
- **Waiver/dispensa** — contratos dispensados da obrigação; motivos.

### Cruzamentos

- **Fiscalização × aditamentos** — contratos flexibilizados cumprem melhor?
- **Fiscalização × operador** — taxa de cumprimento por concessionário.
- **Fiscalização × rodadas** — rodadas com regras mais rígidas têm mais descumprimento?

## Inventário empírico dos brutos

| Arquivo local | Linhas | Formato | Encoding | Sep | Colunas | Notas |
|---------------|-------:|---------|----------|:---:|--------:|-------|
| `fiscalizacao-exploracao-r1-r6-1.csv` | 132 | CSV | utf-8-sig | `;` | 10–11 | Exploração, rodadas 1–6 |
| `fiscalizacao-exploracao-r7-aditados-1.csv` | 280 | CSV | utf-8-sig | `;` | 10–11 | Exploração, rodada 7+ aditados |
| `fiscalizacao-desenvolvimento-mar.csv` | 1 | CSV | utf-8-sig | `;` | 10–11 | Desenvolvimento marítimo (header only?) |
| `fiscalizacao-desenvolvimento-terra.csv` | 14 | CSV | utf-8-sig | `;` | 11 | Desenvolvimento terrestre. Cols: Rodada, Bloco/Campo, Bacia, Contrato, Data, Término, Operador, CNPJ, Nível CL, [outro] |
| `fiscalizacao-desenvolvimento-r1-r4.csv` | 9 | CSV | utf-8-sig | `;` | 10–11 | Desenvolvimento, rodadas 1–4 |
| `fiscalizacao-desenvolvimento-r5-r6.csv` | 3 | CSV | utf-8-sig | `;` | 10–11 | Desenvolvimento, rodadas 5–6 |
| `fiscalizacao-desenvolvimento-r7.csv` | 6 | CSV | utf-8-sig | `;` | 10–11 | Desenvolvimento, rodada 7 |
| `metadados-*.pdf` (7 arquivos) | — | PDF | — | — | — | Dicionários de dados por segmento |

## Qualidade e chaves

- **Chave lógica:** `Campo`/`Bloco` + `Rodada` + `Contrato` (por arquivo de fase)
- **Granularidade:** 1 linha por campo/bloco fiscalizado em determinada fase
- **Encoding:** utf-8-sig, sep `;`, 10–11 colunas (varia por arquivo)
- **Arquivos:** 7 CSVs segmentados por fase e ambiente:
  - Desenvolvimento: mar (0 dados!), R1-R4 (8), R5-R6 (3), R7 (6), terra (14)
  - Exploração: R1-R6 (132), R7-aditados (280)
- **Nulls:** `Multa Aplicada`, `Nº Processo`, `Nº Auto de Infração` — 100% nulos (campos previstos mas não preenchidos)
- **Observações:** `fiscalizacao-desenvolvimento-mar.csv` tem 0 linhas de dados (apenas header). Volume muito baixo — dados esparsos.

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados e arquivos do portal ANP |
| 2026-05-26 | Inventário empírico dos brutos e seção Qualidade e chaves adicionados |
