# django
import os
from celery import Celery

# env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('text_to_sql')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
