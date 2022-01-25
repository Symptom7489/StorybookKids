from django.apps import AppConfig


class ChildrenBooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'children_books'

    def ready(self):
        import children_books.api.signals

default_app_config = "ChildrenBooksConfig"