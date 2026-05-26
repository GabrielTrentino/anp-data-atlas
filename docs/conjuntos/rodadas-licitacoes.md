# Rodadas de Licitações de Petróleo e Gás Natural

| Campo | Valor |
|-------|-------|
| **Slug** | `rodadas-licitacoes` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#39) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/rodadas-de-licitacoes-de-petroleo-e-gas-natural |
| **Unidade ANP (inventário)** | SPL |
| **Periodicidade** | Eventual (por rodada) |
| **Formato** | CSV |
| **Fonte operacional** | E&P / Licitações |
| **Pasta local** | `data/raw/rodadas-licitacoes/` |
| **Inventário ANP** | Rodadas de Licitações |
| **Prioridade fuel-analytics** | Baixa (upstream, institucional) |

## Contexto

Dados das rodadas de licitações da ANP — blocos ofertados, lances, vencedores, bônus de assinatura, compromissos exploratórios mínimos. Inclui rodadas de concessão, partilha de produção e cessão onerosa.

## Relevância para anp-fuel-analytics

Contexto institucional do setor upstream. Blocos arrematados em rodadas se tornam campos produtores futuros. Valor do bônus indica expectativa de mercado sobre a bacia.

## Estrutura dos arquivos

> **Status:** pendente — página ainda não explorada empiricamente.

## Cruzamentos sugeridos

- [fase-exploracao](fase-exploracao.md) — blocos em exploração originados das rodadas
- [relacao-concessionarios](relacao-concessionarios.md) — vencedores das rodadas
- [previsao-atividades-investimentos](previsao-atividades-investimentos.md) — investimentos comprometidos
- [blocos-fase-exploratoria-encerrada](blocos-fase-exploratoria-encerrada.md) — blocos devolvidos pós-rodada

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SPL
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Histórico de rodadas

- **Evolução dos bônus** — valor total arrecadado por rodada; tendência.
- **Blocos ofertados vs arrematados** — taxa de sucesso da ANP em cada rodada.
- **Regime contratual** — concessão vs partilha vs cessão; evolução do mix.
- **Impacto do preço do petróleo** — correlação entre Brent e interesse nas rodadas.

### Perfil dos vencedores

- **Concentração** — Petrobras vs demais; evolução pós-abertura.
- **Novos entrantes** — empresas que participaram pela primeira vez; rodada de entrada.
- **Consórcios** — frequência e composição; operadoras vs não-operadoras.

### Geográfico

- **Bacias licitadas** — distribuição por bacia; fronteiras vs áreas maduras.
- **Onshore vs offshore** — tendência ao longo das rodadas.
- **Áreas de maior competição** — blocos com mais lances; bacias mais disputadas.

### Cruzamentos

- **Rodadas × produção** — blocos arrematados que já estão produzindo; lead time.
- **Rodadas × resultado-poco** — taxa de sucesso por rodada.
- **Rodadas × participações governamentais** — royalties gerados por rodada.

## Uso neste atlas

**Status da exploração:** pendente.

**Próximos passos:**

1. Explorar página e mapear CSVs disponíveis
2. Download de amostras para `data/raw/rodadas-licitacoes/`
3. Documentar schema e volume
