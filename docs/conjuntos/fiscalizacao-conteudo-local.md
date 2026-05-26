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

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/fiscalizacao-conteudo-local/`
3. Documentar schema e volume
