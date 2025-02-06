from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BookListCreate.as_view(), name="book-list"),
    path("authors/", views.AuthorListCreate.as_view(), name="author-list"),
]
