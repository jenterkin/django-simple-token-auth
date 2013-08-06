from tokenauth.models import Token
from django.contrib.auth import authenticate, login

class TokenAuth(object):
    def process_request(self, request):
        try:
            token = request.META['HTTP_AUTHENTICATE']
        except KeyError:
            pass
        else:
            user = Token.objects.get(token=token).user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
