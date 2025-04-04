#!/bin/sh

until cd /app/CVProject
do
    echo "Waiting for server volume..."
done

poetry run celery -A CVProject.celery worker --loglevel=info
