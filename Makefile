serve:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations neighborhoodapp

migrate:
	python3 manage.py migrate
admin:
	python3 manage.py createsuperuser
test:
	python3 manage.py test neighborhoodapp

