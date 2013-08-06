from django.db import models
from uuid import uuid4

class Token(models.Model):
    token = models.CharField(max_length=36)
    user = models.ForeignKey(User)

    def __init__(self):
        self.token = str(uuid4())

    def __unicode__(self):
        return unicode(user)

    def renew(self):
        self.token = str(uuid4())
