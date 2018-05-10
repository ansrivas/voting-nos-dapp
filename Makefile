.DEFAULT_GOAL := help

help:             ## Show available options with this Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY : test
test:             ## Run all the tests
test:
	python setup.py test

.PHONY : auto_create
auto_create:      ## Prepare local environment to run smart-contracts
auto_create:
	@git submodule update --init --recursive && \
	sed -i '/-\ .\/smart-contracts\:\/smart-contracts/a \ \ \ \ \ \ - ..\/..\/voting-smartcontract\:\/custom-smart-contracts' nos-local/neo-local/docker-compose.yml && \
	docker-compose -f nos-local/neo-local/docker-compose.yml up
