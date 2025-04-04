import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CVProject.settings')

# import django
# django.setup()

celery_app = Celery('CVProject')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
