from django.contrib.auth.models import User

from .models import Book, Order
from . import serializers
from .viewsets import CustomModelViewSets
from rest_framework.authtoken.models import Token


class BookViewSet(CustomModelViewSets):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializers


class UserViewSet(CustomModelViewSets):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers


class OrderViewSet(CustomModelViewSets):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializers

