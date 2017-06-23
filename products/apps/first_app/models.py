from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=100)
    productDescription = models.TextField(max_length=1000)
    productWeight = models.CharField(max_length=100)
    productPrice = models.CharField(max_length=100)
    productCost = models.CharField(max_length=100)
    productCategory = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)