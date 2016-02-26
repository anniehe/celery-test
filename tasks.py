from celery import Celery

### Celery ###

# Celery is an asynchronous task queue with real-time processing and task scheduling.
# Celery communicates with Celery workers through Redis, the message broker.
# Celery workers will fetch the task from the message queue and execute the task.

# Instantiate a Celery object to run with Flask.
celery = Celery()
celery.config_from_object('celeryconfig')


@celery.task()
def say_hello():
    print "Hello, world!"
