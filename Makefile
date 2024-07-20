.PHONY: run-server
run-server:
	poetry run python -m core.manage runserver

.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

	.PHONT: install-pre-commit
install-pre-commit:
	poetry run pre-commit install; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

update: install migrate install-pre-commit;
