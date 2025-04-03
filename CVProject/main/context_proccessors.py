from django.conf import settings
from django.http import HttpRequest


def settings_context(request: HttpRequest):
    return {
        "DEBUG": settings.DEBUG,
        "ALLOWED_HOST": settings.ALLOWED_HOSTS,
        "DATABASES": settings.DATABASES
    }
