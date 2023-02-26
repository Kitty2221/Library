from rest_framework import serializers

from api.user_api.serializer import BookSerializer
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['surname', 'name', 'patronymic', 'books']
