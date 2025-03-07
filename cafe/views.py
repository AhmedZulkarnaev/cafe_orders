from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import QuerySet, Q
from typing import Optional

from .models import Order
from .forms import OrderForm


class OrderListView(ListView):
    """
    Представление для отображения списка заказов.

    Атрибуты:
        model: Модель, используемая для представления.
        template_name: Имя шаблона для отображения.
        context_object_name: Имя переменной контекста для списка объектов.
    """
    model: Order
    template_name: str = "order_list.html"
    context_object_name: str = "orders"

    def get_queryset(self) -> QuerySet[Order]:
        """
        Переопределение метода для фильтрации заказов.

        Этот метод фильтрует заказы на основе параметра переданного в запросе.
        Если 'q' содержит текстовый запрос,
        он фильтрует заказы по статусу или номеру стола.
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
    model: Order
    form_class: OrderForm
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
    model: Order
    form_class: OrderForm
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
    model: Order
    template_name: str = "order_confirm_delete.html"
    success_url: str = reverse_lazy("order_list")
