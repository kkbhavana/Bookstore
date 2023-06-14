from django.urls import path

from . import views
from .views import BookList, BookDetailView, BookCheckoutView, PaymentComplete, SearchResultsView, ProfileView, cart, \
    add_to_cart

urlpatterns = [
    path('', BookList.as_view(), name='book'),
    path('home/',views.home,name='home'),
    path('search/',SearchResultsView.as_view(),name='search-results'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('booklist/', BookList.as_view(), name='book'),
    path('bookdetails/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('checkout/<int:pk>', BookCheckoutView.as_view(), name='checkout'),
    path('complete/', PaymentComplete, name='complete'),
    path('cart/',cart,name='mycart'),
    path('cart/add/<int:book_id>/',add_to_cart,name='add_to_cart')


]
