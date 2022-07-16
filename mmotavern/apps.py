from django.apps import AppConfig


class MmoTavernConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mmotavern'

    def ready(self):
        import mmotavern.signals
