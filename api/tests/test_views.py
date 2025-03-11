from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cafe.models import Order, Dish


class OrderViewSetTest(APITestCase):
    def setUp(self):
        """Создаем тестовые данные."""
        self.dish1 = Dish.objects.create(name="Пицца", price=10.00)
        self.dish2 = Dish.objects.create(name="Суп", price=5.00)

        self.order = Order.objects.create(table_number=1, status="pending")
        self.order.items.set([self.dish1, self.dish2])

        self.url_list = reverse("order-list")
        self.url_detail = reverse("order-detail", args=[self.order.id])

    def test_create_order(self):
        """Тест создания заказа через API."""
        data = {
            "table_number": 2,
            "status": "pending",
            "items": [self.dish1.id, self.dish2.id]
        }
        response = self.client.post(self.url_list, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(response.data["table_number"], 2)

    def test_get_orders(self):
        """Тест получения списка заказов."""
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_order(self):
        """Тест обновления заказа."""
        data = {
            "table_number": self.order.table_number,
            "status": "paid",
            "items": [self.dish1.id]
        }
        response = self.client.put(self.url_detail, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "paid")

    def test_partial_update_order(self):
        """Тест частичного обновления заказа (PATCH)."""
        data = {
            "table_number": self.order.table_number,
            "status": "paid",
            "items": [self.dish1.id],
        }
        response = self.client.patch(self.url_detail, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "paid")

    def test_delete_order(self):
        """Тест удаления заказа."""
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())
