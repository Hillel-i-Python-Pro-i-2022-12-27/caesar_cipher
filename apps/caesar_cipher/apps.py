from django.apps import AppConfig


class CaesarCipherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.caesar_cipher"

    def ready(self):
        from . import signals  # noqa: F401
