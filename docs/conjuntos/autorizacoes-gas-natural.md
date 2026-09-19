# Autorizações de Gás Natural

| Campo | Valor |
|-------|-------|
| **Slug** | `autorizacoes-gas-natural` |
| **Catálogo** | [dados-abertos.md](../dados-abertos.md) (#7) |
| **Página oficial** | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-autorizacoes-gas-natural |
| **Unidade ANP (inventário)** | SFI / SCM |
| **Periodicidade** | Conforme atualização cadastral (arquivos republicados no portal) |
| **Formato** | CSV · XLSX |
| **Fonte operacional** | Gás Natural |
| **Pasta local** | `data/raw/autorizacoes-gas-natural/` |
| **Inventário ANP** | Autorizações de gás natural (+ bases do PDA 2026–2028 relacionadas a GNC/GNL, carregamento, comercialização, etc.) |
| **Prioridade fuel-analytics** | Média (complementar a GNV/GLP) |

## Contexto

Registro de autorizações concedidas pela ANP para atividades na cadeia do gás natural — em especial **instalações de transporte e/ou movimentação** de gás natural. A página do portal publica listagens em CSV/XLSX e metadados.

> **Nota (set/2026):** a URL antiga `.../autorizacoes-de-gas-natural` deixou de responder; a vitrine aponta para `.../dados-abertos-autorizacoes-gas-natural`. Em mai/2026 o doc registrou 404 — a página **voltou a ficar disponível**.

## Relevância para anp-fuel-analytics

Mapa dos agentes/instalações autorizados na cadeia do gás. Relevante para entender a estrutura de mercado de gás canalizado e GNV, complementando análises de abastecimento. O inventário 2026-09-19 marca várias **autorizações adicionais** (GNC/GNL, ship-to-ship, importação/exportação) para publicação no [PDA 2026-2028](../dados-abertos.md) — ainda sem páginas próprias na vitrine dos 42.

## Estrutura dos arquivos

> **Status (2026-09-19):** página **disponível** no portal.

Arquivos observados na página oficial:

| Recurso | Atualização informada no portal |
|---------|----------------------------------|
| Metadados — Autorizações de gás natural | 22/4/2025 |
| Autorizações (`.csv`) | 2/4/2025 |
| Autorizações (`.xlsx`) | 2/4/2025 |

Escopo declarado na página: listagem de autorizações para **instalações de transporte e/ou movimentação** de gás natural.

## Cruzamentos sugeridos

- [comercializacao-gas-natural](comercializacao-gas-natural.md) — volumes comercializados pelos agentes autorizados
- [movimentacao-gas-gasodutos](movimentacao-gas-gasodutos.md) — transporte dos volumes
- [importacoes-exportacoes](importacoes-exportacoes.md) — importação de GN autorizada

## Conjuntos relacionados

- [Inventário de Dados ANP](../inventario-dados.md) — bases SFI/SCM e linhas PDA 2026–2028
- [tancagem-abastecimento.md](tancagem-abastecimento.md) — referência de documentação completa
- [Glossário ANP](https://www.gov.br/anp/pt-br/acesso-a-informacao/glossario) — termos da cadeia de gás

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

## Inventário empírico dos brutos

> Página disponível (set/2026). Download local e inventário empírico (linhas, schema) ainda **pendentes** — marcar **Raw** / **Emp.** no [TODO.md](../../TODO.md) após baixar.

---

## Histórico

> Este documento foi gerado a partir de informações extraídas do portal de dados abertos da ANP.

| Data | Evento |
|------|--------|
| 2026-05-26 | Criação do documento — extração inicial de metadados |
| 2026-05-26 | Status: página 404; inventário empírico indisponível |
| 2026-09-19 | Página reencontrada em `dados-abertos-autorizacoes-gas-natural`; CSV/XLSX e metadados (abr/2025); status atualizado |
