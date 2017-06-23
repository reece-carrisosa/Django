from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)