from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView

from .models import Book, Order, Profile, Cart, CartItem


# Create your views here.
def home(request):
    return render(request, 'home.html')


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title=query) | Q(author=query)
        )


class BookList(ListView):
    model = Book
    context_object_name = 'book'
    template_name = 'list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'bookdetail.html'


class BookCheckoutView(DetailView):
    model = Book
    template_name = 'checkout.html'


def PaymentComplete(request, pk):
    product = Book.objects.get(id=pk)
    Order.objects.create(
        product=product

    )
    return JsonResponse('Transaction Completed...', safe=False)


@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItem.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []

        context = {
            'cart': cart_obj,
            'cart_items': cart_items

        }
        return render(request, 'mycart.html', context)


class ProfileView(CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile.html'
