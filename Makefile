
.PHONY: all build ui up


all: build ui up

build:
	docker-compose -f local.yml build

ui:
	cd insights_integration_react_frontend; make install build deploy

up:
	docker-compose -f local.yml up





