from rest_framework import serializers
from book.models import Book
from api.author_api.serializer import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'count', 'authors']

