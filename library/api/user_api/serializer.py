from rest_framework import serializers
from authentication.models import CustomUser
from book.models import Book
from order.models import Order


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'updated_at', 'created_at',
                  'role', 'is_active']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserOrdersListSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['book', 'created_at', 'end_at', 'plated_end_at']


class OrderSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
