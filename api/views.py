from rest_framework import viewsets
from cafe.models import Order, Dish

from api.serializers import OrderSerializer, DishSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """API ViewSet для модели Order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DishViewSet(viewsets.ModelViewSet):
    """API ViewSet для модели Dish."""
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
