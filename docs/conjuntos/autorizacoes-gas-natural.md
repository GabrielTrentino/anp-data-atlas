# Autorizações de Gás Natural

| Campo | Valor |
|-------|-------|
| **Slug** | `autorizacoes-gas-natural` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#7) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/autorizacoes-de-gas-natural |
| **Unidade ANP (inventário)** | SFI / SCM |
| **Periodicidade** | Mensal |
| **Formato** | CSV |
| **Fonte operacional** | Gás Natural |
| **Pasta local** | `data/raw/autorizacoes-gas-natural/` |
| **Inventário ANP** | Autorizações de gás natural |
| **Prioridade fuel-analytics** | Média (complementar a GNV/GLP) |

## Contexto

Registro de autorizações concedidas pela ANP para atividades na cadeia do gás natural — importação, exportação, comercialização, distribuição, transporte, estocagem, entre outras. Cada autorização indica agente, atividade, UF e vigência.

## Relevância para anp-fuel-analytics

Mapa dos agentes autorizados na cadeia do gás. Relevante para entender a estrutura de mercado de gás canalizado e GNV, complementando análises de abastecimento.

## Estrutura dos arquivos

> **Status:** indisponível — página não encontrada no portal (404). Possível reestruturação ou descontinuação.

Nenhum arquivo disponível para download na data de prospecção (mai/2026).

## Cruzamentos sugeridos

- [comercializacao-gas-natural](comercializacao-gas-natural.md) — volumes comercializados pelos agentes autorizados
- [movimentacao-gas-gasodutos](movimentacao-gas-gasodutos.md) — transporte dos volumes
- [importacoes-exportacoes](importacoes-exportacoes.md) — importação de GN autorizada

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — bases SFI/SCM
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Estrutura de mercado

- **Agentes por atividade** — comercializadores, distribuidores, importadores; contagem e evolução.
- **Concentração** — top agentes por número de autorizações; HHI.
- **Novos entrantes** — agentes autorizados recentemente; abertura de mercado pós-Nova Lei do Gás.
- **Vigência** — autorizações ativas vs encerradas; renovações.

### Geográfico

- **Cobertura estadual** — quais UFs têm mais agentes autorizados; vazios.
- **Tipo de atividade por região** — distribuição/comercialização mais presente onde há gasoduto.

### Cruzamentos

- **Autorizações × comercialização** — agentes autorizados que efetivamente comercializam; taxa de inatividade.
- **Autorizações × movimentação** — coerência entre autorizações de transporte e volumes em gasodutos.
- **Autorizações × preços** — número de comercializadores vs preço praticado (proxy de competição).

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/autorizacoes-gas-natural/`
3. Documentar schema e volume
