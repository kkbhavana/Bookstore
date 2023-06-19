from django.contrib import admin
from .models import Book, Profile, Cart, CartItem

# Register your models here.
admin.site.register(Book),
admin.site.register(Profile),
admin.site.register(Cart),
admin.site.register(CartItem),