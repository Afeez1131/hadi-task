from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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
        return super().create(validated_data)


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book', 'user', 'quantity', 'order_date']
        read_only_fields = ['id']



