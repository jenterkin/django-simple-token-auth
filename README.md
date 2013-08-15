django-simple-token-auth
========================

Simple token authentication for API-based back-ends.

Installation
============

- Clone project
- Create a symbolic link from the tokenauth app to your apps for the Django project you want to include it in.
* ```ln -s /path/to/tokenauth /path/to/your/project/apps```
- ```source``` into virtualenv
- Go to directory with requirements.txt
- Run ```pip install -r /path/to/requirements.txt```
- Add ```tokenauth``` to INSTALLED_APPS in your ```settings.py```
- Add ```tokenauth.middleware.TokenAuth``` to MIDDLEWARE_CLASSES in your ```settings.py``` 

Usage
=====

All that is required is for you to send an AUTHENTICATE header with the value being the token.
Using [HTTPIe](https://github.com/jkbr/httpie) the process would go like:

```http -f POST http://location.com:PORT/login/ username={a username} password={a password}```

This will return a token. Save this and pass it in with the AUTHENTICATE header.

```http http://location.com:PORT/test/ "AUTHENTICATE:{token}"```
