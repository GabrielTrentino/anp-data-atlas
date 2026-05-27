# Makefile — anp-data-atlas
# Orquestra tarefas comuns do atlas.

PYTHON ?= python

.PHONY: help download validate generate-docs

help: ## Mostra ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

download: ## Baixa dados brutos de todos os conjuntos (config/datasets.yaml)
	$(PYTHON) scripts/download_raw_all.py

validate: ## Valida documentação (links, seções obrigatórias, coerência com yaml)
	$(PYTHON) scripts/validate_docs.py

generate-docs: ## Gera docs/conjuntos/{slug}.md para slugs novos no yaml
	$(PYTHON) scripts/generate_conjunto_doc.py
