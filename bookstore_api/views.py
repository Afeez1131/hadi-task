from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .models import Book, Order
from . import serializers, permissions
from .viewsets import CustomModelViewSets


class BookViewSet(CustomModelViewSets):
    """
    This ViewSet provides CRUD operations for managing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializers
    search_fields = ['title', 'author', 'genre']
    ordering_fields = ['id', 'publication_date']


class UserViewSet(CustomModelViewSets):
    """
    This ViewSet provides CRUD operations for managing user instances.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    search_fields = ['username', 'email']
    ordering_fields = ['id']


class OrderViewSet(CustomModelViewSets):
    """
    This ViewSet provides CRUD operations for managing order instances.
    """
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializers
    search_fields = ['book__title', 'user__username', 'user__email', 'book__genre']
    ordering_fields = ['id', 'created']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.IsOrderOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
