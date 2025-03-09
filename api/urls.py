from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import OrderViewSet, DishViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'dishes', DishViewSet, basename='dish')

urlpatterns = [
    path('', include(router.urls)),
]
