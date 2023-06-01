build:
	docker-compose up --build -d

migrate:
	docker exec -it apptrix python manage.py migrate
