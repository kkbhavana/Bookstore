from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField( null=True,blank=True)
    image_url = models.CharField(max_length=2083,blank=True)
    book_available = models.BooleanField()