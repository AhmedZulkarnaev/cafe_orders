from typing import Optional, Type
from django.db.models import Q, QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cafe.models import Order
from cafe.forms import OrderForm


class OrderListView(ListView):
    """
    Представление для отображения списка заказов.

    Атрибуты:
        model: Модель, используемая для представления.
        template_name: Имя шаблона для отображения.
        context_object_name: Имя переменной контекста для списка объектов.
    """
    model: Type[Order] = Order
    template_name: str = "order_list.html"
    context_object_name: str = "orders"

    def get_queryset(self) -> QuerySet[Order]:
        """
        Переопределение метода для фильтрации заказов.

        Фильтрует заказы на основе параметра 'q', переданного в запросе.
        Если 'q' содержит текстовый запрос, фильтрует заказы по статусу или номеру стола.

        Returns:
            QuerySet[Order]: Отфильтрованный набор заказов.
        """
        queryset: QuerySet[Order] = super().get_queryset()
        query: Optional[str] = self.request.GET.get('q')
        if query:
            q_filter = Q(status__icontains=query)
            if query.isdigit():
                q_filter |= Q(table_number=int(query))
            queryset = queryset.filter(q_filter)
        return queryset


class OrderCreateView(CreateView):
    """
    Представление для создания нового заказа.

    Атрибуты:
        model: Модель, используемая для представления.
        form_class: Форма, используемая для создания объекта.
        template_name: Имя шаблона для отображения.
        success_url: URL для перенаправления после успешного создания.
    """
    model: Type[Order] = Order
    form_class: Type[OrderForm] = OrderForm
    template_name: str = "order_form.html"
    success_url: str = reverse_lazy("order_list")


class OrderUpdateView(UpdateView):
    """
    Представление для обновления существующего заказа.

    Атрибуты:
        model: Модель, используемая для представления.
        form_class: Форма, используемая для обновления объекта.
        template_name: Имя шаблона для отображения.
        success_url: URL для перенаправления после успешного обновления.
    """
    model: Type[Order] = Order
    form_class: Type[OrderForm] = OrderForm
    template_name: str = "order_form.html"
    success_url: str = reverse_lazy("order_list")


class OrderDeleteView(DeleteView):
    """
    Представление для удаления существующего заказа.

    Атрибуты:
        model: Модель, используемая для представления.
        template_name: Имя шаблона для отображения.
        success_url: URL для перенаправления после успешного удаления.
    """
    model: Type[Order] = Order
    template_name: str = "order_confirm_delete.html"
    success_url: str = reverse_lazy("order_list")
