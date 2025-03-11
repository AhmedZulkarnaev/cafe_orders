from django.test import TestCase

from cafe.models import Order, Dish


class OrderModelTest(TestCase):
    def setUp(self):
        self.dish1 = Dish.objects.create(name="Суп", price=500)
        self.dish2 = Dish.objects.create(name="Салат", price=350)
        self.order = Order.objects.create(table_number=1)

    def test_calculate_total_price(self):
        """Проверяем, что стоимость заказа корректно рассчитывается."""
        self.order.items.add(self.dish1, self.dish2)
        self.assertEqual(self.order.calculate_total_price(), 850)

    def test_status_default(self):
        """Проверяем, что статус по умолчанию — 'pending'."""
        self.assertEqual(self.order.status, "pending")

    def test_total_price_updates_on_dish_add(self):
        """Проверяем, что при добавлении блюда пересчитывается цена."""
        self.order.items.add(self.dish1)
        self.order.refresh_from_db()
        self.assertEqual(self.order.total_price, 500)

        self.order.items.add(self.dish2)
        self.order.refresh_from_db()
        self.assertEqual(self.order.total_price, 850)

    def test_total_price_updates_on_dish_remove(self):
        """Проверяем, что при удалении блюда пересчитывается цена."""
        self.order.items.add(self.dish1, self.dish2)
        self.order.items.remove(self.dish1)
        self.order.refresh_from_db()
        self.assertEqual(self.order.total_price, 350)
