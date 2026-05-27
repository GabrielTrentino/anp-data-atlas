# Variáveis e chaves de ligação — 42 conjuntos

Índice resumido para **navegação e cruzamento** entre conjuntos. Foco em dimensões observáveis (`Data`, `Cnpj`, geo, produto, volume) e chaves que permitem vincular um acesso ao outro.

| Legenda | Significado |
|---------|-------------|
| **✓** | Schema confirmado empiricamente no atlas (`docs/conjuntos/`) |
| **~** | Inferido do portal, inventário ou padrão ANP — validar após download |

Catálogo completo: [dados-abertos.md](dados-abertos.md) · inventário institucional: [inventario-dados.md](inventario-dados.md)

---

## Chaves transversais (hub de ligação)

| Chave | Onde aparece | Liga com |
|-------|--------------|----------|
| **`CodInstalacao`** (i-SIMP, 7 díg.) | SIMP: tancagem, movimentação, pontos abastecimento | Capacidade ↔ volumes ↔ cadastro de instalação |
| **`Cnpj`** | SIMP, cadastros, distribuidores, fiscalização, multas, gás | Agente regulado em qualquer tema downstream |
| **`Uf` + `Municipio`** | Cadastros, tancagem, preços LPC, vendas, PMQC, fiscalização | Geo — agregação regional |
| **`Produto` / `GrupoDeProdutos`** | Movimentação, vendas, preços, refino, importações, tancagem | Mix de combustíveis e derivados |
| **`Ano`/`Mes`/`Periodo`/`Data`** | Quase todas as séries temporais | Sincronizar mês de referência vs `Data` de publicação |
| **`Bloco` / `Campo` / `CodigoPoco`** | E&P, rodadas, produção, acervo | Cluster upstream |
| **`Terminal`** | Capacidade e movimentação aquaviária | Logística portuária/fluvial |

> **`Data` no SIMP (tancagem):** data de **publicação** do CSV na ANP, não o mês de estoque — usar nome do arquivo + valores distintos ao montar série ([tancagem-abastecimento.md](conjuntos/tancagem-abastecimento.md)).

---

## Abastecimento, distribuição e mercado downstream

| # | Slug | Métrica principal | Variáveis principais | Chaves de ligação | Cruzamentos |
|---|------|-------------------|----------------------|-------------------|-------------|
| 41 | [`tancagem-abastecimento`](conjuntos/tancagem-abastecimento.md) | Capacidade m³ (`TancagemM3`) | `Data`, `Cnpj`, `CodInstalacao`, `Uf`, `Municipio`, `Segmento`, `Tag`, `GrupoDeProdutos` **✓** | `CodInstalacao`+`Tag`+`GrupoDeProdutos`; `Cnpj`; geo | movimentação, cadastros, preços |
| 21 | [`movimentacao-derivados`](conjuntos/movimentacao-derivados.md) | Volume movimentado | `Ano`, `Mês`, `Agente Regulado`, `Código do Produto`, `UF Origem/Destino`, volume **✓** | nome agente→tancagem; geo→vendas |
| 12 | [`cadastro-revendas-combustiveis`](conjuntos/cadastro-revendas-combustiveis.md) | Cadastro de postos | `Cnpj`, `Uf`, `Municipio`, `Bandeira`, `Situacao`, endereço **~** | `Cnpj`; `Uf`+`Municipio` | tancagem, preços, movimentação |
| 11 | [`cadastro-revendas-glp`](conjuntos/cadastro-revendas-glp.md) | Cadastro revendas GLP | `Cnpj`, `Uf`, `Municipio`, modalidade botijão/granel, `Situacao` **~** | `Cnpj`; geo | movimentação GLP, tancagem (GLP) |
| 27 | [`pontos-abastecimento`](conjuntos/pontos-abastecimento.md) | Instalações autorizadas | `CodInstalacao`, `Cnpj`, `Uf`, `Municipio`, `Segmento`, `Situacao` **~** | `CodInstalacao`, `Cnpj` | cadastro revendas, fiscalização |
| 15 | [`distribuidores-combustiveis-liquidos`](conjuntos/distribuidores-combustiveis-liquidos.md) | Cadastro atacado | `Cnpj`, `NomeEmpresarial`, `Uf`, contratos cessão, início atividade **~** | `Cnpj` | movimentação, terminais |
| 28 | [`pmqc`](conjuntos/pmqc.md) | Qualidade analítica | `Periodo`, `Produto`, `Uf`/região, parâmetros, % conformidade **~** | `Produto`+geo+mês | fiscalização, cadastros |
| 29 | [`pml`](conjuntos/pml.md) | Qualidade lubrificantes | `Produto`/marca, parâmetros, conformidade, região **~** | código produto | registro lubrificantes, movimentação |
| 40 | [`serie-historica-precos`](conjuntos/serie-historica-precos.md) | Preço R$/L (`PrecoMedio`) | `Produto`, `Regiao`/`Estado`/`Municipio`, semana/mês, min/max **~** | `Produto`+geo+tempo | vendas, cadastros, tancagem |
| 42 | [`vendas-derivados`](conjuntos/vendas-derivados.md) | Volume vendido | `Periodo`, `Segmento`, `Produto`, `Uf`, `Municipio`, volume **~** | `Produto`+geo+mês | movimentação, importações, biocombustíveis |
| 2 | [`fiscalizacao-abastecimento`](conjuntos/fiscalizacao-abastecimento.md) | Ações e documentos | `DataAcao`, `Cnpj`, `Uf`, `Municipio`, `Segmento`, tipo doc, resultado **~** | `Cnpj`; geo | PMQC, cadastros |
| 9 | [`capacidade-armazenagem-terminais`](conjuntos/capacidade-armazenagem-terminais.md) | Capacidade terminal m³ | `Terminal`, `Cnpj`, tipo terminal, `Uf`, `Municipio`, produto **~** | terminal, `Cnpj` | tancagem, mov. aquaviária |
| 22 | [`movimentacao-terminais-aquaviarios`](conjuntos/movimentacao-terminais-aquaviarios.md) | Volume terminal m³ | `Terminal`, `Periodo`, `Produto`, operação carga/descarga **~** | terminal+mês+produto | capacidade terminais, movimentação |
| 37 | [`registro-lubrificantes`](conjuntos/registro-lubrificantes.md) | Catálogo produtos | `RegistroANP`, nome, classe/viscosidade, fabricante **~** | código produto | PML, movimentação lubrificantes |

---

## Produção, refino, comércio exterior e estatística

| # | Slug | Métrica principal | Variáveis principais | Chaves de ligação | Cruzamentos |
|---|------|-------------------|----------------------|-------------------|-------------|
| 32 | [`processamento-petroleo-derivados`](conjuntos/processamento-petroleo-derivados.md) | Volume refino/produção m³ | `Periodo`, refinaria, `Produto`, volume processado/produzido **~** | refinaria+produto+mês | vendas, importações |
| 33 | [`producao-biocombustiveis`](conjuntos/producao-biocombustiveis.md) | Produção biodiesel/etanol | `Periodo`, `Produto`, `Uf`/região, volume **~** | produto+geo+mês | vendas, preços etanol |
| 34 | [`producao-por-estado`](conjuntos/producao-por-estado.md) | Produção E&P por UF | `Periodo`, `Uf`, terra/mar, petróleo, gás, LGN **~** | `Uf`+mês | anuário, importações |
| 35 | [`producao-por-poco`](conjuntos/producao-por-poco.md) | Produção por poço | `Periodo`, `CodigoPoco`, `Campo`, `Bacia`, operador, volumes **~** | `CodigoPoco`+mês | produção por estado, resultado poço |
| 19 | [`importacoes-exportacoes`](conjuntos/importacoes-exportacoes.md) | Volume imp/exp | `Periodo`, `Produto`, `Pais`, importação/exportação **~** | produto+mês+país | vendas, refino |
| 5 | [`anuario-estatistico`](conjuntos/anuario-estatistico.md) | Multi-tabela (~10 anos) | colunas variam: `Ano`, `Produto`, `Volume`, `Uf`… **~** | chave por tabela | benchmark de todas as séries mensais |

---

## Exploração e produção (E&P)

| # | Slug | Métrica principal | Variáveis principais | Chaves de ligação | Cruzamentos |
|---|------|-------------------|----------------------|-------------------|-------------|
| 13 | `dados-ep` | Agregados E&P | bloco, operador, fase, volumes (sub-bases) **~** | `Bloco`, `Campo` | fases, produção |
| 16 | `fase-exploracao` | Blocos em exploração | `BLOCO`, `BACIA`, `OPERADOR`, `CONTRATADOS`, `RODADA`, `REGIME CONTRATUAL` **✓** | `BLOCO` | rodadas, concessionários |
| 17 | `fase-desenvolvimento-producao` | Campos em D&P | `Poço`, `Campo`, `Bacia`, `Estado`, `Instalação`, volumes produção **✓** | `Campo`/`Poço` | produção por poço/estado |
| 8 | `blocos-fase-exploratoria-encerrada` | Blocos encerrados | `Bloco`, `Bacia`, data encerramento, motivo **~** | `Bloco` | rodadas, fase exploração |
| 20 | `incidentes-ep` | Incidentes operacionais | `Numero`, `Empresa`, `CNPJ`, `Data_de_criacao`, `UF`, `Ambiente` **✓** | `Numero`+tabelas dim | produção, concessionários |
| 38 | `resultado-poco` | Resultado de poço | `CodigoPoco`, `Campo`, `Bacia`, resultado, profundidade **~** | `CodigoPoco` | produção por poço, acervo |
| 31 | `previsao-atividades-investimentos` | Investimentos previstos | `ATIVIDADE`, `TIPO`, `ANO PTE`, `QUANTIDADE`, `INVESTIMENTO` **✓** | atividade+ano | rodadas, fase exploração |
| 36 | `relacao-concessionarios` | Concessionários | `Número Contrato`, `CNPJ`, `Nome`, participação, `Rodada` **✓** | `Número Contrato`, `CNPJ` | rodadas, produção |
| 39 | `rodadas-licitacoes` | Licitações | `Bloco`, `Rodada`, `Setor`, `Bacia`, `Bônus`, `Empresa/Consórcio` **✓** | `Bloco`+`Rodada` | concessionários, fases |

---

## Gás natural

| # | Slug | Métrica principal | Variáveis principais | Chaves de ligação | Cruzamentos |
|---|------|-------------------|----------------------|-------------------|-------------|
| 7 | `autorizacoes-gas-natural` | Autorizações | `Cnpj`, tipo atividade, `Uf`, validade **~** | `Cnpj` | comercialização, gasodutos |
| 10 | `comercializacao-gas-natural` | Volume vendido m³ | `Ano`, `Mês`, `TipoMercado`, `RegiãoAgregada`, `Preço MMBtu`, `Volume mil m³/dia` **✓** | segmento+mês | gasodutos, autorizações |
| 23 | `movimentacao-gas-gasodutos` | Volume transportado m³ | `Código Instalação Gasoduto`, `Nome Instalação Transporte`, dias (wide) **✓** | gasoduto+dia | comercialização |

---

## Acervo técnico e geociências

| # | Slug | Métrica principal | Variáveis principais | Chaves de ligação | Cruzamentos |
|---|------|-------------------|----------------------|-------------------|-------------|
| 1 | `acervo-dados-tecnicos` | Poços, sísmica, geoquímica | `POCO`, `CADASTRO`, `OPERADOR`, `ESTADO`, `BACIA`, `CAMPO` (58 cols) **✓** | `POCO`/`CADASTRO` | resultado poço, bacias |
| 4 | `amostras-rochas-fluidos` | Declaração amostras | `CodigoPoco`, código amostra, tipo, profundidade **~** | `CodigoPoco` | acervo, resultado poço |
| 6 | `aquisicao-processamento-estudo-dados` | Surveys sísmicos | relatório mensal EAD (report-style, 5 cols) **✓** | `Bacia`/survey | bacias, acervo |
| 14 | `bacias-sedimentares` | Geometria bacias | `Bacia`, polígonos (shapefile) **~** | `Bacia` | blocos, poços, E&P |

---

## Regulação, fiscalização e participações

| # | Slug | Métrica principal | Variáveis principais | Chaves de ligação | Cruzamentos |
|---|------|-------------------|----------------------|-------------------|-------------|
| 3 | `aditamento-conteudo-local` | Aditamentos contratuais | `Ordem`, `Contrato`, `Operador`, `Bloco/Campo`, `Bacia`, `Rodada`, `Status` **✓** | `Contrato`/`Bloco` | fiscalização conteúdo local |
| 18 | `fiscalizacao-conteudo-local` | Metas conteúdo local | `Rodada`, `Bloco`/`Campo`, `Bacia`, `Contrato`, `Operador`, `CNPJ` **✓** | `Bloco` | aditamentos, rodadas |
| 24 | `multas-2016` | Valor multa R$ | processo, `Cnpj`, valor, vencimento, situação (report-style) **✓** | `Cnpj`, nº processo | fiscalização abastecimento |
| 25 | `participacoes-governamentais` | Royalties e participação especial | `competencia`, `caixa`, `estados`, `municipios`, `fundo_social` **✓** | competência (mês) | produção E&P |
| 26 | `pesquisa-desenvolvimento-inovacao` | Investimento PD&I | `Grupo Econômico`, `Área`, `Ano`, `Valor Obrigação` **✓** | `Grupo`+`Ano` | (fraco) E&P |
| 30 | `prestadores-apoio-administrativo` | Cadastro prestadores | `Cnpj`, tipo serviço, `Situacao`, `Uf` **✓** | `Cnpj` | (fraco) cadastros |

---

## Grafo de ligação — downstream (fuel)

```text
                    ┌─────────────────┐
                    │  CodInstalacao  │
                    │      Cnpj       │
                    └────────┬────────┘
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
  tancagem-abast.    movimentacao-deriv.   pontos-abastecimento
  (TancagemM3)         (Volume m³)          (cadastro inst.)
         │                   │                   │
         └─────────┬─────────┴─────────┬─────────┘
                   ▼                   ▼
            cadastro-revendas    distribuidores
                   │                   │
         ┌─────────┴─────────┐         │
         ▼                   ▼         ▼
  serie-historica-precos   vendas-derivados ←→ importacoes-exportacoes
         (PrecoMedio)         (Volume)              (Volume)
                   │                   │
                   └─────────┬─────────┘
                             ▼
                    Uf + Municipio + Produto + Periodo
                             │
              pmqc · fiscalizacao · producao-biocombustiveis
```

---

## Atualização

| Quando | O que fazer |
|--------|-------------|
| Schema confirmado em `docs/conjuntos/{slug}.md` | Trocar **~** por **✓** neste índice |
| Nova exploração fuel-analytics | Promover variáveis e chaves validadas |
| Próximo candidato | `movimentacao-derivados` — compartilha `CodInstalacao`/`Cnpj` com tancagem |
