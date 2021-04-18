from celery import chain
from celery.task import periodic_task
from celery.schedules import crontab

from mercedes.celery import app
from .brand import update_brands
from .model import update_models
from .generation import update_generations
from .modification import update_modifications

@app.task
def update_db(user_id=None):
    update_brands(user_id)
    update_models(user_id)
    update_generations(user_id)
    update_modifications(user_id)

@periodic_task(run_every=crontab(minute=0, hour=10, day_of_week=1))
def update_db_periodic():
    update_db.delay()
