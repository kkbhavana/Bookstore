from django.urls import path

from .views import BookList, BookDetailView

urlpatterns = [
    path('booklist/', BookList.as_view(), name='book'),
    path('details/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]
