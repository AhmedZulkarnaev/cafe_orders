from django.contrib import admin

from .models import Dish, Order


class OrderAdmin(admin.ModelAdmin):
    """
    Административная модель для управления заказами в админке Django.

    Атрибуты:
        list_display (tuple): Поля, отображаемые в списке объектов.
        list_filter (tuple): Поля, по которым можно фильтровать
        список объектов.
        search_fields (tuple): Поля, по которым можно выполнять поиск.
        readonly_fields (tuple): Поля, которые доступны только для чтения.
    """
    list_display = ('id', 'table_number', 'total_price', 'status',)
    list_filter = ('status',)
    search_fields = ('table_number', 'status')
    readonly_fields = ('total_price',)


class DishAdmin(admin.ModelAdmin):
    """
    Административная модель для управления блюдами в админке Django.

    Атрибуты:
        list_display (tuple): Поля, отображаемые в списке объектов.
        search_fields (tuple): Поля, по которым можно выполнять поиск.
    """
    list_display = ('name', 'price')
    search_fields = ('name',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Dish, DishAdmin)
