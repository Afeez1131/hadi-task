from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

from .models import Order, Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        read_only_fields = ['id']
        fields = ['id', 'title', 'author', 'publication_date', 'isbn', 'genre', 'price']


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=155, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        """we need turn the plain text password into hashed password, else password won't be usable."""
        validated_data['password'] = make_password(validated_data.get('password'))
        user = super().create(validated_data)
        Token.objects.get_or_create(user=user)  # create authentication token
        return user


class OrderSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Order
        fields = ['id', 'book', 'book_title', 'quantity', 'created', 'user']
        read_only_fields = ['id']
