from rest_framework.generics import ListCreateAPIView

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListCreate(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
