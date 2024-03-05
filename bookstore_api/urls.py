from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as auth_view


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderViewSet)


urlpatterns = [
    path('token-auth', auth_view.obtain_auth_token),
    path('', include(router.urls)),
]
