from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book


# Create your views here.

class BookList(ListView):
    model = Book
    context_object_name = 'book'
    template_name = 'list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'bookdetail.html'

# class BookCheckoutView(DetailView):
