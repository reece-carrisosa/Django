from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Message(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)




class Comment(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
    comment = models.TextField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

