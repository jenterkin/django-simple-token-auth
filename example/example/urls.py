from django.conf.urls import patterns, include, url
from tokenauth.views import login, logout, test

urlpatterns = patterns('',
    url(r'^', include('tokenauth.urls')),
)
