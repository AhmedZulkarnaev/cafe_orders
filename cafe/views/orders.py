from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from cafe.models import Order
from cafe.forms import OrderForm


class OrderListView(ListView):
    """
    Представление для отображения списка заказов с фильтрацией и пагинацией.

    Атрибуты:
        model: Модель Order.
        template_name: Шаблон для отображения списка заказов.
        context_object_name: Имя переменной контекста с заказами.
        paginate_by: Количество заказов на странице.
    """
    model = Order
    template_name = "order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        """
        Переопределяет выборку заказов,
        позволяя фильтровать по GET-параметру 'q'.
        Если 'q' является числом, фильтруется также по номеру стола.
        """
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            q_filter = Q(status__icontains=query)
            if query.isdigit():
                q_filter |= Q(table_number=int(query))
            queryset = queryset.filter(q_filter)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст значение запроса
        для сохранения состояния поиска в шаблоне.
        """
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class OrderCreateView(CreateView):
    """
    Представление для создания нового заказа
    с уведомлением об успешном создании.
    """
    model = Order
    form_class = OrderForm
    template_name = "order_form.html"
    success_url = reverse_lazy("order_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        return super().form_invalid(form)


class OrderUpdateView(UpdateView):
    """
    Представление для обновления существующего заказа
    с уведомлением об успешном обновлении.
    """
    model = Order
    form_class = OrderForm
    template_name = "order_form.html"
    success_url = reverse_lazy("order_list")


class OrderDeleteView(DeleteView):
    """
    Представление для удаления заказа
    с подтверждением и уведомлением об успешном удалении.
    """
    model = Order
    template_name = "order_confirm_delete.html"
    success_url = reverse_lazy("order_list")
