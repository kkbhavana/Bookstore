from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=100 ,default='')
    price = models.FloatField( null=True,blank=True)
    image_url = models.CharField(max_length=2083,blank=True)
    book_available = models.BooleanField()


class Order(models.Model):
    product = models.ForeignKey(Book,max_length=200,null=True,on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)


class CartItem(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.book}'

    @property
    def total_price(self):
        return self.book.price * self.quantity

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.TextField(max_length=200)
    alternative_address=models.TextField(max_length=200,default='')

    def __str__(self):
        return self.first_name
