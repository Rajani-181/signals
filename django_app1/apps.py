from django.apps import AppConfig


class DjangoApp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_app1'

    # def ready(self):
    #     import django_app1.signals

    # def custom(self):
    #     import django_app1.customSignals
