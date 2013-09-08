from tokenauth.models import Token
from django.contrib.auth import (
        authenticate, 
        login as auth_login,
        logout as auth_logout,
    )
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

@csrf_exempt
@require_http_methods(['POST'])
def login(request):

    '''
    Gets username and password and authenticates user.
    If user is authenticated, the associated token is passed back.
    If the user is not authenticated, a 403 and a message of 
    incorrect login is returned
    '''

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.get(user=user).token
        data = {'message': '', 'token': token, 'id':user.pk}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=200)
    else:
        data = {'message': 'Incorrect login'}
        data = simplejson.dumps(data)
        return HttpResponse(data, status=403)

@csrf_exempt
@require_http_methods(['GET'])
def logout(request):
    auth_logout(request)
    return HttpResponse(status=200)

@require_http_methods(['GET'])
def test(request):
    
    '''
    Simple view to test authentication.
    '''

    data = {'user': request.user.username}
    data = simplejson.dumps(data)
    return HttpResponse(data, status=200)
