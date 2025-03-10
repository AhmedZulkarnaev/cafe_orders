from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin  # При необходимости для защиты доступа

from cafe.models import Order
from cafe.forms import OrderForm


class OrderListView(LoginRequiredMixin, ListView):
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
    paginate_by = 20

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


class OrderCreateView(LoginRequiredMixin, CreateView):
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
        messages.success(self.request, "Заказ успешно создан.")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Ошибка при создании заказа. Проверьте данные формы."
        )
        return super().form_invalid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для обновления существующего заказа
    с уведомлением об успешном обновлении.
    """
    model = Order
    form_class = OrderForm
    template_name = "order_form.html"
    success_url = reverse_lazy("order_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Заказ успешно обновлён.")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Ошибка при обновлении заказа. Проверьте данные формы."
        )
        return super().form_invalid(form)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления заказа
    с подтверждением и уведомлением об успешном удалении.
    """
    model = Order
    template_name = "order_confirm_delete.html"
    success_url = reverse_lazy("order_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Заказ успешно удалён.")
        return super().delete(request, *args, **kwargs)
