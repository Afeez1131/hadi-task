from rest_framework import viewsets, filters

from bookstore_api import pagination


class CustomModelViewSets(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    pagination_class = pagination.CustomPagination
