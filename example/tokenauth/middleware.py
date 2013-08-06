from tokenauth.models import Token
class TokenAuth(object):
    def process_request(self, request):
        try:
            token = request.META['HTTP_AUTHENTICATE']
        except KeyError:
            pass
        else:
            user = Token.objects.get(token=token).user
            login(request, user)
