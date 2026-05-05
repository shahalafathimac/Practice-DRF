from django.apps import AppConfig


class Home5Config(AppConfig):
    name = 'home5'

    def ready(self):
        import home5.signals