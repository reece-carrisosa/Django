from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publishedDate = models.DateField(auto_now=True)
    category = models.CharField(max_length=100)
    inPrint = models.BooleanField()