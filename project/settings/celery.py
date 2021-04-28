# from datetime import timedelta


CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

BROKER_URL = 'redis://redis/14'
CELERY_BROKER_URL = 'redis://redis/14'
CELERY_RESULT_BACKEND = 'redis://redis/15'

CELERYBEAT_SCHEDULE = {
    # 'test_task': {
    #     'task': 'test_task',
    #     'schedule': timedelta(seconds=3),
    # },
}
