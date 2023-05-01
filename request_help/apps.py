from django.apps import AppConfig


class RequestHelpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'request_help'

    def ready(self):
        import request_help.signals


