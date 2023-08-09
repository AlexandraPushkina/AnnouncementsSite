#что из себя представляет приложение
from django.apps import AppConfig


class BboardConfig(AppConfig):  #оно представляет класс
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bboard'
