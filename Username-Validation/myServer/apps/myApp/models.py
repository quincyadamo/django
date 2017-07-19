from __future__ import unicode_literals
from django.db import models

# Create your models here:
class UsernameManager(models.Manager):
    def validate(self, username):
        if len(username) > 8 and len(username) < 26:
            return True
        else:
            return False
class Username(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsernameManager()
