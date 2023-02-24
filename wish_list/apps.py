from django.apps import AppConfig


class NotesConfig(AppConfig):
    name = 'wish_list'

    def ready(self):
        from . import signals
