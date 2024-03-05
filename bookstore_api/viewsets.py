from rest_framework import viewsets


class CustomModelViewSets(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
