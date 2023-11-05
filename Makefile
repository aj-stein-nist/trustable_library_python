SHELL:=/usr/bin/env bash
PYTHON_BIN_PATH:=/usr/bin/python3
PYTHON_BIN:=$(shell which python3 || echo $(PYTHON_PATH))

.PHONY: help
# Run "make" or "make help" to get a list of user targets
# Adapted from https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?##.*$$' $(MAKEFILE_LIST) | awk 'BEGIN { \
	 FS = ":.*?## "; \
	 printf "\033[1m%-30s\033[0m %s\n", "TARGET", "DESCRIPTION" \
	} \
	{ printf "\033[32m%-30s\033[0m %s\n", $$1, $$2 }'

.PHONY: all
all: install test

.PHONY: deps
install: ## Install dependencies with poetry
	$(PYTHON_BIN) -m poetry install 

.PHONY: test
test: ## Run unit tests
	$(PYTHON_BIN) -m unittest tests/*.py -v 

.PHONY: eval
eval: ## Open shell with poetry configuration
	$(PYTHON_BIN) -m poetry shell
