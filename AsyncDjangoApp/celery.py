from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncDjangoApp.settings')

app = Celery('AsyncDjangoApp')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)
