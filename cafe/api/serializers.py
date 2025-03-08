from rest_framework import serializers

from cafe.models import Order, Dish


class DishSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Dish."""

    class Meta:
        model = Dish
        fields = ['id', 'name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Order."""

    items = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']

    def create(self, validated_data):
        """
        Переопределяет метод create для корректного создания объекта
        с связью многие ко многим.

        После создания заказа устанавливает связь с выбранными блюдами.
        """
        item_data = validated_data.pop('items', [])
        instance = Order.objects.create(**validated_data)
        instance.items.set(item_data)
        return instance
