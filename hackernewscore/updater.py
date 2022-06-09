from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from topnews.cron import cron_job


def scheduled_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(cron_job, 'interval', minutes=5)
    scheduler.start()