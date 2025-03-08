from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Dish(models.Model):
    """
    Модель для представления блюда в кафе.

    Атрибуты:
        name (CharField): Название блюда.
        price (DecimalField): Цена блюда.
    """
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена блюда"
    )

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Order(models.Model):
    """
    Модель для представления заказа в кафе.

    Атрибуты:
        STATUS_CHOICES (list): Возможные статусы заказа.
        table_number (IntegerField): Номер стола, за которым сделан заказ.
        items (ManyToManyField): Список блюд и их цены в формате JSON.
        total_price (DecimalField): Общая стоимость заказа.
        status (CharField): Статус заказа.
    """
    STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("ready", "Готово"),
        ("paid", "Оплачено"),
    ]

    table_number = models.IntegerField(verbose_name="Номер стола")
    items = models.ManyToManyField(Dish, verbose_name="Список блюд")
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        verbose_name="Общая стоимость"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="Статус заказа"
    )

    def calculate_total_price(self):
        """
        Вычисление общей стоимости заказа.
        """
        return sum(dish.price for dish in self.items.all())

    def save(self, *args, **kwargs):
        """
        При сохранении нового заказа задаем total_price = 0,
        а для уже существующего пересчитываем его.
        """
        if not self.pk:
            self.total_price = 0
        else:
            self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} -> Стол {self.table_number} - {self.status}"


@receiver(m2m_changed, sender=Order.items.through)
def update_order_total_price(sender, instance, action, **kwargs):
    """
    Сигнал для обновления общей стоимости заказа при изменении списка блюд.
    """
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.total_price = instance.calculate_total_price()
        instance.save(update_fields=["total_price"])
