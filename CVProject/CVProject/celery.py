import os
from celery import Celery

from utils.config import generate_redis_connection_url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CVProject.settings')

# import django
# django.setup()

celery_app = Celery('CVProject', 
    broker=generate_redis_connection_url(),
    backend=generate_redis_connection_url()
)
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
