from django.apps import AppConfig


class SeatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.seats'

    def ready(self):
        import apps.seats.signals