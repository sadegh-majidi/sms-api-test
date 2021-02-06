import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmsApi.settings')
app = Celery('SmsApi', broker='amqp://localhost')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
