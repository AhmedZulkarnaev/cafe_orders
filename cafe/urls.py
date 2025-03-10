from django.urls import path

from cafe.views.orders import (
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
)
from cafe.views.reports import RevenueView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path("revenue/", RevenueView.as_view(), name="revenue"),
]
