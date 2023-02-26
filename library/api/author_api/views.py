from rest_framework import generics
from api.author_api.serializer import AuthorSerializer, AuthorListSerializer
from author.models import Author


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorSerializer


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
