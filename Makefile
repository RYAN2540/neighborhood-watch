serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations neighborhoodapp

migrate:
	python3.9 manage.py migrate
admin:
	python manage.py createsuperuser
test:
	python3.9 manage.py test neighborhoodapp

