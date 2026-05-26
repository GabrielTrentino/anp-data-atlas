# Multas Aplicadas com Vencimento a partir de 2016

| Campo | Valor |
|-------|-------|
| **Slug** | `multas-2016` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#24) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/multas-aplicadas-com-vencimento-a-partir-de-2016 |
| **Unidade ANP (inventário)** | SFI / SFO |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Fiscalização |
| **Pasta local** | `data/raw/multas-2016/` |
| **Inventário ANP** | Multas (vencimento a partir de 2016) |
| **Prioridade fuel-analytics** | Média (fiscalização downstream) |

## Contexto

Registro de multas aplicadas pela ANP — autuações em ações de fiscalização com vencimento a partir de 2016. Inclui o agente autuado, valor da multa, motivo, UF, status do pagamento/recurso.

## Relevância para anp-fuel-analytics

Relevante para cruzamento com fiscalização do abastecimento: postos autuados e valores de multas por tipo de infração. Pode complementar análise de qualidade (PMQC) e regularidade do mercado.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

## Cruzamentos sugeridos

- [fiscalizacao-abastecimento](fiscalizacao-abastecimento.md) — ações que geraram as multas
- [pmqc](pmqc.md) — postos com não-conformidade que podem ter sido multados
- [cadastro-revendas-combustiveis](cadastro-revendas-combustiveis.md) — postos autuados
- [fiscalizacao-conteudo-local](fiscalizacao-conteudo-local.md) — multas de CL

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SFI/SFO
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Panorama das multas

- **Volume anual** — total de multas aplicadas por ano; tendência.
- **Valor total** — soma dos valores; ticket médio; distribuição (muitas pequenas vs poucas grandes).
- **Por motivo** — classificação das infrações; tipos mais frequentes (adulteração, irregularidade cadastral, etc.).
- **Status** — pago vs recurso vs cancelado; taxa de arrecadação efetiva.

### Geográfico

- **Por UF** — estados com mais multas; normalizado por número de postos/agentes.
- **Concentração** — reincidentes (agentes multados múltiplas vezes).

### Cruzamentos

- **Multas × fiscalização-abastecimento** — ações que geraram multas; perfil.
- **Multas × PMQC** — postos não-conformes que foram multados; lag entre amostragem e sanção.
- **Multas × cadastro** — postos multados que perderam autorização.
- **Multas × preços** — postos que praticam preços outlier e são fiscalizados.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/multas-2016/`
3. Documentar schema e volume
