import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')

app.config_from_object('django.conf:settings', namespace='CELERY_CONF')
app.conf.task_serializer = 'json'

app.autodiscover_tasks()
