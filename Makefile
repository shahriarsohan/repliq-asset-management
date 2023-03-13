.PHONY: all help translate test clean update compass collect rebuild

createm:
	python manage.py makemigrations
migrate:
	python manage.py migrate