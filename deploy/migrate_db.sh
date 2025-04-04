#!/bin/sh

poetry run python /app/CVProject/manage.py makemigrations

poetry run python /app/CVProject/manage.py migrate

poetry run python /app/CVProject/manage.py loaddata CVs
