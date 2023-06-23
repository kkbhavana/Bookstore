from django.urls import path

from . import views
from .views import BookList, BookDetailView, BookCheckoutView, PaymentComplete, SearchResultsView, cart, \
    add_to_cart, remove_from_cart, ProfileView, ProfileCreate, ProfileUpdate

urlpatterns = [
    path('', BookList.as_view(), name='book'),
    path('home/', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('booklist/', BookList.as_view(), name='book'),
    path('bookdetails/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(), name='checkout'),
    path('complete/', PaymentComplete, name='complete'),
    path('cart/', cart, name='mycart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('myprofile/', ProfileView.as_view(), name='profile'),
    path('create/', ProfileCreate.as_view(), name='create-profile'),
    path('update/<int:pk>/', ProfileUpdate.as_view(), name='update-profile')

]
