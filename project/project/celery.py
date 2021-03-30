import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_routes = {
    '*': {'queue': 'celery'},
}

app.conf.broker_url = os.getenv('BROKER_URI')
app.autodiscover_tasks(settings.INSTALLED_APPS)
app.conf.beat_schedule = {}
