EXEC = docker-compose exec api

build:
	@ docker-compose up -d --build

restart:
	@ docker-compose restart

start:
	@ docker-compose start

stop:
	@ docker-compose stop

down:
	@ docker-compose down

up:
	@ docker-compose up -d

install:
	@ pip install -r requirements.txt

shell:
	@ $(EXEC) python manage.py shell_plus

migrate:
	@ $(EXEC) python manage.py migrate

make_migrations:
	@ $(EXEC) python manage.py makemigrations

show_migrations:
	@ $(EXEC) python manage.py showmigrations

show_urls:
	@ $(EXEC) python manage.py show_urls

attach:
	docker attach api
