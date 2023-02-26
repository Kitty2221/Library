
migrations:
	@docker exec -it -w /Library django_api python library/manage.py makemigrations

migrate:
	@docker exec -it -w /Library django_api python library/manage.py migrate

app:
	@mkdir -p src/apps/$(name)
	@docker exec -it -w /Library django_api python library/manage.py startapp $(name) library/$(name)

start_compose:
	@docker-compose -f docker-compose-dev.yml up

test_env:
	@cat ./docker/envs/env_example > ./docker/envs/.env

test_user:
	@docker exec -it -w /Library django_api python library/manage.py createsuperuser



