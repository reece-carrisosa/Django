from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class UserManager(models.Manager):
#     def registration(self, postData):


class InterestManager(models.Manager):
    def makeUser(self, post):
        interest = Post['interest']
        try:
            interest = User.objects.get(interest=interest)
        except:
            interest = User.objects.create(interest=interest)


class Interest(models.Model):
    name = models.CharField(max_length=24)

class UserManager(models.Manager):
    def makeUser(self, post):
        name = POST['name']

        try:
            user = User.objects.get(name=name)
        except:
            user = User.objects.create(name=name)
        return user






class User(models.Model):
    name = models.CharField(max_length=24)
    interest = models.ManyToManyField(Interest)
