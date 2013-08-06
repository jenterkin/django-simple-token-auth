from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Token(models.Model):
    token = models.CharField(max_length=36, unique=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.user)

    def renew(self):
        self.token = str(uuid4())
