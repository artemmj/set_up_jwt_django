from __future__ import absolute_import, unicode_literals
import os

from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.common')

app = Celery('config')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
