from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BookListCreate.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookRetrieve.as_view(), name="book-detail"),
    path("authors/", views.AuthorListCreate.as_view(), name="author-list"),
    path("authors/<int:pk>/", views.AuthorRetrieve.as_view(), name="author-detail"),
]
