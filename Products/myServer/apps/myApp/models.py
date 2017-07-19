from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

# Create your models here:
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length= 1000)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
