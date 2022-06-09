from django.apps import AppConfig


class TopnewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topnews'

    # def ready(self):
    #     from hackernewscore import updater
    #     updater.scheduled_job()
