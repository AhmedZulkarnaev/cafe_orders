from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
