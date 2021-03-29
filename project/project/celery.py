import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = os.getenv('BROKER_URI')
app.autodiscover_tasks()


app.conf.beat_schedule = {}
