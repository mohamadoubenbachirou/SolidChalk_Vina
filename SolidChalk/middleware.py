# middleware.py

from django.utils.translation import activate
from django.conf import settings

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.GET.get('lang')  # Suppose que la langue est passée dans le paramètre GET 'lang'

        if language and language in dict(settings.LANGUAGES):
            request.session[settings.LANGUAGE_SESSION_KEY] = language
            activate(language)

        response = self.get_response(request)
        return response
