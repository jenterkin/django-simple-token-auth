from tokenauth.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.get(user=user).token
        data = {'message': '', 'token': token}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=200)
    else:
        data = {'message': 'Incorrect login'}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=403)

@csrf_exempt
def logout(request):
    logout(request)
    return HttpResponse(status=200)
