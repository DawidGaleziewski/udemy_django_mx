from django.apps import AppConfig


class AbstractedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstracted'
