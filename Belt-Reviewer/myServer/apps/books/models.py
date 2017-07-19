from __future__ import unicode_literals
from django.db import models
from ..login.models import *

# Create your models here:
class Book(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, related_name="user_reviews")
    book= models.ForeignKey(Book, related_name="book_reviews")
