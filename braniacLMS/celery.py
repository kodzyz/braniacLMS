import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "braniacLMS.settings")
celery_app = Celery("braniac")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


# celery -A braniacLMS worker -l INFO
#celery -A braniacLMS worker -l INFO -P eventlet