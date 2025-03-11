from django.test import TestCase
from django.urls import reverse

from cafe.models import Order, Dish


class OrderViewsTest(TestCase):
    def setUp(self):
        self.dish1 = Dish.objects.create(name="Суп", price=500)
        self.order1 = Order.objects.create(table_number=1, status="pending")
        self.order2 = Order.objects.create(table_number=2, status="ready")

    def test_order_list_view(self):
        """Тестируем вывод списка заказов."""
        response = self.client.get(reverse("order_list"))

        self.assertEqual(response.status_code, 200)

    def test_order_filtering(self):
        """Фильтрация по статусу."""
        response = self.client.get(reverse("order_list") + "?q=ready")

        self.assertContains(response, "Готово")
        self.assertNotContains(response, "В ожидании")

    def test_order_create_view(self):
        """Тестируем создание заказа."""
        response = self.client.post(reverse("order_create"), {
            "table_number": 3,
            "status": "pending",
            "items": [self.dish1.id]
        }, follow=True)

        self.assertEqual(Order.objects.count(), 3)

    def test_order_update_view(self):
        """Тестируем изменение заказа."""
        response = self.client.post(reverse("order_update", args=[self.order1.id]), {
            "table_number": self.order1.table_number,
            "status": "paid",
            "items": [self.dish1.id]
        }, follow=True)

        self.order1.refresh_from_db()
        self.assertEqual(self.order1.status, "paid")



    def test_order_delete_view(self):
        """Тестируем удаление заказа."""
        response = self.client.post(reverse("order_delete", args=[self.order1.id]))
        self.assertEqual(Order.objects.count(), 1)
