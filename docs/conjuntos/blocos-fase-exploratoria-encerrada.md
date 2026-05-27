# Blocos com Fase Exploratória Encerrada

| Campo | Valor |
|-------|-------|
| **Slug** | `blocos-fase-exploratoria-encerrada` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#8) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/blocos-com-fase-exploratoria-encerrada |
| **Unidade ANP (inventário)** | SEP |
| **Periodicidade** | Eventual |
| **Formato** | CSV |
| **Fonte operacional** | E&P |
| **Pasta local** | `data/raw/blocos-fase-exploratoria-encerrada/` |
| **Inventário ANP** | Blocos com Fase Exploratória Encerrada |
| **Prioridade fuel-analytics** | Baixa (upstream, histórico) |

## Contexto

Registro de blocos exploratórios cujo contrato encerrou a fase de exploração — seja por conclusão do programa exploratório mínimo, descoberta comercial (transição para desenvolvimento), ou devolução à ANP por insucesso exploratório.

## Relevância para anp-fuel-analytics

Histórico de E&P. Útil para estudos de taxa de sucesso exploratório e como complemento à análise de rodadas.

## Estrutura dos arquivos

> **Status:** parcial — apenas metadados (PDF). CSV não disponível na página atual.

- 1 PDF de metadados (`metadados-blocos-fase-exploratoria-encerrada-2021.pdf`)
- CSV com listagem de blocos não encontrado (possível descontinuação ou acesso via outro canal)

## Cruzamentos sugeridos

- [fase-exploracao](fase-exploracao.md) — blocos atualmente em exploração
- [rodadas-licitacoes](rodadas-licitacoes.md) — rodada de origem do bloco
- [resultado-poco](resultado-poco.md) — resultado dos poços perfurados nesses blocos

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — base SEP
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa

## Sugestões de análises

### Taxa de sucesso

- **Blocos encerrados por motivo** — devolução vs declaração comercial; proporção.
- **Sucesso por bacia** — quais bacias têm maior taxa de descoberta comercial.
- **Sucesso por rodada** — rodadas recentes vs antigas; evolução da qualidade dos ativos ofertados.

### Temporal

- **Duração média da exploração** — tempo entre assinatura e encerramento.
- **Ondas exploratórias** — períodos com muitos encerramentos (crise de preço?).

### Cruzamentos

- **Encerrados × rodadas** — perfil dos blocos devolvidos por rodada; aprendizado.
- **Encerrados → desenvolvimento** — blocos que evoluíram para campos produtores.
- **Encerrados × resultado-poco** — tipo de resultado nos poços perfurados antes da devolução.

## Inventário empírico dos brutos

| Arquivo local | Tipo | Notas |
|---------------|------|-------|
| `metadados-fase-exploratoria-encerrada.pdf` | PDF | Metadados e dicionário de dados |

> CSV não localizado na página (possivelmente descontinuado ou acessível apenas via painel interativo).

## Qualidade e chaves

- **Status:** Não validável empiricamente — apenas metadados (PDF) disponíveis no portal.
- **Schema esperado:** Bloco, Bacia, data de encerramento, motivo
- **Chave lógica esperada:** `Bloco`
- **Observação:** Dados possivelmente descontinuados ou integrados em `fase-exploracao`
