# dteam-django-test

## Django CV Table Migration & Fixture Loading

### Migrate CV Table

```sh
cd CVProject
python manage.py makemigrations && python manage.py migrate
```

### Load CV Data Fixture

```sh
python manage.py loaddata CVs
```

## Django CV Testing

### Run Test for CVs

```sh
python manage.py test main
```

### Run Test for CVs API

```sh
python manage.py test api
```
