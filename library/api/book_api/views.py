from rest_framework import generics
from api.book_api.serializer import BookSerializer, BookListSerializer
from book.models import Book


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
