from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validuser(self, user):
        errors = []

        if len(user) < 8:
            errors.append("Too low")

        if len(user) > 26:
            errors.append("Too high")
        
        if not errors:
            user = User.objects.create(user=user)
            return {"status": True, "data": user}
        else:
            return {"status": False, "data": errors}
class User(models.Model):
    user = models.CharField(max_length=26)
    createdAt = models.DateTimeField(auto_now_add=True)
        
    objects = UserManager()