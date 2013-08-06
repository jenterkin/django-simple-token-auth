from tokenauth.models import Token
from django.contrib.auth import authenticate, login

class TokenAuth(object):
    def process_request(self, request):
        try:
            # Gets token from AUTHENTICATE header
            # All headers are stored in request.META, which is a dict.
            # To access a header, reference the header-name with 'HTTP_' at the beginning
            # followed by the header's name, all uppercase, and all hyphense replaced by
            # underscores.
            token = request.META['HTTP_AUTHENTICATE']
        except KeyError:
            # If no AUTHENTICATE header, do nothing.
            pass
        else:
            # If header is found, get user by associated token and log them in.
            user = Token.objects.get(token=token).user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
