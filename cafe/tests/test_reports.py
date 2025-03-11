from django.test import TestCase
from django.urls import reverse

from cafe.models import Order, Dish


class RevenueViewTest(TestCase):
    def setUp(self):
        """Создаем тестовые заказы"""
        self.dish1 = Dish.objects.create(name="Суп", price=500)
        self.dish2 = Dish.objects.create(name="Салат", price=250)

        self.order1 = Order.objects.create(table_number=1, status="paid")
        self.order1.items.set([self.dish1])

        self.order2 = Order.objects.create(table_number=2, status="paid")
        self.order2.items.set([self.dish2])

    def test_revenue_view_status_code(self):
        """Проверяем, что страница загружается успешно"""
        response = self.client.get(reverse("revenue"))
        self.assertEqual(response.status_code, 200)

    def test_revenue_calculation(self):
        """Проверяем, что общая выручка считается правильно"""
        response = self.client.get(reverse("revenue"))
        self.assertEqual(response.context["total_revenue"], 750)

    def test_revenue_view_filters_paid_orders(self):
        """Проверяем, что в контексте отображаются только оплаченные заказы"""
        response = self.client.get(reverse("revenue"))
        orders = response.context["orders"]
        self.assertEqual(len(orders), 2)
        for order in orders:
            self.assertEqual(order.status, "paid")
