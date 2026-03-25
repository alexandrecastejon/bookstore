.PHONY: help up down build rebuild logs ps migrate makemigrations \
        createsuperuser shell bash test collectstatic \
        restart stop clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make up              - sobe os containers"
	@echo "  make down            - derruba os containers"
	@echo "  make build           - faz o build das imagens"
	@echo "  make rebuild         - rebuild completo e sobe"
	@echo "  make logs            - exibe os logs"
	@echo "  make ps              - mostra os containers"
	@echo "  make migrate         - aplica migrations"
	@echo "  make makemigrations  - cria novas migrations"
	@echo "  make createsuperuser - cria superusuário"
	@echo "  make shell           - abre shell do Django"
	@echo "  make bash            - abre bash no container web"
	@echo "  make test            - roda os testes"
	@echo "  make collectstatic   - coleta arquivos estáticos"
	@echo "  make restart         - reinicia os containers"
	@echo "  make stop            - para os containers"
	@echo "  make clean           - remove containers, rede e volumes"

up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

rebuild:
	docker compose down
	docker compose up --build

logs:
	docker compose logs -f

ps:
	docker compose ps

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

createsuperuser:
	docker compose exec web python manage.py createsuperuser

shell:
	docker compose exec web python manage.py shell

bash:
	docker compose exec web bash

test:
	docker compose exec web pytest

collectstatic:
	docker compose exec web python manage.py collectstatic --noinput

restart:
	docker compose restart

stop:
	docker compose stop

clean:
	docker compose down -v