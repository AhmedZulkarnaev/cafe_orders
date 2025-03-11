from rest_framework import serializers
from cafe.models import Order, Dish


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Order."""
    items = serializers.PrimaryKeyRelatedField(
        queryset=Dish.objects.all(), many=True
    )

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']
        read_only_fields = ['total_price']

    def validate(self, attrs):
        """Проверяет валидность данных заказа."""
        table_number = attrs.get('table_number')
        if table_number is not None and table_number <= 0:
            raise serializers.ValidationError(
                {"table_number": "Номер стола должен быть положительным."}
            )
        if not attrs.get('items'):
            raise serializers.ValidationError(
                {"items": "Список блюд не может быть пустым."}
            )
        return attrs

    def create(self, validated_data):
        """Создаёт объект Order с привязкой к блюдам."""
        item_data = validated_data.pop('items', [])
        instance = Order.objects.create(**validated_data)
        instance.items.set(item_data)
        return instance
