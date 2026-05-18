from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BookListAPIView.as_view(), name="api_book_list"),
    path("books/<int:pk>/", views.BookDetailAPIView.as_view(), name="api_book_detail"),
]