from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver

class Token(models.Model):
    token = models.CharField(max_length=36, unique=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.user)

    def renew(self):
        self.token = str(uuid4())

@receiver(post_save, sender=User)
def create_initial_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.renew()
        while token.token in [x.token for x in Token.objects.all()]:
            token.renew()
        token.save()
